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
Definir escopo e reunir contexto ──> Mapeamento & Propósito ──> Health Check ──> Especificação Técnica ──> Código Morto/Duplicado ──> Relatório & Backlog
```

---

## Etapa 1 — Contexto e mapa de dependências opcional

Comece pela pergunta e pelo escopo. Um mapa de dependências pode ajudar a orientar a leitura, mas não é requisito do analisador Python.
- Se optar por um mapa, gere o arquivo `graphify.md` usando a ferramenta open-source [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) (veja o guia em [`docs/graphify-guia.md`](graphify-guia.md)).
- Confira a cobertura e a atualidade do mapa; valide cada relação relevante no código. Não atribua percentuais de eficiência ou precisão sem uma medição reproduzível.

---

## Etapa 2 — Mapeamento Arquitetural & Propósito

Com o contexto disponível, incluindo um mapa se houver:
- Colete ou preencha rapidamente os manuais mínimos de contexto de negócio (`contexto-produto-template.md` e `contexto-arquitetura-template.md` em [`templates/`](../templates/)) para servir de RAG de produto. Veja o guia explicativo em [`docs/contexto-negocio-guia.md`](contexto-negocio-guia.md).
- Use o prompt [`workflows/manual/01-mapeamento-inicial.md`](../workflows/manual/01-mapeamento-inicial.md) fornecendo os arquivos e os manuais de contexto disponíveis.
- Registre os achados estruturados no template [`templates/01-mapeamento-template.md`](../templates/01-mapeamento-template.md).

---

## Etapa 3 — Health Check e Auditoria de Saúde

Com o mapa de dependências e a arquitetura compreendida:
- Use o prompt [`workflows/manual/05-health-check.md`](../workflows/manual/05-health-check.md) (passando pelos gates de escopo: Função, Módulo ou Geral).
- Mapeie bandeiras vermelhas cruciais: pontas soltas (erros omitidos), redundâncias, inconsistências de tipo de dados (ex: `string` vs `int`) e alertas para estouro sob grande volume de dados.
- Consolide as recomendações (sempre consultivas, sem aplicar alterações) no template [`templates/05-health-check-template.md`](../templates/05-health-check-template.md).

---

## Etapa 4 — Especificação Técnica & Manual do Legado (Code-Derived Spec)

O código evidencia a implementação analisada, mas pode depender de configuração e serviços externos. Esta etapa documenta o comportamento observado e as lacunas:
- Use o prompt [`workflows/manual/06-especificacao-tecnica.md`](../workflows/manual/06-especificacao-tecnica.md) para realizar a engenharia reversa do módulo.
- Extraia rotas/interfaces, schemas de dados, regras de negócio codificadas e **mapeie divergências entre o comportamento real do código e a intenção de produto**.
- Registre no template [`templates/06-especificacao-tecnica-template.md`](../templates/06-especificacao-tecnica-template.md) para validação entre Engenharia e Produto.

---

## Etapa 5 — Investigação de Código Morto, Duplicado ou Redundante

Varra lógicas obsoletas e redundâncias no projeto:
- Execute o script local [`scripts/analisar_repositorio.py`](../scripts/analisar_repositorio.py) para identificar arquivos sem commits recentes, duplicados exatos/similares e arquivos não referenciados.
- Use os prompts [`workflows/manual/02-codigo-morto.md`](../workflows/manual/02-codigo-morto.md) e [`workflows/manual/03-duplicacoes-redundancias.md`](../workflows/manual/03-duplicacoes-redundancias.md) para analisar cada candidato.
- Registre no template [`templates/02-codigo-morto-template.md`](../templates/02-codigo-morto-template.md) e [`templates/03-duplicacoes-template.md`](../templates/03-duplicacoes-template.md).

---

## Etapa 6 — Relatório Final & Governança Corporativa

- Use o prompt [`workflows/manual/04-relatorio-final.md`](../workflows/manual/04-relatorio-final.md) para compilar os achados estratégicos no template [`templates/04-relatorio-final-template.md`](../templates/04-relatorio-final-template.md).
- **Automação de Backlog**: Envie os débitos técnicos e divergências identificadas para o **Jira (Atlassian)** ([`docs/jira-guia.md`](jira-guia.md)), **Azure Boards** ([`docs/azure-devops-guia.md`](azure-devops-guia.md)) ou **GitHub Issues**, priorizando-os no quadro do time.
