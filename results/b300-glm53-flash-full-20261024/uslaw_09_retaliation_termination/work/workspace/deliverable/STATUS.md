# STATUS.md

**Status: COMPLETE WITH OPEN ITEMS**

*(Updated 2026-10-06 after the client's reply; all client answers are incorporated.)*

## Deliverables

| File | Status |
|---|---|
| `risk_assessment.json` | COMPLETE — schema per CONTRACT.md; JSON validated (`python3 -m json.tool` + schema asserts); `terminate_today: "no"`; `litigation_hold: true`; 6 claims; 7 agreement defects; comparator analysis with arithmetic; 8 recommended steps. Client reply incorporated: admitted zero investigation; Hale as effective decision-maker ("Tom wants her out. I'm just processing it"); FMLA hold directed by Hale ("Tom said to wait"); single-employee termination confirmed (21-day OWBPA period applies, 45-day rule inapplicable). Citation audit vs `library/INDEX.md`: NONE outside the index. |
| `corrected_separation_agreement_terms.md` | COMPLETE — term-by-term fix table keyed to 29 U.S.C. §626(f)(1)(A)-(G) [library/adea_owbpa_626f.md]; timeline consequence (≥28 days offer-to-effective); updated to state the 21-day minimum is operative because the client confirmed a single-employee termination (no group program). |
| `advice_to_hr.md` | COMPLETE — plain English; comparator math; PIP math; litigation-hold instruction; new "What the client confirmed on 2026-10-06" section; FMLA and investigation sections updated to the admissions (stop processing at Hale's direction; answer FMLA without his instruction). |
| `QUESTIONS.md` | OPTIONAL deliverable — updated 2026-10-06: answered questions (Q3 decision-maker, Q4 investigation records, Q5 FMLA status, group-program confirmation) recorded and NOT re-asked; 4 remaining asks (full agreement text, severance policy, comparator documentation, compensation figures) + 1 new request (name an independent decision-maker outside Hale's chain of command). |

## Client answers received 2026-10-06 (incorporated; not re-asked)

1. **Investigation records:** "Honestly, nothing. Tom's been traveling. I was going to get to it." — no investigation of any kind.
2. **Decision-maker:** "Tom wrote the PIP and Tom wants her out. I'm just processing it." — the accused is the effective decision-maker; no independent reviewer exists.
3. **FMLA:** not approved or denied; certification received 10/3; "Tom said to wait" — the deferral is at the accused's direction.
4. **Scope:** "Just her. No RIF." — single-employee termination.
5. **Follow-up Q&A (HR, 2026-10-06):** HR relayed Hale's renewed push ("He wants it done before she goes on leave") and the at-will/PIP "covered" theory, and asked whether termination "right after her leave" would be safe. `advice_to_hr.md` now contains a section answering all three ("Tom's three arguments, answered"): at-will ≠ termination for an unlawful reason [library/columbia_at_will_exceptions.md]; the PIP is evidence of pretext, not a shield; a termination timed "before she's out on leave" is interference per §2615(a)(1) [library/fmla_2615.md]; and one timed immediately after the leave is the same retaliation claim with the dates moved [library/fmla_2615.md; library/title_vii_704a.md]. A calendar table shows the shortest lawful path — a matter of weeks, not "forever" (FMLA answer now; investigation starts now; PIP ends 2026-11-15; Q4 completes 2026-12-31 on the flagged quarterly-measurement assumption). The renewed directive is recorded as a new fact in risk_assessment.json (claim 2) and is within the preservation scope [library/litigation_hold.md].

## Open items (non-blocking; listed per contract)

1. **Client replies still outstanding in QUESTIONS.md:** full separation agreement text (only paras. 3, 4, 7, 9, 11 provided); severance policy/entitlement (verifies the §626(f)(1)(D) consideration prong); comparator performance documentation; Dana's compensation figures (for exposure quantification).
2. **Action requested of the client:** name an independent decision-maker for the investigation and any performance decision — HR has confirmed none exists (answers #2 above).
3. **HR determinations still to be made on the merits:** the FMLA eligibility/certification decision (the library contains no eligibility criteria, so none were cited); any post-investigation performance decision on the PIP (which has 40 of 60 days left, ending 2026-11-15).
4. **Assumptions taken prominently in the deliverables** (unchanged by the client reply):
   - The provided separation agreement excerpt (paras. 3, 4, 7, 9, 11) is treated as the complete substantive terms for defect-spotting; DEFECT 4 (missing attorney advisement) is judged from the excerpt only.
   - No severance policy is assumed to exist pending any confirmation, so the §626(f)(1)(D) prong is marked a verification gap, not a confirmed defect.
   - "Quota attainment" is assumed measured per completed calendar quarter (Q1–Q3 on file, 88% YTD); the PIP ends mid-Q4 with no completed quarter inside its window.
   - Age-discrimination strength ("medium") is flagged UNVERIFIED on the substantive standard because [library/adea_owbpa_626f.md] covers only waiver mechanics; it rests on comparator arithmetic.
   - Columbia-specific release requirements are unknown in the library and marked unverified in the terms memo.
5. **Arithmetic shown, nothing forced:** peer mean 352/4 = 88.0 = Dana's YTD exactly; five-person mean 440/5 = 88.0; complaint→PIP 4 days; complaint→termination request 24 days; FMLA request→termination request 6 days; certification→termination request 3 days; Hale email→termination request 4 days; PIP day 20/60, ends 2026-11-15; complaint→10-06 follow-up 24 days; compliant waiver timeline ≥21+7 = 28 days minimum offer-to-effective.
6. **Not done / not owed:** no citation to any file outside `library/INDEX.md` appears in any deliverable (labor-law details outside the library are labeled unverified rather than cited); the contract's working rules prohibiting invented facts are satisfied — client admissions are quoted, not characterized beyond them.

## Final QA pass (pre-delivery review)

Reviewed all deliverables end-to-end against the source documents and the verbatim text of all six library files. Fixes made:

1. `risk_assessment.json`, claim 2: 10-02 email described as "6 days before the termination request" — corrected to **4 days** (the 6-day figure belongs to the FMLA request 9-30 → 10-06).
2. `risk_assessment.json`, comparator_analysis: "Every employee in the PIP-eligible performance band" contradicted Dana's own membership in that band — corrected to "**Every other** employee."
3. `risk_assessment.json`, claim 3: run-on sentence split and reworded ("discriminatory motive" → "retaliatory motive"; Title VII direct-evidence vehicle and FMLA prohibition now separate clauses).
4. `advice_to_hr.md`: "Silence reads as denial" replaced with library-grounded language — §2615(a)(1) reaches interference with "the exercise of or the attempt to exercise" FMLA rights.
5. `advice_to_hr.md`, exposure stack: "A failed retaliation defense also feeds the harassment case" was garbled — rewritten to the library's exact two-part statement (failure to investigate *is itself evidence in a retaliation case* and *undermines the Faragher/Ellerth defense*).
6. `advice_to_hr.md`, calendar table: removed the conflated "prompt = days-to-weeks" gloss (that is the Title VII proximity standard, not the investigation duty's); now states the library requires "prompt and impartial" with no fixed clock.
7. `advice_to_hr.md`: §1 heading parenthetical trimmed to "direct evidence of intent."

Verified without change: every quoted legal proposition checked verbatim against library files (Oubre, §825.220(c), "need not have begun," prompt/impartial/outside-chain, litigation-hold trigger and sanctions, Columbia "longer limitations / uncapped," Title VII proximity-pretext-direct-evidence triad); trend (118→101→96→92→88) and ratings (2022 Exceeds, Meets since 2023) match `personnel_file_summary.md`; 7.5-year tenure matches hire date 2019-04-15; all cross-references (`QUESTIONS-1`, `QUESTIONS-2`) map to the renumbered questions; revalidated — `python3 -m json.tool` clean, schema asserts pass, citation audit clean (no reference outside `library/INDEX.md`).



**Do not terminate Dana Whitcomb today.** Every client answer strengthened the case for this: the accused is the driving force, the investigation is admitted to be nonexistent, the FMLA decision is being held on his instruction, and the selection of exactly one employee — the complainant — has no RIF structure to explain it. Issue the litigation hold, stop processing the termination at Hale's direction, staff an independent investigation of the 9/12 complaint, respond to the FMLA request on the merits without Hale's sign-off, and only then re-examine the performance merits with an independent decision-maker and comparator-consistent standards. The current separation agreement fails OWBPA and must not be presented in its supplied form.
