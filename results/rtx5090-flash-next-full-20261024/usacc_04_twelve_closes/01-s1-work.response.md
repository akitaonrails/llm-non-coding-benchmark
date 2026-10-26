The JE-2025-002 filter caught the Trestle invoice too — fixing to exclude annual invoices from the monthly invoice entry:

One tie-out check failed — let me inspect the actual values:

Values look correct — rerunning the tie-outs cleanly to confirm (the earlier failure was likely stale-file sequencing):

January 2025 is closed. All deliverables are in `deliverable/month_01/`, plus `deliverable/QUESTIONS.md` and `deliverable/STATUS.md` (**COMPLETE WITH OPEN ITEMS**). Note: the month's bank statement is a PDF; this model can't view PDFs, so I extracted its text with `pdftotext` — every figure was then used as-is and verified arithmetically.

**Headline finding — prior-period error corrected, not quietly absorbed.** The opening TB at 2025-01-01 contains January-2025 billings posted in error in Dec-2024, proven by three exact matches:
- 4000 has a Jan-1 balance of **30,450.00** = the 24 monthly invoices dated 2025-01-01 to the cent
- 2200 is **65,000.00** vs the client note's documented **41,000.00** (excess 24,000.00 = Trestle renewal INV-2225, dated 2025-01-01)
- implied A/R overstatement **54,450.00** = total January billing (assumed offset, flagged as a judgment call since no aging was provided)

Per ASC 250-10-45-23 I restated opening balances via **JE-2025-001 (2025-01-01)**: Dr 4000 30,450, Dr 2200 24,000, Cr 1100 54,450, disclosed prominently in `open_items.md` and the ledger, then booked January normally.

**January numbers (11 balanced entries):**
- Revenue **40,650.00** = 30,450 monthly + 8,200 Trestle prior-contract release (41,000/5 per note) + 2,000 renewal release (24,000/12 — invoice said "billed upfront," but ASC 606-10-45-2 and Board policy 1 defer it)
- Deferred roll-forward: 41,000 + 24,000 − 10,200 = **54,800.00** (Trestle prior 32,800; renewal 22,000), ties to TB account 2200
- Bank rec: **nil difference**, all 32 statement lines matched item-by-item; books and bank both 384,900.00
- Payroll agrees to register **and** bank without forcing: 54,404 − 48,200 + 5,076 = 11,280 remitted; account 2100 clears to zero
- Depreciation 1,777.78 per checklist; TB balanced at 785,980.78; net loss **(42,677.78)** with a documented bridge to the 27,100.00 cash decline

**Left open (with questions in QUESTIONS.md):** A/R composition (38,200), A/P 17,420 untouched, prepaid 9,600 unsupported (no amortization invented), whether 2024 statements were issued/closed (drives whether the restatement hits 3900 vs 4000 permanently), and the stray December-2025 `bank_statement.csv` in `documents/` (ignored for January). One of my own summary errors found in review (expense/loss figure) is disclosed in `open_items.md` — it's the kind of thing the Board note exists for; the ledger itself was never wrong.