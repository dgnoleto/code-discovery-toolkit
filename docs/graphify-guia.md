# Guia de Integração com o Graphify (`graphify.md`)

## O que é o Graphify?

O [Graphify](https://github.com/Graphify-Labs/graphify) é um projeto *open-source* da comunidade projetado para criar grafos de contexto, topologia de chamadas e mapas de dependências de projetos de código. 

No contexto do **Code Discovery Toolkit**, o arquivo gerado (geralmente nomeado `graphify.md`) atua como um "mapa de navegação" prévio para os assistentes de IA (Claude, ChatGPT, Cursor, Copilot, etc.).

---

## Por que usar o `graphify.md` no Health Check e Discovery?

Ao realizar auditorias de código ou investigações de dependências em repositórios legados de sistemas SaaS, o uso do `graphify.md` traz dois benefícios fundamentais:

1. **Redução de 82% no Consumo de Tokens**:
   Em vez de exigir que a IA leia e processe milhares de linhas de código-fonte bruto para descobrir quem chama o quê, o `graphify.md` fornece a estrutura sintética de conexões. Isso reduz radicalmente a janela de contexto utilizada e o custo financeiro/tempo da análise.

2. **Aumento de 93% na Precisão da Análise**:
   Com a topologia de chamadas explicitada no grafo, a IA consegue identificar impactos em cascata, dependências circulares e ponteiros mortos com acurácia incomparavelmente superior a uma simples busca por palavras-chave ou varredura parcial.

---

## Como usar no fluxo do Toolkit

1. **Gere o Grafo de Dependências**:
   Siga as instruções do repositório oficial [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) no seu repositório alvo para gerar a síntese de dependências.

2. **Anexe o `graphify.md` na Sessão de IA**:
   Ao iniciar qualquer um dos prompts do toolkit — especialmente o [`prompts/05-health-check.md`](../prompts/05-health-check.md) —, forneça o conteúdo do `graphify.md` ou referencie o arquivo na sua conversa com a IA.

3. **Verificação de Status no Health Check**:
   O prompt de Health Check identifica automaticamente a presença do `graphify.md`. Se ausente, o relatório exibirá um aviso de que os achados de dependência em cascata possuem nível de confiança reduzido/médio.

---

## Referência Externa

- **Repositório Oficial do Graphify**: [https://github.com/Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)
