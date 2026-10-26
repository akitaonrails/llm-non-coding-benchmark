# Brightline Cabinetry — Lone Star (Buyer A) vs. Hensley (Buyer B): tax comparison and negotiating position

Prepared for Ray Brightline. All tax rates are the 2026 engagement rates: ordinary 37%, long-term capital gain 20%, no NIIT on an active trade or business in which the taxpayer materially participates (`capital_gain_rates.md`). Texas has no individual income tax. Every legal point below cites a file in `library/INDEX.md`; points I believe to be law but cannot verify in the library are flagged **[unverified]**.

## 1. Bottom line

| | Buyer A (Lone Star) as drafted | Buyer A with our allocation | Buyer B (Hensley) |
|---|---:|---:|---:|
| Gross proceeds | $3,100,000.00 | $3,100,000.00 | $2,850,000.00 |
| Ordinary income | $1,070,000.00 | $420,000.00 | $0.00 |
| Long-term capital gain | $1,450,000.00 | $2,100,000.00 | $2,430,000.00 |
| Entity-level §1374 tax | $237,300.00 | $237,300.00 | $0.00 |
| Total tax | $923,200.00 | $812,700.00 | $486,000.00 |
| **Net after tax** | **$2,176,800.00** | **$2,287,300.00** | **$2,364,000.00** |

- Ray's estimate ("$3.1M at 20% ≈ $2.5M net") is wrong by roughly **$303,200**. $3,100,000 × 0.80 = $2,480,000, but the real net on Buyer A **as drafted** is **$2,176,800**.
- The smaller offer (Hensley, $2,850,000) actually nets about **$187,200 more** than Lone Star's as drafted — before considering that Hensley also (i) takes all of the company's liabilities, known and unknown, and (ii) pays 6% interest on the $500,000 note (≈ $90,000 of interest over 5 years, $56,700 after tax).
- Buyer A only becomes the better deal if the allocation is rewritten (worth $110,500) **and** either the price goes up or closing is pushed past 12/31/2027 so the built-in gains period expires (worth $237,300). See §7.
- **Do not sign Buyer A's LOI on Friday as drafted.**

### 1a. Update after Ray's answers (turn 2)

- **"I don't care what they call the payment as long as the total is the same" — the label *is* money to Ray.** Same $3,100,000 total, but calling $400,000 a covenant instead of goodwill costs him $400,000 × (37% − 20%) = **$68,000**, and the $250,000 equipment over-allocation another **$42,500**. His indifference to the label is precisely why the counter-allocation is a free trade: Lone Star's amortization of a covenant and of goodwill is identical (both 15-year §197 intangibles, `irc_197_and_noncompete.md`; `irc_1060_form_8594.md`), so it costs them $0 to give it up.
- **Ray is retiring and will sign the 5-year covenant.** Factually helpful twice over: (i) the covenant stays in the PSA for free, so Lone Star loses nothing real by the $0 Class VI allocation; (ii) it strengthens the economic-reality defense of the $0 allocation under *Muskat* / Rev. Rul. 69-643 (`irc_197_and_noncompete.md`) — a retiring seller is little competitive threat, so the covenant's stand-alone value is weak and the $3.1M is plainly payment for the business (Class VII goodwill). Caveat: if the PSA imposes *real* consulting obligations (scope/hours), those services are compensation regardless of the label — show us the obligation before signing and we will price it in a separate services agreement outside the purchase price.
- **Known liabilities (Hardaway dispute $9,800 + unspecified "usual" warranty tail)** sit entirely with Ray under Deal A (uncapped, no escrow running his way) and entirely with Hensley under Deal B (Ray capped at $100,000 escrow / 12 months / $285,000 indemnity). Risk-adjusted on quantified items only: counter-allocated A ≈ **$2,277,500** ($2,287,300 − $9,800, warranty tail still open-ended); B ≈ $2,364,000 with capped exposure. B's lead is **≥ $86,500**, rising to **≈ $143,000–157,000** with after-tax note interest (+$56,700) and installment deferral value (+≈$13,400 PV), before pricing the unsecured note's credit risk and escrow carry (−$6,000). **Ranking unchanged; B's case strengthened.**

### 1b. "How does an offer $250,000 higher net me less?" — the bridge and the matching price (client Q&A)

Bridge, headline figures from §1: price $3,100,000 − $2,850,000 = **+$250,000**, but tax $923,200 − $486,000 = **+$437,200** → **−$187,200** to Ray. Where the extra tax comes from:

