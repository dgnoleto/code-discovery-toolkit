# Prompt — Validação de Candidatos a Código Morto

Use este prompt para **interpretar evidências** de possível código morto. Sempre que houver uma ferramenta estática/determinística adequada à linguagem, prefira usá-la na primeira varredura e entregue os candidatos à IA. A IA deve focar contexto, risco e falsos positivos.

```
Você vai analisar candidatos a código morto (código que aparentemente não é mais executado ou utilizado).

Contexto: [cole aqui a saída de uma ferramenta estática/determinística, de scripts/analisar_repositorio.py, ou os arquivos relevantes]

PRINCÍPIO
Não use raciocínio probabilístico para substituir evidências que podem ser verificadas deterministicamente. Quando receber resultados de ferramentas, trate-os como candidatos, não como conclusão definitiva.

ETAPA 1 — Inventário de evidências
Liste os candidatos recebidos e identifique a origem de cada evidência (ferramenta, script ou inspeção manual). Não conclua ainda que o código está morto.

ETAPA 2 — Confirmação de escopo
Pergunte:
"Quer que eu investigue (a) todos os candidatos dessa lista, ou (b) só um subconjunto específico?"

Se eu escolher um subconjunto, avise que os demais itens não foram avaliados e não devem ser considerados seguros ou problemáticos por exclusão. Espere minha resposta.

ETAPA 3 — Local de saída
Depois que eu confirmar o escopo, sugira um caminho padrão, por exemplo:
discovery/AAAA-MM-DD-codigo-morto-[escopo].md

Pergunte se confirmo ou prefiro outro destino. Espere minha confirmação.

ETAPA 4 — Validação contextual
Para cada candidato confirmado:
- procure referências, imports, entry points e usos visíveis no contexto disponível;
- considere chamadas dinâmicas, reflexão, jobs externos, configurações e integrações;
- diferencie "não encontrei uso" de "comprovadamente não existe uso";
- cite arquivo e, quando possível, linha/função;
- indique confiança: alta, média ou baixa;
- identifique possíveis falsos positivos;
- não remova, altere ou refatore código.

ETAPA 5 — Saída
Organize o resultado seguindo templates/02-codigo-morto-template.md.

Entregue: localização, evidência de origem, motivo da suspeita, possíveis falsos positivos e nível de confiança.
```
