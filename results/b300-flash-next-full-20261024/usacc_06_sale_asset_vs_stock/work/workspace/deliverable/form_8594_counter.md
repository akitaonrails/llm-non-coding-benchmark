# Proposed Form 8594 allocation — counter-proposal to Buyer A's Exhibit A

**Matter:** Brightline Cabinetry LLC — sale of the business
**Prepared for:** Ray Brightline
**Date:** October 26, 2026
**Companion documents:** `memo.md` (full analysis), `comparison.json` (all arithmetic), `QUESTIONS.md` (open facts)

This document is the allocation we propose to put in Exhibit A and to report on Form 8594. Amounts are nominal dollars. Every line is computed in `comparison.json`; authorities are limited to the files listed in `library/INDEX.md`.

---

## 1. The rule that drives every line

Two mechanical facts control this negotiation:

1. **The price is fixed at $3,100,000.** Under the §1060 residual method, "FMV assets (Class V, VII) absorb FMV minus Classes I–IV, VI" (library: `irc_1060_form_8594`). Goodwill is therefore a **residual**: every dollar moved out of Class IV, V or VI necessarily lands in Class VII. You are never trading one ordinary line for another — you are trading ordinary dollars for capital-gain dollars.
2. **That trade is worth exactly 17 points.** Ordinary income is taxed at 37%; long-term capital gain at 20% (library: `capital_gain_rates`). So each $1 moved from Classes IV–VI to Class VII is worth **$0.17** of tax, and each $1 moved the other way **costs** $0.17. This is the unit of the entire allocation negotiation: **$17,000 per $100,000.**

The corollary for drafting: an allocation table cannot be argued line by line as if each line were independent. Lone Star's draft moves $250,000 of goodwill into equipment and $400,000 into a covenant; both moves are paid for out of the same residual.

---

## 2. Proposed allocation (counter) versus Buyer A's Exhibit A

| §1060 class | Asset | Exhibit A | **Proposed** | Δ | Adj. basis | Gain | Character | Tax at proposed |
|---|---|---:|---:|---:|---:|---:|---|---:|
| I | Cash in the company | *omitted* | **to be scheduled** | n/a | face | $0 | n/a | $0 |
| II | §331 deemed-dividend assets | — | — | — | — | — | n/a | — |
| III | Accounts receivable | $200,000 | $200,000 | $0 | $200,000 (conflict — §3.1) | $0 | — | $0 |
| IV | Inventory | $150,000 | **$140,000** | −$10,000 | $140,000 | $0 | — | $0 |
| V | Equipment and vehicles | $900,000 | **$650,000** | −$250,000 | $240,000 | $410,000 | Ordinary (§1245) | $151,700 |
| VI | Covenant not to compete | $400,000 | **$100,000** | −$300,000 | $0 | $100,000 | Ordinary | $37,000 |
| VII | Goodwill / going concern | $1,450,000 | **$2,010,000** | +$560,000 | $0 (§3.2) | $2,010,000 | Long-term capital gain | $402,000 |
| | **Total consideration** | **$3,100,000** | **$3,100,000** | | | | | |
| | Ordinary income | $1,070,000 | **$510,000** | −$560,000 | | | × 37% | $188,700 |
| | Long-term capital gain | $1,450,000 | **$2,010,000** | +$560,000 | | | × 20% | $402,000 |
| | **Shareholder-level tax** | $685,900 | **$590,700** | | | | | **$590,700** |
| | Entity-level §1374 tax | $237,300 | $237,300 | $0 | | | × 21% on $1,130,000 | **$237,300** |
| | **Total tax** | $923,200 | **$828,000** | −$95,200 | | | | **$828,000** |
| | **Net to seller** | $2,176,800 | **$2,272,000** | **+$95,200** | | | | **$2,272,000** |

**Cross-check on the change:** $560,000 moved from the 37% tier to the 20% tier = $560,000 × 17% = **$95,200**, which equals the tax reduction above. §1374 tax does not move, because both 1/1/2023 built-in-gain caps ($230,000 equipment + $900,000 goodwill and trade name = $1,130,000) were already fully absorbed at the drafted numbers, so no reallocation changes them (library: `irc_1374`; appraisal figures from `documents/tax_history_and_conversion.md`).

