I'll do a systematic review: re-check every fact against the documents, re-verify arithmetic with Python, and audit every citation for library-only authority.

Resuming the pre-delivery review. I have the fix list identified; now I need the exact file text to apply the edits precisely. Reading all four deliverables in parallel:

All four files re-read. Before applying fixes, let me verify the library's exact wording on the allocation schedule (so my replacement for "IT-203-B" quotes what the IT-203 excerpt actually says):

Confirmed — the library says "attach the allocation schedule" and never names IT-203-B. All fix targets verified against the exact file text. Applying all edits now in parallel:

12 of 13 edits applied. The §2 expense-caveat edit failed to match — let me re-read that section to get the exact text:

Found it — line-wrapping differed slightly ("Relied on the" ends line 41). Retrying with exact text:

All 13 edits applied. Now the final validation pass — JSON parse/shape check plus a full end-to-end arithmetic recompute cross-checked against `return.json`:

All 37 structural checks pass; the JSON IRS-shaped keys are clean, and the leftover grep hits are only the STATUS.md change-log quoting what was removed (intentional).

The 4 "failures" are bugs in my check script, not the deliverables: (1) my script treated the loss as negative while the JSON fields show loss amounts as positive; (2) my script used the FPL% rounded to 2 dp as an intermediate, giving figure 5.71152% vs the deliverable's unrounded 292.788462% → 5.711538%. Both precision paths land on the same filed numbers (434.79/mo, PTC 7,531, excess 2,369, repayment 1,900).

One real gap though: removing the `conventions` object from the JSON dropped the note that loss fields are positive amounts — I'll preserve that in `return.md`, then fix the script:

Minor edit mismatch in the scratch script (I included a stray line in oldString). Fixing just the figure computation:

All 41/41 checks pass. Final read-through of the changed sections to confirm the documents read cleanly:

All edits render cleanly. One last look at the NY section of `return.md` to confirm the allocation-schedule replacement, plus the final JSON:

Review complete. All fixes applied and re-validated — **41/41 checks pass**, and no filed figure changed.

## What I reviewed
- Every figure re-derived end-to-end in Python (wages → AGI → taxable income → tax → refund; 7203 basis rollforward; 8582 phase-out; 8962 interpolation and repayment cap; NY day count and sourcing).
- Every citation audited against `library/INDEX.md` only; every statement checked for authority the library doesn't contain; all internal cross-references reconciled (e.g., allowed + suspended = 28,000; loss + carryforward = 21,018; excess = 9,900 − 7,531).

## Errors found and fixed (the real catches)

1. **`judgment_calls.md` §11 — garbled arithmetic in the client-pushback answer.** It read `10,000 + 20,800 − 2,100 = 18,700 + 10,000…`, which as written is false (10,000+20,800−2,100 = 28,700). Corrected to: (2,100) + 6,400 + 9,800 + 4,600 = **18,700 net income**; 10,000 + 18,700 − 17,200 = **11,500**; without distributions, 10,000 + 18,700 = 28,700 ≥ 28,000. Conclusion unchanged.
2. **`return.md` §NY — unsupported form name.** "Attach IT-203-B" named a form that isn't in the library (the excerpt only says "attach the allocation schedule"). Replaced with the excerpt's own wording.
3. **`return.md` §7203 — unsupported rule.** "No prior distributions are taxable gain" asserted the excess-distribution rule, which isn't in the library (and isn't needed here). Reworded to the verifiable fact: no prior distribution reduced basis below zero.
4. **`return.md` §8962 — display rounding.** `5,217.50` corrected to **5,217.49** (monthly 434.79 unchanged; every filed figure unchanged).

## Unsupported-implication / documentation fixes

5. **`return.md` line 12:** "even before any SALT limitation" implied a SALT cap applies; reworded — no SALT-cap rule is in the library, outcome holds either way.
6. **`return.json`:** removed the extra `conventions` object so the shape matches the spec exactly; the sign convention (refund positive; loss fields positive) now lives in `return.md`.
7. **`return.md` §8962:** added (a) whole-dollar rounding check — per-month rounding gives PTC 7,530 / excess 2,370, repayment still 1,900 either way; (b) note that Elena's W-2 DD employer coverage (Jul–Dec) overlaps no marketplace-coverage month.
8. **`judgment_calls.md` §2:** removed the unclear "Elena's sole interest" phrase; added the expense-records caveat — no Brooklyn 1098 in the file, and disallowance of any single expense over the **1,468 cushion** (loss 21,018 vs allowance 19,550) would change the allowed loss.
9. **`judgment_calls.md` §9:** same whole-dollar rounding alternative added to the precision note.
10. **`STATUS.md`:** open item 5 extended to cover the expense records; added a dated "Delivery review" change list documenting all of the above.

## Final state
- `return.json` — parses; exactly the spec keys; all filed values verified (AGI 91,350; TI 59,850; tax 6,708; refund 2,322; suspension 11,500/16,500; 8582 19,550/1,468; 8962 excess 2,369 → repayment 1,900; NY 181 days, 100% both).
- **STATUS is COMPLETE WITH OPEN ITEMS** — the open items (QBI unverified/not applied, prior-year rental carryforwards unknown, Form 8332 to be executed, NY tax not computed, Brooklyn basis/expense records unverified, assumed no estimated payments) remain documented and do not affect any filed figure.