| Source | Amount |
|---|---:|
| §1374 entity-level built-in gains tax (Deal A only) | $237,300 |
| Equipment §1245 recapture premium: $660,000 × (37% − 20%) | $112,200 |
| Covenant allocation premium: $400,000 × (37% − 20%) | $68,000 |
| Inventory premium: $10,000 × (37% − 20%) | $1,700 |
| Larger gain base (inside basis $580,000 vs stock basis $420,000) at 20% | $18,000 |
| **Total extra tax under Deal A as drafted** | **$437,200** |

What Lone Star must bid to actually beat Hensley (any extra dollar lands in Class VII goodwill → 20% capital rate; no incremental §1374 because both goodwill caps are already exceeded → extra dollars net 80¢):

| Deal A version | Extra needed | Price that beats Hensley (tax-only table) |
|---|---:|---:|
| As drafted | +$234,000 | **$3,334,000** |
| Counter allocation (§7.1) | +$95,875 | **$3,195,875** |
| Counter allocation vs Hensley *all-in* ($2,428,131: net + $56,700 note interest + $13,431 deferral PV − $6,000 escrow carry; A retains Hardaway $9,800) | +$188,289 | **≈ $3,288,000** |
| **Same $3,100,000, closing after 12/31/2027** | **$0** | already nets ≈ **$2,524,600**, beating Hensley all-in by ≈ **$96,000** |

The date is worth as much as the money: a post-2027 closing erases the $237,300 without a single extra dollar of price. Caveats: 2028 feasibility is untested (QUESTIONS.md §3) and any Hensley §338(h)(10)/§336(e) request re-prices the Hensley side.

## 2. Why "business sales are capital gains" is wrong in an asset sale

In an asset sale the gain is computed **asset by asset under the price allocation** (`stock_vs_asset_overview.md`), and several components are taxed as ordinary income at 37%, not 20%:

1. **Equipment and vehicles — §1245 recapture.** For §1245 property, the lower of (A) recomputed basis (adjusted basis + depreciation allowed) or (B) amount realized, minus adjusted basis, is ordinary income, "notwithstanding any other provision" (`irc_1245.md`). The fixed-asset register shows cost $1,100,000, accumulated depreciation $860,000, adjusted basis $240,000 → recomputed basis = $240,000 + $860,000 = $1,100,000. Any allocation to equipment below $1,100,000 makes **every dollar of equipment gain ordinary**. At Buyer A's proposed $900,000 allocation: $900,000 − $240,000 = **$660,000.00 ordinary**.
2. **The $400,000 "non-compete" allocation — ordinary.** A covenant not to compete entered into in connection with the sale of a business is ordinary income to the seller — compensation for refraining from competing — not capital gain (`irc_197_and_noncompete.md`, citing Rev. Rul. 69-643; *Muskat v. United States*, 554 F.3d 183 (1st Cir. 2009)). Allocating $400,000 of purchase price to the covenant costs **$400,000.00 of ordinary income**.
3. **Inventory.** The $150,000 allocation vs. $140,000 carrying value gives $10,000 of gain. Inventory gain is ordinary **[unverified — the library has no §1221/§1231; the point is universally accepted but I cannot cite it here]**. (`irc_453_installment.md` confirms only that the installment method is unavailable for inventory.)
4. **Goodwill/trade name — capital.** Self-created goodwill has zero basis in the company's hands **[unverified — not in library]**, so the full Class VII allocation is gain; it is the only large capital-gain piece of an asset sale.

## 3. Built-in gains (§1374) — an entity-level tax Buyer A's structure triggers

Brightline elected S corporation status effective 1/1/2023. The recognition period is the **5-year period beginning with the first day of the first S year** (`irc_1374.md`, §1374(d)(7)): **1/1/2023 through 12/31/2027**. A 2026 asset sale falls inside it.

- Tax = highest corporate rate, **21%**, on net recognized built-in gain (§1374(a), (b)(1)).
- Recognized built-in gain per asset is **capped at the built-in gain shown on the 1/1/2023 conversion appraisal** (`irc_1374.md`, (d)(7)).

| Asset | Built-in gain at 1/1/2023 | Actual gain (A as drafted) | Recognized BIG |
|---|---:|---:|---:|
| Equipment & vehicles | $230,000.00 | $660,000.00 | $230,000.00 |
| Goodwill / trade name | $900,000.00 | $1,450,000.00 | $900,000.00 |
| Non-compete / other | $0.00 | $410,000.00 | $0.00 |
| **Net recognized BIG** | | | **$1,130,000.00** |

