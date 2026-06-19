# 🔎 Code Discovery Toolkit

Um conjunto de guia, prompts e script para ajudar times de produto e desenvolvimento a investigar repositórios esquecidos — sem inventar suposições, sem refatorar sem autorização e sem perder o foco do que foi pedido.

## O problema

Toda empresa tem aquele repositório que ninguém lembra exatamente o que faz, ou aquele código que parece morto, duplicado ou redundante, mas que ninguém tem coragem de tocar porque "e se quebrar alguma coisa?". Esse toolkit existe para dar estrutura a esse tipo de investigação — feita por uma pessoa, por um time, ou com ajuda de um assistente de IA.

## O que tem aqui

| Pasta | Conteúdo |
|---|---|
| `docs/` | Metodologia passo a passo e os princípios (guardrails) do processo |
| `prompts/` | Prompts prontos para usar com qualquer assistente de IA durante o discovery |
| `scripts/` | Script Python somente leitura que levanta candidatos a duplicação, inatividade e código não referenciado |
| `templates/` | Template de relatório final para registrar os achados |
| `examples/` | Exemplo real de relatório gerado pelo script (rodado neste próprio repositório) |

## Princípios não negociáveis

- **Não inventar** — toda conclusão precisa de evidência (código, commit, histórico, ou confirmação humana).
- **Não refatorar sem autorização** — o objetivo é mapear e investigar, não corrigir.
- **Não sair do foco** — cada rodada de discovery tem escopo definido; achados fora dele vão para "uma próxima rodada", não para investigação imediata.

Detalhes completos em [`docs/principios.md`](docs/principios.md).

## Como usar

1. Leia o passo a passo em [`docs/metodologia.md`](docs/metodologia.md).
2. Rode o script de varredura (somente leitura, sem dependências externas — só Python 3.8+):
   ```bash
   python scripts/analisar_repositorio.py /caminho/do/repositorio --saida relatorio-discovery.md
   ```
3. Use os prompts em [`prompts/`](prompts/) para investigar os candidatos levantados com mais profundidade.
4. Preencha o [`templates/relatorio-discovery-template.md`](templates/relatorio-discovery-template.md) com os achados.
5. Apresente o relatório para o time decidir os próximos passos — esse toolkit nunca decide por você.

Veja um exemplo real de saída em [`examples/relatorio-exemplo.md`](examples/relatorio-exemplo.md), gerado rodando o próprio script neste repositório.

## Limitações (de propósito)

Esse toolkit é feito de heurísticas, não de verdades absolutas. Ele aponta candidatos para investigação humana — nunca executa, apaga ou modifica nada automaticamente. Quanto mais contexto humano for adicionado durante o processo, melhor o resultado.

## Licença

MIT — veja [`LICENSE`](LICENSE).
