# Memorandum — Brightline Cabinetry LLC: Lone Star asset LOI vs. Hensley stock LOI

**To:** Ray Brightline
**From:** Tax comparison engagement
**Date:** October 26, 2026
**Re:** Lone Star Millwork Holdings LLC ($3,100,000 asset purchase LOI, March 30, 2026) vs. Hensley Family Partners LP ($2,850,000 membership-interest LOI, April 2, 2026) — after-tax comparison, Form 8594 allocation counter, and what your "$2.5M net" estimate missed.

**Sources.** Facts come only from your file: the two LOIs, the prior CPA's tax-history memo, the fixed-asset register, and your email. Law comes only from the reference library in this workspace (`library/INDEX.md` — seven items). Anything outside that library is labelled as an estimate, an inference, or unverified, and is not cited. Numbers to be confirmed are in `QUESTIONS.md`; none of them changes the ranking.

---

## 1. Bottom line

| | Lone Star as drafted | Lone Star with our counter allocation | Hensley stock sale |
|---|---:|---:|---:|
| Price / consideration | $3,100,000 | $3,100,000 | $2,850,000 |
| Ordinary income (37%) | $1,070,000 | $510,000 | $0 |
| Long-term capital gain (20%) | $1,450,000 | $2,010,000 | $2,430,000 |
| Shareholder-level tax | $685,900 | $590,700 | $486,000 |
| Entity-level §1374 tax (21%) | $237,300 | $237,300 | $0 |
| **Total tax** | **$923,200** | **$828,000** | **$486,000** |
| **Net after tax** | **$2,176,800** | **$2,272,000** | **$2,364,000** |

(Hensley's figure excludes the note's interest; the interest adds $56,700 after tax — Section 7.2. All figures are nominal and undiscounted; definitions in Section 1.2.)

**Hensley pays $250,000 less and leaves you $187,200 more than Lone Star as drafted — even before its note pays you interest.** Lone Star's own allocation is what makes its bigger price smaller: the $400,000 you would book to the non-compete is ordinary at 37%, and its $900,000 equipment line exceeds documented fair value, so all $660,000 of equipment gain is §1245 recapture at 37%. Fixing the allocation at the same $3,100,000 is worth $95,200 to you. Even then, Hensley still leads the repaired Lone Star deal by $92,000 — Hensley's structure avoids both the ordinary-income trap and the $237,300 entity-level tax outright.

### 1.1 The three things that drive the entire result

1. **Your S corporation is still inside the five-year built-in-gains recognition period.** The S election is effective January 1, 2023 (CPA memo), and the library states the recognition period is the "5-year period beginning with the first day of the first taxable year for which the corporation was an S corporation" (library: `irc_1374`). A 2026 closing is inside it. An asset sale by an S corporation in the period triggers a **corporate-level tax of $237,300** that a stock sale does not trigger at all — and you cannot reduce it by moving money between asset classes, because the law limits recognized built-in gain to each asset's built-in gain at the start of the period (Section 4).
2. **Lone Star's allocation manufactures ordinary income.** Under the library, covenant payments to a seller are ordinary income and recapture is ordinary (library: `irc_197_and_noncompete`, `irc_1245`, `stock_vs_asset_overview`). As drafted, $1,070,000 — 35% of the price — is taxed at 37% instead of 20%.
3. **Almost none of the price is sheltered by basis.** Your stock basis is $420,000 (CPA memo, as of 12/31/2025) and the company's aggregate inside asset basis is $580,000 (register equipment $240,000 + CPA-memo inventory $140,000 + receivables $200,000 if the receivables carry full basis — Section 3.1), against prices of $2.85M and $3.1M. And inside basis exceeds your outside basis by $160,000, which an asset sale largely wastes (Section 8.4).

### 1.2 What "net after tax" means here (and what it does not)

