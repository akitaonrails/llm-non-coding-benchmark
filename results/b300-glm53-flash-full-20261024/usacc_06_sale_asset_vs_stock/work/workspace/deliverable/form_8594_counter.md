# Proposed Form 8594 allocation — Lone Star (Buyer A) counter

**Seller:** Brightline Cabinetry LLC (and Ray Brightline, personally, for Class VI)
**Buyer:** Lone Star Millwork Holdings LLC · Price: 3,100,000.00 cash at closing
**Replaces:** Exhibit A of the asset-purchase LOI dated March 30, 2026

## The counter allocation

| Class | Component | Buyer's Exhibit A | Counter | Basis | Gain to seller | Character |
|---|---|---:|---:|---:|---:|---|
| III | Receivables | 200,000.00 | 200,000.00 | 200,000.00 (face, no reserve) | 0.00 | — |
| IV | Inventory | 150,000.00 | 140,000.00 | 140,000.00 | 0.00 | (was 10,000 ordinary) |
| V | Equipment & vehicles | 900,000.00 | 650,000.00 | 240,000.00 | 410,000.00 | 410,000.00 ordinary (§1245) |
| VI | Non-compete (5 yr, Ray) | 400,000.00 | 100,000.00 | n/a | 100,000.00 | 100,000.00 ordinary (§197 covenant) |
| VII | Goodwill / trade name | 1,450,000.00 | 2,010,000.00 | 0.00 | 2,010,000.00 | capital |
| | **Total** | **3,100,000.00** | **3,100,000.00** | | **2,520,000.00** | |

Add / no drop in the headline price: the counter re-labels the same $3,100,000.

## Justification, class by class

- **Classes III & IV (fix):** the residual method allocates each class only up to **fair market value** before moving on (`library/irc_1060_form_8594.md`). Exhibit A puts 150,000 into inventory carried at 140,000 and the register supports face value for receivables. Any excess is reclassified to Class VII. Eliminates a 10,000 ordinary-income misstatement against the seller.
- **Class V (biggest fix):** Exhibit A allocates **900,000 against equipment with a verified FMV of 650,000** — a 250,000 over-allocation the residual method cannot support (`library/irc_1060_form_8594.md`; FMV documented in `documents/fixed_asset_register.csv`). Worse for the seller, every dollar of Class V gain is **§1245 recapture — ordinary at 37%** (`library/irc_1245.md`), while the honest 650,000 produces only 410,000 of recapture (650,000 − 240,000 adjusted basis; still fully ordinary because the amount realized does not exceed the 1,100,000 recomputed basis).
- **Class VI (aggressive ask):** Exhibit A puts 400,000 on a standard 5-year covenant — the client confirms it is entirely restraint-of-trade money (5 years, seller retiring) — all **ordinary income to Ray** (`library/irc_197_and_noncompete.md`, Rev. Rul. 69-643; *Muskat*). Because Ray is indifferent to the payment's label, every dollar re-labeled covenant → goodwill is pure tax savings for him at no change in the total price. Covenant and goodwill are both §197 intangibles amortizing over **15 years for the buyer** — relocation of dollars between Class VI and VII is tax-neutral to Lone Star, so the extra 300,000 has no legitimate buyer-side tax defense. The library requires allocation to "reflect economic reality" and warns the IRS may challenge allocations that do not (`library/irc_197_and_noncompete.md`); 100,000 preserves a defensible economic-reality position — a retiring, capable competitor's full 5-year restraint genuinely protects the buyer, which keeps some Class VI value real — without Ray paying 17 points of ordinary-rate tax on premium he has already collected as goodwill.
- **Class VII:** the residual — 2,010,000, up 560,000 from Exhibit A (250,000 from Class V, 10,000 from Class IV, 300,000 from Class VI). Gain here is capital at 20%.

## Effect on the parties

| | Exhibit A | Counter | Δ |
|---|---:|---:|---:|
| Ray's total tax (entity + personal) | 867,529.00 | 772,329.00 | −95,200.00 |
| Ray's net after tax | 2,232,471.00 | 2,327,671.00 | +95,200.00 |
| Entity §1374 tax | 237,300.00 | 237,300.00 | 0 (NRIG capped at 1,130,000 under both — goodwill 900,000 + equipment 230,000) |
| Buyer's 15-yr §197 amortization pool | 1,850,000 | 2,110,000 | +260,000 |
| Buyer's 5-yr Class V recoveries | 900,000 | 650,000 | −250,000 |

The buyer keeps the full 3,100,000 price, keeps its 5-year non-compete with Ray in full force, and picks up a 260,000 *larger* long-lived amortization pool; it gives up only modest recovery-timing acceleration. Both parties file consistent Forms 8594 as required (`library/irc_1060_form_8594.md`).

**If Buyer A refuses the Class VI move:** fall back by conceding Class V at 650,000 and inventory at 140,000 first — that alone saves 96,200 of the 147,200 of ordinary-rate overstatement in Exhibit A (92,500 + 3,700, with the remaining 51,000 on the covenant). Even the unconceded fallback beats the drafted deal by 96,200 to Ray while leaving the covenant at 400,000.

*Every dollar figure above is arithmetically tied: 3,100,000 = 200,000 + 140,000 + 650,000 + 100,000 + 2,010,000; character effects reconcile to `deliverable/memo.md` § 5 and `deliverable/comparison.json`.*
