#!/usr/bin/env python3
"""
Analisador de Discovery de Repositório (Code Discovery Toolkit)

Este script faz uma varredura SOMENTE LEITURA em um repositório de código
para levantar CANDIDATOS a investigação: arquivos duplicados (idênticos e similares),
arquivos sem atividade recente no histórico do Git e arquivos que aparentam não ser
referenciados em nenhum outro lugar do código.

Suporta integração nativa com o Jira (Atlassian) para criação automática de tickets de débito técnico.

IMPORTANTE:
- Este script NÃO modifica, move, renomeia ou apaga nenhum arquivo do projeto.
- Os resultados são HEURÍSTICAS para apoiar uma investigação humana,
  nunca uma conclusão definitiva de "isso é código morto" ou "isso pode ser apagado".
- Sempre valide os achados com o time antes de tomar qualquer decisão.

Uso:
    python analisar_repositorio.py /caminho/do/repositorio --saida relatorio.md
    python analisar_repositorio.py /caminho --jira-url "https://empresa.atlassian.net" --jira-email "dev@empresa.com" --jira-token "TOKEN" --jira-project "DEBT"
"""

import argparse
import base64
import difflib
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

# Pastas ignoradas por padrão (não fazem parte do "código de negócio")
PASTAS_IGNORADAS = {
    ".git", "node_modules", "__pycache__", ".venv", "venv",
    "dist", "build", ".next", ".idea", ".vscode", "vendor",
}

EXTENSOES_TEXTO = {
    ".py", ".js", ".ts", ".jsx", ".tsx", ".java", ".rb", ".go", ".php",
    ".c", ".cpp", ".h", ".cs", ".rs", ".html", ".css", ".scss", ".md",
    ".json", ".yml", ".yaml", ".sql", ".sh",
}


def listar_arquivos(raiz: Path):
    arquivos = []
    for caminho_atual, pastas, nomes_arquivo in os.walk(raiz):
        pastas[:] = [p for p in pastas if p not in PASTAS_IGNORADAS]
        for nome in nomes_arquivo:
            arquivos.append(Path(caminho_atual) / nome)
    return arquivos


def calcular_hash(caminho: Path) -> str:
    hasher = hashlib.sha256()
    try:
        with open(caminho, "rb") as f:
            for bloco in iter(lambda: f.read(8192), b""):
                hasher.update(bloco)
    except (OSError, PermissionError):
        return ""
    return hasher.hexdigest()


def encontrar_duplicados_exatos(arquivos):
    por_hash = defaultdict(list)
    for arquivo in arquivos:
        if arquivo.is_file():
            h = calcular_hash(arquivo)
            if h:
                por_hash[h].append(arquivo)
    return {h: lista for h, lista in por_hash.items() if len(lista) > 1}


def encontrar_duplicados_similares(arquivos, threshold=0.9):
    """
    Compara arquivos de texto com extensões compatíveis e tamanhos semelhantes
    para encontrar similaridade parcial (> threshold), ignorando arquivos 100% idênticos.
    """
    arquivos_texto = [
        a for a in arquivos 
        if a.is_file() and a.suffix in EXTENSOES_TEXTO
    ]
    
    conteudos = {}
    for a in arquivos_texto:
        try:
            if a.stat().st_size > 250000:
                continue
            txt = a.read_text(encoding="utf-8", errors="ignore")
            if txt.strip():
                conteudos[a] = txt
        except OSError:
            pass

    duplicados_similares = []
    lista_arquivos = list(conteudos.keys())
    processados = set()

    for i in range(len(lista_arquivos)):
        file1 = lista_arquivos[i]
        content1 = conteudos[file1]
        len1 = len(content1)
        if not len1:
            continue

        for j in range(i + 1, len(lista_arquivos)):
            file2 = lista_arquivos[j]
            content2 = conteudos[file2]
            len2 = len(content2)
            if not len2:
                continue

            diff_ratio = abs(len1 - len2) / max(len1, len2)
            if diff_ratio > 0.2:
                continue

            if content1 == content2:
                continue

            matcher = difflib.SequenceMatcher(None, content1, content2)
            ratio = matcher.real_quick_ratio()
            if ratio >= threshold:
                ratio = matcher.ratio()
                if ratio >= threshold and ratio < 1.0:
                    duplicados_similares.append((file1, file2, ratio))
                    processados.add(file1)
                    processados.add(file2)

    return duplicados_similares


