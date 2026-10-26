# Memo — Should Ray sign Buyer A's LOI? The real after-tax comparison

**Prepared for:** Ray Brightline · Brightline Cabinetry LLC
**Date:** October 2026 · **Subject:** Lone Star asset offer ($3,100,000) vs Hensley stock offer ($2,850,000)

---

## 1. The short answer

Ray's plan to sign Buyer A "because $3.1M > $2.85M" compares gross prices. After tax, the story reverses:

| | Buy­er A — asset sale, as drafted | Buy­er A — asset sale, counter allocation | Buy­er B — stock sale |
|---|---:|---:|---:|
| Gross price | 3,100,000.00 | 3,100,000.00 | 2,850,000.00 |
| Entity-level tax (§1374 BIG) | (237,300.00) | (237,300.00) | — |
| Personal tax | (630,229.00) | (535,029.00) | (486,000.00) |
| **Net after tax (nominal)** | **2,232,471.00** | **2,327,671.00** | **2,364,000.00** |
| vs Ray's naive estimate (2,480,000) | −247,529 | −152,329 | −116,000 |

- Buyer B's "smaller" $2.85M offer beats Buyer A's drafted asset deal by **131,529.00** in nominal after-tax dollars — and more once the installment note's timing is counted (§ 6).
- Ray's naive estimate ($2.48M) is high for every structure. It assumes all-capital gain at 20% and no entity-level tax. In Buyer A's drafted deal, **$1,070,000 — 34.5% of the price — is ordinary-rate income, and the S corporation itself owes $237,300 of §1374 built-in-gains tax** before anything reaches him.
- Recommendation: **do not sign Buyer A as drafted.** Either (a) sign Buyer A only with the counter allocation in `form_8594_counter.md` (+95,200 to Ray), or (b) take Buyer B — which remains ahead even before any price renegotiation — or renegotiate B's price up using A's $3.1M as leverage. The counters in § 8.

## 2. Facts used

