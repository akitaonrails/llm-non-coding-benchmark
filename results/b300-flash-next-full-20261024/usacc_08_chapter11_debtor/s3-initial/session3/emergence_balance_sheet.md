# Emergence balance sheet — how the discharged debt and the gain are presented

As of the **effective date, 9/30/2026** (plan confirmed 9/2/2026, Dkt. 214; documents/session3/
confirmation_order_excerpt.md).

Premise (from fresh_start.md, ASC 852-10-45-19): **fresh-start reporting does NOT apply** — old
equity keeps 60% (≥ 50%), so the change-of-control condition fails. Consequences drive everything
below: assets stay at carrying amounts (the 14,000,000.00 reorganization value is a test/plan figure,
never pushed onto the balance sheet), retained earnings are not reset, compromised liabilities go to
**present value of amounts to be paid**, and the **gain on discharge is a reorganization item in the
income statement** (library/asc852_fresh_start.md).

## 1. Remove the discharged claim, recognize the plan obligation at present value

- Pre-emergence: the GUC claim sits in **liabilities subject to compromise** at its 8,400,000.00
  allowed amount, reported separately from post-petition liabilities (ASC 852-10-45-4 to 45-6).
- Effective date 9/30/2026: remove the full 8,400,000.00 from LSTC and record the surviving plan
  obligation at the **PV of the 2,940,000.00 cash stream payable over 24 months** (8,400,000.00 ×
  0.35 = 2,940,000.00), per Dkt. 214.
- **First installment is paid in cash on the effective date (Dkt. 214).** The emergence-date balance
  sheet therefore shows the obligation **after** that payment. Installment sizes are not stated in
  the order — only "over 24 months, first installment on the effective date." IF the stream were
  level monthly: 2,940,000.00 ÷ 24 = 122,500.00 per installment; obligation carried at emergence =
  2,940,000.00 − 122,500.00 = **2,817,500.00 undiscounted (PV TBD, ≤ this amount)**.
  - **Discount rate is not in the client file — open item.** Pending the rate, present undiscounted.
    Current/noncurrent split ONLY under the level-monthly assumption: 12 of the remaining 23
    installments fall in the 12 months after emergence → 12 × 122,500.00 = 1,470,000.00 current,
    11 × 122,500.00 = 1,347,500.00 noncurrent (sums to 2,817,500.00). Do not book this split until
    the plan's actual payment terms and an interest rate are provided (QUESTIONS.md).

## 2. The gain — a reorganization item, not equity

- Gain = carrying amount removed − liability recognized = 8,400,000.00 − PV(2,940,000.00), recognized
  on plan consummation, 9/30/2026. Undiscounted proxy: **5,460,000.00**; it shrinks as the PV discount
  is applied (each dollar of discount is a dollar less gain). The effective-date first installment does
  not change the gain — it is a cash payment of the retained obligation, not a discharge.
- Reported **as a reorganization item in the income statement** for the pre-emergence period (through
  9/30/2026) — not an extraordinary item, and NOT credited directly to additional paid-in capital (that
  treatment belongs to fresh-start, which is unavailable). The gain rolls through the income statement
  into the accumulated deficit; no reset occurs.
- Tax presentation: gain carries **no current tax** (excluded from gross income, IRC § 108(a)(1)(A));
  deferred-tax attributes reflect the § 108(b) NOL reduction 6,100,000.00 → 640,000.00
  (cod_schedule.json).

## 3. Remainder of the balance sheet at emergence

- **DIP facility:** repaid in full at emergence (confirmed plan) — DIP financing liability is
  extinguished; exit financing appears at drawn amount (terms not in the client file — open item).
- **Other claims:** of the 16,200,000.00 effective-date claims/post-petition liabilities (figure
  restated in Dkt. 214), 16,200,000.00 − 8,400,000.00 = 7,800,000.00 are assumed paid in full in cash
  per plan (assumption — composition not itemized in file; QUESTIONS.md).
- **Effective-date cash movements:** cash out at emergence = first GUC installment (122,500.00 only
  under the level-monthly assumption) + the 7,800,000.00 assumed full-payment claims + DIP repayment,
  funded by the exit financing. Post-emergence cash is **not computable from the client file** — the
  reorganized company's opening cash depends on exit-financing proceeds and operating cash, which are
  not provided. Nothing below is forced to balance.
- **Equity:** no push-down, so pre-petition capital accounts continue, increased by the reorganization
  gain. The 40% of shares issued to the DIP lender "in satisfaction of fees and as new money" is
  recorded when issued: the fee-satisfaction portion reduces the DIP fee obligation and the new-money
  portion adds cash — the **split of the 40% between fees and new money is not stated in the file**
  and additional paid-in capital cannot be split until it is (QUESTIONS.md; DIP order fee terms —
  the DIP order excerpt does not state them).
- **Mesa coil receivable (~11,000.00)** stays an estate asset, billed and collected separately;
  pre-petition liabilities are not netted against post-petition assets (ASC 852-10-45-9).

## Illustration at 9/30/2026 (undiscounted; TBDs left open, nothing forced to balance)

| | Amount |
|---|---:|
| **Liabilities subject to compromise** | — (eliminated at emergence 9/30/2026) |
| GUC plan obligation after effective-date first installment | ≤ 2,817,500.00 undiscounted (PV TBD; 2,817,500.00 assumes level monthly 122,500.00 × 23 remaining) |
| Exit financing | TBD (terms not in file) |
| Other claims (assumed paid in full) | 0 after payment / 7,800,000.00 before |
| **Income statement (pre-emergence period, through 9/30/2026)** | |
| Gain on discharge of indebtedness — reorganization item | 5,460,000.00 undiscounted, reduced by PV discount |
| **Equity** | |
| Carryover capital accounts + accumulated deficit | carryover (no reset) |
| + reorganization gain | +5,460,000.00 ± PV adjustment |
| + APIC from DIP fee satisfaction and new money | TBD (split unknown) |
