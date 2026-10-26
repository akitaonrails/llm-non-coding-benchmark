# March 2026 MOR — preparation notes and arithmetic

Redwood Fabrication, Inc. — Chapter 11, Case No. 26-11842 (D. Colo.). Petition filed **2026-03-10**;
reporting period March 10–31, 2026; UST Form 11-MOR due the 21st of the month (DIP order ¶4).
Authority cited is limited to `library/INDEX.md`; docket items are case facts from `documents/`.

## Part 1 — Cash receipts and disbursements

**Receipts**

| Source | Amount |
|---|---:|
| DIP draw 2026-03-12 | 600,000.00 |
| DIP draw 2026-03-26 | 450,000.00 |
| Customer collections (pre-petition receivables; use permitted by cash collateral order Dkt. 22) | 1,212,400.00 |
| **Total receipts** | **2,262,400.00** |

**Disbursements**

| Line | Amount |
|---|---:|
| Payroll 3/13 (period 2/28–3/13; pre-petition portion authorized by wage motion Dkt. 9 at ≤ §507(a)(4) cap of $17,150/employee, none exceeded — library: bc_507a4_wages.md) | 412,000.00 |
| Post-petition vendor payments (ordinary course, §363(c)(1)): Grainger 3/15 $2,120.00 + Apex 3/22 $9,800.00 + Front Range 3/28 $7,650.00 = 19,570.00 ✓ ties to activity summary | 19,570.00 |
| Apex pre-petition paid 3/24 under critical-vendor order (Dkt. 48; $35,000 cap) | 31,200.00 |
| Utility deposit (Dkt. 31) | 28,000.00 |
| **Total disbursements** | **490,770.00** |

**Ending cash — OPEN ITEM.** The pre-petition bank balance swept into the DIP account on 3/10 is not
in the client file, so ending cash cannot be computed exactly. It equals:

> ending cash = swept opening balance (B₀) + 2,262,400.00 − 490,770.00 = **B₀ + 1,771,630.00**

Reported as `null` in `march_mor.json` rather than guessed; see `QUESTIONS.md` Q1.

**UST quarterly fee accrual (estimate):** 0.8% × 490,770.00 = **3,926.16** (accrued, not disbursed —
therefore not a Part 1 disbursement; carried in Part 2 as a post-petition payable). The correct fee
base may be *all* disbursements in the calendar quarter Jan 1–Mar 31, including pre-petition ones;
the client file says only "0.8% of disbursements (estimate)" — see `QUESTIONS.md` Q2.

## Part 2 — Asset and liability status

**Post-petition payables at 3/31** (unpaid invoices in the register):

| Item | Amount |
|---|---:|
| Mesa Steel — 3/18 invoice (post-petition delivery) | 18,900.00 |
| Holland & Pierce — 3/31 fee invoice (payable only after §§330/331 process — library: bc_330_331.md) | 140,000.00 |
| Corbin Advisors — 3/31 fee invoice (same) | 45,000.00 |
| Subtotal, documented post-petition invoices | 203,900.00 |
| UST quarterly fee accrual (estimate, see above) | 3,926.16 |
| **Part 2 post-petition payables** | **207,826.16** |

Check: all post-petition invoices 223,470.00 − 19,570.00 paid = 203,900.00 ✓.
The professional fee invoices are accrued as post-petition payables but are **not payable until
allowed** (§503(b); §§330/331 — library: bc_330_331.md).

**Pre-petition liabilities subject to compromise** — documented trade payables only:

| Item | Amount |
|---|---:|
| Mesa Steel — 2/2 invoice | 62,400.00 |
| Front Range Electric — 3/5 invoice | 7,400.00 |
| Grainger — 2/11 invoice | 4,310.00 |
| **Documented outstanding pre-petition trade payables** | **74,110.00** |

Apex 2/20 ($31,200.00) is excluded because it was **paid 3/24** under Dkt. 48 (register totals incl.
Apex: 105,310.00 across all four pre-petition invoices). **Caveat:** this figure covers only the
March vendor register; other scheduled pre-petition liabilities (secured debt, leases, taxes,
accrued interest, etc.) were not provided, and the term sheet assumes allowed general unsecured
claims of $8,400,000.00. See `QUESTIONS.md` Q4 before treating 74,110.00 as the complete Part 2
"liabilities subject to compromise" figure.

## Part 5 — Professional fees

No fee application was approved in the reporting period (the interim compensation order was entered
4/14, after period end — per client file), so **approved 0 / paid 0 / holdback 0**. The H&P
($140,000.00) and Corbin ($45,000.00) invoices are accrued post-petition payables awaiting the
§§330/331 process (library: bc_330_331.md). The 80%/100% holdback mechanics will be applied in
Session 2 (April).

## Part 7 — Questionnaire

- *Payments on pre-petition debt:* **Yes** — Apex $31,200.00 (Dkt. 48); pre-petition portion of the
  3/13 payroll (Dkt. 9, within the §507(a)(4) cap — library: bc_507a4_wages.md). A per-employee
  ≥$17,150 test is satisfied per the client file ("no employee exceeded it"); the exact pre-/post-
  petition wage dollar split is not in the file (`QUESTIONS.md` Q6).
- *Payments outside the ordinary course without approval:* **No** — everything disbursed was ordinary
  course (§363(c)(1)) or court-ordered (Dkt. 9, 22, 31, 48). The Mesa February invoice and the
  proposed netting were **not** executed.

## Classification rules used in `segregation.csv`

- Petition date 2026-03-10: invoices dated on/after 3/11 are post-petition, per the register; the
  register's own note field (e.g., "post-petition delivery") is treated as the delivery/accrual fact.
- "payable_now" answers: may the estate lawfully pay this invoice at 3/31 without further Court
  action? Paid invoices are marked with the payment date; pre-petition trade claims answer no until
  an order (Dkt. 48 covers Apex only); professional fees answer no until §§330/331 allowance.
- Pre-petition liabilities are NOT netted against post-petition assets (library:
  asc852_fresh_start.md); the returned-coils claim against Mesa is preserved as a separate estate
  asset, not netted (DIP order ¶3).