From `documents/tax_history_and_conversion.md`: Texas LLC elected C-corp taxation 2012, **S election effective 1/1/2023** with an appraisal showing built-in gain of goodwill/trade name **900,000** (basis 0) and equipment/vehicles **230,000** (FMV 610,000, basis 380,000). Ray's stock basis **420,000** (12/31/2025). No NOLs. Inventory 140,000, receivables 200,000 (no reserve), both carried at value as of the engagement file.
From `documents/fixed_asset_register.csv`: equipment & vehicles adjusted basis **240,000**, accumulated depreciation **860,000** (recomputed basis 1,100,000), current FMV **650,000**.
From the two LOIs (prices, terms, Buyer A's Exhibit A). From `email_ray.txt`: Ray's intent and naive math.

## 3. Buyer A — asset sale as drafted: character of each gain component

Buyer A Exhibit A allocates the $3,100,000: Class III receivables 200,000 · Class IV inventory 150,000 · Class V equipment & vehicles 900,000 · Class VI 5-yr non-compete 400,000 · Class VII goodwill 1,450,000. Under the residual method the written allocation binds the parties (§1060; *Danielson*-type rule, `library/irc_1060_form_8594.md`, `library/irc_197_and_noncompete.md`), so each class is analyzed as written.

**(a) Receivables — Class III, 200,000 → gain: 0.00.** Face value equals basis (no reserve), sold at face. No gain, no tax.

**(b) Inventory — Class IV, 150,000 → gain 10,000.00 ordinary.** Carrying value 140,000. Inventory gain is ordinary income; the installment method is not available for it (`library/irc_453_installment.md`).

**(c) Equipment & vehicles — Class V, 900,000 → 660,000.00 ordinary under §1245.** Adjusted basis 240,000; recomputed basis (basis + depreciation allowed) 1,100,000. §1245(a)(1) treats as ordinary income the excess of **the lower of recomputed basis (1,100,000) or amount realized (900,000)** over adjusted basis: 900,000 − 240,000 = **660,000 ordinary**; there is no capital gain in this class because the amount realized never exceeds recomputed basis (`library/irc_1245.md`). Itemizing by FMV would not change the class result here — every item's gain sits inside its own accumulated depreciation.

**(d) Non-compete — Class VI, 400,000 → 400,000.00 ordinary.** Payments to the seller for a covenant not to compete are **ordinary income**, never capital gain (`library/irc_197_and_noncompete.md`, citing Rev. Rul. 69-643 and *Muskat*). The client has confirmed the 400,000 is entirely the 5-year restraint payment — no services component — payable with the closing price. Because the covenant is Ray's personal agreement, this 400,000 is paid to Ray himself, on top of the corporation's proceeds. (Ray is indifferent to the label as long as the total is unchanged, which the counter in `form_8594_counter.md` honors.)

**(e) Goodwill / trade name — Class VII, 1,450,000 → capital gain.** The library's overview treats only recapture and covenant payments as ordinary, so goodwill gain is capital (`library/stock_vs_asset_overview.md`). Character as long-term capital gain at 20% follows (`library/capital_gain_rates.md`). The underlying statutes for goodwill-as-capital-asset (§1221/§1231) are **not in the library — flagged as unverified beyond the overview.**

**Character summary (as drafted):** ordinary 10,000 + 660,000 + 400,000 = **1,070,000** (34.5% of price, taxed 37%); capital **1,450,000** (20%).

## 4. The §1374 built-in-gains tax — the item Ray's buddy missed

The S election took effect 1/1/2023, so the **recognition period runs 1/1/2023 through 12/31/2027** (`library/irc_1374.md`, §1374(d)(7)). A 2026 closing falls inside it. The corporation's net recognized built-in gain in the closing year is taxed at the **21% corporate rate**, with each asset's recognized gain limited to its built-in gain at the start of the period:

| Asset | Recognized gain (as drafted) | BIG ceiling at 1/1/2023 | Included in NRIG |
|---|---:|---:|---:|
| Goodwill / trade name | 1,450,000 | 900,000 | 900,000 |
| Equipment & vehicles | 660,000 | 230,000 | 230,000 |
| Inventory / receivables | 10,000 / 0 | 0 | 0 |
| **Total NRIG** | | | **1,130,000** |

**Entity-level tax = 21% × 1,130,000 = 237,300.00**, paid out of the corporation's share of the price — i.e., out of Ray's pocket.

## 5. Ray's personal tax — asset sale as drafted

The BIG tax is "treated as a loss sustained by the S corporation" (`library/irc_1374.md`, citing §1366(f)(2)), which reduces Ray's flow-through. **Assumption (stated because the library does not fix the loss's character):** the loss is allocated to Ray in proportion to the NRIG sources — 189,000 against capital (goodwill) and 48,300 against ordinary (equipment), i.e., 237,300 × (900/1,130 and 230/1,130). Alternate characterings move the personal tax by +8,211 / −32,130 (see § 9, open items).

| Step | Ordinary | Capital |
|---|---:|---:|
| Company gain | 670,000 (inv 10,000 + §1245 660,000) | 1,450,000 |
| Less §1366(f)(2) loss share | (48,300) | (189,000) |
| Plus Ray's personal covenant income | 400,000 | — |
| **Taxable to Ray** | **1,021,700** | **1,261,000** |
| **Tax** | **378,029.00** (37%) | **252,200.00** (20%) |

Personal tax 630,229.00 + entity tax 237,300.00 = **867,529.00** · Net = 3,100,000 − 867,529 = **2,232,471.00**. The arithmetic ties: 867,529 + 2,232,471 = 3,100,000.

## 6. Buyer B — stock sale, and the installment note

The buyer purchases 100% of the membership interests; the company survives and keeps its assets and liabilities. Ray's gain = price − stock basis = 2,850,000 − 420,000 = **2,430,000 capital**, taxed at 20% = **486,000** (`library/stock_vs_asset_overview.md`; `library/capital_gain_rates.md` — the 3.8% NIIT does not apply to gain from an active business in which Ray materially participates; Texas has no individual income tax). **No §1245 recapture** (no asset disposition) and **no §1374 entity tax** (the corporation itself recognizes nothing on a stock sale).

**The 500,000 note (5 yr, 6%, annual principal)** is an installment sale under §453 (`library/irc_453_installment.md`): gain is recognized proportionately as payments are received. Gross-profit ratio = 2,430,000 ⁄ 2,850,000 = 0.852632.

