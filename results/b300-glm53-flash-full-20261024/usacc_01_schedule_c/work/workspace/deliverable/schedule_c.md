# Schedule C (Form 1040) — 2025 — Explanations and Computation

**Taxpayer:** Dana A. Okafor (single, TX) — **Business:** Dana Okafor Design, freelance UX design, sole proprietorship
**Accounting method:** Cash. **Tax year:** 2025.
**Sources:** client bank export 12/2024–12/12/2025 (149 transactions; reconciles exactly to the export header: credits 72,053.65 / debits 43,308.83 / ending 32,955.15), Forms 1099-K (PayHub) and 1099-NEC (Beacon, Orchard, Tessaro), Form W-2 (Larkspur), Dana's mileage notebook, and Dana's email answers. All regulation citations are to the files listed in `workspace/library/INDEX.md` only; anything outside that library is labeled **unverified** in the notes below.

**Headline results:** Line 1 gross receipts **$50,750.00**; total expenses (line 28) **$10,962.43**; net profit (line 31) **$39,787.57**. Schedule SE tax **$5,621.80**, deductible half **$2,810.90**.

---

## Line 1 — Gross receipts: $50,750.00

Two verified income streams, combined:

| Source | Amount | Derivation |
|---|---|---|
| PayHub third-party settlement organization (Form 1099-K) | **41,350.00** | 1099-K box 1a as issued |
| Tessaro Studios (Form 1099-NEC, direct ACH) | **9,400.00** | Bank ACH credits 3/19 $2,400.00 + 6/19 $3,100.00 + 9/19 $2,150.00 + 11/19 $1,750.00 = **9,400.00** — agrees exactly with the 1099-NEC |
| **Line 1** | **$50,750.00** | 41,350.00 + 9,400.00 |

**Deduplication of the Beacon and Orchard 1099-NECs (why $81,450 was rejected).** Mechanically summing all four forms gives 41,350.00 + 18,500.00 + 12,200.00 + 9,400.00 = $81,450.00, but the Schedule C instructions state that *"If the same payment is reported to you on more than one information return … include the amount only once."* Dana confirmed in email: *"Beacon and Orchard both pay me through PayHub. Tessaro pays by bank transfer."* The Beacon ($18,500.00) and Orchard ($12,200.00) payments were therefore processed through PayHub and are already inside the 1099-K figure; adding them again would double-count $30,700.00. Line 1 = $50,750.00.

**Prior-year receipt excluded.** An ACH credit from Tessaro Studios ("INV 1041") of $3,000.00 was received **12/27/2024**. Under the cash-method rule in the Schedule C instructions — *"A payment received in December of the prior year belongs to the prior year's return"* — it belongs on the 2024 return and is excluded here.

**Cross-check of the 1099-K gross against bank deposits.** The eleven 2025 PayHub payout deposits (2/6 through 12/7) sum to $40,150.85. The 1099-K represents amounts at **gross**, before the processor retained its fee: 40,150.85 ÷ 0.971 = **41,350.00**, exactly the 1099-K figure. (0.971 = 1 − 2.9% processor fee.) Gross is reported on line 1; the retained fee is deducted on line 10, not netted against line 1.

## Line 9 — Car and truck expenses: $183.40

Standard mileage rate method per Notice 2025-5: **70 cents per mile** for business use in 2025 — the rate Dana's mileage notebook references ("0.655") is the **2023** rate (65.5¢), which does not apply.

**Supported business miles** (mileage notebook entries with a stated business destination):

| Date (2025) | Purpose per log | Miles |
|---|---|---|
| Jan 6 | Client kickoff — Beacon (downtown) | 14 |
| Feb 12 | Orchard Health — Round Rock | 38 |
| Mar 3 | Print shop — mockups | 11 |
| Apr 29 | Beacon — design review | 14 |
| Jun 2 | Tessaro — Dripping Springs | 58 |
| Jul 15 | Orchard Health — Round Rock | 38 |
| Aug 21 | Camera rental — North Austin | 22 |
| Nov 11 | Tessaro — Dripping Springs | 58 |
| Dec 3 | Office supplies run | 9 |
| | **Total supported** | **262** |

**Computation:** 262 miles × $0.70 = **$183.40**. Purposes are quoted from the log. The Mar 3 print-shop, Aug 21 camera-rental, and Dec 3 office-supplies trips are business errands — not client-site visits and not commuting — included under Notice 2025-5's 70¢-per-mile rate for business use.

Arithmetic check against the notebook's own total: supported 262 = log total 4,860 − 1,200 (Larkspur commuting) − 936 (coworking May–Aug) − 1,296 (coworking Sep–Dec) − 1,150 (misc pg 2) − 16 (client dinner). ✓

