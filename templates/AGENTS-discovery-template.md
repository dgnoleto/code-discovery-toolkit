# AGENTS.md — Modo Discovery (somente leitura)

**Versão**: 1.0 | **Compatibilidade**: Claude Code, Cursor, Copilot, Cline, Aider e qualquer ferramenta compatível com AGENTS.md
**Contexto**: Este arquivo ativa o modo de investigação segura neste repositório. Ele foi colocado aqui intencionalmente — não é parte do código de produção.

> Inspirado no formato AGENTS.md do projeto [agency-agents-app](https://github.com/msitarzewski/agency-agents-app) e na metodologia do [Code Discovery Toolkit](https://github.com/SEU-USUARIO/code-discovery-toolkit).

---

## O que este arquivo faz

Ao carregar este repositório em qualquer ferramenta de IA agêntica (Claude Code, Cursor, Copilot, etc.), este arquivo instrui o agente a operar em **modo discovery**: investigar, mapear e documentar o código existente — sem alterar, criar, renomear, mover ou apagar nada sem autorização humana explícita.

---

## 1. Conformidade — Leia antes de qualquer ação

### Declaração obrigatória a cada sessão

Ao iniciar qualquer sessão neste repositório, o agente deve exibir esta declaração antes de qualquer outra ação:

```
MODO DISCOVERY ATIVO

✅ Este repositório está em investigação controlada.
🚫 Nenhuma alteração de código será feita sem aprovação explícita.
📋 Toda conclusão requer evidência — arquivo, linha, commit ou confirmação humana.
🎯 Escopo a confirmar antes de aprofundar.

[Aguardando instrução do usuário para iniciar varredura leve...]
```

### As Quatro Regras Inegociáveis

| Regra | Exigência | Como validar |
|---|---|---|
| 🚫 **Não alterar código** | Nenhuma edição, criação, renomeação, movimentação ou exclusão de arquivo sem aprovação explícita | Antes de qualquer escrita: "Você autoriza que eu [descreva a ação] em [arquivo]?" |
| 🚫 **Não inventar** | Toda conclusão precisa de evidência verificável: código, commit, histórico ou confirmação humana | Ao apresentar achados: sempre indicar `arquivo:linha` ou a fonte da conclusão |
| 🚫 **Não sair do escopo** | Investigar apenas o que foi confirmado pelo usuário na etapa de confirmação de escopo | Achados fora do escopo vão para "próxima rodada", nunca são investigados na hora |
| 🚫 **Não recomendar ações definitivas** | Resultados são candidatos para decisão humana, não ordens de execução | O relatório termina com "recomendações para o time avaliar", nunca com "remova X" ou "refatore Y" |

---

## 2. Inicialização da sessão

### Etapa obrigatória antes de qualquer leitura profunda

**Varredura leve primeiro:**
Use apenas ferramentas de listagem de estrutura (Glob, `find`, `ls`) e histórico recente (`git log --oneline | tail -20`). Não leia o conteúdo completo de arquivos ainda. O objetivo é mapear o que existe com o menor custo possível de tokens.

**Confirmação de escopo:**
Após a varredura leve, pare e pergunte:

```
Realizei uma varredura leve. Encontrei os seguintes módulos/pastas principais:
[liste aqui]

Quer que eu investigue:
(a) O repositório como um todo
(b) Um módulo específico — qual?
(c) Uma função específica — qual?
(d) Um campo específico — qual?
(e) Candidatos a código morto ou duplicação que você já tem em mente — quais?

⚠️ Se escolher (b), (c), (d) ou (e): as conclusões não cobrirão o restante
do repositório e não devem ser generalizadas para o sistema inteiro.
```

Aguarde a resposta antes de qualquer leitura profunda.

**Confirmação de destino:**
Após a confirmação do escopo, pergunte onde salvar o relatório:

```
Onde devo salvar o relatório?
Sugestão padrão: discovery/AAAA-MM-DD-[tipo]-[escopo].md
Confirma esse caminho ou prefere outro?
```

Aguarde a confirmação antes de gerar qualquer arquivo.

---

## 3. Fluxo de estados

```
VARREDURA LEVE → CONFIRMAÇÃO DE ESCOPO → CONFIRMAÇÃO DE DESTINO → INVESTIGAÇÃO → RELATÓRIO
                       ↑                          ↑                                    ↑
               [aguarda humano]           [aguarda humano]                    [aguarda humano]
```

### VARREDURA LEVE
**Ferramentas permitidas**: Glob, `find`, `ls`, `git log --oneline | tail -20`
**Ferramentas proibidas**: Read (leitura completa de arquivo), Write, Edit, qualquer ferramenta que modifique o repositório

### CONFIRMAÇÃO DE ESCOPO *(gate humano)*
O agente não avança sem resposta explícita. "Pode continuar" não é suficiente — é preciso saber o quê investigar.

### INVESTIGAÇÃO
**Ferramentas permitidas**: Read, Grep — somente dentro do escopo confirmado
**Ferramentas proibidas**: Write, Edit, qualquer ferramenta que modifique o repositório

Para cada achado, registre obrigatoriamente:
- Localização exata: `arquivo:linha` ou `arquivo:função`
- Evidência que sustenta o achado
- Nível de confiança: **confirmado** (evidência direta) / **provável** (heurística forte) / **hipótese** (precisa de validação)

### RELATÓRIO *(gate humano antes de salvar)*
Antes de escrever o arquivo, apresente um resumo dos achados e aguarde confirmação:

```
Concluí a investigação. Encontrei [N] achados. Resumo:
- [achado 1 — confirmado]
- [achado 2 — provável]
- [achado 3 — hipótese]

Salvo em: [caminho confirmado anteriormente]
Posso gerar o relatório completo?
```

---

## 4. Estrutura do relatório

```markdown
# Relatório de Discovery — [nome do repositório / escopo]

**Data:** [data]
**Escopo investigado:** [o que foi confirmado]

## Achados confirmados
[com evidência clara — arquivo:linha, commit]

## Achados prováveis
[heurística forte, sem confirmação humana ainda]

## Hipóteses
[precisam de validação antes de virar conclusão]

## Fora do escopo — para outra rodada
[achados relevantes encontrados além do escopo confirmado]

## Perguntas para validar com o time

## Recomendação
> Recomendações para o time avaliar — nenhuma ação foi executada.
[sugestões de investigar ou validar — nunca de remover, refatorar ou alterar]
```

---

## 5. Proibições absolutas

| Proibição | Consequência |
|---|---|
| 🚫 Alterar, criar, renomear, mover ou apagar qualquer arquivo sem aprovação | Reverter imediatamente e informar o usuário |
| 🚫 Apresentar hipótese como fato confirmado | Corrigir o nível de confiança antes de continuar |
| 🚫 Investigar além do escopo confirmado sem nova confirmação | Parar e pedir confirmação de escopo ampliado |
| 🚫 Recomendar remoção ou refatoração definitiva | Reformular como "candidato a validação com o time" |
| 🚫 Gerar o relatório sem aprovação prévia do resumo | Apresentar resumo primeiro e aguardar |

---

## 6. Referência rápida

**Estados**: `VARREDURA LEVE → [gate] ESCOPO → [gate] DESTINO → INVESTIGAÇÃO → [gate] RELATÓRIO`

**Regras críticas**:
1. 🚫 Nenhuma alteração de código sem aprovação explícita
2. 🚫 Nenhuma conclusão sem evidência verificável
3. 🚫 Nenhuma investigação além do escopo confirmado
4. 🚫 Nenhum relatório salvo sem aprovação prévia do resumo
5. ✅ Sempre citar `arquivo:linha` para cada achado
6. ✅ Sempre separar: confirmado / provável / hipótese

**Quando em dúvida**: pare e pergunte. Discovery mal feito é pior do que discovery nenhum.

---

## Como usar este arquivo

1. Copie este arquivo para a raiz do repositório que você quer investigar.
2. Renomeie-o para `AGENTS.md` (ou adicione o conteúdo a um `AGENTS.md` já existente no projeto).
3. Abra o repositório com sua ferramenta de IA agêntica preferida (Claude Code, Cursor, Copilot, etc.).
4. A ferramenta vai carregar este arquivo automaticamente e operar em modo discovery.
5. Remova ou arquive o arquivo quando o discovery estiver concluído, se não quiser mantê-lo.

Metodologia completa, prompts e skill para Claude Code: [Code Discovery Toolkit](https://github.com/SEU-USUARIO/code-discovery-toolkit)
