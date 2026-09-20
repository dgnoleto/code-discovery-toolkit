# Demonstração local: duplicação não é decisão de remoção

Esta base é fictícia e foi criada para demonstrar o analisador. Não contém código de cliente.

## Execute

Na raiz do Code Discovery Toolkit:

```bash
python scripts/analisar_repositorio.py examples/demo/src --saida relatorio-demo.md
```

Não precisa de IA, Graphify ou credenciais. O relatório será criado na raiz, fora da base analisada.

## Confira os arquivos

- [pricing_rules.py](src/pricing_rules.py): regra simplificada de desconto.
- [pricing_backup.py](src/pricing_backup.py): cópia exata para demonstrar a detecção.
- [checkout_entry.py](src/checkout_entry.py): ponto de entrada que importa a regra.

## O que esperar

| Sinal | Por que aparece | Interpretação |
|---|---|---|
| Duplicação exata entre pricing_rules.py e pricing_backup.py | Conteúdo idêntico, mesmo hash | Investigar por que a cópia existe |
| Nenhuma duplicação parcial | O par idêntico é excluído dessa comparação | As duas seções medem coisas diferentes |
| pricing_backup.py possivelmente não referenciado | Seu nome não aparece nos outros arquivos da base | Candidato a revisão |
| checkout_entry.py possivelmente não referenciado | É um ponto de entrada, chamado externamente | Ausência de referência interna não prova código morto |
| pricing_rules.py não aparece como não referenciado | O ponto de entrada o importa | A heurística encontrou uma referência textual |

A seção de inatividade depende do histórico Git e da data de execução; não tem resultado fixo nesta demonstração. Ordem dos itens e data do relatório podem variar.

## Uma decisão de produto possível

**Pergunta:** podemos simplificar o módulo de preço antes de adicionar outra regra de desconto?

**Observação:** existem dois arquivos idênticos, mas apenas um é importado pelo ponto de entrada incluído.

**Incerteza:** a varredura não conhece agendamentos, consumidores externos ou execução manual da cópia.

**Decisão proposta:** confirmar os consumidores antes de abrir uma tarefa de remoção. Preservar o ponto de entrada, mesmo que ele apareça como não referenciado.

**Critério de aceite para uma futura alteração:** cenários de desconto continuam válidos e os consumidores conhecidos apontam para a implementação mantida.

Essa é uma interpretação didática. O analisador não remove arquivos nem confirma a intenção de negócio.
