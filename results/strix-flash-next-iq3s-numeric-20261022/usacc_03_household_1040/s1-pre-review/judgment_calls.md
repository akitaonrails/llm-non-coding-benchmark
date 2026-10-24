# Judgment calls — every place a decision was required

Each entry: the call made, the authority, and the alternative rejected.

## 1. S-corp loss limited to stock basis (the big one)
**Call:** Marcus's $28,000 K-1 loss is allowed only to $11,500 — his 1/1/2025 stock basis — with
$16,500 suspended. Basis roll-forward increases income before distributions, per the 7203 ordering
("increased by capital contributions and the shareholder's share of income, and decreased by
distributions and by losses (in that order)"). Pike's personal guarantee of the bank line creates no
debt basis; Marcus made no direct loans. **[7203]**
**Rejected:** Marcus's expectation (marcus_basis_note.md, per a friend) that the 2025 loss "comes
straight off" income, i.e. deducting the full 28,000. Also rejected: any argument that the corporate
bank line gives debt basis — a guarantee is not a direct loan. **[7203]**
**Rejected (minor):** ordering distributions before income — arithmetically identical here because
distributions never exceeded basis in any year.
**Client confirmed 10/22:** no contributions since 2021 and no shareholder loans ever; Pike guarantees
the bank line. Basis trail complete on client's word; the 2024 as-filed Form 7203 was still not
produced (residual verification gap, flagged in STATUS.md).
**Turn 3 (Marcus pushback):** asked why the loss is suspended when "my buddy's CPA let him take his
whole loss," and whether Pike's guarantee can count. Answered per **[7203]** verbatim: guarantee ≠
debt basis (and it is Pike's, not Marcus's); the friend's facts (basis, direct loans, entity type)
are unknown and not transferable. Re-verified the K-1: box 16 distributions for 2025 = $0.00, so
nothing reduced basis before the loss — allowed 11,500 / suspended 16,500 unchanged. The only
legitimate lever is documentary: a 2024 as-filed Form 7203 showing higher opening basis, or an
actual direct loan (client says none exists). Decision stands. **Turn 4:** client has no additional
information — the 2024 return is unobtainable, so the basis trail closes as a documented client
representation; open item B is final, not pending.

## 2. S-corp activity treated as nonpassive
**Call:** K-1 Part II G says the shareholder materially participates, so the §469 passive rules do
not gate the S-corp loss; only §1366(d) basis does, and the allowed $11,500 reduces §469(i) MAGI.
**[7203]**, **[8582]** ("nonpassive losses allowed in the year ... do reduce MAGI")
**Rejected:** treating the S-corp loss as passive and funneling it through the $25,000 allowance
with the rental. Nothing in the file supports passivity; the K-1 affirmatively shows material
participation.

## 3. Below-market rent on the Brooklyn condo ($1,500 vs ~$2,600 market)
**Call:** The loss is allowed; the days are not personal-use days. The library states that renting
below market to an *unrelated* tenant because rent was never raised does not by itself trigger the
§280A(d)(2)(C) personal-use rule if the rent is a fair rental for that lease — the file matches
(exact 6-year-old lease, same tenant, never raised). **[8582]**
**Rejected:** reading the personal-use rule strictly — market rent $2,600 > charged $1,500 would
make every day a personal-use day, disallowing the entire 21,018 loss (with no 8582 carryforward,
and no depreciation recapture relief). This is the single largest risk in the return (±21,018 loss,
≈ $2,500 of tax).
**Client confirmed 10/22:** the tenant is unrelated (a nurse found through a broker in 2019) and the
rent was simply never raised — both conditions the library's carve-out names. Residual: the library's
qualifier "if the rent is a fair rental for that lease" has no threshold in the library, and $1,500
is ~42% below market; if that qualifier were read strictly the loss falls. Left open, flagged in
STATUS.md.

## 4. Rental: active participation → $25,000 special allowance
**Call:** Elena approves tenants and arranges repairs herself → active participation; allowance =
25,000 − 50% × (MAGI 110,900 − 100,000) = 19,550. **[8582]**
**Rejected:** (a) treating the rental as a bare passive with no allowance → entire 21,018
disallowed; (b) computing MAGI *without* subtracting the allowed S-corp loss (MAGI 122,400 →
allowance 13,800) — the library expressly says allowed nonpassive losses reduce MAGI. **[8582]**

## 5. Leo (age 9) not claimed in 2025
**Call:** The Kings County custody order alternates years: father claims Leo in odd-numbered tax
years, mother in even. 2025 is odd → Leo is claimed by his father; Elena (custodial parent) executes
Form 8332. The library: "Where a decree or agreement alternates years, the agreement controls."
**[1040-i]** No CTC for Leo: a child claimed by the other parent under an 8332 release is not a
qualifying child for the credit. **[1040-i]**
**Rejected:** claiming Leo because he "resides primarily with the Mother" (the default custodial-parent
rule) — the agreement overrides the default for 2025. Cost of the call: $2,200 CTC. **Client confirmed
10/22:** Elena signed the Form 8332 releasing Leo to his father for 2025 ("his year"), so the call is
locked — no CTC for Leo. This question is closed.

## 6. Form 8962 household = family of 4
**Call:** FPL $31,200 (2025, family of 4). **[8962]** Matches the four covered individuals on the
1095-A (Marcus, Elena, Sofia, Leo), all living in the household even though Leo's tax claim is the
father's for 2025.
**Rejected:** a family-of-3 household (dropping Leo because he is not our 2025 dependent) — the
library provides no family-of-3 FPL, so that computation would be unverifiable, and it conflicts
with the policy composition. (Direction of error if wrong: smaller FPL → higher FPL% → higher
applicable figure → smaller PTC → bigger repayment.)

## 7. Coverage months: 6, not 12
**Call:** Marketplace coverage ran January–June only; PTC computed for 6 months. The 1095-A annual
line-33 totals (10,320 / 10,140 / 9,900) are exactly 6 × the monthly amounts (1,720 / 1,690 /
1,650), and Elena's W-2 box 12 DD is labeled "Jul–Dec employer coverage." **[8962]**
**Rejected:** treating the plan as in force all 12 months (annual APTC/12 as monthly premiums) —
that would overstate both the credit and the arithmetic; it contradicts the internal consistency of
the 1095-A totals. **Client confirmed 10/22:** they dropped the marketplace plan and Elena went on
Halvorsen's employer plan July 1 — 6 covered months, no second 1095-A. Closed.

## 8. Excess APTC repayment capped at $1,900
**Call:** Household income 292.79% FPL → 200%–<300% MFJ band → cap $1,900; repayment = min(2,369,
1,900) = 1,900. **[8962]**
**Rejected:** repaying the full 2,369 excess — the library states the limitation expressly. (The
"no limitation at 400%+" rule does not apply; 292.79% < 400%.)

## 9. Standard deduction $31,500
**Call:** Take the MFJ standard deduction. **[1040-i]**
**Rejected:** itemizing — known itemizable amounts in the file (6,480 Tampa mortgage interest +
11,900 condo mortgage interest + 5,140 condo property tax = 23,520, before state income taxes and
any caps) cannot reach 31,500 once the SALT cap (amount not in library — unverified) and the mixed
personal/rental use of the condo interest are considered. The margin is comfortable, so no further
itemizing data was pursued.

## 10. NY resident period: Jan 1 – Jun 30 (181 days)
**Call:** Resident period ends when the Brooklyn lease ends and the family is out: June 30.
**[IT203]** 181 of 365 days (2025 is not a leap year).
**Rejected:** ending residency at the July 3 FL closing (184 days), or at the July 1 move-out vs.
June 28–30 Queens nights — immaterial for wages (see #11) and de minimis for the Jan–Jun rental
income (all NY-source regardless), but recorded as an assumption. **[IT203]** **Client had no
further information 10/22 on July 1–2 physical presence** — assumption stands and is immaterial
(wages full-year NY source; rental NY-source all year), so this is a documented residual, not an
open dollar risk.

## 11. NY wages: full-year NY source for both spouses (convenience of the employer)
**Call:** Marcus (Reyes & Pike Consulting, NY employer, works remotely from FL after the move) and
Elena (Halvorsen Media Group, NY employer, "let me go fully remote") both work out of state for
their own convenience, not employer necessity → 100% of wages ($68,000 + $54,000) are NY source.
**[IT203]** Marcus's arrangement is family-driven (they bought a house in Tampa), not employer-driven.
**Rejected:** day-ratio allocation of wages (181/365 → 33,709 / 26,745), which would apply only if
the out-of-state work were necessitated by the employers. **[IT203]** NY *tax* is not computed at
all — the library has no NY rate schedules, so any dollar figure would be unverifiable. (The library
only says excess withholding is refunded on IT-203; whether 6,752 of full-year withholding exceeds
the NY tax due is unknowable in the closed library — under the convenience rule most of these wages
are NY-taxable all year regardless, so no refund is asserted.)
**Client confirmed 10/22:** Marcus *asked* to move and the company "didn't need me out of state";
Halvorsen closed its Tampa office years ago and merely *approved Elena's request*. Both arrangements
are employee-initiated with employer approval = convenience, not necessity. **Rejected (after the
answers):** a necessity argument — that a location-independent job or a closed branch office "requires"
out-of-state work. The library keys the exception to days worked *at the employer's necessity*;
employer permission to relocate does not meet it. **[IT203]** Full-year NY wages (68,000 / 54,000) stand.

## 12. Template mapping: pass-through losses shown in `8_other_income_sch1`
**Call:** The template has no Form 1040 line-5 field, so the −31,050 of Schedule E losses (S-corp
−11,500 + rental −19,550) is carried in that field so AGI reconciles.
**Rejected:** putting −31,050 nowhere (line 8 = 0) — AGI (91,350) would not reconcile with the
template's fields. On the actual filed return these belong on **line 5** (Schedule E), not line 8;
`return.md` §3 states this explicitly.

## 13. Items the library cannot support — not taken, labeled unverified
**Call:** No §199A QBI deduction, no EITC, no NY/NYC city tax computations, no SALT-cap arithmetic.
**[INDEX]** limits the authorities to the seven library files.
**Rejected:** estimating a QBI deduction or EITC from memory — every such figure would violate the
engagement's citation rule; each is flagged in `return.md` §8 as unverified/not claimed.

## 14. Filing status
**Call:** MFJ — married and living together as of Dec 31. **[1040-i]**
**Rejected:** none plausible on these facts; recorded for completeness.

## 15. Rounding convention
**Call:** Whole-dollar rounding on 1040 lines; exact fractions kept through the 8962 band
interpolation (292.7885% FPL, 5.7115% applicable figure) and rounded at the end (PTC 7,531, excess
2,369). **[8962]**
**Rejected:** rounding FPL% to 292.8% before interpolation — changes the applicable figure by
0.0006% (≈ $0.60/yr); immaterial, noted only for reproducibility.
