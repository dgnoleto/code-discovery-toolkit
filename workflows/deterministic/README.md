# Workflow Determinístico

Use este modo quando quiser reduzir o trabalho de detecção delegado à LLM.

## Princípio

**Ferramentas detectam e medem; a IA interpreta contexto; pessoas decidem.**

O toolkit oferece duas portas:

- `../../scripts/analisar_repositorio.py`: baseline Python do próprio projeto, sem substituir a validação humana.
- `jscpd-guia.md`: alternativa especializada para detecção de duplicações.

A ideia não é executar todas as ferramentas ao mesmo tempo. Escolha a evidência adequada ao repositório, entregue os candidatos ao workflow manual e use a IA para revisar contexto, falsos positivos e risco.

Nenhum achado determinístico autoriza remoção ou refatoração automática.
