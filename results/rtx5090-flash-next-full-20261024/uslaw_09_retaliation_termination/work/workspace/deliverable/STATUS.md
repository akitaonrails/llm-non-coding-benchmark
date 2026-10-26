# STATUS — updated 2026-10-06 (after client response round 2 — Lena's follow-up)

**COMPLETE WITH OPEN ITEMS**

## Pre-delivery QA pass (review of our own work)

Re-verified every citation against the six library files and re-ran the arithmetic. Fixes made:
1. **Arithmetic error**: addendum said the termination plan was "~10 days into" the 60-day PIP;
   09-16 → 10-06 is **day 20 of 60** (40 days left). Corrected.
2. **Overclaimed authority**: dropped the "PIP is actionable under Burlington Northern
   analysis" proposition — the library carries that case only as a citation; PIP-standing-alone
   actionability now flagged UNVERIFIED (termination is plainly adverse, so nothing changes).
3. **Unsupported authority**: substantive ADEA doctrine (40-and-over threshold, younger-
   comparator framework) is NOT in the library (the ADEA file covers only §626(f)(1) waiver
   rules) — ADEA claim renamed and labeled UNVERIFIED; library-backed portions (defective
   release bars nothing; comparator pretext via Title VII framework) retained.
4. **FMLA retaliation framing**: library's §2615(a)(2) text covers "opposing any practice made
   unlawful"; whether it reaches a leave request is unresolved in the library — the grounded
   route is now stated as §2615(a)(1) + §825.220(c) negative-factor rule.
5. **Causation precision**: no recorded statement references her harassment COMPLAINT (the
   10-02 email references FMLA leave); Title VII causation restated as decision-maker identity
   + proximity + comparators, not "effectively conceded."
6. **Conditional ratings**: FMLA ratings now expressly assume eligibility; if she is ineligible
   the FMLA theories drop away (Title VII/state stand alone). Covered-family-member question
   (mother, post-surgery) also flagged UNVERIFIED.
7. **Scope fix**: "only person on a PIP" limited to the five Account Managers in
   `comparator_data.csv`.
8. **Wording**: "forfeits the company's best defense" → library's actual proposition
   ("undermines the Faragher/Ellerth affirmative defense"); "delay is itself a violation" →
   "likely constitutes restraint."
9. **Reconciliation**: timeline calls the PIP "the first written performance document in her
   file," but the file contains seven years of annual written reviews — now read as her first
   *formal corrective plan* everywhere.
10. **New assumption flagged**: 4 weeks' consideration satisfies §626(f)(1)(D) only if no
    pre-existing severance entitlement exists (no severance policy in file — UNVERIFIED).

All statutory/case citations (Oubre, Faragher/Ellerth, §825.220(c), §626(f)(1)(A)–(G),
§2615(a), §2000e-3(a), Rule 37(e), Zubulake) verified present in the library files. Day-count
and percentage arithmetic re-verified.

Round 2: Lena relayed Tom's "at-will + PIP = covered" position and asked about terminating
"right after her leave." Answered in `advice_to_hr.md` (Addendum) and reflected in
`risk_assessment.json` (FMLA-retaliation key facts + new recommended-course item):
at-will bars unlawful reasons (`columbia_at_will_exceptions.md`); this PIP is pretext
evidence, not a shield (`title_vii_704a.md`); deferring the discharge until leave ends makes
leave the negative factor (`fmla_2615.md`); the company is not "stuck with her forever" but a
defensible future case requires a new decision-maker, fresh prospective documentation, peer
consistency, and a completed investigation — no backfilling.

All required deliverables exist and have been updated with the client's answers:
- `risk_assessment.json` (schema-validated) — terminate_today: **no**; litigation_hold: **true**;
  6 claims; FMLA interference and Title VII retaliation reinforced by client admissions
  ("Tom said to wait"; "Tom wrote the PIP and Tom wants her out")
- `corrected_separation_agreement_terms.md` — OWBPA period now fixed at **21 days**
  (client confirmed individual termination, no RIF)
- `advice_to_hr.md` — updated with the four client answers and their legal effect
- `QUESTIONS.md` — now a register of **remaining unknowns** (client has no further
  information); answered items not re-asked

## Open items (cannot be closed from the file; do not change the advice)
1. **FMLA eligibility facts** missing; library has no eligibility rules — assumed, UNVERIFIED.
2. **Dollar exposure not quantifiable** — salary missing; only day-count and percentage
   arithmetic shown.
3. **Complaint verbatim text** missing — hostile-environment claim held at medium.
4. **Hale's prior-complaint history** unknown.
5. **PIP target benchmark** not produced — PIP remains presumptively pretextual.
6. **FMLA-release validity** — no authority in the library; UNVERIFIED; release not credited
   as FMLA protection.
7. **Employer coverage thresholds** under Title VII/ADEA/FMLA — not in library; UNVERIFIED.
8. **FMLA reinstatement entitlement** — not in library; UNVERIFIED.
9. **Any "safe" waiting period after leave** — no library authority; UNVERIFIED (proximity
   judged case by case per `title_vii_704a.md`).

Core advice unchanged and unaffected by every open item: **do not terminate; issue the
litigation hold today; investigate via someone outside Hale's chain; decide the FMLA
request immediately without Hale; quarantine the PIP; retire the defective release form.**
