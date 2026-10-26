# Questions log — Redwood Fabrication, Inc. (Case No. 26-11842-TBM)

## Client response received (Session 1 follow-up)

The client answered **one** item:

> "Mesa owes us about $11,000 for coils we returned in January. I figured we'd just net it."

That is a new fact (a ~$11,000 pre-petition receivable from Mesa) and a proposal. It is answered and booked in
`session1/response_to_cfo.md` §7, `session1/segregation.csv` (Mesa 2/2 row), `session1/march_mor.json` notes and
Part 7, and `session1/march_mor_workpaper.md`. Netting refused: Dkt. 61 ¶3 bars netting against pre-petition
obligations by name; the credit is an estate asset and applying it to Mesa's pre-petition claim is an avoidable
post-petition transfer, 11 U.S.C. §549(a) (library/bc_362_363_503_549.md); Mesa is not on Dkt. 48 Schedule 1.
Lawful alternative (court-approved application of the credit against Mesa's **post-petition** invoices) is set out
in the memo.

The client also stated: **"For questions not answered above, the client has no additional information"** and
instructed me not to re-ask. Accordingly the items below are **closed as unanswered** and are carried in the
deliverables as explicitly flagged unknowns / stated assumptions — not as open questions.

## Closed as unanswered — now disclosed as assumptions or flagged unknowns

| # | Item | How it is now carried |
|---|---|---|
| Q1a/c | Pre-petition cash swept into DIP account (beginning cash); DIP account bank balance at 3/31 | March `ending_cash` $1,771,630.00 is labeled **activity-only**, understated by the unknown swept balance; NOT reconciled to a bank statement |
| Q1b | Whether any Mesa payment/netting actually went out | **Assumption stated in the MOR:** none has been booked; if it has, Part 7 flips to YES with no docket authority and the transfer is avoidable (§549(a)) |
| Q2 | Pre/post split of the 3/13 payroll; §507(a)(4) per-employee headcount check; cash vs gross; next payroll | Pro-rata split $294,285.71 / $117,714.29 labeled an **assumption**; cap compliance asserted in file but unverifiable; gross used as reported |
| Q3 | Apex written Customary Trade Terms agreement (Dkt. 48 ¶1 condition) | Flagged in Part 7 and segregation.csv as **confirmation outstanding**; if unsigned, the $31,200 payment was outside the order |
| Q4 | Text/terms of the 4/14/2026 H&P interim compensation order ("80%/100% holdback"); Corbin status | `session2/professional_fees.md` gives the rule and both readings of the holdback; actual approved/paid/holdback amounts for April MOR **cannot be computed** without the order text |
| Q5 | Dkt. 61 Exhibit B approved budget | 10% cumulative variance covenant (Dkt. 61 ¶1) is **UNTESTED** — stated in MOR notes |
| Q6 | Pre-petition claims population (schedules, register, AP trial balance) | LSTC reported as **documented subset $74,110.00**; gap to the $8,400,000 allowed GUC pool ($8,325,890.00) **left open, not plugged** |
| Q7 | DIP interest rate, fees, Carve-Out amount | DIP interest/fees excluded from Part 2 as **unquantified**; Part 2 post-petition payables are therefore understated |
| Q8 | Post-petition tax accruals (sales/use, payroll, income) | Only the UST fee accrual $3,926.16 is booked, at the client's **0.8% estimate [unverified — statute not in library]** |
| Q9 | UCC appointment; Mesa contract/PO | Flagged; any Mesa motion will require notice per the orders; no §365 authority in the library, so performance/contract issues are for counsel |

## Data dependencies (not questions — needed when the periods arrive)

For the **April MOR** (`session2/april_mor.json`) the file contains **no April activity data**. When it is
provided, the required inputs are: April receipts (collections, DIP draws), April disbursements, cash balances,
April payroll, amounts actually paid to H&P/Corbin under the 4/14 order (order text), UST fee for the period, and
any Mesa payment/netting entries. Until then `april_mor.json` **cannot be prepared without inventing facts** —
it is recorded as blocked in `STATUS.md`, not fabricated.

For **emergence** (Session 3) I used the figures in `documents/plan_term_sheet.md` and produced
`session3/cod_schedule.json`, `fresh_start.md` and `emergence_balance_sheet.md` **provisionally**, flagging the
effective-date facts still missing (discount rate for the plan payments, exact composition of the $16.2M
post-petition liabilities and allowed claims, whether the unpaid March vendors sit inside the $8.4M GUC pool, DIP
repayment/exit-financing amounts, and the disposition of the Mesa claim).
