# 2025 Federal Form 1040 (MFJ) + NY Part-Year Allocation — Marcus & Elena Reyes

All citations are to files listed in `library/INDEX.md`. Where a point of law is **not** covered by the
library it is labeled *[unverified]*. Assumptions are flagged inline and collected in `judgment_calls.md`.

Bottom line: **federal refund $2,322.** Marcus's expectation that the $28,000 S-corp loss "comes
straight off" their income is **wrong**: only $11,500 clears the basis limitation and $16,500 is
suspended. And because only $11,500 comes off, his MAGI stays above $100,000, so the rental special
allowance is $19,550 instead of $25,000 — which strands a further **$1,468** of rental loss in
carryforward.

---

## 1. Form 7203 — S corporation stock basis (Reyes & Pike Consulting Inc, EIN 82-4471930)

Authority: `form7203_instructions_excerpt.md` — losses allowed only to the extent of adjusted stock
basis plus debt basis; stock basis increased by contributions and income, decreased by distributions
and losses; suspended losses carry forward indefinitely; **a guarantee of corporate debt does not
create debt basis** — only a direct shareholder loan does.

Marcus never lent the corporation money (`marcus_basis_note.md`); his partner Pike personally
guarantees the bank line — that guarantee gives Marcus **no** debt basis.

Year-by-year basis trace (per the note; 2025 loss per K-1 box 1):

