# 2025 Form 1040 + NY part-year allocation — Marcus & Elena Reyes (MFJ)

Prepared from the client file in `documents/` using only the closed library (`library/INDEX.md`).
Per the engagement rules, **authority citations** are bracketed `[...]` and point **only** to files in
`library/INDEX.md`. Files in `documents/` are client **source documents** — they supply facts (input
figures) and are identified as "Source: …"; they are never cited as authority.

**Headline:** AGI $91,350 · taxable income $59,850 · total tax $6,408 · withheld $8,730 → **federal refund $2,322**.
(Corrected this round: the 8962 repayment is capped at $1,900, not the full $2,368.74 excess — see §6 step 8.)
Marcus's expectation that the $28,000 S-corp loss "comes straight off" income is **wrong**: only $11,500 is allowed (basis limit), and it also *reduces* the rental-loss allowance (see §469 MAGI interaction).

---

## 1. Filing status and dependents

- MFJ: married couple living together, status determined as of Dec 31. — [`1040_instructions_tax_computation.md`]
- **Sofia Reyes, 15** — our child, under 17 at year end → qualifying child for the CTC. — [`1040_instructions_tax_computation.md`]
- **Leo Castellano, 9 — NOT claimed on this return.** He is Elena's son; the custody order alternates years: *"The Father shall claim the child in odd-numbered tax years; the Mother shall claim the child in even-numbered tax years."* 2025 is odd → the father claims Leo; the custodial mother executes Form 8332. Library rule: "Where a decree or agreement alternates years, the agreement controls which parent claims the child for that year," and a child claimed by the other parent under an 8332 release is **not** our qualifying child for the CTC. — authority [`1040_instructions_tax_computation.md`]; Source: `documents/custody_agreement_excerpt.pdf`
  **Client confirmed (2025-10-25):** Elena signed the Form 8332 for Leo's dad — "it's his year." (Her response used a `{TY}` template placeholder; read as 2025, consistent with the odd-year rule.) Leo is therefore not claimed; CTC is Sofia only.

## 2. Form 7203 — Marcus's S-corp basis (Reyes & Pike Consulting Inc, 40%)

Order per the library: basis is increased by contributions and income, then decreased by distributions, then losses; a guarantee of corporate debt does **not** create debt basis — only a direct shareholder loan does. Marcus never lent the company money (Pike personally guarantees the bank line), so **debt basis = $0**. — authority [`form7203_instructions_excerpt.md`]; Source: `documents/marcus_basis_note.md`

| Year | Beginning | + Contributions | + Income/(loss) | − Distributions | Ending basis |
|---|---:|---:|---:|---:|---:|
| 2021 | 0 | 10,000 | (2,100) | 0 | 7,900 |
| 2022 | 7,900 | 0 | 6,400 | 0 | 14,300 |
| 2023 | 14,300 | 0 | 9,800 | (12,000) | 12,100 |
| 2024 | 12,100 | 0 | 4,600 | (5,200) | **11,500** |

2025 (Source: `documents/k1_1120s_reyes_pike.pdf`, line 1 loss $(28,000), line 16 distributions $0):

- Stock basis beginning 2025 (line 1): **$11,500**; debt basis: $0.
- Loss allowed (line 11) = lesser of loss and basis = min(28,000, 11,500) = **$11,500**.
- Suspended/carryforward = 28,000 − 11,500 = **$16,500** (carried forward indefinitely until basis is restored).
- Ending basis: 11,500 − 11,500 = $0.

Prior-year basis comes only from Marcus's own note (no prior Forms 7203 in the file) — flagged in `judgment_calls.md` #1. **Client confirmed (2025-10-25):** no capital contributions since 2021, never a shareholder loan, and Pike personally guarantees the bank line — matching the note; no prior K-1s/7203s exist, so the note remains the sole evidence.

## 3. Brooklyn rental — Schedule E and Form 8582

