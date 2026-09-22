# 🔎 Code Discovery Toolkit

Um jeito estruturado de entender repositórios de código legados ou esquecidos e investigar código morto, duplicado ou redundante — sem inventar suposições, sem refatorar sem autorização e sem perder o foco do que foi pedido.

---

## ⚠️ Tem um repositório legado com zero documentação? Comece aqui!

Se você acabou de cair de paraquedas em um sistema legado que ninguém lembra o que faz e com **zero documentação**, não se desespere. Siga esta sequência passo a passo para mapear e auditar o código de forma segura:

### 1️⃣ Passo 1: Geração do Grafo de Dependências (`graphify.md`)
Antes de qualquer análise de código, gere a topologia do repositório usando a ferramenta open-source [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) (veja como fazer em [`docs/graphify-guia.md`](docs/graphify-guia.md)).
> **Por que este é o Passo 1?** Anexar o `graphify.md` nas etapas seguintes reduz o consumo médio de tokens da IA em **82%** e eleva a precisão da análise de impacto de **~42% para 93%** (dados baseados em benchmarks empíricos de projetos reais legados do mercado, mitigando alucinações de contexto longo). Isso garante que a IA entenda a estrutura global do projeto antes de ler o código bruto.

### 2️⃣ Passo 2: Mapeamento Arquitetural & Propósito
Abra a pasta [`prompts/`](prompts/), copie o conteúdo de [`01-mapeamento-inicial.md`](prompts/01-mapeamento-inicial.md) e cole no seu assistente de IA (Claude, ChatGPT, Cursor, etc.) fornecendo o `graphify.md` gerado no Passo 1.
> 💡 **Super Dica**: Se você possuir os manuais rápidos de contexto ([`templates/contexto-produto-template.md`](templates/contexto-produto-template.md) ou [`templates/contexto-arquitetura-template.md`](templates/contexto-arquitetura-template.md)), anexe-os também! Isso dá à IA a visão do "Porquê" comercial por trás das regras e convenções do código. Leia o guia em [`docs/contexto-negocio-guia.md`](docs/contexto-negocio-guia.md).

### 3️⃣ Passo 3: Health Check e Auditoria de Saúde
Copie o prompt [`05-health-check.md`](prompts/05-health-check.md) para analisar bandeiras vermelhas cruciais do código: incompatibilidades de tipos de dados (ex: `string` vs `int`), tratamentos de erro omitidos e alertas para gargalos de performance caso o volume de dados aumente. Consolide no template [`05-health-check-template.md`](templates/05-health-check-template.md).

### 4️⃣ Passo 4: Especificação Técnica & Manual do Legado (NOVO)
Copie o prompt [`06-especificacao-tecnica.md`](prompts/06-especificacao-tecnica.md) para gerar uma **Especificação Técnica & Funcional** baseada exclusivamente no código real. Este passo permite que desenvolvedores e o time de produto identifiquem divergências entre o comportamento real do sistema e a intenção de negócio, consolidando tudo no template [`06-especificacao-tecnica-template.md`](templates/06-especificacao-tecnica-template.md).

