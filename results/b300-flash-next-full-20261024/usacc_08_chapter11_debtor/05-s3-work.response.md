

New client file for emergence — this likely answers the open TBDs (discount rate, voting split, claim composition) that the Session 3 deliverables were flagged on. Let me read what's in the file:





The confirmation order (Dkt. 214) gives dates and confirms terms. Let me read the current Session 3 deliverables to see exactly what needs updating:







The draft was awaiting exactly the items this order addresses. Let me re-check the two governing library excerpts before revising:






Now I'll fold Dkt. 214 into all three deliverables. Starting with `cod_schedule.json`:





Now `fresh_start.md`:





Now `emergence_balance_sheet.md`:





Validating the JSON and arithmetic, and reading the two ledger files to refresh them:







JSON and arithmetic verified. Now updating the two ledger files:





Final consistency pass on the revised fresh-start memo:





Session 3 is finalized against the confirmation order. All three deliverables in `workspace/deliverable/session3/` are updated, plus `QUESTIONS.md` and `STATUS.md`.

## What Dkt. 214 changed vs. what it confirmed

**Confirmed (numbers unchanged):** GUC pool 35% = $2,940,000.00; discharge $5,460,000.00; reorg value $14.0M vs claims $16.2M; 60% old-equity retention. So the core conclusions hold:

- **COD schedule** (`cod_schedule.json`): discharged $5,460,000.00 → excluded in full under §108(a)(1)(A) (title 11, no insolvency cap) → taxable inclusion $0.00; attribute reduction hits the NOL first: $6,100,000.00 − $5,460,000.00 = **$640,000.00 NOL remaining**; still **no §108(b)(5) election**. New: a `case` block pinning the discharge to the **9/30/2026 effective date** — COD arises in the taxable year containing that date, and §108(b) reductions apply after that year's tax is determined.
- **Fresh-start** (`fresh_start.md`): **still NOT applicable** — condition (a) MET (14.0M < 16.2M, measured immediately before the 9/2/2026 confirmation, both figures now restated in Dkt. 214) but condition (b) FAILED (60% ≥ 50%). The order still never says "**voting**" shares — flagged as the single highest-stakes open fact, since a non-voting 60% would flip this and trigger full fresh-start (push-down, equity reset).
- **Emergence balance sheet** (`emergence_balance_sheet.md`): dated 9/30/2026; gain $5,460,000.00 undiscounted stays a **reorganization item** (no equity credit, no push-down, no retained-earnings reset).

**One genuinely new fact:** the **first installment is paid in cash on the effective date**. The emergence-date GUC obligation is therefore shown *after* that payment — ≤ **$2,817,500.00** undiscounted, with the conditional level-monthly arithmetic shown ($2,940,000 ÷ 24 = $122,500/installment; current/noncurrent $1,470,000 / $1,347,500 if level monthly over the remaining 23). The order doesn't state installment sizes or an interest rate, so PV remains TBD and nothing is forced to balance. The first installment does **not** change the COD numbers — amounts actually paid are never discharged.

## Still open (QUESTIONS.md § Session 3)
1. Discount rate + installment sizes for the GUC stream
2. **Voting-share confirmation of the 60/40 split** (could flip fresh-start)
3. DIP fee vs. new-money split of the 40%; exit financing terms
4. Composition of the $7,800,000 non-GUC claims
5. NOL attribute detail (vintages/expiry — labeled unverified, not in library)

Arithmetic re-verified in Python; `cod_schedule.json` validated as parseable JSON. Overall status remains **COMPLETE WITH OPEN ITEMS**.