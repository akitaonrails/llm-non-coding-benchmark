# Status — month_08 (August 2025)

**COMPLETE, WITH OPEN ITEMS**

All five required deliverables exist in `deliverable/month_08/`:
`journal_entries.json` (13 entries), `trial_balance.json` (cumulative;
debits = credits = $2,706,345.24), `deferred_revenue_rollforward.json`
(closing $68,200.00 = account 2200 net), `bank_reconciliation.md` (bank
$123,040.00 = books $123,040.00, difference $0.00, no reconciling items),
and `open_items.md`.

Prior months 01–07 remain closed and untouched: month_07 closing trial
balance (debits = credits = $2,515,587.46, cash $175,330.00, 2200
$79,000.00) is August's opening and was used unchanged.

## New this month — customer cancellation C-012 (no August adjustment)
- `documents/month_08/email_cancellation_C-012.txt` (2025-08-11): Alder
  Studios LLC gives MSA §6.2 non-renewal notice effective **2025-08-31**,
  "stop invoicing after the August invoice."
- **No adjustment booked:** INV-2385 ($1,800.00) was issued 08/01 before the
  notice, the August service month was delivered in full, and the invoice
  was collected 08/22 (bank-tied). Monthly subscriber — no deferred balance,
  no termination fee, no refund. With no remaining unsatisfied services,
  the termination is prospective-only under ASC 606 (no cumulative
  catch-up). Analysis at `month_08/open_items.md` item 1.
- Prospective impact: monthly billing run-rate drops from 24 subscribers /
  $30,450.00 to **23 subscribers / $28,650.00** beginning September.

## Key numbers
- Bank and book cash at 2025-08-31: **$123,040.00**, difference $0.00; all
  31 statement lines (7 debits, 24 credits) matched 1:1 to August entries.
  Timing observation: August receipts applied to **August** invoices
  (prior months applied to the prior month's) — no accounting effect.
- August revenue **$41,250.00** = $30,450.00 monthly + $10,800.00 scheduled
  releases; **no prior-period correction this month**.
- August expenses **$84,517.78** (salaries $54,404.00 + employer taxes
  $5,076.00 + vendor bills $23,260.00 + depreciation $1,777.78); net loss
  **$(43,267.78)**.
- Deferred revenue 2200 net **$68,200.00** = opening $79,000.00 − releases
  $10,800.00; no August upfront billings.
- A/R 1100 net $92,650.00 (opening A/R uncollected 8th consecutive month,
  U3); A/P 2000 net $17,420.00 (unpaid 8th consecutive month, U9; vendor
  drift: AWS $10,760.00, Google Ads $3,600.00).
- Payroll ties three ways (register ↔ books ↔ bank) for an 8th identical
  month (U11); 2210 cumulative $90,240.00 each way, balance $0.00.
- Trial balance: debits = credits = **$2,706,345.24**.

## Open items (see `month_08/open_items.md`)
1. C-012 cancellation — documented, no August adjustment, prospective-only.
2. Harbor Law cadence observation — no August bill; next expected September.
3. U11 payroll identical — 8th month.
4. U3 / U9 opening balances — 8th month static.
5. U4 prepaid schedule; U5 depreciation assumption (1510 now $35,555.24).

## Client question status
`deliverable/QUESTIONS.md`: U1–U11 on record; **August raised no new
questions** (the C-012 email is self-contained). U10 and U12 remain closed.
U6 remains moot.

## Next month (September 2025) readiness
- Monthly billing: expect **23 subscribers / $28,650.00** — verify no
  September invoice is issued to C-012 (Alder Studios LLC).
- Scheduled releases unchanged at $10,800.00/month through December
  (Pinecone continues to January 2026); 2200 opens at $68,200.00.
- Harbor Law LLP bill expected ~09/09 (quarterly cadence) — book when
  received; raise it if absent.
- Pinecone term ends 2026-01-31 (final release January); Trestle renewal
  billing expected January 2026; Saltline auto-renews May 2026.
- Depreciation $1,777.78 continues (1510 reaches $37,333.02 at 09/30).
- Root `bank_statement.csv` remains unused (U8) — reserved for month_12.
