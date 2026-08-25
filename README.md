# 🔎 Code Discovery Toolkit

Um jeito estruturado de entender repositórios de código legados ou esquecidos e investigar código morto, duplicado ou redundante — sem inventar suposições, sem refatorar sem autorização e sem perder o foco do que foi pedido.

---

## ⚠️ Tem um repositório legado com zero documentação? Comece aqui!

Se você acabou de cair de paraquedas em um sistema legado que ninguém lembra o que faz e com **zero documentação**, não se desespere. Siga esta sequência passo a passo para mapear e auditar o código de forma segura:

### 1️⃣ Passo 1: Mapeamento Inicial & Contexto de Negócio
Abra a pasta [`prompts/`](prompts/), copie o conteúdo de [`01-mapeamento-inicial.md`](prompts/01-mapeamento-inicial.md) e cole no seu assistente de IA (Claude, ChatGPT, etc.) junto com a árvore de diretórios do repositório legado. 
> 💡 **Super Dica**: Se você possuir ou preencher os manuais rápidos de contexto ([`templates/contexto-produto-template.md`](templates/contexto-produto-template.md) ou [`templates/contexto-arquitetura-template.md`](templates/contexto-arquitetura-template.md)), anexe-os também! Isso dá à IA a visão do "Porquê" comercial por trás das regras e convenções do código, evitando relatórios puramente técnicos e genéricos. Leia o guia em [`docs/contexto-negocio-guia.md`](docs/contexto-negocio-guia.md).


### 2️⃣ Passo 2: Geração do Grafo de Dependências (`graphify.md`)
Antes de mergulhar fundo no código, gere o grafo de dependências do projeto usando a ferramenta open-source [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) (veja como fazer em [`docs/graphify-guia.md`](docs/graphify-guia.md)).
> **Por que fazer isso agora?** Anexar o `graphify.md` nas próximas etapas reduz o consumo médio de tokens da IA em **82%** e eleva a precisão da análise de impacto de **~42% para 93%** (dados baseados em benchmarks empíricos de projetos reais legados do mercado, mitigando alucinações de contexto longo). Isso garante que a IA entenda a estrutura global do projeto antes de ler o código bruto.


### 3️⃣ Passo 3: Health Check e Auditoria de Saúde
Copie o prompt [`05-health-check.md`](prompts/05-health-check.md) para analisar bandeiras vermelhas cruciais do código: incompatibilidades de tipos de dados (ex: `string` vs `int`), tratamentos de erro omitidos e alertas para gargalos de performance caso o volume de dados aumente. Consolide no template [`05-health-check-template.md`](templates/05-health-check-template.md).

### 4️⃣ Passo 4: Código Morto & Duplicações
Use os prompts [`02-codigo-morto.md`](prompts/02-codigo-morto.md) e [`03-duplicacoes-redundancias.md`](prompts/03-duplicacoes-redundancias.md) (com o apoio do script local [`scripts/analisar_repositorio.py`](scripts/)) para varrer lógicas obsoletas ou duplicadas e preencher os templates correspondentes.

### 5️⃣ Passo 5: Relatório Final
Use o prompt [`04-relatorio-final.md`](prompts/04-relatorio-final.md) para consolidar todos os achados em um único documento estratégico ([`templates/04-relatorio-final-template.md`](templates/04-relatorio-final-template.md)) para validação do time e tomada de decisão.

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

### 🚀 3. Copilot / Cline / Aider
Para outras ferramentas agênticas:
* Cole o conteúdo do [`templates/AGENTS-discovery-template.md`](templates/AGENTS-discovery-template.md) no campo de **System Prompt** (Instruções de Sistema) do agente ou no arquivo de configuração correspondente (ex: `.clinerules` ou `.aider.conf.yml`).

---

## 📁 Estrutura do Repositório

| Pasta / Arquivo | Conteúdo | Precisa saber programar? |
| :--- | :--- | :--- |
| [`prompts/`](prompts/) | Prompts prontos para colar na IA (Mapeamento, Código Morto, Saúde, etc.) | Não |
| [`docs/`](docs/) | Guia de [Metodologia](docs/metodologia.md), [Glossário de IA](docs/glossario.md), [Guia do Graphify](docs/graphify-guia.md), [Guia do Contexto de Negócio](docs/contexto-negocio-guia.md) e [Guia do GitHub Action](docs/github-action-guia.md) | Não |
| [`examples/`](examples/) | Exemplos reais de relatórios gerados (script e template de mapeamento preenchido) | Não |
| [`templates/`](templates/) | Templates markdown de relatórios (incluindo contexto de negócio/arquitetura) e a [GitHub Action Reutilizável](templates/github-action-discovery.yml) | Não |
| [`scripts/`](scripts/) | Script Python somente leitura que executa varredura de duplicados e inatividade | Sim (opcional) |
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