Entity-level tax: $1,130,000 × 21% = **$237,300.00**. The non-compete payment carries no BIG because the covenant did not exist as an asset at 1/1/2023 (appraisal "Other: 0"). The §1374 tax is treated as a loss sustained by the S corporation and passes through to Ray (§1366(f)(2), as summarized in `irc_1374.md`); at a 37% rate that pass-through loss is worth up to $237,300 × 37% = **$87,801**, softening the net cost to ≈ $149,499. I show the **full $237,300** in the headline figures as the conservative view and flag the offset; the offset applies to A (and to any deemed asset sale), never to a clean stock sale.

Key corollary: **the §1374 exposure is a function of structure and timing, not price.** It does not depend on how the $3.1M is allocated (equipment gain stays above the $230,000 cap either way; goodwill stays above the $900,000 cap), and it disappears entirely if the asset-sale closing slips past 12/31/2027, or if the deal is a stock sale.

## 4. Buyer A (Lone Star) — asset sale, as drafted

Allocation per Exhibit A: receivables $200,000 / inventory $150,000 / equipment $900,000 / non-compete $400,000 / goodwill $1,450,000 = $3,100,000.

Component-by-component (bases: receivables $200,000, inventory $140,000, equipment $240,000, goodwill and covenant $0):

| Class | Allocated | Basis | Gain | Character | Authority |
|---|---:|---:|---:|---|---|
| III receivables | $200,000.00 | $200,000.00 | $0.00 | — (face value, no reserve) | §1060 classes, `irc_1060_form_8594.md` |
| IV inventory | $150,000.00 | $140,000.00 | $10,000.00 | Ordinary **[unverified character]** | — |
| V equipment & vehicles | $900,000.00 | $240,000.00 | $660,000.00 | **All ordinary** (§1245; $900,000 < recomputed basis $1,100,000) | `irc_1245.md` |
| VI non-compete (5 yr) | $400,000.00 | $0.00 | $400,000.00 | **Ordinary** | `irc_197_and_noncompete.md` |
| VII goodwill | $1,450,000.00 | $0.00 | $1,450,000.00 | Capital | — |

Shareholder-level tax: ordinary $1,070,000 × 37% = $395,900.00; capital $1,450,000 × 20% = $290,000.00. Plus entity-level §1374 $237,300.00.
**Total tax $923,200.00 → net $2,176,800.00.** (Check: total gain $3,100,000 − $580,000 of asset bases = $2,520,000 = $1,070,000 + $1,450,000. ✓)

Two defects in the drafted allocation itself:

1. **It violates §1060's FMV discipline.** Under the residual method each class is allocated up to **fair market value** before the next class receives anything (`irc_1060_form_8594.md`, Treas. Reg. §1.1060-1). The company's own fixed-asset register puts equipment & vehicles FMV at **$650,000**; Exhibit A allocates **$900,000** — $250,000 above FMV, straight into §1245 ordinary recapture at 37%.
2. **You will be stuck with it.** Buyer and seller must each file Form 8594 and report **consistently with any written allocation agreement** (`irc_1060_form_8594.md`), and the parties' written allocation binds the parties absent strong proof (*Danielson* rule, per `irc_197_and_noncompete.md`). Exhibit A is exactly such a writing. Fix it **before** signing, not after. (The IRS can challenge an allocation the *taxpayer* likes; it will not rescue a signed one — and the recapture rules apply "notwithstanding any other provision," `irc_1245.md`.)

Buyer A is indifferent between Class VI (covenant) and Class VII (goodwill) — both are §197 intangibles amortized by the buyer over 15 years (`irc_197_and_noncompete.md`; `irc_1060_form_8594.md`). The $400,000 covenant allocation is pure damage to Ray (37% vs 20%) and worth $0 to Lone Star. Their $900,000 equipment load helps them (5-year MACRS vs 15-year amortization) at a cost to Ray of $17 per $100 shifted. This "standard" allocation is standard **for buyers**.

Also note the installment rules work *against* A even if they offered a note: §1245 recapture is recognized **in full in the year of sale regardless of payments** (§453(i), `irc_453_installment.md`).

## 5. Buyer B (Hensley) — purchase of 100% of the membership interests

