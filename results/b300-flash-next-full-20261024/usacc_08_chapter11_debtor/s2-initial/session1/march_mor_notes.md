# March 2026 MOR — workpaper (arithmetic and assumptions)

Supports `march_mor.json`. Petition date **3/10/2026**. MOR on UST Form 11-MOR (library/ust_mor_instructions.md), due the 21st of each month (Dkt. 61 ¶ 4), so the March report is filed in April. All statutory citations from library/ only; docket references are the Court's orders in documents/.

## Part 1 — Receipts and disbursements (all estate accounts)

**Receipts**

| Item | Amount |
|---|---:|
| Customer collections 3/10–3/31 (on pre-petition receivables; use permitted by cash collateral order Dkt. 22) | 1,212,400.00 |
| DIP draws (money borrowed): 3/12 $600,000 + 3/26 $450,000 | 1,050,000.00 |
| **Total receipts** | **2,262,400.00** |

The 3/10 sweep of the pre-petition bank balance into the new DIP account is a transfer between estate accounts — not a receipt.

**Disbursements**

| Category | Amount | Authority |
|---|---:|---|
| Payroll 3/13 (gross) | 412,000.00 | Pre-petition portion (est. 10/14 × 412,000 = **294,285.71**) authorized by wage order Dkt. 9 within §507(a)(4) $17,150/employee cap (library/bc_507a4_wages.md); post portion (4/14 × 412,000 = **117,714.29**) is §503(b)(1) admin / ordinary course |
| Post-petition vendor invoices paid: Grainger 3/15 $2,120 + Apex 3/22 $9,800 + Front Range 3/28 $7,650 | 19,570.00 | §503(b)(1), §363(c)(1) (library/bc_362_363_503_549.md) |
| Apex pre-petition invoice paid 3/24 | 31,200.00 | Critical vendor order Dkt. 48 (Apex $31,200 ≤ $35,000 cap) — authorized under §549(a) |
| Utilities deposit | 28,000.00 | Dkt. 31 |
| **Total disbursements** | **490,770.00** | 412,000 + 19,570 + 31,200 + 28,000 |

**Ending cash = beginning cash + receipts − disbursements = ? + 2,262,400.00 − 490,770.00 = ? + 1,771,630.00**

⚠️ **OPEN ITEM / ASSUMPTION (stated prominently):** the amount of the pre-petition bank balance swept into the DIP account on 3/10 was not provided in the client file. `march_mor.json` reports **ending_cash = 1,771,630.00**, which **assumes beginning estate cash of $0**. True ending cash = 1,771,630.00 **+ swept balance**. Question logged in QUESTIONS.md. Not forced to balance.

## Part 2 — Post-petition payables / pre-petition liabilities subject to compromise (at 3/31)

**Post-petition payables (aging), open at 3/31:**

| Item | Amount |
|---|---:|
| Mesa Steel post-petition invoice 3/18 (unpaid) | 18,900.00 |
| Holland & Pierce fees invoiced 3/31 (no order yet; Part 5 holdback) | 140,000.00 |
| Corbin Advisors fees invoiced 3/31 (no order yet; Part 5 holdback) | 45,000.00 |
| UST quarterly fee accrual — **estimate** per client file: 0.8% × 490,770.00 disbursements | 3,926.16 |
| **Total** | **207,826.16** |

Paid post-petition invoices (Apex 9,800; Front Range 7,650; Grainger 2,120) are excluded. Possible other March accruals (utilities usage, rent) not in the file — see QUESTIONS.

**Pre-petition liabilities subject to compromise, open at 3/31:**

| Item | Amount |
|---|---:|
| Mesa Steel 2/02 invoice | 62,400.00 |
| Front Range Electric 3/05 invoice | 7,400.00 |
| Grainger 2/11 invoice | 4,310.00 |
| **Total** | **74,110.00** |

Excluded because already paid under court order: Apex 31,200 (Dkt. 48) and the estimated pre-petition wage slice (Dkt. 9). ⚠️ **Assumption:** this figure covers only pre-petition vendor invoices identified in the March file; the full pre-petition AP/claims register was not provided (the plan term sheet later shows allowed GUC of $8.4M, so the register is larger). See QUESTIONS. UST accrual is post-petition (Part 6 item), not LSTC.

## Part 5 — Professional fees (March period)

Approved **$0**; paid **$0**; holdback **$185,000.00** = Holland & Pierce $140,000 + Corbin $45,000 (both invoiced 3/31, fee applications required per §§330(a)/331, library/bc_330_331.md; the H&P interim comp order was not entered until 4/14 — after this reporting period). Treated as "held back" (requested, unpaid). 80% of H&P ($112,000) becomes potentially payable only under the 4/14 interim order — an April event.

## Part 7 — Questionnaire

- Payments on pre-petition debt: **YES** — Apex $31,200 on 3/24 per **Dkt. 48**; pre-petition wages in the 3/13 payroll per **Dkt. 9**. (UST instructions require the docket refs — included in the JSON.)
- Payments outside ordinary course without court approval: **NO** — every payment above was either ordinary-course post-petition (§363(c)(1), §503(b)(1)) or court-authorized (Dkt. 9, 31, 48). Mesa Feb invoice **not** paid despite the CFO request (see response_to_cfo.md).

## Checks

- Post-petition invoices total 223,470.00 (18,900+9,800+7,650+2,120+140,000+45,000); paid 19,570.00; open 203,900.00 = 207,826.16 − 3,926.16 UST accrual ✓
- Pre-petition invoices total 105,310.00 (62,400+31,200+7,400+4,310); paid 31,200.00 (Dkt. 48); open 74,110.00 ✓
- Wage split: 2/28–3/13 = 14 days; pre 2/28–3/9 = 10 days; 412,000 × 10/14 = 294,285.71; × 4/14 = 117,714.29; sums to 412,000 ✓

## Client-confirmed item — Mesa coil receivable (answered after first draft)

Client confirms Mesa owes **~$11,000** for coils returned **January 2026** (pre-petition) and proposed netting it against the Feb invoice. Netting remains prohibited (Dkt. 61 ¶ 3; §549(a); see response_to_cfo.md § 2 and supplement). Accounting effect: an estate receivable from Mesa Steel of ~$11,000 should sit in Part 2 asset status (customer/other receivables) and be billed and collected separately; it does **not** reduce the $62,400 pre-petition LSTC figure and it is not netted for reporting purposes (ASC 852-10-45-9, library/asc852_fresh_start.md). Amount stated as "about" — exact figure to be confirmed from the credit memo; flagged open.

## Explicitly flagged unknowns (client has no further information — left open, not forced)

1. Swept pre-petition cash balance → ending_cash 1,771,630.00 assumes $0 beginning; understated by the swept amount.
2. Full pre-petition AP / claims register → Part 2 LSTC reflects only the four known invoices less Apex (74,110.00). Plan term sheet's allowed GUC of $8.4M confirms the register is materially larger.
3. Per-employee payroll detail → 10/14–4/14 wage split is a time-proration estimate.
4. UST accrual is the client file's 0.8% estimate.
5. Exact coil-credit amount ("about $11,000"); no Dkt. 48 writing from Mesa on Customary Trade Terms is in the file.
6. Other 3/31 accruals (March utilities usage, rent, DIP interest/reserves, payroll taxes on the 3/13 gross) — none provided; Part 2 payables may be understated.
