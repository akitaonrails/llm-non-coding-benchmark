

I'll do a systematic audit pass: verify every numeric claim against the source files, every legal proposition against the library's actual text, and cross-file consistency. First, targeted greps for the suspicious spots I suspect.





Now verifying each suspect proposition against the library's actual text before editing:





Library text confirmed. Now applying corrections to `advice_to_hr.md`:







Now `corrected_separation_agreement_terms.md` and `STATUS.md` — reading both in full to catch the ADEA headcount error and any other issues:






The ADEA headcount in §8 is backwards — two of five are 40+, not "all except two." Fixing, plus STATUS updates:






All numbers reconcile. Writing the review log and running the final authority-resolution sweep:





Now the final verification sweep — re-parse the JSON, re-check the two new quotes against library text verbatim, and confirm no stale strings remain:





All checks pass. Quick spot-check that the edited passages read cleanly:





Self-review complete. Every legal proposition was re-checked against the actual text of the six library files, every number recomputed in Python, and **14 corrections** were applied. Full log in `workspace/deliverable/REVIEW_LOG.md`; here's what changed and why:

**Fact / arithmetic errors (5)**
1. **PIP quota claim** ("3 of 5" → **4 of 5** team members below the 100% target — only Lind at 103% exceeded it) in `advice_to_hr.md` and `risk_assessment.json`.
2. **ADEA headcount reversed** in corrected-terms §8: it said "all Account Managers except two" are 40+; actually **two of five** are (Whitcomb 42, Lind 47).
3. **Garbled timeline** in the FMLA claim: said the PIP opened "18 days after the complaint" — the PIP was **4 days** after; 18 days is complaint → FMLA leave request. Both intervals now stated correctly.
4. **"Three-plus days"** → exactly **3 days** (cert 10/03 → termination request 10/06).
5. **"40 days from today"** → anchored to the 10/06 request date (PIP window ends 11/15 regardless of when the memo is read).

**Overstated or misattributed authority (9)**
6. "Destroys" the *Faragher/Ellerth* defense → **"undermines"** — the library's actual word.
7. **Excluding Ortiz from the investigation** was cited as a library rule; the library only requires "outside the accused's chain of command." All four occurrences now labeled *our recommendation on these facts, not the library rule*.
8. **"Respondeat superior"** removed — doctrine not in the library; replaced with a plain statement flagged as out-of-library.
9. **PIP as standalone "materially adverse action"** downgraded and flagged **[UNVERIFIED]** — the library cites *Burlington Northern* but never states its materiality standard.
10. **"Direct evidence" applied to the FMLA claim** now explicitly noted as borrowed from the library's *Title VII* entry, not FMLA authority.
11. **§ 825.220(c)** quoted precisely ("the **taking** of FMLA leave"); the pending *request* is covered via § 2615(a)(1)'s "attempt to exercise" language, now cited as the actual support.
12. **"Dana complained to you"** → "filed with HR — the department you head, which acknowledged it" (the record doesn't say Ortiz personally received it).
13. A **fake-looking quotation** in `advice_to_hr.md` ("very close temporal proximity + direct involvement of the accused" — not verbatim, and "establishes" vs. the library's "may be shown by") replaced with the library's exact wording.
14. Same fix in `risk_assessment.json`: pretext now quotes "disparate treatment of comparators who did not complain" verbatim.

**Final verification passed:** JSON parses and matches the contract schema (`no` / 5 claims / 7 defects / `litigation_hold: true`); all 6 `library/…` cites resolve; every case name and statute cite used appears in its cited library file's text; every quoted phrase is verbatim; date math and comparator deltas reconfirmed; zero stale strings remain outside the audit log itself.

Everything not listed was checked and found correct. `STATUS.md` remains **COMPLETE WITH OPEN ITEMS** — the five factual unknowns in `QUESTIONS.md` §B still stand, none of which affects the core advice: **do not terminate, issue the litigation hold, process the FMLA certification now, and get an external investigator on the 9/12 complaint.**