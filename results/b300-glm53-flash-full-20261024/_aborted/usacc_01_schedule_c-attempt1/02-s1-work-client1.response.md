Client answers reconciled against Q1–Q8:

- **Q1 ✓ resolved** — Beacon + Orchard both through PayHub; Tessaro by bank transfer; 2.9% off the top confirmed → Line 1 stays $50,750.00, Line 10 stays $1,199.15.
- **Q4 ✓ resolved** — phone/internet **60% business** (client estimate, no separate line) → Line 25 becomes 60% × $1,860.00 = **$1,116.00**; this cascades into 28/29/31 and the SE block.
- **Q-built-commuting ✓** — the 1,200 Larkspur miles confirmed commuting (stays excluded); "the rest is client stuff" attests the 1,150 misc miles' business character, but page 2 still doesn't exist → keep $999.60 with substantiation flag.
- **Q5 (Denver) ✓** — cousin's wedding, confirmed personal. SF trip/Tartine: not addressed → stands as drafted.
- **Q8 ✓** — BCBS is her own plan after leaving Larkspur → $3,040 stays on Schedule 1 line 17; no Jan–Apr BCBS premiums exist.
- **Q2, Q6, Q7** — explicitly no additional information → remaining unknowns, flagged.

Only Line 25 changes. Let me recompute the cascade exactly:

All downstream numbers confirmed: Line 25 $1,116.00 → Line 28 $11,778.63 → Line 31 $38,971.37 → SE net earnings $35,990.06 → SE tax $5,506.48 → ½ $2,753.24 (wage base $60,790.06 ≤ $176,100). Now propagating into `schedule_c.json` and `schedule_c.md` (resolved answers incorporated, unknowns re-flagged in place):

First batch applied. Continuing with the remaining MD sections (Line 24a/24b, 25 rewrite, 27a, 28–31, SE table, not_on_schedule_c, data gap, plus a client-response reconciliation section):

Now the not_on_schedule_c rows, data-gap note, and the client-response reconciliation section:

Now rewriting `STATUS.md` to reflect the reconciliation, then a final validation pass:

The engagement is complete for the information available. Final wrap-up:

## What the client's answers changed

**One number changed: Line 25 utilities = $0.00 → $1,116.00** (60% × $1,860.00 = $1,020.00 T-Mobile + $840.00 Spectrum − per her "maybe 60% work" estimate). Cascade: Line 28 $11,778.63 → Line 29/31 **$38,971.37** → SE net earnings **$35,990.06** → SE tax **$5,506.48** → ½ SE tax **$2,753.24** (wage base $24,800 + $35,990.06 = $60,790.06 ≤ $176,100).

**Confirmed, no change:** Q1 — Beacon/Orchard via PayHub (inside 1099-K), Tessaro by bank transfer, 2.9% fee off the top (Lines 1/10 hold at $50,750.00/$1,199.15). Q3 partial — the 1,200 Larkspur miles are commuting (yes, that's commuting), and "the rest is client stuff" attests the 1,150 misc miles. Q5 partial — Denver flight + gift confirmed personal. Q8 — BCBS is her own post-Larkspur policy; $3,040 stays on Schedule 1 line 17.

## Remaining unknowns (explicitly flagged, per her "no additional information")

1. **Q2** — export ends 2025-12-12; +$141.30 SE tax per extra $1,000 of receipts if Dec 13–31 activity exists
2. **Q3** — $805.00 of line 9 rests on log label + attestation; page 2 never provided
3. **Q5(SF)** — trip stands as business on bank evidence without written confirmation
4. **Q6** — MacBook 100% business assumed (each 10% = $214.90)
5. **Q7** — no home office claimed (if one qualified: line 30 + up to $1,562.40 of miles open up)

All pre-computed alternates live in `schedule_c.md` and swap in directly if any of this arrives.

## Deliverables (all validated — `ALL CHECKS PASSED`)

- `schedule_c.json` — final figures + SE block
- `schedule_c.md` — per-line arithmetic, client-confirmation notes, Q1 matrix (reconciled), remaining-unknowns table
- `classification.csv` — unchanged by design (gross bank activity vs. form percentages; e.g., 25 shows −$1,860.00, form takes 60%)
- `QUESTIONS.md` — as sent (answers recorded in STATUS/md, not by rewriting the questionnaire)
- `STATUS.md` — **COMPLETE WITH OPEN ITEMS**, with the answer dispositions and open-item quantifications

One process item to remember at filing: the **de minimis safe harbor election statement** (MacBook, Reg. §1.263(a)-1(f)) must be attached to the return.