**Miles excluded from the deduction:**
- **1,200 miles Jan–Apr** — Dana confirmed these were daily drives to the Larkspur office: *"That's commuting."* Commuting is not business use (Schedule C instructions line 9; Notice 2025-5 §4; Pub. 463).
- **2,232 miles of commute to Capital Factory (936 for May–Aug + 1,296 for Sep–Dec, per the log)** — Pub. 463 allows daily transportation between home and another work location only *if the home office qualifies as a principal place of business*. No qualifying home office has been established (see open item), and no office-in-home deduction is claimed, so these miles are excluded.
- **1,150 miles logged as "misc (see pg 2)"** — page 2 of the notebook is missing and Dana provided no further information; the business character of these miles cannot be supported, so they are conservatively **excluded** (open item).
- **16 miles (Oct 20, client dinner)** — driving to a business meal is not addressed anywhere in the reference library (**unverified rule**); no matching meal purchase exists in the bank export. Excluded conservatively.

## Line 10 — Commissions and fees: $1,199.15

PayHub retained its processing fee before remitting each payout. Computation: 1099-K gross 41,350.00 − deposits received 40,150.85 = **$1,199.15** (exactly 2.9% of gross). Corroborated at the monthly level from the 1099-K itself: February monthly-detail box 5b 1,866.68 − February payout deposit 1,812.55 = 54.13 = 2.9% of 1,866.68. ✓ The Schedule C instructions explicitly allow this deduction on line 10 and require it *not* be netted against line 1.

## Line 13 — Depreciation and §179: $0.00

The MacBook Pro 14" purchased 9/14/2025 for **$2,149.00** is at or below the **$2,500 de minimis safe harbor** threshold (per invoice/item). Per the Schedule C instructions, it is expensed in full under the appropriate category — here **line 27a** — with the **election statement attached to the return**, rather than depreciated. Nothing is claimed on line 13. **Open item:** Dana gave no business-use percentage for the laptop; 100% business use is **assumed** and flagged prominently below.

## Line 15 — Insurance (other than health): $480.00

Hiscox professional liability policy premium, charged 2/20/2025: **$480.00** — business insurance within the meaning of line 15. Per the instructions, health insurance is **not** deducted here; Dana's Blue Cross Blue Shield premiums are handled on Schedule 1 line 17 instead (see "Not on Schedule C").

## Line 18 — Office expense: $0.00

No purchase of office supplies or postage can be identified in the bank export. The mileage log shows a 9-mile "Office supplies run" on Dec 3 — counted in line 9's 262 supported miles as a business errand — but every bank debit dated 12/3–12/5 is a recurring subscription (Figma 12/3, Adobe 12/4, Netflix 12/5); no discrete supplies purchase appears, and Dana provided none on request. Mileage for the errand stands on the log alone; a supplies *purchase* requires evidence of a purchase, so nothing is claimed on line 18.

## Line 20b — Rent — other business property: $2,800.00

Capital Factory coworking membership: $350.00 per month × 8 months (May–December 2025) = **$2,800.00**, matching the bank export charge-for-charge. Coworking memberships are rent for other business property under line 20b. **Note:** only 8 months of charges appear (May 8 – Dec 8), with no gap or doubled month. The mileage log's coworking entries likewise begin in May, independently matching the start month of the charges. Dana was asked whether the membership ran before May and gave no answer (Q9), so nothing is claimed for January–April.

## Line 24a — Travel: $1,030.00

DesignWeek SF conference, October 2025 (away-from-home overnight business travel):

| Item | Date | Amount |
|---|---|---|
| Southwest 526 AUS→SFO airfare | 10/2 | **412.00** |
| Hotel Zephyr, San Francisco (lodging) | 10/6 | **618.00** |
| **Line 24a** | | **$1,030.00** |

The 6/13 Southwest AUS→DEN flight of $389.00 is **excluded**: Dana confirmed it was her cousin's wedding ("nothing work-related") — primarily personal travel is not deductible even if some business is conducted (Pub. 463). It also matches the adjacent Venmo wedding-gift payment.

## Line 24b — Deductible meals: $95.00

Two meals on the DesignWeek trip, deductible at **50%** (Pub. 463; Schedule C instructions line 24b):

| Item | Date | Charged | × 50% |
|---|---|---|---|
| SQ *Marina Deli, San Francisco | 10/7 | 64.00 | **32.00** |
| Tartine Manufactory, San Francisco | 10/8 | 126.00 | **63.00** |
| **Line 24b** | | 190.00 | **$95.00** |

