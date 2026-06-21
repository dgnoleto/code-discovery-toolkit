# Prompt — Compilação do Relatório Final

Use este prompt para organizar os achados preenchidos em `01-mapeamento-template.md`, `02-codigo-morto-template.md` e `03-duplicacoes-template.md` num relatório final único. Como essa etapa não lê o código de novo (só compila o que já foi levantado), ela não pede confirmação de escopo — só confirma onde salvar o relatório final.

```
Você vai me ajudar a organizar os achados de um discovery em um relatório final, usando a estrutura do template em templates/04-relatorio-final-template.md.

Contexto: [cole aqui os templates já preenchidos nas etapas anteriores: mapeamento (01), candidatos a código morto (02), duplicações (03)]

ETAPA 1 — Local de saída
Antes de gerar o relatório, sugira um caminho/nome de arquivo padrão (ex: discovery/AAAA-MM-DD-relatorio-final-[escopo].md) e me pergunte se confirmo ou prefiro outro. Espere minha confirmação antes de gerar o conteúdo final.

ETAPA 2 — Compilação (só depois da etapa acima)
Regras importantes:
- Separe os achados em três categorias: confirmado (evidência clara), provável (heurística forte mas sem confirmação humana), hipótese (precisa de validação).
- Não inclua recomendações de ação além de "investigar", "validar com o time" ou "confirmar antes de qualquer mudança". Você não está autorizado a recomendar remoção ou refatoração definitiva.
- Mantenha o relatório dentro do escopo que foi definido nas etapas anteriores. Se achar algo fora do escopo, liste em uma seção separada de "achados fora do escopo, para outra rodada".

Organize tudo no formato do template e me devolva o relatório completo.
```
