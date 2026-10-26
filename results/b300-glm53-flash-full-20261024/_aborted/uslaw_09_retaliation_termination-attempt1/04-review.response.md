I'll do a full review pass: re-read every deliverable, verify every citation against the library, and re-run the arithmetic.

Arithmetic confirms three factual errors to fix: tenure is ~7.5 years (not 5.5), certification→termination is 3 days (not 4), and PIP-remaining is 40 days (not 30). Now re-reading the full deliverables to make exact edits:

Now I have the full picture. Quick verification of the exact subsection attribution in the FMLA library file and the hire date, then I'll apply all fixes:

Confirmed: the negative-factor rule is §825.220(c) per the library, and hire date 2019-04-15 (tenure ≈ 7.5 years). Applying all fixes now — starting with `risk_assessment.json`:

JSON independently validated soon. Now the `advice_to_hr.md` corrections:

Now the corrected-separation-terms memo (the two "Missing"/absent claims were asserted against only an *excerpt* of the form — a real correctness issue), plus QUESTIONS.md wording:

Finally, `STATUS.md` — updated verification math and an accurate unverified-items list:

Final validation pass — JSON parse, leftover-error grep, citation audit:

All clean — the "LEFTOVER" hits are inside the self-review log (deliberately quoting the *pre-correction* wording), and the "outside" citation sweep hits are regex artifacts from digit-containing library filenames (`title_vii_704a.md`, `adea_owbpa_626f.md`) plus legitimate self-references to the deliverables themselves and the draft form under review (subject documents, not authorities). One tiny clarification to the STATUS log so future audits don't trip on the quoted errors:

The read may have raced the edit — verifying the final state:

Review complete — everything now verifies against the sources, and the JSON parses clean (7 claims, 8 defect notes, 12 course items, `terminate_today: no`, `litigation_hold: true`).

## What the review found and what I changed

**Arithmetic errors (3) — fixed, verified in `STATUS.md`:**
1. **Tenure was wrong.** I'd twice written "first PIP in five (and a half) years" / "five-year file." Hired 2019-04-15 → 2,731 days ≈ **7.5 years**. Fixed in `advice_to_hr.md` and `risk_assessment.json`.
2. **Certification gap was off by a day.** "Day 4 after the certification arrived" → 10/03 to 10/06 is **3 days**. Fixed.
3. **PIP-remaining was off.** "30 more days to reconsider" → day 20 of 60 leaves **40 days**. Fixed.

**Unsupported authority (2) — now explicitly labeled unverified, per the contract rule:**
4. I had said the PIP/termination "would dissuade a reasonable worker" under *Burlington Northern*. The library cites the case but does **not** spell out that standard — the doctrinal detail is now flagged unverified (`risk_assessment.json`, `advice_to_hr.md`).
5. I had called Dana "42 (protected)" and said a form fails "employees age 40 and over." The ADEA's **age-40 coverage threshold is not in the library** — flagged unverified in all three places it appeared; the record fact (her age, relative ages of peers) stands on its own.

**Overreach against an incomplete document (3) — hedged:**
6. Only §§3, 4, 7, 9, 11 of the separation form were excerpted, but I had asserted the attorney-advisement (§626(f)(1)(E)) and future-claims carve-out (§626(f)(1)(C)) were **absent from the draft**. Both now hedged: "not in the excerpt HR provided — verify against the full form" (JSON defect list and terms memo table).
7. The §626(f)(1)(B) "defect" (ADEA named only in a list) was softened to a *cleanup* recommendation — the library doesn't say a list reference alone fails; restating it removes doubt.
8. Related hedge added in `advice_to_hr.md` ("what happens if you terminate anyway").

**Precision/consistency fixes:**
9. Cited **§825.220(c)** (the subsection the library actually quotes) wherever the negative-factor rule is invoked rather than bare §825.220.
10. Comparator phrasing: "higher than all three of them by 5.0 points on average" → "higher than all three, and **5.0 points above their average**" (she is +5.0 over the 83.0% peer mean).
11. "88–118% of quota every year since 2022" → "every **recorded** year (2022–2026)" (the file's rating rows start in 2022).
12. Rewrote a confusing recusal sentence in the Round-1 update ("documents dated as of your recusal date" → recuse in writing, memorialize, touch no further decision documents); deduped a repeated clause between recommended_course items 3–4; reworded the awkward QUESTIONS.md intro.

**What checked out clean:** all citations trace to the six INDEX.md files; comparator math (83.0% peer average, 88.0% group mean, median 86) and the day-gap table re-verified; the Oubre/§626(f)(1) citations, Faragher/Ellerth quotes, and litigation-hold authorities match the library text.

`STATUS.md` now carries the corrected verification math and a dated self-review log (8 numbered items) quoting the pre-correction wording, so the audit trail is preserved. Status remains **COMPLETE WITH OPEN ITEMS**.