- Headline net = consideration minus (shareholder-level tax + entity-level §1374 tax), **nominal and undiscounted**.
- Hensley's note interest ($90,000 total, $56,700 after tax at 37%) is a return *on* the note, not on the deal; it is reported separately, not in the headline. Including it, Hensley's nominal net is $2,420,700.
- Excluded because the file gives no amounts: company liabilities (Lone Star's LOI §1 assumes only scheduled trade payables; Hensley assumes everything, known and unknown), the $100,000 Hensley escrow, and the 10% indemnity cap. These are risk items, not taxes — Sections 7.4 and 10.
- Your stock basis is assumed unchanged from 12/31/2025 to the closing date; the file gives no 2026 activity (QUESTIONS.md).

### 1.3 Recommendation (detail in Section 10)

Pursue Hensley at $2,850,000 — but use a corrected Lone Star allocation (Section 6) both to force Lone Star to pay for its defective exhibit and to make Hensley compete. Do not sign the Lone Star LOI as drafted. Do not give Hensley §338(h)(10)/§336(e) consent for free — a deemed asset sale at their price costs you $276,700–$387,200 (Section 7.5). And do not let the non-compete or consulting work become uncompensated ordinary income dressed up as part of the price.

---

## 2. Rates and the arithmetic conventions

All rates from the library (`capital_gain_rates.md`): ordinary income **37%**; long-term capital gain **20%**; the §1374 corporate tax is at the highest corporate rate, **21%** (library: `irc_1374` (b)(1)). **No Texas individual income tax** — the library states "Texas has no individual income tax" (`capital_gain_rates`); the CPA memo agrees. The CPA memo also notes "franchise tax applies to the entity" — the library contains no franchise-tax authority, so it is **not modeled** and is an open item (Section 11).

**The 3.8% net investment income tax is assumed not to apply.** The library's sentence is: "the 3.8% net investment income tax does **not** apply to gain from an active trade or business in which the taxpayer materially participates" (`capital_gain_rates`). That is conditioned on material participation; you have run this company since 2012, so we apply it as an assumption about your facts, not as a legal conclusion about your return. If it were held to apply, add 3.8% to the capital-gain rate — roughly $92,340 on the Hensley gain; it is in QUESTIONS.md.

Gain = amount realized minus adjusted basis; basis recovery is not taxed but reduces what is. That is the standard method; the library does not spell the formula out, so it is labelled as such wherever it does work (Sections 3, 8).

---

## 3. Character of each gain component, with authority

### 3.1 Receivables — $200,000; zero gain assumed, but the basis is an assumption

The CPA memo shows "receivables $200,000.00 (no reserve)." That is a book carrying value; **the file nowhere states their tax basis, and it nowhere states the company's method of accounting** (the fixed-asset register has no receivables line). Lone Star's LOI §1 lists receivables among the assets bought, and Exhibit A allocates the full $200,000 to Class III (the library's §1060 class list: "III mark-to-market assets and receivables").

**Base case (assumption, labelled):** basis = face = $200,000, so zero gain at either price.
**Sensitivity (labelled):** if the company keeps its books on the cash method, billed-but-uncollected receivables typically carry no tax basis, and the $200,000 would be **ordinary income when collected or on sale** — worth $200,000 × 37% = **$74,000** of extra tax. That would cut the counter allocation's net to $2,198,000 and widen Hensley's lead to $166,000. The accounting method is question 1 of `QUESTIONS.md`; it moves dollars, not the ranking.

### 3.2 Inventory — $150,000 as drafted; $10,000 of ordinary margin

CPA memo: "Inventory (materials) carrying value $140,000.00." Exhibit A allocates $150,000 (Class IV, the library's inventory class). The $10,000 excess over the $140,000 carrying value is ordinary income under the standard method (inventory is not a capital asset; also §1060's residual method itself puts inventory in its own class, and the library's §453 text confirms inventory sales are excluded from installment treatment, consistent with their ordinary character). $10,000 × 37% = $3,700 as drafted; we counter inventory at $140,000 (Section 6).

### 3.3 Equipment and vehicles — $900,000 as drafted vs. $650,000 documented FMV; all-ordinary under §1245

Register totals: cost $1,100,000, accumulated depreciation $860,000, adjusted basis **$240,000**, FMV estimate **$650,000**.

Library rule (`irc_1245`): on disposition of §1245 property, "the amount by which the lower of (A) the recomputed basis of the property, or (B) the amount realized, exceeds the adjusted basis of such property **shall be treated as ordinary income**," where "Recomputed basis = adjusted basis plus depreciation allowed or allowable."

- Recomputed basis = $240,000 + $860,000 = **$1,100,000**.
- As drafted: amount realized $900,000. Lower of (A) $1,100,000 and (B) $900,000 is $900,000. Ordinary income = $900,000 − $240,000 = **$660,000 — the entire gain, none of it capital gain.**
- At documented FMV $650,000: lower of $1,100,000 and $650,000 is $650,000; ordinary income = $650,000 − $240,000 = **$410,000**, saving ($660,000 − $410,000) × 17 points = **$42,500** (Section 6).
- Note the ceiling: every allocated dollar above $1,100,000 would have escaped recapture as capital gain. Lone Star chose $900,000 — below the ceiling, above your own FMV evidence, which maximizes ordinary income. That is not accidental and it is not "standard."

### 3.4 The non-compete — $400,000 as drafted; ordinary income, and attackable as overstated

Library (`irc_197_and_noncompete`): "A covenant not to compete entered into in connection with the acquisition of a trade or business is a section 197 intangible amortizable by the buyer over 15 years. **To the seller, payments for a covenant not to compete are ordinary income** (compensation for refraining from competing), not capital gain." So the drafted $400,000 (Class VI, which the library's §1060 list defines as "section 197 intangibles other than goodwill (including covenants not to compete)") is **$400,000 × 37% = $148,000** of tax instead of $80,000 — a $68,000 penalty at the drafted size.

The same library entry gives the attack: "Allocation between a covenant and goodwill must reflect economic reality; the parties' written allocation is binding on them (§1060(a); *Danielson* rule) absent strong proof, and the IRS may challenge it" (citing Rev. Rul. 69-643; *Muskat v. United States*, 554 F.3d 183 (1st Cir. 2009)). Three facts in your own file are the "strong proof" direction:

- The 2023 conversion appraisal values exactly two assets — goodwill/trade name $900,000 and equipment $610,000 — **no covenant value at all** (CPA memo table).
- Hensley's LOI §4 shows a market data point: "No non-compete payment; Seller signs a customary 3-year non-compete as part of the purchase agreement at no separate consideration." A second buyer is getting a 3-year covenant for nothing.
- Lone Star's clause §4 bundles the covenant with a **consulting** obligation ("5-year non-competition and consulting agreement; $400,000.00 of the price is allocated to it") — so the $400,000 is doing double duty and is very likely mis-sized in both directions.

Two-edged discipline follows: we counter the covenant **down** to $100,000 but not to $0 (Section 6.2), and **any consulting you actually perform is separately priced outside the purchase price** — consulting fees are compensation for services, an inference the library does not expressly state, but the point is protective either way: if the IRS re-characterized part of the covenant as services income you would get no capital treatment, and if you work for a year for nothing inside the price you have financed the deal twice.

### 3.5 Goodwill and the residual — Class VII, zero basis

Library §1060 rule: consideration is allocated among seven classes "in order" — I cash; II actively traded personal property; III mark-to-market assets and receivables; IV inventory; V all other assets (equipment, real property); VI §197 intangibles other than goodwill (including covenants); VII goodwill and going concern value — and "**Each class is allocated up to fair market value before moving to the next.**" Goodwill is the residual: everything the buyer pays above the earlier classes' FMV lands in Class VII.

Goodwill/trade-name adjusted basis at 1/1/2023 was **$0** (CPA memo appraisal table), so Class VII gain is capital gain in full at 20% (capital character of goodwill: library's asset-sale description assigns recapture and covenants to ordinary, leaving the balance as gain under the allocation; `stock_vs_asset_overview`). Each dollar moved out of over-filled ordinary classes into Class VII saves 17 points (37 − 20 cents).

### 3.6 Exhibit A, as drafted, cannot be filed — it violates the residual method twice

The library's rule caps each class at fair market value: "Each class is allocated up to fair market value before moving to the next" (`irc_1060_form_8594.md`).

1. **Class V is filled above FMV.** Exhibit A allocates $900,000 to equipment & vehicles; your own register says $650,000. The excess $250,000 is exactly the dollars Lone Star moved out of the goodwill residual to manufacture §1245 ordinary income.
2. **Class I is missing.** Exhibit A totals $3,100,000 across Classes III–VII only. There is no Class I line for cash in the company at closing. If the company holds any cash (QUESTIONS.md), Exhibit A is short by that amount and cannot balance a Form 8594 for a $3.1M purchase of assets plus whatever cash transfers.
3. Also note: Exhibit A's Class VII goodwill is $1,450,000, while the 2023 appraisal valued goodwill/trade name at $900,000. Growth to 2026 is plausible (this is the residual, so it absorbs whatever remains), but do not present the appraisal as "supporting" Exhibit A — it predates it and values goodwill $550,000 lower.

---

## 4. The §1374 built-in gains tax: $237,300 in every asset-sale scenario, and why you cannot allocate your way out of it

### 4.1 You are inside the recognition period

Library (`irc_1374`): "(a) If for any taxable year beginning in the **recognition period** an S corporation has a net recognized built-in gain, there is imposed a tax… (b)(1) The tax is the highest corporate rate (**21%**) on the net recognized built-in gain. (d)(7) The recognition period is the **5-year period beginning with the first day of the first taxable year for which the corporation was an S corporation.**"

The CPA memo: "Elected S corporation status effective January 1, 2023 (Form 2553 accepted)." Recognition period = **January 1, 2023 through December 31, 2027**. Any 2026 or 2027 closing is inside it.

### 4.2 The computation, capped at the conversion values

The library adds the ceiling that decides everything: "Recognized built-in gain on an asset is limited to the asset's built-in gain at the start of the recognition period" (`irc_1374`). The CPA's conversion appraisal fixed exactly that at 1/1/2023:

| Asset | FMV at 1/1/2023 | Adjusted basis at 1/1/2023 | Built-in gain (cap) |
|---|---:|---:|---:|
| Goodwill / trade name | $900,000 | $0 | $900,000 |
| Equipment & vehicles | $610,000 | $380,000 | $230,000 |
| Other | — | — | $0 |

(The appraisal was obtained by the prior CPA; the file does not name the appraiser. The register's 2026 equipment FMV of $650,000 exceeds the 2023 appraisal's $610,000 — irrelevant: the cap is frozen at 1/1/2023 values.)

Under **every** allocation tested in this memo, actual recognized gain in the capped assets exceeds their caps — equipment gain is $660,000 (drafted) or $410,000 (counter), both above $230,000; goodwill gain is $1,450,000 (drafted) or $2,010,000 (counter), both above $900,000. So:

**Net recognized built-in gain = $230,000 + $900,000 = $1,130,000. Entity tax = $1,130,000 × 21% = $237,300.**

(The library's §1374 text imposes the tax on "net recognized built-in gain" without spelling out the netting mechanics; taking the two capped asset amounts at face value is the straightforward reading and is labelled as such. Note also the C-corporation history — 2012 to 2022, elected "at the lender's request" (CPA memo). The library's period runs from the first S year with no C-carryover concept, so nothing is modeled from those years; QUESTIONS.md asks whether any pre-2023 items could affect the computation.)

### 4.3 Re-allocating price does **not** reduce this tax

The cap is per-asset at the start of the period, not a percentage of price. Shifting dollars between Classes IV, V, VI and VII changes your **shareholder-level** character (Section 6) but leaves the entity's $237,300 untouched — as drafted, countered, at covenant $0, or at any price from $2.85M to $3.4M tested here, both caps are fully absorbed. Corollary for negotiation: at the margin, extra price lands in the goodwill residual at 20% with **no additional §1374**, so every incremental dollar of Lone Star price nets you 80 cents.

### 4.4 The §1366(f)(2) credit — a genuine open question, kept out of the headline

The library's §1374 ends: "The tax paid is treated as a loss sustained by the S corporation (§1366(f)(2))." Read at face value, that $237,300 loss passes through to you and offsets your own gain, saving somewhere between $47,460 (if it shelters capital gain at 20%) and $87,801 (if ordinary at 37%). The library contains no §1366 text — no character, ordering, or timing rules — so we cannot verify how (or in what year) it actually applies to a one-year entity. **The headline treats the §1374 tax as a straight cash cost and this credit as an unverified sensitivity.** It does not change the ranking: the stock sale avoids the entity tax entirely, so the credit is worth something only on the Lone Star route.

### 4.5 The one clean escape: wait out the period — and its price

The recognition period ends 12/31/2027. A closing in 2028 pays **$0** §1374 tax: under the counter allocation your net would be $2,272,000 + $237,300 = **$2,509,300** — more than Hensley by $145,300 even before interest. That prices the lever at $237,300. It is commercially unrealistic with these buyers (Lone Star's LOI is cash-at-closing now; Hensley's note already starts in year 1), but it is worth knowing what you are conceding, and it is the only legally clean route around §1374 the file supports.

---

## 5. Lone Star as drafted: $2,176,800 net on a $3.1M price

Exhibit A (LOI A): III receivables $200,000 / IV inventory $150,000 / V equipment & vehicles $900,000 / VI non-compete $400,000 / VII goodwill $1,450,000 = $3,100,000, "to be reported consistently by both parties on IRS Form 8594" (LOI A §3; the library: "**Buyer and seller must each file Form 8594 and report consistently** with any written allocation agreement").

| Component | Allocated | Basis | Gain | Character | Tax |
|---|---:|---:|---:|---|---:|
| III Receivables | $200,000 | $200,000 (assumed) | $0 | — | $0 |
| IV Inventory | $150,000 | $140,000 | $10,000 | Ordinary | $3,700 |
| V Equipment & vehicles | $900,000 | $240,000 | $660,000 | Ordinary (§1245, Section 3.3) | $244,200 |
| VI Non-compete | $400,000 | $0 | $400,000 | Ordinary (§197/Rev. Rul. 69-643) | $148,000 |
| VII Goodwill (residual) | $1,450,000 | $0 | $1,450,000 | LTCG | $290,000 |
| **Shareholder subtotal** | | | $2,520,000 | $1,070,000 ord / $1,450,000 cap | **$685,900** |
| Entity §1374 (Section 4.2) | | | | | **$237,300** |
| **Total tax** | | | | | **$923,200** |
| **Net** | | | | | **$2,176,800** |

Arithmetic: 37% × $1,070,000 = $395,900; 20% × $1,450,000 = $290,000; $395,900 + $290,000 = $685,900; + $237,300 = $923,200; $3,100,000 − $923,200 = $2,176,800. Effective rate on price: 29.78%.

Note what you are also agreeing to: LOI A §4 puts **you** personally in a 5-year covenant *and* consulting obligation for a $400,000 allocation that is taxed at your worst rate; LOI A §1 makes you deliver the receivables (Section 3.1 sensitivity); and Exhibit A as filed would be a written allocation "binding on them" (library: `irc_197_and_noncompete`) against the IRS for both parties. LOI A §5 makes the LOI "Non-binding except confidentiality and exclusivity (45 days)" — non-binding terms, but the exclusivity may already bind you alone (Section 10.1).

---

## 6. The counter allocation: +$95,200 at the same price, and what each line is worth

### 6.1 The counter (full justification and filing mechanics in `form_8594_counter.md`)

| Class | Line | Exhibit A | **Counter** | Basis | Gain | Character |
|---|---|---:|---:|---:|---:|---|
| III | Receivables | $200,000 | $200,000 | $200,000 (assumed) | $0 | — |
| IV | Inventory | $150,000 | $140,000 | $140,000 | $0 | — |
| V | Equipment & vehicles | $900,000 | $650,000 | $240,000 | $410,000 | Ordinary in full |
| VI | Non-compete | $400,000 | $100,000 | $0 | $100,000 | Ordinary |
| VII | Goodwill (residual) | $1,450,000 | $2,010,000 | $0 | $2,010,000 | LTCG |
| | **Total** | $3,100,000 | **$3,100,000** | | $2,520,000 | $510,000 ord / $2,010,000 cap |

Tax: 37% × $510,000 = $188,700; 20% × $2,010,000 = $402,000; shareholder $590,700; entity §1374 $237,300 (unchanged — Section 4.3); total $828,000; **net $2,272,000**. **Gain: $2,272,000 − $2,176,800 = $95,200.**

The arithmetic identity: every dollar moved from Class IV/V/VI into the Class VII residual moves from 37% to 20% — **17 points** — and triggers no extra §1374 because both caps are already fully absorbed:

| Fix | Dollars | Value (17%) |
|---|---:|---:|
| Equipment $900,000 → $650,000 (your own register's FMV) | $250,000 | $42,500 |
| Covenant $400,000 → $100,000 (economic-reality rule, Section 3.4) | $300,000 | $51,000 |
| Inventory $150,000 → $140,000 (CPA carrying value) | $10,000 | $1,700 |
| **Total** | | **$95,200** |

### 6.2 Why covenant $100,000 and not $0

$0 is the economically honest number against the appraisal and the Hensley datapoint, and it is worth the most: covenant at $0 yields ordinary $410,000, capital $2,110,000, tax $573,700 + $237,300 = $811,000, **net $2,289,000** (+$112,200 vs. drafted). But a signed exhibit that pays you **nothing** for a 5-year covenant you refuse to walk away from invites exactly the re-characterization the library warns about: the written allocation is binding absent "strong proof" and the IRS may challenge an allocation that does not reflect economic reality (`irc_197_and_noncompete`). A deal with a 5-year covenant and literally zero allocated to it is the classic fact pattern for the IRS to pull dollars out of goodwill into ordinary income — with interest — on an allocation you signed. **Counter at $100,000 (judgement, labelled), concede toward $0 only in exchange for price, and never below a token real number.** Tier map (same equipment and inventory lines throughout):

| Covenant | Ordinary | Capital | Total tax | Net |
|---:|---:|---:|---:|---:|
| $0 | $410,000 | $2,110,000 | $811,000 | $2,289,000 |
| $100,000 | $510,000 | $2,010,000 | $828,000 | $2,272,000 |
| $400,000 (drafted) | $1,070,000 | $1,450,000 | $923,200 | $2,176,800 |

Each $100,000 of covenant costs you $17,000. That is the price of the risk shield — say so out loud when you negotiate it.

### 6.3 What Lone Star's concessions are actually worth to them (know your trading currency)

Your allocation fixes shift roughly $550,000–$650,000 of buyer amortization between classes but change **nothing** in what Lone Star pays — its cost is only the *timing* of its own deductions (equipment depreciates faster than 15-year §197/goodwill amortization). At a 21% corporate rate the gross shield on the $250,000 equipment reduction is $52,500, and its present-value timing edge is only on the order of $13,000–$15,000 (illustrative: 7-year recovery vs. 15-year, half-year convention, 8–12% discount; **MACRS schedules and PV math are not in the library — directional estimate only**). So: fixing Exhibit A to your own documented FMV costs Lone Star pocket change; you should not "pay" for it with price. The $400,000→$100,000 covenant cut genuinely *helps* Lone Star's optics too (it is their exhibit that violates the FMV rule they want you to sign). The trade to propose: **their exhibit corrected, your signature this week, price unchanged** — and if they insist on keeping Exhibit A as drafted, the fallback is price: $95,200 ÷ 0.80 = **+$119,000** (each extra dollar nets 80 cents — Section 4.3) restores your $2,272,000 at $3,219,000.

### 6.4 Parity prices — what Lone Star must pay to beat Hensley (all net-80¢, §1374 flat)

Measured against Hensley's clean stock net of $2,364,000 (before note interest; add $70,875 of price per $56,700 of interest you value):

| Lone Star structure | Net at $3,100,000 | Price needed to match $2,364,000 |
|---|---:|---:|
| Exhibit A as drafted | $2,176,800 | $3,334,000 (+$234,000) |
| Counter allocation | $2,272,000 | $3,215,000 (+$115,000) |
| Counter with covenant at $0 | $2,289,000 | $3,193,750 (+$93,750) |

<!--APPEND-MARKER-->
