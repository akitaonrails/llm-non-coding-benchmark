Audit is clean. Now the fixes to `memoria.md` — first, the L1 citation row (harmonize with INDEX's exact string, noting body-only provisions):

§3: replace the unsupported claim that receiving date is irrelevant for revenue with a labelled library-silence note plus the robustness argument:

§5: strengthen the folha section — decomposition of 281.400, disclosure that the 06/05 payment isn't in the extrato, and the March-row anomaly with its alternative path to 284.600:

Now the sensitivity paragraph — cover the March-row zero anomaly and its compensation path to 284.600:

That variant sentence needs clearer arithmetic — let me rewrite it:

§8 rounding wording fix, and add assumption P4 to §10:

Now update `STATUS.md` — add the new open item and cross-reference the alternative folha path:

Now the small JSON wording fix — check the exact `observation` text first:

Final validation pass — JSON parse, typo scan, and re-read of the edited sections:

Typo scan clean. Validate the JSON and figures with Python instead:

One precision fix in the correction paragraph — the resumo observation only proves non-payment at the summary date, not at window end:

Review complete. All arithmetic re-audited and clean; the fixes were in **disclosure and authority hygiene**, not in the numbers.

## What the review found and what I changed

**1. Unsupported legal assertion — fixed (`memoria.md` §3).** I had written that the receiving date (26/05) "é indiferente para receita" as if it were settled law. The library is **silent on the revenue-recognition regime** (emissão vs. recebimento). Reframed: library silence stated explicitly (new assumption **P4** in §10) plus a robustness argument — every May note (services and locação) was both *issued and received* within May, so no result depends on the regime.

**2. Reconciliation gap that failed to appear in the records — now disclosed (§5 + STATUS item 5).** The sócio's claimed pró-labore payment of **06/05/2026 does not appear in the bank statement** — the balance chain closes exactly with no debit that day. Treatment kept (client statement taken as fact; possibly another account/channel), and noted the Fator R outcome is identical whether it was paid 6/May or not paid by 30/04 — outside the window either way.

**3. Anomaly in the folha summary — disclosed with a second sensitivity path (§5).** The resumo's line **2026-03 has pró-labore = 0** with April's observation attached to it — anomalous under any reading. Added the explicit variant: if that zero is a keying slip (March pró-labore actually paid mid-March), the paid-window folha recomposes to 193.000 + 32.000 + 3.200 + 0 + 56.400 = **284.600,00 → 27,9020%**. I kept **281.400,00** as primary (client files taken at face value + the only client-confirmed correction; re-deriving March payment would be inventing data).

**4. Precision fix:** "confirma que não estava pago" → the resumo observation only shows unpaid **at the summary draw date**; the sócio then reports payment on 06/05.

**5. Explicit decomposition added:** folha_12m = salários 193.000 + pró-labore in-window 32.000 + encargos 56.400 = 281.400,00.

**6. Citation harmonization (L1 row):** now quotes INDEX.md's exact citation string; §4º (segregação), §5º-B and the devoluções/cancelamentos rule are flagged as provisions found in the file body, not in the citation line.

**7. Wording:** contradictory "arredondamento por truncamento-convencional" → conventional rounding, half-up; JSON cosmetic "per art. 18" → "conforme art. 18".

**8. `STATUS.md`:** added open item 5 (the two folha-data anomalies; any reading keeps Anexo V, faixa 4 and the same DAS).

## Verified unchanged (no errors found)

- Python re-audit: resumo rows (193.000 + 35.200 + 56.400 = 284.600); RBT12 1.020.000,00; effective rates 18,823529% / 12,505882%; DAS 14.682,35 + 506,49 = **15.188,84**; repartição locação slice 505,36 (99,85% library gap — still open, not forced);bank statement balance chain closes fully.
- All citations map to `library/INDEX.md`; `apuracao.json` parses and conforms to the CONTRACT template.

Core deliverable stands: **RBT12 1.020.000,00 · folha 281.400,00 · Fator R 0,275882 · Anexo V, 4ª faixa · DAS total R$ 15.188,84** — status remains `COMPLETE WITH OPEN ITEMS` (now 5 items).