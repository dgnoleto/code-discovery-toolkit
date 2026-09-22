# jscpd — Guia de análise determinística de duplicações

O Code Discovery Toolkit adota o princípio **deterministic-first, AI-second**: quando uma ferramenta consegue detectar evidências objetivas de forma reproduzível, ela deve fazer a primeira varredura. A IA entra depois para interpretar contexto, revisar falsos positivos e produzir recomendações.

## Por que usar jscpd?

O [jscpd](https://github.com/kucherenko/jscpd) detecta blocos de código duplicados sem exigir que uma LLM leia e compare o repositório inteiro. Isso reduz o contexto enviado à IA e separa duas responsabilidades:

1. **Detecção:** ferramenta determinística encontra candidatos.
2. **Interpretação:** IA avalia se a duplicação é relevante, intencional ou um falso positivo.

O jscpd é opcional. Se ele não estiver disponível, o prompt manual continua funcionando.

## Execução rápida

Com Node.js disponível, execute na raiz do repositório analisado:

```bash
npx jscpd .
```

Para gerar uma saída estruturada que possa ser reaproveitada por scripts ou agentes:

```bash
npx jscpd . --reporters json
```

Consulte a documentação oficial do jscpd para opções de linguagem, exclusões, limites e reporters disponíveis na versão instalada.

## Fluxo recomendado

```text
repositório
    ↓
jscpd
    ↓
candidatos a duplicação
    ↓
../manual/03-duplicacoes-redundancias.md
    ↓
validação contextual pela IA
    ↓
../../templates/03-duplicacoes-template.md
    ↓
validação humana
```

A saída da ferramenta é **evidência de similaridade**, não autorização para refatorar.

Antes de recomendar qualquer ação, verifique contexto arquitetural, responsabilidade dos módulos, histórico disponível e possibilidade de duplicação intencional.

## Falsos positivos

Casos comuns que merecem revisão humana ou contextual:

- estruturas repetidas exigidas por frameworks;
- código semelhante em módulos deliberadamente isolados;
- arquivos gerados;
- testes e fixtures;
- migrations;
- código vendorizado ou dependências incorporadas.

Configure exclusões no jscpd quando esses arquivos produzirem ruído recorrente.

## Código morto

Ferramentas determinísticas também podem fornecer candidatos a código morto dependendo da linguagem e do ecossistema. O mesmo princípio vale: use a ferramenta para gerar evidências e o prompt `../manual/02-codigo-morto.md` para avaliar contexto e risco.

Nenhum resultado automatizado deve ser tratado isoladamente como prova de que um trecho pode ser removido.
