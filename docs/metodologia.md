# Metodologia de Discovery de Repositórios Esquecidos

Use este guia para investigar um repositório que ninguém lembra mais o propósito, ou para levantar candidatos a código morto, duplicado ou redundante.

## Antes de começar

- Defina o escopo: qual repositório (ou módulo) e qual pergunta você está tentando responder.
- Garanta que você tem acesso de leitura ao histórico completo (`git log`, issues, PRs antigos).
- Avise o time responsável (se existir) que esse levantamento está sendo feito.

## Etapa 1 — Levantamento inicial

- Leia o README e qualquer documentação existente (mesmo que desatualizada).
- Liste linguagens, frameworks e dependências principais.
- Veja quem são os principais contribuidores e quando foi o último commit relevante.
- Use o prompt [`prompts/01-mapeamento-inicial.md`](../prompts/01-mapeamento-inicial.md) para apoiar essa etapa com IA.

## Etapa 2 — Entendimento do propósito original

- Olhe os primeiros commits e o README nas versões mais antigas — geralmente revelam a intenção original.
- Verifique se existem issues, PRs ou documentos externos (wiki, Notion, Confluence) linkados.
- Procure por quem consome esse repositório hoje (outro serviço, um cron job, um time).

## Etapa 3 — Análise de atividade

- Rode o script [`scripts/analisar_repositorio.py`](../scripts/analisar_repositorio.py) para levantar arquivos sem commits recentes, duplicados exatos e possíveis não referenciados.
- Trate os resultados como candidatos, não conclusões.

## Etapa 4 — Identificação de código morto, duplicado ou redundante

- Use os prompts [`prompts/02-codigo-morto.md`](../prompts/02-codigo-morto.md) e [`prompts/03-duplicacoes-redundancias.md`](../prompts/03-duplicacoes-redundancias.md) junto com a saída do script para investigar cada candidato com mais contexto.
- Para cada candidato, registre: onde está (arquivo/linha), por que é candidato, e qual evidência sustenta isso.

## Etapa 5 — Validação com o time

- Apresente os achados para alguém que conheça (ou conheceu) o repositório.
- Pergunte diretamente: "isso ainda é usado?", "podemos remover isso?", "isso é intencionalmente duplicado?".
- Nunca tome a decisão de remover ou refatorar sem essa validação.

## Etapa 6 — Relatório final

- Use o prompt [`prompts/04-relatorio-final.md`](../prompts/04-relatorio-final.md) para compilar tudo no formato do template.
- Preencha o template [`templates/relatorio-discovery-template.md`](../templates/relatorio-discovery-template.md) com os achados confirmados, prováveis e hipóteses.
- Entregue o relatório como uma recomendação para o time decidir os próximos passos.
