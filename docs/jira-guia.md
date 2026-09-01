# Guia de Integração Nativa com o Jira (Atlassian)

Este guia ensina como integrar o **Code Discovery Toolkit** ao **Jira (Atlassian)** para que os relatórios de discovery e auditoria virem tickets de débito técnico automaticamente no projeto do seu time.

---

## 1. Como Funciona a Integração Nativa no Script Python

O script [`scripts/analisar_repositorio.py`](../scripts/analisar_repositorio.py) possui integração nativa com a API REST do Jira v3, utilizando exclusivamente bibliotecas padrão do Python (**zero dependências externas**).

### Parâmetros Suportados:
- `--jira-url`: URL da sua instância Jira (ex: `https://suaempresa.atlassian.net`).
- `--jira-email`: E-mail da sua conta de usuário no Jira.
- `--jira-token`: Token de API pessoal gerado no Atlassian.
- `--jira-project`: Chave do Projeto no Jira onde o ticket deve ser criado (ex: `PROD`, `DEBT`, `SAAS`).
- `--jira-issue-type`: (Opcional) Tipo de item a criar (padrão: `Task` ou `Bug`).

---

## 2. Como Gerar o API Token no Jira (Atlassian)

1. Acesse [id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens).
2. Clique em **Create API token**.
3. Dê um nome ao token (ex: `Code-Discovery-Toolkit`) e clique em **Create**.
4. Copie a chave gerada e guarde-a com segurança (ela será usada como `--jira-token`).

---

## 3. Exemplo de Execução Manual via Terminal

Você pode executar o script no seu computador e criar o ticket no Jira imediatamente com um único comando:

```bash
python scripts/analisar_repositorio.py /caminho/do/projeto \
  --saida relatorio.md \
  --dias 365 \
  --jira-url "https://minhaempresa.atlassian.net" \
  --jira-email "seu.email@empresa.com" \
  --jira-token "SEU_API_TOKEN_ATLASSIAN" \
  --jira-project "PROD"
```

Se houver achados de código parado ou duplicados no projeto, o script abrirá automaticamente uma Issue no Jira com a descrição do relatório e a tag `TechnicalDebt`.

---

## 4. Integração no GitHub Actions ou Azure Pipelines

Você também pode adicionar as credenciais do Jira nos segredos (*Secrets / Environment Variables*) do seu pipeline de CI/CD para automatizar a abertura de chamados no Jira mensalmente:

### No GitHub Actions (`.github/workflows/discovery-check.yml`):
```yaml
      - name: Executar Script de Discovery com envio ao Jira
        env:
          JIRA_TOKEN: ${{ secrets.JIRA_API_TOKEN }}
        run: |
          python scripts/analisar_repositorio.py ./ \
            --saida relatorio-discovery.md \
            --jira-url "https://minhaempresa.atlassian.net" \
            --jira-email "devsecops@empresa.com" \
            --jira-token "$JIRA_TOKEN" \
            --jira-project "DEBT"
```

---

## 💡 Boas Práticas de Gestão de Produto no Jira

- **Priorização no Backlog**: Ao receber uma Issue automática do Discovery no Jira, classifique-a sob a coluna **Technical Debt** do seu quadro Kanban/Scrum.
- **Vincular a Epics**: Associe o ticket a um Epic de "Modernização de Legado" ou "Higiene de Código".
- **Evite Ruído**: O script foi projetado para **não criar tickets no Jira** caso o repositório esteja limpo e sem achados pendentes.
