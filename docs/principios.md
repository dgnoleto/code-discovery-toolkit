# Princípios do Discovery

Estes princípios existem para proteger o time e o código durante qualquer trabalho de discovery. Eles valem tanto para pessoas quanto para assistentes de IA usados no processo.

## 1. Não inventar

Toda afirmação sobre o que um código faz, por que ele existe ou se ele está em uso precisa estar amparada em evidência verificável: o próprio código, commits, issues, documentação, ou alguém do time confirmando. Se não há evidência, isso é uma hipótese — e precisa ser rotulada como hipótese, nunca apresentada como fato.

## 2. Não refatorar sem autorização

Discovery é sobre entender e mapear, não sobre corrigir. Nenhuma mudança de código, renomeação, remoção de arquivo ou "limpeza" deve ser feita como parte desse processo sem autorização explícita de quem é responsável pelo repositório.

## 3. Não sair do foco

Cada rodada de discovery tem um escopo definido (ex: "mapear o propósito do repositório X" ou "levantar candidatos a código morto no módulo Y"). Achados fora desse escopo devem ser anotados separadamente para uma próxima rodada, não investigados na hora — isso evita que o trabalho nunca termine.

## 4. Separar fato de suposição

Todo relatório final deve indicar claramente o nível de confiança de cada achado:

- **Confirmado** — há evidência direta (código, commit, ou confirmação humana).
- **Provável** — heurística forte, mas sem confirmação humana ainda.
- **Hipótese** — precisa de validação antes de ser tratada como verdade.

## 5. Entregar recomendações, não decisões

O resultado de um discovery é uma lista de candidatos e perguntas para o time decidir — nunca uma ação já tomada. Quem decide o que fazer com o código é sempre o time responsável por ele.

## 6. Confirmar escopo e destino antes de aprofundar

Antes de fazer uma leitura profunda do código (o que consome tempo e tokens), os prompts deste toolkit primeiro fazem uma varredura leve, perguntam qual o escopo desejado (tudo, um módulo, uma função ou um campo específico) e onde o resultado deve ser salvo. Isso evita análises caras e desnecessárias quando só uma parte pequena do repositório precisava ser investigada, e transforma "não sair do foco" em uma confirmação explícita — não em uma suposição.

## 7. Limitações técnicas dos Gates de IA

Os "Approval Gates" e regras deste toolkit (incluindo o arquivo `AGENTS.md`) dependem de **Prompt Engineering** (obediência do modelo de linguagem às instruções fornecidas). Em execuções agênticas autônomas sem supervisão humana constante (como loops do Claude Code ou Cursor em modo autônomo), a IA pode eventualmente burlar ou ignorar essas diretivas se houver estouro de contexto ou instruções de sistema sobrepostas. Portanto, os gates funcionam como diretrizes comportamentais fortes, mas não substituem proteções físicas de infraestrutura (como permissões de escrita em branches protegidos e testes de CI).


## 8. Deterministic-first, AI-second

Sempre que uma verificação puder ser feita de forma objetiva e reproduzível por uma ferramenta adequada, prefira gerar essa evidência antes de consumir contexto de uma LLM.

A ferramenta determinística deve localizar e medir candidatos. A IA entra depois para interpretar contexto, investigar falsos positivos, relacionar o achado à arquitetura e explicar riscos.

Isso não significa confiar cegamente em análise estática. O resultado automatizado continua sendo evidência a validar, especialmente diante de chamadas dinâmicas, reflexão, geração de código, configurações externas e fronteiras entre sistemas.

Em resumo: **máquinas medem primeiro; modelos interpretam depois; pessoas decidem por último.**
