# Prompt — Identificação de Candidatos a Código Morto

```
Você vai analisar trechos de código que vou te fornecer para levantar candidatos a código morto (código que não é mais executado ou utilizado).

Contexto: [cole aqui os arquivos relevantes, ou a saída do script scripts/analisar_repositorio.py]

Regras importantes:
- Trate tudo como CANDIDATO, nunca como conclusão definitiva. Você não tem visibilidade total do sistema (pode haver chamadas dinâmicas, jobs externos, etc).
- Para cada candidato, cite o arquivo e, se possível, a linha ou função específica.
- Indique o nível de confiança: alto (ex: função nunca referenciada em nenhum lugar do código fornecido), médio, ou baixo (ex: parece sem uso, mas pode ser chamada externamente).
- Não sugira remover ou apagar nada. Não escreva código de refatoração.
- Se não tiver certeza, diga isso explicitamente em vez de arriscar um palpite.

Me entregue uma lista de candidatos com: localização, motivo da suspeita e nível de confiança.
```
