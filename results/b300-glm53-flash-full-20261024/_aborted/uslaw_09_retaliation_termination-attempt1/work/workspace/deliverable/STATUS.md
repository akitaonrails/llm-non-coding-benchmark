# STATUS

**COMPLETE WITH OPEN ITEMS** — *updated after client's first response (2026-10-06) and second response (same date)*

## What the client's answers changed — round 1
- **Decision-maker confirmed as the accused.** Hale wrote the PIP, drives the termination, and HR is "just processing it." This upgraded the retaliation/interference analysis: the accused is the sole mover, so the "tainted decision-maker" issue is now admitted fact, not inference. Updated in `risk_assessment.json` (claims) and `advice_to_hr.md` (Update section + sequence).
- **FMLA:** never decided, stalled at Hale's instruction ("Tom said to wait"). Added as affirmative interference evidence (FMLA §2615(a)(1)); added recommended steps: written eligibility decision now, on the certification alone; memorialize and preserve the 'wait' instruction.
- **Harassment investigation:** confirmed zero activity — no investigator, no work product. Faragher/Ellerth breach now admitted fact; hold sweep extended to drafts/texts/calendars because no formal files exist.

## What the client's answers changed — round 2 (Lena's three follow-up questions)
- "At-will + PIP = covered?" — answered **no** in `advice_to_hr.md` (Round 2 section): at-will permits no unlawful reason (Col. Rev. Stat. §24-34-402); the Hale-authored PIP is plaintiff's Exhibit A, not a defense; also flagged that Hale is making legal arguments while under complaint.
- "Waiting means we're stuck with her forever?" — answered **no**: limitations run against Dana's claims, not the company's decision rights; the 60-day PIP completes ~2026-11-15; "stuck" only exists because Hale's conduct consumed the lawful path.
- "Right after her leave?" — answered **no, and prohibited in writing** in `risk_assessment.json` recommended_course (items 8–9): terminating on return from protected leave is the §825.220 negative-factor pattern with liquidated (double) damages; any adverse action timed around the leave dates (role elimination, reorg, account reassignment) is equally barred.


## Deliverables status
- `risk_assessment.json` — updated (valid JSON; terminate_today = no; litigation_hold = true; 7 claims; 12 recommended_course items, incl. written prohibition on leave-timed adverse action).
- `corrected_separation_agreement_terms.md` — unchanged in substance, plus dated client-confirmation addendum.
- `advice_to_hr.md` — updated throughout (Update section, Round 2 question-by-question answers, harassment and FMLA sections, recommended sequence).
- `QUESTIONS.md` — rewritten once: answered items removed (not re-asked) and recorded; 7 remaining unknowns flagged explicitly, each marked "client reports no additional information" where applicable. Round 2 raised no new questions needing client input.

## Open items (none block the analysis; all are flagged in the deliverables)
- **Dollar figures unknowable from the workspace:** base pay / 4-week severance value; exposure stays expressed in multiples (FMLA liquidated = 2× lost wages + fees; Columbia compensatory uncapped).
- **Severance-policy entitlement** — affects §626(f)(1)(D) consideration analysis for any future agreement.
- **No neutral decision authority identified** above Hale; no investigator identified; client states no further information.
- **FMLA decision and 9/12 investigation** remain client actions to execute; the deliverables specify who must do them (outside Hale's chain; certification-only eligibility) but the company must staff them.
- **Litigation hold** not yet confirmed circulated; treat as not in force until written confirmation.
- **Scope limits flagged unverified in the deliverables** — each is labeled in place: state-law and FMLA waiver formalities and non-disparagement scope (`corrected_separation_agreement_terms.md`); interim protective measures for Hale (`advice_to_hr.md`, `risk_assessment.json`); the "materially adverse / dissuade a reasonable worker" retaliation standard and ADEA's age-40 coverage threshold (`risk_assessment.json`, `advice_to_hr.md`); FMLA response deadlines; and the caveat that only §§3, 4, 7, 9, 11 of the separation form were excerpted. All require authority outside this workspace.

## Verification
- All citations point to files in `workspace/library/INDEX.md` (`title_vii_704a.md`, `fmla_2615.md`, `adea_owbpa_626f.md`, `columbia_at_will_exceptions.md`, `harassment_investigation_duty.md`, `litigation_hold.md`); anything beyond the library is explicitly labeled unverified in the deliverables.
- Calculations (`python3`, shown in deliverables): below-quota no-PIP average (79+84+86)/3 = 83.0%; Dana 88% = +5.0; full-group mean (79+84+86+88+103)/5 = 88.0%; median 86%; gaps complaint→PIP = 4 days, complaint→termination = 24, FMLA request→termination = 6, certification→termination = 3, Hale email→termination = 4; PIP day 20 of 60 with 40 days remaining; tenure 2019-04-15→2026-10-06 = 2,731 days ≈ 7.5 years; form 14 days short on consideration and 4 days short on revocation.

## Self-review pass (2026-10-06, before delivery)
Corrected in this pass, all verified against sources above (items quote the pre-correction wording):
1. **Tenure math** — "first PIP in five (and a half) years" and "five-year file" were wrong: hired 2019-04-15 → 2,731 days ≈ 7.5 years. Fixed in `advice_to_hr.md` (×2) and `risk_assessment.json`.
2. **Certification gap** — "day 4 after the certification arrived" was wrong: 10/03 → 10/06 = 3 days. Fixed in `advice_to_hr.md`; gap added to this verification list.
3. **PIP remaining** — "30 more days to reconsider" was wrong: 60 − 20 = 40 days. Fixed in `advice_to_hr.md`.
4. **Comparator phrasing** — "higher than all three of them by 5.0 points on average" → "higher than all three, and 5.0 points above their average" (she is +5.0 above the 83.0% peer mean).
5. **Unsupported doctrine labeled unverified** — Burlington Northern's "dissuade a reasonable worker" standard and ADEA's age-40 coverage threshold are not stated in the library; both now explicitly labeled unverified (`risk_assessment.json`, `advice_to_hr.md`, terms memo).
6. **Excerpt-vs-full-form hedging** — the attorney-advisement (§626(f)(1)(E)) and future-claims-carve-out (§626(f)(1)(C)) defects were asserted as absent from the draft, but only §§3, 4, 7, 9, 11 of the form were excerpted; both now hedged ("not in the excerpt provided — verify against the full form") in `risk_assessment.json` and the terms memo. The §626(f)(1)(B) item was likewise softened to a cleanup recommendation, since the library does not say a list reference alone fails.
7. **Citation precision** — the negative-factor FMLA rule is quoted in the library at §825.220(c); corrected in `advice_to_hr.md` (×2) and `risk_assessment.json` where that rule is quoted.
8. Minor: deduped a repeated Hale-decision-authority clause in recommended_course (items 3 and 4); reworded the confusing recusal sentence and the QUESTIONS.md intro; tightened "every year since 2022" to "every recorded year (2022–2026)".
