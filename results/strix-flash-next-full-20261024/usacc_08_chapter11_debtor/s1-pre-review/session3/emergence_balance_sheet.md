# Emergence balance sheet — presentation without fresh-start reporting

Status: **provisional** — presentation conclusions follow from `library/asc852_fresh_start.md` and
`documents/plan_term_sheet.md`; dollar amounts beyond the term sheet (exit financing terms, plan discount rate,
tax rate, Dkt. 61 Carve-Out) are not in the file and are flagged, not invented.

## Threshold conclusion (from `fresh_start.md`)

Fresh-start reporting is **not** adopted: condition (a) is met (reorganization value 14,000,000.00 < post-petition
liabilities and allowed claims 16,200,000.00) but condition (b) fails (existing voting shareholders receive 60% —
not less than 50%). The reorganized entity therefore **continues historical carrying amounts**: no fair-value
revaluation of assets, no reset of retained earnings, no new-start equity presentation.

## How the discharged debt and the gain are presented

Per `library/asc852_fresh_start.md` (fail case): "liabilities compromised by the plan are stated at **present value
of amounts to be paid** and the **gain on discharge is reported as a reorganization item** in the income statement."

| Line | Pre-emergence (case basis) | At emergence |
|---|---|---|
| GUC claims (allowed 8,400,000.00) | Liabilities subject to compromise, separate from post-petition liabilities (ASC 852-10-45-4 to 45-6) | Replaced by **Plan payment liability at PV of the 2,940,000.00 payable over 24 months** (PV needs the plan discount rate [unknown]; undiscounted 2,940,000.00 → PV is lower) |
| Gain on discharge | not yet recognized | **Reorganization item in the income statement**: gain = 8,400,000.00 − PV(plan payments). Undiscounted placeholder 5,460,000.00; @8% illustration 5,691,458.41 (see `fresh_start.md` table) — do not book until the rate is fixed |
| DIP facility (drawn 1,050,000.00 at 3/31; authority 2,500,000.00) | DIP liability at face + accrued interest/fees [rate not in file — unquantified] | **Repaid in full from exit financing** → DIP extinguished at carrying amount; new exit facility recorded at face at closing (terms [unknown]). No discharge → **no COD and no reorganization gain on the DIP** |
| Professional fees awarded but unpaid (§§330/331 — see `session2/professional_fees.md`) | accrued in post-petition payables; holdbacks tracked in MOR Part 5 | remain post-petition liabilities at approved amounts; holdbacks stay accrued until the final fee award |
| UST fees, other admin | accrued as quantified only | continue as admin obligations; unpaid items remain liabilities |
| Assets | historical cost basis, case-period presentation | **unchanged historical carrying amounts** (no fresh-start step-up; goodwill is NOT recognized — no fresh-start) |
| Mesa Steel (illustrative of the no-netting rule) | LSTC 62,400.00 **gross**; ~11,000.00 coil credit kept as a separate receivable | Mesa's allowed claim folds into the plan payment liability at plan PV share; the ~11,000.00 receivable stays an asset (or a court-approved compromise applies it against post-petition invoices) — never netted against the pre-petition claim |
| Equity | pre-petition paid-in capital and accumulated deficit continue through the case | **no reset**: accumulated deficit carries over; the reorganization gain flows through the income statement into accumulated deficit; cap table 60% existing / 40% DIP lender is a legal share count, not a re-measurement of book equity |

## Tax lines on the emergence balance sheet

- **Current tax**: COD income of 5,460,000.00 is **excluded from gross income** under 26 U.S.C. §108(a)(1)(A)
  (title 11 case — `library/irc_108.md`), so no current tax expense arises from the discharge. Attribute reduction
  is made **after** the discharge year's tax is determined (§108(b)(1)).
- **Deferred tax**: the NOL DTA shrinks by the 5,460,000.00 reduction (NOL 6,100,000.00 → 640,000.00 —
  `cod_schedule.json`); quantifying the DTA movement needs the tax rate [not in the file]. Depreciable tax basis
  stays 3,200,000.00 absent a §108(b)(5) election (recommendation: no election; reasoning in `cod_schedule.json`).
- The book gain (PV-based, > 5,460,000.00 once discounted) and the tax COD (5,460,000.00, excluded) differ by the
  discount on plan payments — a permanent book/tax difference to track in the tax provision. Whether an
  ownership-change limitation (IRC §382) hits the surviving NOL is **[unverified — §382 not in the library]** and
  must go to tax counsel.

## Presentation mechanics at the transition date

1. Stop the Chapter 11 captions (no more "liabilities subject to compromise") **on and after the effective date**;
   comparative case-period statements keep the separate LSTC vs. post-petition split (852-10-45-4 to 45-6) and the
   no-netting rule (pre-petition liabilities not netted against post-petition assets).
2. Record the plan payment liability at PV; recognize the reorganization item gain once, in the pre-emergence
   period's income statement (reorganization items line, near the §549/COD-type items).
3. Keep the pre-petition receivable from Mesa (~11,000.00) as an asset until collected or compromised with approval.
4. Reconcile the equity rollforward to the 60/40 share issuance (40% to DIP lender for fees + new money) — share
   counts change; historical carrying amounts do not.

## What is still needed to put dollars on this sheet

Effective-date balance; plan effective interest rate (PV of the 2,940,000.00); exit facility amount/rate/fees; DIP
accrued interest and exit fees [none quantified in file]; itemization of the 16,200,000.00; final approved fee
amounts and holdbacks (4/14 order text); tax rate and NOL vintages. None are in `documents/`; the client has no
further information, so they are carried as **flagged unknowns**, not estimates.
