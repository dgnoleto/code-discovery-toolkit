# Prompt — Identificação de Duplicações e Redundâncias

Use este prompt para comparar trechos de código em busca de duplicações. Ele pede confirmação do que comparar antes de aprofundar, para evitar comparações cruzadas caras quando você só queria validar um módulo ou um par específico.

```
Você vai comparar os trechos de código abaixo para identificar duplicações ou redundâncias (lógica repetida, funções muito parecidas, arquivos quase idênticos).

Contexto: [cole aqui os arquivos ou funções a comparar]

ETAPA 1 — Listagem leve (sem comparar ainda)
Primeiro, apenas liste os arquivos/funções recebidos no contexto, sem comparar o conteúdo entre eles ainda.

ETAPA 2 — Confirmação de escopo
Depois de listar, pare e me pergunte:
"Quer que eu compare (a) tudo entre si, ou (b) só um subconjunto específico (um módulo, ou pares que eu indicar)?"
Se eu escolher um subconjunto, me avise que duplicações fora desse subconjunto não foram verificadas. Espere eu te dizer quais itens/pares antes de continuar.

ETAPA 3 — Local de saída
Depois que eu confirmar o escopo, sugira um caminho/nome de arquivo padrão (ex: discovery/AAAA-MM-DD-duplicacoes-[escopo].md) e pergunte se confirmo ou prefiro outro. Espere minha confirmação antes de gerar o conteúdo final.

ETAPA 4 — Comparação (só depois das etapas acima)
Regras importantes:
- Aponte apenas duplicações reais, com base no conteúdo fornecido. Não invente similaridades que não estão claramente no código.
- Para cada duplicação encontrada, diga onde está cada ocorrência (arquivo/função/linha aproximada).
- Não proponha a solução de unificação ainda — apenas identifique e descreva a duplicação. A decisão de unificar (e como) é do time.
- Se a duplicação parecer intencional (ex: por isolamento entre módulos), avise isso também.
- Organize sua resposta seguindo a estrutura do template em templates/03-duplicacoes-template.md.

Me entregue uma lista de duplicações/redundâncias encontradas (apenas do escopo confirmado na etapa 2), com localização e uma breve explicação do porquê parecem duplicadas.
```
