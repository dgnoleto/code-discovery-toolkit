# Prompt — Identificação de Candidatos a Código Morto

Use este prompt para investigar candidatos a código morto. Ele pede confirmação do que investigar antes de aprofundar, para não gastar tokens analisando o repositório inteiro quando você só queria validar um módulo ou uma lista específica de candidatos.

```
Você vai analisar trechos de código que vou te fornecer para levantar candidatos a código morto (código que não é mais executado ou utilizado).

Contexto: [cole aqui os arquivos relevantes, ou a saída do script scripts/analisar_repositorio.py]

ETAPA 1 — Listagem leve (sem julgar ainda)
Primeiro, apenas liste os arquivos/funções que aparecem no contexto que te dei, sem ainda avaliar se são ou não candidatos a código morto.

ETAPA 2 — Confirmação de escopo
Depois de listar, pare e me pergunte:
"Quer que eu investigue (a) todos os itens dessa lista, ou (b) só um subconjunto específico (um módulo, um arquivo, ou alguns itens que eu indicar)?"
Se eu escolher um subconjunto, me avise que os demais itens da lista não foram avaliados e não devem ser considerados "ok" ou "sem problema" só porque não entraram nessa rodada. Espere eu te dizer quais itens antes de continuar.

ETAPA 3 — Local de saída
Depois que eu confirmar o escopo, sugira um caminho/nome de arquivo padrão (ex: discovery/AAAA-MM-DD-codigo-morto-[escopo].md) e pergunte se confirmo ou prefiro outro. Espere minha confirmação antes de gerar o conteúdo final.

ETAPA 4 — Análise (só depois das etapas acima)
Regras importantes:
- Trate tudo como CANDIDATO, nunca como conclusão definitiva. Você não tem visibilidade total do sistema (pode haver chamadas dinâmicas, jobs externos, etc).
- Para cada candidato, cite o arquivo e, se possível, a linha ou função específica.
- Indique o nível de confiança: alto (ex: função nunca referenciada em nenhum lugar do código fornecido), médio, ou baixo (ex: parece sem uso, mas pode ser chamada externamente).
- Não sugira remover ou apagar nada. Não escreva código de refatoração.
- Se não tiver certeza, diga isso explicitamente em vez de arriscar um palpite.

Me entregue uma lista de candidatos (apenas dos itens confirmados na etapa 2) com: localização, motivo da suspeita e nível de confiança.
```
