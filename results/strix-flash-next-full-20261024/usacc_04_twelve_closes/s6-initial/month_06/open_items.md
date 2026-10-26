# Open Items — June 2025 Close

**To:** Board, Northwind Analytics Inc.
**From:** Controller
**Period:** June 2025 (month 6 of 12)

No prior-period errors were identified in June activity, so **no ASC 250
restatement entry was needed this month** (January's JE-2501-PC01 correction
stands as closed and disclosed in `month_01/open_items.md`).

## 1. NEW contract C-029 — Saltline Hospitality, $21,600.00 annual, billed upfront

- Order form (`documents/month_06/order_form_C-029.md`, signed electronically
  2025-06-01): annual subscription, **12-month term from service start
  2025-06-01**, auto-renewing, $21,600.00 billed in advance (INV-2349),
  payment due on signature. Governed by MSA v3.2. Wire received 06/15
  (`cash_receipts.csv`, bank `WIRE IN SALTLINE HOSPITALITY`).
- **No new question needed.** As with Quarry (C-028), the term is fully
  documented, so revenue is classifiable and ratable: billed to 2200
  (JE-2506-002), June release $1,800.00 = $21,600.00 ÷ 12 (JE-2506-016,
  policy #1; ASC 606-10-25-27 — same analysis as Quarry). Balance $19,800.00
  covers July 2025 – May 2026, all within 12 months of 06/30/2025 → current.

## 2. OBSERVATION — Harbor Law LLP $2,500.00: second identical occurrence this year

- June `vendor_bills.csv` carries a Harbor Law bill of $2,500.00 dated
  06/09, paid by ACH 06/09. March carried an identical $2,500.00 bill paid
  03/09 (verified against the March statement during the May close).
- We examined duplication risk and cleared it: each bill appears exactly once
  in its own month's documents, each ACH appears exactly once, and no other
  Harbor Law debits exist. The 03/09 → 06/09 cadence is consistent with a
  **quarterly retainer** (expect September). Account 6600 Professional fees
  now stands at $5,000.00 for H1 2025.
- Not an accounting error and not a new question — flagged so the Board is
  aware; if a third identical bill arrives in September without an invoice,
  we will ask.

## 3. Payroll register — sixth consecutive identical month (standing unknown U11)

- Jan = Feb = Mar = Apr = May = Jun: gross $54,404.00, net $48,200.00,
  employer $5,076.00, remitted $11,280.00, 9 employees. Not re-asked per
  protocol. June was clean at the bank: single net-pay debit; register ↔
  books ↔ bank all agree; 2210 clears cumulatively ($67,680.00 in = out).

## 4. Pinecone Dental Group — unchanged (standing unknown U10)

- No new Pinecone documents in June. $36,000.00 remains fully deferred,
  recognized $0.00 for the fifth month running. Not re-asked per protocol.

## 5. Marigold Schools (C-027) and Trestle renewal — routine

- Marigold: released $1,500.00; balance $12,000.00 covering July 2025 –
  February 2026.
- Trestle renewal (C-026): released $2,000.00; balance $12,000.00 covering
  July–December 2025 @ $2,000.00.

## 6. Opening A/R — sixth month uncollected (standing unknown U3)

- $92,650.00 of opening (pre-2025) receivables: **zero** collections applied
  in June; all 24 monthly receipts applied to June invoices, and the Saltline
  wire applied to INV-2349. Aged 17+ months.

## 7. Opening A/P — sixth month unpaid (standing unknown U9)

- $17,420.00 of opening payables: **no** payments in June; all six vendor
  ACHs were June bills (paid in-month), including the Harbor Law bill, which
  is a new June obligation, not part of the opening balance (see item 2).
- Minor recurring-vendor variance, noted not adjusted: AWS $10,520.00 vs May
  $10,400.00; Google Ads $3,500.00 vs May $3,450.00. Both match
  `vendor_bills.csv` 1:1.

## 8. Prepaid expense and depreciation assumptions (U4, U5)

- 1300 Prepaid expense $9,600.00: still no amortization schedule; nothing
  amortized (U4).
- Depreciation $1,777.78 = $64,000.00 ÷ 36 months straight-line per close
  checklist item 6 (U5); 1510 accumulated $31,999.68.

## 9. Deferred revenue classification (account 2200 = $104,800.00)

| Contract | 06/30 balance | Service months remaining | Classification |
|---|---:|---|---|
| Trestle renewal (C-026) | $12,000.00 | Jul–Dec 2025 @ 2,000 | Current |
| Pinecone C-025 | $36,000.00 | Unknown term (U10) | **Not classifiable** (also U6: no non-current contract-liability account exists) |
| Marigold C-027 | $12,000.00 | Jul 2025–Feb 2026 @ 1,500 | Current (within 12 months of 06/30) |
| Quarry C-028 | $25,000.00 | Jul 2025–May 2026 @ 2,500 | Current (within 12 months of 06/30) |
| Saltline C-029 | $19,800.00 | Jul 2025–May 2026 @ 1,800 | Current (within 12 months of 06/30) |
| **Total** | **$104,800.00** | | |

## 10. Standing unknowns carried forward (not re-asked)

U1 (subscription start dates for opening A/R), U2 (equity/AP composition
detail), U3 (opening A/R collectibility — sixth month), U4 (prepaid
schedule), U5 (depreciation life/method), U6 (non-current deferred-revenue
account), U7 (withholding derivation), U8 (root `bank_statement.csv`
Dec-2025 negative balances — still unused, reserved for month 12), U9
(opening A/P aging — sixth month), U10 (Pinecone term), U11 (identical
payroll registers — sixth month). U12 (Gusto recovery) remains closed.
**No new unknowns arose in June; no new questions were raised.**

## Result of the June close

- Revenue $38,250.00 (30,450.00 monthly + 7,800.00 deferred releases);
  expenses $86,677.78 (54,404.00 gross salaries + 5,076.00 employer taxes +
  25,420.00 vendor bills + 1,777.78 depreciation);
  **net loss $(48,427.78)**.
- Cash $227,450.00 = bank statement ending balance, difference $0.00;
  deferred revenue 2200 net $104,800.00 = rollforward closing; trial balance
  in balance (debits = credits = $2,310,169.68).
