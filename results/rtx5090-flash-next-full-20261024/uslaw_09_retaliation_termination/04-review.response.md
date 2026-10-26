Reviewing all five deliverables against the client file and the library line by line.

More JSON fixes — the ADEA substantive-law gap, comparator-scope overstatement, and the HWE elements caveat:

Now re-reading the first half of `advice_to_hr.md` to get exact text before editing:

Applying the advice-document corrections (timeline reconciliation note, comparator scope, "forfeits defense" overstatement, eligibility conditionality, and the PIP-day arithmetic error):

One edit missed (investigation bullet) — re-reading that section for exact text:

Indentation was three spaces, not four. Retrying:

Before finalizing, verifying every case/statute reference against the actual library files:

Library fully supports the frameworks used. Final edits — consideration caveat in the terms document, and the QA record in STATUS:

Final validation — JSON schema, leftover-error scan, and arithmetic re-check:

Review complete. All five deliverables were checked line-by-line against the client file and all six library documents. **Changes made:**

**Errors fixed**
1. **Arithmetic error** (`advice_to_hr.md` addendum): said the planned termination was "~10 days into" the 60-day PIP. 09-16 → 10-06 is **day 20 of 60**, with 40 days left to run. Corrected.
2. **Unreconciled fact**: the timeline calls the PIP "the first written performance document in her file," but her file contains seven years of written annual reviews. Everywhere it appears, it now reads "first *formal corrective plan*" with the reconciliation noted (advice doc timeline table, performance section, addendum).
3. **Scope overstatement**: "she is the only person on a PIP" → "of the five Account Managers in `comparator_data.csv`" (JSON comparator_analysis + advice doc); no data on other employees is an open item.

**Unsupported authority flagged or re-grounded**
4. **"PIP actionable under Burlington Northern analysis"** — the library carries that case only as a citation, with no adverse-action doctrine text. Proposition removed; PIP-standing-alone actionability labeled UNVERIFIED (conclusion unchanged: termination itself is plainly adverse).
5. **ADEA substantive law** — the library's ADEA file covers *only* §626(f)(1) waiver rules. The 40-and-over threshold and younger-comparator framework appear nowhere in the library. Claim renamed "Age discrimination (ADEA theory — substantive standard UNVERIFIED)"; library-backed parts kept (defective release bars nothing; comparator pretext via the Title VII framework).
6. **FMLA retaliation statute route** — the library's §2615(a)(2) text reaches "opposing any practice made unlawful"; whether it covers a leave *request* is unresolved in the library. The grounded route is now stated as §2615(a)(1) + §825.220(c) negative-factor rule.
7. **"Direct evidence conceded" for Title VII** — no recorded statement references her *complaint* (the 10-02 email references FMLA leave). Title VII causation restated as decision-maker identity + 4-day proximity + comparator disparity; the direct-evidence label now belongs only to the FMLA theories (JSON + QUESTIONS table).
8. **Overstatement softened**: "delay is itself a violation" → "likely constitutes restraint"; "forfeits the company's best defense" → the library's actual wording, "undermines the Faragher/Ellerth affirmative defense."
9. **Sex-linking of the comments** re-labeled as counsel's inference from the complaint summary (verbatim text still missing), and HWE elements (severity/pervasiveness) marked UNVERIFIED — not in the library.

**Assumptions now disclosed**
10. FMLA ratings are expressly **conditional on eligibility** — if she's ineligible the FMLA theories drop away (Title VII/state stand alone); covered-family-member question (mother, post-surgery) added to the UNVERIFIED list. The earlier claim that the FMLA theory "doesn't depend on eligibility being resolved" was wrong and is deleted.
11. New flag: the 4-week severance satisfies §626(f)(1)(D) only if no pre-existing severance entitlement exists — no severance policy appears in the file (corrected-terms doc).

**Verified clean (no change needed)**: every statutory/case cite used — *Oubre* 522 U.S. 422, *Faragher/Ellerth*, §825.220(c), §626(f)(1)(A)–(G), §2615(a), §2000e-3(a), Rule 37(e), *Zubulake* — is present in the library files; all day counts (4/24/6/3/18 days, PIP end 11-15) and OWBPA gaps (21−7=14, 7−3=4) re-verified; JSON schema still validates (6 claims, 6 defects, 11 course items, `terminate_today: "no"`, `litigation_hold: true`).

Full QA record added to `STATUS.md`; status remains **COMPLETE WITH OPEN ITEMS** — nothing found changed the core advice: don't terminate, hold today, investigate, decide the leave now without Hale.