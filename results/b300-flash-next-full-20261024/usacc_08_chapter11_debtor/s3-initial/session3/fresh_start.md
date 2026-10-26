# Fresh-start reporting — the two-part test, with numbers

Authority: FASB ASC 852-10-45-19 through 45-29; 852-10-45-9 (library/asc852_fresh_start.md). Fresh-start
reporting is applied upon emergence **only if both** conditions are met.

Case posture (documents/session3/confirmation_order_excerpt.md): plan **confirmed 9/2/2026 (Dkt. 214)**;
**effective date 9/30/2026**. The confirmation order adopts the term-sheet terms and restates both test
figures ($14,000,000.00 reorganization value; $16,200,000.00 post-petition liabilities and allowed claims)
and the 60% old-equity retention. The tests are therefore applied as of confirmation, with emergence on
9/30/2026.

## Condition (a) — reorganization value less than total liabilities and allowed claims

> "the reorganization value of the assets of the emerging entity immediately before the date of
> confirmation is **less than** the total of all post-petition liabilities and allowed claims"

Numbers (restated in the confirmation order Dkt. 214; originally documents/plan_term_sheet.md), measured
immediately before the 9/2/2026 confirmation date:

| Item | Amount |
|---|---:|
| Reorganization value | 14,000,000.00 |
| Post-petition liabilities and allowed claims at effective date | 16,200,000.00 |
| Test: 14,000,000.00 < 16,200,000.00 | **MET** (shortfall 2,200,000.00) |

## Condition (b) — old voting shareholders receive less than 50% of emerging voting shares

> "holders of existing voting shares immediately before confirmation receive **less than 50 percent**
> of the voting shares of the emerging entity"

Numbers (Dkt. 214: "old equity retains 60%"; term sheet: 60% retained / 40% issued to the DIP lender):

| Item | Amount |
|---|---:|
| Reorganized voting shares retained by holders of existing (pre-petition) equity | **60%** |
| Test: 60% < 50%? | **FAILED** |

**Trap avoided:** it is tempting to adopt fresh-start because condition (a) is met (the company is
balance-sheet insolvent by 2,200,000.00), but the test is conjunctive — "only if **both**". The confirmed
plan leaves old equity with a 60% retained stake, which fails the 50% change-of-control test. (Assumption:
the "60% retained / 40% to DIP lender" split refers to **voting** shares, as the test requires — neither
the term sheet nor Dkt. 214 says the words "voting" or "non-voting." If the old-equity 60% were a
non-voting class, condition (b) could flip and fresh-start would apply, changing every presentation in
emergence_balance_sheet.md. This single fact is the highest-stakes open item — QUESTIONS.md.)

## Conclusion: **Fresh-start reporting does NOT apply** at the 9/30/2026 emergence.

Per the same library excerpt, when either condition fails:

1. **Liabilities compromised by the plan are stated at the present value of amounts to be paid** —
   the GUC obligation becomes the PV of the 2,940,000.00 payable over 24 months
   (8,400,000.00 × 0.35 = 2,940,000.00), first installment on the 9/30/2026 effective date (Dkt. 214).
   The discount rate is not in the client file → flagged open; presentations below are undiscounted
   pending the rate.
2. **The gain on discharge is reported as a reorganization item** in the income statement
   (undiscounted 8,400,000.00 − 2,940,000.00 = 5,460,000.00; lower once PV is applied) — it is NOT
   credited to equity and assets are NOT remeasured to the 14,000,000.00 reorganization value; no
   retained-earnings reset occurs. Presentation detail: emergence_balance_sheet.md.
3. During the case, liabilities subject to compromise stay reported separately from post-petition
   liabilities (852-10-45-4 to 45-6), and **pre-petition liabilities are not netted against
   post-petition assets** (852-10-45-9) — the reporting rule consistent with refusing the Mesa
   netting in Session 1.

## Tax side of the same facts (IRC § 108 — library/irc_108.md)

- COD income arising by reason of discharge: **5,460,000.00**.
- Discharge occurs in a title 11 case → **excluded from gross income**, § 108(a)(1)(A) — taxable
  inclusion **0.00**. (The exclusion is unlimited for title 11 discharges; no insolvency computation
  is needed.)
- Timing: the discharge occurs on the **effective date, 9/30/2026** (Dkt. 214), so COD income arises
  in the taxable year containing that date and the §108(b) reductions are made **after** the tax for
  that year is determined (irc_108.md (b)).
- Attribute reduction, § 108(b)(1), in the statutory order — NOLs first:
  6,100,000.00 − 5,460,000.00 = **640,000.00 NOL remaining**.
- **§ 108(b)(5) election: no** — reasoning in cod_schedule.json.
- Book/tax interaction: the 5,460,000.00 gain is a book reorganization item but permanently excluded
  from taxable income; its cost is the NOL reduction, not current tax.

## Assumptions (prominent)

- GUC is the only impaired class; DIP repaid in full at emergence (confirmed plan); the remaining
  16,200,000.00 − 8,400,000.00 = 7,800,000.00 of claims/liabilities is paid in full — composition is
  not itemized in the client file (QUESTIONS.md § Session 3).
- The 60%/40% equity split is of **voting** shares (Dkt. 214 and the term sheet do not say otherwise;
  the entire fresh-start conclusion turns on this — QUESTIONS.md § Session 3).
- PV discount rate for the 24-month GUC stream not provided; installment sizes not stated (only
  "24 months, first installment on the effective date") — QUESTIONS.md § Session 3.
