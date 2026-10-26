Code Mode runs JS, but the contract wants shell/Python — running calculators via shell:

Arithmetic verified. Writing deliverables now.

Cleaning up a few drafting glitches:

Now QUESTIONS.md and STATUS.md:

Fixing a stray non-English artifact in STATUS.md and validating the JSON files:

Float artifact only — math checks out. Final coherence check on the advice file:

Removing the stale duplicated paragraph at line 50:

Verifying the deliverables landed in the aliased workspace path:

The files went to a parallel `/workspace` path — moving them into the real deliverable folder:

Engagement complete. All deliverables are in `workspace/deliverable/` (`STATUS.md`: **COMPLETE WITH OPEN ITEMS**).

## What I found

**The "equal halves" is not equal after tax.** Nominal 770,000 each becomes:
- **Wife: 613,008** — house equity 700,000 − 66,000 selling costs − 90,992 tax (§1041 carryover basis 300,000 → gain 734,000; single §121 exclusion 250,000 → 484,000 taxable × 18.8%) + 70,000 cash/car
- **Husband: 658,960** — 401(k) 400,000 at his assumed 24% (= 304,000) + brokerage 300,000 − 15,040 tax on 80,000 gain + 70,000 cash/car
- **Gap: 45,952 his favor** — §14-10-113(1)(d) expressly makes this argument statutory.

**Leverage found in the documents:**
- **Concealed bonus:** sworn affidavit says "none expected," but an HR letter five months earlier shows a $45,000 target bonus with him at 112% of plan → **$50,400 expected 2026 bonus**, corroborated by $27,212 unexplained YTD gross. Rule 16.2(e) authorizes reopening and an **unequal division** as sanction.
- **Wrong maintenance tax claim:** "deductible to Husband and taxable to Wife" is unavailable post-2018 (§71/TCJA) — it's tax-free to her either way, but he loses the deduction, which argues on the 36-month term.
- **Correct child support: 2,042/month** (combined net 18,876 → basic 3,050; his share 66.95%) vs. his salary-only inputs — range 1,830–2,294 across scenarios.
- **Form 8332:** recommend she sign no release; his "alternating years" plan trades away child tax credits, while head-of-household/EITC/care credits can't transfer to him anyway.

**Alternatives priced in `division.json`:** (A) same structure + ~23,000 cash equalization → 636,008/635,960; (B) sell pre-decree with the $500,000 joint §121 exclusion (saves 47,000, equalizes both at ~619,484 — but breaks her keep-the-house goal); (C) the unquantified Rule 16.2(e) unequal-division route.

`advice.md` covers the house decision (refinance ≈ $2,648/mo on ~26% of gross — lender underwriting flagged as outside the library) and the QDRO/instruments checklist; `QUESTIONS.md` has 7 refinement questions for the (scripted) client — none blocking.