| Anni­versary | Payments | Gain recognized | Tax on gain (20%) | Interest received | Tax on interest (37%) |
|---|---:|---:|---:|---:|---:|
| Closing (yr 0) | 2,350,000 cash | 2,003,684.21 | 400,736.84 | — | — |
| Note yr 1 | 130,000 | 85,263.16 | 17,052.63 | 30,000 | 11,100 |
| Note yr 2 | 124,000 | 85,263.16 | 17,052.63 | 24,000 | 8,880 |
| Note yr 3 | 118,000 | 85,263.16 | 17,052.63 | 18,000 | 6,660 |
| Note yr 4 | 112,000 | 85,263.16 | 17,052.63 | 12,000 | 4,440 |
| Note yr 5 | 106,000 | 85,263.16 | 17,052.63 | 6,000 | 2,220 |
| **Total** | 2,940,000 | 2,430,000.00 | 486,000.01 | 90,000 | 33,300 |

(Annual gain = 100,000 principal × 0.852632 = 85,263.16; the five note-year rows plus the closing row sum to 2,430,000.00, so tax sums to 486,000.00 up to 0.01 rounding. Interest totals 90,000 beyond the 2,850,000 price and is ordinary.)

Two things the note does that the drafted asset deal cannot: it **defers tax** (year-1 capital-gain tax is 400,736.84, not 486,000), and it is additional consideration (interest) for waiting. At an illustrative 5% discount rate, the present value of the capital-gain tax is ≈ 455,486 (vs 486,000 undiscounted) and of the tax on the note's interest ≈ 29,771 (vs 33,300) — **a timing benefit on the order of $34,000**. The discount rate is an assumption, not library authority.

Risks of the note that Buyer A's all-cash deal lacks: it is **unsecured** — Ray bears Hensley Family Partners LP's credit risk for five years — and §453B-type accelerations on default are outside the library (unverified). A §453A interest charge on deferred sales exists in the statute but is **not in the library; unverified** — nothing here suggests it applies at this size, but flag for the CPA. §453's unavailability for inventory and depreciable-property sales to related persons does not affect an unrelated stock buyer.

## 7. Liability and risk differences

- **Buyer A (asset):** assumes only scheduled trade payables; Ray's entity keeps everything else but converts the sale price to cash at closing — no collection/credit risk, but the 12-month window for closing-schedule disputes is not specified in the LOI (question for counsel).
- **Buyer B (stock):** buyer inherits **all liabilities, known and unknown**, with only a 12-month indemnity capped at **10% of price (285,000)** plus a **100,000 escrow**. An unknown liability surfacing in year two lands on Hensley, not Ray — cheap insurance for Ray, which is precisely why the stock price can be lower. The §1374 recognition period keeps protecting the buyer after closing (armor against the BIG tax until 12/31/2027 stays inside the company — with no asset sale, nothing triggers it).

## 8. Negotiating position

