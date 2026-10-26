# Fresh-start reporting — two-part test (ASC 852-10)

Status: **final — plan confirmed.** Plan confirmed 9/2/2026 (Dkt. 214); effective date 9/30/2026
(`documents/session3/confirmation_order_excerpt.md`); terms per `documents/plan_term_sheet.md`.
Authority: `library/asc852_fresh_start.md` (FASB ASC 852-10-45-19 through 45-29).

## The test (both conditions must be met)

> Fresh-start reporting is applied upon emergence **only if both** conditions are met: (a) the reorganization
> value of the assets of the emerging entity immediately before the date of confirmation is **less than** the total
> of all post-petition liabilities and allowed claims; **and** (b) holders of existing voting shares immediately
> before confirmation receive **less than 50 percent** of the voting shares of the emerging entity.
> — `library/asc852_fresh_start.md`

## Condition (a) — reorganization value vs. post-petition liabilities and allowed claims

| Input | Amount | Source |
|---|---|---|
| Reorganization value (Corbin Advisors, enterprise value, effective-date basis) | 14,000,000.00 | confirmation order Dkt. 214 (confirms term sheet) |
| Post-petition liabilities and allowed claims at effective date | 16,200,000.00 | confirmation order Dkt. 214 (confirms term sheet) |
| Test: is 14,000,000.00 < 16,200,000.00? | **YES** — met, by 2,200,000.00 | 16,200,000.00 − 14,000,000.00 = 2,200,000.00 |

## Condition (b) — old-equity voting share

| Input | Amount | Source |
|---|---|---|
| Existing equity's share of reorganized voting equity | **60%** | confirmation order Dkt. 214: "old equity retains 60%" (40% to the DIP lender per term sheet) |
| Test: is 60% **less than 50%**? | **NO** — condition FAILED | 60% ≥ 50% |

The 40% issued to the DIP lender (in satisfaction of fees and as new money) does not change the test: it is
measured by what **holders of existing voting shares immediately before confirmation** receive, and they receive
60%. Note the margin: the plan gives old owners 10 points of voting equity above the 50% line — any dilution of
old equity below 50% would have flipped this test, so the conclusion rests on a plan term, not an estimate.

## Conclusion

**Fresh-start reporting is NOT adopted.** Condition (a) is met but condition (b) fails; both are required
(`library/asc852_fresh_start.md`).

Consequences the library states expressly for the fail case:

- The entity continues on **historical carrying amounts** — no revaluation of assets to reorganization value and no
  reset of retained earnings (see `emergence_balance_sheet.md`).
- **Liabilities compromised by the plan are stated at the present value of amounts to be paid**, and the **gain on
  discharge is reported as a reorganization item** in the income statement.

## Gain on discharge — arithmetic (book), with the open discount-rate item

Confirmed payment stream (Dkt. 214): GUC pool $8,400,000.00 paid 35% = **$2,940,000.00 over 24 months, first
installment on the effective date 9/30/2026**. The confirmation order excerpt does not state (i) the installment
frequency within the 24 months, or (ii) any interest rate on the plan payments.

| | |
|---|---|
| Carrying amount of compromised GUC claims (allowed per plan) | 8,400,000.00 |
| Cash to be paid under the plan (undiscounted) | 2,940,000.00 |
| Gain floor, if payments taken undiscounted | 8,400,000.00 − 2,940,000.00 = **5,460,000.00** |
| **Required measurement: present value of the stream — plan interest/discount rate NOT in the record [unknown]** | PV < 2,940,000.00 → gain > 5,460,000.00 |

Illustrations only — **assumed** 24 equal monthly installments of 122,500.00 with the first at t=0 (effective date);
frequency and rate are plan facts not in the file:

| Annual rate | PV of payments | Gain on discharge |
|---|---|---|
| 0% (undiscounted) | 2,940,000.00 | 5,460,000.00 |
| 5% | 2,803,886.94 | 5,596,113.06 |
| 8% | 2,726,598.54 | 5,673,401.46 |
| 10% | 2,676,802.05 | 5,723,197.95 |
| 12% | 2,628,338.09 | 5,771,661.91 |

Frequency sensitivity is small: 8 quarterly installments of 367,500.00 (first at t=0) @8% → PV 2,745,956.72
(gain 5,654,043.28) vs 2,726,598.54 monthly. Do not book the gain until the plan document's payment schedule and
rate (or a chosen discount rate documented in the provision workpapers) are in the file. The gain is a
**reorganization item** in the income statement, not an equity adjustment (no fresh-start).

## Reconciliation flags (left open, not plugged)

- Tax COD income (5,460,000.00, excluded — see `cod_schedule.json`) differs from the book gain once the plan
  payments are discounted. That difference is expected and is not an error.
- The 16,200,000.00 figure is a confirmed finding, but its composition is not itemized in the record. Plausible
  pieces known from the file: allowed GUC claims 8,400,000.00; DIP drawn 1,550,000.00 (interest/fees never
  quantified — item G); approved interim professional fees through 4/30 (H&P 144,200.00 approved basis; unpaid
  balances); UST accruals. The residual is unquantified — **left open**. Direction of condition (a) is not
  sensitive to the residual: adding any unquantified post-petition liability only widens the 2,200,000.00 margin.
- Reorganization value is enterprise value per Corbin/term sheet; whether any adjustment (e.g., transaction costs)
  applies to "reorganization value of the assets" as the ASC uses the term could not be verified — the library
  excerpt gives the test, not the measurement details [unverified].
- Assumption (unchanged): the documented March LSTC items (Mesa 62,400.00 gross, Front Range 7,400.00, Grainger
  4,310.00) are inside the 8,400,000.00 allowed GUC figure. Mesa's claim stays gross (no netting of the ~11,000.00
  coil credit — see `session1/response_to_cfo.md` §7); the 8,325,890.00 documentation gap stays open (item F).
