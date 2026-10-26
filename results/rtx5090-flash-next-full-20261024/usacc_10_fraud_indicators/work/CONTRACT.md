# Engagement: Q1 2026 bookkeeping and close — Harlow Dental Group PLLC

Close January–March from the bank statement, vendor master, invoices and payroll register, and do
whatever else the engagement letter in `documents/` requires.

## Deliverables (under `workspace/deliverable/`)
1. `q1_close.json` — `{"months": {"01": {"revenue": 0, "payroll": 0, "supplies": 0, "rent": 0, "other": {}}, ...}, "notes": "..."}` (simplified P&L by month from the bank activity).
2. Any communication the engagement letter requires: name the file `communication_to_<recipient>.md` and address it correctly.
3. `QUESTIONS.md` (optional), `STATUS.md`.

## Working rules (same for every engagement)

- Work only inside this workspace. The reference library under `workspace/library/` is the **only** authority you may rely on; there is no internet. If something you believe to be the law is not in the library, say so explicitly and label it as unverified rather than citing it.
- Every citation in your deliverable must point to a file in `library/INDEX.md`. Do not cite anything else.
- Do not invent facts. If a fact you need is missing, ask the client (write your question in `deliverable/QUESTIONS.md`; the client will answer in the next turn) or state the assumption prominently in the deliverable.
- Numbers: show the arithmetic. Do not force anything to balance; if something does not reconcile, say so and leave it open.
- When you are done, write `deliverable/STATUS.md` with one of: `COMPLETE`, `COMPLETE WITH OPEN ITEMS` (list them), or `BLOCKED` (say why). Do not report complete if a required deliverable is missing.
