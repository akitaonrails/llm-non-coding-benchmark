# Professional fees — what may be paid to each professional, and when

Status: **final for April**, updated to the actual order. The controlling procedures are **Dkt. 77 (entered
4/14/2026)** in `documents/session2/interim_compensation_order_excerpt.md`, plus `library/bc_330_331.md` and
Dkt. 61 ¶2. The April MOR reports these amounts in Part 5 (`session2/april_mor.json`).

## The rule (Dkt. 77, entered 4/14/2026)

> Retained professionals may serve monthly fee statements; **absent objection within 14 days** the Debtor **may
> pay 80% of fees and 100% of expenses**; the **20% holdback is paid only upon Court approval of an interim or
> final fee application**. **No payment may be made for any period before the professional's retention date**
> (Holland & Pierce retained nunc pro tunc to 3/10; Corbin retained effective 3/20).

The vendor-file note "80%/100% holdback" is resolved: **Reading A confirmed** — 80% of *fees*, 100% of
*expenses*, 20% fee holdback. Reading B in the earlier interim draft is dead.

Framework reminders that still apply under Dkt. 77:

- Dkt. 77 is an **interim procedure under §331**, not a §330 award. The 20% holdback (and everything not yet
  paid) still requires a noticed, court-approved interim or final application; courts can still trim fees
  (`library/bc_330_331.md`).
- Payments outside the order's procedures remain exposed to **disgorgement** (`library/bc_330_331.md`).
- DIP proceeds may fund these payments: Dkt. 61 ¶2 covers post-petition operating expenses, court-ordered
  administrative items, and the Carve-Out; a Dkt. 77-compliant payment is authorized spending, but stay inside
  the DIP budget (headroom after the 4/9 draw: 2,500,000.00 − 1,550,000.00 = **950,000.00**).

## Holland & Pierce LLP (debtor counsel) — March statement $140,000.00 fees + $4,200.00 expenses

Retention: **nunc pro tunc to 3/10/2026** — the whole March period is period-eligible under Dkt. 77.

Statement served 4/15; 14-day objection period ran through **4/29**; the file records **no objection**. So the
Debtor *may* pay, and the arithmetic maximum is:

| Item | Computation | Amount |
|---|---|---|
| Fees payable now (80%) | 0.80 × 140,000.00 | 112,000.00 |
| Expenses payable now (100%) | 1.00 × 4,200.00 | 4,200.00 |
| **Maximum currently payable** | 112,000.00 + 4,200.00 | **116,200.00** |
| Holdback (20% of fees) | 0.20 × 140,000.00 | **28,000.00** — payable only on Court approval of an interim/final application |

Check: 116,200.00 + 28,000.00 = 144,200.00 = the full statement.

**Cash actually paid in April: $0.00.** The April activity file records no fee disbursement; the objection window
closed 4/29, so a payment would most likely land in May. If a payment went out, cap it at **$116,200.00** and
report it in the May MOR Part 1 + Part 5.

## Corbin Advisors (financial advisor) — March statement $45,000.00 (period 3/10–3/31)

Two independent gates, both currently shut:

1. **Objection status unknown.** Served 4/16; the 14-day period ended **4/30**, but the file does not say whether
   an objection was filed. Until that is confirmed, treat as **nothing payable**.
2. **The retention-date trap.** Dkt. 77 bars payment "for any period before the professional's retention date."
   Corbin was retained **effective 3/20**, but the statement starts **3/10**. Unlike H&P, Corbin has **no nunc
   pro tunc** relief in the file. Pro-rata by days (assumption — no day-level detail in the file):

| Segment | Days | Computation | Amount |
|---|---|---|---|
| Eligible (3/20–3/31) | 12 of 22 | 45,000.00 × 12/22 | **24,545.45** |
| Pre-retention (3/10–3/19) | 10 of 22 | 45,000.00 × 10/22 | **20,454.55** — NOT payable under Dkt. 77 |

Check: 24,545.45 + 20,454.55 = 45,000.00.

- Even if Corbin's statement draws no objection, the maximum payable is 80% × 24,545.45 = **$19,636.36**
  (holdback 4,909.09 upon payment; the pre-retention $20,454.55 stays unpaid).
- To reach the pre-retention portion, Corbin needs a **nunc pro tunc retention motion** — counsel's call, with
  the §331/330 record to support it [application mechanics beyond the library excerpt — unverified].
- Paying the $45,000 as served would violate Dkt. 77 and §§330/331 — disgorgement exposure. **Do not pay until
  (a) objection status is confirmed and (b) the period split is documented.**

## April MOR Part 5 as filed (`april_mor.json`)

| Field | Amount | Basis |
|---|---|---|
| professional_fees_approved | 144,200.00 | H&P March statement procedurally approved under Dkt. 77 (no objection by 4/29); **not** a §330 final award |
| paid | 0.00 | No fee disbursement recorded in April |
| holdback | 28,000.00 | 0.20 × 140,000.00 — the amount that **must be withheld** when the H&P payment is made; no cash has moved yet (presentation choice, disclosed in MOR notes) |

Corbin is excluded from Part 5 entirely (both gates above). The full $45,000 stays accrued in Part 2 post-petition
payables, with the pre-retention $20,454.55 flagged as not payable without further court relief.

## Pay-order discipline (this week)

1. H&P: pay **≤ 116,200.00** once the business decides to pay; log it in Part 1 (professional fees) and Part 5
   (paid) in the **May** MOR; holdback 28,000.00 stays off the cash until a fee application is approved.
2. Corbin: **$0.00** until objection status + period allocation are documented; expected ceiling then 19,636.36.
3. Both: interim fee applications should be calendared now — the 20% holdbacks and any pre-retention amounts only
   become money through noticed, approved applications (library/bc_330_331.md).
