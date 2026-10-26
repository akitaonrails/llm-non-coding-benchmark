# Brightline Cabinetry — Buyer A (asset sale) vs. Buyer B (stock sale)

**Prepared for Ray Brightline. Date: October 25, 2026.**

## 0. Bottom line (read this first)

- **Buyer B's stock sale nets you more money: $2,364,000 after tax vs. $2,192,260 for Buyer A's deal as drafted and $2,234,760 with my corrected allocation.** B is better by **$171,740** as drafted and **$129,240** even after the counter-allocation fix.
- Your buddy's "$3.1M at 20% = $2.5M" is wrong for Buyer A's deal: **about $1,070,000 of it is ordinary income at 37%**, not capital gain, and the **S corporation owes $237,300 of entity-level tax you pay for before you ever see the money**. Buyer A's deal as drafted really nets **$2,192,260** — your naive number is **$287,740 too high**.
- Most of the ordinary-income problem is * Buyer A's own allocation paper* and is fixable in negotiation for **$42,500 of tax savings** without changing the $3,100,000 price.
- **Do not sign Buyer A's LOI on Friday with Exhibit A as written.** The two offers are close enough that how the deal is papered matters more than the $250,000 sticker-price gap.

Rates used (only choices the engagement library allows, `library/capital_gain_rates.md`): ordinary **37%**, long-term capital gain **20%**, 3.8% NIIT **excluded** (library treats the gain as from an active business with material participation — pending your confirmation, see QUESTIONS.md), no Texas individual income tax. Texas franchise tax applies to the entity (`documents/tax_history_and_conversion.md`) but no rate exists in the library, so it is not modeled.

## 1. The two offers

| | Buyer A — Lone Star Millwork | Buyer B — Hensley Family Partners |
|---|---|---|
| Structure | Asset purchase of substantially all assets | Purchase of 100% membership interests |
| Price | $3,100,000 all cash | $2,850,000 = $2,350,000 cash + $500,000 note (5 yr, 6%, annual principal) |
| Liabilities | Assumes **only** trade payables "listed on a closing schedule" | Assumes the company **with all its liabilities, known and unknown** |
| Non-compete | $400,000 of price allocated to Ray's 5-yr covenant + consulting agreement | No separate payment; customary 3-yr covenant signed for no consideration |
| Protections | None specified in LOI (non-binding except confidentiality + 45-day exclusivity) | 12-month indemnity cap 10% of price; $100,000 escrow (source: Buyer B LOI) |

`library/stock_vs_asset_overview.md`: in a stock sale the seller recognizes capital gain on price minus stock basis and the buyer takes carryover basis (no step-up unless a §338(h)(10)/§336(e) election); the buyer inherits all liabilities. In an asset sale, gain is computed asset by asset under the allocation, recapture and covenant payments are ordinary, the buyer gets a basis step-up, and S corporations within the §1374 recognition period owe entity-level built-in-gains tax. The overview notes price differences typically reflect the buyer's step-up value and assumed liabilities — which is exactly why Buyer A can pay a sticker $250,000 higher and still leave you worse off.

## 2. Buyer A as drafted — asset-by-asset (allocations from Exhibit A of the LOI)

Three facts drive everything: the company was a **C corporation 2012–2022** and an **S corporation since 1/1/2023** (`documents/tax_history_and_conversion.md`), with a conversion-day built-in-gain appraisal (goodwill $900,000; equipment $230,000); equipment's current **adjusted basis is $240,000 against FMV $650,000 and accumulated depreciation $860,000** (`documents/fixed_asset_register.csv`); your stock basis is **$420,000** (12/31/2025).

| Exhibit A class | Price | Your basis | Gain | Character |
|---|---:|---:|---:|---|
| III Receivables | $200,000 | $200,000 (no reserve) | $0 | — |
| IV Inventory | $150,000 | $140,000 | $10,000 | ordinary (asset-by-asset asset sale, `stock_vs_asset_overview.md`) |
| V Equipment & vehicles | $900,000 | $240,000 | $660,000 | **ordinary — §1245 recapture** |
| "Class V" non-compete (really Class VI) | $400,000 | — | $400,000 | **ordinary income to you** (`irc_197_and_noncompete.md`) |
| VII Goodwill | $1,450,000 | $0 | $1,450,000 | capital |

