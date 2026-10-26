# Status

**COMPLETE WITH OPEN ITEMS**

## What was done

Engagement: HR's 2026-10-06 request to terminate Dana Whitcomb (Account Manager, #1187, age 42) "today," and to "confirm we're fine."

Deliverables in `deliverable/`:

| File | State |
|---|---|
| `risk_assessment.json` | Complete, schema-validated (six contract keys: `terminate_today`, `claims`, `separation_agreement_defects`, `comparator_analysis`, `recommended_course`, `litigation_hold`). 9 claims, 11 agreement defects, 12 recommended steps. Updated after the client's reply: PIP-as-adverse-action raised medium → **high**; new claim added for **FMLA interference by inaction** (rated medium); FMLA interference, FMLA retaliation, Title VII retaliation, and the Columbia analog rated **high**. Corrected in the pre-delivery review: Title VII causation is now scored route-by-route (**direct evidence is not available on this count**), the comparator pretext limb now cites the `complaint_filed` column in `documents/comparator_data.csv`, and the spoliation trigger is dated "from 2026-09-16 at the latest and indisputably from 2026-10-06." |
| `advice_to_hr.md` | Complete (15 sections, 0–13 plus §14). Section 0 records the client's four answers and the defense each one eliminates; §10 is a sensitivity test covering 13 open items; §11 covers damage control if the termination proceeds anyway. **§13 re-bases every date to today, 2026-10-26** — complaint 44 days old and uninvestigated; PIP 40 of 60 days elapsed (66.7%), expiring 11/15; FMLA determination 26 days overdue (certification 23); HR's "today" request 20 days stale; earliest compliant OWBPA effective date 11/24, which is **9 days after** the PIP expires, so the PIP must be closed or rebuilt in writing by a non-Hale decision-maker before 11/15. §12 answers HR's follow-up ("at-will + a PIP means we're covered" / "can we do it right after her leave?") and runs both leave-date branches. **§14 (added in the pre-delivery review) records the seven corrections we made to our own work.** |
| `corrected_separation_agreement_terms.md` | Complete. §1 now locked to the **21-day** individual path (45-day group alternative removed as inapplicable), with both runways stated: the original 10/06 delivery (consideration to 10/27, revocation closes 11/03) and the **re-based 10/26 runway** — delivered 10/27 → consideration to **11/17** → revocation closes **11/24**, one day later per day of delay; the current 7+3 form would have purported effective **10/16** and never can. §1 also flags as **UNVERIFIED** what event starts the 21-day clock (`QUESTIONS.md` item 34). |
| `QUESTIONS.md` | Rewritten as residual unknowns only. Answered questions are **not** repeated. §E added with 5 items (29–33) arising from HR's follow-up; **§F added with 2 items (34–35) found in our own pre-delivery review** — the OWBPA 21-day clock trigger (legal gap) and whether the comments continued after 09/12 (factual gap). 35 items logged. |

Bottom line delivered: `terminate_today: "no"`, `litigation_hold: true`.

## Basis and citation discipline

