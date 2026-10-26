I'll do a systematic pass: full read-through, then machine-verify quotes, numbers, and citations against the library.

Now machine-verification against the library. First, key quotes and citations:

All library files re-read. Now re-reading the memo in full to cross-check every proposition against these texts:

Three edits applied. Continuing with the remaining fixes — first re-reading the current state of the affected sections to get exact text:

Verifying the exact library wording for the *Marsh* and *Campbell* characterizations before rephrasing:

Library wording confirmed. Applying the memo edits in batch:

Now reading the remaining sections (§4.6 onward, tables, and §9) to apply the final fixes:

Applying the remaining memo fixes:

The L134 line also contains "R&D hub" in its first half — fixing that, plus the remaining items:

Memo edits complete. Now fixing the three citations.json propositions:

Entries are keyed by reporter citation. Inspecting the three propositions to fix:

Re-validating everything — schema, INDEX mapping, and leftover artifacts in the memo:

Review pass is complete. Here is what I found and changed.

## Errors found and fixed

**`memo.md` — citation and characterization errors:**
1. ***Light* reporter cite wrong**: memo said 883 S.W.**3d** 642; the library/INDEX says **883 S.W.2d 642**. Corrected.
2. ***Ixchel* overstated** — the memo (and the authority table) credited *Ixchel* with "enforcement of choice-of-law terms in a thin-California-nexus B2B deal." The library says only: B2B rule of reason, employment context stays with *Edwards*. All "thin nexus" framing removed; the table row now reads just "B2B rule of reason; employment stays with *Edwards*."
3. ***Application Group* mischaracterized** as involving "a multi-state employer" and "employees working for a California business." Library wording: *a Maryland employer's non-compete with an employee recruited to work for a California employer; the Maryland choice-of-law clause did not control.* Memo now tracks that.
4. ***DeSantis* mirrored backwards in spirit**: it was a Florida clause tested against the interests of the state where the employee **worked (Texas)** — the memo/citation said "working in another state." Fixed.
5. ***Marsh* false record cite**: the memo claimed "the file references equity terms not in the excerpt." Nothing anywhere in the produced file references equity or options. Replaced with: the *Marsh* options path exists **only if** the unproduced remainder of the agreement contains such terms — flagged in `QUESTIONS.md`, not assumed. Same qualifier added in §5 (Meridian's best case).
6. ***Sheshunoff* "one-year covenant"**: that detail isn't in the library. Rewritten to what the library supports: ancillarity of a covenant in an at-will agreement via a performed return promise, reasonableness under §15.50 central.
7. ***Campbell* quote inexact**: memo said "a small part of the business"; library (quoting the superseded Ninth Circuit rule) says **"small or limited part of the business, trade or profession."** Quote corrected.

**`memo.md` — unsupported facts / overstatements:**
8. **"R&D hub"** appeared twice as a Meridian Texas contact. No such fact exists in the file. Removed; contacts now stated as the file supports: Austin HQ (per HR file), Austin-administered hiring.
9. **"Two weeks of onsite presence"** → corrected to **two short business trips**, consistent with the HR timeline and the client's confirmation.
10. **LO-233 closing-date speculation**: memo said it was closed "in or around February 2024." The file shows "deprioritized" logged on the Feb. 14, 2024 deadline date and a later closure "won't do" with no closing date. Memo now says exactly that.
11. **§925 counsel framing**: the memo implied Zhao "retained California counsel" as a done fact bearing on §925(e). The file only shows his resignation email reporting an attorney's advice. Reworded to the email's verbatim words ("advises me that §8 is void under California law and that I may void the Texas forum and choice-of-law clauses") and §925(e) is now addressed as: the *contract negotiation* had no counsel — the email is not the exception.
12. **§16600.1(b) company-wide violation overbroad**: previously swept in all post-2022 employees; the fixed Feb. 14, 2024 duty textually reaches those **under contract by the deadline**. Post-deadline hires (Zhao included) now cross-referenced to the already-flagged ambiguity instead.
13. **Probability reconciliation gap**: §2 said 60–80% fee exposure if Meridian sues; Scenario B said 70–85% for the demand-letter path with no bridge. Parenthetical added explaining the demand-letter case sits above the blended range because it completes the (b) violation on its face.
14. **§9 wording fix**: "*Michiana* fallback narrowed" → the confirmed two-trip footprint *is* the practice note's exact "may or may not suffice" fact pattern.

**`citations.json`**: propositions for *DeSantis* (entry 13), *Application Group* (15), and *Ixchel* (17) corrected as above; file rewritten and re-validated.

## What checked out clean (no change)
- Machine validation re-run: 20 entries, exact schema keys, statuses within {in force, superseded, vacated}, every `library_file` maps to an INDEX row.
- All statutory quotes (§925, §16600, §16600.1, §16600.5) verified verbatim against library text; date arithmetic (113 min, 63 days, 940 days, 13-day gap, 731/706-day restraint, 14/19 days) re-verified.
- The remaining grep hits for "thin" were false positives inside "anything/everything/nothing" — no artifacts left.
- No fabricated authorities: the firm-bank cases (*Calderon*, *Westbrook*) remain uncited and flagged; superseded/vacated items are cited only for their negative status.

Probability ranges are otherwise unchanged; **STATUS.md now logs this verification pass** and stays **COMPLETE WITH OPEN ITEMS** (open items unchanged: the §16600.1(b) after-deadline-hire question, §925 recognition in a Texas court, and the unquantified AB 1076 population).