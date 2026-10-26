

I'll run a full QC pass: re-extract the source PDFs, re-verify every citation against the library, re-check all arithmetic, and cross-check consistency between the six deliverables.





Sources re-extracted. Now verifying every citation against the library:






Library and sources verified. Now reading the deliverables in full to catch unsupported authority and reconciliation problems:






Continuing the QC pass — the reads were truncated, so let me get the full text of all deliverables plus the remaining source lines.






Letter verified in full — citations all check against library. Now the redline, note, JSON, and logs:






Found a typo ("unmaskes" → "unmasks"). Two long lines were display-truncated; let me get their full text plus the remaining deliverables:






QUESTIONS.md and cross-refs mostly check out, but I found a real reconciliation break: the letter (§1, permit bullet) says "our redline adds a signing-time covenant to file and cooperation," and QUESTIONS.md cites redline "§6.1/§6.2" — but the redline has no permit covenant. Also Schedule 4.12 currently mixes warranty/Hardaway items into an employee schedule. Let me finish reading the JSON and STATUS, run the math, then fix everything together:






All six deliverables read. Now the verification pass — JSON validity, schema, enums, and every arithmetic claim:






All verification is done — JSON valid, schema/enums pass, every arithmetic figure reconciles. Now applying the QC fixes. Let me get the exact current text of the sections I need to edit:






Now let me verify the library file list and get exact text for the letter's permit bullet, the note lines, JSON finding 6, and STATUS:






All exact strings confirmed — and one important catch: the library has **no permit file**, so the new §6 covenant section must be built on the data-room facts only, labeled as drafting judgment with no citation claim. Applying all fixes now:














All ten fixes applied. Now the post-fix cross-reference verification pass:





Cross-refs all resolve. Final structural check — redline heading order and any stale Schedule-4.12-scope claims in the JSON/letter:





QC pass complete. Everything now reconciles across all six deliverables. Here's the full report.

## What I checked

- **Every citation re-verified verbatim** against the seven library files: SQL Solutions (1991 WL 626458), Rev. Rul. 87-41, Treas. Reg. §31.3121(d)-1, IRC §3509, Tex. Lab. Code §201.041, 40 TAC §815.134, Akorn (correctly flagged as dicta everywhere it appears), Lazard, Marsh USA, §§15.50/15.51(c), WARN §2101(a)(1)/20 C.F.R. §639.3 — all accurate.
- **All arithmetic re-run programmatically** — every figure reconciles: payroll tax ($46,818 + $378 = $47,196/yr; 3-yr $141.6k), overtime ($18.75 premium, $25.3k–$38.0k/yr, $48.3k ceiling, 3-yr $75.9k–$144.9k), combined $217.5k–$286.5k, doubling scenario $293k–$431k, earn-out ($16k now, $1.7M for max, ~2.3x), price $3.1M, basket 2.4%, known claims $32,800, finding-6 annual $72.5k–$95.5k.
- **JSON re-validated**: parses, 14 findings, schema/enums pass.
- **Confidentiality re-swept**: buyer-facing documents never reveal the Hensley friendship or that he's untold, and never assert the contractors are compliant.

## What I changed (10 edits, 5 files)

**`apa_redline.md`**
1. **Added §6.1–6.2 pre-closing permit covenants** — the letter promised "our redline adds a signing-time covenant to file and cooperation" and QUESTIONS cited "§6.1/§6.2," but no such covenant existed. Now drafted (buyer files reapplication at signing; seller cooperation/access; interim-ops cooperation; no seller closing condition), explicitly labeled as data-room-fact-based drafting judgment — important because the library has **no** permit file, so no citation is claimed.
2. **Fixed Schedule 4.12 scope** — it listed the Hardaway dispute and warranty log, which aren't employee-rep subject matter and wouldn't qualify anything they touch. Moved to the disputes schedule with a drafting note (they still get §7.4(c) disclosed-matters protection there).
3. **Softened the basket market claim** — "market-consistent as a structure (ABA Deal Points Study)" wasn't supported; the library's market data covers caps/survival, not deductible-vs-tipping. Now: no market claim made; the ask is that buyer keep what its own draft gave.

**`note_to_ray.md`**
4. "unmaskes" → "unmasks" (typo).
5. "surviving as long as the audit rights in their own draft" → "60 days past the statute of limitations" — their draft's §4.12 survival, stated accurately.
6. "courts have let buyers do this… (Lazard)" → attributed to the library's practice-note proposition instead, since the library doesn't state that holding.
7. "draws attention to the price split — from you" → "invites IRS scrutiny of the price split" (the library's actual point).

**`diligence_findings.json`**
8. Finding 6: "up to $3.1M **for ~5 years**" → "for the statute-of-limitations-plus-60-days survival period; actual lookback periods not in the library — unverified." The ~5-year figure was invented arithmetic I can't source.

**`STATUS.md`**
9. Same "~5-year-survival" fix; redline contents list now includes the new §6.1–6.2 section.

**`QUESTIONS.md`**
10. Added a note that numbering skips 2 and 6 deliberately (answered/locked), so Q1–Q8 cross-references stay stable.

## Post-fix verification

All cross-document promises now resolve: letter → redline §6 ✓; QUESTIONS §6.1/§6.2 ✓; JSON finding 13's generic "disclose on the schedule" is consistent with the narrowed Schedule 4.12 ✓; letter's "Schedule 4.12 discloses the 1099 arrangement in full" matches ✓; redline heading order follows the APA (§2.4 → §3.3 → §4.12 → §6 → §7.4 → §8.2 → §9.3) ✓. No stale references remain.

STATUS remains **COMPLETE WITH OPEN ITEMS** — the eight open unknowns affect final dollar figures only, each carried as a labeled assumption. Ready for the next buyer move.