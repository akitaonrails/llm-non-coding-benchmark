I'll do a full pre-delivery audit: re-read every deliverable, re-verify facts against the source documents, re-run all arithmetic in Python, and re-validate `citations.json` against the index.

Memo fully read. Now verifying every fact and quote against the source documents and the library files themselves.

Source documents check out. Now reading all remaining library files to verify every quoted proposition and status.

Statutes and Texas authority verified. Now the remaining case-law files and the jurisdiction note, plus the employment agreement PDF itself.

All library texts, the PDF, HR timeline, and resignation email are now re-verified against the memo text. Now I'll re-run every computation and re-validate `citations.json` programmatically.

Re-issuing the verification in smaller pieces — first the date arithmetic and probability corridors.

The Code Mode runtime won't take that Python. Running it via shell instead, as before.

All arithmetic confirmed. Now the citations validation against `INDEX.md` and the character scan.

The status values match in substance — my parser conjoined two columns. Let me look at the actual INDEX format and re-validate precisely.

Rows have five data columns; re-running the validator with correct column parsing.

Citation integrity is fully validated. Now checking `cite` fields against the INDEX citation strings, and scanning all four deliverables for character anomalies.

The 14 `cite` "diffs" are benign: each JSON cite is the INDEX **Title + Citation** concatenated (e.g. "Edwards v. Arthur Andersen LLP, 44 Cal.4th 937 (2008)"), and titles/citations/statuses all match — no change needed there. Now re-reading the exact memo regions that need fixes.

I have the exact text for the memo fixes. Now reading `memo.md` Part VI prose, plus the current `QUESTIONS.md` and `STATUS.md` for the cross-file edits.

Resuming the pre-delivery fix pass. I have most edit regions in hand; I still need exact text for memo lines 128–140 (formula block), memo VII.4 (~183–212), QUESTIONS §2, and STATUS §3/§5. Reading those now in parallel.

I have all edit regions. Before writing the fixes, verifying three cross-references the new text will rely on: memo section numbering (Recommendation = Part V?), the Part letter for the ancillarity analysis, and the §16600.5(e) location, plus the resignation email's exact wording.

Cross-references confirmed: Recommendation is Part V; the ancillarity analysis is in **Part IV.B** (not IV.D — important, since my new unknown item 2 must cite the right Part); §16600.5 exposure is Part IV.E; and the email indeed never names §925. One more check — the exact framing of the 0.40–0.60 "independent minimum contacts" factor in the memo:

All cross-references check out (the 0.40–0.60 factor = P(independent minimum contacts survive), stated in Part IV.D — so the printed formula did invert the semantics; corridor unchanged since the interval is symmetric about 0.5). Applying all ten fixes now.

All 10 fixes applied cleanly. Now the post-edit validation pass: citations-vs-INDEX re-check, character scan, arithmetic re-verification (including the new printed multiplication), and spot-checks of the edited regions.

Everything validates. Final spot-check that each edited line landed as intended and no stale text remains:

All replacements landed (the two remaining "Part IV.F" references are correct usages — the AB 1076 section). Three final visual checks of lines the grep pattern couldn't fully show — memo line 33, QUESTIONS line 6, and STATUS §5's new ordering:

All checks pass — the audit fixes are applied and the deliverables validate clean. Here is the pre-delivery review result.

## Pre-delivery review complete — what I changed

**Bottom line: no conclusions, probability bands, recommendation, or cited authorities changed.** Every fix was to cross-references, factor semantics, or list completeness.

**memo.md**
1. **Part II table** — `~0.5–9%` → `≈0.5–9.3%` to match the computed corridor in Part IV.G (0.005–0.093). Brief-answer band "0–10%" unchanged.
2. **Part II counterweight paragraph** — the email section was overstated: it never names §925. Rewrote it to the email's actual content (verified verbatim against `resignation_email.txt`: counsel advised §8 is void and Zhao may void the Texas forum/choice-of-law clauses), and fixed the cross-reference `(Part IV.F)` → `(Part IV.E)`, where the §16600.5(e) exposure actually sits.
3. **Part IV.G formula annotation** — the third factor had inverted semantics: the practice note's 0.40–0.60 is *P(independent minimum contacts survive)* (Part IV.D), not its complement. Annotation corrected; printed corridor 0.20–0.44 unchanged because the interval is symmetric about 0.5.
4. **Part IV.G final line** — added the missing derivation: = P(some injunction issues, 0.10–0.31) × P(order has real-world effect, 0.05–0.30) = 0.005–0.093.
5. **Addendum VII.4** — the unknowns list was missing two items tracked in `QUESTIONS.md` §2. Now lists all eight in the same order: added confidential-information-furnished/access-records (item 2) and business objectives/timing (item 8); moved counsel-inquiry after LO-233; rewrote the resolution-posture sentence to map items 1–8.
6. **Part VI prose** — same unknowns list brought to the same eight items.

**QUESTIONS.md**
7. File-status line now also logs counsel's same-day reply to the client follow-up inquiry (*Calderon*/*Westbrook*/FTC rule), renumbered (1)–(4).

**STATUS.md**
8. §3 item 8: `(memo Part VI)` → `(memo Part V)` — the Recommendation is Part V; Part VI is open items.
9. §5 unknowns: reordered to match QUESTIONS §2 (LO-233 now #6, counsel #7) and added #8 (business objectives/timing) — now eight items, identical across memo VII.4, QUESTIONS §2, and STATUS §5.
10. §1 checklist QUESTIONS row: notes "client-inquiry reply logged."

## Verified and unchanged

- **Citations**: `citations.json` re-validated after the edits — 20 entries, one per citable `INDEX.md` row, statuses verbatim (16 in force / 2 superseded / 1 vacated / 1 modified), zero errors, no memo-bank items cited.
- **Arithmetic** re-run: tenure 940 days ≈ 30.9 months; §8 to 2028-09-30; §9 to 2027-09-30; 718 days remaining; offer 14 / signing 19 days after the AB 1076 deadline; 13 days at Kestrel; bands 20–44% (TX law), 10–31% (injunction), 0.005–0.093 (final), with the printed multiplication confirmed (0.10×0.05 = 0.005; 0.31×0.30 = 0.093).
- **Quotes**: every quoted passage re-checked against the library files and source documents; character scan across all four deliverables clean.
- **Record-preservation advisory stands**: the LO-233 ticket and access records are not to be edited, re-characterized, or deleted; remediation advice remains pending the Company's decision.

Outstanding monitors unchanged: no Zhao-side correspondence received; no questions outstanding for the client; §16600.5(e) quantification deliberately not invented absent fee/damages inputs; *Calderon*/*Westbrook* reliance remains blocked until verified texts with current status are supplied for library addition. Deliverables are ready.