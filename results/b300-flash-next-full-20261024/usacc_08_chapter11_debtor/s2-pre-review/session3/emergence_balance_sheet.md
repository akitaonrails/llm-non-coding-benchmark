# Emergence balance sheet — how the discharged debt and the gain are presented

Premise (from fresh_start.md, ASC 852-10-45-19): **fresh-start reporting does NOT apply** — old
equity keeps 60% (≥ 50%), so the change-of-control condition fails. Consequences drive everything
below: assets stay at carrying amounts (the 14,000,000.00 reorganization value is a test/plan figure,
never pushed onto the balance sheet), retained earnings are not reset, compromised liabilities go to
**present value of amounts to be paid**, and the **gain on discharge is a reorganization item in the
income statement** (library/asc852_fresh_start.md).

## 1. Remove the discharged claim, recognize the plan obligation at present value

- Pre-emergence: the GUC claim sits in **liabilities subject to compromise** at its 8,400,000.00
  allowed amount, reported separately from post-petition liabilities (ASC 852-10-45-4 to 45-6).
- Effective date: remove the full 8,400,000.00 from LSTC and record the surviving plan obligation at
  the **PV of the 2,940,000.00 cash stream payable over 24 months** (8,400,000.00 × 0.35 =
  2,940,000.00).
  - **Discount rate is not in the client file — open item.** Pending the rate, present undiscounted:
    current portion = payments due within 12 months after emergence; noncurrent = remainder (payment
    schedule not in file; 2,940,000.00 ÷ 24 months × 12 = 1,470,000.00 current / 1,470,000.00
    noncurrent ONLY if the plan pays level monthly — confirm terms, QUESTIONS.md).

## 2. The gain — a reorganization item, not equity

- Gain = carrying amount removed − liability recognized = 8,400,000.00 − PV(2,940,000.00).
  Undiscounted proxy: **5,460,000.00**; it shrinks as the PV discount is applied (each dollar of
  discount is a dollar less gain).
- Reported **as a reorganization item in the income statement** for the pre-emergence period — not an
  extraordinary item, and NOT credited directly to additional paid-in capital (that treatment belongs
  to fresh-start, which is unavailable). The gain rolls through the income statement into the
  accumulated deficit; no reset occurs.
- Tax presentation: gain carries **no current tax** (excluded from gross income, IRC § 108(a)(1)(A));
  deferred-tax attributes reflect the § 108(b) NOL reduction 6,100,000.00 → 640,000.00
  (cod_schedule.json).

## 3. Remainder of the balance sheet at emergence

- **DIP facility:** repaid in full at emergence (plan_term_sheet.md) — DIP financing liability is
  extinguished; exit financing appears at drawn amount (terms not in the client file — open item).
- **Other claims:** of the 16,200,000.00 effective-date claims/post-petition liabilities,
  16,200,000.00 − 8,400,000.00 = 7,800,000.00 are assumed paid in full in cash per plan (assumption —
  composition not itemized in file; QUESTIONS.md).
- **Equity:** no push-down, so pre-petition capital accounts continue, increased by the reorganization
  gain. The 40% of shares issued to the DIP lender "in satisfaction of fees and as new money" is
  recorded when issued: the fee-satisfaction portion reduces the DIP fee obligation and the new-money
  portion adds cash — the **split of the 40% between fees and new money is not stated in the file**
  and additional paid-in capital cannot be split until it is (QUESTIONS.md; DIP order fee terms —
  the DIP order excerpt does not state them).
- **Mesa coil receivable (~11,000.00)** stays an estate asset, billed and collected separately;
  pre-petition liabilities are not netted against post-petition assets (ASC 852-10-45-9).

## Illustration (undiscounted; TBDs left open, nothing forced to balance)

| | Amount |
|---|---:|
| **Liabilities subject to compromise** | — (eliminated at emergence) |
| GUC plan obligation (PV of 2,940,000.00 / 24 mo) | ≤ 2,940,000.00 (PV TBD) |
| Exit financing | TBD (terms not in file) |
| Other claims (assumed paid in full) | 0 after payment / 7,800,000.00 before |
| **Income statement (pre-emergence period)** | |
| Gain on discharge of indebtedness — reorganization item | 5,460,000.00 undiscounted, reduced by PV discount |
| **Equity** | |
| Carryover capital accounts + accumulated deficit | carryover (no reset) |
| + reorganization gain | +5,460,000.00 ± PV adjustment |
| + APIC from DIP fee satisfaction and new money | TBD (split unknown) |
