Ray's math confusion is real — and answerable precisely. Let me pull the memo and the calc script so I can walk him through it with the exact tied-out numbers and compute the Hensley-beating price.

Ray deserves both a plain-language walk-through and a hard number. The old calc script is gone from /tmp, so let me rebuild the arithmetic and solve for the Hensley-beating price properly rather than eyeballing it.

The assert-and-print combo is buggy (print returns None). Quick fix:

Everything ties — the memo's three base nets reproduce exactly, the entity tax stays pinned at 237,300 in every future-price case, and the breakevens are solved. Logging the new analysis into the deliverables, then walking Ray through it.

§8 item 4 is in. Now the §10 bottom-line row, the client-log entry, and the STATUS addendum:

Ray's instinct is right — it *should* feel backwards until you see that the two offers aren't two numbers, they're two routes through the tax toll plaza. Here's the walk-through, and the answer to his pricing question.

---

## Why $3.1M pays less than $2.85M (the five-year-old version)

**Hensley's deal = one toll booth.**
Hensley buys the whole piggy bank. You paid 420,000 to build it; he's paying 2,850,000; profit 2,430,000; the taxman takes one bite at 20%. You keep **2,364,000**. Done.

**Lone Star's deal = three toll booths before the money reaches you.**

1. **The gate toll (the one his buddy never counted):** the company itself owes **237,300** because of the 2023 S-conversion (§1374). It's paid out of the sale price before anything hits Ray's pocket — so a "$3.1M" offer is really a "$2.86M-after-the-gate" offer.
2. **The expensive lane:** the drafted Exhibit A puts **1,070,000 — 34.5 cents of every dollar — into buckets taxed at 37%** (equipment "clawback" 660,000, covenant paid to Ray by name 400,000, inventory 10,000).
3. **Only 1,450,000 gets the cheap 20% lane** (goodwill), and 200,000 (receivables) passes toll-free.

**The ledger:**

| | Hensley (stock) | Lone Star (asset, as drafted) |
|---|---:|---:|
| Price | 2,850,000 | 3,100,000 |
| Gate toll (company) | — | −237,300 |
| Bites on Ray | −486,000 (20% × everything) | −630,229 (37% and 20% lanes) |
| **In your pocket** | **2,364,000** | **2,232,471** |

**The flip, in one line:** the extra 250,000 of price comes attached to **381,529 more tax** → 250,000 − 381,529 = **−131,529**. Lone Star pays $250k more *to the borrower's taxman, not to Ray*. The offer is a route, not a number.

---

## What number from Lone Star actually beats Hensley

Above the current price, the gate toll can't grow (it's capped by the 2023 valuations at 237,300 no matter how big the price), so each extra dollar is taxed only by whichever bucket it lands in: **20 cents** if it lands in goodwill (Ray keeps 80¢), **37 cents** if it lands in the ordinary buckets (63¢), or ~26.7¢ on average if the whole Exhibit A rescales. Solving for the crossing point:

| Lone Star pays... | Price needed just to TIE 2,364,000 | New money over 3.1M |
|---|---:|---:|
| **with your counter allocation** (raise → goodwill) | **3,145,411** | **+45,411** |
| as drafted, raise lands in goodwill | 3,264,411 | +164,411 |
| as drafted, whole Exhibit A rescales | ≈3,279,345 | +179,345 |
| as drafted, raise lands in ordinary buckets | ≈3,308,776 | +208,776 |

(Not fixed by the LOI: where a renegotiated price increase would land in Exhibit A — hence the bracket.)

**The punchline Ray can use:** the allocation counter is worth **119,000 of gross price to him** (95,200 ÷ 0.8). With it, Lone Star beats Hensley for just **+45,411**. Without it, they'd need **+164,000 to +209,000** — and any Lone Star raise, of course, costs them real cash either way.

Two honest footnotes:
- Counting Hensley's 90,000 note interest (56,700 net), the tie price with the counter is **3,216,287** — Hensley keeps a standing edge in any exact tie, on top of the unsecured-note timing value and liability armor.
- The other lever works too: Hensley repriced **+46,000 → 2,896,000 nets 2,400,800**, which beats every version of A. So the play is still: counter A's allocation (free +95,200), use A's number to lift B to ~2.9M, take whoever lands higher.

Deliverables updated: breakeven table added to `memo.md` §8(4) and §10, logged in `QUESTIONS.md`, `STATUS.md` addendum added (still COMPLETE WITH OPEN ITEMS). All crossings verified — tax + net = price holds at every point, entity tax stays 237,300 throughout.