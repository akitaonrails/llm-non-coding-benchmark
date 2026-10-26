# Open Items — April 2025 Close

**To:** Board, Northwind Analytics Inc.
**From:** Controller
**Period:** April 2025 (month 4 of 12)

No prior-period errors were identified in April activity, so **no ASC 250
restatement entry was needed this month** (January's JE-2501-PC01 correction
stands as closed and disclosed in `month_01/open_items.md`).

## 1. NEW, MATERIAL — Duplicate Gusto net-pay debit: $48,200.00 out of the bank with no payroll behind it

- **Facts.** The April bank statement shows **two** GUSTO NET PAY ACH debits of
  $48,200.00 (04/25 and 04/26). The payroll register shows **one** April
  payroll (gross $54,404.00, net $48,200.00, 9 employees). The office
  manager's note (`documents/month_04/note_from_office_manager.txt`, Gusto
  ticket **GS-44812** opened 4/27) confirms: *"two net-pay debits hit our
  account, only one payroll was run"* — no resolution yet.
- **Treatment (JE-2504-012).** The cash outflow is real and must be booked for
  the ledger to agree with the bank. It is **not** payroll expense: the
  register evidences exactly one payroll run, and expensing a second would
  overstate April expense by $48,200.00 and break the register-to-book tie we
  have maintained all year. Booked as a recovery claim —
  **Dr 1200 Due from Gusto — duplicate net-pay debit (new account) / Cr 1000**.
- **Judgment call.** The chart of accounts has no vendor-claim/other-receivable
  account; opening 1200 (instead of forcing it into 1100 trade A/R or expensing
  it) is our decision and is flagged here.
- **Recovery is not confirmed (new standing unknown U12).** If Gusto or the
  bank returns the funds, credit 1200. If recovery is refused or lapses, the
  claim must be written off as a loss in a later period — it will **not**
  be quietly buried in payroll.
- **Deadline.** The statement clause ("If no error is reported within 60 days
  the account will be considered correct") runs to approximately **2025-06-25**
  from the 04/26 debit. Keep GS-44812 (and, if needed, a bank ACH recall /
  dispute) alive through that date and retain all correspondence.
- **Effect on the payroll three-way tie.** Register ↔ books ↔ bank holds for
  the single run (net 48,200 on 04/25; tax 11,280 on 04/25). The 04/26 debit
  matches no register item; we isolated it rather than force the tie.

## 2. Payroll register — fourth consecutive identical month (standing unknown U11), now with a hard breach at the bank

- Jan = Feb = Mar = Apr: gross $54,404.00, net $48,200.00, employer $5,076.00,
  remitted $11,280.00, 9 employees. Previously this was a document-quality
  observation only; April's duplicate net-pay debit shows a payment control
  failure reaching cash. The four-month identity plus the duplicate debit
  strengthens the U11 concern materially. Not re-asked per client protocol;
  April instead raises one **new** question (G1) about the GS-44812 recovery,
  which is a new event, not a re-ask of U11.

## 3. Pinecone Dental Group — unchanged (standing unknown U10)

- No new Pinecone documents in April. $36,000.00 remains fully deferred,
  recognized $0.00 for the third month running. Not re-asked per protocol.

## 4. Marigold Schools (C-027) — routine now; Trestle prior contract ends in May

- Marigold: policy #1 release $1,500.00 for April (JE-2504-014); balance
  $15,000.00 covering May 2025 – Feb 2026. No new judgment required.
- Trestle prior contract (ASC 250 corrected balance): released $8,200.00 for
  April; **remaining $8,200.00 = final service month May 2025**, then the line
  closes.
- Trestle renewal: released $2,000.00; balance $16,000.00 covering May–Dec 2025.

## 5. Opening A/R — fourth month uncollected (standing unknown U3)

- $92,650.00 of opening (pre-2025) receivables: **zero** collections applied
  in April; all 24 receipts applied to April invoices. Aged 15+ months.

## 6. Opening A/P — fourth month unpaid (standing unknown U9)

- $17,420.00 of opening payables: **no** payments in April; all vendor ACHs
  were April bills.

## 7. Prepaid expense and depreciation assumptions (U4, U5)

- 1300 Prepaid expense $9,600.00: still no amortization schedule; nothing
  amortized (U4).
- Depreciation $1,777.78 = $64,000.00 ÷ 36 months straight-line per close
  checklist item 6 (U5); 1510 accumulated $28,444.12.

## 8. Deferred revenue classification (account 2200 = $75,200.00)

| Contract | 04/30 balance | Service months remaining | Classification |
|---|---:|---|---|
| Trestle prior contract (C-026, corrected) | $8,200.00 | May 2025 (final) | Current |
| Trestle renewal (C-026) | $16,000.00 | May–Dec 2025 @ 2,000 | Current |
| Marigold C-027 | $15,000.00 | May 2025–Feb 2026 @ 1,500 | Current (within 12 months of 04/30) |
| Pinecone C-025 | $36,000.00 | Unknown term (U10) | **Not classifiable** (also U6: no non-current contract-liability account exists) |

## 9. Standing unknowns carried forward (not re-asked)

U1 (subscription start dates for opening A/R), U2 (equity/AP composition
detail), U3 (opening A/R collectibility), U4 (prepaid schedule), U5
(depreciation life/method), U6 (non-current deferred-revenue account), U7
(withholding derivation), U8 (root `bank_statement.csv` Dec-2025 negative
balances), U9 (opening A/P aging), U10 (Pinecone term), U11 (identical
payroll registers — **strengthened this month**), and **new U12** (recovery of
the duplicate $48,200.00 net-pay debit, GS-44812).

## Result of the April close

- Revenue $42,150.00 (30,450.00 monthly + 11,700.00 releases); expenses
  $83,837.78; **net loss $(41,687.78)**. The duplicate debit does **not**
  appear in expenses.
- Cash $233,880.00 = bank; 1200 claim $48,200.00; deferred revenue 2200 net
  $75,200.00 = rollforward closing; trial balance in balance (debits =
  credits = $1,773,554.12).
