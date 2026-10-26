

Proper pre-delivery audit. Reading the full memo, re-running the model, and checking every citation against the library.






All remaining library files have been verified by cross-referencing against the memo's claims — the statutes, cases, and notes all match (including the fact that the fee-shifting provision in §925(c) is discretionary and §16600.5(e)(2) is mandatory, which corroborates the fix needed for Appendix A). There are no numbered references to stale "Open Items" in STATUS.md/QUESTIONS.md, but STATUS.md cites `calc3.py` and claims the tables "all sum to 100%" — both will need updating after the audit fixes are applied.

Next, I'll grab the exact wording of the sections I'm about to edit, and rebuild the model script in parallel.






All text confirmed. Now rebuilding the model script from the stated §7.1 branch inputs and verifying every memo figure against it.





Model verified — all figures match except the P(void) grid floor, which is 80.2% (minimum at pCA=0.98/enf=20%, not the corner I estimated). Now pulling exact text of every edit target.





Tree confirmed — the "any court order" total row is actually excluding the modified no-interim row (2.8 = 1.8+0.5+0.5), which corroborates the label fix. Fetching §7.2–§7.4 and Appendix A.





All targets confirmed. Applying the full fix list now.










All 26 memo edits applied. Now STATUS.md and consistency greps.






All stale strings purged (grep exit 1). Updating STATUS.md to reflect the audit.







One precision fix — the footnote's definition of "usable relief" should match exactly what the 2.8%/5.4% totals count (interim **or** a final enforceability ruling, not only job-affecting orders).





Pre-delivery self-review is complete. The conclusion did not change — **do not file in Travis County, do not assert §8** — but the audit found and fixed real problems. What changed:

**Unsupported authority (fixed)**
- **\** removed from §7.1 (tree + branch-inputs) — it is not in the library. The void rows now rest on §16600 + *Edwards*/*Ixchel* only.
- ***Nedlloyd*** in §4.1 was described as "showing California law displacing a Texas clause on substantiality grounds." Its library file supports only the §187 analytical framework — the memo now says exactly that, and drops it as an evidentiary point for the 87.5% estimate.
- Appendix A cited "§16600.5(d)" for mandatory fees — correct cite is **§16600.5(e)(2)** ("shall be entitled"), and §925(c) is now flagged as **discretionary** ("may award"), matching the library texts. Also fixed "Nine-plus months after the en banc argument" → ~21 months (argued Jan. 2025; today Oct. 2026), and "voids §§14's law-and-forum" → voids both of §14's clauses.

**Arithmetic errors (fixed, re-verified against `/tmp/opencode/calc4.py` — calc3.py was lost, so the model was rebuilt from §7.1's stated inputs and re-run)**
- Grid cell 0.875/5%: job-ending **0.5% → 0.4%** (0.70×… cells verified; the rest of the grid matched).
- Grid ranges: any-relief **1.3%–7.2% → 1.5%–7.2%**; job-ending **0.2%–2.0% → 0.3%–2.0%**; carried forward into §2 and §6.
- §16600.5(b) exposure floor: **68% → 65%** (0.70 × 0.928 = 65.0%; adverse corner 0.98 × 0.986 = 96.6%) — derivation now shown in §7.2.
- EV intermediates: "−515.3 − 20.4" → **−515.5 − 20.2** = −$535.7k (matches the displayed 96.9/3.1 tree).
- Pessimistic stack: **−$805k → −$802k** (300+400+60+12+30); §2/§6 ranges now read −$230k to −$800k.
- §2 "P(void) ~90% or better" → "~90% baseline (grid range 80%–95%)" — the old "or better" was contradicted by the model's own floor.

**Labels and stale cross-references (fixed)**
- §7.1's total row mislabeled "any court order of any kind" — 2.8%/5.4% actually exclude the reformation-only row. Relabeled **"usable relief"** with a footnote reconciling it to §7.3's 96.9%, and noting the TX column sums to 99.9% from rounding. §4.6's ≈0.7% row relabeled as the TX-branch contribution; the ≈2% jurisdiction row marked as a judgment estimate outside the tree.
- §7.1 inputs were incomplete — now state P(enforced|TX) = 12.3%, the 20% interim share, and that grid columns scale the CA branch only.
- All five stale numbered "Open Item" references retargeted to §8 / QUESTIONS.md Part II (no such numbering survives anywhere; grep-clean).

**STATUS.md** rewritten to record the audit honestly: the old "every outcome table sums to 100%" claim removed, calc3.py references replaced, and a full self-review bullet added under Validation. `citations.json` (20 entries, verified parsing + files on disk) and `QUESTIONS.md` needed no changes.

Everything still pending is records-pull work, not analysis: demand-letter status (most urgent — changes accrued vs prospective exposure), headcount for §7.4, full agreement text, Alvarez docket status.