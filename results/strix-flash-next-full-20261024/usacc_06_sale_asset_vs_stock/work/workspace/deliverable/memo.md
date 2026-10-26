# Brightline Cabinetry LLC — comparison of the Lone Star (Buyer A) and Hensley (Buyer B) offers

**To:** Ray Brightline
**Re:** $3,100,000 asset purchase vs. $2,850,000 membership-interest purchase — which one actually pays more, and what to ask for
**Prepared:** engagement deliverable 2 of 3. All citations are to files listed in `library/INDEX.md`. Anything I could not verify in the closed library is labelled **[unverified]**.

---

## 1. Bottom line

Your friend's rule — "business sales are capital gains, 20%" — is wrong for this deal, and it is wrong in a way that costs you about **$303,200** on the Lone Star paper you want to sign Friday.

| | Buyer A (Lone Star) **as drafted** | Buyer A **with my allocation** | Buyer B (Hensley) |
|---|---:|---:|---:|
| Price | 3,100,000.00 | 3,100,000.00 | 2,850,000.00 |
| Ordinary income | 1,070,000.00 | 520,000.00 | 0.00 |
| Long-term capital gain | 1,450,000.00 | 2,000,000.00 | 2,430,000.00 |
| Entity-level tax (IRC §1374) | (237,300.00) | (237,300.00) | 0.00 |
| Your personal tax | (685,900.00) | (592,400.00) | (486,000.00) |
| **Total tax** | **(923,200.00)** | **(829,700.00)** | **(486,000.00)** |
| **After-tax (price only)** | **2,176,800.00** | **2,270,300.00** | **2,364,000.00** |
| Note interest, net of tax | — | — | +56,700.00 |
| **After-tax incl. interest** | **2,176,800.00** | **2,270,300.00** | **2,420,700.00** |

**The $2.85M offer nets you $187,200 more than the $3.1M offer as drafted** — $243,900 more counting the note interest, before any adjustment for risk, time, the escrow, or who ends up carrying the company's liabilities.

Three reasons, in order of size:

1. **Built-in gains tax.** Brightline was a C corporation until it elected S status on 1/1/2023. The §1374 recognition period runs 1/1/2023 through 12/31/2027, so a 2026 asset sale triggers a **corporate-level tax of $237,300** that a stock sale avoids entirely. `library/irc_1374.md`.
2. **Buyer A's allocation turns $1,070,000 of your gain into ordinary income at 37%.** Their Exhibit A puts $900,000 on equipment whose §1245 recapture is already total, and pays you $400,000 for a non-compete, which is ordinary income to you by definition.
3. **Liability transfer.** Hensley takes the company with "all its liabilities, known and unknown." Lone Star takes only scheduled trade payables and leaves the rest — including the §1374 tax itself — in your corporation. This is worth real money and I cannot yet quantify it (see `QUESTIONS.md`).

**Do not sign the LOI Friday with Exhibit A as written.** §1060 and the *Danielson* rule mean the written allocation binds *you* too, and both sides must file Form 8594 consistently (`library/irc_1060_form_8594.md`, `library/irc_197_and_noncompete.md`). Fix the paper before you sign it, not after.

---

## 2. Why "$3.1M > $2.85M" is the wrong comparison

Buyers price asset purchases higher because *they* get a basis step-up, and stock purchases lower because *they* inherit the liabilities. `library/stock_vs_asset_overview.md` says exactly this: "Price differences between the two structures typically reflect the buyer's step-up value and assumed liabilities."

Rough check on Lone Star's side of the table (21% rate taken from §1374(b), the only corporate rate in the library — treat as an estimate): their stepped-up basis would be roughly $3,100,000 of purchase price against roughly $580,000 of Brightline's inside basis (240,000 equipment + 140,000 inventory + 200,000 receivables + 0 goodwill/covenant), i.e. a **step-up of about $2,520,000**, worth up to roughly **$529,000** of future deductions to them, undiscounted. Lone Star is paying only $250,000 more than Hensley for that. **They are getting a bargain, and they have room to pay more.** That is the single most important negotiating fact in the file.

---

## 3. Character of each gain component — Buyer A's Exhibit A, line by line

