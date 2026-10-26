Session 3. Let me read the new documents and the two library files I'll need.

The pattern is clear and matches the flag I carried from Sessions 1–2: equity retains 60%, so the fresh-start test will turn on prong (b). Let me run the arithmetic first.

Resuming Session 3. Arithmetic is done; before writing the deliverables let me confirm the current state of `deliverable/` (QUESTIONS.md, STATUS.md, session3 folder) and re-verify the citation whitelist.

State confirmed: Sessions 1–2 are in place, Q1–Q12 still unanswered, `deliverable/session3/` doesn't exist yet, and `irc_108.md` + `asc852_fresh_start.md` are both whitelisted. Let me re-check the exact CONTRACT.md spec for the Session 3 deliverables before writing.

Contract shape confirmed. Let me quickly check how the earlier MOR JSONs handled the contract shape (strict keys vs. extras) so Session 3's JSON is consistent.

State confirmed: Sessions 1–2 are in place, Q1–Q12 remain unanswered, the library whitelist covers `irc_108.md` and `asc852_fresh_start.md`, and the CONTRACT.md shapes match what I have. Writing the three Session 3 deliverables now, per the validated arithmetic.

The parallel block exceeded the output budget. Reissuing one file at a time, starting with `cod_schedule.json`.

`cod_schedule.json` is in. Now `fresh_start.md`.

Now `emergence_balance_sheet.md`.

All three Session 3 deliverables are written. Now updating `deliverable/QUESTIONS.md` — header note plus the three new questions.

Now the `deliverable/STATUS.md` rewrite covering all three sessions.

Final validation run — JSON shape, arithmetic, and a check that everything in `deliverable/session3/` is in place.

One artifact to fix: a soft hyphen snuck into "restate­ment" in STATUS.md.

Session 3 is delivered. Status: **COMPLETE WITH OPEN ITEMS**.

## Deliverables — `deliverable/session3/`

**`cod_schedule.json`** (contract shape, validated by assertion)
- Debt discharged 9/30/2026: **$5,460,000** = allowed GUC $8,400,000 − 35% plan recovery $2,940,000 (the term sheet's "balance discharged on the effective date")
- COD income $5,460,000 → excluded in full under §108(a)(1)(A) (`irc_108.md`)
- Attribute reduction per §108(b)(1): **NOL $6,100,000 → $640,000**; nothing left for attributes (B)–(G); fixed-asset basis $3,200,000 untouched
- **§108(b)(5) election: No.** The default order ends inside the NOL. Electing would wipe out all $3.2M of depreciable basis and still leave $2,260,000 of exclusion to place — where that remainder goes after basis is exhausted isn't covered by the library (labeled unverified). Even on the favorable assumption it goes to NOL, the election just swaps certain depreciation deductions for an equal-face NOL ($3,840,000 either way) that is worth less because it only pays against future income.

**`fresh_start.md`**
- Prong (a): $14,000,000 reorg value < $16,200,000 post-petition liabilities + allowed claims → passes
- Prong (b): old equity retains **60%**, needs < 50% → **fails**
- Both required → **no fresh-start reporting**. Downstream: plan payables at present value, gain as a reorganization item in the income statement, no asset revaluation or goodwill.

**`emergence_balance_sheet.md`**
- LSTC $8,400,000 derecognized against plan payables $2,940,000 (undiscounted placeholder) and a **$5,460,000 gain** in reorganization items — final gain = $8,400,000 − PV, so it rises once the PV is known
- Pre-petition/post-petition kept separate throughout; DIP repaid from exit financing; tax footnote ties to the §108 schedule.

## Open items (added to `QUESTIONS.md` as Q13–Q15; Q1–Q12 still awaiting answers)
- **Q13** — GUC installment calendar and the discount rate → PV restatement of plan payables
- **Q14** — any 2026 discharge-year NOL, confirmation no other §108(b) attributes exist, and tax rates
- **Q15** — exit financing terms, final DIP payoff, 9/30 carrying values, DIP fees settled in the 40% equity

`STATUS.md` now covers all three sessions, including the correction that the §108 schedule depends on Q14 (attributes/rates), not Q4.