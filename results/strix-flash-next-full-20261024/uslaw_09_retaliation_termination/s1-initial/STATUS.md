# Status

**COMPLETE WITH OPEN ITEMS**

## What was done

Engagement: HR's 2026-10-06 request to terminate Dana Whitcomb (Account Manager, #1187, age 42) "today," and to "confirm we're fine."

Deliverables in `deliverable/`:

| File | State |
|---|---|
| `risk_assessment.json` | Complete, schema-validated (six contract keys: `terminate_today`, `claims`, `separation_agreement_defects`, `comparator_analysis`, `recommended_course`, `litigation_hold`). 9 claims, 11 agreement defects, 11 recommended steps. Updated after the client's reply: PIP-as-adverse-action raised medium → **high**; new claim added for **FMLA interference by inaction** (rated medium); FMLA interference, FMLA retaliation, Title VII retaliation, and the Columbia analog rated **high**. |
| `advice_to_hr.md` | Complete. New section 0 records the client's four answers and the defense each one eliminates; sections 3–5, 8–9 revised. Sections **10–11** added 2026-10-26 (no new facts): §10 is a sensitivity test showing which open items could change the outcome, §11 covers damage control if the termination proceeds. |
| `corrected_separation_agreement_terms.md` | Complete. §1 now locked to the **21-day** individual path (45-day group alternative removed as inapplicable) with the dated runway: delivered 10/06 → consideration to **10/27** → 7-day revocation closes **11/03**; the current 7+3 form would have purported effective **10/16** — a lawful deal is ~**18 days** later. |
| `QUESTIONS.md` | Rewritten as residual unknowns only. Answered questions are **not** repeated. |

Bottom line delivered: `terminate_today: "no"`, `litigation_hold: true`.

## Basis and citation discipline

- Every legal citation in every deliverable resolves to one of the six files listed in `library/INDEX.md` (`title_vii_704a.md`, `fmla_2615.md`, `adea_owbpa_626f.md`, `columbia_at_will_exceptions.md`, `litigation_hold.md`, `harassment_investigation_duty.md`). This was verified mechanically against the deliverable text, and re-verified on 2026-10-26 after the §10–11 and litigation-hold-duration additions: zero invalid `library/` references, and every statute/rule/case token used (2615(a), 825.220(c), 2000e-3(a), 626(f)(1)(A)–(G), 24-34-402, Rule 37(e), *Oubre*, *Zubulake*, *Faragher*/*Ellerth*, *Burlington Northern*) appears in library text.
- Facts come only from `documents/` (`timeline.md`, `comparator_data.csv`, `hr_request.md`, `personnel_file_summary.md`, `separation_agreement_draft.md`) plus the client's two written replies.
- The client's answers are quoted verbatim where relied on. They are admissions by a management representative and are treated as such: (1) no investigation in 24 days; (2) the accused wrote the PIP and chose the outcome, HR "just processing"; (3) the certified FMLA request left undecided because "Tom said to wait"; (4) individual termination, no RIF.
- Arithmetic is shown, not smoothed: mean attainment 440 ÷ 5 = 88.0, Whitcomb 2nd of 5; male mean 249 ÷ 3 = 83.0; PIP elapsed 20/60 = 33.3%; tenure 2,731 days = 7.48 years; severance 4/52 = 7.7% of base; FMLA one year doubled = 104 weeks = 26× the severance; OWBPA runway 21 + 7 = 28 days.
- **Deliberately not reconciled:** the 4-week payment cannot be squared with the exposure it is meant to buy, and the assessment says so rather than forcing a number.

## Open items (client states no further information exists)

The client has confirmed there is no further information. No answered question has been re-asked, and nothing in these deliverables depends on information the client says does not exist. Per `advice_to_hr.md` §10, the recommendation was tested against each open item, in both directions: **`terminate_today: "no"` holds under every assumption set, including the ones that help the company.** Only two open items could plausibly change the litigation outcome (not the timing decision) — whether any CRM/pipeline documentation predating 2026-09-16 exists, and whether Dana meets the FMLA hours/site eligibility tests. Everything else changes magnitude, not the answer.

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

Legal standards **not in the closed library**, flagged as unverified and therefore not asserted (`QUESTIONS.md` §C): hostile-work-environment severity standard; substantive ADEA standards; all FMLA eligibility/designation/notice/cure rules; federal damages caps; Columbia final-pay, limitations period, and implied-contract rules; non-disparagement limits; whether a defective OWBPA waiver also degrades non-ADEA releases; whether a PIP is per se "materially adverse"; cat's-paw liability.

## Decisions we need from the client

1. **Authorize sources beyond `library/INDEX.md`** (full 29 C.F.R. Part 825, ADEA/Title VII substantive standards, damages caps, Columbia pay/limitations rules) — or instruct us to keep working on the closed library, in which case items above stay open and any decision is made on an admittedly incomplete record.
2. Whether to **stop the termination in writing today** and issue (a) the litigation hold, (b) Hale's written removal from all decisions about Dana, (c) a written FMLA determination, (d) an outside-chain harassment investigation. We have recommended all four and can draft them on instruction.

## Not addressed

No independent verification of HR's timeline, no contact with Dana Whitcomb, no review of documents outside `documents/`, no agency or court filings reviewed, no opinion on unemployment insurance, benefits continuation (COBRA), or tax treatment of any payment.