def data_ultimo_commit(raiz: Path, arquivo: Path):
    try:
        resultado = subprocess.run(
            ["git", "log", "-1", "--format=%ct", "--", str(arquivo)],
            cwd=raiz, capture_output=True, text=True, timeout=5,
        )
        saida = resultado.stdout.strip()
        if saida:
            return datetime.fromtimestamp(int(saida))
    except (subprocess.SubprocessError, ValueError, FileNotFoundError):
        pass
    return None


def encontrar_arquivos_parados(raiz: Path, arquivos, dias_limite: int):
    limite = datetime.now() - timedelta(days=dias_limite)
    parados = []
    for arquivo in arquivos:
        if arquivo.suffix not in EXTENSOES_TEXTO:
            continue
        data = data_ultimo_commit(raiz, arquivo)
        if data and data < limite:
            parados.append((arquivo, data))
    return parados


def encontrar_possiveis_nao_referenciados(arquivos):
    """
    Heurística de correspondência de palavras inteiras (usando limites \b no Regex)
    para verificar se o nome de um arquivo (sem a extensão) é mencionado em outro
    arquivo de texto. Mitiga falsos positivos com nomes comuns.
    """
    arquivos_codigo = [a for a in arquivos if a.suffix in EXTENSOES_TEXTO]
    conteudos = {}
    for arquivo in arquivos_codigo:
        try:
            conteudos[arquivo] = arquivo.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            conteudos[arquivo] = ""

    suspeitos = []
    for arquivo in arquivos_codigo:
        nome_base = arquivo.stem
        if len(nome_base) < 4:
            continue
        
        pattern = re.compile(r'\b' + re.escape(nome_base) + r'\b')
        referenciado = False
        
        for outro, conteudo in conteudos.items():
            if outro == arquivo:
                continue
            if pattern.search(conteudo):
                referenciado = True
                break
                
        if not referenciado:
            suspeitos.append(arquivo)
            
    return suspeitos


def enviar_para_jira(raiz_nome, relatorio_texto, jira_url, jira_email, jira_token, jira_project, issue_type="Task"):
    """
    Envia o relatório de achados diretamente para a API REST v3 do Jira (Atlassian)
    usando a biblioteca urllib nativa do Python (zero dependências externas).
    """
    if not (jira_url and jira_email and jira_token and jira_project):
        return False

    api_endpoint = f"{jira_url.rstrip('/')}/rest/api/3/issue"
    auth_str = f"{jira_email}:{jira_token}"
    b64_auth = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")

    summary = f"🔎 Discovery & Higiene de Código — {raiz_nome} ({datetime.now().strftime('%d/%m/%Y')})"
    
    # Payload no formato Atlassian Document Format (ADF) para o Jira v3
    payload = {
        "fields": {
            "project": {"key": jira_project},
            "summary": summary,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text",
                                "text": "Este ticket foi criado automaticamente pelo Code Discovery Toolkit com os achados da varredura:"
                            }
                        ]
                    },
                    {
                        "type": "codeBlock",
                        "language": "markdown",
                        "content": [{"type": "text", "text": relatorio_texto}]
                    }
                ]
            },
            "issuetype": {"name": issue_type},
            "labels": ["TechnicalDebt", "CodeDiscovery"]
        }
    }

    data_bytes = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        api_endpoint,
        data=data_bytes,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Basic {b64_auth}"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            issue_key = res_data.get("key", "N/A")
            print(f"Ticket criado com sucesso no Jira: {issue_key}")
            return True
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8", errors="ignore")
        print(f"Erro HTTP ao enviar para o Jira ({e.code}): {error_body}")
        return False
    except Exception as e:
        print(f"Erro ao conectar com o Jira: {e}")
        return False


