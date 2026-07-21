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

Se você usa Claude Code no dia a dia e quer essa metodologia de forma autônoma (sem copiar e colar prompt nenhum), veja o repositório irmão [Claude Code para PM/PO](https://github.com/SEU-USUARIO/claude-code-for-pm), que traz a mesma lógica como uma Skill real.

## O problema

Toda empresa tem aquele repositório que ninguém lembra exatamente o que faz, ou aquele código que parece morto, duplicado ou redundante, mas que ninguém tem coragem de tocar porque "e se quebrar alguma coisa?". Esse toolkit existe para dar estrutura a esse tipo de investigação — feita por uma pessoa, por um time, ou com ajuda de um assistente de IA.

## De onde isso vem

Esse toolkit não nasceu de um exercício teórico. Ele resume uma prática real de discovery técnico assistido por IA aplicada em ecossistemas de produto B2B complexos: uso de frameworks de arquitetura de decisão para impedir refatorações automatizadas não autorizadas, mapeamento de dependências em sistemas legados sem histórico ativo, e recuperação de regras de negócio críticas documentadas do zero. A diferença aqui é que o processo foi generalizado e organizado para qualquer time poder aplicar, sem expor nenhum dado específico de cliente, projeto ou empresa.

## O que tem aqui

| Pasta / Arquivo                          | Conteúdo                                                                                                                                                                | Precisa saber programar? |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| `prompts/`                               | Textos prontos para colar numa IA e conduzir o discovery e o Health Check (`05-health-check.md`)                                                                       | Não                      |
| `docs/`                                  | O passo a passo completo, [Glossário de IA & Arquitetura](docs/glossario.md), guia do Graphify (`graphify-guia.md`) e guia da [GitHub Action](docs/github-action-guia.md) | Não                      |
| `templates/`                             | Templates de relatórios e a [GitHub Action Reutilizável](templates/github-action-discovery.yml) para automação mensal                                                   | Não                      |
| `examples/`                              | Um exemplo real de relatório gerado pelo script                                                                                                                         | Não                      |
| `scripts/`                               | Um programa em Python que automatiza parte da varredura                                                                                                                 | Sim (opcional)           |
| `templates/AGENTS-discovery-template.md` | Template de `AGENTS.md` para colocar na raiz do repositório investigado — ativa o modo discovery/health check em ferramentas como Claude Code, Cursor, Copilot, etc.    | Não                      |

## Princípios não negociáveis

- **Não inventar** — toda conclusão precisa de evidência (código, commit, histórico, ou confirmação humana).
- **Não refatorar sem autorização** — o objetivo é mapear, auditar e recomendar, nunca alterar ou inflar o código de produção sem aprovação.
- **Não sair do foco** — cada rodada de discovery tem escopo definido; achados fora dele vão para "uma próxima rodada", não para investigação imediata.

Detalhes completos em [`docs/principios.md`](docs/principios.md).

## Como usar (passo a passo completo)

1. Leia o passo a passo em [`docs/metodologia.md`](docs/metodologia.md) e consulte o [`docs/glossario.md`](docs/glossario.md) para nivelar conceitos do time (de Júnior a CTO).
2. Para auditorias de saúde mais precisas e de baixo custo, recomenda-se gerar previamente o mapa de dependências [`graphify.md`](docs/graphify-guia.md) (via [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)). Isso proporciona uma **redução de 83% no consumo de tokens** e um **aumento de 93% na precisão** da análise.
3. Para automatizar a higiene mensal do seu projeto no GitHub, siga o [`docs/github-action-guia.md`](docs/github-action-guia.md) para copiar o template [`templates/github-action-discovery.yml`](templates/github-action-discovery.yml).
4. Se alguém do seu time souber programar, pode rodar o script de varredura local (somente leitura, sem dependências externas — só Python 3.8+):
   ```bash
   python scripts/analisar_repositorio.py /caminho/do/repositorio --saida relatorio-discovery.md
   ```
   > **Alternativa para equipes que usam Claude Code, Cursor ou Copilot:**
> 	Copie o [`templates/AGENTS-discovery-template.md`](templates/AGENTS-discovery-template.md) para a raiz do repositório que você quer investigar, renomeie para `AGENTS.md`, e abra o repositório na sua ferramenta. Ela vai carregar as regras automaticamente — sem precisar copiar e colar prompt nenhum.
5. Use os prompts em [`prompts/`](prompts/) para investigar com mais profundidade — incluindo o [`05-health-check.md`](prompts/05-health-check.md) para levantamento de bandeiras vermelhas (pontas soltas, redundâncias, inconsistências de tipo de dados e gargalos de escalabilidade).
6. Cada prompt te aponta pro template certo em [`templates/`](templates/). Preencha o template correspondente com os achados de cada etapa.
7. Use o prompt [`04-relatorio-final.md`](prompts/04-relatorio-final.md) pra juntar os templates no [`04-relatorio-final-template.md`](templates/04-relatorio-final-template.md).
8. Apresente o relatório para o time decidir os próximos passos — esse toolkit nunca decide por você e nunca aplica alterações no código automaticamente.

Veja um exemplo real de saída em [`examples/relatorio-exemplo.md`](examples/relatorio-exemplo.md), gerado rodando o próprio script neste repositório.

## Glossário & Conceitos

Consulte o documento completo em **[`docs/glossario.md`](docs/glossario.md)** para explicações didáticas sobre:
- **Conceitos de IA & Agentes**: LLM, RAG, Graphify, Chain-of-Verification (CoVE), Approval Gates, Human-in-the-Loop (HITL), Context Window, Análise Determinística vs Heurística, Read-Only Agent, MCP e AST.
- **Conceitos de Engenharia & Produto**: Discovery Técnico, Débito Técnico, Código Morto, Code Smells, Inconsistência de Tipos de Dados e Clean Code.

## Inspirações e referências

- [**Graphify-Labs/graphify**](https://github.com/Graphify-Labs/graphify) — inspirou a integração do mapa de dependências (`graphify.md`), reduzindo o consumo de tokens em 832% e aumentando a precisão da auditoria em 93%.
- [**llm-council**](https://github.com/karpathy/llm-council) (Andrej Karpathy) — inspirou a ideia de, em achados críticos, validar a conclusão cruzando respostas de mais de uma IA antes de tratá-la como confirmada, em vez de confiar numa única resposta.
-  [**agency-agents-app**](https://github.com/msitarzewski/agency-agents-app) — inspirou o template `AGENTS-discovery-template.md`: o formato AGENTS.md e o conceito de "Approval Gates" (gate humano obrigatório antes de qualquer ação de escrita) foram adaptados para criar uma terceira porta de entrada para a metodologia de discovery, compatível com qualquer ferramenta agêntica.

## Limitações (de propósito)

Esse toolkit é feito de heurísticas, não de verdades absolutas. Ele aponta candidatos para investigação humana — nunca executa, apaga ou modifica nada automaticamente. Quanto mais contexto humano for adicionado durante o processo, melhor o resultado.

## Autor

Feito por **Danilo Nolêto**, Product Manager com prática em discovery técnico assistido por IA, governança de IA aplicada à engenharia de requisitos e recuperação de sistemas legados.
[LinkedIn](https://linkedin.com/in/danilog-noleto)

## Licença

MIT — veja [`LICENSE`](LICENSE).
