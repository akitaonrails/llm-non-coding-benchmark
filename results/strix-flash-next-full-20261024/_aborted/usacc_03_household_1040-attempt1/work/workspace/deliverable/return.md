# 2025 Form 1040 — Marcus & Elena Reyes (MFJ) + NY part-year allocation

Return prepared from `documents/` using only `library/` (see `library/INDEX.md`). Every figure below
shows its arithmetic and the library authority. Judgment calls are cross-referenced to
`judgment_calls.md`; unresolved items are in `QUESTIONS.md` and `STATUS.md`.

**Headline:** AGI $91,350 · taxable income $59,850 · total tax $6,408 · withholding $8,730 ·
**federal refund $2,322**.

**Round 2 (2026-10-25):** the client answered the open questions; the answers **confirmed** the basis
facts and zero debt basis, the signed Form 8332 releasing Leo to his father for 2025, marketplace
coverage ending June 30 (employer plan from July 1), employee-convenience remote work for both
spouses, and an unrelated broker-found tenant whose rent was never raised. **No figure below
changed.** What remains open is listed in `QUESTIONS.md` §B; the only open item that moves money is
the 8962 family-size question (B1), which cannot be priced from the library.

**Marcus's expectation is wrong, and it is the largest item in the return.** The $28,000 S-corp loss
does **not** come straight off their income: it is allowed only to the extent of his stock basis
($11,500), so $11,500 is deducted in 2025 and **$16,500 is suspended** and carried forward
([form7203_instructions_excerpt.md]).

---

## 1. Form 1040 line by line

