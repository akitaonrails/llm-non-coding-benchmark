# STATUS — month_04 (April 2025)

**COMPLETE WITH OPEN ITEMS**

Deliverables produced under `deliverable/month_04/`: journal_entries.json (9 entries, each self-balancing), trial_balance.json (cumulative: 991,114.12 debit = 991,114.12 credit), deferred_revenue_rollforward.json (opening 110,900.00 + billed 0.00 − recognized 11,700.00 = closing 99,200.00, ties to TB 2200), bank_reconciliation.md (bank 233,880.00 vs book 282,080.00 — **difference 48,200.00, fully identified as a bank-side duplicate net-pay debit, nothing forced** — all 32 statement lines independently recomputed, all 24 deposits matched to receipts and invoices, 7 of 8 withdrawals matched to bills and payroll), open_items.md.

April result: revenue 42,150.00; expenses 83,837.78; **net loss (41,687.78)**; four-month 2025 net loss (171,231.12). Book cash 282,080.00; bank 233,880.00.

Key judgment this month: **the bank double-posted the April payroll net-pay debit (04/25 and 04/26, 48,200.00 each) for a single payroll run** (office-manager memo; Gusto ticket #GS-44812 opened 04/27, unresolved at close). The payroll register supports exactly one payroll and the books carry exactly one (JE-2025-04-08, agreed to register AND to the real 04/25 debits to the penny), so **books are NOT adjusted; no receivable booked** (library silent on bank-error claims — stated gap). The bank's own header totals include both debits, proving a processing duplicate, not a display artifact. Presentation: bank 233,880.00 + 48,200.00 pending reversal = 282,080.00 = book. When the reversal arrives, expect **no journal entry** — the reconciling item simply extinguishes; if it doesn't, escalate to the Board.

Open items (full list in month_04/open_items.md, running numbers 1–11 carried from month_03, new April item 12):
1. **NEW: bank duplicate net-pay debit 48,200.00** — bank-side error, ticket GS-44812 open; no JE booked; reversal expected in May; escalation path documented.
2. Marigold C-027 — release 2 of 12 (1,500.00) booked; 15,000.00 remains; MSA v3.2 still not in file, treatment independent of it (stated).
3. Harbor Law 2,500.00 in 5400 G&A-other (no dedicated code; disclosed); no April Harbor bill.
4. C-025 $36,000 still fully deferred, $0 recognized — final stated assumptions unchanged; year-end disclosure.
5. Trestle overlap assumption ongoing — 8,200.00 (prior, release 4 of 5; final in May) + 2,000.00 (renewal, release 4 of 12, closing 16,000.00) released; over-recognition 8,000.00 at 04/30, caps 10,000.00 by end-May if renewal actually starts Jun 2025.
6. $24,000 unidentified opening deferred revenue — $0 recognized.
7. Opening TB oddities (4000 credit 30,450 = 2024 revenue; 3900 debit 205,953) left as received; cumulative 4000 196,050.00 includes the 30,450.00; year-end disclosure committed.
8. Opening A/R 92,650.00 — four months, zero collected; all 24 April invoices again collected in-month; no allowance (library gap stated).
9. Opening A/P 17,420.00 — four months, unpaid; all April bills paid in-month.
10. Prepaid 9,600.00 — no schedule, unamortized.
11. Misfiled Dec-2025 bank_statement.csv — unused, flagged.

No prior-month corrections were needed (April documents raise no conflict with January–March; no ASC 250 matter arose). April bank statement PDF text layer prints its header values one caption below their labels (333,690.00 / 130,260.00 / 30,450.00) and displaces the 04/25 Fjord running balance onto the 04/26 row — both extraction/layout artifacts documented in bank_reconciliation.md; after content-based reading and re-merge, the recomputed ledger lands exactly on the printed ending 233,880.00.
