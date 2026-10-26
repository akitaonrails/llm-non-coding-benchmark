# 2025 Schedule C — Dana Okafor, freelance UX design ("Dana Okafor Design")

**Method:** Cash (income reported in the year actually received — library `schedule_c_instructions_excerpt.md`, "Cash method" note).
**Scope:** Schedule C and Schedule SE only. Wage income, withholding, estimated-tax payments, health insurance, and personal items are **not** on Schedule C (see not_on_schedule_c section and `schedule_c.json`).

**Figures below are final for the information available:** the client has answered the questionnaire — Q1 (Beacon/Orchard inside the 1099-K, 2.9% processor fee) and Q8 (own health plan) are resolved and confirmed, Q4 (phone/internet 60% business) is incorporated at the client's stated estimate, and Q5's Denver/gift leg is confirmed personal. Q2, Q6 and Q7 came back with no additional information and the 1,150 misc miles lack page-2 itemization — those remain flagged in situ and in `STATUS.md`. Line numbers follow the library excerpt (`schedule_c_instructions_excerpt.md`), including **Line 18 = Office expense**.

## Summary

| | Amount |
|---|---|
| Line 1 Gross receipts | $50,750.00 |
| Line 28 Total expenses | $11,778.63 |
| Line 29/31 Net profit | $38,971.37 |
| Schedule SE net earnings (92.35%) | $35,990.06 |
| Schedule SE tax (15.3%) | $5,506.48 |
| ½ SE tax → Schedule 1 line 15 | $2,753.24 |

---

## Line 1 — Gross receipts or sales: **$50,750.00**

$$41{,}350.00 \;(\text{PayHub 1099-K, gross}) + 9{,}400.00 \;(\text{Tessaro 1099-NEC, direct ACH}) = 50{,}750.00$$

****ASSUMPTION (prominent):** the *Beacon Fintech* $18,500 and *Orchard Health PBC* $12,200 1099-NEC amounts were paid to Dana **through PayHub** and are therefore already inside the $41,350.00 1099-K gross — they are **not** added a second time. The library's Line 1 instructions require exactly this: *"If the same payment is reported to you on more than one information return … include the amount only once"* (`schedule_c_instructions_excerpt.md`). Confirmation requested in Q1.

**Support from the bank export** (`documents/bank_checking_2024-12_to_2026-01.csv`, 149 rows, opening balance $4,210.33, running balance reconciles exactly):

1. **No Beacon or Orchard deposits exist.** Zero bank rows mention Beacon or Orchard as a payer (0 credit rows either way). If they had paid $18,500 and $12,200 outside PayHub, the money would be in the only account Dana has ("I only have the one checking account" — client email).
2. **Every PayHub payout ties to the 1099-K gross.** 11 monthly payouts sum to $40,150.85, and $41,350.00 − $1,199.15 = $40,150.85, with $1,199.15 = $41,350.00 × 2.9% exactly. Each payout is the gross month × 97.1% (2.9% processor fee retained):
   - Probe on the only month the 1099-K discloses: box 5a–l Feb = $1,866.68 → $1,866.68 × 0.971 = $1,812.55 = bank payout 2025-02-06, to the cent.
3. **The only other income is Tessaro**, verified in the bank as 4 ACH credits ($2,400.00 + $3,100.00 + $2,150.00 + $1,750.00 = $9,400.00 = the Tessaro 1099-NEC box 1), direct from the client — by nature card/third-party-network-free, so not inside the 1099-K.