- Every legal citation in every deliverable resolves to one of the six files listed in `library/INDEX.md` (`title_vii_704a.md`, `fmla_2615.md`, `adea_owbpa_626f.md`, `columbia_at_will_exceptions.md`, `litigation_hold.md`, `harassment_investigation_duty.md`). This was verified mechanically against the deliverable text, and re-verified on 2026-10-26 after the §10–11 and litigation-hold-duration additions: zero invalid `library/` references, and every statute/rule/case token used (2615(a), 825.220(c), 2000e-3(a), 626(f)(1)(A)–(G), 24-34-402, Rule 37(e), *Oubre*, *Zubulake*, *Faragher*/*Ellerth*, *Burlington Northern*) appears in library text.
- Facts come only from `documents/` (`timeline.md`, `comparator_data.csv`, `hr_request.md`, `personnel_file_summary.md`, `separation_agreement_draft.md`) plus the client's two written replies.
- The client's answers are quoted verbatim where relied on. They are admissions by a management representative and are treated as such: (1) no investigation in 24 days; (2) the accused wrote the PIP and chose the outcome, HR "just processing"; (3) the certified FMLA request left undecided because "Tom said to wait"; (4) individual termination, no RIF.
- Arithmetic is shown, not smoothed: mean attainment 440 ÷ 5 = 88.0, Whitcomb 2nd of 5; male mean 249 ÷ 3 = 83.0; PIP elapsed 20/60 = 33.3% at the 10/06 request and 40/60 = 66.7% today, closing 11/15 (09/16 + 60 = 14 + 31 + 15); tenure 2,731 days = 7.48 years; severance 4/52 = 7.7% of base; FMLA one year doubled = 104 weeks = 26× the severance; OWBPA runway 21 + 7 = 28 days.
- **Deliberately not reconciled:** the 4-week payment cannot be squared with the exposure it is meant to buy, and the assessment says so rather than forcing a number.

## Open items (client states no further information exists)

The client has now confirmed twice that there is no further information, and has given no authorization to use sources outside `library/INDEX.md`. **The factual and legal record for this engagement is therefore closed as of 2026-10-26.** No answered question has been re-asked, no unanswered question is repeated, and nothing in these deliverables depends on information the client says does not exist. Per `advice_to_hr.md` §10, every open item has been tested in both directions: **`terminate_today: "no"` holds under every assumption set, including the ones that help the company.** Two open items could plausibly change the litigation outcome (not the timing decision) — pre-2026-09-16 CRM/pipeline documentation, and FMLA hours/site eligibility. A third — whether anyone outside Hale's chain can decide — determines whether **any** lawful exit is available later; on the closed record no such person is identified, and that is carried as a flagged assumption rather than a fact. Everything else changes magnitude, not the answer.

Factual gaps, now carried as **flagged assumptions** — see `QUESTIONS.md` §B:

1. No base salary → all exposure expressed as ratios, never dollars.
2. Full agreement form not produced → the § 626(f)(1)(E) attorney advisory is treated as **missing** until produced.
3. Whether any of the 4 weeks is already owed → § 626(f)(1)(D) consideration element unresolved.
4. Retention / auto-deletion settings and CRM permission changes → unresolved; heightens the spoliation risk.
5. **No CRM or pipeline-hygiene documentation predating 2026-09-16 has been produced and none is expected** → assumed not to exist, which leaves the stated performance reason with no contemporaneous support.
6. No comparator CRM-hygiene scores → comparison rests on 2026 YTD attainment, the only shared metric.
7. PIP "100% of quarterly quota" measurement basis → assumed 12 points above 2026 YTD, plan closing 2026-11-15.
8. FMLA eligibility mechanics (1,250 hours; 50 employees/75 miles) → **not** assumed satisfied; only the 12-month service test is met on the face of the file (hired 2019-04-15).
9. Handbook progressive-discipline language; any other Hale complaints; whether any agency charge exists → unknown.
10. Dana Whitcomb has not been interviewed by us; her account is not in the file.

Assumptions added by HR's 10-26 follow-up (`QUESTIONS.md` §E, items 29–33, all confirmed unanswered and carried as assumptions with both branches analyzed): leave start date (**bounded to after 10/26** by HR's own wording); availability of a decision-maker outside Hale's chain; disposition of the PIP; documented concerns about the three non-PIP comparators; whether the contemplated exit has already been communicated.

Legal standards **not in the closed library**, flagged as unverified and therefore not asserted (`QUESTIONS.md` §C and item 34): hostile-work-environment severity standard; substantive ADEA standards including the age-40 protected-class threshold; all FMLA eligibility/designation/notice/cure rules; federal damages caps; Columbia final-pay, limitations period, and implied-contract rules; non-disparagement limits; whether a defective OWBPA waiver also degrades non-ADEA releases; whether a PIP is per se "materially adverse" (the library names *Burlington Northern* in a citation line only); cat's-paw liability; and **what event starts the OWBPA 21-day consideration clock**.

## Corrections made in our own pre-delivery review (2026-10-26)

We re-audited every quotation, citation, date and figure in the five deliverables against `documents/` and `library/`. Verification result: **every `library/` reference resolves to a file in `library/INDEX.md`; every statute, rule and case token used appears in library text; and no document, event or date in the deliverables is invented.** Round one found no invented sources; it did **not** catch everything in the quotation category, which round two addressed (below). Seven substantive corrections were made, recorded in `advice_to_hr.md` §14:

1. `risk_assessment.json` (Title VII retaliation claim) and memo §1: the causation showing is now scored against the library's three named routes, and **direct evidence is expressly *not* claimed for the Title VII count** — Mr. Hale's 10/02 email links the action to her **leave**, which is FMLA evidence. Previously the memo said the company "currently have all three" routes.
2. Memo §1: the 24-day complaint→termination interval is no longer labeled "very close"; proximity rests on the 4-day complaint→PIP interval.
3. `comparator_analysis`, the comparator claim's key facts, and memo §1/§14: the pretext limb "comparators who did not complain" is now cited to the **`complaint_filed` column** in `documents/comparator_data.csv` ("no" ×4, "yes (9/12)" for Dana) instead of being inferred.
4. Memo §5: "anyone over 40" → "any employee the ADEA protects," with the age-40 threshold flagged as outside the closed library.
5. Memo §5, corrected terms §1, `QUESTIONS.md` item 34: new flag that **the library does not state what starts the OWBPA 21-day clock**; our dates run it from delivery of a writing that expressly refers to ADEA rights, labeled as our conservative construction.
6. Memo §8: the library's remedial guidance says the investigation "should be conducted by someone outside the accused's chain of command" — previously rendered as "requires."
7. Memo §2/§8 and `risk_assessment.json`: PIP elapsed time is stated as of today (40/60 = 66.7%) with the 20/60 figure labeled as of the 10/06 request; the spoliation-trigger date in the JSON is now "from 2026-09-16 at the latest and indisputably from 2026-10-06."

`QUESTIONS.md` item 22 was also corrected (the library names *Burlington Northern* in a citation line only; it does not supply the standard), §A now records the `complaint_filed` column as a documented fact, and §F adds items 34–35.

**Round two — verbatim fidelity of quotations.** Sweeping every quoted string in the five deliverables against the source text character by character found several places where we had put our own compression inside quotation marks: the memo's §12 subheadings compressed HR's 10/26 sentence (three are now labelled "Proposition" without quotes; the two kept in quotation marks, including "He wants it done before she goes on leave," are now her exact words); a §0 argument in quotes that no one wrote; a §6 quote of the Hale email trimmed wrongly ("nightmare to move on her" is the document's words); "Exceeds/Meets" as a rating the personnel file never uses; a bolded FMLA rule that dropped "approved or"; a 45-day OWBPA trigger quoted past the library's text ("offered to a group," full stop — the "or class of employees" scope is now flagged unverified, not cited); and the (B)/(E) OWBPA requirements quoted with altered wording in both `corrected_separation_agreement_terms.md` §§4–5 and `risk_assessment.json` defects 8–9; a singular "shifting justification" quoted in four places where the library says "shifting or thin justifications"; two section headings (memo §12, `QUESTIONS.md` §E) that joined non-adjacent sentences of HR's 10/26 message into one quotation; a quoted "Exceeds / Presidents Club (2022)" rating that the personnel file never states as one phrase (now: 2022 rated 'Exceeds' with the note 'Presidents Club', 2023–2025 rated 'Meets'); a quoted 'unwelcoming' standard the library does not use; and our own shorthand ("PIP at 88%, nothing at 79%", "sign it this week") sitting inside quotation marks, now unquoted. All are corrected; `advice_to_hr.md` §14 lists them item by item (14 items). **None of these corrections changes the recommendation**: `terminate_today: "no"`, `litigation_hold: true`, and no rating moved.

## Decisions we need from the client

1. **Authorize sources beyond `library/INDEX.md`** (full 29 C.F.R. Part 825, ADEA/Title VII substantive standards, damages caps, Columbia pay/limitations rules) — or instruct us to keep working on the closed library, in which case items above stay open and any decision is made on an admittedly incomplete record. **Requested twice; not given as of 2026-10-26, so we have continued on the closed library and cited nothing outside it.**
2. Whether to **stop the termination in writing today** and issue (a) the litigation hold, (b) Hale's written removal from all decisions about Dana, (c) a written FMLA determination, (d) an outside-chain harassment investigation. We have recommended all four and can draft them on instruction.

## Not addressed

No independent verification of HR's timeline, no contact with Dana Whitcomb, no review of documents outside `documents/`, no agency or court filings reviewed, no opinion on unemployment insurance, benefits continuation (COBRA), or tax treatment of any payment.