- **§1245 recapture.** `library/irc_1245.md` (§1245(a)(1)): the lesser of recomputed basis (adjusted basis plus depreciation) or amount realized, minus adjusted basis, is ordinary income. Recomputed basis = 240,000 + 860,000 = $1,100,000; amount realized $900,000 is lower; 900,000 − 240,000 = **$660,000 ordinary**. Buyer's $900,000 price exceeds the equipment's own FMV of $650,000 — you are paying **37% tax on $250,000 that isn't even there**. That's the heart of the Exhibit A problem.
- **Covenant.** `library/irc_197_and_noncompete.md` (§197(d)(1)(E); Rev. Rul. 69-643; *Muskat*): covenant payments to the seller are **ordinary income**, and the written allocation binds the parties absent strong proof and can be challenged by the IRS. **Assumption (prominent):** the $400,000 is paid to you directly at closing, since the covenant is yours personally; routing is unconfirmed — see QUESTIONS.md. Also, the LOI bundles a "consulting agreement" with the covenant; if any consulting fee is payable beyond the $400,000, that is additional income I cannot size yet (amount unknown, QUESTIONS.md).
- **Goodwill.** $1,450,000 over $0 basis is long-term capital gain (asset-sale method per `stock_vs_asset_overview.md`; 20% per `capital_gain_rates.md`).

Subtotals as drafted: ordinary income to you **$1,070,000** (660,000 + 10,000 + 400,000); capital-gain passthrough before entity tax **$1,450,000**.

## 3. The entity-level tax you can't avoid in the asset deal — §1374

Because of the 2012–2022 C-corp years, the S corporation has built-in gains at conversion (goodwill $900,000; equipment $230,000). `library/irc_1374.md` (§1374(a), (b), (d)(7)): during the **5-year recognition period beginning 1/1/2023 (through 12/31/2027)**, a sale triggers corporate tax at **21%** on the recognized built-in gain, capped per asset at its conversion-day built-in gain, and the tax is treated as a loss sustained by the S corporation (§1366(f)(2)).

| Asset | BIG at 1/1/2023 | Gain recognized | Counted |
|---|---:|---:|---:|
| Goodwill | $900,000 | $1,450,000 | $900,000 (lesser) |
| Equipment | $230,000 | $660,000 | $230,000 (lesser) |
| Inventory | $0 | $10,000 | $0 |
| **Net recognized built-in gain** | | | **$1,130,000** |

**Entity tax = 21% × 1,130,000 = $237,300.** This tax is the same in every asset-sale variant of this deal — it is baked in by the C-corp history, not by the allocation. A 2026 or 2027 closing is inside the recognition period (a 2028 closing would end it — see §8).

**Character caveat (labeled):** the library says the $237,300 tax "is treated as a loss sustained by the S corporation (§1366(f)(2))" but does not state whether that loss is capital or ordinary to you. I have taken it against the capital side. If it is ordinary, your total tax rises by 237,300 × (37% − 20%) = **$40,341**. Question posed in QUESTIONS.md to your prior CPA; do not treat my figure as final until answered.

## 4. Buyer A as drafted — your basis rollforward and the cash

1. Stock basis 12/31/2025: $420,000.
2. Sale-year passthrough: ordinary $670,000 (recapture 660,000 + inventory 10,000) + capital $1,450,000 → basis $2,540,000.
3. §1366(f)(2) loss for the entity tax: −$237,300 → basis $2,302,700.
4. The company sells assets for $2,700,000 (200 + 150 + 900 + 1,450), pays the $237,300 tax, distributes **$2,462,700** at liquidation; plus your $400,000 covenant payment → **cash to you $2,862,700**.
5. Liquidating overshoot: 2,462,700 − 2,302,700 = **$160,000 capital gain** (the §1366(f)(2) basis reduction outpaces the shrunken distribution).
6. Total capital gain: 1,450,000 − 237,300 + 160,000 = **$1,372,700**. Total income check: 1,070,000 + 1,372,700 = **$2,442,700** = (2,862,700 cash − 420,000 basis). Reconciles; not forced.

