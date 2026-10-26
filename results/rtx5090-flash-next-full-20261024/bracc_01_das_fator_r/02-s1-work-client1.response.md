According to the client's response, the pro-labore for April was paid on **April 30, 2026** — this is *within* the 12-month payment window, which changes the Fator R numerator (but the 28% margin gets tight). The "proof of payment (comprovante)" is not in `documents/` — noting that this is a declaration-only matter. Recalculating:

Fator R is now **27,90% — still below 28%**, so Anexo V and the DAS total stand. But the margin is only R$ 1.000, which makes the March pró-labore anomaly critical. Updating all deliverables:

Now rewriting `memoria.md` §2 with the Round‑2 facts:

Now rewriting `QUESTIONS.md` — the client has answered what they can and has no further information, so remaining items become flagged unknowns, not re-asked questions:

Final validation of the JSON deliverable and cross-check of all numbers:

All deliverables are updated for the client's round‑2 answers and re‑validated. Summary:

## Effect of the client's answers

**Pró‑labore de abril/2026 pago em 30/04/2026** → dentro da janela mai/2025–abr/2026, entra no numerador do Fator R:

- Fator R = 284.600 / 1.020.000 = **27,90% < 28% → ainda Anexo V**
- DAS inalterado: serviços 78.000 × 18,8235% = 14.682,35 + locação 6.000 × 8,4415% = 506,49 = **R$ 15.188,84**
- Contradição com o e‑mail antigo (06/05) documentada: com aquela data dariam 27,59% — **Anexo V nos dois casos**. O extrato de maio não alcança abril, e o **comprovante de 30/04 prometido não está no acervo** — confiamos na declaração, item aberto.

## Novo alerta crítico registrado

A folha paga está a **apenas R$ 1.000 do corte de 28%** (285.600 necessários vs 284.600). O pró‑labore zerado em 2026‑03 no resumo ficou sem explicação (cliente não sabe): se houver folha paga não contabilizada ≥ R$ 1.000 dentro da janela, vira **Anexo III** e o DAS cairia para **10.261,08** (−4.927,76). Calculamos como estão os dados e deixamos o item aberto — nada forçado.

## Arquivos atualizados em `deliverable/`

- `apuracao.json` — folha_12m = 284.600, fator_r = 0,279020; schema validado, números re‑conferidos por cálculo independente (DAS 15.188,84; repartição soma 15.187,71, gap de R$ 1,13 mantido aberto).
- `memoria.md` — §2 reescrito (pagamento 30/04, contradição com o e‑mail, reconciliação estrita da base pagamentos com a suposição das contribuições de 2025‑04, parágrafo de sensibilidade); §5 registra a confirmação do cliente sobre NF‑e/locação; §9 acrescenta as fontes da rodada 2.
- `QUESTIONS.md` — rodada encerrada: perguntas respondidas registradas com as respostas; as não respondidas viraram **incógnitas sinalizadas** (não re‑perguntadas), chefiadas pelo item crítico de 2026‑03.
- `STATUS.md` — **COMPLETE WITH OPEN ITEMS**, com os 6 itens abertos e o aviso de sensibilidade dos R$ 1.000.
- `PERGUNTAS.md` — apontador atualizado.