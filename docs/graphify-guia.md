# Mapas de dependências e Graphify

Um mapa de dependências pode orientar a navegação por uma base de código. Neste toolkit, `graphify.md` é uma convenção para fornecer esse contexto ao assistente; não é requisito do analisador Python.

O [Graphify](https://github.com/Graphify-Labs/graphify) é uma referência externa. Consulte o projeto para instalação, formatos de saída e compatibilidade. O toolkit não instala nem executa essa ferramenta.

## Como usar um mapa na investigação

1. Registre a ferramenta, versão, data e commit da base usada para gerar o mapa.
2. Confira se a exportação cobre as linguagens e os módulos de interesse.
3. Forneça o mapa junto à pergunta de negócio e ao escopo da análise.
4. Use o mapa para localizar candidatos; confirme relações nos arquivos e, quando necessário, com execução e responsáveis pelo sistema.
5. Registre dependências externas, carregamentos dinâmicos e outras lacunas que o mapa não represente.

Sem mapa, investigue referências e imports diretamente. Sua ausência não determina uma nota fixa de confiança; a confiança deve depender da evidência de cada achado. Um mapa desatualizado também pode induzir conclusões incorretas.

## Como avaliar o efeito do contexto

Este repositório não publica um benchmark reproduzível que sustente os percentuais de economia ou precisão anteriormente mencionados. Para medir no seu cenário:

- Fixe um commit, um conjunto de perguntas e respostas esperadas revisadas por alguém que conheça a base.
- Execute as mesmas perguntas com e sem mapa, em sessões independentes, usando o mesmo modelo, versão, configuração e acesso a ferramentas.
- Registre entrada, saída, tokens de cache quando disponíveis, tempo e custo real separadamente.
- Avalie afirmações corretas, incorretas, omissões e referências verificáveis. Defina o denominador de cada métrica antes da comparação.
- Repita as rodadas para observar variação. Registre falhas e resultados desfavoráveis.
- Publique prompts, saídas e método em uma base que possa ser compartilhada.

| Campo | Registro |
|---|---|
| Base e commit | Identificação da amostra |
| Pergunta e resposta de referência | Definidas antes da execução |
| Modelo e configuração | Incluindo acesso a ferramentas |
| Condição | Com mapa / sem mapa |
| Qualidade | Corretas, incorretas, omissões e referências |
| Consumo | Tokens de entrada, saída e cache separadamente |
| Tempo e custo | Medidos, sem converter tokens diretamente em ganho financeiro |
| Limitações | Cobertura, tamanho da amostra e variação entre rodadas |

Economia de tokens não implica melhoria de qualidade. Os resultados de uma base não garantem o mesmo efeito em outras.

Veja também o [prompt de health check](../prompts/05-health-check.md).