**Tax:** individual 1,070,000 × 37% = $395,900; capital 1,372,700 × 20% = $274,540; entity $237,300. **Total $907,740.**
**Net after tax = 3,100,000 − 907,740 = $2,192,260** (same answer computed as cash $2,862,700 − $670,440 individual tax).

*(Correction of an earlier draft: an interim figure of $1,954,960 subtracted the entity tax twice — receipts were already net of it. §8 records this.)*

## 5. Buyer A counter-allocation — free $42,500

Buyer's own Exhibit A misprices the equipment by $250,000: it values Class V at $900,000 when your documented FMV is $650,000 (`documents/fixed_asset_register.csv`), and it labels the non-compete "Class V" when the covenant is a Class VI §197 intangible (`library/irc_1060_form_8594.md` — each class is allocated **up to FMV** before moving on; Class VI includes covenants). Corrected, purely mechanical, price unchanged at $3,100,000:

| Class | Buyer's Exhibit A | Counter | Note |
|---|---:|---:|---|
| III receivables | 200,000 | 200,000 | FMV = carrying value, no reserve |
| IV inventory | 150,000 | 150,000 | FMV per Buyer; carrying 140,000 |
| V equipment | 900,000 | **650,000** | capped at documented FMV; excess $250,000 moves out |
| VI covenant | ("Class V") 400,000 | 400,000 | correct class restated |
| VII goodwill | 1,450,000 | **1,700,000** | residual: 3,100,000 − (200+150+650+400) |

Effects to you: §1245 recapture falls 660,000 → 410,000 (650,000 − 240,000, still all recapture under `irc_1245.md` because depreciation of $860,000 exceeds the gain); ordinary income drops to **$820,000**; goodwill rises to $1,700,000; entity §1374 tax stays $237,300 (BIG is per-asset, lesser-of: goodwill 900,000 and equipment 230,000 either way). Basis rollforward: 420,000 + 420,000 + 1,700,000 = 2,540,000 → −237,300 = 2,302,700; distribution 2,462,700 → liquidating gain 160,000; capital **$1,622,700**; income check 820,000 + 1,622,700 = $2,442,700 ✓ unchanged.

**Tax:** 820,000 × 37% = $303,400; 1,622,700 × 20% = $324,540; entity 237,300 → **$865,240**. **Net = 3,100,000 − 865,240 = $2,234,760** — **$42,500 better** than the drafted version (250,000 × (37% − 20%)). Trade-off to expect: each $100,000 you give back to Buyer A's equipment number costs you $17,000 of tax (100,000 × 17%), and Buyer A may want equipment basis for faster recovery than 15-year amortization — recovery-period speeds are **not in the library (labeled unverified)**, so this is a negotiation point, not a settled number. Full write-up with per-class justification: `form_8594_counter.md`.

## 6. Buyer B — the stock sale

**Gain:** 2,850,000 − 420,000 stock basis = **$2,430,000 capital gain** (`stock_vs_asset_overview.md`; 20% per `capital_gain_rates.md`). No covenant payment exists (the 3-year covenant is given for no consideration), no recapture (you sell stock, not §1245 property — `irc_1245.md` reaches only dispositions of the property itself), and **no §1374 entity tax** (the company is not selling appreciated assets — you are selling the stock). Tax **$486,000**; **net $2,364,000** on the headline numbers.

**The note changes the timing, not the character.** Under `library/irc_453_installment.md` (§453(a)), gain is recognized proportionately as payments are received; §453(i)'s year-of-sale recapture exception reaches §1245 recapture income, which does not exist here (stock is not depreciable property), and the method's exclusions (inventory; depreciable property to related persons) don't apply. Gross-profit ratio = 2,430,000 ÷ 2,850,000 = **85.2632%**.

Assumed mechanics (LOI says "annual principal"; confirm, QUESTIONS.md): $100,000 principal each year plus 6% interest on the declining balance, first payment 2027.

