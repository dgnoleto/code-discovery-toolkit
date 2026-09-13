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
Gerar Graphify (Mapa Topológico) ──> Mapeamento & Propósito ──> Health Check ──> Especificação Técnica ──> Código Morto/Duplicado ──> Relatório & Backlog
```

---

## Etapa 1 — Geração do Grafo de Dependências (`graphify.md`)

Antes de qualquer análise de código ou pergunta complexa para a IA, o primeiro passo é gerar o mapa topológico do projeto.
- Gere o arquivo `graphify.md` usando a ferramenta open-source [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) (veja o guia em [`docs/graphify-guia.md`](graphify-guia.md)).
- **Por que este é o Passo 1?**: O grafo de dependências resume a arquitetura do projeto em poucas linhas. Com base em testes reais do mercado, alimentar a IA com esse arquivo reduz o consumo médio de tokens em **82%** e eleva a precisão das análises de impacto de **~42% para 93%** (evitando alucinações), servindo de base sólida para todas as etapas seguintes.

---

## Etapa 2 — Mapeamento Arquitetural & Propósito

Com o mapa topológico `graphify.md` em mãos:
- Colete ou preencha rapidamente os manuais mínimos de contexto de negócio (`contexto-produto-template.md` e `contexto-arquitetura-template.md` em [`templates/`](../templates/)) para servir de RAG de produto. Veja o guia explicativo em [`docs/contexto-negocio-guia.md`](contexto-negocio-guia.md).
- Use o prompt [`prompts/01-mapeamento-inicial.md`](../prompts/01-mapeamento-inicial.md) fornecendo o `graphify.md` e os manuais de contexto coletados.
- Registre os achados estruturados no template [`templates/01-mapeamento-template.md`](../templates/01-mapeamento-template.md).

---

## Etapa 3 — Health Check e Auditoria de Saúde

Com o mapa de dependências e a arquitetura compreendida:
- Use o prompt [`prompts/05-health-check.md`](../prompts/05-health-check.md) (passando pelos gates de escopo: Função, Módulo ou Geral).
- Mapeie bandeiras vermelhas cruciais: pontas soltas (erros omitidos), redundâncias, inconsistências de tipo de dados (ex: `string` vs `int`) e alertas para estouro sob grande volume de dados.
- Consolide as recomendações (sempre consultivas, sem aplicar alterações) no template [`templates/05-health-check-template.md`](../templates/05-health-check-template.md).

---

## Etapa 4 — Especificação Técnica & Manual do Legado (Code-Derived Spec)

Em sistemas sem documentação, o código é a única fonte da verdade. Esta etapa gera o Manual Técnico do sistema:
- Use o prompt [`prompts/06-especificacao-tecnica.md`](../prompts/06-especificacao-tecnica.md) para realizar a engenharia reversa do módulo.
- Extraia rotas/interfaces, schemas de dados, regras de negócio codificadas e **mapeie divergências entre o comportamento real do código e a intenção de produto**.
- Registre no template [`templates/06-especificacao-tecnica-template.md`](../templates/06-especificacao-tecnica-template.md) para validação entre Engenharia e Produto.

---

## Etapa 5 — Investigação de Código Morto, Duplicado ou Redundante

Varra lógicas obsoletas e redundâncias no projeto:
- Execute o script local [`scripts/analisar_repositorio.py`](../scripts/analisar_repositorio.py) para identificar arquivos sem commits recentes, duplicados exatos/similares e arquivos não referenciados.
- Use os prompts [`prompts/02-codigo-morto.md`](../prompts/02-codigo-morto.md) e [`prompts/03-duplicacoes-redundancias.md`](../prompts/03-duplicacoes-redundancias.md) para analisar cada candidato.
- Registre no template [`templates/02-codigo-morto-template.md`](../templates/02-codigo-morto-template.md) e [`templates/03-duplicacoes-template.md`](../templates/03-duplicacoes-template.md).

---

## Etapa 6 — Relatório Final & Governança Corporativa

- Use o prompt [`prompts/04-relatorio-final.md`](../prompts/04-relatorio-final.md) para compilar os achados estratégicos no template [`templates/04-relatorio-final-template.md`](../templates/04-relatorio-final-template.md).
- **Automação de Backlog**: Envie os débitos técnicos e divergências identificadas para o **Jira (Atlassian)** ([`docs/jira-guia.md`](jira-guia.md)), **Azure Boards** ([`docs/azure-devops-guia.md`](azure-devops-guia.md)) ou **GitHub Issues**, priorizando-os no quadro do time.