A membership-interest sale is a sale of Ray's capital asset: one gain = price − stock basis, **all long-term capital gain**; the company's assets are never disposed of, so **no §1245 recapture and no §1374 tax** (`stock_vs_asset_overview.md`).

- Gain: $2,850,000 − $420,000 (stock basis, 12/31/2025) = **$2,430,000.00 LTCG** (held since 2012).
- Tax: $2,430,000 × 20% = **$486,000.00** → **net $2,364,000.00**.
- No NIIT (active business, material participation — `capital_gain_rates.md`).
- **The 3-year non-compete is not separately priced** ("customary … at no separate consideration"). Under *Muskat*, a covenant entered in connection with the sale of a business does not automatically create ordinary income — the question is economic reality and separate consideration (`irc_197_and_noncompete.md`). With no allocated or separate payment, the whole price stays capital. Keep it that way in the PSA: do not let a dollar be itemized to the covenant.
- **Installment method (§453) applies** (`irc_453_installment.md`): gain is recognized proportionately as payments are received. Stock sale, unrelated buyer, no inventory, no recapture — no exception applies.
  - Gross profit ratio = $2,430,000 ÷ $2,850,000 = 0.85263158.
  - Closing: cash $2,350,000 × 0.85263158 = **$2,003,684.21** gain (tax ≈ $400,736.84).
  - Note: $500,000, 5 years, **annual principal** $100,000/yr → gain $100,000 × 0.85263158 = $85,263.16/yr × 5; tax $17,052.63/yr. Deferral ≈ $85,211 of 20% tax pushed out 1–5 years (≈ $13,400 of present value at a 6% assumption — real, but modest).
  - Note interest (6% on declining balance): $30,000 + $24,000 + $18,000 + $12,000 + $6,000 = **$90,000**, ordinary at 37% → **+$56,700 after tax** — extra return Hensley pays for the seller financing.
- Risks to price in: the note is **unsecured** (get security and a guaranty — §8), and the $100,000 escrow for 12 months costs about $6,000 of interest at 6%.
- **Watch for a §338(h)(10)/§336(e) election request.** Hensley's LOI keeps the S election in place through closing and asks for none. If they later want the deemed-asset-sale election, that converts the deal into an asset sale for Ray: recapture character **and** the §1374 tax land on him (`stock_vs_asset_overview.md`). Do not give the election without a material price increase (≈ $237,300 + the recapture character spread).

## 6. Non-tax difference that matters: who keeps the liabilities

- **Buyer A** assumes "only trade payables listed on a closing schedule." Everything else — unlisted payables, accrued payroll/PTO, sales-tax and franchise-tax history, tort/product/warranty claims, environmental (spray booth, dust collection), unknown claims — stays with Brightline Cabinetry LLC, i.e., ultimately with Ray's shell holding all $3.1M. There is no indemnity cap or escrow running in Ray's favor.
- **Buyer B** takes the company "with all its liabilities, known and unknown," with only a 12-month indemnity capped at 10% ($285,000) and a $100,000 escrow. That is a clean break: capped, short, and quantified.

Ray now confirms known items: the **Hardaway dispute ($9,800)** and "usual warranty stuff," unquantified ("nothing big that I know of"). Under Deal A every one of those stays in Ray's shell with the $3.1M inside it — uncapped and open-ended; $9,800 is small but the warranty tail is not quantified and the *unknown* items are the real exposure. Under Deal B they are Hensley's, with Ray's total exposure capped at the $100,000 escrow for 12 months. (If Hardaway is a disputed *receivable* rather than a claim, Class III FMV may be below face — tax-neutral: receivables at face produce no gain, and any shortfall simply shifts value to Class VII goodwill; practically, flag it in the closing schedule either way.) Texas franchise tax history (entity-level, both structures) and any further undisclosed debt remain unquantified — see QUESTIONS.md.

## 7. Recommendation and negotiating position

**Sign Hensley (Buyer B), not Lone Star as drafted.** On the stated facts Hensley nets ≈ $2,364,000 (plus ≈ $56,700 of after-tax note interest, plus the deferral benefit) with a clean liability break, versus ≈ $2,176,800 under Lone Star's own paper — Hensley wins by ≈ **$187,200+** despite being $250,000 smaller. Use Lone Star only as leverage, on these terms:

1. **Rewrite Exhibit A now** (Form 8594 consistency and *Danielson* will otherwise bind it): Class V capped at register FMV **$650,000** (each class up to FMV before the next — Treas. Reg. §1.1060-1); Class VI covenant **$0**; Class VII goodwill **$2,100,000**. Worth **$110,500** ($250,000 × 17% + $400,000 × 17%). Justification in `form_8594_counter.md`. Lone Star loses nothing on the covenant shift (VI and VII are both 15-year §197 intangibles to them) — and Ray, retiring, confirms he will sign the 5-year covenant for the same total price (`documents/email_ray.txt`), so the covenant simply stays in the PSA at **$0 allocated**: they keep the protection, he keeps the capital character. His stated indifference to the label costs him $68,000 only if the label is left as drafted.
2. **If Lone Star insists on equipment > $650,000**, every extra dollar costs Ray 17 points; charge for it (price up ≈ $17 per $100 shifted), or refuse. Ray is retiring, so real post-closing consulting is unlikely — but if Lone Star nevertheless imposes actual service obligations, those belong in a **separate services agreement priced at market outside the purchase price**, not a $400,000 price allocation (services compensation is ordinary whatever Exhibit A calls it). Show us the obligation's scope/hours before signing.
3. **Play the clock against §1374**: recognition period ends 12/31/2027. An asset-sale closing in 2028 erases the $237,300 entity tax — counter-allocated A in 2028 nets ≈ **$2,524,600** ($2,287,300 + $237,300), the only version of Deal A that beats B. If Lone Star won't wait, extract that ≈ $237,300 in price now. *(Client has no information on whether a 2028 closing is commercially possible — treat this as an untested negotiating lever, not a plan.)*
4. **If Hensley asks for a §338(h)(10)/§336(e) election**, price it: ≈ $237,300 of §1374 tax plus recapture spread (equipment gain would otherwise be ordinary to the entity — full recapture either way, so the dominant item is the BIG tax).
5. **Secure the note**: first-priority security interest in the assets or the escrow structure plus a personal/affiliate guaranty of Hensley's $500,000 obligation; confirm the $100,000 escrow releases at 12 months absent noticed claims.
6. Keep the Hensley non-compete **unpriced** (*Muskat*): no dollar amount, no separate consulting fee inside the price.
7. In Deal A only: insist on a full liability schedule; assume nothing unlisted; demand an indemnity/escrow from Lone Star for undisclosed pre-closing liabilities.

## 8. Key assumptions (state prominently)

1. Ray is a calendar individual in the 37% bracket for the year of sale; engagement rates per `capital_gain_rates.md`; no NIIT (material participation in an active business).
2. Tax bases: receivables $200,000, inventory $140,000 (book), equipment $240,000 (register), self-created goodwill and covenant $0 **[basis-in-goodwill point is unverified in the library]**; Ray's stock basis $420,000 as of 12/31/2025 — 2026 pass-throughs and distributions through closing will adjust it (they reduce Deal B's gain dollar-for-dollar; any correction moves both deals' nets only via B). **Unresolved flag:** client has no additional information on whether $420,000 is fully adjusted or on 2026 pass-throughs; Deal B's tax is therefore the conservative number (each $1 of basis not yet counted understates B's net by 20¢).
3. Equipment FMV = the register's $650,000 estimate; the 1/1/2023 appraisal is the §1374 ceiling (equipment $230,000, goodwill $900,000). **Unresolved flag:** client has no appraisal or other FMV information beyond the register, so the $650,000 ceiling in `form_8594_counter.md` stands unless Lone Star produces a competing appraisal — if one appears, re-run §7.1.
4. §1374 per the library text only: 21% on net recognized BIG, per-asset cap at conversion BIG; §1366(f)(2) pass-through loss shown as a refinement, not in headline totals.
5. The $400,000 covenant payment is ordinary to Ray whether paid to him or to the S corporation and passed through; character flows through the S corporation **[unverified pass-through mechanics — not in library]**.
6. Liabilities per Ray's answer: known items are the **Hardaway dispute ($9,800)** and "usual warranty stuff," with "nothing big that I know of." The warranty tail is **not quantified** and unknown claims are not excluded — treated as an open, uncapped exposure under Deal A and a capped one under Deal B (§6). Texas franchise tax history, further undisclosed debt, and environmental (spray booth/dust collection) exposure remain unquantified — see QUESTIONS.md. The "inventory gain is ordinary," "receivables at basis produce no gain," and "self-created goodwill has zero basis" points are treated as settled practice but lack citation in the closed library **[flagged above]**.
7. Interest computations assume the note pays 6% annually on the declining balance with level $100,000 annual principal per the LOI.