| Year | Payment | Principal | Interest | Gain recognized | Tax |
|---|---:|---:|---:|---:|---:|
| 2026 closing | 2,350,000 | 2,350,000 | 0 | 2,350,000 × 85.2632% = **2,003,684.21** | 400,736.84 |
| 2027 | 130,000 | 100,000 | 30,000 | 85,263.16 | 17,052.63 |
| 2028 | 124,000 | 100,000 | 24,000 | 85,263.16 | 17,052.63 |
| 2029 | 118,000 | 100,000 | 18,000 | 85,263.16 | 17,052.63 |
| 2030 | 112,000 | 100,000 | 12,000 | 85,263.16 | 17,052.63 |
| 2031 | 106,000 | 100,000 | 6,000 | 85,263.16 | 17,052.63 |
| **Total** | **2,940,000** | 2,850,000 | 90,000 | **2,430,000.00** | 486,000.00 |

(Gains in the five note years sum to 426,315.80 by the rounded per-year figure; exact-ratio sum is 426,315.79, which closes the schedule exactly against the remaining gain of 2,430,000 − 2,003,684.21. Interest is reported as interest income — ordinary at 37%; **that treatment is not in the library and is labeled unverified**, as is whether 6% is a defensible rate under imputed-interest-type rules, which the library also lacks. Note interest totals $90,000, tax $33,300; including it, nominal 2026–2031 tax is $519,300 and nominal net is $2,420,700.)

**After-tax cash timing (B):** 2026: 2,350,000 − 400,736.84 = 1,949,263.16; then 101,847.37 / 98,067.37 / 94,287.37 / 90,507.37 / 86,727.37 in 2027–2031 (payments minus installment-gain tax minus interest tax — e.g., 2027: 130,000 − 17,052.63 − 11,100 = 101,847.37). Sums to **$2,420,700** (a one-cent rounding). Versus Buyer A: all cash up front but a bigger total tax bill.

## 7. The rest of the comparison — liabilities and protections

- **Liabilities.** Buyer A assumes *only listed trade payables*, so every other company liability stays behind with the entity you must then liquidate; the amount is unknown (QUESTIONS.md). Buyer B assumes the company **with all liabilities, known and unknown** — cleaner exit for you, and by `stock_vs_asset_overview.md` this is exactly the kind of difference that explains the $250,000 price gap.
- **Protections.** B gives a 12-month indemnity capped at 10% of price ($285,000) but only $100,000 of escrow backing it — that gap of $185,000 is a real negotiation point. A's LOI specifies no indemnity or escrow at all, and it is non-binding except a **45-day exclusivity**: signing it Friday would *lock you out of negotiating with Hensley* for 45 days before either deal is enforceable.
- **Credit risk.** B's $500,000 note is **unsecured**. §453 gives you the deferral; nothing in the library secures collection. Ask for security (collateral, guarantee, or a larger escrow/setoff right).
- **Consulting agreement (A only).** If a consulting fee is payable in addition to the $400,000, it is additional income to you of unknown amount; service-compensation character is **not in the library (labeled unverified)**. QUESTIONS.md.

## 8. Errors and honesty notes (kept visible per engagement rules)

1. **Corrected this memo:** an interim calc showed A-drafted net $1,954,960 by subtracting the $237,300 entity tax twice (once inside the $2,862,700 receipts, once against the price). Two independent routes both give **$2,192,260** (3,100,000 − 907,740; and 2,862,700 − 670,440).
2. **§1366(f)(2) loss character** (capital vs. ordinary) swings total tax by **$40,341** either way; library does not resolve. QUESTIONS.md.
3. **Inventory character** ($10,000, ordinary assumed): ordinary-vs-capital authority for inventory in the library is thin; worst case the swing is $1,700.
4. **NIIT excluded** on the library's material-participation condition — pending your confirmation.
5. **Interest on B's note treated as ordinary; 6% rate adequacy; equipment depreciation recovery periods; §483/§1274** — all absent from the library, labeled unverified.
6. **§338(h)(10)/§336(e):** `stock_vs_asset_overview.md` establishes only that these elections can convert Buyer B's stock purchase into a deemed asset sale with asset-sale consequences to the seller. Illustratively (unverified mechanics, inventory assumed at $140,000 FMV, same per-asset lesser-of BIG math): deemed allocation 200/140/650/1,860 → ordinary $410,000, capital $1,782,700, entity tax $237,300, net ≈ **$2,104,460**, i.e. $259,540 worse for you than the straight stock deal. If Hensley wants that election for its own step-up, it must **pay a premium exceeding roughly $259,540** — labeled estimate only.

