

Good practice — I'll re-audit everything from source: figures against the client documents, citations against the closed library, and arithmetic recomputed in Python, then reconcile the five deliverables against each other.






Now the library — checking every cited proposition actually exists there:










Library cross-check complete — all cited propositions exist verbatim or accurately paraphrased. Now the source documents and the contract schema:






The extraction output truncated — let me capture it fully to a file and inspect each document's figures.






All PDF figures tie to what I used. Now the three text files and the remaining deliverable sections:






Basis rollforward, rental loss, and move dates all tie. Now the full narrative and remaining deliverables:






Now the remaining two library files in full, plus a complete independent recomputation:







All library propositions verified verbatim. Now the full independent recomputation of every number in all three scenarios:





The Code Mode runtime is JavaScript, not Python — rewriting:





Recomputation is complete — all mainline figures tie, but it surfaced four defects (two previously suspected, two new: the §1 rejected-alternative cascade and wrong prorate illustrations in §5). Checking for any other occurrences of the bad figures, then applying fixes:





All four defects confirmed located, with no other occurrences. Let me read the exact surrounding text in both files to craft precise edits:







All targets verified verbatim. Applying the four fixes now:







All edits applied. Now a brief self-audit note in STATUS.md, plus final verification passes:





Final verification — stale figures gone, JSON still valid, edited sections read clean:







Stale figures fully purged (the one surviving "5,217.49" is the intentional exact-value annotation). JSON validation via shell:





Audit complete. All fixes are in and everything re-verified. Here's the report.

## What I audited

1. **Authority check** — every citation in the deliverables traced back to the six files in `workspace/library/INDEX.md` (standard deduction $31,500; tax-table row and "must use the Tax Table below $100,000" rule; CTC/8332/alternation; 7203 ordering + guarantee rule; 8582 MAGI definition + below-market carve-out; 8962 bands/caps; NY convenience-of-the-employer rule). All propositions verified present verbatim; nothing cited from outside the library.
2. **Source-document check** — all 10 documents in `workspace/documents/` re-extracted and every figure re-tied (W-2s, 1095-A, 1098, 1099-INT, K-1, basis note, rental summary, custody agreement, move email).
3. **Arithmetic** — full independent recomputation of the mainline and both documented alternative scenarios; the tax-table row cross-checked against the table's own midpoint construction (6,708 exact); day counts (181/184) recomputed.
4. **Unsupported-authority scan** — flagged anything not backed by the library or source file; all such items already carry **[ASSUMPTION]** tags or sit in `QUESTIONS.md` (R1–R5).

## What I changed (4 fixes — all display/illustration-level)

| # | File | Defect | Fix |
|---|---|---|---|
| A | `judgment_calls.md` §1 | Rejected full-$28,000 alternative illustrated with AGI $74,850 / TI $43,350 — internally inconsistent (it held the $19,550 allowance fixed even though that scenario's MAGI of $94,400 unlocks the full $25,000) | Rewritten as a self-consistent cascade: MAGI $94,400 → full $25,000 allowance → full $21,018 rental allowed → AGI $73,382, TI $41,882 (outside the table excerpt → tax uncomputable from authority); 8962 ≈ 235.2% FPL, repayment ≈ $1,010 |
| B | `return.md` §4 | "91,350 × 5.7115% = 5,217.49" — the printed product didn't match the printed multiplier (5.7115% × 91,350 = 5,217.46; 5,217.49 is the unrounded-5.711538% value) | Product corrected to **5,217.46** with the exact value noted; FPL shown unrounded (292.7885) in the interpolation line so it multiplies exactly. Monthly is 434.79 either way |
| C | `return.md` §4 | "1,255.21 × 6 = 7,531.25" — product is actually 7,531.26 | Corrected to **7,531.26 → $7,531** (rounded figure unchanged) |
| D | `judgment_calls.md` §5 | Rejected-prorate illustrations $33,699 / $26,762 were miscalculated (68,000×181/365 and 54,000×181/365) | Corrected to **$33,721 / $26,778** |

Also added a short "Pre-delivery self-audit" note to `STATUS.md` recording the review and confirming the bottom line moved nowhere.

## What did *not* change

**No computed figure moved.** The verified chain stands: wages $122,000 + interest $400 − Sch.1 $31,050 → AGI **$91,350** → TI **$59,850** → tax **$6,708** (table row, midpoint-verified) − CTC $2,200 + capped repayment $1,900 → total tax **$6,408** vs. withholding $8,730 → **federal refund $2,322**. `return.json` needed no edits — all its values re-validated against independent recomputation, and its internal tie-outs pass programmatically. `QUESTIONS.md` unchanged: R1–R5 remain the honest residual unknowns (prior-year 7203s, the lease document, exact residency end date, NY rate schedule, Schedule A rules).

The return is ready for delivery.