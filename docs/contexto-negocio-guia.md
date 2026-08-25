# Guia de Mapeamento de Contexto de Negócio & Produto

## O "Porquê" por trás do "Como"

Ao usar Inteligência Artificial para analisar um repositório legado, é comum que a IA traga respostas puramente técnicas e genéricas. Ela consegue ler o código e entender *como* ele funciona, mas não tem como adivinhar o *porquê* de sua existência ou o seu impacto no produto.

Para evitar isso, adotamos a prática de **RAG Local (Retrieval-Augmented Generation)** de negócio: alimentar a IA com arquivos Markdown simples que servem como "manuais de contexto" da sua empresa antes de pedir análises de código.

---

## 📁 Os 4 Manuais de Contexto Recomendados

Para calibrar o entendimento da IA, recomenda-se criar e manter arquivos Markdown estruturados na raiz do seu projeto ou em uma pasta `contexto/`. Os 4 manuais sugeridos são:

### 1. Manual das Linhas de Produto (`templates/contexto-produto-template.md`)
- **Objetivo**: Explicar o que o seu SaaS faz de fato.
- **Conteúdo**: Módulos de negócio, regras de faturamento, personas (quem usa), fluxos de valor e casos de uso chaves.
- **Exemplo de uso**: Ajuda a IA a relacionar o arquivo `billing.py` às regras de planos específicos da empresa (ex: B2B Enterprise).

### 2. Manual da Arquitetura e Stack (`templates/contexto-arquitetura-template.md`)
- **Objetivo**: Explicar as convenções e limites técnicos do seu ambiente.
- **Conteúdo**: Escolhas de banco de dados, bibliotecas legadas que não podem ser alteradas, padrões de projeto decididos pelo time e integrações ativas (APIs externas).
- **Exemplo de uso**: Evita que a IA sugira trocar uma biblioteca legada por uma moderna se houver uma restrição documentada.

### 3. Manual de Concorrentes e Players de Mercado
- **Objetivo**: Alinhar a IA com os padrões competitivos do seu segmento de mercado.
- **Conteúdo**: Terminologias comuns do mercado (ex: FinTech, AgTech, HealthTech), concorrentes mapeados e padrões de UX/Regras adotados por eles.
- **Exemplo de uso**: Permite à IA sugerir melhorias de produto no código que estejam alinhadas às tendências do seu setor.

### 4. Manual de Processos e Rituais do Time
- **Objetivo**: Explicar como a equipe de engenharia e produto opera no dia a dia.
- **Conteúdo**: Nomes das sprints, rituais, ritos de deploy, uso do Jira/Notion, e regras de governança e accountability.
- **Exemplo de uso**: Permite à IA sugerir melhorias de documentação ou tags de tarefas diretamente formatadas para o seu fluxo (Jira).

---

## ⚡ Como Usar no Discovery

1. **Preencha os templates**: Use os modelos disponíveis em `templates/` para criar os arquivos de contexto do seu projeto.
2. **Anexe na Conversa**: Ao iniciar o prompt [`prompts/01-mapeamento-inicial.md`](../prompts/01-mapeamento-inicial.md) ou [`prompts/05-health-check.md`](../prompts/05-health-check.md), informe a IA sobre a presença desses manuais.
3. **Cruzamento de Dados**: A IA usará as definições dos manuais para classificar os achados técnicos, gerando relatórios ricos que conectam a linha de código diretamente à regra de negócio correspondente.
