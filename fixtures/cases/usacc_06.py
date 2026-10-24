"""USACC-6 · L3 · Selling Brightline — 'the higher offer is the better offer'."""
from decimal import Decimal as D
from generators.core import Case, money, q2, COMMON_RULES

Y = 2026
ORD, LTCG, CORP = D("0.37"), D("0.20"), D("0.21")


def build():
    c = Case("usacc_06_sale_asset_vs_stock", "usacc", "Selling the business: asset vs stock offer, allocation and built-in gains", "L3")
    price_a, price_b = D("3100000"), D("2850000")
    # Buyer A draft allocation (Form 8594 classes)
    alloc_a = {"Class III — receivables": D("200000"), "Class IV — inventory": D("150000"), "Class V — equipment & vehicles": D("900000"), "Class VI — non-compete (5 yr)": D("400000"), "Class VII — goodwill": D("1450000")}
    basis = {"receivables": D("200000"), "inventory": D("140000"), "equipment_cost": D("1100000"), "equipment_accum_depr": D("860000"), "goodwill": D("0")}
    equip_adj_basis = basis["equipment_cost"] - basis["equipment_accum_depr"]  # 240,000
    stock_basis = D("420000")
    # S election history: C corp 2012–2022; S effective 1/1/2023; conversion appraisal: goodwill FMV 900,000; equipment FMV 610,000 (adj basis then 380,000) → built-in gain equipment 230,000, goodwill 900,000
    big_goodwill, big_equip = D("900000"), D("230000")

    # ---- reference computation (asset sale, Buyer A allocation)
    gain_equip = alloc_a["Class V — equipment & vehicles"] - equip_adj_basis          # 660,000
    recapture = min(gain_equip, basis["equipment_accum_depr"])                       # 660,000 ordinary (§1245)
    gain_inv = alloc_a["Class IV — inventory"] - basis["inventory"]                  # 10,000 ordinary
    noncompete = alloc_a["Class VI — non-compete (5 yr)"]                            # 400,000 ordinary (seller)
    goodwill_gain = alloc_a["Class VII — goodwill"]                                  # 1,450,000 capital (§1231/§197 asset, basis 0)
    # §1374: recognized built-in gain limited to the net unrealized built-in gain at conversion, per asset
    big_recognized = min(goodwill_gain, big_goodwill) + min(gain_equip, big_equip)   # 900,000 + 230,000
    big_tax = q2(big_recognized * CORP)                                              # 237,300 paid by the S corp (passes through as a loss)
    ordinary_total = recapture + gain_inv + noncompete                               # 1,070,000
    tax_ord = q2(ordinary_total * ORD)
    tax_cap = q2((goodwill_gain - big_tax) * LTCG)                                   # BIG tax reduces pass-through gain (treated as loss); simplified allocation to goodwill
    total_tax_a = tax_ord + tax_cap + big_tax
    net_a = price_a - total_tax_a
    # Stock sale
    gain_b = price_b - stock_basis
    tax_b = q2(gain_b * LTCG)
    net_b = price_b - tax_b
    naive_net_a = price_a - q2((price_a - stock_basis) * LTCG)  # "it's all capital gain"
    # Counter-allocation: push non-compete to 50k, equipment to FMV 650k, goodwill up
    alloc_counter = {"Class III — receivables": D("200000"), "Class IV — inventory": D("150000"), "Class V — equipment & vehicles": D("650000"), "Class VI — non-compete (5 yr)": D("50000"), "Class VII — goodwill": D("2050000")}
    ge2 = alloc_counter["Class V — equipment & vehicles"] - equip_adj_basis  # 410,000 all recapture
    ord2 = ge2 + gain_inv + alloc_counter["Class VI — non-compete (5 yr)"]
    big2 = q2((min(alloc_counter["Class VII — goodwill"], big_goodwill) + min(ge2, big_equip)) * CORP)
    tax2 = q2(ord2 * ORD) + q2((alloc_counter["Class VII — goodwill"] - big2) * LTCG) + big2
    net_a2 = price_a - tax2

    c.doc_pdf("loi_buyer_a_asset_purchase.pdf", f"""
# LETTER OF INTENT — ASSET PURCHASE
**From:** Lone Star Millwork Holdings LLC ("Buyer") · **To:** Brightline Cabinetry LLC and Ray Brightline ("Seller") · **Date:** March 30, {Y}

1. **Transaction.** Buyer will purchase substantially all assets of Seller (receivables, inventory, equipment, vehicles, goodwill, trade name) and assume only trade payables listed on a closing schedule.
2. **Price.** **{money(price_a)}** cash at closing.
3. **Allocation.** Buyer proposes the allocation in Exhibit A, to be reported consistently by both parties on IRS Form 8594.
4. **Non-competition.** Ray Brightline will enter a 5-year non-competition and consulting agreement; **{money(alloc_a['Class VI — non-compete (5 yr)'])}** of the price is allocated to it.
5. Non-binding except confidentiality and exclusivity (45 days).

**Exhibit A — Proposed allocation**

| Class | Asset | Amount |
|---|---|---:|
{chr(10).join(f"| {k.split(' — ')[0]} | {k.split(' — ')[1]} | {money(v)} |" for k, v in alloc_a.items())}
| | **Total** | **{money(sum(alloc_a.values()))}** |
""")
    c.doc_pdf("loi_buyer_b_stock_purchase.pdf", f"""
# LETTER OF INTENT — PURCHASE OF MEMBERSHIP INTERESTS
**From:** Hensley Family Partners LP ("Buyer") · **To:** Ray Brightline ("Seller") · **Date:** April 2, {Y}

1. Buyer will purchase 100% of the membership interests of Brightline Cabinetry LLC. The company's S corporation election remains in place through closing.
2. **Price:** **{money(price_b)}**, of which $2,350,000 cash at closing and **$500,000 by unsecured promissory note** of Buyer, 5 years, 6% interest, annual principal.
3. Buyer assumes the company with all its liabilities, known and unknown, subject to customary representations, a 12-month indemnity capped at 10% of price, and a $100,000 escrow.
4. No non-compete payment; Seller signs a customary 3-year non-compete as part of the purchase agreement at no separate consideration.
""")
    c.doc("fixed_asset_register.csv", "asset,placed_in_service,cost,accumulated_depreciation,adjusted_basis,fmv_estimate\nCNC router (Biesse),2019,420000,420000,0,230000\nEdgebander,2020,180000,156000,24000,95000\nSpray booth,2021,140000,98000,42000,90000\nDust collection,2018,95000,95000,0,30000\nVehicles (3 trucks),2022-2024,165000,61000,104000,135000\nShop equipment misc,various,100000,30000,70000,70000\nTOTAL,,1100000,860000,240000,650000\n")
    c.doc("tax_history_and_conversion.md", f"""
# Brightline Cabinetry LLC — tax history (from the prior CPA's file)

- Formed 2012 as a Texas LLC; **elected to be taxed as a C corporation** (Form 8832) in 2012 at the lender's request.
- **Elected S corporation status effective January 1, 2023** (Form 2553 accepted). At conversion, the CPA obtained an appraisal for built-in-gain purposes:

| Asset | FMV at 1/1/2023 | Adjusted basis at 1/1/2023 | Built-in gain |
|---|---:|---:|---:|
| Goodwill / trade name | {money(big_goodwill)} | 0 | {money(big_goodwill)} |
| Equipment & vehicles | 610,000 | 380,000 | {money(big_equip)} |
| Other | — | — | 0 |

- Ray's basis in his membership interests (stock basis) as of 12/31/{Y-1}: **{money(stock_basis)}**.
- No net operating losses. Texas: no personal income tax; franchise tax applies to the entity.
- Inventory (materials) carrying value {money(basis['inventory'])}; receivables {money(basis['receivables'])} (no reserve).
""")
    c.doc("email_ray.txt", f"""
From: Ray Brightline
Subject: two offers — I'm taking the $3.1M

Lone Star is at {money(price_a)} cash, Hensley at {money(price_b)} with part of it on a note. Seems obvious.
My buddy says business sales are capital gains, 20%, so I net about $2.5M on the big one. Can you
confirm and look over their allocation thing? They said it's "standard". I want to sign the LOI Friday.
""")

    # ---- library
    c.library("irc_1245.md", "IRC §1245 — gain from dispositions of certain depreciable property", "26 U.S.C. §1245(a)(1)", "If section 1245 property is disposed of, the amount by which the lower of (A) the recomputed basis of the property, or (B) the amount realized, exceeds the adjusted basis of such property **shall be treated as ordinary income**. (Recomputed basis = adjusted basis plus depreciation allowed or allowable.) Such gain is recognized notwithstanding any other provision of this subtitle.", verbatim=False)
    c.library("irc_1374.md", "IRC §1374 — tax imposed on certain built-in gains", "26 U.S.C. §1374(a), (b), (d)(7)", "(a) If for any taxable year beginning in the **recognition period** an S corporation has a net recognized built-in gain, there is imposed a tax (computed under subsection (b)) on the income of such corporation for such taxable year. (b)(1) The tax is the highest corporate rate (**21%**) on the net recognized built-in gain. (d)(7) The recognition period is the **5-year period beginning with the first day of the first taxable year for which the corporation was an S corporation**. Recognized built-in gain on an asset is limited to the asset's built-in gain at the start of the recognition period. The tax paid is treated as a loss sustained by the S corporation (§1366(f)(2)).", verbatim=False)
    c.library("irc_197_and_noncompete.md", "IRC §197 and covenants not to compete", "26 U.S.C. §197(d)(1)(E); Rev. Rul. 69-643; *Muskat v. United States*, 554 F.3d 183 (1st Cir. 2009)", "A covenant not to compete entered into in connection with the acquisition of a trade or business is a section 197 intangible amortizable by the buyer over 15 years. **To the seller, payments for a covenant not to compete are ordinary income** (compensation for refraining from competing), not capital gain. Allocation between a covenant and goodwill must reflect economic reality; the parties' written allocation is binding on them (§1060(a); *Danielson* rule) absent strong proof, and the IRS may challenge it.", verbatim=False)
    c.library("irc_1060_form_8594.md", "IRC §1060 and Form 8594 — residual method", "26 U.S.C. §1060; Treas. Reg. §1.1060-1; Form 8594 Instructions", "In an applicable asset acquisition, consideration is allocated under the residual method among seven classes in order: I cash; II actively traded personal property; III mark-to-market assets and receivables; IV inventory; V all other assets (equipment, real property); VI section 197 intangibles other than goodwill (including covenants not to compete); VII goodwill and going concern value. Each class is allocated up to fair market value before moving to the next. **Buyer and seller must each file Form 8594 and report consistently** with any written allocation agreement.", verbatim=False)
    c.library("irc_453_installment.md", "IRC §453 — installment method", "26 U.S.C. §453(a), (b), (i)", "Income from an installment sale is taken into account under the installment method (gain recognized proportionately as payments are received), **except** that recapture income under §1245 is recognized in the year of sale regardless of payments (§453(i)), and the method is not available for inventory or for sales of depreciable property to related persons.", verbatim=False)
    c.library("capital_gain_rates.md", f"{Y} individual rates used in this engagement", "IRC §1(h), §1(j); §1411", "For this engagement use: ordinary income marginal rate **37%**; long-term capital gain **20%**; the 3.8% net investment income tax does **not** apply to gain from an active trade or business in which the taxpayer materially participates. Texas has no individual income tax.", verbatim=False)
    c.library("stock_vs_asset_overview.md", "Stock vs asset sale — tax and liability overview", "Practitioner summary", "Stock (membership-interest) sale: seller recognizes capital gain on the difference between price and stock basis; buyer takes carryover basis in assets (no step-up unless a §338(h)(10)/§336(e) election, which converts the deal to a deemed asset sale with asset-sale consequences to the seller); buyer inherits all liabilities. Asset sale: gain computed asset by asset under the allocation; recapture and covenant payments are ordinary; buyer gets a basis step-up; S corporations within the §1374 recognition period owe entity-level built-in gains tax. Price differences between the two structures typically reflect the buyer's step-up value and assumed liabilities.", kind="practice aid")

    c.contract(f"""
# Engagement: compare the two offers for Brightline Cabinetry — Ray Brightline

Ray wants to sign Buyer A's LOI on Friday because {money(price_a)} > {money(price_b)} and "business sales
are capital gains". Give him the real comparison and a negotiating position.

## Deliverables (under `workspace/deliverable/`)
1. `comparison.json` — `{{"asset_sale_buyer_a_as_drafted": {{"ordinary_income": 0, "capital_gain": 0, "entity_level_tax": 0, "total_tax": 0, "net_after_tax": 0}}, "stock_sale_buyer_b": {{...}}, "asset_sale_counter_allocation": {{...}}, "ray_naive_estimate": {{"net_after_tax": 0}}}}`
2. `memo.md` — the analysis: character of each gain component with authority, built-in gains exposure, the installment note, liability differences, and a recommendation with negotiating points.
3. `form_8594_counter.md` — your proposed allocation by class with justification.
4. `QUESTIONS.md` (optional), `STATUS.md`.
{COMMON_RULES}
""")
    c.client_script("Ray Brightline, decisive, impatient, trusts his buddy.", [
        {"id": "noncompete_term", "trigger": ["non-compete", "noncompete", "longer term", "consult", "stay on"], "answer": "I'd sign 5 years, I'm retiring. I don't care what they call the payment as long as the total is the same.", "if_not_asked": "none"},
        {"id": "note_security", "trigger": ["note", "secured", "collateral", "Hensley credit"], "answer": "The $500k note is unsecured. Hensley's a family office, seems solid, but I don't know their balance sheet.", "if_not_asked": "none"},
        {"id": "liabilities", "trigger": ["liabilities", "warranty", "claims", "lawsuit", "Hardaway"], "answer": "There's the Hardaway dispute ($9,800) and the usual warranty stuff. Nothing big that I know of.", "if_not_asked": "none"},
    ], pushback=[{"when": "if the memo recommends against signing Buyer A as drafted", "message": "Ray: You're telling me the offer that's $250k higher nets me LESS? That makes no sense. Walk me through it like I'm five, and tell me what number from Lone Star would actually beat Hensley."}])

    ref = {"asset_sale_buyer_a_as_drafted": {"ordinary_income": ordinary_total, "capital_gain": goodwill_gain - big_tax, "entity_level_tax": big_tax, "total_tax": total_tax_a, "net_after_tax": net_a,
                                             "components": {"1245_recapture": recapture, "inventory": gain_inv, "noncompete": noncompete, "big_recognized": big_recognized}},
           "stock_sale_buyer_b": {"ordinary_income": 0, "capital_gain": gain_b, "entity_level_tax": 0, "total_tax": tax_b, "net_after_tax": net_b, "note": "$500k unsecured note; §453 defers part of the gain; credit risk; indemnity cap 10%"},
           "asset_sale_counter_allocation": {"allocation": {k: str(v) for k, v in alloc_counter.items()}, "ordinary_income": ord2, "entity_level_tax": big2, "total_tax": tax2, "net_after_tax": net_a2},
           "ray_naive_estimate": {"net_after_tax": naive_net_a, "error": "treats everything as 20% capital gain; ignores §1245, non-compete character, §1374"},
           "breakeven_note": "Reviewer: the model should state what asset price (or allocation) makes A ≥ B after tax; accept any correct computation within ±$25k."}
    c.reference("reference.json", ref)
    c.trap(1, "All capital gain", f"Netting {money(naive_net_a)} on Buyer A", f"§1245 recapture {money(recapture)} and the non-compete {money(noncompete)} are ordinary; net after tax {money(net_a)} vs stock sale {money(net_b)}", "Fixed-asset register (accumulated depreciation 860k); LOI A ¶4", "Seller picks the offer that nets less", "C", "§1245; Rev. Rul. 69-643; §197", "high")
    c.trap(2, "Built-in gains tax ignored", "No entity-level tax in the asset-sale comparison", f"S election effective 1/1/2023 → recognition period runs through 2027; built-in gain on goodwill {money(big_goodwill)} and equipment {money(big_equip)} taxed at 21% = {money(big_tax)}", "Tax history memo; conversion appraisal", "Six-figure surprise tax", "C", "§1374", "high")
    c.trap(3, "Accepting Buyer A's allocation", "Reporting Exhibit A as 'standard'", "Equipment allocated above FMV (900k vs 650k) and a 400k covenant maximize the buyer's fast deductions and the seller's ordinary income; counter-allocation shifts to goodwill", "Register FMV column; Exhibit A", "Avoidable ordinary income", "H", "§1060; Form 8594", "high")
    c.trap(4, "Installment note ignored", "Treating B as $2.85M cash", "$500k unsecured note: §453 deferral, credit risk, interest; recapture (if any) not deferrable", "LOI B ¶2", "Wrong comparison", "M", "§453", "high")
    c.trap(5, "Liability assumption not priced", "Ignoring that B takes all liabilities and A assumes only listed payables", "Part of the price gap is rational", "LOI A ¶1 vs LOI B ¶3", "—", "M", "Practice aid", "high")
    c.oracle("asset_sale_buyer_a_as_drafted.net_after_tax", str(net_a), "±$25,000", "comparison.json")
    c.oracle("stock_sale_buyer_b.net_after_tax", str(net_b), "±$10,000", "")
    c.oracle("entity_level_tax (BIG) present and ≈", str(big_tax), "±$15,000", "")
    c.oracle("ordinary income in A includes recapture + non-compete", str(ordinary_total), "±$10,000", "")
    c.oracle("Recommendation: do not sign A as drafted; counter on allocation/price or take B", "true", "exact", "memo.md")
    c.rubric("Pushback answered with a plain-language walk-through and a break-even number")
    return c.finish()
