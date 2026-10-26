# March 2026 MOR workpaper (petition date 3/10/2026) — arithmetic

Every figure in `march_mor.json` comes from here. Source: `documents/petition_month_activity.md`,
`documents/vendor_invoices_march.csv`, `documents/dip_financing_order_excerpt.pdf` (Dkt. 61),
`documents/critical_vendor_order.pdf` (Dkt. 48). Period used: **3/10/2026 – 3/31/2026**.

## Part 1 — cash receipts and disbursements (all estate accounts)

Receipts
| Item | Date | Amount |
|---|---|---|
| Customer collections (all on pre-petition receivables; use permitted by cash-collateral order Dkt. 22) | 3/10–3/31 | 1,212,400.00 |
| DIP draw (Prairie Capital, Dkt. 61 ¶1, authority $2,500,000) | 3/12 | 600,000.00 |
| DIP draw | 3/26 | 450,000.00 |
| **Total receipts** | | **2,262,400.00** |

1,212,400.00 + 600,000.00 + 450,000.00 = **2,262,400.00**

Disbursements
| Category | Amount | Authority |
|---|---|---|
| Payroll 3/13 (gross, covers 2/28–3/13) | 412,000.00 | Dkt. 9 (pre-petition wages up to §507(a)(4) cap) |
| Post-petition vendor invoices: Grainger 3/15 2,120.00 + Apex 3/22 9,800.00 + Front Range 3/28 7,650.00 | 19,570.00 | §§503(b)(1), 363(c)(1) |
| Apex pre-petition invoice paid 3/24 | 31,200.00 | Dkt. 48 ¶1 + Schedule 1 |
| Utilities deposit | 28,000.00 | Dkt. 31 |
| Professional fees | 0.00 | §§330(a), 331 — no award yet |
| **Total disbursements** | **490,770.00** | |

2,120 + 9,800 + 7,650 = 19,570 ✓ (ties to the activity file)
412,000 + 19,570 + 31,200 + 28,000 = **490,770.00**

Cash movement from case activity: 2,262,400.00 − 490,770.00 = **1,771,630.00**

Ending cash = beginning cash (3/10) + 1,771,630.00. **Beginning cash is unknown** — the pre-petition bank balance
swept into the DIP account on 3/10 is not quantified in the file (QUESTIONS Q1), so the `ending_cash` figure in
the JSON is understated by that amount and is not tied to a bank statement.

Not in Part 1 (accrual only): UST quarterly fee 3,926.16 — Part 1 is cash.

## Part 2 — post-petition payables (aging at 3/31/2026)

| Item | Amount |
|---|---|
| Mesa Steel invoice 3/18/2026 (post-petition, unpaid) | 18,900.00 |
| Holland & Pierce LLP invoice 3/31/2026 (accrued; no fee award yet) | 140,000.00 |
| Corbin Advisors invoice 3/31/2026 (accrued; no fee award yet) | 45,000.00 |
| UST quarterly fee accrual | 3,926.16 |
| **Total reported** | **207,826.16** |

18,900 + 140,000 + 45,000 + 3,926.16 = **207,826.16**
UST fee: 490,770.00 × 0.008 = **3,926.16** (client-supplied 0.8% rate; statute not in library → unverified)

Known omissions (unquantified in the file, so the real figure is higher): wages earned 3/14–3/31 unpaid at 3/31;
post-petition sales/use and payroll taxes; DIP interest/fees (no rate given); uninvoiced post-petition goods/services.

## Part 2 — pre-petition liabilities subject to compromise (at 3/31/2026)

Pre-petition vendor invoices in the file: 62,400.00 (Mesa 2/2) + 31,200.00 (Apex 2/20) + 7,400.00 (Front Range 3/5)
+ 4,310.00 (Grainger 2/11) = **105,310.00**
Less Apex paid 3/24 under Dkt. 48: 105,310.00 − 31,200.00 = **74,110.00** reported.

| | |
|---|---|
| Mesa Steel 2/2/2026 | 62,400.00 |
| Front Range Electric 3/5/2026 | 7,400.00 |
| Grainger 2/11/2026 | 4,310.00 |
| **Reported LSTC** | **74,110.00** |
| Plan term sheet allowed GUC pool (later period) | 8,400,000.00 |
| **Unreconciled gap — left open** | **8,325,890.00** |

