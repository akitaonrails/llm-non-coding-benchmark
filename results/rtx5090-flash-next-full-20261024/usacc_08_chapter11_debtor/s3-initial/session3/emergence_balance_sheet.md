# Emergence balance sheet — presentation of the discharged debt and the gain

Authority: ASC 852-10 (library: `asc852_fresh_start.md`); plan term sheet (`documents/plan_term_sheet.md`)
as restated by the confirmation order excerpt (Dkt. 214: **confirmed 9/2/2026; effective date
9/30/2026** — the emergence date); DIP facts from Dkt. 61 (documents). No fresh-start reporting (see
`fresh_start.md`), so the emerging entity **continues historical-cost accounting**.

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
| Retained plan obligation | PV of $2,940,000.00 paid **over 24 months, first installment on the effective date 9/30/2026** (Dkt. 214) (PV < $2,940,000.00; **discount rate still not in file — open item**, QUESTIONS.md) | Debt of the reorganized entity at **present value of amounts to be paid**; split current/noncurrent per the payment schedule. If 24 equal monthly installments: $2,940,000.00 ÷ 24 = **$122,500.00/month**, first paid on 9/30/2026 itself (annuity-due) — installment amount/cadence NOT stated in Dkt. 214, assumption flagged |
| Discharged balance | $8,400,000.00 − $2,940,000.00 = **$5,460,000.00 face** | **Removed from liabilities** on the effective date — NOT shown as a liability at any amount |

## 3. The gain — reorganization item, then retained earnings

On the effective date — **9/30/2026** (ASC 852-10; library text): liabilities compromised by the plan are
stated at PV of amounts to be paid, and the **gain on discharge is reported as a reorganization item** in
the income statement (not an extraordinary item, and not booked directly to equity):

```
Gain on discharge (reorganization item), recorded 9/30/2026
  = allowed claims derecognized            8,400,000.00
  − PV of retained plan obligation                    PV(2,940,000.00, 24 mo, first pmt day-of)  [rate unknown → open]
  ≥ 5,460,000.00   (equals 5,460,000.00 if undiscounted; grows by the discount)
```

**Illustrative PV sensitivity — NOT booked.** Dkt. 214 states 24 months with the first installment on the
effective date (annuity-due), but gives no interest rate and no installment amount. IF the stream were 24
equal monthly installments of $2,940,000.00 ÷ 24 = $122,500.00, discounted at a nominal annual rate with
monthly compounding, PV at emergence (9/30/2026) would be:

| Rate (illustrative) | PV of $2.94M stream | Implied gain (8.4M − PV) |
|---:|---:|---:|
| undiscounted | 2,940,000.00 | 5,460,000.00 |
| 4% | 2,830,363.93 | 5,569,636.07 |
| 6% | 2,777,770.87 | 5,622,229.13 |
| 8% | 2,726,598.54 | 5,673,401.46 |
| 10% | 2,676,802.05 | 5,723,197.95 |
| 12% | 2,628,338.09 | 5,771,661.91 |

PV formula (annuity-due, i = r/12): 122,500 × [1 − (1+i)^−24] ÷ i × (1+i). **Nothing in this table is
booked** — the plan's rate and installment schedule are open items (QUESTIONS.md); the first installment
is paid on the effective date itself, so the balance sheet records the obligation net of (or gross with a
simultaneous cash outflow for) that $122,500.00 day-of payment under the equal-installment assumption.

Flow: reorganization-item gain → net income for the effective-date period → **retained earnings/equity**.
Equity also gains from the DIP-to-equity conversion (40% of reorganized equity issued to the DIP lender
in satisfaction of fees and as new money — DIP facility up to $2.5M, draws $1,550,000.00 through 4/9/2026
per the April MOR; May–August 2026 draws unknown).

## 4. Liabilities side at emergence (from the file's numbers)

- **GUC plan obligation** at PV (above). Illustrative current/noncurrent split (equal-monthly assumption,
  nominal amounts before discounting): of the 24 installments, one ($122,500.00) is paid on the effective
  date itself, the next 12 (t = 1–12 months) = **$1,470,000.00** current, the final 11 (t = 13–23) =
  **$1,347,500.00** noncurrent; cross-foot 122,500 + 1,470,000 + 1,347,500 = 2,940,000. PV split would be
  rate-dependent — same open rate item.
- **Post-petition liabilities and allowed claims: $16,200,000.00** at the 9/30/2026 effective date
  (Dkt. 214 — the figure used in fresh-start test (a); on the balance sheet it is stated as actual
  obligations: admin claims/paid-in-course payables, UST fees, any unpaid post-petition goods, etc.;
  detail not in file — flagged). Note the $16.2M and the $8.4M GUC pool appear to be
  **separate buckets** ("post-petition liabilities and allowed claims" vs. the allowed pre-petition GUC
  pool being compromised); if the $16.2M was intended to *include* the $2.94M retained plan payments,
  the emergence BS would double-count — **flagged, not forced** (QUESTIONS.md).
- **Exit financing**: DIP repaid in full from exit financing (term sheet). New long-term debt on the
  emergence balance sheet ≈ the DIP repayment amount (draws + fees — **amount unknown**; the DIP cap is
  $2.5M, drawn $1,550,000.00 through 4/9/2026, further draws May–August 2026 unknown). Flag open.
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
for the 24-month obligation and confirmation of the installment schedule (the $122,500/month figure is
our equal-installment assumption, not a stated plan term), (iii) the exit-financing amount, (iv) May–
August 2026 activity (April is now recorded — `session2/april_mor.json`), and (v) resolution of the
$16.2M/$8.4M overlap question. The dates are no longer open: confirmation 9/2/2026, effective date
9/30/2026 (Dkt. 214). Per the engagement rules the remaining items are left open, not forced.
