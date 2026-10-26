# Bank reconciliation — February 2025

**Account:** Pacific Summit Bank, operating account ending 5531 · **Period:** 2025-02-01 to 2025-02-28
**Sources:** `documents/month_02/bank_statement.pdf` (32 transactions), `documents/month_02/cash_receipts.csv`,
`documents/month_02/vendor_bills.csv`, `documents/month_02/payroll_register.json`,
`deliverable/month_02/journal_entries.json`.

## Reconciliation statement

| | Amount |
|---|---:|
| Bank balance per statement, 2025-02-28 | 369,630.00 |
| Cash per books (account 1000, cumulative debits 532,900.00 − credits 163,270.00) | 369,630.00 |
| **Difference** | **0.00** |

Opening agreement: the statement's beginning balance **384,900.00** equals the reconciled 2025-01-31 balance in
`month_01/bank_reconciliation.md` — no lagging or missing items carried through.

Roll: 384,900.00 + 66,450.00 credits − 81,720.00 debits = 369,630.00 (statement header totals agree with the
item detail; every running balance on the statement was recomputed line-by-line with no exception).

## Credits (receipts) — 25 items, 66,450.00, all matched

Every cash receipt appears on the bank **the same day** and was applied against the stated February invoice;
invoice amounts tie 1:1 (`cash_receipts.csv` → `invoices.csv` → bank):

| Bank credit | Amount | Applied | Matches |
|---|---:|---|---|
| 02/15 WIRE IN PINECONE DENTAL GROUP | 36,000.00 | INV-2250 | billed 2025-02-01, "due on signature"; collected in full — **revenue treatment is deferred, see open_items.md item 6; collection ≠ recognition** |
| 02/20 CEDAR LOGISTICS INC | 450.00 | INV-2241 | ✓ same day |
| 02/20 ALDER STUDIOS INC | 900.00 | INV-2243 | ✓ |
| 02/20 KESTREL FOODS CO | 650.00 | INV-2245 | ✓ |
| 02/20 EMBER SYSTEMS INC | 450.00 | INV-2248 | ✓ |
| 02/21 CEDAR LOGISTICS LLC | 1,800.00 | INV-2235 | ✓ |
| 02/21 EMBER FOODS LLC | 1,800.00 | INV-2249 | ✓ |
| 02/22 EMBER HEALTH CO | 2,400.00 | INV-2227 | ✓ |
| 02/22 GRANITE SYSTEMS LLC | 1,800.00 | INV-2229 | ✓ |
| 02/22 CEDAR LABS LLC | 1,800.00 | INV-2234 | ✓ |
| 02/22 ALDER STUDIOS LLC | 1,800.00 | INV-2237 | ✓ |
| 02/23 JUNIPER LOGISTICS LLC | 650.00 | INV-2233 | ✓ |
| 02/23 EMBER CAPITAL INC | 2,400.00 | INV-2236 | ✓ |
| 02/23 EMBER LOGISTICS INC | 450.00 | INV-2238 | ✓ |
| 02/23 HARBOR LOGISTICS LLC | 1,200.00 | INV-2242 | ✓ |
| 02/23 CEDAR STUDIOS INC | 900.00 | INV-2246 | ✓ |
| 02/24 KESTREL SYSTEMS INC | 2,400.00 | INV-2228 | ✓ |
| 02/24 IRIS HEALTH LLC | 900.00 | INV-2230 | ✓ |
| 02/24 BIRCH LABS LLC | 2,400.00 | INV-2231 | ✓ |
| 02/25 DUNE HEALTH CO | 900.00 | INV-2239 | ✓ |
| 02/25 EMBER CAPITAL CO | 2,400.00 | INV-2244 | ✓ |
| 02/25 FJORD HEALTH CO | 450.00 | INV-2247 | ✓ |
| 02/26 BIRCH HEALTH CO | 650.00 | INV-2226 | ✓ |
| 02/26 FJORD STUDIOS INC | 450.00 | INV-2232 | ✓ |
| 02/26 DUNE FOODS CO | 450.00 | INV-2240 | ✓ |
| **Total** | **66,450.00** | | 30,450.00 monthly (24) + 36,000.00 Pinecone |

No unidentified receipts → nothing to account 2300 (policy #4 not triggered). Every February invoice was
collected in full in February; the 92,650.00 opening receivable again received **no** application (open item 3).

## Debits — 7 items, 81,720.00, all matched

| Bank debit | Amount | Matched to | Posted |
|---|---:|---|---|
| 02/05 ACH AWS | 10,040.00 | bill 2025-02-05 | 5000 Hosting |
| 02/06 ACH WEWORK | 7,200.00 | bill 2025-02-06 | 5200 Rent |
| 02/07 ACH GUSTO FEES | 240.00 | bill 2025-02-07 | 5900 G&A other (platform fee, not payroll tax) |
| 02/08 ACH NOTION/SLACK/GITHUB | 1,460.00 | bill 2025-02-08 | 5300 Software |
| 02/09 ACH GOOGLE ADS | 3,300.00 | bill 2025-02-09 | 5400 Marketing |
| 02/25 ACH GUSTO NET PAY | 48,200.00 | register net pay | payroll JE |
| 02/25 ACH GUSTO TAX | 11,280.00 | register taxes_remitted | payroll JE |
| **Total** | **81,720.00** | | |

AWS is 120.00 higher than January (10,040.00 vs 9,920.00) and Google Ads 50.00 higher (3,300.00 vs 3,250.00);
both bills were paid exactly as invoiced, so no cash difference arises — usage variance noted in
`open_items.md` item 7, no accrual or prepaid implication.

## Payroll — register ↔ bank ↔ books (close-checklist item 4)

| Test | Computation | Result |
|---|---|---|
| Withheld from employees | gross 54,404.00 − net 48,200.00 | 6,204.00 |
| Remitted per register | withheld 6,204.00 + employer 5,076.00 | 11,280.00 = register `taxes_remitted` ✓ |
| Bank shows | 02/25 net 48,200.00 and tax 11,280.00 | ✓ both items |
| Cash out vs expense | 48,200.00 + 11,280.00 = 59,480.00 = 54,404.00 + 5,076.00 | ✓ (JE-2025-02-06) |

February register is identical to January (9 employees, same amounts); no variance to explain.

## Conclusion

All 32 statement items are matched to source documents; every bank difference is **0.00**; nothing was forced.
`documents/bank_statement.csv` in the documents root remains the unexplained December-2025-dated file and was
**not** used (open item 8).