### Class III — receivables, $200,000
Buyer allocates face value. If Brightline's tax basis in the receivables equals the $200,000 carried on the books, there is **no gain**. **[Open item]** If the company reports on the cash method, the receivables have no basis and the entire $200,000 is ordinary income — **$74,000 more tax**. Method of accounting is not in the file; I asked. I have used the no-gain assumption in the headline numbers and flagged it.

### Class IV — inventory, $150,000
Gain of **$10,000, ordinary**. Inventory sold in the ordinary course is ordinary in every possible allocation, so there is nothing to negotiate here. (Note that §453 installment reporting is not available for inventory — `library/irc_453_installment.md` — irrelevant here only because Lone Star pays all cash.)

### Class V — equipment & vehicles, $900,000 — **the big problem**
From `documents/fixed_asset_register.csv`: cost $1,100,000, accumulated depreciation $860,000, **adjusted basis $240,000**, your own FMV estimate **$650,000**.

§1245(a)(1) (`library/irc_1245.md`): ordinary income = (recomputed basis, i.e. basis + depreciation allowed) minus adjusted basis, capped by the amount realized.

- Recomputed basis: 240,000 + 860,000 = **1,100,000**
- Amount realized under Exhibit A: **900,000** → lower of the two is 900,000
- Ordinary income: 900,000 − 240,000 = **$660,000 at 37% = $244,200**

Because depreciation allowed ($860,000) exceeds the entire gain, **every dollar of equipment gain is ordinary**, and the §1245 rule applies "notwithstanding any other provision." Asset-by-asset check at your register's FMVs: CNC 230,000, edgebander 71,000, spray booth 48,000, dust collection 30,000, trucks 31,000, misc 0 = $410,000, each at or below that asset's own depreciation. All ordinary.

Two further points:

- **Exhibit A's $900,000 exceeds fair market value.** Under §1060 each class is allocated *up to fair market value* before moving to the next (`library/irc_1060_form_8594.md`). Your own register says $650,000; the 2023 appraisal said $610,000. $900,000 is not defensible and, worse, *you* signed up to report it consistently.
- Pushing Class V above FMV is pure transfer from you to the buyer: **$250,000 moves from goodwill (20%) to equipment (37%)**, costing you **$42,500**, and Lone Star gains nothing (they amortize Class V and Class VII in essentially the same way).
- **[Unverified]** If the spray booth or any other item is real property, unrecaptured §1250 gain could change the rate. §1250 is not in the library, so I have not modeled it.

### Class VI — non-competition covenant (5 years), $400,000 — **the second problem**
"To the seller, payments for a covenant not to compete are **ordinary income** (compensation for refraining from competing), not capital gain." (`library/irc_197_and_noncompete.md`, citing Rev. Rul. 69-643 and *Muskat v. United States*, 554 F.3d 183 (1st Cir. 2009).) The buyer amortizes it over 15 years under §197(d)(1)(E); you get 37% treatment. Cost: **$400,000 × 37% = $148,000**, versus **$80,000** if the same dollars sat in goodwill — a **$68,000** difference.

The economic-reality test in that same library file is your argument, and the file hands it to you: **Hensley requires a 3-year non-compete as part of the purchase agreement "at no separate consideration."** Lone Star is not paying you *more* for the covenant; it is re-labelling $400,000 of the identical purchase price into the one class that is taxed worst to you and equally to them. That is a device, and the parties' own inconsistent treatment of the same covenant in two competing offers is exactly the kind of proof the library says can overcome a written allocation.

### Class VII — goodwill / going concern, $1,450,000
Basis is **zero** (the 2023 appraisal shows goodwill/trade name FMV $900,000 against basis $0, and no depreciation was ever claimed on it, so §1245 does not reach it). Gain of **$1,450,000 is long-term capital gain at 20% = $290,000** at your level — **but** see §1374 below, which taxes $900,000 of it a second time at the corporate level.

---

## 4. Built-in gains exposure (IRC §1374) — the $237,300 that "cash at closing" hides

Brightline elected C status in 2012 and S status effective **1/1/2023** (`documents/tax_history_and_conversion.md`). Per `library/irc_1374.md`:

