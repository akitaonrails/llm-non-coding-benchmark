

March close begins. Let me gather the source documents and re-verify the prior-month deliverables:






March documents are in. Before building entries, let me re-read the February package (structure to mirror + cumulative TB to carry forward) and the library:






All sources are in hand. Now programmatic verification before writing entries — invoice totals, per-customer agreement vs February, receipts↔invoices↔bank multiset, and full running-balance recomputation:





There are 2 parsing artifacts that need to be fixed: my regex was misclassifying deposit amounts as withdrawals (so all the running totals came out wrong), and 2 transactions got dropped at the column break. Also, the per-customer check against February flagged as False — investigation needed. Properly re-parsing now:





Let me inspect the exact raw structure around the wire row:





The wire's amounts rode into the *next* block, which carries 4 amounts and the Cedar description. Generalized merge rule:





All 33 running balances verify; the Gusto "mismatch" is just my loose name matcher hitting three GUSTO lines (fees 240 is present and correct). One check remains false — let me see exactly where deposits diverge from receipts:





The date-format flip was my bug (`d[3:5]`/`d[0:2]` swapped). Amounts already match exactly. Proper comparison:





The TB stores net balances (per Feb convention), but my loop posted gross — contra entries in the same account inflated both sides by 169,450. Netting each account after posting:





All 33 rows verified. Checking Feb's reconciliation format for consistency, then writing March's:





Writing March's bank reconciliation:





Now reading Feb's open items to carry them forward accurately:





Writing March's open items:





Now updating STATUS.md:





March 2025 close is complete. `deliverable/month_03/` now holds all five deliverables, and `STATUS.md` reads **COMPLETE WITH OPEN ITEMS**.

**The numbers (all independently re-verified after writing):**

| | Amount |
|---|---:|
| Revenue (recurring 30,450 + Trestle 8,200 + renewal 2,000 + Marigold 1,500; **C-025 $0**) | 42,150.00 |
| Expenses (opex 24,910 + payroll 59,480 + depreciation 1,777.78) | 86,167.78 |
| **March net loss** | **(44,017.78)** — Q1 YTD (129,543.34) |
| Cumulative TB | 958,886.34 = 958,886.34 ✓ |
| Deferred revenue rollforward | 104,600 + 18,000 − 11,700 = **110,900** = TB 2200 ✓ |
| Bank vs book cash | 333,690 = 333,690, **zero difference** |

**What made March clean:**
- **INV-2275 Marigold** — the first new contract with full documentation (price, service start 2025-03-01, 12-month term), so policy #1 releases exactly 1/12 = 1,500. Booked as deferred at billing, not revenue. The missing "MSA v3.2" is flagged as a stated assumption (treatment doesn't depend on it) — no question re-asked.
- **Bank statement** — all 33 printed running balances recomputed to the penny from 369,630; the pdftotext column-break on the 03/15 wire row was re-merged and documented in the reconciliation; 25 deposits match receipts by name+date+amount (zero in transit); 8 withdrawals = bills 24,910 + net pay 48,200 + tax 11,280.
- **Payroll** — register agrees to bank exactly on both legs.

**Open items (11, all carried or disclosed, no ASC 250 corrections):** opening A/R 92,650 now 3 months dead; opening A/P 17,420 3 months unpaid; Trestle overlap (6,000 released to date, exposure ≤ 10,000 through May); C-025 36,000 final-stated-assumption deferral; UNIDENTIFIED 24,000; prepaid 9,600; opening TB oddities; expense-code assignments (new: Harbor Law → 5400).

Ready for April on your go.