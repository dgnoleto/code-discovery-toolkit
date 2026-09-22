# Guia de Integração: Azure DevOps (Repos, Pipelines & Boards)

Este guia ensina como integrar o **Code Discovery Toolkit** a repositórios hospedados no **Azure DevOps** para automação de varreduras e criação de Work Items no **Azure Boards**.

---

## 1. Modo Interativo e Agentes (Azure Repos & VS Code / Cursor)

Se a sua equipe utiliza repositórios no **Azure Repos**:
1. **Persona de IA no VS Code / Cursor**: Copie o arquivo [`workflows/agentic/AGENTS-discovery-template.md`](../workflows/agentic/AGENTS-discovery-template.md) para a raiz do seu projeto no Azure Repos com o nome de **`AGENTS.md`** ou **`.cursorrules`**.
2. **Execução no Azure OpenAI**: Ao colar os prompts de `workflows/manual/` na IA corporativa da sua empresa (conectada ao Azure OpenAI Service), inclua os manuais de contexto (`contexto-produto-template.md`) e o `graphify.md`.

---

## 2. Automação Mensal via Azure Pipelines

Para executar a varredura automaticamente e receber alertas de código parado diretamente no seu painel de tarefas do Azure Boards:

### Passo 1: Copiar o arquivo de Pipeline
1. Copie o arquivo [`templates/azure-pipelines-discovery.yml`](../templates/azure-pipelines-discovery.yml) para a raiz do seu projeto no Azure Repos.
2. Certifique-se de que o script `scripts/analisar_repositorio.py` também esteja presente na pasta `scripts/` do repositório.

### Passo 2: Criar o Pipeline no Azure DevOps
1. No seu projeto do Azure DevOps, vá no menu **Pipelines** > **New Pipeline**.
2. Selecione **Azure Repos Git** e escolha o seu repositório.
3. Selecione a opção **Existing Azure Pipelines YAML file** e aponte para `azure-pipelines-discovery.yml`.
4. Clique em **Save**.

### Passo 3: Configurar Permissões no Azure Boards
Para que o pipeline consiga criar Work Items (Tasks/Bugs) automaticamente no Azure Boards:
1. No Azure DevOps, vá em **Project Settings** > **Repositories** > **Select your repository**.
2. Na aba **Security**, localize a conta de serviço **[Project Name] Build Service ([Org Name])**.
3. Garanta que a permissão **Contribute** e a permissão de criação de Work Items no projeto estejam marcadas como **Allow**.

---

## 💡 Como Funciona a Automação

- **Execução Agendada**: Todo dia 1º de cada mês às 08:00 UTC o Azure Pipelines executa o script de varredura.
- **Checagem Inteligente**: Se houver arquivos sem commits há mais de 365 dias ou duplicações altas, uma **Task** com a tag `TechnicalDebt` é criada automaticamente no Azure Boards para revisão da equipe.
- **Zero Ruído**: Se o repositório estiver limpo e sem achados pendentes, o pipeline conclui com sucesso sem criar tarefas duplicadas no painel.