- §1374(a), (b)(1): an S corporation with net recognized built-in gain in a taxable year **beginning in the recognition period** pays tax at the **highest corporate rate, 21%**.
- §1374(d)(7): the recognition period is the **5-year period beginning with the first day of the first taxable year for which the corporation was an S corporation** → **1/1/2023 through 12/31/2027**. A 2026 closing is inside it.
- Recognized built-in gain on an asset is **limited to that asset's built-in gain at the start of the recognition period**, which the prior CPA conveniently appraised at conversion: goodwill/trade name **$900,000**, equipment & vehicles **$230,000**, other **$0**.

Computation (same under Exhibit A and under my counter-allocation, which matters — the allocation does not change this number):

| Asset | Gain on sale (counter-allocation) | Built-in gain at 1/1/2023 | Recognized BIG |
|---|---:|---:|---:|
| Equipment & vehicles | 410,000.00 | 230,000.00 | 230,000.00 (gain exceeds the cap) |
| Goodwill / trade name | 2,000,000.00 | 900,000.00 | 900,000.00 (capped) |
| Inventory, receivables, covenant | 10,000.00 / 0 / 100,000.00 | 0 (appraisal "Other") | 0.00 |
| **Net recognized built-in gain** | | | **1,130,000.00** |

**Entity-level tax: 1,130,000 × 21% = $237,300.00**, paid by Brightline out of the sale proceeds. Note the asymmetry: the $550,000 of goodwill appreciation *after* 1/1/2023 is not built-in gain — only the pre-conversion $900,000 is. That is why the entity tax is the same whether they allocate $1,450,000 or $2,000,000 to goodwill.

Two important consequences:

1. **The §1374 tax is the price of the asset structure, not of the allocation.** No amount of re-allocating Exhibit A removes it. Only these three things do: sell the **interests** (Buyer B), close the asset sale **after 12/31/2027**, or make Lone Star pay for it.
2. The library notes the §1374 tax "is treated as a loss sustained by the S corporation (§1366(f)(2))," which passes through to you. **[Unverified]** The library gives no rule for the *character* of that loss, so I have not credited it in the headline numbers. If it shelters you at 37%, it is worth $87,801 and the net §1374 cost drops to $149,499 — which would bring a re-allocated Lone Star deal within about $5,900 of Hensley on nominal price alone (it still loses on time value, risk, and liabilities).

**[Unverified] Limits on the §1374 figure.** The library contains only §1374(a), (b), and (d)(7). It does **not** contain the §1374(d) definitions of "net recognized built-in gain," any exclusion for inventory sold in the ordinary course, or the limitation of recognized gain to the corporation's taxable income. I applied the library text as written; the real return could be somewhat lower and I cannot verify by how much. It does not change the ranking.

---

## 5. The Hensley note (IRC §453) and what the "smaller" check is really worth

Buyer B: **$2,850,000** for 100% of the membership interests — $2,350,000 cash plus a **$500,000 unsecured note, 5 years, 6%, annual principal**. The S election stays in place through closing.

At your level this is a sale of a capital asset:

- Amount realized $2,850,000 − stock basis **$420,000** = **$2,430,000, all long-term capital gain at 20% = $486,000**.
- **No §1245 recapture** (the corporation disposes of nothing), and **no §1374 entity-level tax** (same reason). Entity-level tax: **$0**.
- Because there is no recapture, the §453(i) exception in `library/irc_453_installment.md` — recapture income is recognized in the year of sale regardless of payments — **does not bite**. This is a genuine advantage of the stock sale: you defer part of the tax.

Installment mechanics (`library/irc_453_installment.md`, §453(a)):

- Gross profit fraction = 2,430,000 / 2,850,000 = **85.2632%**
- Closing year (2026): 2,350,000 × 85.2632% = **$2,003,684.21** gain → **$400,736.84** tax
- Each of years 1–5: 100,000 principal × 85.2632% = **$85,263.16** gain → **$17,052.63** tax
- Check: 2,003,684.21 + 5 × 85,263.16 = 2,430,000.00 ✓
- **Deferred out of year 1: $85,263.16 of gain, i.e. $17,053 of tax per year for five years.**

Interest on the note is ordinary income to you at 37%, not capital gain:

| Year | Balance | Interest @6% | Tax @37% |
|---|---:|---:|---:|
| 1 | 500,000 | 30,000.00 | 11,100.00 |
| 2 | 400,000 | 24,000.00 | 8,880.00 |
| 3 | 300,000 | 18,000.00 | 6,660.00 |
| 4 | 200,000 | 12,000.00 | 4,440.00 |
| 5 | 100,000 | 6,000.00 | 2,220.00 |
| | | **90,000.00** | **33,300.00** |

