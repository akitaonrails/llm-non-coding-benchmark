# Status — Reyes 2025 engagement

**COMPLETE WITH OPEN ITEMS** (open items are now limited to documented assumptions — see below;
all round-1 client questions were answered and the deliverables updated accordingly)

All required deliverables are present: `return.json`, `return.md`, `judgment_calls.md`,
`QUESTIONS.md`, `STATUS.md`. Every citation resolves to a file listed in `library/INDEX.md`;
nothing outside the workspace was used. No figure was forced to reconcile.

Headline: federal **refund $2,322.00**; S-corp loss allowed 11,500 / suspended 16,500; rental
loss allowed 19,550 / carryforward 1,468; APTC repayment capped at 1,900; CTC 2,200 (Sofia only);
NY part-year with 183 resident days and full-year NY-source wages under the convenience rule.

## Resolved this round by client confirmation (no figure changes)

- Leo not claimed — Form 8332 signed for the father's year (odd-year rule).
- Convenience-of-the-employer confirmed for both spouses; post-move NY workdays are now
  immaterial to wage sourcing, so the earlier zero-workday assumption is no longer needed.
- Rental tenant unrelated, rent never raised — library's below-market carve-out applies.
- S-corp basis note complete — no post-2021 contributions, no shareholder loans, debt guaranteed
  by Pike, not Marcus (zero debt basis).

## Remaining open items (documented assumptions; each could change figures)

1. **8962 family size 4 vs 3** — family size 4 used because the library supplies only the
   4-person FPL and no shared-policy allocation rule or 3-person data exists, and the client has
   no additional information (Leo's individual SLCSP; whether the father claimed any credit for
   Leo). If a 3-person allocation applied, repayment ≈ $2,989 (cap $3,150) → refund ≈ $1,233
   (swing ≈ $1,089). The 3-person FPL figure itself is outside the library (unverified).
2. **Form 8332 year wording** — the client's reply said "{TY}"; confirm the executed release
   names tax year 2025. No effect if correct.
3. **NY tax not computed** — the library contains no NY rate tables, so NY part-year tax is not
   fabricated; the excess NY withholding ($6,752) is recovered on IT-203, which must be prepared
   with NY-forms authority outside this engagement. The IT-203 excerpt also supplies no sourcing
   rule for real-property income; the full-year NY sourcing of the Brooklyn condo rental is flagged
   as an outside-library assumption (judgment call #12).
4. **Unverified inputs carried through** — 2019 Zillow rent estimate (used only contextually,
   never in a computation); "fair rental for that lease" undefined in the library.

## Verification notes

- All internal cross-foots in `return.json` pass (AGI 91,350; taxable income 59,850; tax 6,708;
  total tax 6,408; refund 2,322.00).
- Taxable income 59,850 falls inside the library's tax-table excerpt (row 59,850–59,900 → $6,708,
  cross-checked by the midpoint method). Reversal of the rental or S-corp calls would push
  taxable income outside the excerpt — flagged in `judgment_calls.md`, not extrapolated.
- Both Form 8962 rounding conventions tested; the $1,900 repayment cap binds under either.
- Pre-delivery self-audit performed: corrected Leo's name/DOB in `return.json` (custody order says
  Leo Castellano, DOB 03/14/2016 — the JSON had "Leo Reyes, b. 2017-06-21"); fixed the garbled 2024
  rollforward row in `return.md`; recomputed the 3-person 8962 scenario (repayment ≈ 2,989, refund
  ≈ 1,233, swing ≈ 1,089); labeled three statements that asserted authority the library does not
  contain — the $10k SALT cap, gain on distributions exceeding basis (moot on these facts), and the
  NY real-property rental sourcing rule (judgment call #12) — as outside-library or moot. No
  headline figure changed.
