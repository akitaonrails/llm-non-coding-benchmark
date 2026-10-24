# 2025 Form 1040 — Marcus & Elena Reyes (MFJ) — figure-by-figure

All citations are to files listed in `library/INDEX.md`. Sign convention: income/loss lines carry
the sign that enters the 1040 (losses negative); basis balances, allowances, carryforwards and
repayments are shown as positive amounts. Note on the two same-named JSON fields:
`form7203.loss_allowed` is shown **positive** ($11,500 — a limitation amount feeding the basis
computation), while `form8582.loss_allowed` is shown **negative** ($(19,550) — the amount as it
enters the 1040 side). Both are the allowed loss; the signs differ by design.

## Source documents (client file)

| Doc | Key figures |
|---|---|
| W-2 Marcus (Reyes & Pike Consulting Inc, NYC) | wages $68,000; fed WH $5,120; NY wages $68,000; NY WH $3,842 |
| W-2 Elena (Halvorsen Media Group LLC, NYC) | wages $54,000; fed WH $3,610; NY wages $54,000; NY WH $2,910 |
| K-1 Reyes & Pike (40%) | ordinary loss $(28,000); distributions $0; gross receipts $612,400; **materially participates: Yes** |
| Marcus basis note | $10,000 contributed 2021; prior-year income/losses and distributions; never lent the corporation money |
| Rental summary (Brooklyn condo) | rent $18,000; expenses $29,200; depreciation $9,818; rent $1,500/mo vs ~$2,600 market |
| 1095-A (NY of Health) | covered Jan–Jun only; enrollment premium $1,720/mo ($10,320/yr); SLCSP $1,690/mo ($10,140/yr); APTC $1,650/mo ($9,900/yr); 4 covered individuals |
| 1098 | Tampa mortgage interest $6,480 |
| 1099-INT | $400 (Elena) |
| Custody agreement | Leo Castellano (DOB 03/14/2016): father claims in **odd** years, mother in even years; child resides primarily with mother; 8332 to be executed for father's years |
| Move email | Brooklyn lease ended 6/30, out by then; Tampa closing 7/3; Queens (mother's) nights 6/28–30; both employers kept NY withholding all year; Marcus "just works remotely now"; Halvorsen "let me go fully remote" |
| Client responses (round 2) | Tenant is a stranger (nurse) found through a broker in 2019; rent never raised. Marcus: nothing contributed since 2021, never lent the corporation money; Pike guarantees the bank line. Remote work was employee-initiated and approved in both cases (Marcus asked to move; Halvorsen closed its Tampa office years ago and approved Elena's request). Elena signed Form 8332 for Leo's father for 2025 (his year). No other 2025 items; no prior Forms 7203 or lease copy available. |

---

## Form 7203 — S corporation basis (Marcus)

Authority: `library/form7203_instructions_excerpt.md` — losses allowed only to the extent of stock
basis + debt basis; increases first, then decreases by distributions and losses in that order; a
guarantee of corporate debt does **not** create debt basis; line 11 allowed = lesser of loss and basis.

Rollforward (Marcus's note; assumes prior-year losses were allowed — each was ≤ available basis):

| Year | Begin | + Income | − Distributions | − Loss | End |
|---|---:|---:|---:|---:|---:|
| 2021 | 10,000 | — | — | 2,100 | 7,900 |
| 2022 | 7,900 | 6,400 | — | — | 14,300 |
| 2023 | 14,300 | 9,800 | 12,000 | — | 12,100 |
| 2024 | 12,100 | 4,600 | 5,200 | — | **11,500** |

- **Line 1 stock basis at beginning of 2025: $11,500.**
- Debt basis: **$0** — client confirms Marcus never lent the corporation money and has contributed
  nothing since 2021; Pike's personal guarantee of the bank line gives *Marcus* no debt basis
  (library: only a direct shareholder loan creates debt basis).
- 2025 K-1 loss $28,000. **Loss allowed = min($28,000, $11,500) = $11,500.**
- **Suspended/carried forward = 28,000 − 11,500 = $16,500** (indefinite carryforward until basis restored).

Marcus's expectation that "the loss comes straight off our income" is **wrong**: only $11,500 is
currently deductible. (K-1 Part II G: materially participates → the allowed loss is nonpassive and
reduces ordinary income.)

## Form 8582 — Brooklyn rental (Elena)

Authority: `library/form8582_instructions_excerpt.md` — active-participation special allowance up to
$25,000; reduced 50% of MAGI over $100,000, zero at MAGI ≥ $150,000; MAGI computed **without** the
passive loss; nonpassive allowed losses (the S-corp loss) **do** reduce MAGI; below-market-to-unrelated-tenant carve-out.

Net rental loss: 18,000 − 29,200 − 9,818 = **$(21,018)**.
(Depreciation: 270,000 ÷ 27.5 = 9,818.18 → 9,818 as booked; full year, property rented all year.
The 27.5-year recovery period is the client's own computation in the summary — depreciation rules
are **not in the library**, so it is used as the client's booked figure, not cited as authority.)

Elena handles everything (approves tenants, arranges repairs) → active participation.
Below-market rent ($1,500 vs ~$2,600): does **not** trigger §280A(d)(2)(C) per the library's
carve-out — renting below market to an unrelated tenant because rent was never raised does not by
itself convert the days to personal use, "if the rent is a fair rental for that lease." Client
confirms the tenant is an unrelated stranger (a nurse found through a broker in 2019) and the rent
was simply never raised (see `judgment_calls.md`). Lease copy not available.

MAGI for §469(i) = AGI **excluding the rental loss**, including the allowed S-corp loss:
- 68,000 + 54,000 (wages) + 400 (interest) − 11,500 (allowed S-corp loss) = **$110,900**.

Special allowance phase-out: (110,900 − 100,000) × 50% = 5,450 → allowance = 25,000 − 5,450 = **$19,550**.
- **Loss allowed: $19,550** (lesser of loss 21,018 and allowance 19,550).
- **Carryforward (Part VII): 21,018 − 19,550 = $1,468.**

No circularity: MAGI excludes the PAL itself, so the rental allowance does not feed back into MAGI.

## Form 1040

| Line | Figure | Arithmetic / authority |
|---|---:|---|
| 1a Wages | 122,000 | 68,000 + 54,000 (W-2s) |
| 2b Interest | 400 | 1099-INT |
| 8 Sch 1 income | **(31,050)** | rental allowed (19,550) + S-corp allowed (11,500); both are Schedule E losses reported on Schedule 1 and carried to line 8 (per the engagement schema field `8_other_income_sch1`); the line-by-line mechanics (Sch E → Sch 1 line 15) are form logistics **not in the library** |
| 11 AGI | **91,350** | 122,000 + 400 − 31,050 |
| 12 Deduction | **31,500** | Standard MFJ 2025 = $31,500 (`1040_instructions_tax_computation.md`). Itemized would be ≈ 6,480 mortgage + 6,752 state income tax withheld ≈ 13,232 < 31,500, so standard. (Deductibility of state/local taxes and the $10,000 SALT cap are **not in the library** — see open items; the standard deduction wins even ignoring state taxes entirely. No FL property-tax data in file.) |
| 15 Taxable income | **59,850** | 91,350 − 31,500 |
| 16 Tax | **6,708** | TI < $100,000 → **must** use Tax Table (library rule); row at least $59,850 but less than $59,900 → 6,708 (`tax_table_2025_excerpt.md`) |
| 17 Sch 2 (excess APTC) | **1,900** | Form 8962 repayment, limited by the library's line 28 limitation (below); entering the 1040 at line 17 per the engagement schema field `17_sch2_excess_aptc` |
| 19 CTC | **2,200** | $2,200 × 1 qualifying child (Sofia, 15) (`1040_instructions_tax_computation.md`); Leo excluded — claimed by father in odd years per agreement/8332 |
| 24 Total tax | **6,408** | (16) 6,708 + (17) 1,900 = 8,608; less (19) 2,200 = 6,408. No Sch 3 credits; the credit is fully used against tax (2,200 < 8,608), so refundability mechanics — which are not in the library — are not in play |
| 25d Withholding | **8,730** | 5,120 + 3,610 |
| 34 Overpayment (refund) | **2,322** | 8,730 − 6,408 |

## Form 8962 — Premium Tax Credit

Authority: `library/form8962_instructions_excerpt.md`.

Coverage: Jan–Jun only (6 months; employer coverage DD box per Elena's W-2 starts Jul — consistent).

- Household income (MAGI for PTC) = 91,350 + 0 (no tax-exempt interest, nontaxable SS, or excluded
  foreign income) = **$91,350**.
- FPL (family of 4, 2025, per library): **$31,200**.
  **Family-size assumption (open item):** computed as a family of **4** — the only FPL figure in the
  library. Leo lived in the household all year and was on the policy, but is *not* claimed as a
  dependent in 2025. Whether the 8962 family count follows the dependents claimed or the household,
  and the family-of-3 FPL, are **not in the library**; the client has no further information, so the
  gap cannot be closed here. Sensitivity (household income fixed at 91,350; library bands only):
  if a smaller FPL puts income ≥ 300% FPL (FPL below $30,450) the cap rises to $3,150 and the
  excess — itself larger at a smaller FPL — becomes repayable: e.g. at the 300% boundary the excess
  is $2,500.50; at ≥ 400% FPL (FPL ≤ $22,837.50) there is no cap and the excess maxes at
  **$3,642.38** (refund would fall from $2,322 to as low as $579.62). See `judgment_calls.md` §5.
- % FPL = 91,350 ÷ 31,200 = **292.79%**.
- Applicable figure (250–300% band, linear 4.00–6.00%): 4.00% + 2.00% × (292.7884615 − 250)/50
  = 4.00% + 1.7115385% = **5.7115385%** (exactly 5.7115384615…%; `return.json` carries 5.7115385, which
  reproduces the PTC below to the cent — the PTC is computed from the unrounded figure).
- Annual contribution = 91,350 × 5.711538% = 5,217.49 → monthly 434.79.
- Monthly PTC = lesser of enrollment $1,720 and SLCSP 1,690 − 434.79 = 1,255.21 → **$1,255.21**.
- **Annual PTC = $1,255.2091 × 6 = $7,531.25.** (Carrying unrounded cents; multiplying the rounded
  monthly 1,255.21 × 6 gives 1,255.21×6 = $7,531.26 — the 1-cent difference moves nothing, since the
  repayment is capped at $1,900 either way.)
- APTC (1095-A col C) = 1,650 × 6 = **$9,900**.
- **Excess APTC = 9,900 − 7,531.25 = $2,368.75.**
- Repayment limitation: 292.79% falls in 200–<300% FPL, MFJ → **$1,900**.
- **Repayment = min(2,368.75, 1,900) = $1,900** → Form 1040 line 17 / Sch 2.

## Dependents

- **Sofia Reyes, 15** — their child, under 17 → claimed; CTC $2,200.
- **Leo Castellano, 9** — **not** claimed for 2025. Custody agreement: father claims odd years,
  mother even; 2025 is odd. Client confirms Elena signed Form 8332 for Leo's father for 2025 ("it's
  his year"). Library: the agreement controls, and a child claimed by the other parent under an
  8332 release is not your qualifying child for the CTC.

## New York (IT-203) part-year

Authority: `library/ny_it203_part_year_excerpt.md` — resident period income + NY-source income in
nonresident period; convenience-of-the-employer rule for remote work for a NY employer.

- **Resident period: Jan 1 – Jun 30 = 181 days** (Brooklyn lease ended 6/30; they were out by then;
  nights at Elena's mother's in Queens 6/28–30 fall inside that period and do not extend it).
  Nonresident: Jul 1 – Dec 31 = 184 days (Tampa home acquired 7/3; Jul 1–2 travel days are not NY
  resident days).
- **Marcus — NY wages $68,000 (all).** Employer is NYC-based; client confirms Marcus *asked* to move
  and the company simply approved ("they didn't need me out of state") → employee convenience, so the
  convenience-of-the-employer rule makes all his wages NY source even during the nonresident period.
- **Elena — NY wages $54,000 (all).** Jan–Jun taxed as resident-period income regardless; Jul–Dec
  client confirms Halvorsen closed its Tampa office years ago and approved *her* request to go fully
  remote → employee convenience, not employer necessity → NY source. (Had a NY-business-necessity
  fact existed, her Jul–Dec wages would leave NY source; the client's answer closes that branch.)
- NY WH of $6,752 (3,842 + 2,910) is credited on IT-203; excess withheld over tax
  due is refunded there. NY tax is not computed here — the library contains no NY rate tables.
- Brooklyn rental: the Jan–Jun rent is taxable in any case as resident-period income (library). The
  Jul–Dec rent would also be taxed by NY under the general principle that income from New York real
  property is New York source — but that principle is **not stated in the library** (the excerpt
  only addresses wage sourcing), so it is flagged as **unverified context, not cited**. Either way
  it does not change the federal figures above.

## Items not computable / not in library (stated, not invented)

- Deductibility of state/local taxes and the $10,000 SALT cap are not in the library; the itemized
  comparison is labeled approximate and does not change the result (standard deduction controls —
  even ignoring state taxes, 6,480 ≪ 31,500).
- NY tax on IT-203: no NY rate schedule in the library → not computed. NY *inputs* (resident days,
  NY-source wages) are client-confirmed. The rule that NY real-property income is NY source is also
  not in the library (unverified context).
- Form logistics not in the library (used only per the engagement schema's line labels, not cited as
  authority): Schedule E → Schedule 1 routing, the 8962 line-28 placement into 1040 line 17, and the
  27.5-year depreciation convention (client's own computation).
- CTC refundability mechanics are not in the library; not in play here because tax (8,608) exceeds
  the credit (2,200).
- Form 8962 family-size rule and the family-of-3 FPL: not in the library and the client has no
  further information → family-of-4 assumption flagged above with quantified sensitivity. This is the
  only remaining item that could change a federal figure.
- Supporting documents not in the file (client has none): the 2019 Brooklyn lease and prior-year
  Forms 7203. The facts for the §280A carve-out and the basis rollforward rest on client statements.
