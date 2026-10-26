# STATUS: COMPLETE WITH OPEN ITEMS

Round 2 (client answers received 2026-10-25): **no filed figure changed.** Five open items closed
(basis facts/debt basis, Leo/Form 8332, coverage months, NY convenience-of-the-employer facts,
below-market-rent tenant relationship). Federal return and the New York **allocation** stand,
internally reconciled: `return.json`, `return.md`, `judgment_calls.md`, `QUESTIONS.md`.

Bottom line: AGI **$91,350** · taxable income **$59,850** · tax $6,708 · excess APTC repayment $1,900 ·
CTC $2,200 · total tax **$6,408** · withholding **$8,730** → **federal refund $2,322**.
S-corp loss allowed **$11,500** (not $28,000), **$16,500 suspended**; rental loss allowed **$19,550**,
**$1,468** carried forward; PTC repayment capped at **$1,900**; dependents: **Sofia only** (Leo's
8332 release to the father confirmed); NY resident days **181**, wages **100% NY** under the
convenience-of-the-employer rule (confirmed by the taxpayers: both remote arrangements were at their
own request, not employer necessity).

## Closed this round by client answers

- **Stock basis / debt basis:** no contributions since 2021, no shareholder loans, Pike (not Marcus)
  guarantees the bank line → $11,500 basis, zero debt basis stands. (Prior-year Forms 7203 still not
  in the file — see open item 2.)
- **Leo:** Form 8332 signed for 2025 (father's odd year) → not claimed; CTC $2,200 locked. *(Client's
  answer carried a literal "{TY}" placeholder, read as 2025.)*
- **Coverage:** marketplace plan dropped June 30; employer plan from July 1 → Form 8962 on six months
  is final; no second 1095-A exists.
- **NY sourcing:** employee-convenience confirmed → $68,000 / $54,000 fully NY source; day-ratio
  alternative affirmatively rejected on confirmed facts.
- **Rental:** unrelated broker-found tenant, rent never raised → library carve-out squarely met on the
  facts; loss allowed. Residual documentation risk stays flagged (open item 4).

## Open items — flagged, not resolved (see QUESTIONS.md §B)

1. **8962 family size / poverty line (only dollar-moving item).** Filed on the only FPL in the library
   (family of 4, $31,200 = the covered individuals). A family-of-3 basis would raise the repayment to
   ≈$2,806 (300–<400% cap $3,150) and cut the refund by ≈$906 — but the family-of-3 poverty line is
   **not in the library**, so that branch is unpriceable here; the figure is an unverified estimate.
2. **Prior-year Forms 7203 not in the file.** Facts confirmed by the client, but the $11,500 basis is
   still a client-prepared number; a contrary prior-year return would move everything.
3. **Depreciation support** ($270,000 building basis, 27.5-year) — client has none; no depreciation
   authority in the library; labelled **[unverified]**.
4. **Brooklyn lease / market-rent evidence** — client has none. "Fair rental for that lease" (the
   library's own condition) is undocumented at $1,500 vs ~$2,600 market; if it failed, the $21,018
   rental loss is disallowed and the PTC repayment rises to the $3,150 cap — the federal tax on that
   branch is unpriceable (see below).
5. **"No other 2025 items"** — client had nothing to confirm; return reports none because the file
   contains none. Not a signed negative confirmation.
6. **NY July–Dec day counts** — not supplied. Immaterial to wage sourcing (100% under the confirmed
   convenience rule) but relevant to the flagged residency-status assumption (open item below).

## Not computable from this library (stated, not estimated)

- **New York IT-203 tax and the disposition of $6,752 of NY withholding**, and any NYC resident tax for
  Jan–Jun: `library/` contains no NY rate schedule, deduction, or credit — only the IT-203 part-year
  sourcing excerpt. NY part-year **status** is itself an assumption: the library excerpt has no
  definition of NY residency (abode test / 183-day test).
- **Federal tax at any taxable income outside $59,000–$61,000:** the tax-table excerpt covers only that
  MFJ range, which is what makes the alternative branches in `judgment_calls.md` (§4, §3) unpriceable.
  This return lands at $59,850, so it is priced — but open item 1 or 4 could move it out of range.
- **Schedule A limits** (SALT cap, mortgage-interest limits) and **depreciation rules** are not in the
  library; labelled unverified. Neither changes the outcome here (itemized potential $13,232 vs the
  $31,500 standard deduction).
- All citations are to files listed in `library/INDEX.md`; anything else is marked unverified in
  `return.md` and `judgment_calls.md`. No facts outside `documents/` and the client's in-engagement
  answers were used.
