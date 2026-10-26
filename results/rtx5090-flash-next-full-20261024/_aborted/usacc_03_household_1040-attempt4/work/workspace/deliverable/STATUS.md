# STATUS: COMPLETE WITH OPEN ITEMS

All four required deliverables are written and current with the client's 2025-10-25 responses:
`return.json`, `return.md`, `judgment_calls.md`, `QUESTIONS.md`. The federal return is computed
end-to-end from the closed library and the client file; every cited authority is in
`library/INDEX.md`.

## Result summary (current figures)
- AGI $91,350 · taxable income $59,850 · tax $6,708 (Tax Table) · CTC $2,200 (Sofia only) ·
  8962 excess APTC $2,368.74 **capped at $1,900 repayment** · **total tax $6,408** ·
  withheld $8,730 · **federal refund $2,322**
- S-corp: $11,500 allowed, **$16,500 suspended** (Marcus's "straight off" expectation rejected)
- Rental: $19,550 allowed under the §469(i) special allowance, $1,468 carried forward
- NY: 181 resident days (Jan 1–Jun 30); convenience-of-the-employer keeps **all $122,000 of
  wages** NY source; NY tax intentionally not computed (no NY rate schedule in the library)

## Correction made during preparation (transparency)
The first draft repaid the full $2,368.74 excess APTC, having applied the $3,150 cap — which per
`form8962_instructions_excerpt.md` is the **300%–<400%** FPL band. At 292.79% FPL the correct
band is 200%–<300% → cap **$1,900**. Lines 17/24/34 corrected from 2,369/6,877/1,853 to
**1,900/6,408/2,322**; $468.74 of the excess is not repayable. Details: `judgment_calls.md` #14.

## Closed by the client's 2025-10-25 answers (do not re-ask)
- Leo: father's year; Elena signed Form 8332 (`{TY}` placeholder read as 2025) → no CTC for Leo
- Brooklyn tenant: unrelated (broker-sourced nurse, 2019); rent never raised → §280A(d)(2)(C)
  carve-out applies; rental loss allowed
- S-corp: no contributions since 2021; no shareholder loans; Pike guarantees the bank line →
  debt basis $0 stands
- Remote moves: employer-permitted, not employer-necessity → convenience-of-the-employer rule
  (all wages NY source) is confirmed, not assumed
- Marketplace plan dropped 7/1/2025 → 1095-A Jan–Jun coverage and 6-month 8962 confirmed

## Remaining open items (client has no further information)
1. **Prior-year basis unverifiable.** No 2021–2024 K-1s or Forms 7203 exist; the $11,500 opening
   basis rests solely on Marcus's note (client-confirmed as to its inputs, still not verified
   against records). Any error moves the 2025 allowed/suspended split dollar-for-dollar.
2. **Brooklyn lease never produced.** "Fair rental for that lease" rests on the client's account;
   if the written lease contradicts it, the full $19,550 rental deduction is at risk.
3. **8962 family size.** Prepared on the library's only FPL line ("used for 2025 coverage", family
   of 4, $31,200). With Leo now confirmed as claimed by his father, a family-of-3 reading is
   arguable but not computable (no family-of-3 FPL in the library). Bounded sensitivity: if a
   family-of-3 FPL keeps FPL% under 300% (FPL above $30,450), the $1,900 cap and booked repayment
   are **unchanged**; if FPL% crosses 300%, repayment would be **$2,500.50–$3,150** (≥$600
   higher); above 400% FPL there is no cap. Labeled, not booked (`judgment_calls.md` #5).
4. **NY tax not computable from the library** (no rate schedule). NY source figures, resident
   days, and method are delivered; liability/refund left uncomputed — labeled, not invented.
   NY return preparation scope and any NY carryovers also unanswered (QUESTIONS.md #5).

## Pre-delivery self-audit (2025-10-25)
- **Inputs re-verified from the source documents themselves** (all 7 PDFs text-extracted and the 3
  text sources re-read): wages 68,000/54,000; federal withholding 5,120/3,610; NY withholding
  3,842/2,910; box 12 DD 7,140 (Jul–Dec); interest 400; 1098 interest 6,480 (acquired 07/03/2025);
  K-1 (28,000)/distributions 0/AC 612,400/Part II G "Yes"/40%; 1095-A A 1,720/B 1,690/C 1,650
  monthly and 10,320/10,140/9,900 annual for Jan–Jun; custody odd/even clause; basis note
  rollforward 10,000−2,100+6,400+9,800−12,000+4,600−5,200 = 11,500 (never negative in any year);
  move dates. **No discrepancies found.**
- **Every quoted library passage re-checked verbatim** against the six library files — including
  the 8332 alternating-years clause, the below-market-rent carve-out, the guarantee/no-debt-basis
  rule, the 8962 cap bands and monthly PTC formula, the NY convenience-of-the-employer rule, and
  the Tax Table row (59,850–59,900 → 6,708). The §4 midpoint sanity check relies only on the rate
  schedule printed in the tax-table excerpt itself (labeled there "for reference only").
- **Citation hygiene fixed:** four spots in `return.md` had `documents/` files inside the bracketed
  authority citations (contrary to the library-only citation rule). Brackets now hold library
  files only; source documents are labeled "Source: documents/…". Same convention stated in
  `judgment_calls.md`.
- **Precision labels added:** the $10,000 SALT cap amount and the NY sourcing of the rental and
  pass-through items (nonresident period) are now flagged as not spelled out in the closed
  library; the itemized-vs-standard conclusion is shown robust even uncapped (18,372 < 31,500).
- **8962 family-of-3 sensitivity refined:** if a family-of-3 FPL kept FPL% under 300% (above
  $30,450), the $1,900 cap stands; the "≥$600 higher" range requires FPL% to cross 300%.
- **Schema conformance fixed:** `return.json` had carried a `_notes` key outside the engagement's
  JSON schema; removed so the file matches the specified keys exactly. Its content (sign
  conventions, cap note) was moved into `return.md` §8 — no information lost.
- **Full arithmetic chain re-run programmatically** (7203/8582/8962/1040 identities, JSON schema
  key check). **No dollar figure changed** as a result of this audit — the only computational
  correction in the engagement was the 8962 cap band fix (2,369/6,877/1,853 →
  1,900/6,408/2,322) made in the prior round, already reflected above.

Nothing was forced to balance; all internal cross-checks tie (7203: 11,500+16,500=28,000;
8582: 19,550+1,468=21,018; 8962: 7,531.26+2,368.74=9,900 and 1,900+468.74=2,368.74;
payments − total tax: 8,730−6,408=2,322).
