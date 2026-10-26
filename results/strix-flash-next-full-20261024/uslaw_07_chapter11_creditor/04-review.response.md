Good discipline — let me re-audit the deliverables against the library line by line. First, systematic greps for authority risks (statements that must trace to a library file) and arithmetic anchors:

Last read confirms the §502(d) "can have its entire claim disallowed" wording at line 137. Let me pull the exact text of every line I need to fix, then apply the fixes:

Workpapers §4 is fully consistent with the CSVs (`days_after_invoice` baseline 43–47, the 14-days-faster claim checks: min historical 43 − 29 = 14 ✓), and its §502(d) already tracks the library's "shall disallow." Now let me get complete coverage of the soft-phrasing grep (the earlier one was truncated), then apply all fixes:

Tail reviewed clean. Now rebuilding the audit tool with all checks (recalculating from source CSVs, plus new checks for the fixes just applied):

Seven failures — most look like audit-side artifacts, but two need inspection in the deliverables. Let me examine them:

The audit flagged real and artifact issues. Let me check the workpapers' actual basis for the 95,000/85,000 split so the audit check matches the deliverable's reasoning:

All 253 audit checks pass. One final look at `STATUS.md` to confirm it still accurately describes the post-review state:

Pre-delivery review is done and the full audit (253 checks: every figure recomputed from the source CSVs, every citation resolved against `library/INDEX.md`, statutory-language probes, cross-file consistency) now passes with zero failures. Here is what I changed, and why:

## Fixes applied (12 edits across 6 files)

**1. §502(d) mischaracterized as discretionary — 5 spots.** The library text (`library/bc_502d_setoff.md`) is mandatory: the court **"shall disallow"** a claimant's claim unless and until it pays the recoverable preference. My drafts softened this to "can have its claim disallowed," "can freeze," "lets the court disallow," etc. Restated to the library's mandatory formulation in `advice_to_ceo.md` (two places), `client_answers_round2.md`, `proof_of_claim_draft.md`, and `claim_analysis.json`. This matters commercially: if preference liability attaches, disallowance of the whole $125,000 isn't a risk the judge may impose — it follows automatically, which sharpens the "resolve the preference fight early" advice.

**2. Bad citation in `claim_analysis.json`.** The §502(d) sentence cited `library/bc_547.md` + `library/bc_502d_setoff.md`; `bc_547.md` contains no §502(d) (grep: zero hits). Narrowed to `bc_502d_setoff.md` only.

**3. Unsupported "this account is 40+ days late" — 4 spots** (`advice_to_ceo.md`, `claim_analysis.json`, `workpapers_calculations.md`, `QUESTIONS.md`). The payment file has no due-date aging — its column is literally `days_after_invoice`. Replaced with record-based arithmetic: MS-7740 (invoiced 2026-02-02) is **45 days past invoice as of 2026-03-19** (38 when the 03-12 notice fired; 30 past the shortened net-15 due date of 02-17). Also showed the 03-12 firing can *only* be explained by invoice-age counting — net-15 aging gives 23 days, and the original net-45 due date was 2026-03-19 itself — and added the system's unknown "late" convention to `QUESTIONS.md` flag 7 for the audit.

**4. "Roughly" before an exact number.** `advice_to_ceo.md` said "roughly $95,000 protected / $85,000 exposed." The split is exact on this record — removed "roughly" and added the addends (51,000 + 44,000 vs 48,200 + 36,800).

**5. Bar-date filing method under-described — 2 spots** (`claim_analysis.json`, advice deadline table). The notice permits filing "by e-filing with the claims agent **or by mail**"; both now say so.

**6. Citation hygiene in `proof_of_claim_draft.md`.** One paragraph crammed a §547 point (citing `bc_547.md`) and the §502(d) point (citing `bc_502d_setoff.md`) into a single run-on; split so each cite maps to its own sentence.

## Checked and confirmed correct (no change needed)

- All claim math, preference windows, new-value offsets, reclamation deadline, and the $210,000/$125,000 reconciliation re-derived from the CSVs — everything ties.
- Workpapers §4 transfer table (including the "paid 14 days faster than any prior payment" claim: min historical 43 − 29 = 14) checks out against `payment_history_12m.csv`.
- *Kmart* cite matches the library verbatim; FRBP library supports "voting and distribution" and excusable neglect; bar date used as printed (still open item 1).
- `STATUS.md` still accurate post-review — `COMPLETE WITH OPEN ITEMS`, 12 open items unchanged; no edits needed.

The deliverable set in `workspace/deliverable/` is ready for delivery.