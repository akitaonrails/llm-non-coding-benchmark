# STATUS — Dana Okafor 2025 Schedule C / Schedule SE

**State: complete.** All client answers received and applied; the client confirms no
further information exists. Four residual unknowns are flagged in place (not re-asked).

## Bottom line

| Item | Amount |
|---|---|
| Line 1 gross receipts | $50,750.00 |
| Line 28 total expenses | $11,778.63 |
| Lines 29/31 net profit | $38,971.37 |
| Schedule SE net earnings (×92.35%) | $35,990.06 |
| Schedule SE tax (×15.3%) | $5,506.48 |
| Deductible ½ SE tax (Sch 1 line 15) | $2,753.24 |

Line detail: 9 = $999.60 · 10 = $1,199.15 · 15 = $480.00 · 20b = $2,800.00 ·
24a = $1,030.00 · 24b = $95.00 · 25 = $1,116.00 · 27a = $4,058.88.

Off Schedule C: W-2 $24,800.00 (1040 line 1a) · BCBS $3,040.00 (Sch 1 line 17) ·
½SE $2,753.24 (Sch 1 line 15) · federal ES payments $6,500.00 (payment credits —
treatment beyond library, **UNVERIFIED**) · 2024-12-27 Tessaro $3,000.00 (2024 year) ·
personal rows (IRC 262).

## Client answers applied this round (Q1, Q2, Q5, Q9a)

- Q1 → line 1 stays $50,750.00: PayHub 1099-K gross $41,350.00 (Beacon $18,500 +
  Orchard $12,200 NECs are inside it) + Tessaro direct ACH $9,400.00 (NEC ties exactly).
- Q2 → Denver flight $389.00 personal (cousin's wedding); line 24a = $1,030.00 SF only.
- Q5 → phone/internet at 60% business: line 25 = $1,860.00 × 0.60 = $1,116.00
  (was 80%/$1,488.00; net profit and SE tax updated accordingly).
- Q9a → BCBS is her own post-Larkspur policy; $3,040.00 stays off Schedule C on
  Sch 1 line 17; documents corroborate the timing.

## Flagged unknowns (client has no additional information — flagged, not re-asked)

1. MacBook $2,149.00 expensed at assumed 100% business use (de minimis safe harbor).
2. Mileage log page 2 missing; 1,150 "misc" miles included in line 9, unsubstantiated.
3. Home-office status unknown; 2,232 coworking miles excluded as commuting.
4. $1,090.00 Larkspur payroll-credit gap vs W-2 — 1040-side reconciliation item only.

## Verification performed

- Re-extracted every document (`pdftotext -layout`) and re-summed every component from
  the 149-row bank export in the same process as writing: PayHub payouts $40,150.85
  (= 41,350 × 97.1%), Tessaro ACH $9,400.00, phone $1,020.00, internet $840.00,
  BCBS $3,040.00, Hiscox $480.00, coworking $2,800.00 (8 × $350), Adobe $719.88,
  Figma $540.00, MacBook $2,149.00, flight $412.00, hotel $618.00, meals $190.00,
  DESIGNWEEK reg $650.00, IRS ES $6,500.00, Larkspur credits $19,502.80 — all tie.
- Mileage log p.1 rows sum exactly to 4,860 (1,200 + 2,232 + 1,150 + 278); line 9 math
  1,428 × $0.70 = $999.60 re-checked; her 0.655 rate rejected per Notice 2025-5.
- `classification.csv`: all 149 rows row-identical to the bank export; distribution
  63 business_expense / 50 personal / 16 other_schedule / 15 business_income /
  3 tax_payment / 2 prior_year; notes updated for the client answers.
- Only `workspace/library/` materials cited (5 excerpts per INDEX); anything outside
  the library is labeled **UNVERIFIED**.

## Deliverables

`workspace/deliverable/`: `schedule_c.json`, `schedule_c.md`, `classification.csv`,
`QUESTIONS.md`, `STATUS.md` — all rewritten to this final state.
