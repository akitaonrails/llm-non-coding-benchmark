# April MOR — working notes (all arithmetic shown)

Sources: `documents/session2/april_activity.md`; `documents/session2/interim_compensation_order_excerpt.md`
(Dkt. 77); March MOR (roll-forward base); Dkt. 48, 61.

## Part 1

Receipts:
- operating receipts (activity file): **980,300.00**
- DIP draw 4/9: **500,000.00** → receipts **1,480,300.00** (March presentation kept: draws in receipts)
- Facility: 600,000 + 450,000 + 500,000 = **1,550,000.00** drawn of 2,500,000.00; headroom **950,000.00**.
  Exhibit B line-variance (10%) untestable — not in file.

Disbursements:
- payroll 4/10 + 4/24: 398,000 × 2 = **796,000.00**
- post-petition vendor payments: **214,600.00**
- subtotal confirmed: **1,010,600.00**
- H&P interim (Dkt. 77, allowed after 4/29): 140,000 × 80% = 112,000 + expenses 4,200 = **116,200.00** —
  payment date NOT in file → disbursements = **1,010,600.00** (unpaid) or **1,126,800.00** (paid).
- NOT included: DIP interest/fees (no figures anywhere in file) — flagged.

Ending cash (roll-forward):
- 1,771,630.00 + 1,480,300.00 = 3,251,930.00
- − 1,010,600.00 = **2,241,330.00** (H&P unpaid) / − 1,126,800.00 = **2,125,130.00** (H&P paid)
- Both UNDERSTATED by the never-quantified 3/10 swept pre-petition balance (permanent flag).

## Part 2 — post-petition payables roll-forward

3/31 baseline: **207,826.16** = Mesa 3/18 18,900 + H&P 140,000 + Corbin 45,000 + UST 3,926.16
(March vendor invoices Apex 3/22 9,800, FR 3/28 7,650, Grainger 3/15 2,120 were paid in March — 19,570.00.)

Known April movements:
- vendor payments −214,600.00; only 18,900.00 of prior payables existed → **at least 214,600 − 18,900 =
  195,700.00** went to invoices not on the 3/31 books (April invoices) — itemization needed.
- H&P expenses +4,200.00 (served 4/15).
- UST accrual +0.8% × 1,010,600.00 = **+8,084.80** (or 0.8% × 1,126,800.00 = 9,014.40 if H&P paid) →
  accrual balance 12,010.96 (or 12,940.56). Method/estimate carried from March.
- H&P interim −116,200.00 if paid in April (unconfirmed).

Known components at 4/30 (NOT a total — unknown additions remain):
- H&P: 144,200.00 unpaid, or 28,000.00 holdback if interim paid
- Corbin: 45,000.00 (payment restricted — see Part 5)
- Mesa 18,900.00 (application unconfirmed)
- UST: 12,010.96
- unknown: unpaid April vendor invoices, April monthly statements, 4/24–4/30 payroll accrual

LSTC: **74,110.00** unchanged (Mesa 2/2 62,400 + FR 3/5 7,400 + Grainger 2/11 4,310). Dkt. 83 itself says
the Mesa February invoice "remains an unsecured pre-petition claim" — best documentation we could ask for.
Full scheduled LSTC still unknown (permanent flag). Mesa coil receivable ~11,000.00 still un-netted,
collection not evidenced in April receipts (composition of 980,300.00 unknown).

## Part 5 — professional fees (Dkt. 77 replaces the prior assumption)

Dkt. 77 is procedural, not a §330(a) award: statement → 14-day objection → may pay **80% fees + 100%
expenses**; 20% holdback only on Court approval; **no payment for periods before retention date**.

H&P (retained nunc pro tunc to 3/10 → retention bar does not bite):
- statement 4/15: fees 140,000.00 + expenses 4,200.00; no objection by 4/29 (4/15 + 14 = 4/29 ✓)
- allowed interim: 112,000.00 + 4,200.00 = **116,200.00**; holdback **28,000.00**; full amount at final-review risk.

Corbin (retained effective 3/20; statement 4/16 covers 3/10–3/31 → **10 days pre-retention**):
- Dkt. 77 bars payment for the pre-retention portion; file has no allocation → allowed 0, paid 0, holdback 0.
- Illustration ONLY (not booked, day-count pro-rata 22 days): 45,000 × 10/22 = 20,454.55 barred;
  45,000 × 12/22 = 24,545.45 payable; 80% of that = 19,636.36. Actual time records control; ask (QUESTIONS).

## Part 7

Pre-petition payments: **NO** (all April items post-petition; Dkt. 83 confirms Mesa Feb unpaid as pre-petition
claim; 62,400 − 11,000 = 51,400 netting NOT executed). Caveats: vendor itemization; 4/10 pay period coverage.
Outside ordinary course without approval: none; H&P interim is court-ordered procedure; DIP draw under Dkt. 61.

## Cross-check

- March Part 2 baseline + April movements re-foot in Python.
- 207,826.16 = 18,900 + 140,000 + 45,000 + 3,926.16 ✓
- 74,110.00 = 62,400 + 7,400 + 4,310 ✓
- 3,926.16 = 0.008 × 490,770.00 ✓ (March method re-verified)
