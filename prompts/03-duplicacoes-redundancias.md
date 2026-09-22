# Prompt — Validação de Duplicações e Redundâncias

Use este prompt preferencialmente **depois de uma análise determinística**. Para repositórios compatíveis, consulte [`docs/jscpd-guia.md`](../docs/jscpd-guia.md). A ferramenta encontra candidatos; a IA avalia contexto, falsos positivos e relevância.

O modo manual continua disponível quando não houver ferramenta adequada.

```
Você vai analisar candidatos a duplicação ou redundância.

Contexto: [cole aqui a saída do jscpd/outra ferramenta e, quando necessário, os trechos de código correspondentes]

PRINCÍPIO
A detecção automática indica similaridade. Ela não prova que os trechos devem ser unificados. Sua função é interpretar as evidências, não inventar novas duplicações sem suporte.

ETAPA 1 — Inventário das evidências
Liste os pares/grupos apontados pela ferramenta, incluindo arquivos, funções, linhas e métricas disponíveis. Se o contexto veio sem ferramenta determinística, deixe isso explícito.

ETAPA 2 — Confirmação de escopo
Pergunte:
"Quer que eu valide (a) todos os candidatos, ou (b) só um subconjunto específico?"

Se eu escolher um subconjunto, avise que duplicações fora dele não foram avaliadas. Espere minha resposta.

ETAPA 3 — Local de saída
Sugira um caminho padrão, por exemplo:
discovery/AAAA-MM-DD-duplicacoes-[escopo].md

Pergunte se confirmo ou prefiro outro destino. Espere minha confirmação.

ETAPA 4 — Análise contextual
Para cada candidato confirmado:
- valide se a similaridade representa de fato lógica duplicada/redundante;
- diferencie duplicação textual de duplicação semântica;
- procure sinais de duplicação intencional por isolamento de módulos, domínio, compatibilidade ou arquitetura;
- identifique falsos positivos;
- cite as ocorrências e a evidência que originou o candidato;
- não proponha automaticamente unificação ou refatoração;
- não altere código.

ETAPA 5 — Saída
Organize o resultado seguindo templates/03-duplicacoes-template.md.

Entregue uma lista de candidatos validados, falsos positivos e itens inconclusivos, com localização, evidência e breve justificativa.
```