**How to read the per-line tax column.** The gain on each asset line is booked at that asset's own rate, and the goodwill line absorbs the entire $560,000 of shifted value at 20%. That is why the equipment line appears to save $92,500 (250,000 × 37%) rather than the $42,500 it is actually worth: the $50,000 of extra goodwill tax is shown on the goodwill line (+$112,000 on $560,000), not as an offset on the equipment line. The negotiation figures are the 17-point figures: equipment re-cut **$42,500**; covenant at $100,000 **$51,000**; covenant at $0 **$68,000**; inventory **$1,700**.

---

## 3. Justification, line by line

### 3.1 Class III — Accounts receivable, $200,000 (unchanged)

We hold the line at face value. Two documents in the file disagree about its basis: the fixed asset register states "AR method in tax basis: cash method, so basis = 0" (`documents/fixed_asset_register.csv`), while the conversion schedule carries the receivables as a $200,000 basis item (`documents/tax_history_and_conversion.md`). We present the deal on the conversion-schedule basis ($0 gain), and flag the conflict rather than resolve it: it is the largest single unknown in the engagement, and if the register is right the receivables produce $200,000 of ordinary income and every asset-sale number here falls by $74,000 (see `memo.md` §2.1 and `QUESTIONS.md`). Nothing in the library addresses basis in cash-method receivables, so we do not assert an answer.

Allocating receivables away from face is not available to either side anyway: they are worth their face amount and Class III is a non-residual class under the library's description of the classes (library: `irc_1060_form_8594`).

### 3.2 Class VII — Goodwill, $2,010,000, basis taken as $0

We model the Class VII basis as zero. The conversion schedule does show $100,000 of adjusted basis in "goodwill and trade name" at **1/1/2023** (`documents/tax_history_and_conversion.md`), but the file contains no amortization history after that date, so the 2026 remaining basis is somewhere between $0 and $100,000. Zero is the conservative figure and is used throughout; each remaining $1 of basis is worth 20 cents to you (at most $20,000). Flagged in `QUESTIONS.md`. The residual structure means a lower goodwill number is not "conservative" in any direction — it simply shifts value into ordinary income.

### 3.3 Class V — Equipment and vehicles, $650,000 (Exhibit A says $900,000)

**This is the line we will not sign as drafted.** Four reasons:

1. **It contradicts the appraisal.** The fixed asset register gives equipment and vehicles a fair market value of **$650,000**; Exhibit A allocates **$900,000** (`documents/fixed_asset_register.csv`). Under the residual method, Class V is a fair-value class — "FMV assets (Class V, VII) absorb FMV minus Classes I–IV, VI" (library: `irc_1060_form_8594`) — so the only supportable number is the appraised number. $900,000 is not a residual result; it is a chosen number, and Class VII is then forced down to $1,450,000 as the plug.
2. **It costs you $42,500 of tax.** Above adjusted basis of $240,000, gain on equipment is ordinary income up to the §1245 depreciation ceiling of $860,000 (library: `irc_1245`): "If an allocated amount exceeds adjusted basis, the excess is ordinary income up to the §1245 ceiling." The ceiling is never reached at any price here, so every dollar parked in equipment above $240,000 is ordinary at 37%. $250,000 × 17 points = **$42,500**.
3. **It buys no §1374 relief.** The 1/1/2023 built-in gain on equipment is capped at $230,000 (library: `irc_1374`), which is already fully absorbed at $650,000 or at $900,000. Over-allocating to equipment does not reduce the entity-level tax by a dollar.
4. **It is Lone Star's audit exposure, not only yours.** Exhibit A itself says the "allocation is binding and reported consistently on Form 8594," and the library states the same rule: "Buyer and seller report the allocation consistently" (library: `irc_1060_form_8594`). If Lone Star signs Form 8594 reporting $900,000 of equipment and then depreciates that basis, it is claiming $250,000 of amortizable cost basis that its own appraisal contradicts. Point this out in writing. The step-up value to Lone Star is close to identical either way — same $2,520,000 of total step-up, sheltered at 21% wherever it sits — so what the extra equipment dollars actually buy Lone Star is faster recovery of the same shield, which is a timing benefit we estimate at roughly $13,100–$15,800 of present value (5-year MACRS against 15-year §197 amortization at 21%; **recovery periods and PV tables are not in the library, so this is a labelled estimate, not an authority**). That is roughly a third of the $42,500 the line costs you in cash at closing.

