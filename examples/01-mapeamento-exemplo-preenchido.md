# Mapeamento inicial — demonstração de checkout

**Natureza:** exemplo didático, sem cliente ou resultado de produção.  
**Escopo:** os três arquivos de [demo/src](demo/src/).  
**Pergunta:** há duplicação que mereça investigação antes de evoluir a regra de desconto?

## Evidência disponível

| Evidência | Conclusão permitida | Limite |
|---|---|---|
| [pricing_rules.py](demo/src/pricing_rules.py) e [pricing_backup.py](demo/src/pricing_backup.py) têm o mesmo conteúdo | Existe duplicação exata | Não explica a necessidade da cópia |
| [checkout_entry.py](demo/src/checkout_entry.py) importa pricing_rules | Existe um consumidor nessa base | Não cobre consumidores externos |
| A cópia não é mencionada pelos outros arquivos | É candidata a investigação | Não comprova que pode ser excluída |

## Regra observada

A função `total_com_desconto` aplica um desconto inteiro de 10% em centavos quando o subtotal é pelo menos 10.000 centavos. Abaixo disso, retorna o subtotal original. A demonstração presume entradas inteiras não negativas; não modela impostos, frete ou validação de entrada.

## Alternativas

| Alternativa | Benefício | Risco ou custo |
|---|---|---|
| Manter as duas implementações | Evita mudança imediata | Regras podem divergir no futuro |
| Remover a cópia após mapear consumidores | Reduz manutenção duplicada | Exige evidência de que nenhum consumidor depende dela |
| Investigar uso externo primeiro | Reduz incerteza da decisão | Demanda consulta a execução, configuração ou responsáveis |

## Decisão proposta e critérios de aceite

Investigar consumidores externos antes de propor remoção. Não alterar a regra de desconto nessa rodada.

Uma futura tarefa deve indicar os consumidores verificados, a implementação mantida e testes nos limites da regra: 9.999, 10.000 e 10.001 centavos. O ponto de entrada deve continuar executável.

## Perguntas abertas

- A cópia tem algum consumidor fora desse escopo?
- O arredondamento do desconto está alinhado à política desejada?
- A regra deveria considerar outros descontos?

O exemplo mostra como transformar achados em perguntas e critérios de decisão. Não representa uma investigação concluída de um sistema real.
