Good — a full pre-delivery audit. Let me re-read the contract schema, the entire library, and `return.json`, then re-verify every figure and every citation independently.

All six library files re-read. Now re-verify the source documents themselves and re-run every computation from scratch.

Source documents re-verified — all figures match. Now the full arithmetic + citation audit:

All 28 reconciliations pass. The citation grep was truncated — let me see the full citation inventory and check the one `§36B` mention, which is outside the library.

The single `§36B` mention is correctly labeled as outside-library. Now check every explicit filename citation resolves to an INDEX-listed file:

All citations resolve to INDEX files. Now re-read the four narrative deliverables in full to catch unsupported assertions:

Now I need the exact tail of two library files whose endings were truncated earlier (the §280A carve-out wording and the custody-agreement sentence), to confirm my claims match:

Library language confirmed. Now the other three narrative files:

Full audit complete. Findings: **every figure reconciles** (28/28 checks pass, 8962 rounds exactly to 7,531.25) and **every filename cited is in INDEX.md**. But the audit found several places where the write-ups assert form logistics or legal premises that are **not in the library** and were presented without an unverified label — plus one sign-convention trap. Applying the fixes now (labels only — no figure changes):

Now the biggest unsupported-authority item — the "Brooklyn rental is NY-source" assertion, which the library never states (it only sources wages):

Now judgment_calls.md — §8, §9, §10:

The flat-key check was wrong — the schema is nested. Validate properly against CONTRACT.md:

The "mismatch" is only the CONTRACT example's `"..."` placeholder vs. real dependent names — that's schema-conformant. Let me re-verify the 8962 math against the library excerpt one more time, since the JSON shows 5.71 vs the write-up's 5.7115:

The library's formula confirms the 8962 logic (6-month PTC: (1,690 − 91,350×5.71154%÷12)×6 = 7,531.25 ✓, repayment min(2,368.75, 1,900) = 1,900 ✓). However, one real reconciliation flaw has surfaced: `applicable_figure_pct` in the JSON is set to **5.71**, and recalculating from 5.71 gives 7,531.93, not 7,531.25. The write-up uses 5.7115. The JSON should show the full interpolated value so it matches on its own. Let me check where 5.71 appears in the narrative file:

Two precision fixes needed: JSON `5.71` should carry the same 5.7115 the computation uses (so the JSON reproduces 7,531.25 exactly), and the two narrative mentions of "5.71%" should match. Applying:

The last edit batch hit the output limit. Checking current state and redoing the precision fix:

One digit short — using 5.7115385 (rounded to 7 dp, reproduces 7,531.25):

All 21 checks pass and every citation resolves. One last touch — record the pre-delivery review in STATUS.md:

The pre-delivery review is done and everything now reconciles. Here's what I found and what I changed:

## Audit result
- **No dollar-figure errors.** I re-derived every number from the source documents (pdftotext on the PDFs) and the closed library; a 21-point machine re-check of `return.json` passes (AGI 91,350 → TI 59,850 → tax 6,708 + 1,900 − 2,200 = 6,408 → refund **$2,322**; 7203: 11,500 + 16,500 = 28,000; 8582: −21,018 net, 19,550 allowance, 1,468 carryforward).
- Every filename cited in the deliverables resolves to a file listed in `library/INDEX.md`; the one `§36B` mention was already labeled outside-library.

## What I changed
1. **One precision fix in `return.json`** — `applicable_figure_pct` was `5.71`, which recomputes the PTC as 7,531.**93**, not the 7,531.**25** the return uses. It now carries the exact band interpolation `5.7115385` so the JSON reproduces the PTC, excess (2,368.75), and capped repayment (1,900) to the cent. No dollar amounts moved; refund stays $2,322. (This was found by re-deriving the 8962 against the library formula: monthly PTC = 1,690 − 91,350×5.7115385%÷12 = 1,255.21, × 6 covered months = 7,531.25.)
2. **Unsupported-authority labels added** (these rules are *not* in the library and had been asserted without qualification):
   - NY real-property income = NY source (used for the Jul–Dec Brooklyn rent) — now flagged unverified in `return.md`, `QUESTIONS.md` item D, and `STATUS.md` item 2; Jan–Jun rent is taxable as resident-period income regardless, and the federal return is unaffected either way.
   - State/local tax *deductibility* (not just the $10k cap) — labeled; the standard-deduction conclusion holds even if state taxes were excluded entirely (6,480 ≪ 31,500).
   - Form-line logistics (Sch E → Sch 1 line 15; "8962 Part IV" — the library only says line 28; 1040 line 17 per the engagement schema) — relabeled as schema/venue mechanics, not cited authority.
   - 27.5-year depreciation — now stated as the client's own booked computation, not cited authority.
   - CTC refundability mechanics — labeled outside-library and noted as not in play (tax 8,608 > credit 2,200).
3. **Sign-convention note** in `return.md`: `form7203.loss_allowed` (+11,500, basis computation) vs `form8582.loss_allowed` (−19,550, 1040-side) is now called out explicitly as deliberate.
4. **§280A carve-out wording** aligned to the library's conditional: below-market rent to an unrelated tenant doesn't trigger §280A(d)(2)(C) *"if the rent is a fair rental for that lease"* (client-confirmed facts).
5. **STATUS.md** — expanded the not-in-library list (item 4) and recorded the audit outcome.

Final state: `STATUS: COMPLETE WITH OPEN ITEMS` — figures locked at refund **$2,322**; open items unchanged (family-size FPL gap could raise the 8962 repayment to 3,642.38 and drop the refund to as low as 579.62; NY rate tables and prior-year 7203s unavailable in the file).