**Alternative scenarios** if Q1 had come back differently (computed at the draft utilities figure of line 25 = $0.00; the client has since confirmed the base answer — with line 25 now $1,116.00, each alternative's profit is exactly the figure shown minus $1,116.00):

| Scenario | Line 1 | Line 28 | Line 31 net profit | SE net earnings | SE tax | ½ SE tax |
|---|---|---|---|---|---|---|
| **Base (per return, client-confirmed): Beacon & Orchard inside 1099-K** | **$50,750.00** | **$10,662.63** | **$40,087.37** | **$37,020.69** | **$5,664.17** | **$2,832.09** |
| Beacon outside the 1099-K, Orchard inside | $69,250.00 | $10,662.63 | $58,587.37 | $54,105.44 | $8,278.13 | $4,139.07 |
| Orchard outside, Beacon inside | $62,950.00 | $10,662.63 | $52,287.37 | $48,287.39 | $7,387.97 | $3,693.99 |
| Both outside (worst case mechanical sum) | $81,450.00 | $10,662.63 | $70,787.37 | $65,372.14 | $10,001.94 | $5,000.97 |

Bank evidence makes the base scenario the only one consistent with deposits in the account; mechanical summing of the four forms ($81,450.00) would report income Dana never received, which the Line 1 instruction forbids ("You must report all income actually received in the tax year"). **Client confirms (post-questionnaire):** "Beacon and Orchard both pay me through PayHub. Tessaro pays by bank transfer," and "PayHub takes 2.9% off the top before paying out. The 1099-K number is before their cut." Q1 is resolved in favor of the base figures — the matrix stays for documentation.

## Lines 2–7 — Receipts block

- **Line 2 (returns/allowances): $0.00** — no credit notes/refunds found in the export.
- **Line 3** = 50,750.00 − 0 = **$50,750.00**.
- **Line 4 (cost of goods sold): $0.00** — service business; no inventory or purchases for resale appear in the bank export.
- **Line 5** = 50,750.00 − 0 = **$50,750.00**; **Line 6 (other income): $0.00**; **Line 7 (gross income) = $50,750.00**.

*(Lines 2–7 are the form's standard receipts block; the library excerpt defines Line 1, the cash rule, and the expense lines, and does not restate lines 2–7. Their treatment here is purely arithmetic on top of Line 1.)*

## Line 9 — Car and truck expenses (standard mileage): **$999.60**

Business miles from the mileage log (notebook photo):

| Entry | Miles |
|---|---|
| Jan 6 Beacon kickoff (downtown) | 14 |
| Feb 12 Orchard Health — Round Rock | 38 |
| Mar 3 Print shop — mockups | 11 |
| Apr 29 Beacon design review | 14 |
| Jun 2 Tessaro — Dripping Springs | 58 |
| Jul 15 Orchard — Round Rock | 38 |
| Aug 21 Camera rental — North Austin | 22 |
| Oct 20 Client dinner — Beacon | 16 |
| Nov 11 Tessaro — Dripping Springs | 58 |
| Dec 3 Office supplies run | 9 |
| **Subtotal itemized** | **278** |
| Misc "other client errands (see pg 2)" | 1,150 |
| **Business miles** | **1,428** |

$$1{,}428 \text{ mi} \times \$0.70/\text{mi} = \$999.60$$

Rate: **70¢/mile for 2025 business miles** (Notice 2025-5, Section 3; library: 65.5¢ is the **2023** rate and 67¢ the 2024 rate). Dana's own calculation — 4,860 × $0.655 = **$3,183.30** — is rejected for two independent reasons: (1) the 65.5¢ rate is 2023's, not 2025's; (2) 4,860 total miles includes 3,432 nondeductible **commuting** miles, which Notice 2025-5 §4 and Pub. 463 say stay personal "regardless of the distance":

- 1,200 mi — home → Larkspur office, Jan 7–Apr 25 (W-2 employer's workplace; commuting).
- 936 mi — home → Capital Factory coworking, May–Aug (3×/week, 9 mi round trip).
- 1,296 mi — home → Capital Factory, Sep–Dec.

$999.60 − $3,183.30 = the claimed figure is **$2,183.70 overstated**.

**Client confirms (post-questionnaire):** the ~1,200 Jan–Apr Larkspur miles were daily drives to the W-2 employer's office ("I guess that's commuting?" — correct, that is commuting: Notice 2025-5 §4 / Pub. 463), and "the rest is client stuff and the coworking space" — an attestation that the 1,150 misc miles were client errands. They therefore stay on line 9 as business miles. **Flagged remaining unknown:** page 2 of the notebook was never provided, so per-trip support for 1,150 × $0.70 = $805.00 rests on the log label plus the client's attestation. If treated as unsubstantiated: line 9 = 278 × 0.70 = **$194.60**, line 28 = $10,973.63, line 31 = $39,776.37, SE tax = $5,620.22 (impact +$805.00 of profit).

## Line 10 — Commissions and fees: **$1,199.15**

$41,350.00 − $40,150.85 = **$1,199.15** ($41,350.00 × 2.9% processor fee). The excerpt directs fees retained by a payment processor on amounts reported at gross on Form 1099-K to be deducted here, *not* netted against Line 1 — which is why Line 1 stays at the 1099-K gross. **Client confirms** the fee: "PayHub takes 2.9% off the top before paying out. The 1099-K number is before their cut."

## Line 13 — Depreciation / §179: **$0.00**

The MacBook Pro 14 ($2,149.00, bank 2025-09-14) has no client-approved classification as depreciable property; per the excerpt's Line 13 rule we elect the **de minimis safe harbor** (Reg. §1.263(a)-1(f), items ≤ $2,500 per invoice/item) and expense it under **Line 27a** instead. De minimis election statement to be attached to the return (reminder tracked in `STATUS.md`). No other assets; no §179.

## Line 15 — Insurance (other than health): **$480.00**

Hiscox professional liability, one charge 2025-02-20 = **$480.00**. Health premiums are **excluded** by the excerpt's Line 15 instruction and belong on **Schedule 1 line 17** (see not_on_schedule_c).

## Line 18 — Office expense: **$0.00**

No office-supplies or postage purchases appear in the bank export (the Dec 3 "office supplies run" in the log generated miles only; no corresponding debit). Line per the library excerpt is 18 — note: an earlier working note referenced 16; corrected to follow the library.

## Line 20b — Rent or lease, other business property: **$2,800.00**

Capital Factory coworking membership, 2025-05-08 → 2025-12-08, 8 × $350.00 = **$2,800.00**. The excerpt permits coworking memberships on line 20b. Apartment rent ($1,650 × 12 = $19,800 to M. Okafor) is **not** here — no home-office claim is asserted (see Q7); absent a qualifying qualifying-use home office it stays personal under IRC §262(a)/Pub. 463.

## Line 24a — Travel (away from home overnight on business): **$1,030.00**

October San Francisco / DesignWeek trip:

- Southwest 526 AUS→SFO, 2025-10-02 — **$412.00**
- Hotel Zephyr SF, 2025-10-06 — **$618.00**

$$412.00 + 618.00 = 1{,}030.00$$

**Excluded, client-confirmed:** the June Denver flight ($389.00) and wedding-gift Venmo ($200.00) — "Denver was my cousin's wedding, nothing work-related"; Pub. 463: primarily personal travel is not deductible even if some business casual. The San Francisco legs above stand as drafted (client offered no further information on that trip; the DesignWeek registration $650.00 on line 27a corroborates the business purpose on the bank record).

## Line 24b — Deductible meals: **$95.00**

Business meals during the October SF trip: Marina Deli (2025-10-07) $64.00 + Tartine Manufactory (2025-10-08) $126.00 = $190.00 × 50% = **$95.00** (Pub. 463: 50% of business meals, including while traveling). **Stands as drafted** — client offered no further information on the SF meals. If the Tartine meal alone were not a business meal: line 24b = 64.00 × 50% = **$32.00**, line 28 = $11,841.63, line 31 = $38,908.37, SE tax = $5,497.58.

## Line 25 — Utilities: **$1,116.00**

Gross costs in the bank export: T-Mobile wireless 12 × $85.00 = $1,020.00; Spectrum internet 12 × $70.00 = $840.00; total $1,860.00.

**Client answer (Q4):** "Phone and internet are maybe 60% work. I don't have a separate line."

$$1{,}860.00 \times 60\% = 1{,}116.00$$

**Flagged:** the 60% is Dana's own estimate with no separate business line or usage log behind it. It is applied as given because it is her stated, documented basis — the library item title requires "a reasonable, documented business-use percentage" — but it is the least-corroborated figure on the form. Each 10 percentage points is worth $186.00 of expense (50% → $930.00; 100% → $1,860.00; at $0 a pre-confirmation sensitivity alternative).

## Line 27a — Other expenses: **$4,058.88**

| Item | Computation | Amount |
|---|---|---|
| Figma subscription | 12 × $45.00 | $540.00 |
| Adobe Creative Cloud | 12 × $59.99 | $719.88 |
| DesignWeek SF conference registration (2025-10-06) | — | $650.00 |
| MacBook Pro 14 (2025-09-14) — de minimis safe harbor election (≤ $2,500/item), statement attached | — | $2,149.00 |
| **Total** | 540 + 719.88 + 650 + 2,149 | **$4,058.88** |

All four items fall within the excerpt's line 27a guidance (software subscriptions, professional development, de minimis safe harbor items). MacBook **assumption: entirely used for the business** — client offered no further information on the business-use share (each 10% personal use = $214.90 of expense).

## Line 28 — Total expenses: **$11,778.63**

$$999.60 + 1{,}199.15 + 0.00 + 480.00 + 0.00 + 2{,}800.00 + 1{,}030.00 + 95.00 + 1{,}116.00 + 4{,}058.88 = 11{,}778.63$$

## Line 29 — Tentative profit: **$38,971.37**

50,750.00 − 11,778.63 = 38,971.37.

## Line 30 — Home-office expenses: **$0.00**

Not claimed. Q7 asks whether Dana has an area used *exclusively and regularly* for the business; if yes, the approach changes (home-office deduction on line 30, and per Pub. 463 the home→coworking trips could become deductible at 2,232 mi × $0.70 = $1,562.40 — the Larkspur miles stay commuting regardless, they are the W-2 employer's workplace).

## Line 31 — Net profit or (loss): **$38,971.37**

38,971.37 − 0.00 = 38,971.37.

---

## Schedule SE

| Line | Computation | Amount |
|---|---|---|
| Net earnings from self-employment | 38,971.37 × 0.9235 = 35,990.06019… → **35,990.06** | $35,990.06 |
| SE tax | 35,990.06 × 0.153 = 5,506.47918… → **5,506.48** (12.4% social security + 2.9% Medicare) | $5,506.48 |
| ½ SE tax → Schedule 1 line 15 | 5,506.48 ÷ 2 = **2,753.24** | $2,753.24 |

Wage-base check (library `schedule_se_excerpt.md`, 2025 social-security wage base $176,100): W-2 social security wages $24,800.00 + SE net earnings $35,990.06 = $60,790.06 ≤ $176,100 → social security portion is uncapped here, uniform 15.3% applies. Rounding convention: each SE line is rounded to cents at the point it would be entered on the form.

## Not on Schedule C (personal, other schedules, prior year)

| Item | Amount | Where / why |
|---|---|---|
| Larkspur W-2 wages | $24,800.00 | Form 1040 line 1a — Dana was an **employee** (W-2), not self-employment income |
| Larkspur W-2 federal income tax withheld | $2,310.00 | Form 1040 line 25a |
| 2025 federal estimated tax payments (1,500 + 2,500 + 2,500) | $6,500.00 | Form 1040 line 26 |
| BCBS TX self-employed health premiums, 8 × $380 (May–Dec) | $3,040.00 | **Schedule 1 line 17** — health insurance is barred from Schedule C by the library's Line 15 note; **client confirms** it is her own policy after leaving Larkspur ("not through any employer"), and no BCBS premiums were paid Jan–Apr while she was covered under the W-2 employer plan (box 12 DD $1,960.00). The SEHI employer-availability limitation itself is **not** in the library — flagged unverified |
| Tessaro invoice 1041 paid 2024-12-27 | $3,000.00 | **Prior year** — cash method (library excerpt): belongs on the 2024 return |
| Rent to M. Okafor, 12 × $1,650 | $19,800.00 | Personal, IRC §262(a) — no qualifying home office (Q7 open) |
| H-E-B groceries / debit-card purchases 2025 | $2,102.95 | Personal, IRC §262(a) |
| Netflix 12 × $15.49 | $185.88 | Personal, IRC §262(a) |
| Orangetheory 12 × $49.00 | $588.00 | Personal, IRC §262(a) |
| Southwest AUS-DEN June flight | $389.00 | Personal — **client confirms** "cousin's wedding, nothing work-related"; IRC §262(a); Pub. 463 primarily-personal travel |
| Venmo wedding gift | $200.00 | Personal (gift), IRC §262(a) |
| H-E-B purchase 2024-12-30 | $84.12 | Prior year — personal |

*Informational, no action:* W-2 box 12 DD $1,960 (employer-sponsored health coverage cost, relevant to Q8). Net wage credits in the bank are 8 × $2,437.85 = $19,502.80, versus $24,800.00 − $2,310.00 − $1,537.60 − $359.60 = $20,592.80 implied net — a $1,090.00 difference (likely benefit/payroll detail not visible in the export). The W-2 boxes control the 1040; this does not touch Schedule C.

## Data gap

The bank export file is named `2024-12_to_2026-01` but its last row is **2025-12-12**: no rows exist for Dec 13–31, 2025, and no Q4-2025 estimated-payment row. Asked in Q2; the client offered no additional information, so the figures stand on the export as received. If late-December business receipts exist, Line 1 and the SE tax rise accordingly (+$141.30 SE tax per extra $1,000.00 of receipts); if a 2026-01-15 payment for tax year 2025 was made, Form 1040 line 26 would increase beyond $6,500.00.

## Client responses (post-questionnaire) and remaining unknowns

| Q | Subject | Outcome |
|---|---|---|
| Q1 | Beacon/Orchard via PayHub | **Resolved** — both paid through PayHub, inside the 1099-K; Tessaro by bank transfer; 2.9% fee confirmed → lines 1 and 10 unchanged ($50,750.00 / $1,199.15) |
| Q2 | Activity after 2025-12-12 | **Unknown — no information offered**; figures end 12/12 (see Data gap above) |
| Q3 | 1,150 misc miles | **Partially resolved** — business character attested ("the rest is client stuff and the coworking space"); page 2 never provided → $805.00 of miles lacks per-trip support |
| Q4 | Phone / internet | **Resolved** — "maybe 60% work," no separate line → line 25 = 60% × $1,860.00 = $1,116.00 (flagged as an estimate) |
| Q5 | SF trip / Tartine; Denver & gift | **Partially resolved** — Denver flight + wedding gift confirmed personal; SF trip and its meals stand as drafted (no further information) |
| Q6 | MacBook business use | **Unknown — no information offered**; 100% business assumed ($2,149.00; each 10% personal = $214.90) |
| Q7 | Home office | **Unknown — no information offered**; none claimed (line 30 $0.00), rent stays personal, home→coworking miles stay excluded as commuting |
| Q8 | BCBS coverage | **Resolved** — her own policy after leaving Larkspur, not employer-subsidized; May–Dec premiums $3,040.00 stay on Schedule 1 line 17 |

## Citations used (all in `library/INDEX.md`)

- `schedule_c_instructions_excerpt.md` — IRS, 2025 Instructions for Schedule C (Lines 1, 9, 10, 13 de minimis, 15, 18, 20b, 24a/24b, 25, 27a; cash method; include-taxed-once rule)
- `schedule_se_excerpt.md` — IRS, Schedule SE (92.35%, 15.3%, $176,100 wage base, ½ deduction)
- `irs_notice_2025-5_standard_mileage.md` — Notice 2025-5 (70¢ business rate; commuting nondeductible §4)
- `pub463_commuting_meals.md` — IRS Pub. 463 (commuting, 50% meals, primarily-personal travel, home-office condition for daily transportation)
- `irc_262.md` — 26 U.S.C. §262(a) (personal/living expenses not deductible)

*Unverified beyond the library (stated per contract):* the self-employed-health-insurance eligibility limitation for months with employer-coverage availability (Schedule SEHI rule basis underlying Q8); no other authority is used.
