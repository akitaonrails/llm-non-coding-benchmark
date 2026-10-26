# Status — month_09 (September 2025)

**COMPLETE, WITH OPEN ITEMS**

All five required deliverables exist in `deliverable/month_09/`:
`journal_entries.json` (15 entries), `trial_balance.json` (cumulative;
debits = credits = $2,958,693.02), `deferred_revenue_rollforward.json`
(closing $82,150.00 = account 2200 net), `bank_reconciliation.md` (bank
$93,280.00 = books $93,280.00, difference $0.00, no reconciling items),
and `open_items.md`.

Prior months 01–08 remain closed and untouched: month_08 closing trial
balance (debits = credits = $2,706,345.24, cash $123,040.00, 2200
$68,200.00) is September's opening and was used unchanged.

## New this month — erroneous invoice voided; new paid-in-advance contract
- **INV-2409 ($1,800.00, C-012 Alder Studios LLC)** was issued 09/01 despite
  the 08/31 cancellation; the customer refused to pay (email 09/06) and had
  not paid. Voided by **same-period credit memo CM-2509-01** (JE-2509-002):
  error and correction both inside open September, so **no ASC 250** entry —
  August's books were correct. Control note to the Board: the billing system
  missed the cancellation stop.
- **C-030 Vireo Clinics PBC**: $27,000.00 annual billed upfront (INV-2422),
  wired 09/15. Billed to 2200; releases **$2,250.00/month** Sep 2025 –
  Aug 2026 (ASC 606-10-25-14(b), 25-27). Analysis at `month_09/open_items.md`
  items 1–2.

## Key numbers
- Bank and book cash at 2025-09-30: **$93,280.00**, difference $0.00; all
  32 statement lines (8 debits, 24 credits) matched 1:1 to September
  entries; running balance verified line-by-line across the page break.
- September revenue **$41,700.00** = $28,650.00 monthly (23 subscribers;
  gross $30,450.00 − $1,800.00 credit memo) + $13,050.00 scheduled releases
  (incl. Vireo $2,250.00); **no prior-period correction this month**.
- September expenses **$87,187.78** (salaries $54,404.00 + employer taxes
  $5,076.00 + vendor bills $25,930.00 + depreciation $1,777.78); net loss
  **$(45,487.78)**.
- Deferred revenue 2200 net **$82,150.00** = opening $68,200.00 + billed
  $27,000.00 − releases $13,050.00; six contracts, all current.
- A/R 1100 net $92,650.00 (opening A/R uncollected 9th consecutive month,
  now 100% legacy after the credit memo, U3); A/P 2000 net $17,420.00
  (unpaid 9th consecutive month, U9; vendor drift: AWS $10,880.00,
  Google Ads $3,650.00).
- Payroll ties three ways (register ↔ books ↔ bank) for a 9th identical
  month (U11); 2210 cumulative $101,520.00 each way, balance $0.00.
- Trial balance: debits = credits = **$2,958,693.02**.

## Open items (see `month_09/open_items.md`)
1. C-012 INV-2409 voided by same-period credit memo; billing-control note
   to the Board (confirm the stop; watch for an October invoice).
2. C-030 Vireo new paid-in-advance contract — $2,250.00/month through
   August 2026; auto-renewal watch ~Aug 2026.
3. Harbor Law LLP quarterly cadence confirmed (03/09, 06/09, 09/09) — next
   expected December.
4. U11 payroll identical — 9th month; U3 / U9 opening balances — 9th month
   static.
5. U4 prepaid schedule; U5 depreciation assumption (1510 now $37,333.02).

## Client question status
`deliverable/QUESTIONS.md`: U1–U11 on record; **September raised no new
questions** (the dispute email and the Vireo order form are each
self-contained). U10 and U12 remain closed. U6 remains moot.

## Next month (October 2025) readiness
- Monthly billing: expect **23 subscribers / $28,650.00** — verify **no
  October invoice** is issued to C-012 (confirm the billing-system stop).
- Scheduled releases rise to **$13,050.00/month** through December (Trestle
  runs out after December 2025; Pinecone final release January 2026);
  2200 opens at $82,150.00.
- Harbor Law LLP bill expected ~12/09 (quarterly cadence).
- Trestle renewal billing expected January 2026; Vireo auto-renews ~August
  2026; Saltline auto-renews May 2026.
- Depreciation $1,777.78 continues (1510 reaches $39,110.80 at 10/31).
- Root `bank_statement.csv` remains unused (U8) — reserved for month_12.
