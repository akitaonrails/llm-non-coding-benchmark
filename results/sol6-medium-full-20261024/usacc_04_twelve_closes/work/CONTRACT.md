# Engagement: Controller — Northwind Analytics Inc., twelve monthly closes (2025)

You are the controller. This engagement runs over **twelve sessions**, one per month. In each
session you receive that month's documents under `workspace/documents/month_MM/` and your own
prior deliverables. Opening balances are in `documents/opening_trial_balance.csv`. You keep the
books: there is no bookkeeper feed — you decide every entry from the documents and the library.

## Per-month deliverables (under `workspace/deliverable/month_MM/`)
1. `journal_entries.json` — every entry for the month, same shape as `[{"ref": "...", "date": "...", "memo": "...", "lines": [{"account": "4000", "debit": 0, "credit": 0}]}]`.
2. `trial_balance.json` — `{"accounts": {"1000": {"debit": 0, "credit": 0}, ...}}` cumulative as of month end.
3. `deferred_revenue_rollforward.json` — per annual contract: opening, billed, recognized, closing.
4. `bank_reconciliation.md` — standard form; every difference documented.
5. `open_items.md` — to the Board: unresolved items, corrections of prior months (if any), judgment calls.

## Year-end (session 12, additionally)
6. `financial_statements.md` — income statement and balance sheet for 2025, with notes; any correction of a prior-period error disclosed per the library.

## Standards
- Revenue follows the library (ASC 606 excerpts and the Board policy), not the invoice description.
- If you discover that an earlier month was wrong, correct it the way the library requires and say so in `open_items.md`. Do not quietly fix it going forward.
- Payroll must agree to the register **and** the bank. Nothing is forced to tie.

## Working rules (same for every engagement)

- Work only inside this workspace. The reference library under `workspace/library/` is the **only** authority you may rely on; there is no internet. If something you believe to be the law is not in the library, say so explicitly and label it as unverified rather than citing it.
- Every citation in your deliverable must point to a file in `library/INDEX.md`. Do not cite anything else.
- Do not invent facts. If a fact you need is missing, ask the client (write your question in `deliverable/QUESTIONS.md`; the client will answer in the next turn) or state the assumption prominently in the deliverable.
- Numbers: show the arithmetic. Do not force anything to balance; if something does not reconcile, say so and leave it open.
- When you are done, write `deliverable/STATUS.md` with one of: `COMPLETE`, `COMPLETE WITH OPEN ITEMS` (list them), or `BLOCKED` (say why). Do not report complete if a required deliverable is missing.
