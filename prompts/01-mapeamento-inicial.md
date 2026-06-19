# Prompt — Mapeamento Inicial de Repositório

Use este prompt para ajudar a entender o propósito de um repositório esquecido. Substitua os campos entre `[ ]`.

```
Você vai me ajudar a entender o propósito de um repositório de código que ninguém no time lembra exatamente o que faz.

Contexto que vou te dar: [cole aqui o README, a estrutura de pastas, ou a saída de "git log --oneline | tail -20" para ver os commits iniciais]

Regras importantes:
- Baseie toda conclusão apenas no que eu te forneci. Se faltar informação para responder algo, diga claramente "não há evidência suficiente" em vez de supor.
- Não sugira refatorações, melhorias ou remoções de código nesta etapa — o objetivo aqui é só entender, não mudar nada.
- Separe claramente o que é fato (está escrito no código/commits) do que é sua interpretação.

Quero que você me entregue:
1. Um resumo do que esse repositório parece fazer, e com que nível de confiança.
2. Pistas sobre quem o usa ou usava (outros sistemas, times, dependências).
3. Perguntas que eu deveria fazer para alguém do time para confirmar ou descartar suas hipóteses.
```