## Line 25 — Utilities: $1,116.00

Business portion of telephone and internet. Annual charges from the bank export: T-Mobile wireless 85.00 × 12 = **1,020.00**; Spectrum home internet 70.00 × 12 = **840.00**. Dana estimates 60% business use for both ("Phone and internet are maybe 60% work? I don't have a separate line."). There is no second/dedicated work line.

- T-Mobile: 1,020.00 × 60% = **612.00**
- Spectrum: 840.00 × 60% = **504.00**
- **Line 25 = $1,116.00**

**Two flags:**
1. **The 60% is Dana's estimate with no usage log**, while the instructions call for *"a reasonable, documented business-use percentage."* It is claimed on Dana's representation and flagged as an estimate; Dana should keep a usage log going forward.
2. **Interpretation of the "first line" carve-out.** The instructions say the cost of *"basic local telephone service for the first line into your home"* is not deductible. We read that as referring to a basic local (landline) service; Dana's T-Mobile plan is a **wireless** plan, and Dana has no landline. Under that reading, the phone line is deductible at its business-use percentage. **If this reading is wrong, the phone portion ($612.00) would instead be $0** — flagged.* (The internet line is unaffected by the carve-out in any reading.)

## Line 27a — Other expenses: $4,058.88

| Item | Date | Amount |
|---|---|---|
| Figma subscription, 45.00 × 12 | Jan–Dec | **540.00** |
| Adobe Creative Cloud, 59.99 × 12 | Jan–Dec | **719.88** |
| MacBook Pro 14" — de minimis safe harbor (see line 13) | 9/14 | **2,149.00** |
| DesignWeek SF conference registration | 10/6 | **650.00** |
| **Line 27a** | | **$4,058.88** |

The instructions list software subscriptions, professional development, and de minimis safe harbor items as line 27a contents. The MacBook deduction rests entirely on the **stated assumption of 100% business use**: no usage record exists and Dana provided none (see stated assumptions).

## Line 28 — Total expenses: $10,962.43

 183.40 (line 9)
 + 1,199.15 (line 10)
 + 480.00 (line 15)
 + 2,800.00 (line 20b)
 + 1,030.00 (line 24a)
 + 95.00 (line 24b)
 + 1,116.00 (line 25)
 + 4,058.88 (line 27a)
 = **$10,962.43** (lines 8, 13, 18, 19, 26, 27 other than 27a on Part II are $0.00 as explained above)

**Tie-out to the bank export.** Cash charged in the export for items classified business = $8,558.88. Bridge to line 28: 8,558.88 + 1,199.15 processor fees retained before deposit (never touched the bank account) + 183.40 mileage (no cash charged) − 95.00 (meals charged 190.00 but deductible at 50%) + 1,116.00 (telephone/internet charged $1,860.00 but only the 60% business share deducted) = **10,962.43** ✓

**Full export reconciliation (all 149 rows classified, both directions).** Credits 72,053.65 = net payroll deposits 19,502.80 (2,437.85 × 8) + PayHub payouts 40,150.85 + Tessaro 2025 ACH 9,400.00 + prior-year Tessaro 3,000.00 (received 12/27/2024). Debits 43,308.83 = business items charged 8,558.88 + federal ES payments 6,500.00 + BCBS premiums 3,040.00 + T-Mobile 1,020.00 + Spectrum 840.00 + home rent 19,800.00 + Netflix 185.88 + Orangetheory 588.00 + 2025 H-E-B groceries 2,102.95 + the single 2024 H-E-B row 84.12 (12/30/2024) + Denver flight 389.00 + wedding gift 200.00. Beginning balance 4,210.33 + 72,053.65 − 43,308.83 = ending 32,955.15 ✓ — the header ties on both sides, confirming `classification.csv` accounts for 100% of the export's rows and dollars.

## Line 31 — Net profit: $39,787.57

50,750.00 − 10,962.43 = **$39,787.57** — the figure the Schedule SE excerpt uses as "net profit from Schedule C." The specific Schedule 1 line that carries it onto Form 1040 is not stated in the reference library (**unverified**), so no line number is asserted here.

---

## Schedule SE (from the Schedule SE excerpt, 2025)

| Step | Computation | Amount |
|---|---|---|
| Net earnings from self-employment | 39,787.57 × 92.35% (0.9235) | **36,743.82** |
| Self-employment tax | 36,743.82 × 15.3% | **5,621.80** |
| One-half of SE tax (Schedule 1, line 15) | 5,621.80 ÷ 2 | **2,810.90** |

