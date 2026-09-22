# Workflow Manual

Use este modo quando quiser conduzir o discovery passo a passo com qualquer assistente de IA, sem depender de ferramentas adicionais.

## Fluxo

1. Gere ou forneça o contexto arquitetural disponível.
2. Execute `01-mapeamento-inicial.md`.
3. Execute o health check e a especificação conforme o objetivo.
4. Para código morto e duplicações, forneça os arquivos/candidatos manualmente ou use evidências produzidas pelo script compartilhado.
5. Consolide os resultados usando os templates da raiz em `../../templates/`.

Este modo prioriza portabilidade, transparência e controle humano. Para uma primeira varredura determinística, veja `../deterministic/`. Para loops autônomos controlados, veja `../agentic/`.
