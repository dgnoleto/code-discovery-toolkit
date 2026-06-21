# 🔎 Code Discovery Toolkit

Um jeito estruturado de entender repositórios de código esquecidos e investigar código morto, duplicado ou redundante — sem inventar suposições, sem refatorar sem autorização e sem perder o foco do que foi pedido.

## Nunca viu nada parecido? Comece aqui

Se você chegou nesse repositório e pensou "eu nem sei por onde começar", relaxa — você não precisa saber programar pra usar a parte principal disso. São só 4 passos:

1. Abra a pasta [`prompts/`](prompts/) e clique no arquivo `01-mapeamento-inicial.md`.
2. Copie o texto que está dentro do bloco cinza (o "código").
3. Cole esse texto numa conversa com uma IA (Claude, ChatGPT, etc.), junto com informações do repositório que você quer entender — pode ser o README dele, ou até um print da estrutura de pastas.
4. Siga a conversa. A própria IA vai te perguntar o que você quer investigar (tudo, ou só uma parte) e onde quer salvar o resultado.

Depois desse primeiro contato, vale ler o resto deste README com mais calma pra entender a lógica completa.

## Pra quem é isso

- Você é PM/PO e te pediram pra entender um sistema antigo que ninguém mais lembra o que faz? É pra você.
- Você é dev e quer investigar um repositório legado sem o risco de alguém (ou alguma IA) sair refatorando por engano? Também é pra você.

Nenhuma das duas situações exige saber git, GitHub ou programação — isso só entra em jogo se você quiser usar o script de automação (`scripts/`), que é opcional.

## O problema

Toda empresa tem aquele repositório que ninguém lembra exatamente o que faz, ou aquele código que parece morto, duplicado ou redundante, mas que ninguém tem coragem de tocar porque "e se quebrar alguma coisa?". Esse toolkit existe para dar estrutura a esse tipo de investigação — feita por uma pessoa, por um time, ou com ajuda de um assistente de IA.

## De onde isso vem

Esse toolkit não nasceu de um exercício teórico. Ele resume uma prática real de discovery técnico assistido por IA aplicada em ecossistemas de produto B2B complexos: uso de frameworks de arquitetura de decisão para impedir refatorações automatizadas não autorizadas, mapeamento de dependências em sistemas legados sem histórico ativo, e recuperação de regras de negócio críticas documentadas do zero. A diferença aqui é que o processo foi generalizado e organizado para qualquer time poder aplicar, sem expor nenhum dado específico de cliente, projeto ou empresa.

## O que tem aqui

| Pasta | Conteúdo | Precisa saber programar? |
|---|---|---|
| `prompts/` | Textos prontos para colar numa IA e conduzir o discovery | Não |
| `docs/` | O passo a passo completo e os princípios do processo | Não |
| `templates/` | Quatro templates: mapeamento, código morto, duplicações, e o relatório final que junta os três | Não |
| `examples/` | Um exemplo real de relatório gerado pelo script | Não |
| `scripts/` | Um programa em Python que automatiza parte da varredura | Sim (opcional) |

## Princípios não negociáveis

- **Não inventar** — toda conclusão precisa de evidência (código, commit, histórico, ou confirmação humana).
- **Não refatorar sem autorização** — o objetivo é mapear e investigar, não corrigir.
- **Não sair do foco** — cada rodada de discovery tem escopo definido; achados fora dele vão para "uma próxima rodada", não para investigação imediata.

Detalhes completos em [`docs/principios.md`](docs/principios.md).

## Como usar (passo a passo completo)

1. Leia o passo a passo em [`docs/metodologia.md`](docs/metodologia.md).
2. Se alguém do seu time souber programar, pode rodar o script de varredura (somente leitura, sem dependências externas — só Python 3.8+):
   ```bash
   python scripts/analisar_repositorio.py /caminho/do/repositorio --saida relatorio-discovery.md
   ```
3. Use os prompts em [`prompts/`](prompts/) para investigar com mais profundidade — com ou sem a saída do script. Cada prompt primeiro faz uma leitura leve, depois pergunta o escopo desejado (tudo, um módulo, uma função ou um campo) e onde salvar o resultado, antes de aprofundar. Isso evita gastar tempo (e tokens, se estiver usando IA) analisando mais do que você realmente precisa.
4. Cada prompt te aponta pro template certo: [`01-mapeamento-template.md`](templates/01-mapeamento-template.md), [`02-codigo-morto-template.md`](templates/02-codigo-morto-template.md) e [`03-duplicacoes-template.md`](templates/03-duplicacoes-template.md). Preencha o template correspondente com os achados de cada etapa.
5. Use o prompt [`04-relatorio-final.md`](prompts/04-relatorio-final.md) pra juntar os três templates preenchidos no [`04-relatorio-final-template.md`](templates/04-relatorio-final-template.md).
6. Apresente o relatório para o time decidir os próximos passos — esse toolkit nunca decide por você.

Veja um exemplo real de saída em [`examples/relatorio-exemplo.md`](examples/relatorio-exemplo.md), gerado rodando o próprio script neste repositório.

## Glossário rápido

- **Discovery**: o processo de investigar e entender algo — nesse caso, um repositório de código — antes de decidir o que fazer com ele.
- **Código morto**: trecho de código que parece não ser mais usado por nada no sistema.
- **Escopo**: o tamanho do que está sendo investigado — pode ser o repositório inteiro, um módulo, uma função ou um campo específico.
- **Heurística**: uma regra prática que indica uma possibilidade, mas não garante 100%. Por isso todo achado aqui é tratado como candidato, nunca como verdade absoluta.
- **Repositório**: a "pasta" onde o código de um sistema fica guardado e versionado (nesse caso, no GitHub).

## Limitações (de propósito)

Esse toolkit é feito de heurísticas, não de verdades absolutas. Ele aponta candidatos para investigação humana — nunca executa, apaga ou modifica nada automaticamente. Quanto mais contexto humano for adicionado durante o processo, melhor o resultado.

## Autor

Feito por **Danilo Nolêto**, Product Manager com prática em discovery técnico assistido por IA, governança de IA aplicada à engenharia de requisitos e recuperação de sistemas legados.
[LinkedIn](https://linkedin.com/in/danilog-noleto)

## Licença

MIT — veja [`LICENSE`](LICENSE).
