# Guia de Configuração: GitHub Action de Discovery Continuado

Este guia ensina como integrar o **Code Discovery Toolkit** a qualquer repositório no GitHub para automatizar a varredura e higiene mensal de código parado ou duplicado.

---

## Como instalar em qualquer repositório no GitHub

### Passo 1: Copiar o arquivo de Workflow
1. No repositório onde deseja aplicar a varredura, crie a seguinte estrutura de pastas na raiz (caso ainda não exista):
   ```text
   .github/workflows/
   ```
2. Copie o arquivo [`templates/github-action-discovery.yml`](../templates/github-action-discovery.yml) deste toolkit para a pasta `.github/workflows/` do seu projeto. Você pode renomeá-lo para `discovery-check.yml`.
3. Garanta que o script `scripts/analisar_repositorio.py` também esteja presente na pasta `scripts/` do seu projeto (ou ajuste o caminho no arquivo `.yml`).

### Passo 2: Configurar Permissões no GitHub
Para que a Action consiga criar Issues automaticamente com os relatórios de achados:
1. No seu repositório do GitHub, vá em **Settings** > **Actions** > **General**.
2. Na seção **Workflow permissions**, selecione **Read and write permissions**.
3. Clique em **Save**.

---

## Como Funciona a Automação

* **Execução Agendada (Cron)**: O workflow roda automaticamente todo dia 1º de cada mês às 08:00 UTC.
* **Execução Manual (Workflow Dispatch)**: Você pode disparar a varredura a qualquer momento indo na aba **Actions** do seu repositório no GitHub, selecionando `Code Discovery & Hygiene Check` e clicando em **Run workflow**.
* **Resultados**: 
  - O relatório em Markdown é disponibilizado para download como um *Artifact* na execução da Action.
  - Uma Issue no GitHub é aberta automaticamente com o resumo dos arquivos sem commit há mais de 365 dias e candidatos a duplicação, pronta para o time revisar.

---

## Vantagens para o Time de Produto e Engenharia

- **Higiene Continuada**: Evita que o acúmulo de débito técnico e arquivos esquecidos vire uma bola de neve.
- **Visibilidade Passiva**: O time não precisa lembrar de rodar scripts locais; o relatório mensal chega ativamente como uma Issue no GitHub.
- **Zero Risco**: A Action opera 100% em modo somente leitura no código-fonte — ela gera relatórios e Issues, mas nunca altera nem remove nada do seu código.