So the note's true after-tax yield to you is $90,000 − $33,300 = **$56,700** on deferred principal — about **3.8% per year on the average outstanding balance** ($300,000), spread over five years, on **unsecured** paper. That is why "6%" is not the answer to "what is the note worth."

Discounting every dollar at 6% (the note rate — **an assumption**, not a market rate you have confirmed): Lone Star as drafted **$2,176,800**; Lone Star with my allocation **$2,270,300**; Hensley including net interest **$2,348,289**. On a present-value basis Hensley is still ahead by **$171,500** (as drafted) or **$78,000** (with my allocation) — before any charge for the credit risk on $500,000 of unsecured paper, which is 17.5% of the price.

Other Hensley terms to price: the **$100,000 escrow** is your own money tied up for 12 months with no stated interest (about $6,000 of opportunity cost at 6%), and the **indemnity capped at 10% of price ($285,000) for 12 months** means the clean exit is not quite total. **[Unverified]** Whether that escrow is a qualified escrow account for §453 purposes is not addressed in the library; if it is not, it may be treated as payment at closing (accelerating $85,263 of gain into 2026, not changing total tax).

---

## 6. Arithmetic, shown in full

**Buyer A as drafted**
- Ordinary: inventory 10,000 + equipment 660,000 (§1245) + covenant 400,000 = **1,070,000** → × 37% = **395,900.00**
- Capital: goodwill 1,450,000 → × 20% = **290,000.00**
- Entity: (900,000 goodwill + 230,000 equipment) × 21% = **237,300.00**
- Total tax = 395,900.00 + 290,000.00 + 237,300.00 = **923,200.00**; net = 3,100,000.00 − 923,200.00 = **2,176,800.00**

**Buyer A with counter-allocation**
- Ordinary: 10,000 + (650,000 − 240,000 = 410,000) + 100,000 = **520,000** → × 37% = **192,400.00**
- Capital: 2,000,000 → × 20% = **400,000.00**
- Entity: unchanged **237,300.00**
- Total tax = **829,700.00**; net = **2,270,300.00**; saving vs. drafted = **93,500.00** = 17% × (250,000 + 300,000) ✓

**Buyer B**
- 2,850,000 − 420,000 basis = **2,430,000** capital → × 20% = **486,000.00**; entity **0**
- Net = 2,850,000.00 − 486,000.00 = **2,364,000.00**; with net interest **2,420,700.00**

**Your estimate**
- 3,100,000 × 80% = **2,480,000.00** → overstates the drafted deal by **303,200.00**

**Break-even prices for Lone Star** (they keep the same $3.1M of value for themselves; these are the prices at which *you* end up even with Hensley, nominal, price only):

| Deal shape | Price Lone Star must pay to match Hensley's $2,364,000 |
|---|---:|
| Exhibit A unchanged | **3,334,000.00** |
| My counter-allocation | **3,217,125.00** |
| My counter-allocation, matching Hensley incl. interest ($2,420,700) | **3,288,000.00** |

Each additional dollar of price under a goodwill-residual allocation is worth 80 cents to you (20% tax). So the **$234,000** of extra price needed to close the whole gap between the two offers (3,334,000 − 3,100,000) is what you are really asking Lone Star for; the allocation fix on its own is worth 17 cents on the $550,000 they mis-classified.

**Not in these numbers, and not silently netted:** the method-of-accounting question on receivables (±$74,000), trade payables and retained liabilities in either deal (unknown amounts — `QUESTIONS.md`), Texas franchise tax (the library confirms it applies but gives no rate), the cost of winding up the corporation after an asset sale (IRC §§331/336 are not in the library — **[unverified]**), and the credit risk on the Hensley note.

---

## 7. Liability differences — the part of the deal you are not pricing

