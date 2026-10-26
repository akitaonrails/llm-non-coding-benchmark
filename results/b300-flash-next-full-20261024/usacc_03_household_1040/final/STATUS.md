# STATUS

**Status: COMPLETE WITH OPEN ITEMS** (open items = residual unknowns only; see below)

## Deliverables (all present in `workspace/deliverable/`)

| File | State |
|---|---|
| `return.json` | Final. JSON-validated. Contract schema. |
| `return.md` | Final. Full computation narrative, assumptions A1–A4 annotated, §7 arithmetic tie-out, §8 client-response log. |
| `judgment_calls.md` | Final. 12 judgment calls, each with the rejected alternative(s) and the response updates from the client. |
| `QUESTIONS.md` | Round 1 (Q1–Q7) closed; residual unknowns R1–R5 only. |
| `STATUS.md` | This file. |

## Bottom line (unchanged by client answers)

Federal: AGI **$91,350** → taxable income **$59,850** → tax **$6,708** → CTC $2,200 → 8962 excess-PTC
repayment **$1,900** (capped) → total tax **$6,408** vs. withholding $8,730 → **refund $2,322**.
NY IT-203 part-year: residency ends 6/30 (181 days); both spouses' wages fully NY-sourced
($68,000 / $54,000) under the convenience-of-the-employer rule (client-confirmed employee convenience).

## Client round 1 — outcome

Every answer landed in the direction the return was already computed (unrelated tenant / rent never
raised; no contributions or loans since 2021; remote = employee convenience; Form 8332 executed for
the father's 2025 year; Marketplace coverage ended 6/30). **No computed figure changed.**

## Open items (residual unknowns — unresolvable from client or library)

- **R1** Prior-year filed 7203s unavailable; $11,500 opening S-corp basis rests on Marcus's note
  (client-confirmed consistent: no contributions/loans since 2021).
- **R2** Brooklyn lease document not in file; below-market carve-out proviso accepted on client's
  word. If it failed, AGI → $110,900 and 8962 repayment → $3,150 cap (documented alternative).
- **R3** Exact residency end date (6/30 kept; 7/3 alternative documented) — immaterial to wages.
- **R4** NY tax liability not computable — library contains no NY rate schedule; sourcing/day-count
  delivered instead. NY refund unquantified.
- **R5** Schedule A rules and Tampa property tax unknown — standard deduction ($31,500) is the
  library-supported path and wins on all available numbers.

Nothing was invented to close R1–R5; nothing was forced to reconcile. The return as computed ties
internally (§7 of `return.md`).

## Pre-delivery self-audit

Every library citation was re-verified against the six `workspace/library/` files, every source figure
re-extracted from `workspace/documents/`, and the full arithmetic independently recomputed (mainline plus
both documented alternative scenarios). Four presentation/illustration defects were found and fixed — a
stale rejected-alternative cascade in `judgment_calls.md` §1 (now self-consistent: MAGI $94,400 → full
$25,000 allowance → AGI $73,382 / TI $41,882, tax outside the table excerpt), two cents-level display
figures in `return.md` §4 (annual contribution 5,217.46; annual PTC product 7,531.26), and two wrong
prorate illustrations in `judgment_calls.md` §5 ($33,721 / $26,778). **No computed figure changed** —
headline remains AGI $91,350 → tax $6,708 → refund $2,322.
