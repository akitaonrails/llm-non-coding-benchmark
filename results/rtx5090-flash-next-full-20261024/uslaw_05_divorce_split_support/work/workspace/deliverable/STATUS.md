# Status

COMPLETE WITH OPEN ITEMS (round 2 — client responses incorporated)

Deliverables written:
- `deliverable/division.json` — proposal nominal $770,000/$770,000; after tax $613,008/$658,960 (gap $45,952 at the stated 24% 401(k) rate; range $13,952–$93,952); undisclosed income FOUND: $45,000 target bonus (HR letter 2026-03-02; possibly $50,400 at 112% of plan) — **now confirmed recurring by client: "always gets a bonus," 2025 ≈ $40,000 (client-reported; corroborate via 2024–2025 W-2s)**; three alternatives with Option C confirmed as the fit for the client's stay-3–6-years goal and Option B as fallback (client cannot refinance $400k on $72k income); maintenance = non-deductible/non-includible (TCJA §11051); dependents → Wife custodial (Form 8332 releases move only the CTC).
- `deliverable/child_support.json` — corrected guideline support $2,022.63/mo (proposal's salary-only figure $1,830.00 is short $192.63/mo); bonus sensitivity $2,004.29 (bonus $40k) – $2,041.74 (bonus $50.4k), same $3,050 bracket throughout.
- `deliverable/advice.md` — full analysis with arithmetic; §3 decision tree updated for the client-confirmed refinance constraint (solo keep off the table; C requires no refinance by Wife, exit trigger = sale; B fallback); §8 updated for the recurring-bonus pattern (affidavit false as to a multi-year pattern); §10 lists all unresolved unknowns.
- `deliverable/QUESTIONS.md` — round-1 questions closed out as an answer log: 2 answered and incorporated (bonus history; refinance constraint); 9 open unknowns converted to discovery/research tasks per the client's instruction not to re-ask.

Open items (do not affect the direction of the advice; client has no further information — all flagged in `advice.md` §10):
1. Wife's marginal tax rate and both parties' ages (59½) unknown — 401(k) split value and Form 8332 pricing use the engagement's 24% convention as a labeled proxy.
2. House running costs (taxes/insurance/HOA/utilities) missing — HOH >half-cost test and full carrying-cost figures provisional; P&I-only ratios are firm ($2,648.15/mo = 44.1% of Wife's gross alone; 26.4% with support; 33.0% after maintenance ends at 36 months).
3. Columbia child-support termination terms and any add-ons/retroactivity rules are not in the library — flagged unverified, not assumed.
4. ~$4,712 of Husband's YTD gross is unexplained even after the September bonus installment — discovery follow-up queued.
5. NIIT on Wife's solo house-sale gain applied per engagement convention though her MAGI is likely below $200k (both values shown: gap $27,560–$45,952).
6. Husband's willingness to remain on title/mortgage (Option C feasibility) unknown — largest negotiation variable; fallback = Option B (sell now), since the client's confirmed refinance constraint rules out solo retention.
7. Bonus history ≈ $40,000 (2025) is client-reported — convert to employer evidence via 2024–2025 W-2s/plan statements in discovery.

## Pre-delivery audit (done; changes applied)

- **Fixed (numeric):** `advice.md` §3 said "≈ $762,700 interest remains" — that figure is total remaining P&I (288 × $2,648.15); interest alone is ≈ **$362,700**. Corrected in place.
- **Fixed (garbled figure):** `division.json` alternative B said the 734,000 gain was "sheltered to 468,000" — the shelter is the **two 250,000 exclusions (500,000)** → 234,000 taxable (117,000 each). The downstream tax figures (21,996 / 17,550 / 39,546) were already correct and are unchanged.
- **Precision (authority phrasing):** `advice.md` §5 non-QDRO language now mirrors `library/qdro_72t.md` ("a distribution to the participant to pay the former spouse is taxable to the participant and, if under 59½, subject to the 10% additional tax"); §9 HOH bullet adds the library's **qualifying-child-living-with-you >half-year** requirement (~70% overnights satisfy it), mirrored in `division.json`.
- **Labeled assumption:** 3.8% NIIT on Husband's brokerage gain is a **conservative extension** of IRC §1411 — the library's stated convention covers only the wife's house gain — now labeled as such in `advice.md` §2 and `division.json` assumptions.
- **Caveat added:** §1's "his slice does not shrink under Option C" holds at the 24% convention and 32%, **not** at the 12% sensitivity — noted with a pointer to §2.
- **Checked and kept (proposed fix reversed):** `child_support.json`'s "$2,311.58/yr" shortfall is **correct** — it is the unrounded difference ($2,022.6316 − $1,830.00 = $192.6316 × 12); an earlier plan to "fix" it to 2,311.56 (which multiplies the rounded monthly figure) was withdrawn.
- **Re-verified:** both JSONs re-parsed and matched to the CONTRACT.md schemas; the full 69-check arithmetic script re-run; all six library files re-read against every citation; all fact claims re-checked against `documents/`.

All citations trace to files listed in `library/INDEX.md` — one nuance: **§408(d)(6)** appears in the *body* of `library/qdro_72t.md` though not in that row's citation column, and is flagged at its citation point in `advice.md` §5. All figures trace to `documents/` plus client round-2 responses, with arithmetic shown.
