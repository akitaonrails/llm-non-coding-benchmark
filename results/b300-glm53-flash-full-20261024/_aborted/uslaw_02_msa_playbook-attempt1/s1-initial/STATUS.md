# STATUS

**COMPLETE WITH OPEN ITEMS**

## Deliverables
- `deliverable/issues.json` — 7 ranked issues (5 hard A1–A5; 1 preferred B5; 1 note). Nothing flagged that the playbook accepts.
- `deliverable/redlines.md` — replacement text for every hard-rule break, plus the preferred B5 addition and the §5.4 note; includes an "accepted, no redline" table.
- `deliverable/coo_onepager.md` — plain-English brief for the COO.
- `QUESTIONS.md` — not required: no missing fact blocked the analysis.

## Citations
All authority cited in the deliverables comes from `library/INDEX.md`:
- `library/gdpr_art28.md` (Regulation (EU) 2016/679, Art. 28(3)) — ranks 1, 7.
- `library/contract_interpretation_notwithstanding.md` (Restatement (Second) of Contracts §203; Delaware 'notwithstanding' cases) — rank 2.
- `library/ucc_2_distractor.md` (U.C.C. §2-102) — cited only to record that Article 2 does not apply to this services agreement (checked and rejected, not relied on for any issue).
No fact or legal point outside the library was relied on. If something reads like law and is not traceable to `library/INDEX.md`, treat it as unverified — none is used.

## Open items (client decisions / negotiation actions, not missing deliverables)
1. **A5 route choice:** cover affiliates via amended §2.2 plus Exhibit A designation (recommended in redlines.md R5; route (a)) or by Holdings signing on behalf of listed affiliates (route (b)). Redlines support either; GC to pick.
2. **Exhibit C (DPA)** must be drafted/attached and executed concurrently with the MSA (redline R1 specifies the required Art. 28(3) content per `library/gdpr_art28.md`); signature cannot proceed on "[To be attached]".
3. **CPI-U figure:** not needed for the redline (the replacement formula "lower of 5% or CPI-U" is self-executing), but the live index value would matter for RouteWise-side pricing responses.

## Assumptions (stated, not balanced)
- CPI-U change assumed below 8%, so the Order Form §4 "greater of 8% or CPI-U" floors at 8%; if CPI-U exceeded 8% the draft's exposure would be higher.
- Worst-case mid-term increase assumes the 60-day-notice increase takes effect near the start of the 36-month Initial Term (~3 years of increased fees); actual timing is RouteWise's choice under the draft.
- SLA downtime math uses a 30-day month (43,200 min); 31-day months give 3.72 h.

## Arithmetic (verified with Python)
- Annual fees: $18,500 × 12 = $222,000; Initial Term: × 36 = $666,000; + $25,000 implementation = $691,000.
- 8% = $1,480/mo = $17,760/yr; 5% = $925/mo = $11,100/yr; excess = $6,660/yr; worst-case mid-term ≈ $53,280.
- Missed renewal notice: 24 × $18,500 = $444,000 (draft) vs 12 × $18,500 = $222,000 (playbook); with 8%/5% pricing: $479,520 vs $233,100.
- SLA: 43,200 min × 0.5% = 216 min (3.6 h) permitted downtime/30-day month, plus ≤ 8 h excluded maintenance; max credit 25% × $18,500 = $4,625/mo.
