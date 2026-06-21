#!/usr/bin/env python3
"""
Analisador de Discovery de Repositório (Code Discovery Toolkit)

Este script faz uma varredura SOMENTE LEITURA em um repositório de código
para levantar CANDIDATOS a investigação: arquivos duplicados, arquivos sem
atividade recente no histórico do Git e arquivos que aparentam não ser
referenciados em nenhum outro lugar do código.

IMPORTANTE:
- Este script NÃO modifica, move, renomeia ou apaga nenhum arquivo.
- Os resultados são HEURÍSTICAS para apoiar uma investigação humana,
  nunca uma conclusão definitiva de "isso é código morto" ou
  "isso pode ser apagado".
- Sempre valide os achados com o time antes de tomar qualquer decisão.

Uso:
    python analisar_repositorio.py /caminho/do/repositorio --saida relatorio.md
"""

import argparse
import hashlib
import os
import subprocess
import sys
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
    Heurística simples: verifica se o NOME do arquivo (sem extensão) é
    mencionado em algum outro arquivo de texto do repositório. Isso é
    apenas um indício, não uma prova de que o arquivo não é usado em
    nenhum lugar (pode haver chamadas dinâmicas, configs externas, etc).
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
            continue  # nomes muito curtos geram falsos positivos
        referenciado = any(
            nome_base in conteudo
            for outro, conteudo in conteudos.items()
            if outro != arquivo
        )
        if not referenciado:
            suspeitos.append(arquivo)
    return suspeitos


def gerar_relatorio(raiz, duplicados, parados, suspeitos, dias_limite):
    linhas = [
        f"# Relatório de Discovery — {raiz.name}",
        "",
        f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}",
        "",
        "> Este relatório contém CANDIDATOS a investigação, baseados em "
        "heurísticas automáticas. Nenhuma ação foi executada. "
        "Valide cada item com o time antes de decidir qualquer coisa.",
        "",
        "## 1. Arquivos duplicados (conteúdo idêntico)",
    ]

    if duplicados:
        for lista in duplicados.values():
            linhas.append("")
            for arquivo in lista:
                linhas.append(f"- `{arquivo.relative_to(raiz)}`")
    else:
        linhas.append("\nNenhum arquivo com conteúdo idêntico encontrado.")

    linhas.append("")
    linhas.append(f"## 2. Arquivos sem commits há mais de {dias_limite} dias")
    if parados:
        for arquivo, data in sorted(parados, key=lambda x: x[1]):
            linhas.append(
                f"- `{arquivo.relative_to(raiz)}` — último commit em {data.strftime('%d/%m/%Y')}"
            )
    else:
        linhas.append("\nNenhum arquivo parado encontrado (ou repositório sem histórico Git).")

    linhas.append("")
    linhas.append("## 3. Arquivos possivelmente não referenciados em outro lugar")
    linhas.append("\n_Heurística textual simples — confirme manualmente antes de concluir qualquer coisa._\n")
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
    args = parser.parse_args()

    raiz = Path(args.caminho).resolve()
    if not raiz.is_dir():
        print(f"Caminho inválido: {raiz}")
        sys.exit(1)

    print(f"Analisando {raiz} ...")
    arquivos = listar_arquivos(raiz)
    print(f"{len(arquivos)} arquivos encontrados.")

    duplicados = encontrar_duplicados_exatos(arquivos)
    parados = encontrar_arquivos_parados(raiz, arquivos, args.dias)
    suspeitos = encontrar_possiveis_nao_referenciados(arquivos)

    relatorio = gerar_relatorio(raiz, duplicados, parados, suspeitos, args.dias)

    with open(args.saida, "w", encoding="utf-8") as f:
        f.write(relatorio)

    print(f"Relatório gerado em: {args.saida}")


if __name__ == "__main__":
    main()
