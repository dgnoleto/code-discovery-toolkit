# Prompt — Mapeamento Inicial de Repositório

Use este prompt para entender o propósito de um repositório esquecido. Ele já inclui uma confirmação de escopo antes de aprofundar, para evitar gastar tokens mapeando o repositório inteiro quando você só precisava de um pedaço. Substitua os campos entre `[ ]`.

```
Você vai me ajudar a entender o propósito de um repositório de código que ninguém no time lembra exatamente o que faz.

Contexto que vou te dar: [cole aqui o README, a estrutura de pastas, ou a saída de "git log --oneline | tail -20" para ver os commits iniciais]

ETAPA 1 — Leitura leve (sem aprofundar ainda)
Faça primeiro uma varredura leve: liste a estrutura de pastas, os nomes de arquivos e os módulos que você identifica, SEM ler o conteúdo completo de cada arquivo ainda. O objetivo aqui é só me mostrar o que existe, não analisar profundamente.

ETAPA 2 — Confirmação de escopo
Depois de me mostrar essa lista, pare e me pergunte:
"Quer que eu mapeie (a) o repositório como um todo, (b) um módulo específico, (c) uma função específica, ou (d) um campo específico?"
Se eu escolher qualquer opção que não seja "o repositório como um todo", me avise claramente que as conclusões não vão cobrir o restante do repositório e podem não se sustentar se eu tentar generalizar para o sistema inteiro. Espere eu te dizer qual módulo, função ou campo antes de continuar.

ETAPA 3 — Local de saída
Depois que eu confirmar o escopo, sugira um caminho/nome de arquivo padrão para o resultado (ex: discovery/AAAA-MM-DD-mapeamento-[escopo].md) e me pergunte se confirmo esse caminho ou prefiro outro. Espere minha confirmação antes de gerar o conteúdo final.

ETAPA 4 — Mapeamento (só depois das etapas acima)
Regras importantes:
- Baseie toda conclusão apenas no que eu te forneci. Se faltar informação para responder algo, diga claramente "não há evidência suficiente" em vez de supor.
- Não sugira refatorações, melhorias ou remoções de código nesta etapa — o objetivo aqui é só entender, não mudar nada.
- Separe claramente o que é fato (está escrito no código/commits) do que é sua interpretação.

Me entregue:
1. Um resumo do que esse repositório (ou o escopo escolhido) parece fazer, e com que nível de confiança.
2. Pistas sobre quem o usa ou usava (outros sistemas, times, dependências).
3. Perguntas que eu deveria fazer para alguém do time para confirmar ou descartar suas hipóteses.
```