1. **With Buyer A:** refuse Exhibit A as drafted; sign only with the counter allocation (`form_8594_counter.md`). Worth **+95,200.00** to Ray with zero change in the headline price and no change in the buyer's 15-year amortization on the shifted intangibles. The Class V request at FMV (650,000) is hard for the buyer's CPA to defend against the residual method (`library/irc_1060_form_8594.md`); the Class VI request (100,000 vs 400,000) is aggressive but §197 amortization is identical for either label, so push hard (`library/irc_197_and_noncompete.md`). Also hand Buyer A the §1374 table (§ 4): they are buying inside the recognition period, so Exhibit A's overshoot of actual FMV does not even dodge the entity tax for their side — the buyer's only benefit is faster recovery (5-year on the extra 250,000 of Class V, immediate on the extra 10,000 of Class IV vs 15-year amortization), which is modest and can be priced into the give-and-take.
2. **With Buyer B:** the 131,529 after-tax lead narrows to 36,329 if A signs the counter — so **use Buyer A's $3.1M to reprice**: every 1,000 of additional price adds 800 to Ray's after-tax net, so raising B by ≈46,000 (36,329 ⁄ 0.8) restores a clear win. Also ask Hensley (a corporation-affiliated LP) about a **§338(h)(10)/§336(e)-style deemed asset sale** — the library notes stock buyers get no step-up without such an election (`library/stock_vs_asset_overview.md`); if Hensley wants the step-up of ~2.43M of depreciation-amortizable basis, Ray is well placed to charge for it. The election's mechanics and rates are **not in the library beyond the overview — unverified; confirm with the CPA before offering.**
3. **Either way:** Ray signs nothing Friday on the "$3.1M > $2.85M" comparison. The real decision is **2,327,671 (A, countered) vs 2,364,000+ (B)** — and B's installment/living-liability posture earns the small premium.
4. **What price from Lone Star actually beats Hensley (computed, turn 3):** above either allocation, the entity §1374 tax stays capped at 237,300 (NRIG 1,130,000, § 4) and the 237,300 §1366(f)(2) loss offset (§ 5) is fixed in dollars, so each extra dollar is taxed only at its class rate: 80¢ net if it lands in goodwill (20%), 63¢ if it lands in an ordinary class (37%), ≈73.3¢ if Exhibit A rescales across all buckets (26.66¢ average tax per drafted-rescale dollar). Tying B's 2,364,000 nominal requires:

   | Lone Star route | Price to tie B (2,364,000) | Add-on vs 3,100,000 |
   |---|---:|---:|
   | Sign **with the counter allocation**; raise lands in goodwill | **3,145,411.25** | +45,411.25 |
   | As drafted; raise lands in goodwill | 3,264,411.25 | +164,411.25 |
   | As drafted; Exhibit A rescales proportionally | ≈3,279,345 | +179,345 |
   | As drafted; raise lands in the ordinary classes | ≈3,308,776 | +208,776 |

   The LOI does not specify where a renegotiated price increase lands in Exhibit A — hence the bracket. Each crossing keeps the entity tax at exactly 237,300, and tax + net = price holds at every point. **The counter allocation is worth 119,000 of gross price to Ray** (95,200 ⁄ 0.8): it moves Lone Star's required outlay from ≈3.26–3.31M down to **3,145,412**. Note Buyer B repriced +46,000 (→ 2,896,000) nets **2,400,800** and beats every Drafted A variant — the two plays (counter A / reprice B) are worth pairing. For the record: crediting B's note interest (90,000 gross − 33,300 tax nets 56,700, bar 2,420,700) lifts the tie prices to 3,216,286.25 with the counter and ≈3,335,287–3,398,776 as drafted — B keeps a standing edge in any exact tie because of the interest, timing (§ 6), and liability armor (§ 7).

## 9. Assumptions and open items

- §1366(f)(2) BIG-tax loss character: allocated by NRIG source (189,000 capital / 48,300 ordinary). Taxing the full loss against capital first instead gives personal tax 638,440 (net 2,224,260); against ordinary first, 598,099 (net 2,264,601). Range: +8,211 / −32,130 around the primary figure; the library does not fix the rule.
- Goodwill-as-capital rests on `library/stock_vs_asset_overview.md`; §1221/§1231/§1253 citations are outside the library — unverified.
- Self-employment tax on Ray's 400,000 covenant income (client confirms it is all covenant, no services; retirement does not change this analysis), Texas franchise tax on the closing year, and the §453A interest-charge floor are **not addressed in the library — unverified; referred to the CPA.**
- **FMV support for Class V at 650,000** (who prepared the register's `fmv_estimate`, and as of what date) is unconfirmed by the client; if Buyer A disputes it, an appraisal is needed before signing — flagged as an open item in `QUESTIONS.md`.
- **Receivables history** ("no reserve" per the file, but prior-year bad-debt treatment unconfirmed): unconfirmed by the client; unverified — flagged in `QUESTIONS.md`.
- Buyer B's note is unsecured; collectibility and any security/escrow upgrade is a commercial question (§ 8).
- Whether the closing occurs in 2026 (inside the recognition period either way for any plausible date through 2027) is assumed from the LOI dates.
- See `deliverable/QUESTIONS.md` for the client-question log: one answered (covenant), two unresolved (Class V FMV support; receivables history).

## 10. Bottom line for Ray

| Answer to "can you confirm I net about $2.5M?" | **No.** As drafted, Buyer A nets **2,232,471**; Buyer B nets **2,364,000** nominal (more with the note's timing). |
| What to do | Don't sign Friday. Counter Buyer A's allocation (+95,200) and re-price Buyer B upward against it; take whichever lands higher after the counters. |
| Price from Lone Star that ties Hensley | **3,145,412 with the counter allocation** (+45,412); ≈3.26M–3.31M as drafted depending where the raise lands (§ 8(4)). |

*Sources: every citation above points to `library/INDEX.md`. All arithmetic shown; nothing forced to balance except items explicitly tied (§ 5, § 9).*
