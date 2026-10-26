# Open Items — May 2025 Close

**To:** Board, Northwind Analytics Inc.
**From:** Controller
**Period:** May 2025 (month 5 of 12)

No prior-period errors were identified in May activity, so **no ASC 250
restatement entry was needed this month** (January's JE-2501-PC01 correction
stands as closed and disclosed in `month_01/open_items.md`).

## 1. CLOSED — Gusto duplicate net-pay debit recovered: $48,200.00 returned and verified in cash

- **Facts.** The May bank statement shows `ACH CREDIT GUSTO REFUND $48,200.00`
  on **05/09** (`documents/month_05/bank_statement.pdf`), matching the April
  04/26 duplicate debit exactly. The office manager's ticket **GS-44812**
  (`documents/month_04/note_from_office_manager.txt`) is thereby satisfied.
- **Treatment (JE-2505-005).** Dr 1000 / Cr 1200 Due from Gusto, $48,200.00.
  Account 1200 now nets to **$0.00** (debit $48,200.00 from April, credited in
  May). April's books stand unchanged — no restatement; recovery was booked in
  the period the cash arrived.
- **Standing unknown U12 / question G1: resolved by evidence, no client answer
  needed.** The refund arrived well inside the statement's 60-day window
  (≈2025-06-25), so no bank ACH recall remains necessary. Retain the GS-44812
  correspondence in the file.
- **The April duplicate-debit pattern did not recur:** the May statement shows
  exactly one GUSTO NET PAY debit (05/25), tied to the one May payroll.
  Recommend the Board still ask Gusto for the root cause under GS-44812 so the
  control failure is closed out, but no accounting item remains open.

## 2. Payroll register — fifth consecutive identical month (standing unknown U11)

- Jan = Feb = Mar = Apr = May: gross $54,404.00, net $48,200.00, employer
  $5,076.00, remitted $11,280.00, 9 employees. Not re-asked per protocol.
  May was clean at the bank (single net-pay debit; register ↔ books ↔ bank all
  agree), so unlike April the U11 observation carries no cash consequence this
  month.

## 3. NEW contract C-028 — Quarry Analytics Co, $30,000.00 annual, billed upfront

- Order form (`documents/month_05/order_form_C-028.md`, signed 2025-05-01):
  annual subscription, **12-month term, service start 2025-05-01**, $30,000.00
  billed in advance (INV-2324). Wire received 05/15 (`cash_receipts.csv`,
  bank `WIRE IN QUARRY ANALYTICS CO`).
- **No new question needed.** Unlike Pinecone (U10), the term is fully
  documented, so revenue is classifiable and ratable: billed to 2200
  (JE-2505-002), May release $2,500.00 = $30,000.00 ÷ 12 (JE-2505-016,
  policy #1; ASC 606-10-25-27). Balance $27,500.00 covers June 2025 – April 2026.

## 4. Trestle prior contract line CLOSED (ASC 250-corrected balance fully released)

- Final service month May 2025: released the remaining $8,200.00 (JE-2505-016).
  The line's cumulative balance is $0.00 and drops out of the rollforward from
  June forward. The January correction is fully worked off.

## 5. Pinecone Dental Group — unchanged (standing unknown U10)

- No new Pinecone documents in May. $36,000.00 remains fully deferred,
  recognized $0.00 for the fourth month running. Not re-asked per protocol.

## 6. Marigold Schools (C-027) and Trestle renewal — routine

- Marigold: released $1,500.00; balance $13,500.00 covering June 2025 – March
  2026.
- Trestle renewal (C-026): released $2,000.00; balance $14,000.00 covering
  June–December 2025 @ $2,000.00.

## 7. Opening A/R — fifth month uncollected (standing unknown U3)

- $92,650.00 of opening (pre-2025) receivables: **zero** collections applied
  in May; all 24 monthly receipts applied to May invoices, and the Quarry wire
  applied to INV-2324. Aged 16+ months.

## 8. Opening A/P — fifth month unpaid (standing unknown U9)

- $17,420.00 of opening payables: **no** payments in May; all five vendor ACHs
  were May bills (paid in-month). No Harbor Law ACH appeared in May; the March
  Harbor Law invoice ($2,500.00) was verified as paid in March on the March
  statement, so it is not part of the $17,420.00.
- Minor recurring-vendor variance, noted not adjusted: AWS $10,400.00 vs April
  $10,280.00; Google Ads $3,450.00 vs April $3,400.00. Both match
  `vendor_bills.csv` 1:1.

## 9. Prepaid expense and depreciation assumptions (U4, U5)

- 1300 Prepaid expense $9,600.00: still no amortization schedule; nothing
  amortized (U4).
- Depreciation $1,777.78 = $64,000.00 ÷ 36 months straight-line per close
  checklist item 6 (U5); 1510 accumulated $30,221.90.

## 10. Deferred revenue classification (account 2200 = $91,000.00)

| Contract | 05/31 balance | Service months remaining | Classification |
|---|---:|---|---|
| Trestle renewal (C-026) | $14,000.00 | Jun–Dec 2025 @ 2,000 | Current |
| Pinecone C-025 | $36,000.00 | Unknown term (U10) | **Not classifiable** (also U6: no non-current contract-liability account exists) |
| Marigold C-027 | $13,500.00 | Jun 2025–Mar 2026 @ 1,500 | Current (within 12 months of 05/31) |
| Quarry C-028 | $27,500.00 | Jun 2025–Apr 2026 @ 2,500 | Current (within 12 months of 05/31) |
| **Total** | **$91,000.00** | | |

## 11. Standing unknowns carried forward (not re-asked)

U1 (subscription start dates for opening A/R), U2 (equity/AP composition
detail), U3 (opening A/R collectibility — fifth month), U4 (prepaid schedule),
U5 (depreciation life/method), U6 (non-current deferred-revenue account), U7
(withholding derivation), U8 (root `bank_statement.csv` Dec-2025 negative
balances — still unused, reserved for month 12), U9 (opening A/P aging — fifth
month), U10 (Pinecone term), U11 (identical payroll registers — fifth month).
**U12 (Gusto recovery) is resolved and retired** — cash verified 05/09.
No new unknowns arose in May; no new questions were raised.

## Result of the May close

- Revenue $44,650.00 (30,450.00 monthly + 14,200.00 deferred releases);
  expenses $84,007.78 (54,404.00 gross salaries + 5,076.00 employer taxes +
  22,750.00 vendor bills + 1,777.78 depreciation);
  **net loss $(39,357.78)**.
- Cash $260,300.00 = bank statement ending balance, difference $0.00; 1200
  claim $0.00 (closed); deferred revenue 2200 net $91,000.00 = rollforward
  closing; trial balance in balance (debits = credits = $2,074,891.90).
