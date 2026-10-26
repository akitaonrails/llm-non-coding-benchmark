

I'll do a systematic audit: (1) re-verify every computation independently, (2) check each cited authority actually exists in the library files, (3) cross-check numbers between deliverables, (4) check reconciliation claims. Starting by re-reading the library and deliverables:






Library confirmed — every authority I cited has a basis there. Now reading the remaining deliverables in full to audit each claim:





All fixes identified. Applying them — six edits to `advice.md`, four to `division.json` (they're independent anchors, so in parallel):














All ten edits are applied. Now re-validating both JSON files and checking `STATUS.md` for the audit entry:






Schema matches exactly — my check key was wrong, not the file. Verifying nested keys quickly, then adding the round-4 audit line to STATUS.md:





Both schemas fully conform. Adding the round-4 audit entry to `STATUS.md`:





Final sweep to confirm no stale references survive anywhere in the deliverables:





Audit complete. The only grep hits left are inside `STATUS.md`'s own audit log (quoting the old wording to describe the fix — intentional). Both JSON files re-validated against the CONTRACT schemas, and all five deliverables are final.

## What I found and changed

**Unsupported authority (2 fixes — the most serious find)**
- `advice.md` §2A said the Columbia equitable-distribution factors "consider the children's custody and each party's needs," cited to `columbia_equitable_distribution.md`. That's wrong: the library excerpt lists **only** economic circumstances, contributions, and tax consequences of the division (§113(1)(d)). Both passages corrected to cite exactly what the library says; the related "no court realistically evicts two children over an equalization figure" point is now explicitly labeled as practical judgment **outside the library**, not cited authority.

**Reconciliation error (1 fix)**
- `division.json` Alternative A had a $104 asymmetry (Wife 637,556 / Husband 637,452) caused by rounding the equalizing QDRO face to 32,300 (0.76 × 32,300 = 24,548 vs the exact half-gap of 24,496). Re-derived properly: 24,496 ÷ 0.76 = 32,231.58 → face **32,232**, both sides ≈ **637,504**, with the 64-cent whole-dollar rounding residual disclosed in the file.

**Wording precision (2 fixes)**
- "Sell now while both $250k exclusions can be used" → the **$500,000 joint-return §121 exclusion**, flagged as requiring both parties and a joint return in the sale year.
- Sale trigger "youngest completes **6th grade**" — a detail I invented, and one that would actually fire *earlier* than the client's stated goal ("until the kids make it through middle school, 3–6 years"). Changed in all three places to "youngest finishes middle school (client's stated 3–6-year objective; exact date a drafting choice)."
- $2,544/yr → **$2,541/yr** (211.74 × 12).

**What was checked and held up**
- Full library re-read: every other citation (IRC §1041/§121, QDRO/§72(t)(2)(C), filing-status/§152(e), support guidelines worksheet + bonus rule, §113 + Rule 16.2(e), tax-rate conventions) traces correctly to `library/INDEX.md` files.
- Independent Python recompute of every number: mortgage payments (2,648.15 / 2,423.98), housing ratios (58.73 / 43.82 / 35.09%), proposal after-tax (613,008 / 662,000, gap 48,992), all four sensitivities, child support (2,041.74 plus the three variants), Alt B/C pot (1,322,008 → 661,004 each), joint-sale saving (47,000). Everything reconciles.
- The **~$2,012 pay-stub residual stays deliberately open** per the contract's "never force it to balance" rule — flagged in all files and in QUESTIONS.md.

No core figures changed — the advice and recommendations stand as delivered. `STATUS.md` now carries the round-4 audit entry; deliverables remain **COMPLETE WITH OPEN ITEMS** (U1–U11 unknowns, none of which block delivery).