**Wage-base check (no proration needed).** W-2 social security wages from Larkspur: $24,800.00. 24,800.00 + 36,743.82 = $61,543.82 ≤ $176,100 wage base → the full 12.4% social security portion plus 2.9% Medicare applies, i.e., the whole 15.3%.

## Items NOT on Schedule C (and where they belong)

| Item | Amount | Where it belongs |
|---|---|---|
| Larkspur W-2 wages (gross, Jan–Apr 2025) | 24,800.00 | Form 1040, line 1a (employment income; never Schedule C) |
| W-2 federal income tax withheld | 2,310.00 | Form 1040, line 25a (payment) |
| W-2 box 12a DD — dependent care benefits | 1,960.00 | Form 2441 if qualifying care — **unverified**; no qualifying dependent confirmed in file |
| BCBS health premiums, 380.00 × 8 (May–Dec) | 3,040.00 | Schedule 1, line 17 — self-employed health insurance. Explicitly **not** line 15 per the instructions; Dana confirmed her own plan, not employer-eligible |
| One-half of SE tax | 2,810.90 | Schedule 1, line 15 |
| 2025 federal estimated payments (1,500 + 2,500 + 2,500) | 6,500.00 | Form 1040, line 26 (payments; not an expense) |
| Tessaro INV 1041 received 12/27/2024 | 3,000.00 | Prior year (2024 return) — cash method |
| Home rent (Zelle, 1,650.00 × 12) | 19,800.00 | Personal — §262(a); no home-office deduction claimed, so no allocation |
| Denver flight 6/13 | 389.00 | Personal — Pub. 463 (wedding trip, client-confirmed) |
| Wedding gift (Venmo) | 200.00 | Personal — §262(a) |
| Groceries (H-E-B ×12) | 2,102.95 | Personal — §262(a) |
| Netflix (15.49 × 12) | 185.88 | Personal — §262(a) |
| Orangetheory (49.00 × 12) | 588.00 | Personal — §262(a) |
| Personal 40% of phone/internet | 744.00 | Personal — remains after the line 25 allocation |

**Labeling of form placements.** The library contains none of Form 1040, Form 2441, or Form 8829, so placements such as "Form 1040 line 1a / 25a / 26," the Form 2441 reference above, and the Form 8829 reference in the open-items section are standard-form convention — **not library-verified** (the amounts themselves are from the file). Likewise, the library only *redirects* health premiums to Schedule 1 line 17; any eligibility conditions for that deduction (employer-coverage status, net-earnings limit) are outside the library (**unverified**), and no deduction rests on them beyond Dana's confirmation that her plan is not employer-based.

Per-row detail for every one of the 149 bank transactions is in `classification.csv`.

---

## Stated assumptions (prominent, per the engagement terms)

1. **MacBook business use = 100%.** Dana was asked and answered "no additional information." There is no contemporaneous usage record. This is an **assumption**, not a supported fact; the $2,149.00 line 27a item would shrink pro-rata if actual business use is lower.
2. **Phone/internet business use = 60%.** Dana's own estimate, not documented; see line 25.
3. **Capital Factory membership treated as 100% Dana's business expense** (no evidence of shared/subsidized membership in the file).
4. **Hiscox premium treated as 100% business** — the policy (purchased 2/20/2025) is for the design practice; the policy declaration is not in the file.
5. **The "first line into your home" carve-out is read as limited to basic local landline service** — see line 25, item 2 (flagged there).

## Open items (client could not answer; none answers arrived)

- **Revenue after 12/12/2025 unverified:** the bank export's label says it extends to 1/31/2026, but the last transaction is 12/12/2025. No 1099-K covers 12/13–12/31 payouts after the 12/7 payout. Dana gave no additional information; **no income is assumed for 12/13–12/31.**
- **"Misc" mileage, 1,150 miles (log page 2 missing):** excluded from line 9; would add ~$805.00 at 70¢/mi if later substantiated as business.
- **Coworking commute, 2,232 miles:** excluded as commuting; would become deductible daily transportation (and Form 8829 would open) **only** if a qualifying principal-place-of-business home office is established.
- **Client-dinner miles (Oct 20, 16 miles):** excluded; the meal-transport rule is not in the reference library (**unverified**) and no meal expense exists in the bank data.
- **De minimis safe harbor election statement** for the MacBook ($2,149.00) must be attached to the return.
- **W-2 box 12a DD $1,960.00:** Form 2441 applicability unverified (no dependent information in file).
- **Phone/internet usage log:** recommend Dana begin contemporaneously logging business use to support the 60%.

*Nothing outside `workspace/library/` has been relied on for any conclusion; items marked unverified above were treated conservatively (excluded) rather than deducted.*
