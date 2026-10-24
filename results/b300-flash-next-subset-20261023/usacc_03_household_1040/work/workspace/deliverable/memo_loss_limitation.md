# Memo — why $16,500 of the 2025 S-corp loss is suspended (client Q&A)

*Added 2nd turn in response to Marcus's challenge to the Form 7203 result. No figures in
`return.json` change.* Authority: `library/form7203_instructions_excerpt.md`; facts from
`documents/marcus_basis_note.md` and `documents/k1_1120s_reyes_pike.pdf`.

## Marcus's questions and the answers

**"Why are you suspending $16,500?"** Because stock basis at 1/1/2025 was $11,500 and basis
cannot go below zero:

min(loss, basis) = min(28,000, 11,500) = **11,500 allowed**; 28,000 − 11,500 = **16,500 suspended**
— "suspended and carried forward indefinitely until basis is restored" (7203 excerpt, IRC §1366(d)).

**"My buddy's CPA let him take his whole loss."** Not comparable evidence. Basis is
shareholder-specific. Note the arithmetic from Marcus's own note: **the $17,200 of 2023–24
distributions are precisely the reason for the shortfall.** Without them, opening 2025 basis =
10,000 − 2,100 + 6,400 + 9,800 + 4,600 = 28,700 ≥ 28,000, and the full loss would have been
allowed. The friend either had kept profits in his company (no basis-depleting distributions), had
made direct loans to it, or his CPA got it wrong — none of which is knowable or usable from our
file. We do not copy an unverified third party's position.

**"Can't we count Pike's guarantee?"** No, twice over. The library states expressly: "A guarantee
of corporate debt does **not** create debt basis; only a direct loan from the shareholder to the
corporation does." (a) No guarantee by anyone creates debt basis; (b) even a real direct loan would
belong to **Pike's** debt basis, not Marcus's. Marcus's note confirms he never loaned the company
money.

## Planning notes (labeled by verification status)

- **Verified by library:** future basis is restored by capital contributions and the shareholder's
  share of income; suspended loss is indefinite, not lost, and is allowed as basis recovers; a
  direct Marcus→corporation loan creates debt basis; a guarantee does not.
- **UNVERIFIED (not in library, flagged per working rules):** whether a contribution or loan made
  *during* 2025 could be counted when testing the 2025 loss (timing/ordering of in-year funding vs.
  the year-end loss test). I believe in-year contributions are treated as occurring after the loss
  (so an end-of-2025 cash injection would **not** save the 2025 deduction), but no authority in
  `library/INDEX.md` covers this — do not act on it as settled. Either way it does not change the
  return as filed.
- Behavioral lever going forward: keeping income in the company in good years (instead of
  distributing) preserves basis for bad years.

## Effect on deliverables

None. Form 7203: basis_begin 11,500 / loss_allowed 11,500 / loss_suspended 16,500 stands; all
downstream Form 1040 / 8582 / 8962 figures unchanged. See `judgment_calls.md` #3 and #22.