Net loss from source document `documents/rental_summary_brooklyn.md`:

- Rent received: 12 × $1,500 = $18,000
- Expenses: 29,200 (mortgage interest 11,900 + common charges 7,860 + property tax 5,140 + repairs 2,350 + insurance 1,150 + mgmt/legal 800) + depreciation 9,818 (270,000 ÷ 27.5) = **$39,018**
- **Rental loss = 18,000 − 39,018 = −$21,018**

Below-market rent ($1,500 vs ~$2,600 market): the library says renting below market to an **unrelated** tenant because rent was never raised "does not by itself trigger" the §280A(d)(2)(C) personal-use rule "if the rent is a fair rental for that lease." Facts fit that carve-out exactly (6-year lease, unrelated tenant, never raised), so the unit is treated as rental property and a loss is possible. See `judgment_calls.md` #4. — [`form8582_instructions_excerpt.md`]
  **Client confirmed (2025-10-25):** the tenant is a stranger — a nurse found through a broker in 2019 — and "we just never raised the rent." The carve-out's factual predicates (unrelated tenant, rent never raised) are confirmed. Residual caveat: the written lease was never produced, so "$1,500 is a fair rent for that lease" rests on the client's account, not a document (STATUS.md).

Active participation: Elena "handles everything herself (approves tenants, arranges repairs)" → active participation, so the $25,000 special allowance is available. — [`form8582_instructions_excerpt.md`]

**MAGI for §469(i)** = AGI figured **without** the passive rental loss, but **reduced by** the nonpassive S-corp loss allowed this year (K-1 Part II G: "Shareholder materially participates: Yes" → the allowed loss is nonpassive and "does reduce MAGI"):

- MAGI = wages 122,000 + interest 400 − allowed S-corp loss 11,500 = **$110,900**

**Special allowance** = 25,000 − 50% × (MAGI − 100,000) = 25,000 − 0.5 × 10,900 = 25,000 − 5,450 = **$19,550** (allowance is zero only at MAGI ≥ 150,000).

- Rental loss allowed = min(21,018, 19,550) = **$19,550**
- Carryforward (Part VII) = 21,018 − 19,550 = **$1,468**

Note the interaction: the allowed S-corp loss lowered MAGI, which *increased* the allowance (had the S-corp loss been fully disallowed for basis, MAGI would be 122,400, allowance 13,800). It still does not let the whole rental loss through.

## 4. Form 1040 — income, deduction, tax

| Line | Item | Amount | Arithmetic / authority |
|---|---|---:|---|
| 1a | Wages | 122,000 | Marcus 68,000 + Elena 54,000 (Source: `documents/w2_marcus_reyes_pike.pdf`, `documents/w2_elena_reyes.pdf`) |
| 2b | Interest | 400 | Chase 1099-INT, recipient Elena (Source: `documents/1099int_chase.pdf`) |
| 8 | Additional income from Schedule 1 (Sch E + K-1) | **−31,050** | −(S-corp loss allowed 11,500 + rental loss allowed after 8582 19,550) |
| 9/11 | Total income = AGI (no above-the-line adjustments) | **91,350** | 122,000 + 400 − 31,050 |
| 12 | Standard deduction, MFJ 2025 | 31,500 | [`1040_instructions_tax_computation.md`]. Itemized alternative ≈ 16,480 (Tampa mortgage interest 6,480 — Source: `documents/1098_mortgage.pdf` — + SALT capped at 10,000: 5,140 property tax + 6,752 NY withholding) < 31,500 → standard wins. The $10,000 SALT cap *amount* is not in the closed library — unverified context, comparison only; the conclusion is robust even with no cap at all: 6,480 + 11,892 = 18,372 < 31,500. (The Brooklyn mortgage interest is on Schedule E, not Schedule A.) |
| 15 | Taxable income | **59,850** | 91,350 − 31,500 |
| 16 | Tax | **6,708** | TI < $100,000 → **must** use the Tax Table ([`1040_instructions_tax_computation.md`]). Row "at least 59,850 / but less than 59,900" → **6,708** ([`tax_table_2025_excerpt.md`]). Sanity check with the reference-only rate schedule at the bracket midpoint 59,875: 23,850×10% + (59,875−23,850)×12% = 2,385 + 4,323 = 6,708 ✓ (schedule itself not used). |