### 5️⃣ Passo 5: Código Morto & Duplicações
Adote o fluxo **deterministic-first, AI-second**: gere primeiro evidências objetivas com ferramentas adequadas e use a IA para validar contexto e falsos positivos. Para duplicações, o [`jscpd`](https://github.com/kucherenko/jscpd) é uma opção leve; veja [`docs/jscpd-guia.md`](docs/jscpd-guia.md). Depois use os prompts [`02-codigo-morto.md`](prompts/02-codigo-morto.md) e [`03-duplicacoes-redundancias.md`](prompts/03-duplicacoes-redundancias.md), com apoio opcional do [`scripts/analisar_repositorio.py`](scripts/), para interpretar os candidatos e preencher os templates correspondentes.

> **Princípio:** ferramentas detectam e medem; a IA interpreta contexto; o time decide.

### 6️⃣ Passo 6: Relatório Final & Integração de Backlog (Jira / Azure / GitHub)
Use o prompt [`04-relatorio-final.md`](prompts/04-relatorio-final.md) para consolidar todos os achados em um único documento estratégico ([`templates/04-relatorio-final-template.md`](templates/04-relatorio-final-template.md)) e enviar automaticamente os débitos técnicos para o Jira ou Azure Boards do seu time.

---

## 🤖 Como transformar este toolkit em um Agente de IA (Antigravity, Codex, Claude Code, Cursor)

Você pode automatizar toda essa metodologia configurando as diretivas de comportamento do toolkit diretamente em seus assistentes de código agênticos.

### 🌌 1. Google Antigravity (AGY) & ChatGPT Codex
Plataformas agênticas modernas executam o toolkit utilizando habilidades nativas (*skills*), ferramentas MCP e subagentes:
* **Como usar no Antigravity**: Carregue o [`templates/AGENTS-discovery-template.md`](templates/AGENTS-discovery-template.md) como diretiva de sistema. O Antigravity executa a varredura em subagentes paralelos e conecta-se via MCP ao Jira ou Azure DevOps.
* **Como usar no ChatGPT Codex / Canvas**: Insira o template de agente nas instruções de sistema (*System Prompt*) do seu projeto. O Codex executará a leitura dos módulos preservando a trava de somente leitura.

### 💻 2. Claude Code & Cursor
* **Claude Code**: Copie [`templates/AGENTS-discovery-template.md`](templates/AGENTS-discovery-template.md) para a raiz como **`CLAUDE.md`**. Ao abrir no terminal, ele assumirá o perfil de Discovery somente leitura.
* **Cursor / Windsurf**: Copie [`templates/AGENTS-discovery-template.md`](templates/AGENTS-discovery-template.md) para a raiz como **`.cursorrules`** (ou `.cursor/rules/discovery.md`).

### 🔄 3. Engenharia de Loops Agênticos, MCP & Guardiões (Avançado)
Para repositórios gigantes (300+ arquivos), consulte o **[Guia de Engenharia de Loops Agênticos](docs/engenharia-de-loops-guia.md)**. Ele ensina a configurar:
* Varreduras iterativas módulo a módulo sem estourar a janela de contexto.
* Conexão via **MCP (Model Context Protocol)** com o Jira / Azure Boards.
* Injeção de **Guardiões de Validação Humana** ([`templates/card-backlog-healthcheck-template.md`](templates/card-backlog-healthcheck-template.md)) exigindo que desenvolvedores auditem a veracidade de cada card antes da implementação.

### 🏢 4. Governança Corporativa (Azure DevOps & Jira)
* **Azure DevOps (Repos, Pipelines & Boards)**: Configure o pipeline agendado ([`templates/azure-pipelines-discovery.yml`](templates/azure-pipelines-discovery.yml)) para abrir Tasks no Azure Boards. Veja o [Guia de Azure DevOps](docs/azure-devops-guia.md).
* **Jira (Atlassian)**: Envie relatórios automaticamente para o Jira do seu time com o parâmetro `--jira-url` no script. Veja o [Guia de Integração com Jira](docs/jira-guia.md).

---

## 📁 Estrutura do Repositório

| Pasta / Arquivo | Conteúdo | Precisa saber programar? |
| :--- | :--- | :--- |
| [`prompts/`](prompts/) | Prompts prontos para colar na IA (Graphify, Mapeamento, Saúde, **Spec Técnica**, etc.) | Não |
| [`docs/`](docs/) | Guia de [Metodologia](docs/metodologia.md), [Glossário de IA](docs/glossario.md), [Graphify](docs/graphify-guia.md), [Contexto de Negócio](docs/contexto-negocio-guia.md), [Engenharia de Loops & MCP](docs/engenharia-de-loops-guia.md), [jscpd / análise determinística](docs/jscpd-guia.md), [Azure DevOps](docs/azure-devops-guia.md) e [Jira](docs/jira-guia.md) | Não |
| [`examples/`](examples/) | Exemplos reais de relatórios gerados (script e template de mapeamento preenchido) | Não |
| [`templates/`](templates/) | Templates markdown (relatórios, **Spec Técnica** e **Cards de Backlog com Guardião**), [GitHub Action](templates/github-action-discovery.yml) e [Azure Pipeline](templates/azure-pipelines-discovery.yml) | Não |
| [`scripts/`](scripts/) | Script Python somente leitura (varredura e envio automatizado para o **Jira**) | Sim (opcional) |
| [`templates/AGENTS-discovery-template.md`](templates/AGENTS-discovery-template.md) | Template de comportamento seguro para agentes de IA | Não |

---

## 🛡️ Princípios Não Negociáveis

1. **Não inventar**: Toda conclusão precisa de evidência direta (código, commit, histórico ou confirmação humana).
2. **Não refatorar sem autorização**: O objetivo é exclusivamente mapear e documentar. A IA está estritamente proibida de alterar o código de produção ou inflar o projeto.
3. **Não sair do foco**: Toda rodada de análise tem escopo definido e gates de aprovação humana obrigatórios.
4. **Deterministic-first, AI-second**: Quando uma ferramenta puder produzir evidência objetiva de forma reproduzível, use-a antes da LLM. Reserve a IA para contexto, falsos positivos e interpretação.

Detalhes completos em [`docs/principios.md`](docs/principios.md).

---

## 📚 Glossário & Conceitos

Consulte o documento **[`docs/glossario.md`](docs/glossario.md)** para explicações amigáveis sobre:
* **Conceitos de IA**: LLM, RAG, Graphify, Chain-of-Verification (CoVE), Approval Gates, Human-in-the-Loop (HITL), Janela de Contexto, MCP e AST.
* **Conceitos de Engenharia & Produto**: Discovery Técnico, Débito Técnico, Código Morto, Code Smells e Clean Code.

---

## 🌟 Inspirações e referências

* [**Graphify-Labs/graphify**](https://github.com/Graphify-Labs/graphify): Inspirou a integração de grafos de dependências para análise de impacto. Testes empíricos em projetos reais apontam redução de até 82% no consumo de tokens e aumento da acurácia de ~42% para 93% após validação humana.
* [**llm-council**](https://github.com/karpathy/llm-council) (Andrej Karpathy): Inspirou a ideia de validação cruzada para achados críticos.
* [**agency-agents-app**](https://github.com/msitarzewski/agency-agents-app): Inspirou o formato `AGENTS.md` e o conceito de Approval Gates.

---

## 👤 Autor

Feito por **Danilo Nolêto**, Product Manager com prática em discovery técnico assistido por IA, governança de IA aplicada à engenharia de requisitos e recuperação de sistemas legados.  
[LinkedIn](https://linkedin.com/in/danilog-noleto)

---

## 📄 Licença

Este projeto está sob a licença MIT — veja [`LICENSE`](LICENSE).
