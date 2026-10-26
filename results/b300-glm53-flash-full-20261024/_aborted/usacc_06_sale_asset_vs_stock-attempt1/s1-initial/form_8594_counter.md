# Counter-proposal to Exhibit A — Form 8594 allocation, Lone Star Millwork Holdings asset purchase

**Rule set (library only):** `library/irc_1060_form_8594.md` (§1060; Treas. Reg. §1.1060-1; Form 8594 Instructions) — residual method, seven classes in order, **each class filled up to FMV before moving to the next**; Class III receivables, Class IV inventory, Class V all other assets (equipment), Class VI §197 intangibles **other than goodwill (including covenants not to compete)**, Class VII goodwill. Both parties file Form 8594 and report consistently with any written allocation (`stock_vs_asset_overview.md` adds the step-up to buyer; `irc_197_and_noncompete.md` adds that the written allocation binds absent strong proof and may be IRS-challenged if it ignores economic reality).

**Total consideration: unchanged at $3,100,000.** This is a re-characterization of Buyer A's own papers, not a price negotiation.

## Buyer A's Exhibit A vs. counter

| Class | Buyer's Exhibit A | Counter | Difference | Justification |
|---|---:|---:|---:|---|
| I cash | — | — | — | No cash acquired |
| II actively traded property | — | — | — | None |
| III receivables | 200,000 | **200,000** | — | FMV = carrying value $200,000, no reserve (`documents/tax_history_and_conversion.md`); gain to seller $0 |
| IV inventory | 150,000 | **150,000** | — | Buyer's FMV figure kept (FMV, not carrying value $140,000, governs). Seller-side gain $10,000 ordinary; disputing saves at most 10,000 × (37% − 20%) = $1,700 — not worth the fight |
| V equipment & vehicles | 900,000 | **650,000** | −250,000 | Class V may only be filled to FMV. Buyer's $900,000 exceeds the seller's documented FMV of **$650,000** (`documents/fixed_asset_register.csv`; adjusted basis 240,000, accumulated depreciation 860,000). To the seller this overstatement produced $250,000 of extra §1245 ordinary income at 37% rather than capital gain at 20% (`library/irc_1245.md`) |
| VI covenant not to compete | 400,000 *labeled "Class V"* | **400,000** | relabel | A covenant not to compete is a **Class VI** §197 intangible (`irc_1060_form_8594.md`); payments to the seller are **ordinary income** (`irc_197_and_noncompete.md`). Amount held at Buyer's $400,000 figure; any change must reflect economic reality per `irc_197_and_noncompete.md` — and Ray's retirement changes that calculus (see the optional variant below) |
| VII goodwill/going concern | 1,450,000 | **1,700,000** | +250,000 | **Residual:** 3,100,000 − (200,000 + 150,000 + 650,000 + 400,000) = 1,700,000. Under the residual method the price over Class V's $650,000 FMV belongs in the residual class |
| **Total** | **3,100,000** | **3,100,000** | — | Balances — no forced balancing beyond the LOI price |

## Effect on Ray (why the counter matters)

- §1245 recapture: 660,000 → 410,000 (650,000 − 240,000; still all ordinary because depreciation $860,000 exceeds the gain, `irc_1245.md`).
- Ordinary income to Ray: 1,070,000 → **820,000**; capital gain → **1,622,700**; entity §1374 tax unchanged at **$237,300** (built-in gain is per-asset, lesser-of: goodwill $900,000, equipment $230,000 — `irc_1374.md`).
- Individual tax 303,400 + 324,540 = 627,940; total tax **865,240**; **net after tax $2,234,760** — up **$42,500** (= 250,000 × (37% − 20%)) from the drafted allocation. Aggregate income check: 820,000 + 1,622,700 = 2,442,700 = cash 2,862,700 − basis 420,000 ✓.

## Buyer-side note (honesty about Buyer A's likely pushback)

