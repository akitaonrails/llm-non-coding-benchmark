The previous check failed on a typo'd script. Let me re-run the full verification cleanly, and in parallel re-read the current deliverables so my edits match their exact text.

Verification confirms the two errors: **total tax = 10,895** (9,945 + 3,150 − 2,200 — the CTC must be netted) and **owed = 2,165**, plus the item-5 rejected-alternative figure is 15,825. Fixing `return.json` now, and reading the other three files:

`return.json` is fixed. Before editing the prose files, let me sweep for any other stale figures across the deliverables (e.g., old totals appearing in `QUESTIONS.md`):

All stale figures located. Now applying every fix — the two total-tax lines, the NY wording, the expense-parenthetical wording, the unverified labels, and the ACTC/itemized additions:

`return.md` updated. Now `judgment_calls.md` — fix the item-5 arithmetic, rewrite item 10 with explicit unverified labels, and append the ACTC item:

Now `STATUS.md` — correct the audit trail, add the new open items, and record the review pass:

All edits applied. Final consistency sweep — confirm no stale figures remain anywhere and that `return.json` still parses:

Wrong path prefix — the deliverables live under `/work/workspace/deliverable`. Re-running:

Review pass complete. The only remaining mentions of the old figures are in `STATUS.md`'s review log, where they belong. Here's what I found and changed:

## Errors fixed (figures)

1. **Wrong total tax and balance owed — the main error.** I had built line 24 as "tax + Sch 2 AssyPTC" and never netted the $2,200 child tax credit against the tax before adding back the $3,150 excess-APTC repayment. Every check now reconciles:
   - Line 24 = 9,945 + 3,150 − 2,200 = **10,895** (was 13,095)
   - Line 37 = 10,895 − 8,730 withholding = **2,165 owed** (was 4,365)
   - Fixed in `return.json`, `return.md`, and the two `STATUS.md` audit lines.
2. **Judgment call 5's rejected-alternative arithmetic was wrong**: allowance computed on AGI would be 25,000 − 0.5×(118,350−100,000) = **15,825**, not 13,050. (Fixed; conclusion unchanged — library defines MAGI before passive losses, so 10,550 stands.)
3. **8582 loss wording was internally inconsistent** in `return.md` (parenthetical made 29,200 look like it included the 9,818 depreciation; 18,000 − 29,200 ≠ 21,018). Reworded: 29,200 cash expenses + 9,818 depreciation = 39,018; 18,000 − 39,018 = 21,018 loss ✔.
4. **"Jan–Jul 2 wages"** (would imply a 183-day resident period, contradicting my own 181-day Jan 1–Jun 30 determination) → "Jan–Jun 30".

## Unsupported-authority gaps now explicitly labeled (per contract, not applied)

5. **ACTC refundable portion** — the library only gives the $2,200/child credit, nothing on Schedule 8812 refundability. Earlier the return silently presented all 2,200 as nonrefundable without saying so. Now labeled ⚠ unverified/unapplied in `return.md`, new judgment call 11, and `STATUS.md` open item 6 — with the reconciliation that even under the unverified split (line 24 = 12,595, 1,700 refundable on line 28), **the owed amount is unchanged at 2,165**, so no schema figure changes.
6. **Itemized-deduction rules (SALT cap, mortgage-interest limits) are not in the library** — the standard-vs-itemized comparison previously read as if rules were known. Rewrote `return.md` and judgment call 10: the ≈16,480 itemized figure (even assuming an unverified 10k SALT cap) is a rough client-fact sum, explicitly labeled, and the 31,500 standard deduction is safe under any plausible reading.
7. Added "(7.9832% unrounded)" to the PTC contribution math so 787.34 is traceable to the unrounded figure, not the rounded 7.983 display.

## Confirmed without change

AGI 118,350 / TI 86,850; MAGI 128,900 → allowance 10,550, carryforwards 16,500 (S-corp) + 10,468 (rental); basis walk to 11,500; PTC chain (787.34 → 902.66 → 5,416; excess 4,484 capped at 3,150 — 379.33% is inside the 300–<400% band); withholding 8,730 and NY 6,752; the 181-day resident-period computation; the CTC/tax-table household-of-4/interest-location flags. The open item that remains: **line 16's 9,945 is still unverified** — the library's Tax Table excerpt lacks the $86,850 MFJ row, and that uncertainty now correctly flows through to 10,895 / 2,165 instead of the old wrong totals.

Status remains **COMPLETE WITH OPEN ITEMS**.