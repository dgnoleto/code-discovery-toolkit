# Prompt 01 — Mapeamento Arquitetural & Propósito do Repositório

Use este prompt após ter gerado o `graphify.md` (Passo 1 do Discovery). Ele utiliza o grafo topológico e o código para entender a arquitetura e os módulos de um sistema sem documentação.

```text
Você vai me ajudar a entender o propósito e a arquitetura de um repositório de código legado que não possui documentação.

Contexto que vou te dar: [Cole o conteúdo do arquivo graphify.md gerado no Passo 1]

Manuais de Contexto (Opcional): [Se houver, indique manuais como contexto-produto-template.md ou contexto-arquitetura-template.md]

ETAPA 1 — Leitura da Topologia (via graphify.md)
1. Analise o grafo de dependências e topologia fornecido no `graphify.md`.
2. Liste os módulos principais identificados, destacando como eles se relacionam entre si.
3. Se manuais de contexto de negócio tiverem sido fornecidos, cruze os módulos do código com as regras comerciais desde o início.

ETAPA 2 — Confirmação de escopo
Depois de me mostrar essa lista de módulos, pare e me pergunte:
"Quer que eu mapeie (a) o repositório como um todo, (b) um módulo específico, (c) uma função específica, ou (d) um campo específico?"
Se eu escolher qualquer opção que não seja "o repositório como um todo", me avise claramente que as conclusões não vão cobrir o restante do repositório. Espere minha confirmação antes de continuar.

ETAPA 3 — Local de saída
Depois que eu confirmar o escopo, sugira um caminho/nome de arquivo padrão para o resultado (ex: discovery/AAAA-MM-DD-mapeamento-[escopo].md) e aguarde minha confirmação.

ETAPA 4 — Mapeamento Arquitetural
Regras importantes:
- Baseie toda conclusão nas evidências do graphify.md e do código fornecido. Se faltar informação, diga "não há evidência suficiente".
- Não sugira refatorações ou remoções nesta etapa — o objetivo é exclusivamente entender o sistema.
- Organize sua resposta seguindo o template em ../../templates/01-mapeamento-template.md.

Me entregue:
1. Um resumo do que o repositório (ou módulo escolhido) faz e com qual nível de confiança.
2. Pistas sobre quem o usa ou usava (outros sistemas, times, dependências externas).
3. Perguntas técnicas e de produto para validar hipóteses com o time.
```
