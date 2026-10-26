Good discipline. I'll re-verify every number and every citation against the source library, then fix what's wrong. First, re-read all the authorities and deliverables I relied on:

All client documents check out. Now re-running every number in the deliverables in one comprehensive Python cross-check:

JSON files are valid. Now the `advice.md` edits — reading the exact current text of §§5, 8, 9:

§1's numbers need explicit `tax_rates_assumed.md` cites. Applying:

Now applying the remaining `advice.md` edits (line-5 update paragraph, §1 tax paragraph cite, §5(b) NIIT conditionality, §8 QDRO allocation + conditional edge, §9 assumptions):

All six `advice.md` edits applied. Now updating `STATUS.md` with the conditional-edge and QDRO-allocation open items:

Final verification pass — JSON validity, no stale strings, and the corrected fraction in place:

**Pre-delivery self-review complete.** I re-audited every deliverable three ways: (1) recomputed every figure in Python from the source documents; (2) checked every cited legal proposition against the six files in `library/`; (3) checked internal consistency across the files. All cited law turned out to be genuinely supported by the library, and all headline numbers verified. I found one real arithmetic typo, one material ambiguity, and several places where assumptions were under-cited or a "finding" was stated more confidently than the library supports. Everything below is now fixed.

## Errors found and fixed

**1. `child_support.json` — wrong fraction shown for the $40,000 bonus band.** The notes showed `3,050 × 12,045/18,285 = 2,004.29`, but that fraction doesn't produce 2,004.29. The correct arithmetic is husband `(208,000/12 − 2,000) × 0.78 = 11,960`, combined `18,200` → `3,050 × 11,960/18,200 = 2,004.29`. The dollar result was right; the displayed work was wrong. Fixed with the full computation shown.

**2. QDRO equalization amount was ambiguous (`division.json`, `advice.md` §8).** The ~$134,211 figure silently assumes Wife takes **all** $100,000 of joint cash. Both files now spell out the allocation (297,227 + 100,000 + 144,000 + 20,000 + 17,100 = 578,327 base → shortfall 102,000 ÷ 0.76 = 134,210.53) and flag the alternative: **with cash split 50/50 the QDRO is exactly $200,000** — a negotiable dial the decree must state. Added as open item 9 in `STATUS.md`.

**3. A2's tax advantage over immediate sale was overstated as unconditional.** This was the biggest substantive reconciliation issue. The $4,446 saving (39,546 vs 43,992) holds only while Wife's taxable share stays ≤ ~128,000 (MAGI ≤ $200,000); the library itself (`tax_rates_assumed.md`) prescribes a blanket conservative convention (assume NIIT on the taxable portion), under which **A2 and B are worth exactly the same — 678,104 each**. `advice.md` §5(b), the §8 fallback bullet ("~$2,200 worse" → conditional), the round-2 update paragraph, a new dedicated NIIT-conditionality instrument in `division.json`'s A2 block, and `STATUS.md` open item 8 now all state this — and note that A2's core value (the stay, no refinance, deferral) doesn't depend on the NIIT point at all.

**4. Under-cited rates.** 15% LTCG, 3.8% NIIT, the $200,000 single threshold, the 24% ordinary rate, and the 6% selling costs were cited only as "engagement assumption." They are all in `library/tax_rates_assumed.md`, and now every use of them cites that file explicitly.

**5. Unsupported extensions tagged `[unverified]`:**
- Applying the library's 24% rate to **Wife's** QDRO cash-out (the library states it for Husband only) — flagged everywhere it's used.
- Applying 24% to Husband's **bonus** when valuing it at 0.76 — flagged.
- Applying NIIT to **brokerage** gains (+$3,040) — the library only prescribes NIIT on the house gain; tagged as a conservative extrapolation.
- Scenario B's 18.8%-both-sides: the **MFJ NIIT threshold is not in the library**, so this is now labeled a conservative-convention assumption, not fact.
- Noted that actual §1411 mechanics (NIIT on the *lesser* of NII or MAGI-over-threshold) are **not in the library** — the 90,992/43,992/62,017 figures correctly use the library's stated conservative convention and are now labeled as such.

**6. `STATUS.md`** — added the review note to the header and the two new open items (conditional A2 edge; QDRO allocation).

## Checked and found correct (no changes)

- Every number in every file re-verified in Python: 613,008 / 662,000 / 48,992 gap; 90,992; A2 tax 39,546 and net 594,454; B tax 43,992; estates 1,360,654 / 1,356,208; halves 680,327 / 678,104; QDRO variants 32,231.58 and 134,210.53; support figures 2,022.63 / 1,830 / band 2,004–2,042; refi P&I 2,648.15, ratios 44.1%/26.4%/33.0%, paydown 24,221 to balance 375,779; appreciation illustration 1,202,000 / 62,017. (Two apparent mismatches during the audit turned out to be bugs in my check script, not in the deliverables.)
- Legal propositions: §121(b)(1)/(d)(3)(A), §1041 carryover basis, TCJA §11051, QDRO/§72(t)(2)(C), §152(e)/Form 8332/§2(b)/§7703(a), worksheet rules, Rule 16.2(e) — all match the library text.
- Closed-library rule respected: nothing in the files relies on outside authority; everything outside the library carries an `[unverified]` tag.

The deliverable set is consistent and ready for delivery.