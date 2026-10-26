

Good practice — a full QA pass before delivery. Let me first re-verify every cited authority against the library, re-check the docket facts against the client file, and re-run the arithmetic across all three sessions:






All three files confirmed. Applying the QA fixes now — starting with `cod_schedule.json` (election wording precision + discharge-year NOL ordering + tie-out):





Now updating QUESTIONS.md with the new discharge-year item:





Now re-validating all JSON files and arithmetic across all three sessions:





All arithmetic verified. Final step — syncing STATUS.md with the QA changes:





QA pass complete. Everything I checked either reconciles or has been fixed. Here's the full report.

## What was verified (no changes needed)

- **Arithmetic, all three sessions, re-run in Python — all pass:** March roll-forward (2,262,400 − 490,770 = 1,771,630), April roll-forward (1,771,630 + 1,480,300 − 1,010,600 = 2,241,330), DIP cumulative 1,550,000 ≤ 2,500,000 cap, LSTC 62,400 + 7,400 + 4,310 = 74,110, UST 3,926.16 + 8,084.80 = 12,010.96, H&P 0.8 × 140,000 + 4,200 = 116,200, holdback 28,000 + 45,000 = 73,000, and all Session 3 figures (2,940,000 / 5,460,000 / 640,000 / 122,500 / 2,817,500 / 1,470,000 + 1,347,500 = 2,817,500). All three JSON files parse.
- **New cross-check added:** Dkt. 214's payment figure ties to the term sheet's allowed claim — 2,940,000 ÷ 0.35 = 8,400,000 exactly.
- **Docket quotes** re-checked against the client file (Dkt. 77 terms, Dkt. 214 figures/dates).

## Changes made

**`session3/cod_schedule.json`**
1. **Fixed an imprecise claim in the §108(b)(5) analysis.** I had written "total future deductions identical (5,460,000.00 either way)" — that's the *reduction*, not the deductions. Corrected to: reduction 5,460,000.00 either way, and future deductions *remaining* 3,840,000.00 either way (default: 640,000 NOL + 3,200,000 basis; election: 3,840,000 NOL + 0 basis), with the sum shown.
2. **Added the §108(b)(1)(A) ordering caveat:** the statute hits the discharge-year (2026) NOL *before* carryovers; the file's 6,100,000 is a petition-date figure. If 2026 generates its own NOL, the total 5,460,000 reduction is unchanged but more of the carryover survives. `nol_after` 640,000 now explicitly labeled as assuming no 2026 NOL.
3. Added the 2,940,000 ÷ 0.35 = 8,400,000 tie-out.

**`session3/fresh_start.md`**
4. **Measurement-date gap disclosed:** the file's 14.0M/16.2M are effective-date figures; condition (a) measures immediately before confirmation (9/2/2026). Stated that we use the plan figures as best available rather than invent interim numbers.
5. **Removed an overstatement:** the assumptions previously said Dkt. 214/term sheet "do not say otherwise" about voting shares — neither document says "voting" *or* "non-voting", so the assumption is entirely ours. Rephrased honestly; the condition (b) table row now reads "assumed voting."
6. **Re-labeled fresh-start counterfactuals** (asset remeasurement, retained-earnings reset) as general ASC 852 mechanics not in the library excerpt — unverified as to specifics, and not needed since the excerpt's two non-application rules drive the presentation.
7. Noted in conclusion #1 that the emergence balance sheet carries the obligation net of the effective-date first installment (removed a surface tension between the two files).
8. Tax bullets now carry the 2026 discharge-year NOL caveat.

**`session3/emergence_balance_sheet.md`**
9. **Deleted "not an extraordinary item"** and the parenthetical that APIC treatment "belongs to fresh-start" — neither doctrine is in the library excerpt. Replaced with library-only language (gain → income statement → accumulated deficit; excerpt provides no direct APIC credit or reset) and an explicit unverified label on period presentation.
10. **Labeled the current/noncurrent classification convention** (within-12-months = current) as general presentation practice, unverified against the library; also spelled out the boundary installment (k=12 lands exactly on the 12-month anniversary 9/30/2027).
11. **Added a DIP reconciliation note:** the file supports draws of only 1,550,000.00 through 4/30; May–September draws/interest/fees are absent, so the emergence payoff is explicitly *not computable* — previously the file just said "terms not in file" without anchoring what IS known.
12. Illustration table header changed from "pre-emergence period, through 9/30/2026" to "period including the 9/30/2026 effective date (presentation customary, not library text)."

**`QUESTIONS.md`**
13. Added: projected 2026 (discharge-year) taxable income/NOL; DIP payoff detail; confirmation-date vs effective-date test figures (minor).

**`STATUS.md`**
14. Session 3 bullets and open-items list updated to match; the unverified-law disclosure now also lists the general-practice items labeled this pass (extraordinary-item doctrine, gain-period presentation, current/noncurrent convention, fresh-start counterfactuals — none of which any conclusion depends on).

**Bottom line:** no number in any deliverable changed. All fixes were authority-hygiene (three claims I'd made that the library doesn't actually contain, now removed or labeled), one imprecise tax statement corrected, one statutory-ordering nuance added, and three reconciliation gaps disclosed rather than papered over. The highest-stakes open fact remains unchanged: whether the old equity's 60% is *voting* — if it isn't, fresh-start applies and every Session 3 presentation flips.