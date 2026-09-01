# Metodologia de Discovery de Repositórios Esquecidos

Use este guia para conduzir uma investigação estruturada em repositórios legados — especialmente aqueles com **zero documentação**. Siga esta sequência lógica para economizar tempo, evitar retrabalho e não estourar a janela de contexto das IAs.

---

## 📋 Antes de Começar

- **Defina o escopo**: qual repositório (ou módulo) e qual pergunta você está tentando responder.
- **Garanta acesso**: certifique-se de que tem acesso de leitura ao histórico completo (`git log`, PRs antigos, issues).
- **Alinhamento**: avise o time responsável (se existir) que esse levantamento está sendo feito para evitar ruídos de comunicação.

---

## 🚦 O Fluxo Sequencial de Discovery

```text
Levantamento Inicial ──> Atividade & Propósito ──> Gerar Graphify (Mapa) ──> Health Check ──> Código Morto/Duplicado ──> Validação ──> Relatório Final
```

---

## Etapa 1 — Levantamento Inicial & Mapeamento de Contexto

- Leia o README existente e qualquer documentação (mesmo que antiga ou desatualizada).
- **Mapeamento de Contexto de Negócio**: Colete ou preencha rapidamente os manuais mínimos de contexto (como `contexto-produto-template.md` e `contexto-arquitetura-template.md` em [`templates/`](../templates/)) para servir de RAG de produto. Veja o guia explicativo em [`docs/contexto-negocio-guia.md`](contexto-negocio-guia.md).
- Liste linguagens, frameworks e dependências principais do repositório.
- Identifique os principais contribuidores históricos e quando foi o último commit relevante.
- Use o prompt [`prompts/01-mapeamento-inicial.md`](../prompts/01-mapeamento-inicial.md) fornecendo a árvore do repositório e os manuais de contexto coletados. Registre no template [`templates/01-mapeamento-template.md`](../templates/01-mapeamento-template.md).


---

## Etapa 2 — Propósito Original & Análise de Atividade

- **Histórico**: olhe os primeiros commits e as primeiras versões do README para desvendar a intenção original do projeto.
- **Integração**: procure quem consome esse repositório hoje (outro microsserviço, um cron job, ou se está abandonado).
- **Varredura rápida**: execute o script local [`scripts/analisar_repositorio.py`](../scripts/analisar_repositorio.py) para identificar arquivos sem commits recentes, duplicados exatos e arquivos sem referências óbvias. Trate os resultados como *candidatos*, não conclusões.

---

## Etapa 3 — Geração do Grafo de Dependências (`graphify.md`)

Antes de analisar o código em detalhes ou fazer perguntas complexas para a IA, é crucial gerar o mapa topológico do projeto.
- Gere o arquivo `graphify.md` usando a ferramenta open-source [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) (veja o guia em [`docs/graphify-guia.md`](graphify-guia.md)).
- **Por que agora?**: O grafo de dependências resume a arquitetura em poucas linhas. Com base em testes reais do mercado, alimentar a IA com esse arquivo reduz o consumo médio de tokens em **82%** e eleva a precisão das análises de impacto de **~42% para 93%** (evitando alucinações), servindo de base sólida para as próximas etapas.

---

## Etapa 4 — Health Check e Prontidão de Escala (Auditoria de Saúde)

Com o mapa de dependências gerado na etapa anterior, você pode auditar a qualidade técnica do código de forma barata e precisa.
- Use o prompt [`prompts/05-health-check.md`](../prompts/05-health-check.md) (passando pelos gates de escopo: Função, Módulo ou Geral).
- Mapeie bandeiras vermelhas cruciais: pontas soltas (erros omitidos), redundâncias, inconsistências de tipo de dados (ex: `string` vs `int`) e alertas para estouro sob grande volume de dados.
- Consolide as recomendações (sempre consultivas, sem aplicar alterações) no template [`templates/05-health-check-template.md`](../templates/05-health-check-template.md).

---

## Etapa 5 — Investigação de Código Morto, Duplicado ou Redundante

Investigue os arquivos parados e suspeitos de abandono mapeados nas Etapas 2 e 3.
- Use os prompts [`prompts/02-codigo-morto.md`](../prompts/02-codigo-morto.md) e [`prompts/03-duplicacoes-redundancias.md`](../prompts/03-duplicacoes-redundancias.md) para analisar cada candidato.
- Registre os achados detalhadamente nos templates [`templates/02-codigo-morto-template.md`](../templates/02-codigo-morto-template.md) e [`templates/03-duplicacoes-template.md`](../templates/03-duplicacoes-template.md).

---

## Etapa 6 — Validação com o Time

- Reúna-se com os desenvolvedores responsáveis ou quem trabalhou no projeto.
- Valide as dúvidas geradas nas etapas anteriores: *"este código realmente não é mais usado?"*, *"esta conversão implícita de tipo de dado é intencional?"*, *"podemos limpar esta duplicação?"*.
- Nunca tome decisões de remoção ou refatoração sem esta validação humana.

---

## Etapa 7 — Relatório Final

- Use o prompt [`prompts/04-relatorio-final.md`](../prompts/04-relatorio-final.md) para compilar os templates preenchidos nas etapas anteriores.
- Consolide tudo no template [`templates/04-relatorio-final-template.md`](../templates/04-relatorio-final-template.md).

---

## ⚡ Automação Continuada & Governança Corporativa

Para evitar que a higiene de código seja um esforço isolado de uma única vez, integre o toolkit aos fluxos corporativos do seu time:
- **Nuvem & CI/CD**: Agende varreduras mensais no **GitHub Actions** ([`templates/github-action-discovery.yml`](../templates/github-action-discovery.yml)) ou no **Azure DevOps Pipelines** ([`templates/azure-pipelines-discovery.yml`](../templates/azure-pipelines-discovery.yml) / [`docs/azure-devops-guia.md`](azure-devops-guia.md)).
- **Gestão de Tarefas**: Direcione os achados de inatividade automaticamente para o **Jira (Atlassian)** ([`docs/jira-guia.md`](jira-guia.md)), **Azure Boards** ou **GitHub Issues**, transformando débitos técnicos em tarefas priorizáveis no backlog do time.

- Entregue o relatório final como recomendação técnica estruturada para embasar os próximos passos de planejamento ou refatoração do produto.
