I'll audit everything from scratch: re-read every library file, re-extract every client document, re-verify every citation and number, then fix what I find.

Library confirms the core rules. Now re-extracting every client document to verify each number:

Library and documents extracted. Now let me read the full deliverables and re-verify every figure and citation in one pass:

Continuing the audit — the library `cat` output was truncated earlier, so let me re-read each library file completely, then the full deliverables.

Now re-verify the client documents' key figures and read the remaining deliverables:

STATUS.md, QUESTIONS.md, and the 1095-A are now confirmed (Sofia age 15 and Leo age 9 are printed right on the 1095-A ✓ — that supports the CTC analysis). Now let me re-read the exact text of the sections I need to edit:

The quote in judgment #10 is verbatim from the library ✓ — only its arithmetic is broken (`23,850 + 4,320 = $6,690`: it conflates the 10% bracket threshold $23,850 with the 10% tax on it, $2,385). Now applying the fixes. First return.md — the substantive §7/bottom-line error:

Exact text confirmed. Applying the three judgment_calls.md fixes:

Now return.json — reading it fully to make the exact fixes:

All edits applied. Now the final validation pass — JSON parse + figure asserts, plus a sweep for any leftover wrong-direction phrasing:

Everything verifies — the three remaining grep hits were benign substrings ("2**6,690**" matching the "6,690" pattern; "shrinks" in QUESTIONS.md is the legitimate family-size sensitivity note), and the only surviving "5,450" is the correct §2 phase-out arithmetic. Final state of all edited sections confirmed above.

## Audit complete — findings and changes

The audit found **real errors** (mostly narrative/derivation, not outcome). Headline figures are unchanged — refund stays **$2,322** — but the reasoning shown alongside them is now correct and every arithmetic claim re-verified in Python (all 48 checks pass; nothing was forced to reconcile).

### Errors fixed

**return.md** (6 edits):
1. **Bottom line — backwards causation (substantive).** Old text said the allowed $11,500 S-corp loss "*reduces* the rental special allowance… costs him $5,450." That's inverted: an allowed nonpassive loss **lowers** MAGI and **raises** the allowance. Correct story: because only $11,500 (not $28,000) clears basis, MAGI stays at $110,900 → allowance $19,550 instead of the $25,000 he'd have gotten at MAGI $94,400 — stranding $1,468 of rental loss in carryforward.
2. **§7 rewritten** with that corrected domino effect, both counterfactuals (full-28k → MAGI 94,400 → $25,000; passive loss → MAGI 122,400 → $13,800), and the tie-out: −$31,050 vs naive −$49,018; the $17,968 gap = $16,500 + $1,468 exactly.
3. **§1 basis table, 2021 row.** The client's basis note shows (2,100) as a **loss**; the table had it in the "income" column. Moved to the loss column (end basis 7,900 unchanged).
4. **§4 8962 block** now carries the unrounded chain (292.7885% → 5.711538% → 5,217.49/434.79) so the displayed arithmetic actually reproduces.
5. **§4 rounding note** added: rounding FPL to 292.79 first gives excess 2,368.80 — the $1,900 cap binds either way, so rounding can't change the result.
6. **§5 authority line** — the custody PDF and Form 8332 are now labeled case-file evidence, not library authority (the library citation stands only for the CTC rules).

**judgment_calls.md** (3 edits):
7. **#10 broken arithmetic:** "23,850 + 4,320 = $6,690" → **2,385 + 4,320 = $6,705** (it had confused the $23,850 bracket threshold with the $2,385 of 10% tax). Added the midpoint consistency check (2,385 + 0.12 × 36,025 = $6,708 = table figure). The quoted "for reference only — not to be used under $100,000" was confirmed **verbatim** in the library (tax-table excerpt line 51).
8. **§1 residual doubt rewritten:** old text wrongly said the ordering was "not spelled out in library" — the library does say "decreased by distributions and losses (in that order)." Narrowed to the only live question (within-2021 contribution vs. loss) and fixed a wrong claim: loss-first wouldn't "still end at 7,900" — it ends 10,000 with 2,100 suspended, which unwinds in 2022; 2025's 11,500/16,500 is identical either way.
9. **#8:** the 27.5-year recovery period itself is flagged as a client-file figure, not library authority *[unverified]*.

**return.json** (2 edits):
10. **form8962 block** — fpl_pct 292.7885, applicable_figure_pct 5.711538, plus new `annual_contribution` 5,217.49, `monthly_contribution` 434.79, `monthly_ptc` 1,255.21 so the JSON ties to §4 line-by-line.
11. **ny.method parenthetical** — the employer-necessity alternative would have cut **each** spouse's nonresident wages to a NY-workday share (Marcus ≈33,609, Elena ≈26,690); old text mentioned only Elena's.

### Audit confirmations (no change needed)
- All library rules re-confirmed verbatim; every citation traces to a file in `INDEX.md`.
- All arithmetic re-run independently: basis trace, MAGI/allowance, AGI 91,350, taxable 59,850, Tax Table 6,708, CTC 2,200, repayment 1,900, refund 2,322, NY 181 days / 6,752 withholding, workday allocations, and the below-market flip scenario (computes to $1,271 due, consistent with the file's ≈$1,270).
- return.json re-validated: parses, all line tie-outs assert clean.
- QUESTIONS.md and STATUS.md audited and left as-is — consistent with the corrected text; open items (8962 family-size assumption, NY tax not computable from the library, rental-characterization risk) unchanged.