| Year | Begin | + Contribution / income | − Distributions | − Loss allowed | End basis |
|---|---:|---:|---:|---:|---:|
| 2021 | 0 | 10,000 contribution | 0 | 2,100 (that year's K-1 **loss**, per the note — fully allowed within basis) | 7,900 |
| 2022 | 7,900 | +6,400 | 0 | — | 14,300 |
| 2023 | 14,300 | +9,800 | (12,000) | — | 12,100 |
| 2024 | 12,100 | +4,600 | (5,200) | — | 11,500 |
| **2025** | **11,500** | 0 | 0 | **11,500** | **0** |

- 2025 beginning stock basis (Part I line 1): **$11,500**
- 2025 loss per K-1: $(28,000). Allowed = lesser of loss and basis = **$11,500** (line 11).
- Suspended/carryforward (line 12 et seq.) = 28,000 − 11,500 = **$16,500**.

The K-1's gross receipts ($612,400) and Part II ("shareholder materially participates: Yes") mean the
allowed $11,500 is a **nonpassive** Schedule E loss — it is *not* subject to §469. The suspended
$16,500 stays on Form 7203, not Schedule E.

## 2. Form 8582 — Brooklyn rental (318 Dean St #4B)

Authority: `form8582_instructions_excerpt.md` — active participation gives a special allowance up to
$25,000, reduced 50% of MAGI over $100,000, zero at $150,000 (MFJ); MAGI excludes passive losses but
**is reduced by nonpassive losses allowed in the year (e.g., an S-corp loss allowed to the extent of
basis)**; below-market rent to an unrelated tenant that "was never raised" does not by itself trigger
the §280A(d)(2)(C) personal-use rule "if the rent is a fair rental for that lease."

Net rental loss (from `rental_summary_brooklyn.md`; depreciation 270,000 ÷ 27.5 = 9,818.18, used as
the file's 9,818; rented all 12 months):

```
Gross rent                     12 × 1,500 =  18,000.00
Expenses excl. depreciation   (29,200.00)
Depreciation                   ( 9,818.00)
Net rental loss                = (21,018.00)
```

Elena "handles everything herself (approves tenants, arranges repairs)" → active participation
satisfied (that is the standard the library states; no material-participation record exists, which is
fine — the special allowance needs only active participation).

**MAGI for §469(i):**
```
Wages 68,000 + 54,000            122,000
Interest                            400
S-corp loss allowed (nonpassive) (11,500)   ← library: this DOES reduce MAGI
MAGI                            = 110,900
```
(No add-backs apply: no SE tax, IRA, or student-loan items in the file.)

**Special allowance:** 25,000 − 0.50 × (110,900 − 100,000) = 25,000 − 5,450 = **$19,550**
(> 0 because MAGI < 150,000).

**Allowed rental loss** = min(21,018, 19,550) = **$19,550**.
**Part VII carryforward** = 21,018 − 19,550 = **$1,468**.

**Below-market rent:** rent $1,500 vs market ~$2,600, same tenant 6 years, "we never raised it,"
unrelated tenant. Client confirmed: the tenant is a stranger — a nurse found through a broker in 2019 —
and the rent was simply never raised. That is squarely the library's safe sentence ("renting below
market to an unrelated tenant because rent was never raised does not by itself trigger this rule").
Treated as a full rental. Residual unknown: no signed lease in the file to document that $1,500 is a
"fair rental for that lease" — client has no further documents; flagged. Rejected alternative and
risk: see `judgment_calls.md` #4 (if the Service called $1,500 below fair rental for that lease, **all
365 days would be personal-use and the entire $21,018 loss — and all deductions — would be
disallowed**, which would *increase* AGI to $110,900, *increase* tax, and turn the $2,322 refund into
an estimated **balance due of ≈ $1,270** *[estimate uses the reference-only rate schedule and
recomputed 8962; outside the table excerpt — unverified]*).

## 3. Form 1040 — federal figures

W-2s (`w2_marcus_reyes_pike.pdf`, `w2_elena_reyes.pdf`), interest (`1099int_chase.pdf`):

| Line | Figure | Arithmetic |
|---|---:|---|
| 1a wages | **122,000** | 68,000 (Marcus) + 54,000 (Elena) |
| 2b taxable interest | **400** | Chase, Elena |
| 8 additional income from Sch 1 | **(31,050)** | Sch 1 line 5 → Sch E: S-corp (11,500) + rental (19,550) |
| 9 total income | 91,350 | 122,000 + 400 − 31,050 |
| 10 adjustments | 0 | none in file |
| 11 AGI | **91,350** | 91,350 − 0 |
| 12 standard deduction | **31,500** | MFJ 2025 = $31,500 (`1040_instructions_tax_computation.md`) |
| 15 taxable income | **59,850** | 91,350 − 31,500 |
| 16 tax | **6,708** | Tax Table (required under $100,000): row "at least 59,850 / but less than 59,900" → 6,708 (`tax_table_2025_excerpt.md`) |
| 17 Sch 2 line 2 (excess APTC) | **1,900** | Form 8962, §4 below |
| 19 child tax credit | **2,200** | $2,200 per qualifying child under 17 (`1040_instructions_tax_computation.md`); Sofia only, §5 below; tax on line 18 = 8,608 > 2,200 so fully usable |
| 22 / 24 total tax | **6,408** | 6,708 + 1,900 − 2,200 |
| 25d federal withholding | **8,730** | 5,120 (Marcus W-2) + 3,610 (Elena W-2) |
| 34 refund | **2,322** | 8,730 − 6,408 |

Itemizing was not taken: Schedule A items in the file are only Tampa mortgage interest $6,480
(`1098_mortgage.pdf`) plus NY withholding $6,752 (2,910 + 3,842); no Tampa property-tax statement in
the file. Documented itemized deductions ≈ 13,232 < 31,500 standard. (SALT/interest deductibility
rules are not in the library *[unverified]*, but the conclusion — standard deduction — does not hinge
on them.) QBI deduction (§199A) not reported: no positive qualified business income; §199A is not in
the library *[unverified]*.

## 4. Form 8962 — premium tax credit (NY Marketplace policy NYSH-77120-RE)

Authority: `form8962_instructions_excerpt.md` (2025 FPL family of 4 = $31,200; Table 2 bands; PTC
formula; repayment caps MFJ $750 / $1,900 / $3,150, none at ≥400% FPL).

Coverage per `1095a_marketplace.pdf`: months 1–6 only (Marcus, Elena, Sofia, Leo); monthly enrollment
premium 1,720.00, SLCSP 1,690.00, APTC 1,650.00; annuals 10,320 / 10,140 / 9,900.

**Household income** = MAGI = AGI 91,350 + no tax-exempt interest + no nontaxable SS + no excluded
foreign income = **91,350**.

**Family size = 4** (see `judgment_calls.md` #5 — an *assumption*, now confirmed unresolvable: the
client has no Marketplace-application records and no other information. The library supplies only the
family-of-4 FPL ($31,200), and the 1095-A enrolled exactly 4 individuals including Leo. If the correct
size were 3, the 2025 family-of-3 FPL is not in the library *[unverified]* and the income percentage
would rise — direction: a smaller PTC and a repayment up to the 300–400% FPL cap of $3,150 *[the cap
is in the library; the banding for a 3-person family is not computable here]*, reducing the refund by
up to ≈ $1,250.)

```
FPL %:            91,350 ÷ 31,200                       = 292.7885%   (250–300% band)
Applicable figure: 4.00% + 2.00% × (292.7885 − 250)/50  = 5.711538%
Annual contribution: 91,350 × 5.711538% = 5,217.49; monthly = 434.79
Monthly PTC = min( enrollment 1,720.00 , SLCSP 1,690.00 − 434.79 = 1,255.21 ) = 1,255.21
Annual PTC  = 6 × 1,255.21 = 7,531.26      (no PTC for months 7–12 — no Marketplace coverage)
APTC per 1095-A     = 9,900.00
Excess              = 9,900.00 − 7,531.26  = 2,368.74
Repayment cap (MFJ, income 200%–<300% FPL) = 1,900
Repayment (Sch 2 line 2 → 1040 line 17)    = min(2,368.74, 1,900) = 1,900
```

(Rounding note: the chain above carries the FPL ratio unrounded. If FPL % is first rounded to 292.79,
the applicable figure is 5.7116% → excess APTC 2,368.80 — the $1,900 repayment cap binds either way,
so the rounding choice cannot change the result.)

## 5. Dependents and child tax credit

Authority: `1040_instructions_tax_computation.md` (CTC $2,200, under 17, claimed-by-other-parent rule;
alternating-year decree controls). The custody order (`custody_agreement_excerpt.pdf`) and the
client-confirmed Form 8332 are **case-file evidence**, not library authorities.

- **Sofia Reyes, 15** — the couple's child, lives with them → dependent; under 17 at year-end → **CTC
  $2,200**.
- **Leo Castellano, 9** (DOB 03/14/2016) — Elena is the custodial parent ("child resides primarily
  with the Mother"), **but** ¶9 of the custody order: father claims in **odd** years, mother in even
  years → **2025 is the father's year**; Elena **signed Form 8332 for 2025** (client confirmed —
  "it's his year"). The library: "where a decree or agreement alternates years, the agreement
  controls," and a child claimed by the other parent under an 8332 release "is not your qualifying
  child for the credit." → Leo is **not** claimed on this return and generates **no** credit.
  (Some states let a custodial parent reclaim the child when child support is delinquent — that rule
  is not in the library *[unverified]*; client has no information on delinquency, and it is not
  applied.)

## 6. New York part-year (IT-203) allocation

Authority: `ny_it203_part_year_excerpt.md`.

**Resident period.** Brooklyn lease ended June 30 and they were out by then (`email_move_dates.txt`);
NY abode and domicile surrendered that date. Tampa closing/move-in July 3. Resident period =
Jan 1 – Jun 30 = 31+28+31+30+31+30 = **181 days**; nonresident = Jul 1 – Dec 31 = 184 days. (The
Queens nights June 28–30 fall inside the resident period and are immaterial.)

**Wages.** Both W-2s show NY employers (Reyes & Pike — 1 Liberty Plaza, NYC; Halvorsen Media Group —
230 Park Ave S, NYC), NY state wages = full federal wages, and NY withholding all year because
"nobody updated the forms."

- Resident period: all wages are taxed as resident-period income (181 days' worth, allocated by
  workdays 129/261 if the W-2 totals need splitting: Marcus ≈ 33,609, Elena ≈ 26,690).
- Nonresident period: services performed entirely outside NY are not NY source **except** under the
  convenience-of-the-employer rule — wages paid by a NY employer to an employee working from an
  out-of-state home for the employee's own convenience. **Client confirmed both spouses were remote
  for their own convenience:** Marcus asked to move and "they didn't need me out of state" (he is a
  40% owner of the NYC firm); Elena's remote arrangement was her own request, which Halvorsen (an NYC
  employer per both W-2s) approved. → **Convenience rule applies to both; the employer-necessity
  alternative is resolved out** on the client's own statements. No workday log exists (client has no
  additional information), and none is needed for this conclusion.

