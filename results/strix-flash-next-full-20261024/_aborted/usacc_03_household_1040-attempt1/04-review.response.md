Good instruction — this is exactly what a pre-delivery review should catch. I'll re-derive everything from the source documents and library files, then check each deliverable line against them.

QUESTIONS.md line count looks wrong (48 vs expected ~66) — checking whether the answers section is still there.

Now aligning QUESTIONS.md B1 and STATUS.md to the corrected sensitivity figures:

Final audit: extract every quoted span from the deliverables and verify each appears verbatim in the library, and confirm no stale sensitivity figures remain:

Code Mode parsed that as JavaScript — rerunning the audit through the shell with Python:

Schema matches the contract exactly; my key paths were guesses. Dumping the actual structure:

The exact Decimal re-derivation confirms the original figures were right and my mid-review "corrections" were wrong. Reverting all four:

Reverts applied. Now checking the return.md §4 step-5 rounding display and re-running the full assert battery with the confirmed original values:

Now re-running the full invariant battery with the confirmed values:

All invariants pass. Final visual check of the reverted passages:

Pre-delivery review is done. Here is the honest accounting.

## What I changed

1. **`judgment_calls.md` §3 (rental active participation)** — added the note that the library excerpt states *active participation* as a condition of the $25,000 exception but **never defines it** [unverified definition]; Elena's own description is the only evidence, and the rejected alternative (non-active participation → whole $21,018 deferred) stays disclosed.
2. **`judgment_calls.md` §10 (NY sourcing)** — moved markdown emphasis outside a client quote (`"Halvorsen **let me** go fully remote"` → emphasis marked as added), so the quotation is now verbatim.
3. **`return.md` §4 step 3–5 (Form 8962)** — the displayed rate was rounded in a way that didn't reproduce the shown product: `91,350 × 5.7115% = 5,217.49` actually uses the unrounded 5.711538% (rounded rate gives 5,217.45). Now shows the unrounded 292.788462% / 5.711538% chain and flags the 4-cent display effect explicitly.
4. **Nothing in `return.json` changed** — every filed figure survived review unchanged.

## What review caught me nearly getting wrong

During the review I briefly "corrected" the two sensitivity branches (family-of-3 FPL branch and the personal-use branch) in `judgment_calls.md` §4/§6, `QUESTIONS.md` B1 and `STATUS.md`. A final exact-Decimal re-run proved **my corrections were the error** — the original published figures (fam-3: PTC 7,094.43 → repayment 2,805.57 → refund ~1,416, ~$906 worse; personal-use: PTC 6,044.34, excess 3,855.66, capped at 3,150) were already right. **All four edits were reverted**; the documents state the originals again. No false "corrected at review" notes remain anywhere.

## What review verified (no change needed)

- **Schema:** programmatic diff of `return.json` against the CONTRACT.md JSON block — exact match, no extra or missing keys.
- **Arithmetic battery re-run, all pass:** wages 122,000; Sch1 −31,050 (11,500 + 19,550); AGI 91,350; TI 59,850; tax 6,708 (table row 59,850–59,900); excess APTC 1,900; CTC 2,200; total tax 6,408; WH 8,730; refund 2,322. 7203 trail `10,000−2,100+6,400+9,800−12,000+4,600−5,200 = 11,500`; 8582 MAGI 110,900 → allowance 19,550, carryforward 1,468; 8962 unrounded chain 292.788462% → 5.711538% → 434.79/mo → PTC 7,531.25 → excess 2,368.75 → repay 1,900; NY 181 days, day-ratio check figures 33,720.55 / 26,778.08.
- **Authority audit:** every library quote in the four `.md` deliverables was string-matched against `library/` — all verbatim (Tax Table instruction, 7203 guarantee sentence, 8582 carve-out, IT-203 refund sentence, 1040 lines 12/14). Non-library quotes are client/document words, properly sourced to `documents/`. Nothing outside the INDEX is cited.

## Still open (not fixable from here, flagged in STATUS.md / QUESTIONS.md §B)

- **B1** family-of-3 FPL — only dollar-moving unknown; the ~$906 sensitivity is magnitude-only because the family-of-3 line isn't in the library.
- **B4** "fair rental for that lease" documentation (lease/market evidence) for the below-market-rent call.
- NY IT-203 tax, disposition of the $6,752 NY withholding, and NYC tax — no NY rate schedule/deductions in the library; stated, not estimated.
- Prior-year 7203s and depreciation support remain client-prepared facts.

STATUS remains **COMPLETE WITH OPEN ITEMS**.