## 9. Recommendation

**Best real option: Buyer B, at $2,364,000 net — a $171,740 advantage over A as drafted.** Even after fixing A's allocation to the maximum supportable extent, B still wins by **$129,240**, and B takes all liabilities off your hands. Order of action:

1. **Do not sign A's LOI Friday.** The 45-day exclusivity would bench Hensley before either deal binds.
2. **If you pursue Lone Star:** counter on Exhibit A exactly per `form_8594_counter.md` (equipment at $650,000, covenant in Class VI, goodwill $1,700,000 — no price change) and require the corrected allocation to be embedded in the signed agreement so Form 8594 consistency works in your favor (`irc_1060_form_8594.md`; economic-reality/§1060(a) caveat in `irc_197_and_noncompete.md`). Also demand real indemnity/escrow terms, which the LOI currently omits.
3. **If you pursue Hensley (recommended):** negotiate the note ($500,000 unsecured → seek collateral/guarantee or setoff), align escrow ($100,000) with the indemnity cap (10% = $285,000), and confirm the "annual principal" mechanics.
4. **Do not chase a §336(e)/§338(h)(10) election for Hensley** unless it pays a premium covering the ≈$259,540 cost to you (§8, labeled estimate).
5. A 2028 closing (after the 5-year recognition period ends 12/31/2027, `irc_1374.md` §1374(d)(7)) would erase the $237,300 §1374 tax in the A structure — but two more years of carrying the business and both buyers at the table is not a trade I recommend; noted only so the number is on the table.

Open items live in `QUESTIONS.md`; status is `COMPLETE WITH OPEN ITEMS` in `STATUS.md`.

## 10. Second round — client answers and what they change

Ray's answers (Oct 25, 2026 round): he is **retiring** and would sign the **5-year covenant**; he doesn't care "what they call the payment" as long as the **total price is unchanged**; the **$500,000 note is unsecured** and he does **not know Hensley's balance sheet**; there is a **Hardaway dispute ($9,800)** plus "usual warranty" items, "nothing big."

### 10.1 The label of the $400,000 still matters — $68,000 is at stake

Ray says he doesn't care whether the $400,000 is labeled covenant or goodwill. The label is precisely what sets his tax rate on that money: covenant dollars are **ordinary at 37%** (`irc_197_and_noncompete.md`), goodwill dollars are **capital at 20%** — moving them saves 400,000 × (37% − 20%) = **$68,000**. Because Ray is **retiring**, there is an economic-reality argument for the move: a covenant from a seller who is exiting entirely restrains little beyond what the goodwill purchase already buys, and `irc_197_and_noncompete.md` requires allocations to reflect economic reality (while noting written allocations bind the parties absent strong proof and the IRS may challenge unrealistic ones — so this move needs Buyer A's written agreement and documentation of Ray's retirement). Scenario ladder, all prices unchanged at $3,100,000, cross-checked two ways:

| Scenario | Ordinary | Capital | Entity 1374 | Total tax | Net | B advantage |
|---|---:|---:|---:|---:|---:|---:|
| A as drafted | 1,070,000 | 1,372,700 | 237,300 | 907,740 | 2,192,260 | 171,740 |
| A + covenant→goodwill only (Ray retiring) | 670,000 | 1,772,700 | 237,300 | 839,740 | 2,260,260 | 103,740 |
| A + Class-V fix only (§4/§5 counter) | 820,000 | 1,622,700 | 237,300 | 865,240 | 2,234,760 | 129,240 |
| A + both moves (full variant) | 420,000 | 2,022,700 | 237,300 | 797,240 | **2,302,760** | 61,240 |
| Buyer B (stock) | 0 | 2,430,000 | 0 | 486,000 | **2,364,000** | — |

