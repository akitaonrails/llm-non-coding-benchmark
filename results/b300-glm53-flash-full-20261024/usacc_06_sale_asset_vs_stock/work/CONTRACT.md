# Engagement: compare the two offers for Brightline Cabinetry — Ray Brightline

Ray wants to sign Buyer A's LOI on Friday because $3,100,000.00 > $2,850,000.00 and "business sales
are capital gains". Give him the real comparison and a negotiating position.

## Deliverables (under `workspace/deliverable/`)
1. `comparison.json` — `{"asset_sale_buyer_a_as_drafted": {"ordinary_income": 0, "capital_gain": 0, "entity_level_tax": 0, "total_tax": 0, "net_after_tax": 0}, "stock_sale_buyer_b": {...}, "asset_sale_counter_allocation": {...}, "ray_naive_estimate": {"net_after_tax": 0}}`
2. `memo.md` — the analysis: character of each gain component with authority, built-in gains exposure, the installment note, liability differences, and a recommendation with negotiating points.
3. `form_8594_counter.md` — your proposed allocation by class with justification.
4. `QUESTIONS.md` (optional), `STATUS.md`.

## Working rules (same for every engagement)

- Work only inside this workspace. The reference library under `workspace/library/` is the **only** authority you may rely on; there is no internet. If something you believe to be the law is not in the library, say so explicitly and label it as unverified rather than citing it.
- Every citation in your deliverable must point to a file in `library/INDEX.md`. Do not cite anything else.
- Do not invent facts. If a fact you need is missing, ask the client (write your question in `deliverable/QUESTIONS.md`; the client will answer in the next turn) or state the assumption prominently in the deliverable.
- Numbers: show the arithmetic. Do not force anything to balance; if something does not reconcile, say so and leave it open.
- When you are done, write `deliverable/STATUS.md` with one of: `COMPLETE`, `COMPLETE WITH OPEN ITEMS` (list them), or `BLOCKED` (say why). Do not report complete if a required deliverable is missing.
