Client confirmed the covenant structure and left the other items unresolved. Updating the deliverables to reflect his answers and flag the remaining unknowns explicitly.

Fixing a stray-character typo in that file:

Now updating the memo's facts (§3d), open items (§9), and the counter justification to reflect the client's answer:

Also updating §9's reference to the question count and the counter doc's Class VI justification:

Finally, updating `STATUS.md` to reflect the new state of open items:

The engagement is essentially wrapped. Let me run a final integrity check on the deliverables before closing out.

All checks pass — the engagement is complete. Final state of the deliverables:

## Deliverables (`workspace/deliverable/`)

| File | Contents |
|---|---|
| `memo.md` | Full 10-section analysis with tied-out arithmetic, citations to library only |
| `comparison.json` | Numeric schema for all scenarios (valid JSON, verified) |
| `form_8594_counter.md` | Proposed §1060 allocation by class with per-class justification |
| `QUESTIONS.md` | Client answer log — Q1 answered, Q2/Q3 flagged unresolved |
| `STATUS.md` | **COMPLETE WITH OPEN ITEMS** |

## Bottom line (network after all taxes)

- **Buyer A stock... as drafted:** **2,232,471** — total tax 867,529 (entity §1374: 21% × NRIG-capped 1,130,000 = 237,300; personal 630,229)
- **Buyer A with counter allocation (3,100,000 unchanged):** **2,327,671** — saves Ray **95,200**, driven by §1245 recapture falling 660,000 → 410,000
- **Buyer B stock sale:** **2,364,000** (tax 486,000) — nominally best but 36,329 short of the countered A
- Ray's naive estimate: 2,480,000 — optimistic by ~247,000 even in the best case

## Recommendation

Counter Buyer A on allocation, not price: Classes V/VI/VII (650,000 → 650,000 held / 400,000 → 100,000 covenant / 2,010,000 goodwill) keep the purchase price identical — Lone Star is tax-indifferent between covenant and goodwill (both 15-year §197 amortization) — and Ray banks 95,200. Fallback if the buyer fights Class VI: fixing only V + IV still saves 96,200.

## Open items (explicitly flagged, none change the headline)

1. **Class V FMV support at 650,000** — the register's `fmv_estimate` has no preparer/date; an appraisal may be needed if Lone Star disputes (worth 92,500 to Ray).
2. **Receivables history** — prior-year bad-debt treatment unconfirmed; if any exists, the Class III "wash" becomes ordinary-gain trap.
3. **Out-of-library legal items** labeled unverified and referred to the return CPA: SE tax on covenant income, Texas franchise tax, §453A/§453B, §1221/§1231/§1253 basis for goodwill-as-capital, §338(h)(10)/§336(e), §1366(f)(2) loss character (+8,211/−32,130 swing quantified), and the illustrative 5% discount rate.