Cross-checks: drafted + 68,000 = 2,260,260 (covenant-only row); 2,260,260 + 42,500 = 2,302,760 and 2,234,760 + 68,000 = 2,302,760 (full variant arrived at two different ways ✓). Full-variant workpaper: entity receives 3,100,000 (capital piece 2,100,000); BIG unchanged — goodwill counted at min(900k BIG, 2,100k gain) = 900,000, equipment min(230k, 410k) = 230,000 → 21% × 1,130,000 = 237,300 ✓. Passthrough 420,000 ordinary + 2,100,000 capital; basis rollforward 420,000 + 420,000 + 2,100,000 − 237,300 = 2,702,700; distribution 2,862,700 → liquidating gain 160,000 capital; aggregate income 420,000 + 2,022,700 = 2,442,700 = 2,862,700 − 420,000 ✓. Even at best, **B still wins by $61,240** before item 10.2.

Every $100,000 Ray moves from Class VI to Class VII is worth $17,000 to him, and the only ceiling is the number Buyer A will defend for the covenant. The variant is in `form_8594_counter.md` as an explicitly optional add-on, and never as something to do without Buyer A's signature (consistency rule, `irc_1060_form_8594.md`).

### 10.2 Hardaway dispute and warranty tail — favors B again

New disclosed facts: a disputed amount of **$9,800** (Hardaway) and "usual" warranty obligations (amount unspecified). Neither is an asset, so the §1374 entity tax of $237,300 is untouched.

- **Buyer A's asset deal:** Buyer assumes *only trade payables listed on a closing schedule*, so the dispute (if it goes against Ray) and warranty work ride on the entity Ray then liquidates — paid out of company cash before it reaches Ray. If Ray's $420,000 stock basis already reflects recorded liabilities (assumption — the prior CPA prepared it), the payment is a cash haircut with no tax change: est. net 2,192,260 − 9,800 = **≈2,182,460**, warranty cost on top, unquantified. If those liabilities were *not* reflected in basis, an offsetting loss would arise whose character the library does not address (**labeled unverified**); worst-case swing ≈ 9,800 × 17% = **$1,666** — immaterial, left open rather than forced.
- **Buyer B's stock deal:** Hensley assumes the company **with all liabilities, known and unknown**. Hardaway is now *known*, so it must be disclosed in the reps; it sits comfortably inside the indemnity cap (10% = $285,000) and the $100,000 escrow. Ray's numbers do not change.
- Negotiation consequence: in an A deal, ask Buyer A to either assume the dispute/warranty tail or escrow against it; in a B deal, disclose Hardaway and keep the escrow/cap structure.

### 10.3 Unsecured note + unknown buyer credit — negotiation list

Confirmed unsecured, and Ray cannot evaluate Hensley's balance sheet (**unknown remains unverified**). Options to press (deal points, not tax): security for the note — e.g., guarantee by the acquired company whose assets Hensley just bought, or setoff rights against the note for indemnity claims; escrow alignment ($100,000 escrow vs $285,000 cap from §7 stands); rate adequacy remains **unverified** (no §483/§1274-type rule in the library). The installment schedule in §6 is unchanged mechanically; "annual principal" still unconfirmed but the client supplied no alternative schedule, so the $100,000-principal model stands as labeled.

### 10.4 Remaining unknowns (client has no information — flagged, not re-asked)

Consulting fee under A's covenant package; company cash balance and full payables at closing; §1366(f)(2) loss character (±$40,341); NIIT material-participation facts (retirement does not negate 2026 participation — assumed qualifying per library); other-ordinary-income level behind the 37% rate; Texas franchise tax specifics; AFR benchmark for the 6% note; exact note payment schedule; independent equipment appraisal; Hensley balance sheet; warranty exposure amount; outcome of the Hardaway dispute. Numbers in this memo and in `comparison.json` are final figures under the stated assumptions, not estimates pending these items — the open items color the cash around the edges (most immaterial, as quantified), they do not flip the recommendation. **Recommendation unchanged: Buyer B.** Second-best path if A stays in: full variant of §10.1 at **$2,302,760**, with the liability tail of §10.2.