Buyer A takes a step-up basis in every class (`stock_vs_asset_overview.md`) totaling the same $3,100,000 either way, but the mix shifts $250,000 from equipment to goodwill, and Buyer A may claim it prefers the faster recovery equipment basis offers. Recovery-period speeds for equipment are **not in the library (labeled unverified)**; the covenant amortizes for the buyer over 15 years (`irc_197_and_noncompete.md`). If Buyer A insists, the quantified fallback is stated in the memo: every $100,000 restored to Buyer A's Class V number costs Ray $17,000 of tax.

## Consistency mechanics

- This allocation must appear in the **signed written agreement** to be binding between the parties (`irc_197_and_noncompete.md`, §1060(a); *Danielson* rule) and to drive consistent Form 8594 filings (`irc_1060_form_8594.md`).
- Do not sign Buyer A's non-binding LOI with its Exhibit A intact: once both sides sign an allocation, they report consistently per `irc_1060_form_8594.md`, and the written allocation binds absent strong proof (`irc_197_and_noncompete.md`).
- Cap open: any class allocation above FMV is too high by construction (`irc_1060_form_8594.md`); the covenant figure must be supportable as economic reality (`irc_197_and_noncompete.md`).

## Optional variant — move the covenant into Class VII goodwill (client confirmed retiring; requires Buyer A's written agreement)

This round Ray confirmed: *"I'd sign 5 years, I'm retiring. I don't care what they call the payment as long as the total is the same."* A retiring seller changes the economic-reality calculus the library requires for the covenant/goodwill split (`irc_197_and_noncompete.md`): a covenant from a seller who is leaving the industry entirely restrains little beyond what the goodwill purchase already buys, so pricing it at nearly zero above goodwill is the allocation the facts support. The label is also worth real money — covenant dollars are ordinary at 37%, goodwill dollars capital at 20% — so moving all $400,000 saves 400,000 × (37% − 20%) = **$68,000** ($17,000 per $100,000 on any partial move the buyer will accept).

| Class | Base counter | Retiring-seller variant |
|---|---:|---:|
| III receivables | 200,000 | 200,000 |
| IV inventory | 150,000 | 150,000 |
| V equipment & vehicles | 650,000 | 650,000 |
| VI covenant not to compete | 400,000 | **0** |
| VII goodwill/going concern | 1,700,000 | **2,100,000** (residual: 3,100,000 − 1,000,000 of III–V) |
| **Total** | **3,100,000** | **3,100,000** |

Mechanics: the $400,000 then flows to the entity with the rest of the price (no separate direct payment to Ray). The §1374 entity tax is unchanged at **$237,300** — goodwill stays at its lesser-of cap min(900,000 built-in gain; 2,100,000 allocated) = 900,000, equipment at 230,000 (`irc_1374.md`). Ray's ordinary income drops to **420,000** (inventory 10,000 + equipment 410,000) and capital gain rises to **2,022,700**; total tax **797,240**; **net after tax $2,302,760** (+68,000 vs the base counter). Aggregate check: 420,000 + 2,022,700 = 2,442,700 = receipts to Ray's level 2,862,700 − basis 420,000 ✓.

Conditions and caveats — this is optional, not the primary ask:
1. **Buyer A must agree in the signed written allocation.** Both parties report consistently and the written allocation binds absent strong proof (`irc_1060_form_8594.md`; `irc_197_and_noncompete.md`); no one relabels unilaterally. Ray's "I don't care what they call it" is worth repeating to Buyer A, but the tax value of the label is $68,000 — which is **his** money, so the ask is worth making.
2. **The IRS may challenge allocations that ignore economic reality in either direction** (`irc_197_and_noncompete.md`). The support here is Ray's retirement; document it, and if the facts change (e.g., Ray stays active in the trade), drop the variant.
3. Buyer A's likely counter: goodwill already prices the competitive risk, so a covenant premium hidden in goodwill doubles counts. The fallback ladder (base counter nets $2,234,760; covenant-only fix on Buyer A's own Exhibit A nets $2,260,260; full variant $2,302,760) is in `memo.md` §10.1 — Buyer B at $2,364,000 still beats the best case by $61,240, plus the liability-tail point of §10.2.
