# Fresh-start reporting — the two-part test, with numbers

Authority: FASB ASC 852-10-45-19 through 45-29; 852-10-45-9 (library: `asc852_fresh_start.md`).
Facts: plan term sheet (`documents/plan_term_sheet.md`) as restated in the confirmation order excerpt
(`documents/session3/confirmation_order_excerpt.md`, Dkt. 214: plan confirmed **9/2/2026**, effective date
**9/30/2026**, terms as in the term sheet). Fresh-start applies on emergence **only if BOTH** conditions
are met.

## Condition (a) — reorganization value < post-petition liabilities + allowed claims

Reorganization value of the assets of the emerging entity **immediately before the 9/2/2026 confirmation**
(**Corbin Advisors opinion: $14,000,000.00**, enterprise value, effective-date basis — restated in Dkt. 214)
versus total post-petition liabilities and allowed claims at the effective date (**$16,200,000.00** —
restated in Dkt. 214):

```
14,000,000.00  <  16,200,000.00   →  TRUE — condition (a) is MET (shortfall 2,200,000.00)
```

## Condition (b) — existing voting shareholders receive < 50% of emerging voting shares

Plan term sheet: existing equity **retains 60%** of reorganized equity; 40% goes to the DIP lender
(fees + new money). The test looks at holders of existing voting shares *immediately before confirmation*
receiving **less than 50%** of the emerging entity's voting shares:

```
60%  is NOT <  50%   →  FALSE — condition (b) FAILS
```

(There is no old-equity cancellation/reissuance structure here — 60% stays put.)

## Conclusion — **fresh-start reporting is NOT adopted**

Both conditions are required; (a) is met but (b) fails, so the reorganized entity continues on
**historical-cost (going-concern) accounting** — no revaluation of assets to reorganization value, no
new goodwill.

## Consequences (per the library excerpt, `asc852_fresh_start.md`)

- Liabilities **compromised by the plan** (the GUC balance) are stated at the **present value of amounts
  to be paid**: plan pays $2,940,000.00 of $8,400,000.00 allowed GUCs **over 24 months, first installment
  on the effective date (9/30/2026)** (Dkt. 214) — that obligation is carried at PV(2,940,000), split
  current/noncurrent per the payment schedule. The excerpt does not state the installment amounts
  (if 24 equal monthly payments: $2,940,000.00 ÷ 24 = $122,500.00 each — assumption, see
  `emergence_balance_sheet.md`); cadence/amount confirmation is an open item.
- The **gain on discharge is reported as a reorganization item** in the income statement:
  derecognize the allowed claim and recognize the PV obligation —
  **gain = $8,400,000.00 − PV($2,940,000.00 over 24 months)**. If undiscounted, $5,460,000.00; any
  discount increases the gain. **Discount rate not in the file — flagged open item** (QUESTIONS.md);
  not forced.
- During the case, LSTC remain reported separately from post-petition liabilities (852-10-45-4 to 45-6).
- Contrast for the tax side (see `cod_schedule.json`): fresh-start's non-adoption is an *accounting*
  result only — the §108(a)(1)(A) exclusion and attribute reduction happen regardless of fresh-start,
  because the exclusion turns on the title 11 case, not on GAAP presentation. Also relevant to the
  §108(b)(5) election analysis: because fresh-start is not adopted, historical asset basis survives,
  so voluntarily burning it is unattractive.

## Caveats

- The (a) test uses reorganization value of the **assets** of the emerging entity; we rely on Corbin's
  $14.0M enterprise value as the file's only reorganization-value evidence — if the court finds an
  equity-value-based figure differs, (a) could change. (a) is met on the file's numbers as stated.
- Confirmation and effective dates are now in the file (Dkt. 214: confirmed 9/2/2026; effective
  9/30/2026), so the test date ("immediately before the date of confirmation") is fixed at 9/2/2026 and
  the conclusion is final on the file's numbers: (a) met, (b) fails. The result turns on the fixed 60%
  equity split (restated in Dkt. 214), which timing cannot change.
