# Open items — January 2025 close — to the Board

No prior deliverables existed (this is the first close, month_01; deliverable/month_00/ is empty), so the books were opened directly from `documents/opening_trial_balance.csv` and `documents/note_opening_deferred.md`. No prior-month corrections were made — none could be identified against any previously issued statements.

**Client-response status (second turn):** the client replied it has **no additional information** for any of the questions filed in `deliverable/QUESTIONS.md`, which are not repeated there. Per the engagement working rules, each unknown is now converted into a **stated assumption, prominently flagged below**, and is carried into the year-end notes. None of the assumptions changes a January number — the treatments adopted were the conservative ones and stand.

## Unresolved items / stated assumptions

1. **$24,000 of opening deferred revenue is unidentified — ASSUMPTION: genuine contract liability, no revenue until documented.** Opening TB deferred revenue (2200) = **65,000.00**, but `note_opening_deferred.md` explains only **41,000.00** (Trestle prior contract). Residual **24,000.00** has no contract documentation and the client cannot provide any. Per ASC 606-10-45-2 (library/asc606_excerpts.md) it is carried as a contract liability with **$0 recognized** — no performance is evidenced. Carried in the roll-forward as a separate "UNIDENTIFIED" line. Note the exact coincidence with the Trestle renewal amount (possible premature posting of INV-2225 into the opening TB), but there is no evidence and nothing was forced. **If this remains unresolved at year-end, it will be disclosed as a contract liability of unknown origin; it will never be released to revenue absent evidence of performance (or treated as a refund liability if the Board directs).**

2. **Trestle contract overlap — ASSUMPTION: books follow the documents; renewal term is Jan–Dec 2025 and prior-contract releases continue Jan–May 2025 at 8,200/mo.** January Trestle revenue = **10,200.00** (8,200 old + 2,000 new), as the note and order form C-026 each state. If the renewal is instead early billing for a Jun 2025–May 2026 term, recognition of 2,000/mo in Jan–May is premature — **exposure through May 2025 up to 10,000.00 (2,000 × 5 months)**, reversing to correct going forward (no error in documents as received; ASC 606-10-25-10 noted re: modifications). Flagged for the Board as the largest open judgment of the close.

3. **Opening trial balance carries a revenue balance — ASSUMPTION: the 4000 opening credit of 30,450.00 is 2024 revenue never closed, and 3900's debit balance of 205,953.00 is a cumulative deficit; both left exactly as received.** The engagement's TB is cumulative from the opening TB as given, so account 4000 shows 71,100.00, of which **January 2025 revenue activity proper is 40,650.00** (monthly 30,450.00 + 8,200.00 + 2,000.00). The client cannot confirm whether 2024 statements were issued to the Board/lender; **no correction made on my own initiative** — if prior-period statements exist that embed this, the correction must follow ASC 250-10-45-23 restatement/disclosure rules (library/asc250_excerpts.md), not a quiet go-forward fix. **Disclosed at year-end either way; flagged as unknown.**

4. **Opening accounts receivable 92,650.00 fully uncollected.** All January bank receipts apply to January invoices; zero collections against opening A/R; A/R closes unchanged at 92,650.00. **ASSUMPTION: opening balances are valid and collectible — no allowance recorded.** No credit-loss guidance exists in the closed library, and any allowance estimate would be invention; explicitly noted: this is a gap in the library, not a cited exemption. Aging remains unknown; carried as an open item.

5. **Opening accounts payable 17,420.00 unpaid — ASSUMPTION: genuine open payable, remains in 2000.** No payments against it on the January statement (2000: opening 17,420 + bills 22,070 − payments 22,070 = 17,420). Vendor detail unknown; flagged.

6. **Prepaid expenses 9,600.00 — ASSUMPTION: no amortization schedule exists (client has none), so nothing is amortized.** Checklist item 3 ("prepaids reviewed") was performed to the extent the file allows: reviewed, unsupported, carried at opening value. **Risk stated: if this is a consumable prepayment (e.g., annual insurance), assets/expenses are misstated by up to the amortizable portion; unknown composition, flagged.** If no schedule surfaces, this must be resolved before year-end statements.

7. **Misfiled document:** `documents/bank_statement.csv` (workspace root) is a **December 2025** statement (negative balances ~−73k). Not applicable to this close, not used; client could not clarify. Stays flagged — when the December 2025 session arrives, the real Q4 statements must come from the client file, and this file's negative-cash trajectory is noted only as a possible warning of a future overdraft, nothing more.

## Judgment calls (unchanged)

- **Expense account codes** (5000 hosting, 5100 rent, 5200 software, 5300 marketing, 5400 G&A-other, 6000 salaries, 6100 payroll taxes & benefits, 6200 depreciation) assigned by controller from vendor-bill `category_hint`s — no client chart of accounts was supplied or available. Easy to re-map.
- **Payroll** booked as a single entry (expense 54,404.00 + 5,076.00; cash 48,200.00 + 11,280.00): withholding 6,204.00 + employer 5,076.00 = 11,280.00 remitted in-month, liability nets to zero; agrees to register **and** bank with no forcing (see bank_reconciliation.md).
- **Invoices INV-2201..2224** recognized fully in January as monthly services delivered; no implementation/set-up fees billed (none would qualify separately per ASC 606-10-25-17 / policy #2).
- **Customer C-025** absent from January invoices (IDs run C-001..C-024, then C-026). No cancellation document; no adjustment — noted only.
- Depreciation 1,777.78/mo per close_checklist item 6; no new fixed assets.

## January result (for context; full statements at year-end per contract)

Revenue (Jan activity) 40,650.00 − expenses 83,327.78 (opex 22,070.00 + payroll 59,480.00 + depreciation 1,777.78) = **net loss (42,677.78)**.
