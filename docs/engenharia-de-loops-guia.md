# Guia Avançado: Engenharia de Loops Agênticos, MCP & Guardiões de Tarefas

Este guia é voltado para desenvolvedores e arquitetos que utilizam assistentes e agentes de Inteligência Artificial de alta autonomia — como **Google Antigravity (AGY)**, **ChatGPT Codex**, **Claude Code**, **Cursor Agent**, **Aider** ou **Windsurf** — para realizar auditorias e higiene de código em bases legadas de grande porte (300+ arquivos).

---

## 🚀 O que fazer agora? (Passo a Passo Prático de 3 Minutos)

Se você quer executar a Engenharia de Loops no seu repositório legado agora, siga estas 3 etapas diretas:

1. **Passo 1 — Copie a Diretiva do Agente**:
   Copie o arquivo [`templates/AGENTS-discovery-template.md`](../templates/AGENTS-discovery-template.md) para a raiz do seu repositório legado com o nome correspondente à sua ferramenta de IA:
   - **Google Antigravity (AGY)** ou **Claude Code**: salve como `AGENTS.md` ou `CLAUDE.md`.
   - **Cursor / Windsurf**: salve como `.cursorrules` ou `.windsurfrules`.
   - **ChatGPT Codex / Canvas**: cole o texto nas *Instruções de Sistema* do seu projeto.

2. **Passo 2 — Cole o Prompt do Loop de Varredura**:
   No chat do seu assistente de IA, cole a seguinte instrução:
   > *"Leia o mapa `graphify.md`. Execute uma varredura iterativa módulo por módulo. Para cada módulo, salve o relatório em `discovery/modulos/[nome-do-modulo].md` sem modificar o código de produção."*

3. **Passo 3 — (Opcional) Publique os Cards no Jira/Azure via MCP**:
   Após o término do loop, instrua a IA:
   > *"Converta os achados do health check em cards no Jira/Azure Boards utilizando o modelo `templates/card-backlog-healthcheck-template.md` com a tag [Pendente Validação Humana]."*

---


## 🔁 O que é Engenharia de Loops Agênticos (Agentic Loops)?

Em repositórios legados extensos, pedir para uma IA analisar todos os arquivos de uma única vez estoura a **janela de contexto** (*context window*) do modelo, gerando alucinações, omissões ou respostas truncadas.

A **Engenharia de Loops Agênticos** resolve esse problema dividindo o discovery em um ciclo iterativo e controlado:

```text
[Grafo de Módulos (graphify.md)]
              │
              ▼
    ┌──────────────────┐
    │ Loop por Módulo  │ ──> Análise do Módulo N ──> Salva em discovery/modulos/
    └──────────────────┘
              │ (Próximo Módulo)
              ▼
    ┌──────────────────┐
    │ Loop CruzadoCoVE │ ──> Compara relatórios parciais (Duplicações entre módulos)
    └──────────────────┘
              │
              ▼
    ┌──────────────────┐
    │ Disparo via MCP  │ ──> Conecta via MCP Server (Jira / Azure Boards)
    └──────────────────┘
              │
              ▼
    ┌──────────────────┐
    │ Task Guardian    │ ──> Injeta etiqueta [Pendente Validação Humana] + Checklist
    └──────────────────┘
```

---

## 🛠️ Suporte a Ferramentas Agênticas

Este padrão de loop é agnóstico e pode ser aplicado nas principais plataformas agênticas do mercado:

- **Google Antigravity (AGY)**: Utiliza `subagents`, `skills` e conexões MCP nativas para delegar varreduras paralelas e executar scripts locais com salvamento em disco.
- **ChatGPT Codex / OpenAI Canvas**: Executa o loop via chamadas iterativas de funções (*function calling*) ou salvamento de artefatos.
- **Claude Code**: Executa subagentes e comandos de terminal em modo somente leitura (`CLAUDE.md`).
- **Cursor / Windsurf**: Utiliza regras agênticas (`.cursorrules` ou `.windsurfrules`) atreladas ao Composer/Agent.

---

## 🚀 Padrão 1: Loop de Varredura Iterativa Módulo por Módulo

### Prompt de Instrução do Loop:
```text
Você é um agente de discovery autônomo. Sua tarefa é auditar o repositório módulo por módulo utilizando a topologia em `graphify.md`.

Instruções para o Loop:
1. Leia a lista de módulos principais declarada em `graphify.md`.
2. Para CADA módulo identificado:
   a. Execute o Health Check (prompts/05-health-check.md) focado exclusivamente nos arquivos daquele módulo.
   b. Salve o resultado intermediário no arquivo `discovery/modulos/[nome-do-modulo].md`.
   c. Limpe sua memória intermediária antes de avançar para o próximo módulo.
3. Não altere nenhum arquivo de código-fonte durante a execução do loop.
```

---

## 🔍 Padrão 2: Loop de Verificação Cruzada (CoVE - Chain of Verification)

Após concluir a varredura individual de todos os módulos, o agente inicia uma segunda iteração:

```text
Instruções para o Loop de Verificação Cruzada:
1. Leia todos os arquivos de relatório gerados na pasta `discovery/modulos/`.
2. Identifique trechos de código, funções ou estruturas de dados que aparecem duplicadas ENTRE módulos diferentes.
3. Consolide as duplicações cruzadas no relatório final em `templates/03-duplicacoes-template.md`.
```

---

## 🔌 Padrão 3: Disparo via MCP & Guardiões de Tarefas (Jira / Azure Boards)

Para evitar que os achados fiquem esquecidos em arquivos Markdown, o agente pode utilizar o **MCP (Model Context Protocol)** para publicar os resultados diretamente na ferramenta de gestão de tarefas da empresa (Jira ou Azure Boards).

### O Conceito de "Task Guardian" (Guardião de Validação Humana)
> ⚠️ **REGRA CRÍTICA DE SEGURANÇA**: IAs podem gerar falsos positivos ou apontar como "código parado" uma função intencionalmente reservada para contingências de negócio.

Para proteger o time de engenharia, **todo card de backlog criado via IA/MCP DEVE conter obrigatoriamente um Guardião de Validação Humana**:

1. **Tag de Status**: O card deve ser publicado no Jira/Azure Boards com a tag `[Pendente Validação Humana]` ou `[TechnicalDebt-AI]`.
2. **Checklist Obrigatória do Desenvolvedor**: O corpo da tarefa precisa conter o modelo [`templates/card-backlog-healthcheck-template.md`](../templates/card-backlog-healthcheck-template.md), exigindo que um desenvolvedor humano marque os seguintes itens antes de mover o card para a coluna "Aprovado para Execução":
   - `[ ] Fato Verificado (Não é falso positivo)`
   - `[ ] Impacto de Negócio Validado com Produto`
   - `[ ] Solução Técnica Aprovada`

---

## 🛡️ Travas de Segurança (Loop Guardrails)

Para evitar consumo descontrolado de tokens ou loops infinitos:
1. **Limite de Iterações**: Fixe um número máximo de iterações por execução (ex: `max_iterations = 10`).
2. **Approval Gates em Bloco**: A cada 3 módulos auditados, o agente deve pausar e emitir um resumo parcial, solicitando a confirmação do usuário antes de prosseguir com os demais módulos.
3. **Somente Leitura Garantida**: Nenhuma chamada MCP ou comando de terminal em loop tem permissão para modificar o código-fonte de produção.
