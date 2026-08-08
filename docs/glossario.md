# Glossário de IA, Discovery Técnico & Arquitetura

Este glossário explica em linguagem didática e acessível todos os conceitos utilizados neste repositório — desde os termos explícitos do dia a dia até os **conceitos avançados de Inteligência Artificial e Arquitetura que estão implícitos no funcionamento do toolkit**.

---

## 🤖 1. Conceitos de Inteligência Artificial & Engenharia Agêntica

estos conceitos explicam como as IAs modernas (ChatGPT, Claude, Cursor, Copilot) funcionam e por que este toolkit impõe regras rígidas para garantir acurácia e segurança.

### **LLM (Large Language Model / Modelo de Linguagem de Grande Porte)**
* **O que é**: O "cérebro" de IAs como Claude e ChatGPT, treinado em bilhões de textos para entender e gerar linguagem humana e código.
* **No Toolkit**: As LLMs ajudam no discovery, mas sem instrução clara podem "alucinar" (inventar coisas) ou tentar "corrigir" códigos sem permissão.

### **Chain-of-Verification (CoVE / Cadeia de Verificação)** *(Implícito)*
* **O que é**: Uma técnica avançada de prompting onde a IA é forçada a checar e tentar refutar suas próprias hipóteses antes de emitir um diagnóstico final.
* **No Toolkit**: Quando o toolkit exige que a IA aponte `arquivo:linha` e traga evidências para cada achado (separando em *Confirmado*, *Provável* e *Hipótese*), estamos aplicando o princípio do CoVE para eliminar respostas enganosas.

### **Approval Gates (Gates Humanos de Aprovação)** *(Implícito)*
* **O que é**: Pontos de parada obrigatórios em um fluxo de trabalho agêntico onde a IA é proibida de avançar sem a autorização explícita de um humano.
* **No Toolkit**: Presente no `AGENTS.md` e em todos os prompts. A IA faz uma varredura leve, para e pergunta o escopo. Ela apresenta o resumo, para e pede confirmação antes de gerar o relatório.

### **Human-in-the-Loop (HITL / Humano no Controle)** *(Implícito)*
* **O que é**: Filosofia de design onde sistemas de IA operam como assistentes consultivos, mantendo o ser humano responsável pelas decisões finais e modificações do sistema.
* **No Toolkit**: O toolkit nunca apaga, refatora ou move arquivos por conta própria. Todas as saídas são candidatas para validação humana.

### **RAG (Retrieval-Augmented Generation / Geração Aumentada por Recuperação)**
* **O que é**: A prática de alimentar a IA com arquivos, documentações ou contextos locais antes de fazer uma pergunta, em vez de depender apenas da memória pré-treinada da IA.
* **No Toolkit**: Ao copiar a estrutura do repositório, relatórios ou o `graphify.md` para o chat da IA, você está realizando RAG manual.

### **Graphify & Topologia de Contexto**
* **O que é**: Técnica de mapeamento que converte o código-fonte em um grafo sintético de dependências entre chamadas e arquivos (baseado em [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)).
* **No Toolkit**: Anexar o `graphify.md` permite que a IA entenda a relação estrutural do código. Benchmarks empíricos em projetos legados reais do mercado apontam uma **redução média de 82% no volume de tokens** na conversa e uma **melhoria da precisão de ~42% para 93%** nas análises de cascata de impacto.


### **Janela de Contexto (Context Window) & Token Limits**
* **O que é**: A "memória de trabalho" máxima que uma IA consegue ler de uma só vez. Cada palavra ou trecho de código consumido conta como "tokens".
* **No Toolkit**: Prompts e ferramentas do toolkit foram otimizados com "varreduras leves" para não estourar os tokens da sua conta e manter o custo financeiro mínimo.

### **Análise Determinística vs. Análise Heurística** *(Implícito)*
* **Análise Determinística**: Processo exato e matemático onde a mesma entrada gera sempre a mesma saída (ex: o script Python que calcula o hash SHA256 de um arquivo para achar duplicações exatas).
* **Análise Heurística**: Processo probabilístico ou baseado em regras práticas que sugere possibilidades fortes, mas exige validação (ex: IAs analisando a semântica do código).

### **Agente Somente Leitura (Read-Only Agent)** *(Implícito)*
* **O que é**: Um perfil de agente de IA cujas ferramentas de escrita e edição são desabilitadas ou travadas por instrução de sistema.
* **No Toolkit**: Garantido através do `AGENTS-discovery-template.md` (`AGENTS.md`), que desativa a capacidade dos agentes autônomos (Cursor, Claude Code, etc.) de alterarem código de produção.

### **MCP (Model Context Protocol)** *(Implícito)*
* **O que é**: O novo padrão universal da indústria que conecta assistentes de IA diretamente a ferramentas e arquivos do computador de forma segura e padronizada.

### **AST (Abstract Syntax Tree / Árvore de Sintaxe Abstrata)** *(Implícito)*
* **O que é**: A representação gramatical e estrutural que computadores usam para entender o código sem precisar executá-lo.

---

## 🛠️ 2. Conceitos de Engenharia de Software & Gestão de Produtos Digitais

Termos práticos do dia a dia de times de produto (PMs, POs) e engenharia (Devs, Tech Leads, CTOs).

### **Discovery Técnico**
* **O que é**: O processo de investigar, auditar e mapear a arquitetura, regras de negócio e saúde de um repositório de código antes de planejar novas funcionalidades ou refatorações.

### **Débito Técnico (Technical Debt)**
* **O que é**: O custo acumulado de escolher soluções rápidas no passado em vez de uma arquitetura limpa. Como um empréstimo financeiro, ele acumula "juros" na forma de lentidão e bugs futuros.

### **Código Morto (Dead Code)**
* **O que é**: Arquivos, funções, rotas de API ou variáveis que continuam existindo na base de código, mas não são mais chamados ou utilizados por nenhuma parte ativa do sistema.

### **Code Smells & Red Flags (Bandeiras Vermelhas)**
* **O que é**: Sintomas no código que indicam problemas mais profundos de manutenção, como funções gigantescas, `try/catch` vazios ou ausência de *timeouts*.

### **Inconsistência & Incompatibilidade de Tipos de Dados**
* **O que é**: Quando a mesma entidade ou campo de dado é tratado de formas diferentes no sistema (ex: `user_id` manipulado como `string` em um módulo e como `int` em outro; ou um campo `varchar` no banco recebendo números de forma solta).

### **Clean Code (Código Limpo)**
* **O que é**: Um conjunto de práticas e filosofias de escrita de código focadas na clareza, legibilidade, simplicidade e facilidade de manutenção por outros seres humanos.

### **Escopo (Scope Constraint)**
* **O que é**: a limitação deliberada da investigação a um trecho específico (uma função, um módulo ou um arquivo), impedindo que a análise se disperse.

---

## 💡 Como usar este Glossário

- **Para Juniores**: Use para entender o significado das decisões de arquitetura e aprender as boas práticas de Clean Code e auditoria.
- **Para PMs e POs**: Use para dominar os termos técnicos ao conversar com o time de engenharia e entender os riscos e custos de manutenção do produto.
- **Para Tech Leads e CTOs**: Use como guia de treinamento do time para instituir a cultura de Discovery não-destrutivo e governança de IA na empresa.
