# Pre-delivery audit log — corrections applied

Every legal proposition was re-checked against the text of the six files in `library/` (the only permitted authority), every date and statistic was recomputed in Python, and cross-file consistency was checked. What follows is the full list of changes; anything not listed was verified and left as-is.

## Errors of fact / arithmetic (fixed)

1. **PIP quota overstatement** (`advice_to_hr.md` FAQ; `risk_assessment.json` comparator analysis): said the 100% quota target exceeded what "3 of the 5" team members attained. Recomputed from `documents/comparator_data.csv`: four of five finished below 100% (Whitcomb 88, Park 86, Osei 84, Brennan 79); only Lind (103%) exceeded it. Corrected to **4 of 5**.
2. **ADEA headcount reversed** (`corrected_separation_agreement_terms.md` §8): said "all current Account Managers except two are within ADEA protection." Actual: **two of five** are 40+ (Whitcomb 42, Lind 47); three are under 40 (Brennan 35, Osei 29, Park 31). Fixed.
3. **Garbled timeline sentence** (`risk_assessment.json`, FMLA claim): said "the PIP supplying the 'cause' was opened … 18 days after the harassment complaint." The PIP came **4** days after the complaint (09-12 → 09-16); 18 days is complaint → FMLA request (09-12 → 09-30). Sentence rewritten with both intervals stated correctly.
4. **"Three-plus days"** (`advice_to_hr.md` FMLA section): certification pendency is exactly 3 days as of the anchored 10/06 date (10/03 → 10/06). Stated as three days with the dates shown.
5. **"40 days from today"** (`advice_to_hr.md` FAQ): recomputed (PIP opened 09-16 + 60 days = 11-15; 40 days remain at the 10/06 request date). Reworded to anchor explicitly to the 10/06 request date the client's materials use, so the math is not dependent on when this memo is read.

## Unsupported or overstated authority (fixed)

6. **"Destroys the Faragher/Ellerth defense"** (`advice_to_hr.md`): the library says failure "**undermines**" the affirmative defense. Adopted the library's word.
7. **Ortiz exclusion attributed to the library** (`advice_to_hr.md`, `risk_assessment.json` ×2, `STATUS.md`): the library's rule is "outside the accused's chain of command." Excluding the complaint recipient's (Ortiz's) handling is sound practice on these facts but is not in the library — every occurrence now labeled as **our recommendation, not the library rule**.
8. **"Respondeat superior runs the other way"** (`advice_to_hr.md`): doctrine label not in the library. Replaced with a plain statement flagged as a general principle the library does not address (flagged, not cited).
9. **PIP as standalone "materially adverse action"** (`advice_to_hr.md` FAQ): the library cites *Burlington Northern v. White* but does not state that decision's materiality standard. Downgraded to "may itself be a separate adverse action" with an explicit **[UNVERIFIED]** flag on the standalone-actionability point.
10. **"Direct evidence" applied to the FMLA claim** (`risk_assessment.json`): the direct-evidence framework is defined in the library's **Title VII** entry, not its FMLA entry. The FMLA claim's key fact now states the borrowing explicitly (analogized, not cited as FMLA authority).
11. **§ 825.220(c) precision** (`risk_assessment.json`, `advice_to_hr.md`): the library quotes the rule as barring use of "the **taking** of FMLA leave" as a negative factor. Our claim that the pending **request** also can't be a factor now carries its actual support: § 2615(a)(1) reaches interference with the *attempt* to exercise a right.
12. **"Dana complained to you"** (`advice_to_hr.md`): the file says the complaint was filed "with HR," acknowledged by HR; Ortiz heads HR and acknowledged the 10/06 facts, but the record does not say she personally received it. Softened to "filed with HR — the department you head, which acknowledged it" (also in `risk_assessment.json`).
13. **Quotation-fidelity fix** (`advice_to_hr.md`): the Title VII section quoted a composite — "very close temporal proximity + direct involvement of the accused" — that is not verbatim library text and said the pattern "establishes" retaliation where the library says causation "may be shown by" proximity. Replaced with the library's exact quoted language ("may be shown by **very close temporal proximity** (days to a few weeks)").
14. **Quotation-fidelity fix** (`risk_assessment.json`): the pretext key fact put a paraphrase ("disparate treatment of non-complaining comparators") in quotation marks beside the citation. Now quotes the library precisely: "disparate treatment of comparators who did not complain."

## Items checked and found correct (not changed)

- All other date math: complaint→PIP 4d; complaint→FMLA request 18d; request→Hale email 2d; email→termination request 4d; complaint→termination request 24d; PIP ends 11/15.
- Comparator deltas (Whitcomb +9 vs Brennan, +4 vs Osei, +2 vs Park; ranks 2nd of 5); "all men aged 29–35" for the three non-PIP lower performers; seven-year tenure (hired 04/15/2019).
- OWBPA gaps (21−7=14; 7−3=4), the four statutory defects, *Oubre* consequence, 21-day period (individual separation confirmed).
- Remedies lists (FMLA: lost wages, liquidated damages, fees, reinstatement); Columbia uncapped compensatory damages + longer limitations; litigation-hold triggers and sanctions language.
- Every `library/…` cite resolves to a file in `library/INDEX.md`; every case name used (Oubre, Faragher/Ellerth, Burlington Northern, Breeden) appears in the text of the cited library file; `risk_assessment.json` still parses and matches the contract schema.
