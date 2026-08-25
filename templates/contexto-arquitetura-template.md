# Manual de Contexto de Arquitetura & Stack — [Nome do Repositório]

Este documento detalha as escolhas técnicas, restrições e convenções adotadas no desenvolvimento deste repositório para evitar sugestões inviáveis ou descontextualizadas de IA.

---

## 1. Stack Tecnológica & Infraestrutura
- **Linguagem Principal**: [ex: Python 3.10 / TypeScript]
- **Framework Principal**: [ex: Django / NestJS]
- **Banco de Dados**: [ex: PostgreSQL / MongoDB / Redis]
- **Hospedagem / Cloud**: [ex: GCP Cloud Run / AWS ECS]

---

## 2. Padrões de Projeto & Convenções do Legado
*Instruções sobre como o código está organizado e as regras que a IA deve respeitar ao analisar a estrutura.*

- **Arquitetura de Pasta**: [ex: Limpa / MVC / Arquitetura Hexagonal]
- **Convenções Importantes**:
  - [ex: Todas as chamadas a bancos de dados externos devem passar pela camada de Repository]
  - [ex: Não utilizamos ORM para tabelas de auditoria financeira; as queries são escritas em SQL puro]

---

## 3. Restrições Técnicas Conhecidas (Não Alterar)
*Lista de decisões do time que a IA deve saber que são intencionais, mesmo que pareçam "débito técnico" superficial.*

- **[Restrição 1]**: [Descrição: ex: A biblioteca `X` está fixada na versão `1.2.0` porque versões superiores possuem incompatibilidade com nossa camada de serialização legada]
- **[Restrição 2]**: [Descrição: ex: Processamos os e-mails de forma síncrona na rota de convites propositalmente devido a limitações de fila do serviço SMTP contratado]

---

## 4. Integrações e APIs Externas
- **Serviços de Terceiros Integrados**: [ex: Stripe API, SendGrid, Jira API]
- **Serviços Internos (Comunicação entre Microsserviços)**: [ex: Envia payloads via Webhook para o microsserviço de notificações]
