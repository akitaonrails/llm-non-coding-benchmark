# Passivo fiscal da União — solução (Sessão 3)

**Débito:** R$ 2.700.000 (IRPJ/CSLL/PIS/COFINS federais — `relacao_credores.csv`)

## Por que o plano NÃO resolve

- **CTN art. 187**: crédito tributário não vai a concurso/habilitação em RJ.
- **LRF art. 68**: crédito tributário **não se sujeita ao plano** (a cláusula "deságio 50% em 180 parcelas" da minuta é ineficaz — ver `sessao2/analise_plano.md`, cláusula 4).
- **Art. 6º, §7º-B**: a execução fiscal **não se suspende** — a União pode constritor a qualquer momento; só há proteção parcial para atos sobre bens de capital essenciais (as máquinas da linha de separação — prioridade absoluta de defesa).
- **Art. 57 da LRF + CTN art. 191-A**: sem prova de quitação/certidão (CPEN), **a recuperação não é concedida**. Ou seja: o parcelamento não é opcional — é condição do processo.

## Via correta: Lei 10.522/2002, arts. 10-A a 10-C (Lei 14.112/2020); Lei 13.988/2020; Portaria PGFN 2.382/2021

Três modalidades, com aritmética sobre os R$ 2.700.000 (**valores nominais, sem juros/multa consolidados — a biblioteca não traz as taxas de calcamento; premissa sinalizada**):

| Opção | Base legal | Estrutura | Aritmética | Parcela/mês |
|---|---|---|---|---|
| **A — Parcelamento padrão RJ** | art. 10-A | até **120 parcelas** | 2.700.000 ÷ 120 | **R$ 22.500,00** |
| **B — Parcelamento com liquidação por prejuízo fiscal** | art. 10-A, §1º-B | abater **até 30%** com prejuízo fiscal/base negativa de CSLL; saldo em **84 parcelas** | 30% × 2.700.000 = 810.000 liquidados em prejuízo; saldo 1.890.000 ÷ 84 | **R$ 22.500,00** (e preserva caixa de 810.000) |
| **C — Transação com a PGFN** | art. 10-C c/ Lei 13.988/2020 e Portaria PGFN 2.382/2021 | desconto **até 70%**, exaustão em até **120 meses** | desconto máx. 1.890.000; pago 810.000 ÷ 120 | **R$ 6.750,00** |

A adesão gera **certidão positiva com efeitos de negativa (CPEN)** — suficiente para o art. 57/CTN 191-A.

## Recomendação e sequência (prazos)

1. **Imediato (antes da concessão da recuperação / junto à impugnação do plano):** aderir à **Opção A** como piso — garante CPEN e destrava o art. 57 no ato. Custo mensal R$ 22.500, compatível com o fluxo (semanas 1–4: +R$ 20.000 líquidos em 4 semanas; parcelas A e B cabem no caixa, C folga).
2. **Em paralelo (60–90 dias):** negociar **transação (Opção C)** com a PGFN pela capacidade de pagamento (Portaria 2.382/2021). Cenário máx. de desconto: pagar R$ 810.000 em 120 meses (R$ 6.750/mês) — economia nominal de R$ 1,89 mi. A transação substitui o parcelamento A na consolidação.
3. **Se houver prejuízo fiscal relevante:** comparar **B vs. uso do prejuízo para abater o ganho do deságio** (Sessão 2). O mesmo estoque de prejuízo não serve aos dois: compensar o ganho de R$ 3.882.000 de IRPJ/CSLL sem trava (art. 50-A II) vale ~R$ 1,32 mi de tributos (alíquotas não verificadas na biblioteca), enquanto a Opção B libera só R$ 810.000 de caixa — a **prioridade, se o estoque for pequeno, é o ganho do deságio; o excedente vai para a Opção B**. Como o cliente não tem o valor do prejuízo, mantenho a decisão em aberto.
4. **Estaduais/municipais (ICMS/ISS):** se existirem (cliente não informou), a biblioteca só cobre a via federal — sinalizado como não verificável.

## Riscos a monitorar

- Execução fiscal ativa durante todo o processo (art. 6º, §7º-B): pedir que o AJ acompanhe atos constritivos sobre as **máquinas essenciais** (competência do juízo da RJ, ressalva do próprio §7º-B).
- Sem adesão até a fase de concessão: risco de **indeferimento da recuperação** (art. 57/CTN 191-A), não de apenas multa.
- Valores acima são nominais: a consolidação da transação inclui juros/multa conforme ato PGFN — **valores exatos não calculáveis com a biblioteca**.