**NY-source wages for the year: Marcus $68,000, Elena $54,000** (full federal wages).

NY tax/refund is **not computed here**: the library contains no NY rate tables or deductions
*[unverified]* — flagged as an open item. Direction only: their IT-203 NY-source income is nearly all
of their wages plus resident-period share of other income, against NY withholding of $6,752
(3,842 + 2,910), so they should expect a small refund-or-balance-due on IT-203, not the large refund
the all-year NY withholding might suggest.

## 7. Why Marcus's plan failed (client education)

The $28,000 K-1 loss does not "come straight off" income. (1) His stock basis is only $11,500 — the
2023–2024 distributions ($12,000 + $5,200) drained it — so $16,500 is suspended on Form 7203 until he
restores basis. (2) Knock-on effect: had the full $28,000 cleared basis, §469(i) MAGI would have been
$122,400 − $28,000 = $94,400 — under $100,000 — and the rental special allowance would have been the
full $25,000, enough to absorb the entire $21,018 rental loss. Because only $11,500 is allowed, MAGI
stays at $110,900, the allowance is $19,550, and $1,468 of rental loss is carried forward on Form 8582
Part VII as well. (Direction matters: the *allowed* nonpassive loss lowers MAGI and therefore *raises*
the allowance — had this loss been passive, MAGI would be $122,400 and the allowance only $13,800.)
Net Schedule E effect: −$31,050, not the −$49,018 the file might naively suggest; the $17,968 gap is
exactly $16,500 (suspended S-corp) + $1,468 (rental carryforward).
