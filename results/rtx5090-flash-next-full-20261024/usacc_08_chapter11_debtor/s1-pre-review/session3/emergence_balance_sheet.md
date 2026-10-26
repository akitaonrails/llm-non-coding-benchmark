# Emergence balance sheet — presentation of the discharged debt and the gain

Authority: ASC 852-10 (library: `asc852_fresh_start.md`); plan term sheet (`documents/plan_term_sheet.md`);
DIP facts from Dkt. 61 (documents). No fresh-start reporting (see `fresh_start.md`), so the emerging
entity **continues historical-cost accounting**.

## 1. Continuity of amounts (no revaluation)

- Assets stay at their **pre-petition carrying amounts** (as adjusted for normal post-petition activity:
  capex, depreciation, amortization). **No** write-up to the $14.0M reorganization value; **no new goodwill**
  — those are fresh-start mechanics, and fresh-start failed test (b) (existing equity keeps 60% ≥ 50%).
- Liabilities not compromised by the plan (post-petition liabilities, allowed admin claims, exit financing)
  carry over from the case-period balance sheet.

## 2. The GUC claims ($8,400,000.00 allowed) — split into three presentations

| Component | Amount | Presentation on the emergence balance sheet |
|---|---:|---|
| Pre-effective-date (during the case) | $8,400,000.00 allowed | **Liabilities subject to compromise**, reported separately from post-petition liabilities (ASC 852-10-45-4 to 45-6) |
| Retained plan obligation | PV of $2,940,000.00 paid over 24 months (PV < $2,940,000.00; **discount rate not in file — open item**, QUESTIONS.md) | Debt of the reorganized entity at **present value of amounts to be paid**; split into current (next 12 months of payments) and noncurrent; payment schedule not stated — allocation is an open item |
| Discharged balance | $8,400,000.00 − $2,940,000.00 = **$5,460,000.00 face** | **Removed from liabilities** on the effective date — NOT shown as a liability at any amount |

## 3. The gain — reorganization item, then retained earnings

On the effective date (ASC 852-10; library text): liabilities compromised by the plan are stated at PV
of amounts to be paid, and the **gain on discharge is reported as a reorganization item** in the income
statement (not an extraordinary item, and not booked directly to equity):

```
Gain on discharge (reorganization item)
  = allowed claims derecognized            8,400,000.00
  − PV of retained plan obligation                    PV(2,940,000.00, 24 mo)  [rate unknown → open]
  ≥ 5,460,000.00   (equals 5,460,000.00 if undiscounted; grows by the discount)
```

Flow: reorganization-item gain → net income for the effective-date period → **retained earnings/equity**.
Equity also gains from the DIP-to-equity conversion (40% of reorganized equity issued to the DIP lender
in satisfaction of fees and as new money — DIP facility up to $2.5M, draws to 3/31 $1,050,000.00; April
and later draws unknown).

## 4. Liabilities side at emergence (from the file's numbers)

- **GUC plan obligation** at PV (above).
- **Post-petition liabilities and allowed claims: $16,200,000.00** at the effective date (term sheet —
  this is the figure used in fresh-start test (a); on the balance sheet it is stated as actual
  obligations: admin claims/paid-in-course payables, UST fees, any unpaid post-petition goods, etc.;
  detail not in file — flagged). Note the term sheet's $16.2M and the $8.4M GUC pool appear to be
  **separate buckets** ("post-petition liabilities and allowed claims" vs. the allowed pre-petition GUC
  pool being compromised); if the $16.2M was intended to *include* the $2.94M retained plan payments,
  the emergence BS would double-count — **flagged, not forced** (QUESTIONS.md).
- **Exit financing**: DIP repaid in full from exit financing (term sheet). New long-term debt on the
  emergence balance sheet ≈ the DIP repayment amount (draws + fees — **amount unknown**; the DIP cap is
  $2.5M, drawn $1,050,000.00 through 3/31). Flag open.
- **Deferred taxes**: no cash tax on the discharge (§108(a)(1)(A) — see `cod_schedule.json`), but the
  NOL DTA shrinks: attributes reduce $6,100,000 → $640,000 (arithmetic in cod_schedule). Deferred-tax
  measurement details (rates, valuation allowance) are outside the library — labeled unverified; do not
  book a specific DTA without the rate.

## 5. What does NOT appear

- No goodwill, no asset step-up (no fresh-start).
- No liability for the discharged $5,460,000.00.
- No pre-petition/post-petition netting (852-10-45-4 to 45-6), including the Mesa coil receivable
  (~$11,000, client estimate) which stays a pre-petition receivable, not netted against the $62,400.00 LSTC.

## 6. Reconciliation status — explicit

This schedule is presented as **presentation guidance with the file's numbers**, not a balancing trial
balance: the trial balance cannot be built without (i) the asset carrying values, (ii) the discount rate
for the 24-month obligation, (iii) the exit-financing amount, (iv) April+ activity, and (v) resolution
of the $16.2M/$8.4M overlap question. Per the engagement rules these are left open, not forced.