### 3.4 Class VI — Covenant not to compete, $100,000 (Exhibit A says $400,000)

**Authority:** "A covenant not to compete is **ordinary income** to the recipient, not capital gain" (library: `irc_197_and_noncompete`). The same entry notes the buyer does not even get amortization on it, because §197(d)(1)(E) excludes payments for a covenant not to compete from §197 intangibles; and that the IRS tests substance — "a $0-allocated covenant with a signed covenant invites recharacterization of part of goodwill as ordinary income."

So the $400,000 line is 37% dollars for you and, for Lone Star, a non-amortizable payment that Hensley proposes to obtain **for no separate consideration** (`documents/loi_buyer_b_stock_purchase.pdf`). Cutting it to $100,000 is worth **$51,000**; cutting it to $0 is worth **$68,000**.

**Why not $0.** A signed five-year covenant with $0 allocated is the library's own description of the recharacterization fact pattern, and the exposure is unlimited-tail against a $17,000 incremental saving. $100,000 (3.2% of price) is a number you can defend. Ask for $0 with the ancillary recital as the opening rung (§5 below).

**Drafting conditions attached to this line, whichever number is agreed:**
- recite that the covenant is **ancillary and subordinate to the sale of the goodwill** of the business (library: `irc_197_and_noncompete` identifies this as the substance test that protects capital treatment of the balance);
- move any **consulting** obligation out of Exhibit A entirely. Lone Star's §4 bundles a five-year non-compete *and* a consulting agreement into the single $400,000 line. Consulting compensation is ordinary income whatever label the allocation puts on it (library: `irc_197_and_noncompete`), so bundling only manufactures ordinary income inside the purchase price. Any consulting arrangement should be a separate agreement, at market compensation, priced above and outside the purchase price.

### 3.5 Class IV — Inventory, $140,000 (Exhibit A says $150,000)

Carrying value is $140,000 (`documents/fixed_asset_register.csv`), so Exhibit A's $150,000 creates $10,000 of ordinary income for $0 of additional consideration. Worth $3,700 on this line, **$1,700** net of the goodwill residual (10,000 × 17 points). Offer it as an early concession — it is real but trivial, and it buys credibility for the two lines that matter.

### 3.6 Class I — Cash, omitted from Exhibit A

Exhibit A allocates the whole $3,100,000 to Classes III–VII. The library's class list puts cash in Class I (library: `irc_1060_form_8594`), and the LOI's financing section refers to the purchase price being "adjusted for cash," so the company holds cash at closing. Whatever that amount is, it belongs on Class I at face and must come out of the Classes III–VII stack (either out of the price, if the price is *plus* cash, or out of the residual, if it is *within* it). We cannot complete the exhibit without the number — see `QUESTIONS.md`. This is a defect in the exhibit, not a negotiating position: it must be fixed whichever allocation is agreed.

---

## 4. Accepted alternatives (same price, ranked)

| Variant | Class IV | Class V | Class VI | Class VII | Individual tax | Total tax incl. §1374 | **Net to seller** | vs Hensley $2,364,000 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Recommended counter** | $140,000 | $650,000 | $100,000 | $2,010,000 | $590,700 | $828,000 | **$2,272,000** | −$92,000 |
| Covenant at $0 (recital required) | $140,000 | $650,000 | $0 | $2,110,000 | $573,700 | $811,000 | **$2,289,000** | −$75,000 |
| Covenant at $400,000, equipment fixed at FMV | $140,000 | $650,000 | $400,000 | $1,710,000 | $641,700 | $879,000 | **$2,221,000** | −$143,000 |
| Buyer A's Exhibit A as drafted | $150,000 | $900,000 | $400,000 | $1,450,000 | $685,900 | $923,200 | **$2,176,800** | −$187,200 |

Ladder for negotiation: each $100,000 of covenant is **$17,000** of after-tax money to you, and each $100,000 of equipment overstatement is also **$17,000**.

**Fallback if Lone Star insists on Exhibit A as drafted:** the allocation is worth $95,200 to you, so keeping it costs Lone Star nothing and costs you that amount. A price increase of **$119,000 (to $3,219,000)** restores you to the counter's net of $2,272,000 exactly — the extra $119,000 falls into the Class VII residual, is taxed at 20%, and nets $95,200 ($119,000 × 80%). Present it as: *fix the allocation, or fix the price.*

