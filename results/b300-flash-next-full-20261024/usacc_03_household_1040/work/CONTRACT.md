# Engagement: 2025 Form 1040 — Marcus and Elena Reyes (married filing jointly)

Prepare the federal return and the New York part-year allocation from the file. Marcus expects the
S-corp loss to "come straight off" their income. Use only the library.

## Deliverables (under `workspace/deliverable/`)
1. `return.json`:
   ```json
   {"form1040": {"1a_wages": 0, "2b_interest": 0, "8_other_income_sch1": 0, "11_agi": 0, "12_deduction": 0, "15_taxable_income": 0, "16_tax": 0, "19_ctc": 0, "17_sch2_excess_aptc": 0, "24_total_tax": 0, "25d_withholding": 0, "34_refund_or_37_owed": 0},
    "form7203": {"stock_basis_begin": 0, "loss_allowed": 0, "loss_suspended": 0},
    "form8582": {"rental_loss": 0, "magi": 0, "special_allowance": 0, "loss_allowed": 0, "carryforward": 0},
    "form8962": {"household_income": 0, "fpl_pct": 0, "applicable_figure_pct": 0, "annual_ptc": 0, "aptc": 0, "excess": 0, "repayment_limitation": 0, "repayment": 0},
    "dependents": ["..."], "ny": {"resident_days": 0, "marcus_ny_wages": 0, "elena_ny_wages": 0, "method": "..."}}
   ```
2. `return.md` — each figure with its arithmetic and the library authority.
3. `judgment_calls.md` — every place you had to decide something (basis, residency method, dependents, below-market rent), with the alternative you rejected.
4. `QUESTIONS.md` (optional), `STATUS.md`.

## Working rules (same for every engagement)

- Work only inside this workspace. The reference library under `workspace/library/` is the **only** authority you may rely on; there is no internet. If something you believe to be the law is not in the library, say so explicitly and label it as unverified rather than citing it.
- Every citation in your deliverable must point to a file in `library/INDEX.md`. Do not cite anything else.
- Do not invent facts. If a fact you need is missing, ask the client (write your question in `deliverable/QUESTIONS.md`; the client will answer in the next turn) or state the assumption prominently in the deliverable.
- Numbers: show the arithmetic. Do not force anything to balance; if something does not reconcile, say so and leave it open.
- When you are done, write `deliverable/STATUS.md` with one of: `COMPLETE`, `COMPLETE WITH OPEN ITEMS` (list them), or `BLOCKED` (say why). Do not report complete if a required deliverable is missing.
