# Engagement status — Whitcomb termination risk assessment

**Date:** 2026-10-06 (updated same day after client's 10/06 responses) · **Deliverables directory:** `workspace/deliverable/`

## STATUS: COMPLETE WITH OPEN ITEMS

Required deliverables (per `CONTRACT.md`):

| Deliverable | File | State |
|---|---|---|
| 1. Risk assessment | `risk_assessment.json` | Complete; schema validated (`terminate_today: "no"`, 5 claims, 7 defects, comparator analysis, recommended course incl. client admissions, `litigation_hold: true`) |
| 2. Corrected agreement terms | `corrected_separation_agreement_terms.md` | Complete; 21-day (not 45-day) period confirmed by client ("Just her. No RIF.") |
| 3. Advice to HR | `advice_to_hr.md` | Complete; updated for client admissions, follow-up Q&A answered (at-will/PIP myths, "before leave" = the violation, "stuck forever?" and "right after leave?" — both no, with the conditions-precedent path), 9-item checklist |
| 4. Questions / status | `QUESTIONS.md`, `STATUS.md` | Complete; answered questions recorded, not repeated; remaining unknowns flagged |

**Core conclusion does not depend on any open item:** do not terminate today; litigation hold immediately (now expressly including Ortiz's records); external investigation of the 9/12 complaint outside Hale's chain (library rule) and — our recommendation beyond the library rule — outside existing HR handling; rescind the "Tom said to wait" instruction and process the FMLA certification via neutral/counsel-supervised handling; retire the 7-day separation form.

**What the client's 10/06 answers changed (strengthened, not weakened, the analysis):**
- "Tom said to wait" on the certification → second direct-evidence fact; interference is occurring *now*, independent of any termination.
- "Tom wrote the PIP and Tom wants her out. I was just processing it." → the accused is the sole decision-maker; HR Director is a fact witness whose interests may diverge from the company's (conflict note added).
- "Honestly, nothing / I was going to get to it" → 24 days of admitted non-investigation, on the record.
- "Just her. No RIF." → OWBPA 21-day consideration period confirmed (45-day program rule inapplicable).

## Open items (explicitly flagged; none blocking)

1. **Facts the client could not supply** — listed in `QUESTIONS.md` §B with the assumption used for each: (a) base salary → **damages exposure not computed, by design**; (b) FMLA employer coverage/eligibility and certification contents → assumed covered employer, eligible employee (tenure 2019 supports it); (c) whether PIP targets/policy were applied to peers → comparator file is best evidence; (d) pre-9/12 performance documentation → none per client, PIP is first written document; (e) existing severance entitlements → assumed none, must verify before any future agreement.
2. **Unverified law (flagged, never cited as authority)** — not in the closed library: FMLA-claim release enforceability; EEOC charge-filing carve-outs; FMLA certification-response deadlines; Columbia non-ADEA release standards; Columbia final-pay rules; Title VII remedies detail.
3. **Follow-on facts that only the investigation/HR process will produce** — certification sufficiency; any other Hale conduct discovered in the investigation. These belong to the recommended course, not to this advice.

## Verification performed

- `risk_assessment.json` parses and matches the contract's schema (keys, enums, boolean hold).
- Every citation in every deliverable points to one of the six files in `library/INDEX.md`; nothing outside the library is cited as authority; out-of-library points carry an explicit **[UNVERIFIED]** label.
- **Pre-delivery audit pass (post-Q&A):** every legal proposition was re-checked against the library files' actual text, and every number recomputed. Corrections applied, recorded in `REVIEW_LOG.md`: (1) "destroys" → "undermines" the *Faragher/Ellerth* defense (library's word); (2) the recommendation to exclude Ortiz's handling is now labeled as our judgment, not the library rule (library states only "outside the accused's chain of command"); (3) PIP quota claim corrected from "3 of 5" to **4 of 5** team members below 100% (only Lind, 103%, exceeded it); (4) corrected-terms §8 ADEA headcount fixed: **two** of five Account Managers are 40+ (Whitcomb 42, Lind 47), previously stated backwards; (5) FMLA key-fact sentence fixed — the leave request came 18 days after the complaint and the PIP **4** days after it (the PIP was never "18 days" after); (6) certification delay stated as exactly 3 days (10/03 → 10/06), not "three-plus"; (7) "respondeat superior" removed and relabeled (not a library proposition); (8) standalone-PIP-as-adverse-action now flagged **[UNVERIFIED]** (library cites *Burlington Northern* but does not state its materiality standard); (9) the "direct evidence" framework applied to the FMLA claim is labeled as borrowed from the Title VII entry; (10) § 825.220(c) quoted precisely ("taking of FMLA leave"), with the pending request covered via § 2615(a)(1)'s "attempt to exercise" language; (11) all relative dates anchored to the client's 10/06 request date (the PIP's 60-day window ends 11/15 regardless).
- Date math (complaint→PIP 4 days; complaint→termination request 24 days; complaint→FMLA request 18 days; leave request→Hale email 2 days; Hale email→termination request 4 days; certification pending 3 days; PIP 60-day window 09-16 → 11-15) and comparator deltas (+9/+4/+2 pts over non-PIP peers; OWBPA gaps 21−7=14 and 7−3=4) computed in Python and shown in the deliverables; audit pass re-verified all of it.
- No facts invented; client admissions used verbatim where quoted.