**Two levers that change all of these numbers, in order of value:**
- **Close after 12/31/2027.** The §1374 recognition period (five years from the 1/1/2023 conversion) expires; entity tax goes to $0 and the counter net becomes **$2,509,300** — above Hensley even counting Hensley's note interest (library: `irc_1374`, recognition period).
- **Lone Star pays the §1374 tax.** It is an entity-level tax on the LLC that you still own after an asset sale, and Lone Star's §3 expressly leaves all debt and tax behind. **+$237,300** of price, or a dollar-for-dollar indemnity, puts Lone Star's deal in front of Hensley's on our base assumptions.

---

## 5. §1374 note for the allocation cover letter

The entity-level tax is $237,300 at **every** allocation above, and that is a feature to state out loud: it forecloses the argument that the allocation should be re-cut to "manage" the built-in-gains tax. The caps are fixed by the 1/1/2023 appraisal — $230,000 of equipment built-in gain and $900,000 of goodwill and trade-name built-in gain — and both are fully absorbed at every price and allocation in this table (library: `irc_1374`). What allocation *can* change is the shareholder-level mix, and the 17-point rule in §1 is the entire story.

We have deliberately **not** reduced the $237,300 for any §1366(f)(2) pass-through benefit in these headline figures. The library says the built-in-gains tax "passes through to the shareholders" and can be taxed at the ordinary tier (library: `irc_1366` / `irc_1374` as indexed in `library/INDEX.md`), but it does not work the arithmetic out; we quantify that credit only as a labelled sensitivity in `memo.md` §3.3–3.4 ($47,460–$87,801) rather than bank it.

---

## 6. Form 8594 and filing mechanics to fix before signature

1. **Complete the class list.** Add the Class I cash line (§3.6 above). An exhibit that allocates $3,100,000 across five classes while the company holds cash and scheduled trade payables is not a Form 8594 schedule.
2. **Consistency covenant, both directions.** Exhibit A already says the allocation "is binding and reported consistently on Form 8594" (library: `irc_1060_form_8594`: "Buyer and seller report the allocation consistently"). Add that neither party will file an allocation inconsistent with Exhibit A, and that a change requires both signatures.
3. **One return, one allocation.** Both parties file Form 8594 for the same transaction; the amounts must agree line for line. Whatever Lone Star's depreciation basis ends up being is a permanent record of what you swore the assets were worth, so no line should exceed an appraisal you would sign (`irc_1060_form_8594`).
4. **No note on this deal without a §453 check.** If Lone Star offers a seller note instead of all cash, §453(i) pulls **all** of the recapture and ordinary gain into the year of disposition, defeating the installment deferral you would be signing up for (library: `irc_453_installment`). On the counter allocation that is $510,000 of ordinary income recognized in year 1 regardless of when you are paid. Hensley's note does not have this problem, because a stock sale produces no depreciation recapture (library: `irc_453_installment`; see `memo.md` §5.3).
5. **Trade payables schedule.** Lone Star assumes only "scheduled trade payables" and no "other debt or tax" (`documents/loi_buyer_a_asset_purchase.pdf` §3). Every unscheduled payable stays with the LLC you keep. Get the schedule in dollars before signing.
6. **Sell as S-corp, not after termination.** These computations assume the entity is an S-corporation at closing and the 1/1/2023 conversion date is correct; both should be confirmed before Exhibit A is finalised (`QUESTIONS.md`).

---

## 7. One-paragraph version for the cover note

We propose: cash at face in Class I; receivables at face; inventory at carrying value $140,000; equipment and vehicles at appraised FMV $650,000; covenant not to compete $100,000, ancillary to the sale of goodwill, with consulting separately documented and separately paid; goodwill $2,010,000. Total $3,100,000, unchanged. This is the allocation the §1060 residual method produces when each class is valued at its own facts, and it is the only version of this exhibit that both parties can report on Form 8594 consistently with the appraisal in the file. If Buyer A prefers the current numbers, the price needs to rise $119,000, and the deal still loses to Hensley's stock purchase unless the built-in-gains tax is paid for or the closing is moved past 12/31/2027.
