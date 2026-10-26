I'll do a systematic review: full re-read of every deliverable, every [L] citation checked against the actual library files, and every number recomputed.

All library files verified. Now cross-checking the contract schema and re-verifying the appraisal figure via pdftotext:

Continuing the review fixes. Let me re-read the current state of the two sections in `recommendation.md` I still need to fix, to get exact text:

JSON read. Now applying the §5(5) entity-layer disclosure and the JSON option-4 assumption disclosure, plus reading the remaining files to fix:

Now the final three fixes — term sheet tag-along, calendar anchor note — plus reading STATUS.md for its note:

STATUS.md gets the review note and a refresh of open item 9 (the CA corporate-tax line now reflects both disclosed readings):

All fixes applied. Now the final validation pass — JSON parse plus component-sum reconciliation across all four options:

Validation passed: JSON parses, schema keys complete, all four options reconcile, 4 options ≥ the required 3. The review is complete.

## Pre-delivery review — what I checked and what I changed

**Audit performed**
- **Authority:** every **[L]** citation in all five deliverables traced back to a real file in `library/INDEX.md`, and the quoted language re-read against the library texts (§1361/§1362(d)(2), §7701(b)(3), §351, §721 + Rev. Procs. 93-27/2001-43, §83(b), §199A, *Watson*, CA §§17941/17942/23153, buy-sell checklist, Form 2553). No citation points outside the library; §1362(g) and other out-of-library points remain labeled **UNVERIFIED**.
- **Arithmetic:** all recomputed — SPT math (161 / 177.3 / 182.3 / 183.0; thresholds 128 / 123 / 122; steady-state line exactly 122), §351 control (~57% fails; $39,000 / $50,000), Watson exposure $27,540, every option's build-up (12,240 + 2×37,296 + 3,300 = 90,132; 3,300 + 2×34,632 + 39,780 = 112,344; +16,650 = 128,994; 800 + 2×43,290 + 39,780 = 127,160), the §5(5) illustration (19,890 + 77,922 + 800 = 98,612), and all date math (Feb 2 + 30d = Mar 4; +90d = May 3; 2 mo 15 d = Mar 15, 2027).
- **Facts:** questionnaire, travel calendar, projections, and the appraisal (via `pdftotext`: $120,000 FMV, $89,000 deducted, $31,000 basis, Coastline, 1/15/2026) all tie to the deliverables.
- **Schema:** `year1_comparison.json` matches the contract's required keys exactly.

**Six errors/gaps found and fixed**
1. **Unsupported factual claim (real error)** — `recommendation.md` §5(5) said Priya's U.S.-person status was "not in the questionnaire." It isn't true: `documents/founders_questionnaire.md` states she is a **U.S. citizen**. Corrected to "confirmed."
2. **Stale internal contradiction** — the §7 "Other" option header still read "only possible after Tomás becomes a resident, **e.g. 2027**," contradicting the round-2 residency analysis. Corrected to "realistically ~2029 on his day pattern, see §2."
3. **Reconciliation gap in prose** — §7's plan-as-stated total ($90,132) omitted the $3,300 entity component that the JSON carries. Now shown explicitly (12,240 + 2×37,296 + 3,300), with the reason the CA fee schedule still applies (election void → LLC stays partnership-taxed for CA).
4. **Entity-layer ambiguity now disclosed, not hidden** — the library literally says "**every** LLC doing business in California pays $800 **and** a gross-receipts fee," which would make corporation-taxed-LLC scenarios $3,300, not $800; which rule actually governs is outside the library. Both readings are now shown wherever it matters: §5(5) ($98,612, up to ≈$101,112), §7 Other option ($127,160, or $129,660), the JSON option-4 assumptions, and STATUS open item 9. Not forced to reconcile, per the engagement rules.
5. **Term sheet inconsistency** — tag-along read "if Priya sells her **control block**"; there is no control block in a 50/50. Made mutual: if either member sells to a third party, the other may join pro rata on the same terms.
6. **Timing caveat added** — the engagement file is dated October 2026, so if formation hasn't happened yet, the assumed Feb–May 2026 calendar dates have already passed. `compliance_calendar.md` now says so bluntly and directs immediate re-anchoring (the 30-day §83(b) and 2-month-15-day election rules have no extension).

`STATUS.md` records that the review was performed and lists these fixes. Everything else — citations, computations, and cross-document consistency — checked out unchanged, and the final JSON re-validated after the edits.