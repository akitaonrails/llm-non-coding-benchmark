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
| Q4 | Text/terms of the 4/14/2026 H&P interim compensation order ("80%/100% holdback"); Corbin status | **Provided in Session 2** — Dkt. 77 excerpt in `documents/session2/`. Confirms 80% of fees + 100% of expenses absent 14-day objection, 20% fee holdback pending interim/final application, and **no payment for periods before retention**. April Part 5 filed 144,200.00 / 0.00 / 28,000.00; Corbin excluded pending objection status and the 3/20 retention gate (see `session2/professional_fees.md`) |
| Q5 | Dkt. 61 Exhibit B approved budget | 10% cumulative variance covenant (Dkt. 61 ¶1) is **UNTESTED** — stated in MOR notes |
| Q6 | Pre-petition claims population (schedules, register, AP trial balance) | LSTC reported as **documented subset $74,110.00**; gap to the $8,400,000 allowed GUC pool ($8,325,890.00) **left open, not plugged** |
| Q7 | DIP interest rate, fees, Carve-Out amount | DIP interest/fees excluded from Part 2 as **unquantified**; Part 2 post-petition payables are therefore understated |
| Q8 | Post-petition tax accruals (sales/use, payroll, income) | Only the UST fee accrual $3,926.16 is booked, at the client's **0.8% estimate [unverified — statute not in library]** |
| Q9 | UCC appointment; Mesa contract/PO | Flagged; any Mesa motion will require notice per the orders; no §365 authority in the library, so performance/contract issues are for counsel |

## Data dependencies (not questions — needed when the periods arrive)

New facts from the CFO's follow-up ("call it a deposit on the Q2 order"): **Denver Water is the debtor's
customer**, and Mesa is conditioning the Q2 structural order on payment of its pre-petition invoice. Answered and
refused in `session1/response_to_cfo.md` §8. If a Q2 order/deposit is actually executed, the file will need: the
signed PO with deposit terms, the payment record, and confirmation the ~$62,400.00 pre-petition invoice remains
unpaid at gross (if Mesa applied the "deposit" to the old balance, it is a disguised pre-petition payment — Part 7
disclosure + avoidance analysis; 11 U.S.C. §547 is **not in the library** [unverified]). If the Mesa
critical-vendor motion is filed/granted, the order will change the segregation.csv classification and the next
MOR's Part 7.

The **April MOR** (`session2/april_mor.json`) was built from `documents/session2/april_activity.md` once it
arrived; the previously missing inputs (receipts, DIP draw, payrolls, vendor payments, fee statements) are all in
that file. Remaining April unknowns are **flagged in the MOR notes and `STATUS.md` item J**, not re-asked:
itemization of the $214,600.00 vendor payments; whether/when H&P's payable $116,200.00 was paid; Corbin objection
status at 4/30 and day-level allocation; unpaid April invoices and 4/25–4/30 wages at 4/30; the Dkt. 83 order
text (confirm it leaves the February invoice unpaid and whether it touches the ~$11,000 coil credit).

For **emergence** (Session 3) I used the figures in `documents/plan_term_sheet.md` and produced
`session3/cod_schedule.json`, `fresh_start.md` and `emergence_balance_sheet.md` **provisionally**, flagging the
effective-date facts still missing (discount rate for the plan payments, exact composition of the $16.2M
post-petition liabilities and allowed claims, whether the unpaid March vendors sit inside the $8.4M GUC pool, DIP
repayment/exit-financing amounts, and the disposition of the Mesa claim).

## Session 3 turn — emergence deliverables finalized on the confirmed plan (no new asks)

`documents/session3/confirmation_order_excerpt.md` (Dkt. 214, confirmed 9/2/2026, effective date 9/30/2026)
**answered** the Session 3 provisional flags without any re-ask: effective/discharge date is 9/30/2026; the GUC
stream is confirmed at $2,940,000.00 (35%) over 24 months with the **first installment on the effective date**;
reorganization value $14,000,000.00, post-petition liabilities and allowed claims $16,200,000.00, and old-equity
retention of **60%** are confirmation-order findings; "Terms as in the term sheet" keeps the DIP repayment-from-exit-
financing and 40%-to-DIP-lender structure. The trio in `deliverable/session3/` was re-run on these facts and is
final on the confirmed plan.

Still-missing emergence inputs are carried as **flags in `STATUS.md` item I**, not re-asked (the client has no
further information): plan interest/discount rate and installment frequency (blocks the PV of the plan payments,
the exact reorganization gain, and the current/noncurrent split — PV tables in `fresh_start.md` are illustrations
only); composition of the $16,200,000.00; exit financing terms; DIP accrued interest/fees and payoff total
(item G); final professional-fee awards; tax rate and NOL vintages (the $640,000.00 NOL-after figure is the
order-level result and moves with the 2026 return); §382 question for tax counsel [unverified — not in library].

**New data need (compliance, not a re-ask):** May–September 2026 monthly activity. Dkt. 61 ¶4 (verbatim): "The
Debtor shall file Monthly Operating Reports on the UST Form 11-MOR by the 21st of each month" — no end condition
appears in the excerpt, and the DIP was repaid only on the effective date, so MORs for periods ending
5/31–9/30/2026 (due 6/21–10/21/2026 — all now passed) appear unaddressed (`STATUS.md` item K). With the monthly
activity files, the five MORs (the last one final, through 9/30) can be prepared; without them, the emergence cash
line and post-April Part 2 amounts stay flagged unknowns.