| Line | Figure | Source / arithmetic |
|---|---:|---|
| 1a Wages | **122,000** | Marcus $68,000 (W-2, Reyes & Pike Consulting Inc) + Elena $54,000 (W-2, Halvorsen Media Group) |
| 2b Taxable interest | **400** | 1099-INT, JPMorgan Chase (Elena) |
| 8 Additional income (Sch 1, line 8) | **(31,050)** | Schedule E: S-corp loss allowed (11,500) + rental loss allowed (19,550) = (31,050) — see §2 and §3 |
| 9 Total income | 91,350 | 122,000 + 400 − 31,050 |
| 10 Adjustments | 0 | none in the file |
| **11 AGI** | **91,350** | 122,000 + 400 − 31,050 |
| 12 Deduction | **31,500** | MFJ standard deduction, 2025 — [1040_instructions_tax_computation.md] |
| 15 Taxable income | **59,850** | 91,350 − 31,500 |
| **16 Tax** | **6,708** | Tax Table (taxable income < $100,000 ⇒ the table is mandatory, not the rate schedule): row "at least 59,850 / but less than 59,900" MFJ = 6,708 — [1040_instructions_tax_computation.md], [tax_table_2025_excerpt.md] |
| 17 Schedule 2, line 3 | **1,900** | Excess advance premium tax credit repayment (Form 8962, limitation at line 28) → Schedule 2 line 2 → Form 1040 line 17 — see §4 *(the line routing is not in the library; the amount is)* |
| 18 | 8,608 | 6,708 + 1,900 |
| **19 CTC** | **2,200** | 1 qualifying child × $2,200 (Sofia, 15). Leo excluded — see §5 |
| 22 | 6,408 | 8,608 − 2,200 |
| 23 Other taxes | 0 | no SE tax, no other Schedule 2 taxes in the file |
| **24 Total tax** | **6,408** | 6,408 + 0 |
| **25d Withholding** | **8,730** | Fed. FIT withheld: Marcus 5,120 + Elena 3,610 |
| **34 Refund** | **2,322** | 8,730 − 6,408 (overpayment; refund or applied, client's election) |

Authority for the tax method: "If your taxable income is less than $100,000, you **must** use the Tax
Table … do not compute it from the rate schedules" — [1040_instructions_tax_computation.md]. The
rate-schedule footnotes in [tax_table_2025_excerpt.md] are marked "for reference only — not to be used
under $100,000", so 6,708 (not a hand-computed 6,705 or similar) is the figure.

### Why the standard deduction, not itemizing
Possible Schedule A items in the file: home mortgage interest $6,480 (1098, Gulf Atlantic, Tampa home
acquired 07/03/2025) + NY income tax withheld $6,752 (3,842 + 2,910) = **$13,232**, still far below
$31,500. (Even if the Brooklyn property tax of $5,140 were counted twice it would be $18,372; it is not
countable twice — it is already a Schedule E expense.) Standard deduction chosen.
*Deductibility limits on Schedule A (SALT cap, mortgage-interest limits) are **not in the library** —
labelled unverified; the conclusion is insensitive to them because the total is under $31,500 either way.*
Authority used: standard deduction amounts, [1040_instructions_tax_computation.md].

### Filing status
MFJ: married couple living together, status determined as of December 31 —
[1040_instructions_tax_computation.md].

---

## 2. Form 7203 — S corporation (Reyes & Pike Consulting Inc, EIN 82-4471930, 40%)

Basis trail from `documents/marcus_basis_note.md` (client-prepared; see Open items). Per
[form7203_instructions_excerpt.md] stock basis is increased by contributions and the shareholder's
share of income and decreased by distributions and then by losses, in that order:

| Year | Beginning | + income | − distributions | Ending |
|---|---:|---:|---:|---:|
| 2021 | 10,000 (contribution) | (2,100) | 0 | 7,900 |
| 2022 | 7,900 | 6,400 | 0 | 14,300 |
| 2023 | 14,300 | 9,800 | (12,000) | 12,100 |
| 2024 | 12,100 | 4,600 | (5,200) | **11,500** |

2025 (Form 7203 Part I):
- Line 1 stock basis, beginning of year = **11,500**
- Debt basis = **0.** Marcus never lent the corporation money; the bank line is personally guaranteed
  by *Pike*, and "a guarantee of corporate debt does **not** create debt basis" —
  [form7203_instructions_excerpt.md]. Marcus's $68,000 W-2 wages from the S corp do not increase
  stock basis (they are compensation, not a contribution or share of income).
- Line 11 loss allowed = lesser of loss (28,000) and basis available (11,500) = **11,500**
- Line 12 et seq. carryover = 28,000 − 11,500 = **16,500** (suspended indefinitely until basis is
  restored)

K-1 box 1 loss (28,000); Part II G states "Shareholder materially participates: **Yes**", so the
allowed $11,500 is a **nonpassive** Schedule E Part II loss (not a passive activity), which matters
for §3.

---

## 3. Form 8582 — Brooklyn rental (318 Dean St #4B)

Schedule E loss before the limitation (from `documents/rental_summary_brooklyn.md`):

```
Rent received                    18,000  (12 x 1,500)
Mortgage interest               (11,900)
Common charges                   (7,860)
Property tax                     (5,140)
Repairs (water heater)           (2,350)
Insurance                        (1,150)
Management/legal                   (800)
Depreciation (270,000 / 27.5)    (9,818)
                                 ------
Net rental loss                 (21,018)     expenses 39,018 - rent 18,000
```

Passive-activity / special allowance — [form8582_instructions_excerpt.md]:

- Elena "handles everything herself (approves tenants, arranges repairs)" ⇒ **active participation** ⇒
  eligible for the up-to-$25,000 allowance against nonpassive income.
- **MAGI** = AGI figured *without* any passive activity loss, but *with* nonpassive losses allowed in
  the year (the S-corp loss, "to the extent allowed by basis"):
  `122,000 + 400 − 11,500 = 110,900`
- Allowance = `25,000 − 50% x (110,900 − 100,000) = 25,000 − 5,450 = 19,550` (not yet zero; MAGI is
  under the $150,000 MFJ cliff)
- **Loss allowed = min(21,018 ; 19,550) = 19,550**
- **Carryforward (Part VII) = 21,018 − 19,550 = 1,468**

Note the interaction: because basis limited the S-corp loss to 11,500, MAGI stayed at 110,900, which
*shrank* the rental allowance by 5,450. If the full 28,000 had been allowed (as Marcus expects), MAGI
would be 94,400 and the full 25,000 allowance — and the full 21,018 rental loss — would have been
available. That is not the law under the library, and the effect of the basis limitation is that
1,468 of rental loss is also carried forward.

**Below-market rent ($1,500 vs ~$2,600 market):** per the same file, renting below market to an
*unrelated* tenant because rent was never raised "does not by itself trigger this rule if the rent is a
fair rental for that lease," so the days are not personal-use days and the loss is allowed. This is a
judgment call with a large downside — see `judgment_calls.md` §4.

---

## 4. Form 8962 — Premium Tax Credit (NY State of Health, policy NYSH-77120-RE)

1095-A: covered individuals Marcus, Elena, Sofia (15), Leo (9); coverage **January–June** only
(6 months); annual totals: enrollment premium $10,320 ($1,720/mo), SLCSP $10,140 ($1,690/mo),
advance PTC $9,900 ($1,650/mo). (Totals confirm 6 months: 1,720×6=10,320, 1,690×6=10,140,
1,650×6=9,900.)

Per [form8962_instructions_excerpt.md]:

1. **Household income** = modified AGI (AGI + tax-exempt interest + nontaxable Social Security +
   excluded foreign income) = **91,350** (the file has none of the add-backs).
2. **FPL**, family of 4, 48 contiguous states, 2025 = **31,200**.
3. **% FPL** = 91,350 / 31,200 = **292.79%** (unrounded 292.788462%)
4. **Applicable figure** (Table 2, linear within the 250–300% band: 4.00% → 6.00%):
   `4.00% + (292.788462 − 250)/50 x 2.00% = 4.00% + 1.711538% = 5.711538%`
5. **Contribution** = 91,350 × 5.711538% = **5,217.49/yr** → **434.79/month** (carried unrounded;
   multiplying by the display-rounded 5.7115% would give 5,217.45 — the unrounded rate is used)
6. **Monthly PTC** = lesser of enrollment premium (1,720) and SLCSP − contribution
   (1,690 − 434.79 = 1,255.21) ⇒ **1,255.21/month**
7. **Annual PTC** = 6 covered months × 1,255.209 = **7,531.25** (Jul–Dec: no coverage, no PTC —
   *client confirmed the marketplace plan was dropped when Elena joined Halvorsen's employer plan on
   July 1; there is no second 1095-A*).
   *Unrounded monthly × 6 = 7,531.25; using the rounded monthly (1,255.21 × 6) gives 7,531.26 — a
   1-cent difference I am leaving visible rather than forcing.*
8. **Excess APTC** = 9,900 − 7,531.25 = **2,368.75**
9. **Repayment limitation (line 28)**, MFJ, income 200%–<300% FPL = **1,900**
10. **Repayment** = min(2,368.75 ; 1,900) = **1,900** → Schedule 2, line 2 → Form 1040 line 17

The repayment does **not** arise because coverage ended in June — the credit and the advance payments
are both counted for the same six months. It arises because $1,650/month was being advanced against a
credit of only $1,255.21/month. It does arise *because of* the losses: household income of 91,350 is
292.79% FPL, which puts the repayment cap at $1,900 (200–<300% band); with no losses allowed,
household income would be 122,400 = 392.3% FPL, the cap would be $3,150, and the applicable figure
would be higher (so the credit smaller).

---

## 5. Dependents

- **Sofia Reyes, 15** — their child, under 17 at year end, lives with them ⇒ qualifying child,
  **CTC $2,200** ([1040_instructions_tax_computation.md]: "$2,200 per qualifying child under age 17 at
  the end of the year who is your dependent").
- **Leo Castellano, 9** (DOB 03/14/2016) — **not claimed, no CTC.** The Kings County custody order
  ¶9 alternates: "The Father shall claim the child in odd-numbered tax years; the Mother shall claim
  the child in even-numbered tax years," and the library states that "where a decree or agreement
  alternates years, the agreement controls which parent claims the child for that year," and that "a
  child claimed by the other parent under a Form 8332 release is not your qualifying child for the
  credit" — [1040_instructions_tax_computation.md]. 2025 is odd ⇒ father's year, even though Leo
  resides primarily with Elena. *Confirmed by the client 2026-10-25: Elena signed the Form 8332
  releasing 2025 to the father ("it's his year"), so the release mechanism in ¶9 of the order was in
  fact executed.*
- Dependents list for the return: **Sofia only.**
- Leo is still a covered individual on the 1095-A; the 8962 family-size question this creates is an
  open item (`QUESTIONS.md` B1, sensitivity in `judgment_calls.md` §6).

---

## 6. New York part-year (IT-203) — allocation only

Residency facts from `documents/email_move_dates.txt`: Brooklyn lease ended **June 30**; they slept in
Queens June 28–30 (inside the NY period either way) and closed/moved into the Tampa home **July 3**.

- **Resident period: Jan 1 – Jun 30, 2025 = 181 days** (31+28+31+30+31+30).
  Nonresident: Jul 1 – Dec 31 = **184 days**.
- **Marcus NY wages: $68,000 (100%).** Reyes & Pike is a New York employer (1 Liberty Plaza, NYC).
  Under the convenience-of-the-employer rule, "wages paid by a New York employer to an employee who
  works from an out-of-state location for the employee's own convenience are New York source income";
  only days worked outside NY "for the employer's necessity" are not. *Client confirmed 2026-10-25:
  the company "said remote was fine when I asked to move; they didn't need me out of state" ⇒ all of
  his wages are NY taxable (resident-period wages as resident income, Jul–Dec wages as NY source
  income).*
- **Elena NY wages: $54,000 (100%).** Halvorsen Media Group is at 230 Park Ave S, NYC; "Halvorsen let
  me go fully remote" reads as her accommodation, i.e. convenience ⇒ same treatment. *Confirmed
  2026-10-25: Halvorsen "closed their Tampa office years ago; they approved my request" — no employer
  necessity.*
- **Method:** day-count for residency period (181/365) for non-wage income; wages 100% NY under the
  convenience rule; attach the allocation schedule. Authority:
  [ny_it203_part_year_excerpt.md].
  *Rejected alternative:* if remote work were documented as employer necessity, wages would be
  allocated 181/365 ⇒ Marcus $33,720.55, Elena $26,778.08.
- The Brooklyn condo rent ($18,000 gross, net loss) is NY source for the nonresident period, and the
  S-corp loss has an unaddressed NY sourcing question; the library excerpt does not cover either.
- **Not computable from the library:** NY tax, whether the $6,752 of NY withholding is refunded, and
  any NYC resident tax for Jan–Jun. The library has no NY rate schedule, standard deduction, or
  credits; it says only that "tax withheld in excess of the tax due is refunded on IT-203."
  **This is an open item, not a number I will invent.**
- Assumption stated prominently: they are **part-year** residents, i.e. they abandoned the NY abode on
  June 30 and spent ≤183 days in NY after. The library excerpt does not contain NY's definition of
  residency (abode test / 183-day test), so the part-year status itself is assumed, not verified.
  Post-July NY visit day counts were not supplied and stay flagged (`QUESTIONS.md` B6); they do not
  change the wage allocation under the confirmed convenience treatment.

---

## 7. Items in the file that produced no federal figure
- Form 1098 mortgage interest $6,480 (Tampa) — itemizing is not beneficial (see §1).
- NY state withholding $6,752 — a NY matter only; not federally deductible given the standard deduction.
- W-2 box 12 DD $7,140 (employer health coverage, Jul–Dec) — informational; note it implies they had
  employer coverage in H2, consistent with marketplace coverage ending June 30 (*client confirmed:
  the marketplace plan was dropped when Elena joined Halvorsen's plan July 1 — no second 1095-A*).
- K-1 gross receipts $612,400 — informational.