No schedules or claims register were provided, so 74,110.00 is the documented vendor-invoice subset only. The gap is
not plugged (QUESTIONS Q6).

## Part 5 — professional fees (March)

Approved 0.00 · Paid 0.00 · Holdback 0.00. Nothing granted, nothing paid, and the Holland & Pierce interim
compensation order (80%/100% holdback) was entered **4/14/2026**, outside the March period. Invoiced but not
approved: 140,000.00 + 45,000.00 = 185,000.00 (reported in Part 2, not Part 5).

## Part 7 — questionnaire support

Payments on pre-petition debt: Apex 31,200.00 on 3/24 (Dkt. 48) + the pre-petition share of the 3/13 payroll (Dkt. 9).
Pre-petition wage split is **not** in the books; pro-rata calendar estimate over the 14-day cycle, 2/28–3/9 = 10 days
pre, 3/10–3/13 = 4 days post:
412,000 × 10/14 = **294,285.71** pre-petition (assumption) · 412,000 × 4/14 = **117,714.29** post-petition (assumption).
Cap check cannot be run without headcount: §507(a)(4) cap $17,150/employee → with 100 employees the aggregate cap
would be 100 × 17,150 = 1,715,000, far above the ~294,285.71 estimated pre-petition share, so the cap probably does
not bind — but the file's assertion "no employee exceeded it" is per-employee and needs the payroll register
(QUESTIONS Q2).

Payments outside the ordinary course without approval: none identified. All March payments trace to
Dkt. 9, Dkt. 31, Dkt. 48 or §363(c)(1) ordinary course.

### Client follow-up — the ~$11,000 Mesa coil credit (no netting)

CFO proposed netting Mesa's ~$11,000 credit owed to the estate (January returned coils) against Mesa's $62,400
pre-petition invoice. Refused — see `response_to_cfo.md` §7.

| | |
|---|---|
| Netting = in-kind payment on a pre-petition claim | 11,000 ÷ 62,400 = **17.63%** of the claim, no court order |
| Cash variant the CFO implied | 62,400 − 11,000 = **51,400** paid from DIP funds — still a pre-petition payment |
| Authority | Dkt. 61 ¶3 (bars setoff/recoupment/**netting** by name); §549(a) (avoidable transfer of the estate's receivable); Dkt. 48 excludes Mesa |

Reporting effect (assumes no netting was actually booked — client could not confirm):

- Mesa LSTC stays **gross 62,400.00** → Part 2 LSTC total stays **74,110.00** (unchanged).
- New estate asset: **~11,000.00 pre-petition receivable from Mesa**, kept gross, pursued for collection; not in
  ending cash (uncollected). Need the credit memo — "about $11,000" is an estimate.
- Ledger must not net the credit against the pre-petition payable (or against the post-petition payable without
  approval). Library presentation rule: `library/asc852_fresh_start.md` (LSTC separate; pre-petition liabilities
  not netted against post-petition assets) — note both Mesa items here are pre-petition, so Dkt. 61 ¶3 / §549(a) do
  the work. Setoff rights (11 U.S.C. §§506/558) not in library [unverified].
- Lawful route to the same cash: build application of the documented credit against Mesa's **post-petition**
  invoices into the Mesa critical-vendor motion (notice + hearing).

## Orders / cap math used

| | |
|---|---|
| Dkt. 48 ¶1 aggregate critical-vendor cap | 35,000.00 |
| Apex used (paid 3/24) | 31,200.00 |
| **Remaining headroom** | **3,800.00** — Mesa's 62,400.00 cannot fit, even on an amended order without raising the cap |
| Dkt. 61 authority | 2,500,000.00; drawn 1,050,000.00; available 1,450,000.00 |

Mesa economics (plan term sheet, 35% GUC recovery): 62,400 × 0.35 = **21,840.00** expected plan payment vs.
**62,400.00** to pay in full now → **40,560.00** premium for paying a GUC claim outside the plan.
