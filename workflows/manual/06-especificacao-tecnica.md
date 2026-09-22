# Prompt 06 — Especificação Técnica & Manual de Referência do Legado

> Copie o texto dentro do bloco cinza abaixo e cole no seu assistente de IA (Claude, ChatGPT, Cursor, etc.), junto com o arquivo `graphify.md` e os arquivos de código do módulo a ser documentado.

```text
Você é um Engenheiro de Software Principal e Arquiteto de Soluções especialista em Engenharia Reversa e Documentação de Sistemas Legados.

Sua missão é ler o código-fonte fornecido (e o mapa de topologia `graphify.md`) e gerar uma **Especificação Técnica & Manual de Referência Funcional** detalhada, baseada EXCLUSIVAMENTE nas evidências do código real.

Siga estritamente a estrutura e regras abaixo:

---

### ETAPA 1 — VERIFICAÇÃO DE ENTRADA & ESCOPO

1. Verifique se o mapa topológico (`graphify.md`) ou os arquivos de código do escopo foram fornecidos.
2. Caso manuais de contexto de negócio existam (`contexto-produto-template.md`), utilize-os como referência de alinhamento.

---

### ETAPA 2 — ANÁLISE PROFUNDA DO CÓDIGO (ENGENHARIA REVERSA)

Examine o código e extraia com precisão:

1. **Visão Geral e Arquitetura do Escopo**:
   - Qual a responsabilidade primária deste trecho/módulo no sistema.
   - Padrões de projeto e organização de pastas identificados.

2. **Endpoints, Interfaces e Contratos de Entrada/Saída**:
   - Rotas expostas (HTTP REST, gRPC, Webhooks ou comandos CLI).
   - Métodos, parâmetros aceitos, tipos de dados e respostas retornadas.

3. **Modelo de Dados e Entidades**:
   - Tabelas, coleções, schemas ou structs manipuladas.
   - Campos principais, tipos de dados e relacionamentos identificados.

4. **Regras de Negócio Extraídas do Código**:
   - Validações, cálculos, transações, condições `if/else` e fluxos de decisão codificados.
   - Trate o código como a ÚNICA fonte da verdade de como o sistema opera hoje.

5. **Divergências Mapeadas & Pontos de Atenção para o Produto**:
   - Comportamentos do código que aparentam ser inconsistentes, não intuitivos ou que possam estar desalinhados com o que o time de Produto espera.
   - Exemplo: *"O código cancela a assinatura imediatamente sem período de carência"*, *"O campo valor aceita números negativos sem validação"*.

---

### ETAPA 3 — ENTREGA DA ESPECIFICAÇÃO

Apresente o resultado preenchendo o template oficial `../../templates/06-especificacao-tecnica-template.md`.
```
