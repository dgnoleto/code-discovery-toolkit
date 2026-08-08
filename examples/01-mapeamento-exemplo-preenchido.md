# Mapeamento Inicial — iRancho Payment Gateway Integration (Exemplo Fictício)

**Data:** 06/08/2026  
**Responsável:** Danilo Nolêto (Product Manager)  
**Escopo:** Módulo específico — `src/services/payments/`  

> Se o escopo não for "repositório completo", as conclusões abaixo cobrem apenas o que foi especificado — não generalize para o restante do repositório sem investigar separadamente.

---

## 1. O que esse escopo parece fazer

- **Resumo**: Este módulo realiza a comunicação e integração com a API da iRancho Payments para liquidação de assinaturas mensais e geração de boletos/Pix para os clientes do SaaS. Ele parece gerenciar chamadas de cobrança, webhooks de notificação de status e tentativas de reprocessamento (retries).
- **Nível de confiança**: **Confirmado** (para liquidação de boletos) e **Provável** (para fluxo de estorno/refund, pois o código existe no arquivo `refund.py` mas não encontramos chamadas diretas no app).
- **Evidências que sustentam essa conclusão**:
  - `src/services/payments/boleto.py`: Contém a classe `iRanchoBoletoService` que consome as credenciais `IRANCHO_API_KEY` do ambiente.
  - `src/services/payments/webhooks.py`: Rota exposta `/webhooks/payments/` mapeada no controller principal.
  - O histórico de Git aponta que o último commit relevante foi feito há 10 meses por um engenheiro focado no módulo de faturamento (commit `bf8392d`).

---

## 2. Quem usa (ou usava) isso

- **A aplicação principal do SaaS**: Faz chamadas síncronas na classe `iRanchoBoletoService` durante o checkout de novos usuários.
- **Microserviço de Cobrança Recorrente (Cron/Scheduler)**: Executa em lote toda madrugada chamando `webhooks.py` para atualizar o status dos boletos pendentes.

---

## 3. Perguntas abertas para validar com o time

- **[Dúvida/Hipótese]**: O fluxo de estorno em `refund.py` ainda está ativo? Não encontramos nenhuma rota no frontend ou controller principal que o acione. Pode ser código obsoleto.
- **[Dúvida/Tipagem]**: O campo `payment_value` está sendo lido como `string` em `boleto.py:34` mas é persistido como `int` (em centavos) no banco de dados. Essa conversão implícita pode quebrar sob centavos quebrados?
- **[Dúvida/Segurança]**: A rota de webhook em `webhooks.py` não valida a assinatura da requisição (`HMAC-SHA256`). Qualquer payload falso pode ser enviado e processado. Isso é conhecido pelo time de segurança?

---

## Próximos passos sugeridos

- [x] Validar as hipóteses acima com alguém que conheça (ou conheceu) esse repositório.
- [ ] Seguir para a investigação de código morto e duplicações nesse mesmo escopo, usando os prompts [`02-codigo-morto.md`](../prompts/02-codigo-morto.md) e [`03-duplicacoes-redundancias.md`](../prompts/03-duplicacoes-redundancias.md).
- [ ] Rodar a skill de **Health Check** ([`05-health-check.md`](../prompts/05-health-check.md)) para identificar inconsistências de tipagem (ex: string vs int em cobrancas) e segurança nas rotas.
