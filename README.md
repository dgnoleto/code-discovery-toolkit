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
Use os prompts [`02-codigo-morto.md`](prompts/02-codigo-morto.md) e [`03-duplicacoes-redundancias.md`](prompts/03-duplicacoes-redundancias.md) (com o apoio do script local [`scripts/analisar_repositorio.py`](scripts/)) para varrer lógicas obsoletas ou duplicadas e preencher os templates correspondentes.

### 6️⃣ Passo 6: Relatório Final & Integração de Backlog (Jira / Azure / GitHub)
Use o prompt [`04-relatorio-final.md`](prompts/04-relatorio-final.md) para consolidar todos os achados em um único documento estratégico ([`templates/04-relatorio-final-template.md`](templates/04-relatorio-final-template.md)) e enviar automaticamente os débitos técnicos para o Jira ou Azure Boards do seu time.

---

## 🤖 Como transformar este toolkit em um Agente de IA (Claude Code, Cursor, etc.)

Você pode automatizar toda essa metodologia configurando as diretivas de comportamento do toolkit diretamente em seus assistentes de código agênticos.

### 💻 1. Claude Code
O Claude Code lê automaticamente instruções de comportamento de arquivos markdown específicos.
* **Como configurar**: Copie o arquivo [`templates/AGENTS-discovery-template.md`](templates/AGENTS-discovery-template.md) para a raiz do repositório que você deseja analisar e renomeie-o para **`CLAUDE.md`**.
* **Como usar**: Ao iniciar o Claude Code no terminal, ele carregará as regras do `CLAUDE.md` automaticamente, assumindo a persona de Discovery (agente somente leitura, com gates de confirmação de escopo e checagem de `graphify.md`).

### ⌃ 2. Cursor
O Cursor permite definir regras de comportamento para a IA usando arquivos `.cursorrules`.
* **Como configurar**: Copie o arquivo [`templates/AGENTS-discovery-template.md`](templates/AGENTS-discovery-template.md) para a raiz do repositório legado e renomeie para **`.cursorrules`**.
* **Alternativa (Novo padrão do Cursor)**: Salve o arquivo na pasta do projeto como **`.cursor/rules/discovery.md`**.
* **Como usar**: O Chat do Cursor (Ctrl+L) e o Composer (Ctrl+I) seguirão estritamente as regras de não-alteração de código e validação prévia de escopo.

### 🏢 3. Governança Corporativa (Azure DevOps & Jira)
Este toolkit é 100% compatível com grandes ecossistemas corporativos:
* **Azure DevOps (Repos, Pipelines & Boards)**: Configure o pipeline agendado ([`templates/azure-pipelines-discovery.yml`](templates/azure-pipelines-discovery.yml)) para abrir Tasks no Azure Boards. Veja o [Guia de Azure DevOps](docs/azure-devops-guia.md).
* **Jira (Atlassian)**: Envie relatórios automaticamente para o Jira do seu time com o parâmetro `--jira-url` no script. Veja o [Guia de Integração com Jira](docs/jira-guia.md).

---

## 📁 Estrutura do Repositório

| Pasta / Arquivo | Conteúdo | Precisa saber programar? |
| :--- | :--- | :--- |
| [`prompts/`](prompts/) | Prompts prontos para colar na IA (Graphify, Mapeamento, Saúde, **Spec Técnica**, etc.) | Não |
| [`docs/`](docs/) | Guia de [Metodologia](docs/metodologia.md), [Glossário de IA](docs/glossario.md), [Guia do Graphify](docs/graphify-guia.md), [Contexto de Negócio](docs/contexto-negocio-guia.md), [Azure DevOps](docs/azure-devops-guia.md) e [Jira](docs/jira-guia.md) | Não |
| [`examples/`](examples/) | Exemplos reais de relatórios gerados (script e template de mapeamento preenchido) | Não |
| [`templates/`](templates/) | Templates markdown (relatórios e **Spec Técnica**), [GitHub Action](templates/github-action-discovery.yml) e [Azure Pipeline](templates/azure-pipelines-discovery.yml) | Não |
| [`scripts/`](scripts/) | Script Python somente leitura (varredura e envio automatizado para o **Jira**) | Sim (opcional) |
| [`templates/AGENTS-discovery-template.md`](templates/AGENTS-discovery-template.md) | Template de comportamento seguro para agentes de IA | Não |

---

## 🛡️ Princípios Não Negociáveis

1. **Não inventar**: Toda conclusão precisa de evidência direta (código, commit, histórico ou confirmação humana).
2. **Não refatorar sem autorização**: O objetivo é exclusivamente mapear e documentar. A IA está estritamente proibida de alterar o código de produção ou inflar o projeto.
3. **Não sair do foco**: Toda rodada de análise tem escopo definido e gates de aprovação humana obrigatórios.

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
