Good discipline — full audit before delivery. I'll re-verify every input against the source documents, every citation against `library/INDEX.md`, and every figure by recomputation.

INDEX confirms 6 citable files; `custody_agreement_excerpt.pdf` and other PDFs are **source documents**, not authorities. Now reading all library files and source documents to re-verify inputs and cited language:

All source figures now re-verified against actual document text. Key confirmations:

- **W-2s**: 68,000 / 5,120 / NY 3,842; 54,000 / 3,610 / NY 2,910; Box 12 DD 7,140 (Jul–Dec) ✓
- **1099-INT**: 400 ✓; **1098**: 6,480, Tampa acquired 07/03/2025 ✓
- **K-1**: line 1 (28,000), line 16 = 0.00, AC 612,400, Part II G "Yes", 40% ✓
- **1095-A**: A 1,720 / B 1,690 / C 1,650 monthly; annual 10,320 / 10,140 / 9,900; Jan–Jun; covered individuals = 4 including Leo ✓
- **Custody order**: father odd years / mother even years → **2025 = father's year** ✓
- **Basis note rollforward**: 10,000 −2,100 +6,400 +9,800 −12,000 +4,600 −5,200 = **11,500** ✓ (basis never negative at any point, so no ordering issue — each intermediate balance stays positive)
- **Move email**: out of NY by June 30, Tampa closed July 3 → resident period Jan 1–Jun 30 = 181 days ✓; both employers NYC, remote by employer permission (convenience, not necessity) ✓

Now re-reading the deliverables to audit citations and cross-consistency:

`return.md` edits done. Now the `judgment_calls.md` updates — let me pull the exact text of entries #5 and #7:

Now `STATUS.md` — reading it in full to refine open item 3 and add the audit record:

All edits applied. Now the final verification pass — full assert chain + JSON schema key check + citation-hygiene grep:

One schema deviation found: `return.json` has an extra `_notes` key not in the CONTRACT schema. Checking its contents before moving it:

`_notes` is an extra key outside the CONTRACT schema. Its content (sign conventions, cap explanation) belongs in `return.md`, not in the schema-locked JSON. Fixing both:

All green. One last audit-record entry in `STATUS.md` for the JSON schema fix:

Audit complete. Here's exactly what I found and what I changed.

## What changed

**1 real defect — schema conformance in `return.json`**
- The JSON carried a `_notes` key that is **not in the CONTRACT schema**. Removed it so the file matches the specified keys exactly; its content (sign conventions, the repayment-cap note) was moved into `return.md` §8 so no information was lost. Verified with a programmatic exact key-match.

**Citation hygiene (4 spots in `return.md`, 1 in `return.json`'s method text)**
- The engagement rules say authority citations must point **only** at `library/INDEX.md` files — but four bracketed citations mixed in `documents/` files (custody PDF, basis note, 1095-A/W-2, and the move email was cited in authority-bracket form entirely). Brackets now hold library files only; source documents are relabeled "Source: documents/…". A `comm` cross-check confirms every remaining bracketed citation is one of the 6 INDEX files.
- Added the same convention statement to `judgment_calls.md`.

**Unsupported-authority labels added (things I'd stated as if library-backed but the excerpts don't spell out)**
- The **$10,000 SALT cap amount** isn't in the library — now labeled unverified context in §4; the standard-deduction conclusion is robust even with *no* cap (6,480 + 11,892 = 18,372 < 31,500).
- **NY sourcing of the rental and S-corp/pass-through items** during the nonresident period: the library excerpt only states the sourcing rule for *wages*. Now labeled unverified in §7, `judgment_calls.md` #7, and the JSON `method` string (immaterial here — NY tax isn't computed anyway).

**Precision fix to the family-of-3 sensitivity (`judgment_calls.md` #5, STATUS item 3)**
- My earlier "at least $600 higher" claim silently assumed FPL% crosses 300%. Now stated properly: if a family-of-3 FPL fell between $30,450 and $31,200, FPL% stays under 300% and the **$1,900 cap and repayment are unchanged**; only if FPL% crosses 300% does repayment land in [$2,500.50, $3,150].

**Wording**
- §8's garbled sign check "91,350 + (−31,050 sign-checked) = 122,400" rewritten as the clean chain 122,000 + 400 = 122,400; 122,400 − 31,050 = 91,350.
- STATUS: renamed the correction heading (the 8962 cap fix was last round, not this one) and added a dated "Pre-delivery self-audit" section recording everything below.

## What I re-verified and found **correct** (no changes needed)

- **Every source figure**, re-extracted directly from the 7 PDFs and 3 text files: wages, both W-2 withholdings, box 12 DD, interest, 1098 (6,480, acquired 07/03/25), K-1 (28,000)/0/612,400/Part II G "Yes", 1095-A monthly and annual figures for Jan–Jun, custody odd/even clause, move dates. Basis rollforward re-checked year-by-year — basis never goes negative, so ordering is safe: ending 2024 basis is 11,500.
- **Every quoted library passage**, verbatim — including the 8332 alternating-years clause, below-market-rent carve-out, guarantee/no-debt-basis rule, 8962 cap bands and monthly PTC formula, NY convenience rule, and the Tax Table row (59,850–59,900 → 6,708). The §4 midpoint sanity check leans only on the rate schedule printed in the tax-table excerpt (labeled there "for reference only"), so it's library-covered.
- **All arithmetic**, re-run as a Python assert chain including the exact rounding chain for 8962 (contribution 434.79 is rounding-insensitive) and the 8962 cap identity (1,900 + 468.74 = 2,368.74).

**No dollar figure changed this round.** The final numbers stand: AGI 91,350 · TI 59,850 · total tax 6,408 · refund **2,322**; S-corp 11,500 allowed / 16,500 suspended; rental 19,550 / 1,468; 8962 repayment 1,900. (The only computational correction in the engagement was the 8962 cap-band fix — 2,369/6,877/1,853 → 1,900/6,408/2,322 — made in the *prior* round, not this audit.)

Still irreducible, and flagged as such in STATUS/QUESTIONS: the basis note is the sole evidence for opening basis; no written lease exists; family-of-3 FPL isn't in the library; NY tax can't be computed from the closed library; NY prep scope (Q5) remains unanswered.