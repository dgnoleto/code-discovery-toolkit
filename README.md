# Code Discovery Toolkit

**Discovery técnico de sistemas legados: do código pouco documentado a evidências para decisões de produto.**

Para PMs, POs, FDEs e equipes de engenharia que precisam entender um sistema antes de estimar uma mudança, priorizar débito técnico ou escrever uma especificação.

O toolkit combina um analisador Python, prompts de investigação e modelos de documentação. Os resultados ajudam a levantar perguntas e orientar a revisão com quem conhece o negócio.

## Veja primeiro

- [Demonstração local e interpretação dos achados](examples/demo/README.md): uma base fictícia, um comando e resultados conferíveis.
- [Exemplo de decisão de produto](examples/01-mapeamento-exemplo-preenchido.md): hipótese, evidência, alternativas e critério de aceite.
- [Metodologia](docs/metodologia.md): roteiro de investigação.

## Comece pelo analisador

Pré-requisitos: Python 3.11+; Git é necessário para consultar o histórico de commits. O analisador usa somente a biblioteca padrão do Python. Não precisa de chave de IA, Graphify ou acesso ao Jira para a análise local.

```bash
git clone https://github.com/dgnoleto/code-discovery-toolkit.git
cd code-discovery-toolkit
python scripts/analisar_repositorio.py examples/demo/src --saida relatorio-demo.md
```

Abra o relatório e compare com a [interpretação da demonstração](examples/demo/README.md). Grave relatórios fora da pasta analisada para não incluí-los na próxima varredura.

Para investigar outra base:

```bash
python scripts/analisar_repositorio.py /caminho/do/repositorio --saida relatorio-discovery.md --dias 365 --similaridade 0.90
```

A varredura lê os arquivos do alvo; o relatório é escrito no caminho de saída. Se esse caminho já existir, será sobrescrito. O envio ao Jira é opcional e cria uma issue quando há achados e os parâmetros de conexão são fornecidos.

## O que está implementado

| Parte | Como funciona | Limite |
|---|---|---|
| Duplicações exatas | Agrupa arquivos pelo hash SHA-256 | Igualdade de conteúdo não determina se a duplicação é desnecessária |
| Similaridade textual | Compara textos com `difflib.SequenceMatcher` | Não compara semântica; ignora textos acima de 250 KB e pares com diferença de tamanho superior a 20% |
| Inatividade | Consulta o último commit de cada arquivo com Git | Ausência de commits recentes não significa abandono |
| Possíveis arquivos não referenciados | Procura o nome-base como palavra inteira em outros arquivos de texto | Pode omitir usos dinâmicos ou externos e considerar comentários como referências |
| Relatório | Consolida candidatos em Markdown | Requer investigação e validação humana |
| Jira | Envia o relatório à API REST v3 | Precisa de credenciais e permissões; não evita issues duplicadas entre execuções |

O código está em [scripts/analisar_repositorio.py](scripts/analisar_repositorio.py). O analisador não executa o código investigado, não extrai uma árvore sintática e não produz um grafo de chamadas.

## Da investigação à decisão

1. **Defina a pergunta e o escopo.** Que mudança, risco ou dúvida de negócio precisa ser esclarecida?
2. **Reúna contexto.** Use os modelos de [produto](templates/contexto-produto-template.md) e [arquitetura](templates/contexto-arquitetura-template.md).
3. **Mapeie o comportamento.** Comece pelo [prompt de mapeamento](prompts/01-mapeamento-inicial.md) e confronte as respostas com os arquivos.
4. **Investigue os candidatos.** Use os prompts de [código morto](prompts/02-codigo-morto.md), [duplicações](prompts/03-duplicacoes-redundancias.md) e [health check](prompts/05-health-check.md).
5. **Documente a evidência.** Registre arquivo, símbolo ou linha, hipótese, impacto e dúvida aberta. O [modelo de especificação](templates/06-especificacao-tecnica-template.md) apoia essa consolidação.
6. **Decida com o time.** Compare alternativas, priorize pelo impacto e registre critérios de aceite antes de implementar.

Os prompts são instruções para um assistente de IA; sua execução depende da ferramenta e do contexto fornecido. Uma análise escrita não comprova correção, desempenho ou segurança em produção.

## Mapas de dependências e agentes

Um mapa de dependências pode ajudar a orientar a leitura. O [guia de Graphify](docs/graphify-guia.md) explica como tratar esse contexto externo e como medir seus efeitos. Ele não é requisito do script Python.

O [template de instruções para agentes](templates/AGENTS-discovery-template.md) orienta investigação e revisão humana. Adapte-o às instruções e permissões da ferramenta escolhida. Regras em Markdown não substituem controles de acesso ou isolamento do ambiente.

Para um pacote de skills específico do Claude Code, veja [Claude Code for PM](https://github.com/dgnoleto/claude-code-for-pm).

## Integrações e automação

- [Jira](docs/jira-guia.md): configuração do envio opcional de relatórios.
- [GitHub Actions](docs/github-action-guia.md): guia e template de execução.
- [Azure DevOps](docs/azure-devops-guia.md): guia e template de pipeline.

Os templates precisam ser adaptados e testados no ambiente de destino. Para rotinas recorrentes, revise credenciais, exposição de relatórios e prevenção de duplicações antes de ativar publicação automática.

## Validação e limitações

```bash
python -m pip install pytest
python -m pytest tests/ -q
```

A suíte inclui detecção de duplicações, filtros de diretórios, referências textuais e envio ao Jira com resposta simulada. Esses testes não demonstram integração real com um ambiente Jira nem precisão da análise por IA.

Não há benchmark reproduzível publicado aqui que sustente percentuais universais de economia de tokens ou acurácia. O [protocolo de comparação](docs/graphify-guia.md) separa consumo, qualidade e custo.

Para bases grandes, a comparação de pares e a leitura de arquivos em memória podem ser custosas. Comece por um módulo e valide o tempo e a memória consumidos.

## Estrutura e contribuição

- [prompts/](prompts/): roteiros de investigação.
- [templates/](templates/): modelos de relatório, contexto e automação.
- [examples/](examples/): demonstrações e exemplos didáticos.
- [docs/](docs/): metodologia, princípios, glossário e integrações.
- [scripts/](scripts/): analisador Python.
- [tests/](tests/): testes automatizados.

Ao relatar um problema, informe comando, versão do Python, comportamento esperado e exemplo mínimo sem dados privados. Sugestões devem explicar qual problema de investigação resolvem e como verificar o resultado.

## Autor e referências

**Danilo Nolêto** — produto, discovery técnico, integrações e IA aplicada.  
[Perfil](https://github.com/dgnoleto) · [LinkedIn](https://www.linkedin.com/in/danilog-noleto)

Referências e inspirações: [Graphify](https://github.com/Graphify-Labs/graphify), [llm-council](https://github.com/karpathy/llm-council) e [agency-agents-app](https://github.com/msitarzewski/agency-agents-app). As ferramentas externas têm instalação e manutenção próprias.

Licença MIT — [LICENSE](LICENSE).
