# Status — month_05 (May 2025)

**COMPLETE WITH OPEN ITEMS**

All five required deliverables for `deliverable/month_05/` are present:
`journal_entries.json` (16 entries, no prior-period correction needed this
month),
`trial_balance.json` (cumulative; debits = credits = $2,074,891.90),
`deferred_revenue_rollforward.json` (closing $91,000.00 ties to account 2200),
`bank_reconciliation.md` (bank $260,300.00 = books $260,300.00, difference
$0.00, no reconciling items), `open_items.md`.

Prior months stand as closed and validated: month_01–month_04 files unchanged
this session (month_04 closing TB — debits = credits $1,773,554.12, cash
$233,880.00 — is the May opening).

## Closing date record
- Period: May 2025 (month 5 of 12). All entries dated 2025-05-01 through
  2025-05-31. Bank activity spans 05/05–05/26; statement covers
  05/01–05/31.
- Opening point: month_04 close. No opening balances changed; no ASC 250
  entry was required for May activity. April's duplicate Gusto debit stays as
  booked in April (current-period bank error, claim asset 1200); the May
  refund is a May event booked currently (JE-2505-005).

## Key figures
- **U12/G1 CLOSED with cash verified:** the Gusto refund appears on the May
  statement — `ACH CREDIT GUSTO REFUND $48,200.00`, 05/09 — booked Dr 1000 /
  Cr 1200 (JE-2505-005). Account 1200 nets to **$0.00** (48,200 Dr = 48,200
  Cr). No write-off; April books unchanged.
- Bank/book cash 2025-05-31: **$260,300.00**, difference $0.00. All 26
  statement credits and all 7 statement debits matched 1:1; no deposits in
  transit, no outstanding items, no unrecorded bank items — a natural tie
  this month.
- **New contract C-028 Quarry Analytics Co:** $30,000.00 billed upfront
  (INV-2324, JE-2505-002 → 2200), wire collected 05/15 (JE-2505-004), May
  release $2,500.00 = 30,000 ÷ 12 (JE-2505-016). Term fully documented on the
  order form — **no new question** (contrast Pinecone).
- A/R net **$92,650.00** — May billings ($30,450, INV-2300…2323) all
  collected in-month; opening A/R uncollected a fifth month (U3). A/P net
  credit **$17,420.00** unchanged (fifth month, U9); verified Harbor Law's
  March $2,500.00 was paid in March, so it is outside the 17,420.
- Deferred revenue 2200 net **$91,000.00**: opening $75,200.00 + billed
  $30,000.00 − recognized $14,200.00. May releases: Trestle prior $8,200.00
  (**line closed** — service period ended 05/31), Trestle renewal $2,000.00,
  Marigold $1,500.00, Quarry $2,500.00; Pinecone $0.00 (U10).
- May result: revenue $44,650.00 (30,450 monthly + 14,200 releases), expenses
  $84,007.78 (54,404 gross salaries + 5,076 employer taxes + 22,750 vendors +
  1,777.78 depreciation), net loss **$(39,357.78)**.
- Payroll three-way tie (register ↔ books ↔ bank) holds: single net-pay debit
  48,200 and single tax remit 11,280 on 05/25 — **exactly one GUSTO NET PAY
  debit this month**; April's duplicate pattern did not recur. 2210 cleared
  cumulatively ($56,400.00 Dr = $56,400.00 Cr).

## Open items (detail in `month_05/open_items.md`, question record in `QUESTIONS.md`)
1. **CLOSED — Gusto duplicate-debit recovery.** $48,200.00 refunded 05/09,
   verified on the statement, booked; 1200 → $0.00. U12 retired. Recommend
   the Board have Gusto close ticket GS-44812 with a root cause (control
   follow-up, no accounting item remains).
2. **Payroll register identical five months running (U11)** — Jan = Feb =
   Mar = Apr = May in every field. May clean at the bank. Not re-asked.
3. Pinecone $36,000 still fully deferred, $0 recognized, fourth month (U10).
4. Opening A/R $92,650 and opening A/P $17,420: fifth month with zero
   activity against either (U3, U9).
5. Prepaid $9,600 still unamortized (U4); depreciation $1,777.78/mo per close
   checklist (U5); 1510 accumulated $30,221.90.
6. Deferred revenue classification (table in open_items): Trestle renewal
   $14,000, Marigold $13,500, Quarry $27,500 all current; Pinecone $36,000
   not classifiable (U10); no non-current contract-liability account exists
   (U6).
7. Minor recurring-vendor variances noted, not adjusted: AWS $10,400.00 vs
   April $10,280.00; Google Ads $3,450.00 vs April $3,400.00 (both match
   vendor bills 1:1).

## Client question status
January questions 1–9 and February F1–F5: closed as asked, carried as U1–U11.
March: no new questions. April G1 (Gusto refund): **closed as asked and now
closed by evidence** — refund verified on the May 05/09 statement and booked.
May: **no new questions** (record in `QUESTIONS.md`) — the new Quarry contract
is fully documented on its order form, so nothing was re-asked or newly asked.

## Remaining unknowns — explicit status after the May close

**U12 resolved and retired** (cash verified 05/09). Still open and **not**
re-asked: **U1** (subscription start dates behind opening A/R), **U2**
(equity/AP composition detail), **U3** (opening A/R collectibility — five
months zero collections), **U4** (prepaid amortization schedule), **U5**
(depreciation life/method — 36-mo SL assumption per close checklist), **U6**
(no non-current contract-liability account in the chart), **U7** (payroll
withholding component split — derived gross−net), **U8** (root
`bank_statement.csv`, Dec-2025 negative balances — reserved for the December
2025 close), **U9** (opening A/P aging — five months unpaid), **U10**
(Pinecone term / MSA v3.2 — $36,000 still $0 recognized), **U11** (five-month
identical payroll registers).

## Engagement readiness — month_06 (June 2025)

June source documents have not yet been provided (`documents/` contains
month_01–month_05 only). The June close will require: June bank statement,
invoices, cash receipts, payroll register, vendor bills, and any new
documents. Scheduled June items already known: (1) deferred-revenue releases
total **$6,000.00** — Trestle renewal $2,000.00, Marigold $1,500.00, Quarry
$2,500.00; Trestle prior line is closed and will not reappear; Pinecone stays
$0.00 (U10). (2) 2200 opening $91,000.00 before any new June billings.
(3) Depreciation $1,777.78 continues (1510 accumulated would reach
$31,999.68).
(4) If the payroll register repeats identically for a sixth month, continue
carrying U11 per protocol without re-asking.
