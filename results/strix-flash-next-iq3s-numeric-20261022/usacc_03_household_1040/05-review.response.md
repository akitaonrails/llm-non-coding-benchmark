I'll do a full independent review pass: re-derive every number from source documents, verify every citation against the actual library text, and cross-check consistency between deliverables.

Now re-verifying against source material. Reading the library and documents:

Library text confirms all six citation sources. Now re-extracting the client documents to re-verify every input figure:

All source figures re-verified against documents. Now re-deriving the full chain from scratch, including the worst-case (C) scenario numbers I want to re-check:

Continuing with the remaining fixes. Let me pull the exact current text of the pending spots:

Applying the JSON and return.md §7 fixes now, and reading the exact QUESTIONS/STATUS item-C text:

Now fixing QUESTIONS.md (header, item C, item D's sourcing claim) and STATUS.md item C:

Updating the STATUS header to record this review pass, then running final validation:

Script syntax slip (mixed dict/set literal) — fixing and re-running:

The sweep caught one more thing: a `**[INDEX]**` tag in `judgment_calls.md`. Checking its context:

Checking exactly how many authorities INDEX.md lists (my validation flagged this sentence's "seven files" claim):

Now re-running the full validation sweep:

This §10 heading is now inaccurate — the section covers both turn-2 answers and turn-4 "no further information" responses:

Re-running the full validation:

All checks pass. Final visual sanity check on the files edited this pass:

Both files look right. One last tightening — the STATUS header lists only three of the review fixes; making it complete:

Review pass complete. Every source figure was independently re-derived (whole chain recomputed in code), and the full validation suite now passes: template keys exact, all JSON arithmetic identities hold, Form 8962 reproduces from its own stated inputs, every citation is one of the six library files, every cross-reference resolves, and no stale text remains.

## What I changed

**Actual errors (3):**

1. **Day-ratio arithmetic** (`judgment_calls.md` #11) — the rejected day-apportionment alternative showed 33,709/26,745; correct values are 68,000×181/365 = **33,721** and 54,000×181/365 = **26,778**. These were only in the rejected-alternative discussion, so nothing filed changes.
2. **`return.json` 8962 applicable figure: 5.71 → 5.7115.** At 5.71% the JSON no longer reproduces its own PTC (it yields 7,532, not 7,531). With 5.7115 the whole 8962 chain (PTC 7,531, excess 2,369, repayment 1,900) regenerates exactly from the stored fields.
3. **Open item C's worst-case estimate was understated** — it said "≈ $2,500." If the below-market condo rent were recharacterized, the full 21,018 rental loss disallowance *cascades through Form 8962*: AGI rises to 112,368, tax +2,522, and the repayment cap steps 1,900 → 3,150 (+1,250). **Total ≈ $3,770, flipping the 2,322 refund to ≈ 1,450 owed.** Corrected in `QUESTIONS.md`, `STATUS.md`, `return.md` §10, and `judgment_calls.md` #3. This was the largest misstatement in the file set.

**Unsupported authority relabeled (1):**

4. **NY sourcing of the Brooklyn rental** was asserted as fact in four places. The library's IT-203 excerpt defines sourcing only for *wages* (convenience-of-the-employer); it states no real-property rule. Now labeled an unverified assumption everywhere (`return.md` §7/§7-day-count/§10, `judgment_calls.md` #10/#11, `return.json` `ny.method`, `QUESTIONS.md` D). Outcome-neutral: Jan–Jun rental is resident-period income regardless, Jul–Dec is a net loss, and no NY tax figure is computed.

**Accuracy/consistency fixes (4):**

5. `judgment_calls.md` #13 claimed INDEX "limits the authorities to the seven library files" and used a `**[INDEX]**` citation tag — INDEX indexes **six** content files (it's the 7th file but not an indexed authority), and it isn't a citation key. Rewritten plainly.
6. `QUESTIONS.md` header said "turn 2"; it reflects turn-4 responses. Fixed.
7. `return.md` §10 heading said "(turn 2)"; the section now also carries turn-4 "no further information" responses. Relabeled "turns 2 and 4".
8. `return.md` §4 — the 23,520 "known deductible amounts" figure is now flagged as *deliberately overstated*: the condo is rented all year, so its 11,900 interest + 5,140 tax are Schedule E amounts that can't also sit on Schedule A. (Only strengthens the standard-deduction call.)

**Unchanged — all core figures verified correct:** wages 122,000; S-corp loss allowed 11,500 / suspended 16,500; rental loss 21,018 / allowance 19,550 / carryforward 1,468; AGI 91,350; taxable 59,850; tax 6,708 (table row + midpoint cross-check); CTC 2,200; 8962 repayment 1,900; total tax 6,408; withholding 8,730; **refund $2,322**. NY tax remains deliberately uncomputed — the library has no NY rate schedules, and no deliverable quotes a NY refund or balance due.

The deliverables in `/work/deliverable/` are ready to deliver.