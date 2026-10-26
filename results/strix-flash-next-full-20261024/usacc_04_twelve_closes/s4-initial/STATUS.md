# Status — month_04 (April 2025)

**COMPLETE WITH OPEN ITEMS**

All five required deliverables for `deliverable/month_04/` are present:
`journal_entries.json` (14 entries, no prior-period correction needed this
month),
`trial_balance.json` (cumulative; debits = credits = $1,773,554.12),
`deferred_revenue_rollforward.json` (closing $75,200.00 ties to account 2200),
`bank_reconciliation.md` (bank $233,880.00 = books $233,880.00, difference
$0.00 — see the duplicate-debit note below), `open_items.md`.

> **Transparency note (month_03).** The March deliverables had not been
> written to disk in the March session. They were materialized **this
> session** from the previously validated March analysis, into
> `deliverable/month_03/` (all five files). March figures are unchanged from
> that analysis: debits = credits = $1,535,056.34, cash $333,690.00 = bank,
> 2200 closing $86,900.00, net loss $(44,017.78). Every automated check
> passed for both months (51/51).

## Closing date record
- Period: April 2025 (month 4 of 12). All entries dated 2025-04-01 through
  2025-04-30. Bank activity spans 04/05–04/26; statement covers
  04/01–04/30.
- Opening point: month_03 close (debits = credits = $1,535,056.34). No
  opening balances changed; no ASC 250 entry was required for April
  activity — the duplicate net-pay debit is a **current-period bank error**,
  not a prior-period error, so it is booked currently, not restated.

## Key figures
- Bank/book cash 2025-04-30: **$233,880.00**, difference $0.00; all 24
  credits and all 8 debits matched 1:1; no deposits in transit or
  outstanding items. The tie holds **because the duplicate $48,200.00
  GUSTO NET PAY debit (04/26) was recorded** — as claim asset 1200, not as
  expense.
- **New: account 1200 Due from Gusto — duplicate net-pay debit, $48,200.00
  debit.** Unconfirmed at close (U12); since closed: Gusto admitted the double
  debit and posted the refund **2025-05-09** — recovery entry books in May
  against the May statement (see readiness section).
- A/R net **$92,650.00** — April billings ($30,450) all collected in-month;
  opening A/R uncollected for a fourth month. A/P net credit **$17,420.00**
  unchanged (fourth month, U9).
- Deferred revenue 2200 net **$75,200.00**: Trestle prior $8,200.00 (final
  month May 2025), Trestle renewal $16,000.00, Marigold $15,000.00, Pinecone
  $36,000.00 (recognized $0 — U10). April releases $11,700.00
  (8,200 + 2,000 + 1,500).
- April result: revenue $42,150.00, expenses $83,837.78, net loss
  **$(41,687.78)**. The duplicate debit does **not** touch expenses.
- Payroll three-way tie (register ↔ books ↔ bank) holds for the single
  April run; the 04/26 duplicate matches no register item and was isolated,
  not forced into payroll. 2210 cleared cumulatively ($45,120.00 Dr =
  $45,120.00 Cr).

## Open items (detail in `month_04/open_items.md`, question record in `QUESTIONS.md`)
1. **NEW, MATERIAL — duplicate Gusto net-pay debit $48,200.00.** Two
   GUSTO NET PAY debits (04/25, 04/26) vs one payroll run (register; office
   manager's note, Gusto ticket GS-44812). Booked Dr 1200 (new account,
   judgment call) / Cr 1000 — a recovery claim, not payroll expense.
   Recovery unconfirmed at close → new standing unknown **U12**; new question
   **G1** asked this session. Deadline discipline required through ~2025-06-25.
   **Post-close client reply (office manager): "Gusto admitted the double
   debit; refund posted May 9."** April books stand unchanged — the refund is
   a May event, not an April restatement. Recovery entry scheduled for the
   month_05 close (Dr 1000 / Cr 1200, $48,200.00, 2025-05-09), conditional on
   the credit appearing on the May bank statement. **U12 resolved by reply;**
   cash confirmation pending month_05. No write-off needed.
2. **Payroll register identical four months running (U11)** — Jan = Feb =
   Mar = Apr in every field. Previously a document-quality observation;
   April's duplicate debit shows a payment-control failure that reached
   cash, materially strengthening the concern. Not re-asked per protocol.
3. Pinecone $36,000 still fully deferred, $0 recognized, third month (U10).
4. Opening A/R $92,650 and opening A/P $17,420: fourth month with zero
   activity against either (U3, U9).
5. Prepaid $9,600 still unamortized (U4); depreciation $1,777.78/mo per
   close checklist (U5); 1510 accumulated $28,444.12.
6. Deferred revenue classification: Marigold and Trestle amounts are
   current; Pinecone $36,000 not classifiable (U10); no non-current
   contract-liability account exists in the chart (U6).
7. March adds no new unknowns (Marigold fully documented on its order
   form; 6600 Professional fees opened as a disclosed judgment call);
   U1–U11 all carried forward, none re-asked.

## Client question status
January questions 1–9: answered "no additional information"; closed as
asked, carried as U1–U9. February questions F1–F5: closed as asked; F2/F3
answered (confirming Pinecone treatment); F1/F4 → U10, F5 → U11. March:
**no new questions** (record in `QUESTIONS.md`). April: one **new** question
**G1** (status and path of the $48,200.00 duplicate-debit refund, GS-44812,
60-day window to ~2025-06-25) — **closed as asked: answered this round**
("Gusto admitted the double debit; refund posted May 9"); recovery entry
scheduled for month_05 as above. No previously answered or carried item has
been re-asked.

## Remaining unknowns — explicit status after this reply round

Client reports **no additional information** on anything else, so the
following remain open and are **not** re-asked: **U1** (subscription start
dates behind opening A/R), **U2** (equity/AP composition detail), **U3**
(opening A/R collectibility — now four months zero collections), **U4**
(prepaid amortization schedule), **U5** (depreciation life/method — 36-mo SL
assumption per close checklist), **U6** (no non-current contract-liability
account in the chart), **U7** (payroll withholding component split — derived
gross−net), **U8** (root `bank_statement.csv`, Dec-2025 negative balances —
reserved for the December 2025 close), **U9** (opening A/P aging — four
months unpaid), **U10** (Pinecone term / MSA v3.2 — $36,000 still $0
recognized), **U11** (four-month identical payroll registers — **strengthened
by the April duplicate debit**). **U12 is resolved by reply** (Gusto admitted,
refund 05/09) and will be formally closed in the month_05 close once the
refund credit is verified on the May bank statement.

## Engagement readiness — month_05 (May 2025)

May source documents have not yet been provided (`documents/` contains
month_01–month_04 only). The May close will require: May bank statement,
invoices, cash receipts, payroll register, vendor bills, and any new
documents. Scheduled May items already known: (1) recovery entry
Dr 1000 / Cr 1200 **$48,200.00** dated 2025-05-09, verified against the
statement; (2) Trestle prior contract **final release $8,200.00** (final
service month May 2025), closing that rollforward line; (3) Pinecone release
stays $0.00 (U10); (4) Marigold $1,500.00 and Trestle renewal $2,000.00
continue.
