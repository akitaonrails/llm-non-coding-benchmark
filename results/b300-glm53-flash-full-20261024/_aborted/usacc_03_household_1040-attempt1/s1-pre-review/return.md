# Reyes / Reyes — 2025 Form 1040 (MFJ) + NY part-year — return.md

All citations point to files in `library/INDEX.md`: 1040 instructions [1], 2025 Tax Table [2], Form 7203 instructions [3], Form 8582 instructions [4], Form 8962 instructions [5], NY IT-203 instructions [6].

## Income

| Item | Amount | Source / arithmetic | Authority |
|---|---:|---|---|
| 1a Wages (Marcus 68,000 + Elena 54,000) | 122,000 | W-2s, box 1 | [1] |
| 2b Interest | 400 | 1099-INT box 1 | [1] |
| K-1 1120-S loss, allowed by basis | (11,500) | See Form 7203 below | [3] |
| Rental loss allowed (after 8582) | (10,550) | See Form 8582 below | [4] |
| **11 AGI** | **118,350** | 122,000 + 400 + 18,000 rental gross − 11,500 − 10,550 | [4] |

## Form 7203 — S corporation basis (Marcus, Reyes & Pike Consulting, 40%)

Starting stock basis = 10,000 (2021) + (−2,100) + 6,400 + 9,800 − 12,000 + 4,600 − 5,200 (2021–2024 income/loss and distributions, in order: income first, then distributions per [3]) = **11,500**; debt basis = 0 (no shareholder loans; a personal guarantee of the bank line does not create debt basis [3]).

2025 loss (K-1) = 28,000. Loss allowed (Part I line 11) = lesser of loss and basis = **11,500**; **suspended carryforward = 16,500** (28,000 − 11,500). The loss does **not** come straight off income — Marcus's expectation is wrong to that extent. Marcus materially participates (K-1 Part II G), so the allowed 11,500 is a nonpassive loss on Schedule 1, which does reduce MAGI for Form 8582 [4].

## Form 8582 — Brooklyn rental (Elena actively participates)

Loss before limitation = 18,000 rent − (29,200 expenses incl. 11,900 rental mortgage interest + 9,818 depreciation) = **21,018**.

MAGI = AGI with the passive rental loss added back = 122,000 + 400 + 18,000 − 11,500 = **128,900** (nonpassive S-corp loss allowed this year does reduce MAGI [4]).

Special allowance = 25,000 − 50% × (128,900 − 100,000) = 25,000 − 14,450 = **10,550** (MAGI < 150,000, so allowance > 0 [4]).

Loss allowed = lesser of 21,018 and 10,550 = **10,550**; **carryforward = 10,468** (21,018 − 10,550).

## Standard deduction / taxable income

Itemized would be ≈ 6,480 (Tampa 1098 mortgage interest, acquired 07/03/2025) plus FL/NY property taxes — far below the MFJ standard deduction **31,500** [1]; standard deduction taken.

**15 Taxable income = 118,350 − 31,500 = 86,850.**

## Tax — OPEN ITEM (library gap)

Taxable income 86,850 is under 100,000, so [1] requires the Tax Table, and [2]'s excerpt covers only 59,000–61,000 (MFJ). **Tax on 86,850 cannot be verified from the closed library.** The rate-schedule parenthetical in [2] is "for reference only — not to be used under $100,000." For completeness only, computing from that reference schedule (10% to 23,850 = 2,385; 12% on 63,000 = 7,560; total **9,945**) is self-consistent arithmetic but is labeled **unverified**; line 16 is reported at 9,945 solely to allow the return to be filed after the table page is supplied.

## Credits and PTC (Form 8962)

19 Child tax credit: **2,200** — Sofia (15) only. Leo (9) is claimed by his father in 2025 per the alternating custody agreement, which controls [1]; the client confirmed Elena signed Form 8332 releasing Leo for 2025. A Form 8332-released child is not our qualifying child for the credit [1].

Form 8962 (coverage Jan–Jun, 6 months):
- Household income = AGI (no tax-exempt interest) = **118,350** [5].
- FPL% = 118,350 ÷ 31,200 (family of 4 [5]) = **379.3%**.
- Applicable figure, 300–400% band, linear [5]: 6.00% + 2.50% × (379.3269 − 300)/100 = **7.983%**.
- Monthly contribution = 118,350 × 7.983% ÷ 12 = 787.34.
- Monthly PTC = lesser of premium 1,720 and (SLCSP 1,690 − 787.34 = 902.66) = 902.66 ⇒ **annual PTC = 5,416** (902.66 × 6).
- APTC (1095-A) = 9,900 ⇒ excess advance = **4,484** (9,900 − 5,416).
- Repayment limitation, MFJ at 300%–<400% = **3,150** [5]; **Sch 2 excess APTC repayment = 3,150** (line 17).

## Total tax and balance

- 24 Total tax = 9,945 (unverified, see above) + 3,150 = **13,095**.
- 25d Withholding = 5,120 + 3,610 = **8,730**.
- **37 Amount owed = 13,095 − 8,730 = 4,365.**

## New York (IT-203 part-year)

- Resident period Jan 1–Jun 30 = **181 days** (31+28+31+30+31+30); the Jun 28–30 nights in Queens were NY days in transit after the Brooklyn lease ended; FL domicile established on arrival Jul 3.
- Both spouses worked for NY employers. Jan–Jul 2 wages are taxed as resident-period income; Jul–Dec remote work from FL for NY employers is NY source under the convenience-of-the-employer rule [6]. **NY wages: Marcus 68,000; Elena 54,000 (100% of each W-2).**
- NY withheld 6,752 (3,842 + 2,910) against 100% NY-source wages — likely a liability, not a refund; exact NY tax computed on IT-203 is outside this filing's federal scope and needs rate schedules not in the library.
