Good instruction. I'll re-audit the four deliverables end-to-end: cite-by-cite against `library/INDEX.md`, number-by-number against my Python arithmetic, and cross-document counts. Let me first pull the exact current text of the files I need to correct.

QC pass done. Findings:

1. **Substantive error (caught):** `coo_onepager.md` item 2 ends "IP claims above $222,000 would otherwise be RouteWise's cost, not ours" — that's backwards, and it contradicts the Business-impact bullet ("IP dispute costs above $222,000... fall on us"). As drafted, the award slice above the cap lands on Cobalt; the fix restores it to RouteWise.
2. **Authority precision:** R1's Exhibit C rider said "(g) deletes or returns data **at the end of service**" — the library excerpt attaches no timing; trim to match `library/gdpr_art28.md` exactly.
3. **Loose claim:** issues.json rank 3 says the "60-day notice fails A3's 90-day requirement" — the 60-day notice attaches to the mid-term increase, which A3 prohibits outright regardless of notice; 90 days governs any permitted renewal increase. Needs rewording.
4. **Internal consistency:** R5's route (a) replacement §2.2 refers to affiliates "as designated in Exhibit A" without adding that rider — dangling reference.
5. **Scope discipline:** R7 carried a second sentence ("shall not sell...") beyond the note-level Art. 28(3)(a) conformity ask; not playbook-required.

Everything else reconciles: all citations trace to `library/INDEX.md` only; counts (5 hard, 1 preferred, 1 note) agree across files; all figures re-verified ($222,000/yr, $691,000 total, $17,760 vs $11,100/yr, $6,660/yr excess, $53,280, $444,000 vs $222,000, $479,520 vs $233,100, $4,625/mo, 216 min = 3.6 h). Applying the fixes now.

Exact text confirmed. Applying the remaining fixes now.

QC pass complete. The only remaining matches are the change log itself in `STATUS.md` — the defects are gone from the deliverables. Here's what I found and fixed:

**Corrected (5 items):**

1. **`coo_onepager.md` — substantive error.** Item 2 said "IP claims above $222,000 would otherwise be RouteWise's cost, not ours" — backwards, and it contradicted the Business-impact bullet on the same page. Corrected: as drafted, the award slice above the $222,000 cap lands on **Cobalt**; the carve-out keeps RouteWise liable for the whole award.
2. **`redlines.md` R1 — authority precision.** Exhibit C rider item (g) said "deletes or returns data **at the end of service**" — the `library/gdpr_art28.md` excerpt attaches no timing. Trimmed to match the library text exactly.
3. **`issues.json` rank 3 — imprecise claim.** "60-day notice also fails A3's 90-day requirement" conflated two regimes: the 60-day notice attaches to the mid-term increase, which A3 prohibits **outright regardless of notice**; 90 days governs any permitted renewal increase. Reworded.
4. **`redlines.md` R5 + `issues.json` rank 5 — dangling cross-reference.** Route (a)'s §2.2 replacement pointed to affiliates "as designated in Exhibit A" without adding that rider. The replacement is now self-contained (names written into the clause); the Exhibit A rider is an explicit optional companion and a stated dependency of route (b) only.
5. **`redlines.md` R7 — scope discipline.** Dropped the "shall not sell / publish" sentence — beyond the note-level Art. 28(3)(a) conformity ask and not playbook-required.

**Checked, no change needed:**
- All citations trace to `library/INDEX.md`'s three files only — no unsupported authority found after the R1 trim.
- Issue counts (5 hard A1–A5, 1 preferred B5, 1 note A2-conformity) agree across `issues.json`, `redlines.md`, and the one-pager.
- All figures re-reconciled with the earlier Python arithmetic ($222,000/yr; $691,000 initial-term total; $17,760 vs $11,100/yr; $6,660/yr excess; ≈$53,280 worst case; $444,000 vs $222,000; $479,520 vs $233,100; $4,625/mo; 216 min ≈ 3.6 h).
- Rank 2's "Survival is fine (§12.3 includes §10)" verified against the MSA; UCC Article 2 rejection stands on `library/ucc_2_distractor.md`.
- `issues.json` re-validated after edits: 7 issues, structure intact.

The full change log is also recorded in `deliverable/STATUS.md` under "Pre-delivery QC," so the record ships with the package. Ready to send.