## 5. Credits and payments

- **Line 19 Child tax credit = $2,200.** One qualifying child (Sofia; $2,200 per qualifying child under 17). Leo is claimed by his father under the alternating-years order (see §1). Tax before credits (6,708) exceeds the credit, so the full 2,200 is usable. — [`1040_instructions_tax_computation.md`]
- **Line 17 (Sch 2) excess advance PTC = $1,900** (Form 8962 line 29: excess $2,368.74 limited by the repayment cap — see §6 step 8).

| Line | Item | Amount |
|---|---|---:|
| 24 | Total tax = 6,708 (tax) + 1,900 (excess APTC, capped) − 2,200 (CTC) | **6,408** |
| 25d | Federal withholding = 5,120 (Marcus W-2) + 3,610 (Elena W-2) | **8,730** |
| 34 | Refund = 8,730 − 6,408 | **2,322** |

No other Schedule 2/3 items in the file (no self-employment, no AMT indicators).

## 6. Form 8962 — Premium Tax Credit reconciliation (1095-A: NY of Health, policy NYSH-77120-RE, covered months **Jan–Jun**)

The 1095-A shows coverage January–June only: A monthly enrollment premium $1,720 (annual $10,320 = 6 × 1,720), B SLCSP $1,690 (annual $10,140), C advance PTC $1,650 (annual $9,900). July–December the couple had employer coverage (Elena's W-2 box 12 code DD $7,140, "(Jul–Dec employer coverage)"). — Source: `documents/1095a_marketplace.pdf`, `documents/w2_elena_reyes.pdf`

1. **Household income** = MAGI for 8962 = AGI 91,350 (no tax-exempt interest, nontaxable SS, or excluded foreign income) = **$91,350**.
2. **FPL** (2025, family of 4, 48 states) = **$31,200** ([`form8962_instructions_excerpt.md`]; family-size judgment in `judgment_calls.md` #5).
3. **FPL %** = 91,350 ÷ 31,200 = **292.79%** (2.927885).
4. **Applicable figure** (250–300% band: 4.00%→6.00%, linear): 4.00% + (292.7885−250)/50 × 2.00% = 4.00% + 1.7115% = **5.71%** (5.7115%).
5. Contribution = 91,350 × 5.7115% = $5,217.49/yr ÷ 12 = **$434.79/month**.
6. **Monthly PTC** = lesser of A ($1,720) and B − contribution ($1,690 − 434.79 = $1,255.21) = **$1,255.21** × 6 covered months = **annual PTC $7,531.26**.
7. Excess APTC = 9,900.00 − 7,531.26 = **$2,368.74**.
8. **Repayment limitation**: the library's MFJ cap table is <200% FPL → $750; 200%–<300% → **$1,900**; 300%–<400% → $3,150; no cap at ≥400%. Household income is **292.79% FPL**, inside the **200%–<300% band → cap $1,900**. Repayment = min(2,368.74, 1,900) = **$1,900**; **$468.74** of the excess is not repayable. Entered on 1040 line 17 as **1,900**. — [`form8962_instructions_excerpt.md`]
   *(Correction: the first draft used the $3,150 figure, which is the 300–<400% band — wrong band for 292.79% FPL. Fixed this round; lines 17/24/34 changed from 2,369/6,877/1,853 to 1,900/6,408/2,322.)*

**Client confirmed (2025-10-25):** the marketplace plan was dropped July 1 when Elena enrolled on Halvorsen's plan after the move — consistent with the 1095-A (Jan–Jun) and W-2 box 12 DD (Jul–Dec), so **6 covered months** stands.

The repayment is an additional tax, not an AGI adjustment, so it does not loop back into household income.

## 7. New York — IT-203 part-year

- **Resident period: Jan 1 – Jun 30, 2025 = 181 days.** Brooklyn lease ended June 30 and they were physically out of the apartment by then (June 28–30 at Elena's mother's in Queens — still New York — then drove to Tampa; Tampa closing July 3). Alternative end-date July 3 (closing, 184 days) rejected — see `judgment_calls.md` #6. — Source: `documents/email_move_dates.txt`
- Tax rule: a part-year resident owes tax on **all** income in the resident period plus **NY-source** income in the nonresident period. — [`ny_it203_part_year_excerpt.md`]
- **Convenience of the employer:** wages paid by a NY employer to an employee working from an out-of-state home for the *employee's own convenience* are NY source; only days worked out of state for the *employer's necessity* are not. Both employers are NY-based (Reyes & Pike, 1 Liberty Plaza; Halvorsen Media, 230 Park Ave S). The file says Marcus "just works remotely now" and Halvorsen "let me go fully remote" — permissive remote work with no facts showing employer necessity → convenience rule applies July 1–Dec 31.
  **Client confirmed (2025-10-25):** Marcus — the company allowed remote when he asked to move and "didn't need me out of state"; Elena — Halvorsen (NY office per W-2) approved her request; their Tampa office closed years ago. Neither move was an employer necessity, so both worked out of state for their **own convenience** → the convenience-of-the-employer rule applies and 100% of wages stay NY source.
- **marcus_ny_wages = $68,000** (full year: resident-period wages + convenience-rule wages after the move).
- **elena_ny_wages = $54,000** (same analysis).
- Wage allocation ratio is therefore **100%** (181/181 resident-period days × pre-move wages + 100% NY-source post-move wages). Other NY-source items: the Brooklyn rental (real property in NY) and the Reyes & Pike wage/K-1 items (NY business). Note: the library excerpt spells out the sourcing rule only for **wages**; NY-source status of the rental and the pass-through items during the nonresident period rests on general New York sourcing principles **not spelled out in the closed library** — labeled unverified (NY tax is not being computed in any event). Rental income received during the resident period (Jan–Jun) is taxable under the library's resident-period rule regardless of sourcing.
- **NY withholding:** 3,842 + 2,910 = **$6,752**. The library says excess withholding is refunded on IT-203, but **no NY rate schedule or tables are in the closed library**, so the NY tax figure and refund **cannot be computed here** and are left open (STATUS.md). Do not book a NY refund number.

## 8. Reconciliation checks

- 7203: 11,500 allowed + 16,500 suspended = 28,000 = K-1 loss ✓
- 8582: 19,550 allowed + 1,468 carryforward = 21,018 rental loss ✓
- 1040 line 8: −(11,500 + 19,550) = −31,050 ✓; gross income 122,000 + 400 = 122,400; 122,400 − 31,050 = 91,350 AGI ✓
- 8962: 7,531.26 + 2,368.74 = 9,900.00 = APTC ✓; repayment 1,900 + non-repayable 468.74 = 2,368.74 excess ✓
- Payments − total tax = 8,730 − 6,408 = 2,322 refund ✓
- `return.json` sign convention: 1040 figures are signed as entered on the return (line 8 is negative income; 34 = 2,322 is a positive **refund**, not an amount owed); 7203/8582 loss fields are positive loss magnitudes; 8962 amounts are dollars-and-cents. Excess APTC 2,368.74 is capped at 1,900 by the library's 200%–<300% band table, so line 17 = 1,900 (468.74 not repayable).

Everything above reconciles internally. Items left genuinely open (client confirmations, NY tax uncomputable) are in `STATUS.md` / `QUESTIONS.md`.