def gerar_relatorio(raiz, duplicados, similares, parados, suspeitos, dias_limite, sim_threshold):
    linhas = [
        f"# Relatório de Discovery — {raiz.name}",
        "",
        f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}",
        "",
        "> Este relatório contém CANDIDATOS a investigação, baseados em "
        "heurísticas automáticas. Nenhuma ação foi executada. "
        "Valide cada item com o time antes de decidir qualquer coisa.",
        "",
        "## 1. Arquivos duplicados (conteúdo 100% idêntico)",
    ]

    if duplicados:
        for lista in duplicados.values():
            linhas.append("")
            for arquivo in lista:
                linhas.append(f"- `{arquivo.relative_to(raiz)}`")
    else:
        linhas.append("\nNenhum arquivo com conteúdo idêntico encontrado.")

    linhas.append("")
    linhas.append(f"## 2. Arquivos altamente similares (similaridade >= {int(sim_threshold * 100)}%)")
    linhas.append("\n_Detecção por difflib.SequenceMatcher — candidatos a redundância ou clonagem._\n")
    if similares:
        for f1, f2, ratio in similares:
            linhas.append(
                f"- `{f1.relative_to(raiz)}` <-> `{f2.relative_to(raiz)}` (similaridade: {ratio:.1%})"
            )
    else:
        linhas.append("Nenhum arquivo com alta similaridade parcial encontrado.")

    linhas.append("")
    linhas.append(f"## 3. Arquivos sem commits há mais de {dias_limite} dias")
    if parados:
        for arquivo, data in sorted(parados, key=lambda x: x[1]):
            linhas.append(
                f"- `{arquivo.relative_to(raiz)}` — último commit em {data.strftime('%d/%m/%Y')}"
            )
    else:
        linhas.append("\nNenhum arquivo parado encontrado (ou repositório sem histórico Git).")

    linhas.append("")
    linhas.append("## 4. Arquivos possivelmente não referenciados em outro lugar")
    linhas.append("\n_Heurística de palavra inteira (\\b) — confirme manualmente antes de concluir qualquer coisa._\n")
    if suspeitos:
        for arquivo in suspeitos:
            linhas.append(f"- `{arquivo.relative_to(raiz)}`")
    else:
        linhas.append("\nNenhum candidato encontrado.")

    linhas.append("")
    linhas.append("## Próximos passos sugeridos")
    linhas.append("")
    linhas.append("1. Revisar esta lista com alguém que conheça o contexto do repositório.")
    linhas.append("2. Usar os prompts da pasta `prompts/` para investigar cada item com mais profundidade.")
    linhas.append("3. Preencher o template correspondente na pasta `templates/` (01, 02 ou 03) com as conclusões.")
    linhas.append("4. Só remover, mover ou refatorar algo após autorização explícita do time responsável.")

    return "\n".join(linhas)


def main():
    parser = argparse.ArgumentParser(
        description="Varredura somente leitura para apoiar discovery de repositórios."
    )
    parser.add_argument("caminho", help="Caminho do repositório a ser analisado")
    parser.add_argument(
        "--saida", default="relatorio-discovery.md",
        help="Arquivo de saída do relatório (padrão: relatorio-discovery.md)",
    )
    parser.add_argument(
        "--dias", type=int, default=365,
        help="Dias sem commit para considerar um arquivo 'parado' (padrão: 365)",
    )
    parser.add_argument(
        "--similaridade", type=float, default=0.90,
        help="Limite de similaridade parcial (SequenceMatcher) (padrão: 0.90)",
    )
    # Parâmetros opcionais para integração com o Jira
    parser.add_argument("--jira-url", help="URL do Jira (ex: https://empresa.atlassian.net)")
    parser.add_argument("--jira-email", help="E-mail da conta do Jira")
    parser.add_argument("--jira-token", help="API Token do Jira")
    parser.add_argument("--jira-project", help="Chave do Projeto no Jira (ex: PROD, DEBT)")
    parser.add_argument("--jira-issue-type", default="Task", help="Tipo do Ticket no Jira (padrão: Task)")

    args = parser.parse_args()

    raiz = Path(args.caminho).resolve()
    if not raiz.is_dir():
        print(f"Caminho inválido: {raiz}")
        sys.exit(1)

    print(f"Analisando {raiz} ...")
    arquivos = listar_arquivos(raiz)
    print(f"{len(arquivos)} arquivos encontrados.")

    duplicados = encontrar_duplicados_exatos(arquivos)
    similares = encontrar_duplicados_similares(arquivos, args.similaridade)
    parados = encontrar_arquivos_parados(raiz, arquivos, args.dias)
    suspeitos = encontrar_possiveis_nao_referenciados(arquivos)

    relatorio = gerar_relatorio(
        raiz, duplicados, similares, parados, suspeitos, args.dias, args.similaridade
    )

    with open(args.saida, "w", encoding="utf-8") as f:
        f.write(relatorio)

    print(f"Relatório gerado em: {args.saida}")

    # Envia para o Jira caso as credenciais sejam fornecidas e existam achados
    if args.jira_url and args.jira_email and args.jira_token and args.jira_project:
        tem_achados = bool(duplicados or similares or parados or suspeitos)
        if tem_achados:
            print("Enviando relatório de achados para o Jira...")
            enviar_para_jira(
                raiz.name, relatorio, args.jira_url, args.jira_email,
                args.jira_token, args.jira_project, args.jira_issue_type
            )
        else:
            print("Nenhum achado pendente. Ignorando criação de ticket no Jira.")


if __name__ == "__main__":
    main()