| | Buyer A — asset purchase | Buyer B — membership interests |
|---|---|---|
| Liabilities assumed by buyer | "**only trade payables listed on a closing schedule**" | "**all its liabilities, known and unknown**, subject to customary reps" |
| Liabilities you keep | everything not on that schedule: warranty and jobsite-defect claims, employee claims, sales/franchise tax, contract exposure, environmental exposure from the spray booth and dust collection, plus **the $237,300 §1374 tax, paid by your corporation** | nothing beyond the reps: capped indemnity of **$285,000** for **12 months**, plus the **$100,000 escrow** |
| Entity | survives in your hands; you must then liquidate it to get the cash (untaxed analysis not possible — IRC 331/336 not in the library **[unverified]**) | disappears from your hands; the S election ends at closing when a partnership becomes the member **[unverified — no §1362 authority in the library; does not change your numbers]** |
| Collection risk | $3,100,000 all cash at closing | $2,350,000 cash; **$500,000 unsecured** seller paper |

An asset sale in the 2026 tax year also means the §1374 tax is owed **by the entity you still own**, so if the corporation's cash is inadequate you fund it personally. In the stock sale, that tax simply does not arise.

---

## 8. Recommendation

**Do not sign Buyer A's LOI on Friday.** Take Hensley's structure as your benchmark and make Lone Star pay for its own structure.

Recommended sequence:

1. **Tell Lone Star the allocation is not agreed**, and countersign Exhibit A only on the numbers in `form_8594_counter.md`: Class V **$650,000** (your own register's FMV; §1060 caps each class at FMV), Class VI **$100,000 max**, the balance to Class VII goodwill. Worth **$93,500** to you at zero cost to them.
2. **Put the §1374 tax in their column.** The asset structure costs you $237,300 that the stock structure does not. Either they raise the price to about **$3.30M** to absorb it, or you offer to close the same asset deal **in 2028**, after the recognition period ends (`library/irc_1374.md`, (d)(7)) — worth the full $237,300 to you. If Lone Star can wait, that is the cleanest fix; if they cannot, the price has to move.
3. **Kill or shrink the non-compete allocation.** Hensley gets a 3-year covenant for free; Lone Star's $400,000 of "covenant" is goodwill wearing a different hat, and it costs you $68,000 in tax. If they insist on a real 5-year covenant, price it separately on top of the purchase price rather than out of it.
4. **If you go with Lone Star, ask them to assume more liabilities** (the full balance-sheet schedule, not "listed trade payables") and to represent that no undisclosed claims exist. Retained unknown liabilities are the part of the asset deal you are being paid nothing for.
5. **If you go with Hensley:** (a) get the $500,000 note **secured** by a lien on the company's assets (worth much more than a few basis points of rate), or at least guaranteed; (b) negotiate interest to a market rate — 6% on unsecured 5-year small-business paper looks low, and note the trade-off: incremental *interest* costs you 37% while incremental *price* costs you 20%, so **prefer more price and less interest**; (c) shorten to a 2–3-year balloon with a security package rather than 5-year annual amortization; (d) put interest on the escrow, and shorten the escrow to 12 months max with the indemnity cap already at 10%; (e) **expressly prohibit any §338(h)(10) or §336(e) election without your written consent** — `library/stock_vs_asset_overview.md` notes that election converts the deal into a deemed asset sale, which would hand you the entire §1245 + §1374 problem while keeping the lower $2,850,000 price. That single clause protects the whole advantage of this deal.
6. **Get the accounting-method and payables answers** (see `QUESTIONS.md`) before either LOI is signed; the receivables question alone is ±$74,000.

If Lone Star will move to roughly **$3.2M–$3.3M with the corrected allocation and the liabilities**, they are the better deal. Short of that, **Hensley at $2,850,000 pays you more, cleaner, and with less residual risk**, even though it looks $250,000 smaller.

---

## 9. Items I could not verify from the library

Listed so you do not mistake them for advice I have confirmed: the character of the §1366(f)(2) pass-through loss; the §1374(d) definitions (net recognized built-in gain, ordinary-course inventory, taxable-income limitation); §1375 passive income tax; §1250/unrecaptured gain on any real property; §§331/336 liquidation of Brightline after an asset sale; §1362(d) termination of the S election when a partnership becomes the member; whether the Hensley escrow is a qualified escrow for §453; §453(d) security/benefits-of-benefit rules; Texas franchise tax rates; the §338(h)(10)/§336(e) mechanics. Each is flagged where it touches a number. None of them changes the direction of the recommendation.
