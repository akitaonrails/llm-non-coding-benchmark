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

## Pre-delivery QC (changes made in the final review pass)
1. `coo_onepager.md` item 2: exposure sentence had been written backwards ("IP claims above $222,000 would otherwise be RouteWise's cost, not ours"). Corrected — as drafted, any part of an IP award above the $222,000 cap lands on Cobalt; the carve-out keeps RouteWise liable for the whole award. (The Business-impact bullet was already correct; the two documents now agree.)
2. `redlines.md` R1: Exhibit C rider item (g) said "deletes or returns data **at the end of service**"; the `library/gdpr_art28.md` excerpt attaches no timing — trimmed to "deletes or returns data" to stay exactly within the library text.
3. `issues.json` rank 3 "why": "60-day notice also fails A3's 90-day requirement" was imprecise — the 60-day notice attaches to the mid-term increase, which A3 prohibits outright regardless of notice; 90 days is the A3 minimum for any permitted renewal-term increase. Reworded.
4. `redlines.md` R5 and `issues.json` rank 5 redline: route (a) replacement §2.2 referenced affiliates "as designated in Exhibit A" without adding that rider (dangling cross-reference). §2.2 replacement is now self-contained (names written into the clause); the Exhibit A rider is an explicit optional companion, and is a stated dependency of route (b).
5. `redlines.md` R7: removed the second sentence ("Provider shall not sell Customer Data or publish it in identifiable form") — it went beyond the note-level Art. 28(3)(a) conformity ask and is not a playbook requirement.
6. Re-verified after fixes: all citations trace to `library/INDEX.md` (3 files only); issue counts (5 hard A1–A5, 1 preferred, 1 note) agree across `issues.json`, `redlines.md` and `coo_onepager.md`; all figures re-reconciled ($222,000/yr; $691,000 initial-term total; $17,760 vs $11,100 per year; $6,660/yr excess; ≈$53,280 worst case; $444,000 vs $222,000; $479,520 vs $233,100; $4,625/mo; 216 min ≈ 3.6 h). No further defects found.
