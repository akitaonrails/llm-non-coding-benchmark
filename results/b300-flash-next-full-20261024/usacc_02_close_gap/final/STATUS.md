# Engagement status — Brightline Cabinetry LLC, March 2026

**Status: COMPLETE WITH OPEN ITEMS**

Prepared by the outsourced accounting function, March 2026 close; updated
2026-10-25 after the client's reply (answers recorded in QUESTIONS.md — none
re-asked). All amounts USD. Every reconciling item cites a source document
from `workspace/documents/`; procedures follow `library/bank_rec_standard.md`
and `library/close_policy.md` (the two items in `library/INDEX.md`). Nothing
is plugged.

## Resolved by the client's 2026-10-25 reply

- **Cascade CH-7731 duplicate — closed.** Owner confirms one invoice, keyed
  twice (email then mail), paid once. AJE-1's single reversal is complete;
  the email-copy row exists only as a March posting (appended at the end of
  the March ledger), so it was never in the closed February A/P — no second
  reversal is needed (open_items.md §5).
- **$1,500.00 *4420 transfer — closed.** Owner's personal checking, moved in
  to cover payroll: "my money, not a sale." Booked to 3100 Owner's
  contributions by **AJE-8** (Dr 2100 1,500.00 / Cr 3100 1,500.00), per
  policy that owner money flows through 3200/3100, never revenue or expense.
  Balance-sheet only — net income and the reconciled cash figure unchanged.
- **Uchi $212.00 dinner — closed.** Owner confirmed personal ("grabbed the
  wrong card. Put it on me."). AJE-7 draw classification is final.
- **Hardaway $9,800.00 — instruction received, deliberately not booked.**
  Owner: "Still arguing with them. Don't write it off yet." Full amount
  stays in A/R; no write-off, no credit memo, until the dispute settles with
  documentation (open_items.md §1).

## What is done

- **`bank_reconciliation.md`** — Operating account reconciled to a true cash
  balance of **$10,318.30**; adjusted book equals adjusted bank to $0.00, no
  unexplained difference. Every clearing item matched line-by-line; Delgado
  #4471 confirmed as a deposit in transit, not an outstanding check. Credit
  card statement ties to the books exactly ($2,306.12).
- **`adjusting_entries.json`** — Eight entries, AJE-1…AJE-8, each with a
  document citation: duplicate Cascade bill reversal ($4,860.00); unrecorded
  mobile deposit ($4,312.00, to suspense per policy); bank fee ($35.00);
  $1,500.00 transfer moved out of revenue to suspense (AJE-4) and then to
  Owner's contributions on the owner's confirmation (AJE-8); software
  license fully deferred ($1,188.00 — term 04/2026–03/2027 per the card
  statement); Allied Q2 premium deferred in full ($1,150.00 — Apr–Jun
  assumed, still unconfirmed); Uchi dinner as owner's draw (confirmed).
- **`trial_balance_2026-03-31.json`** — Post-AJE trial balance,
  **debits $429,792.07 = credits $429,792.07** (AJE-8 is a credit-side
  reclass, suspense 2100 $5,812.00 → $4,312.00 and contributions 3100
  $1,500.00, so totals are unchanged). March net income $15,821.53;
  year-to-date net income $25,084.23. Cash on the TB equals the reconciled
  balance.

## Deliberately not done (documented, not plugged)

- **Hardaway disputed credit:** not recorded — no signed document exists,
  the close policy forbids unsupported adjustments, and the owner
  instructed (2026-10-25) not to write it off. This is also why the owner's
  earlier request to "put it somewhere sensible" (`email_owner.txt`) was
  declined: burying a difference is a plug by another name, and the reports
  the loan officer sees carry every item on their face.
- **Opening $2,400 prepaid amortization, March depreciation, March sales-tax
  accrual, A/R and A/P gap clearance:** each needs client data that does not
  exist — and the client has now confirmed it has none. Recorded-none is
  stated explicitly in open_items.md §§3–8.
- **AJE-5/AJE-6 carry stated assumptions** (deferral start dates; Allied's
  Apr–Jun period) — client has no further detail, so the assumptions stand
  as disclosed.

## Remaining unknowns — explicitly flagged (full detail in open_items.md)

The client's 2026-10-25 reply states it has no additional information beyond
the items above. What therefore remains open on the March 31 books:

1. **$4,312.00 unidentified mobile deposit in suspense (2100).** Owner and
   office manager Carla cannot identify it; client asked us to "park it" —
   policy's parking account is 2100, which is where it sits, disclosed.
   Policy limit: April month-end. Next step: bank's mobile-deposit image.
   Not classified to revenue or contributions on our own; a post-delivery
   request (2026-10-25) to rebook it to income or contributions before the
   bank sees it was declined for that reason (open_items.md §2).
2. **A/R: books $115,288.00 vs aging $56,100.00 — $59,188.00 unexplained.**
3. **A/P: $27,615.40 February carryforward with no supporting document;
   Rivera $5,600.00 and Allied $1,150.00 invoices not provided.**
4. **Prepaid insurance: $2,400.00 opening balance with no policy schedule;
   Allied coverage dates unconfirmed.**
5. **Depreciation: none recorded (no asset list or schedule exists);
   Equipment $148,000.00 / Accum. dep. $61,250.00 presented as-is.**
6. **Sales tax: registration, filings and taxable-sales detail unknown;
   $4,121.55 liability untouched; a filing may be due independent of this
   close.**
7. **Shop lease absent — rent run-rate for future months unvalidated.**
8. **Cash-presentation preference and possible overdraft fees on a second
   account: no answer.**
9. **Controls: vendor + invoice-number duplicate check offered for April;
   no decision yet.**

None of items 2–9 blocks the deliverables: the books close and balance as
delivered, each unknown is disclosed where the number appears, and each
converts to a small follow-up entry when information arrives. Item 1 has a
policy deadline (April month-end).
