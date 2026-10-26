# Fresh-start reporting — two-part test (ASC 852-10)

Status: **provisional** — computed from `documents/plan_term_sheet.md` (effective-date basis); to be re-run at
confirmation/effective date. Authority: `library/asc852_fresh_start.md` (FASB ASC 852-10-45-19 through 45-29).

## The test (both conditions must be met)

> Fresh-start reporting is applied upon emergence **only if both** conditions are met: (a) the reorganization
> value of the assets of the emerging entity immediately before the date of confirmation is **less than** the total
> of all post-petition liabilities and allowed claims; **and** (b) holders of existing voting shares immediately
> before confirmation receive **less than 50 percent** of the voting shares of the emerging entity.
> — `library/asc852_fresh_start.md`

## Condition (a) — reorganization value vs. post-petition liabilities and allowed claims

| Input | Amount | Source |
|---|---|---|
| Reorganization value (Corbin Advisors, enterprise value, effective-date basis) | 14,000,000.00 | plan term sheet |
| Post-petition liabilities and allowed claims at effective date | 16,200,000.00 | plan term sheet |
| Test: is 14,000,000.00 < 16,200,000.00? | **YES** — met, by 2,200,000.00 | 16,200,000.00 − 14,000,000.00 = 2,200,000.00 |

## Condition (b) — old-equity voting share

| Input | Amount | Source |
|---|---|---|
| Existing equity's share of reorganized voting equity | **60%** | plan term sheet ("retains 60%; 40% issued to the DIP lender") |
| Test: is 60% **less than 50%**? | **NO** — condition FAILED | 60% ≥ 50% |

The 40% issued to the DIP lender (in satisfaction of fees and as new money) does not change the test: it is measured
by what **holders of existing voting shares immediately before confirmation** receive, and they receive 60%.

## Conclusion

**Fresh-start reporting is NOT adopted.** Condition (a) is met but condition (b) fails; both are required
(`library/asc852_fresh_start.md`).

Consequences the library states expressly for the fail case:

- The entity continues on **historical carrying amounts** — no revaluation of assets to reorganization value and no
  reset of retained earnings (see `emergence_balance_sheet.md`).
- **Liabilities compromised by the plan are stated at the present value of amounts to be paid**, and the **gain on
  discharge is reported as a reorganization item** in the income statement.

## Gain on discharge — arithmetic (book), with the open discount-rate item

| | |
|---|---|
| Carrying amount of compromised GUC claims (allowed per term sheet) | 8,400,000.00 |
| Cash to be paid under the plan (35% over 24 months) | 2,940,000.00 (undiscounted) |
| Gain if payments taken undiscounted | 8,400,000.00 − 2,940,000.00 = **5,460,000.00** |
| **Required measurement: present value of the 24 monthly payments — plan discount rate NOT provided [unknown]** | PV < 2,940,000.00 → gain > 5,460,000.00 |

Illustrative PVs of 24 equal monthly payments totaling 2,940,000.00 (payments at month-end; **illustrations only —
the rate is a plan fact, not in the file**):

| Rate | PV of payments | Gain on discharge |
|---|---|---|
| 0% (undiscounted) | 2,940,000.00 | 5,460,000.00 |
| 5% | 2,792,252.55 | 5,607,747.45 |
| 8% | 2,708,541.59 | 5,691,458.41 |
| 10% | 2,654,679.72 | 5,745,320.28 |

Do not book until the plan's effective interest rate is known. The gain is a **reorganization item** in the income
statement, not an equity adjustment (no fresh-start).

## Reconciliation flags (left open, not plugged)

- Tax COD income (5,460,000.00, excluded — see `cod_schedule.json`) differs from the book gain once the plan
  payments are discounted. That difference is expected and is not an error.
- The 16,200,000.00 "post-petition liabilities and allowed claims" composition is not itemized in the file; it
  presumably includes the plan payments on allowed GUC claims, administrative/ professional claims, and DIP/exit
  items — **unverified**. If the 2,940,000.00 of plan payments are NOT included in the 16,200,000.00, condition (a)
  is unchanged in direction but the margin moves.
- Reorganization value is enterprise value per the term sheet; whether any adjustment (e.g., transaction costs)
  applies to "reorganization value of the assets" as the ASC uses the term could not be verified — the library
  excerpt gives the test, not the measurement details [unverified].
- Assumption: the documented March LSTC items (Mesa 62,400.00 gross, Front Range 7,400.00, Grainger 4,310.00) are
  inside the 8,400,000.00 allowed GUC figure. Mesa's claim stays gross (no netting of the ~11,000.00 coil credit —
  see `session1/response_to_cfo.md` §7).
