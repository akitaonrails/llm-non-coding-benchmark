# Engagement: 2025 Schedule C and Schedule SE for Dana Okafor

You are the staff preparer. Dana is a single filer in Texas with four months of W-2 employment and
a first year of freelance UX design income. Dana asked you to "just add up the 1099s". Your job is
to prepare a correct Schedule C and the self-employment tax figure from the documents in
`workspace/documents/`, using only `workspace/library/` as authority.

## Deliverables (write all under `workspace/deliverable/`)

1. `schedule_c.json` — machine-readable, one entry per Schedule C line you use, in this shape:
   ```json
   {"tax_year": 2025, "lines": {"1": 0.00, "9": 0.00, "10": 0.00, "...": 0.00, "28": 0.00, "31": 0.00},
    "schedule_se": {"net_earnings": 0.00, "se_tax": 0.00, "deductible_half": 0.00},
    "not_on_schedule_c": [{"item": "...", "amount": 0.00, "where": "Schedule 1 line 17 / personal / prior year"}]}
   ```
   Amounts in dollars and cents. Use the line numbers from the Schedule C instructions in the library.
2. `schedule_c.md` — the same figures with a one-paragraph explanation per line showing the arithmetic.
3. `classification.csv` — every row of the bank export, with columns `date,description,amount,classification,schedule_c_line,note`, where classification is one of `business_income`, `business_expense`, `personal`, `prior_year`, `tax_payment`, `transfer`, `other_schedule`.
4. `QUESTIONS.md` — anything you need to ask Dana (optional, answered next turn).
5. `STATUS.md`.

## Standards you will be held to

- Gross receipts must reflect what Dana actually earned in 2025, not a mechanical sum of forms.
- Personal items must not appear on Schedule C. Items that belong on another schedule must be listed under `not_on_schedule_c`, not dropped silently.
- Use the rates and rules in the library, not ones you remember.
- Business-use percentages you cannot support from the file must be asked or stated as assumptions.

## Working rules (same for every engagement)

- Work only inside this workspace. The reference library under `workspace/library/` is the **only** authority you may rely on; there is no internet. If something you believe to be the law is not in the library, say so explicitly and label it as unverified rather than citing it.
- Every citation in your deliverable must point to a file in `library/INDEX.md`. Do not cite anything else.
- Do not invent facts. If a fact you need is missing, ask the client (write your question in `deliverable/QUESTIONS.md`; the client will answer in the next turn) or state the assumption prominently in the deliverable.
- Numbers: show the arithmetic. Do not force anything to balance; if something does not reconcile, say so and leave it open.
- When you are done, write `deliverable/STATUS.md` with one of: `COMPLETE`, `COMPLETE WITH OPEN ITEMS` (list them), or `BLOCKED` (say why). Do not report complete if a required deliverable is missing.
