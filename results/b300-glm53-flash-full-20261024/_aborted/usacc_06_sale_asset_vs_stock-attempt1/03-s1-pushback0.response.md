Great question from Ray — and it deserves a real answer with numbers, not a shrug. Let me compute the break-even prices first, then update the deliverables so this walkthrough is on the record.

The key identity I'll verify: in *any* Lone Star asset deal, each extra price dollar lands in Class VII goodwill at 20% — Ray keeps 80¢. So "beat Hensley" = solve 0.80·P − structure_drag = 2,364,000, and the drag differs by allocation (287,740 drafted / 245,240 counter / 177,240 variant):

Math verified three independent ways — now let me put this on the record in the deliverables, then give Ray the plain-English answer.

All three verified. Now recording the walkthrough in the deliverables — three independent file edits in parallel:

Ray — you're right that it *seems* backwards. Here's the trick: you don't get the offer, you get the offer **minus tax**, and the two buyers' deals get taxed in completely different ways.

## Like I'm five: think of "converters"

Every dollar of offer goes through a converter before it reaches your pocket:

- **Hensley's converter gives you 83 cents.** They buy the *whole company* (stock). The tax code sees one simple event: you sold for $2,850,000 something that cost you $420,000 (your basis). One tax, at the lowest rate: ($2,850,000 − $420,000) × 20% = $486,000. You net **$2,364,000**.
- **Lone Star's converter gives you 71 cents.** They buy the *pieces* (equipment, inventory, covenant, goodwill) and leave most liabilities behind. Two extra tolls come out before the money gets to you:
  1. **The company pays its own tax first: $237,300.** Selling assets within 5 years of converting to an S corp (your window runs to 12/31/2027) triggers tax on the company's old, never-taxed gains. Hensley buying stock never triggers this — it vanishes.
  2. **Big chunks of your money are taxed at 37%, not 20%.** The equipment profit ($660,000 of depreciation recapture) and the $400,000 covenant are "ordinary income," not capital gain. As drafted, $1,070,000 of your money gets the 37% rate.

So: Lone Star pays you $250,000 more on the sticker, but their converter wastes 29¢ of every dollar where Hensley wastes 17¢. The bigger pile runs through the worse converter and comes out **smaller: $2,192,260 vs $2,364,000**. (Your own estimate of $2,480,000 assumed the plain 80¢-per-dollar rule — the $287,740 gap to reality is exactly what the asset structure adds.)

## The killer detail: their bonus $250k is only worth $200k

In *(any)* asset deal, every extra price dollar lands in goodwill at the 20% rate — **you keep exactly 80¢ of it, no more**. So their $250,000 premium buys you $200,000. Meanwhile, at the *same* price, the A structure would trail Hensley by $371,740 ($237,300 company tax + $134,440 rate drag on the 37% chunks). $200,000 < $371,740 — they're short $171,740, which is precisely the ledger gap. To fill that hole at 80¢ per added dollar, they have to add $464,675 of price.

## What number from Lone Star actually beats Hensley

Solve 0.80 × price − structure toll = $2,364,000 (each row verified forward):

| If Lone Star accepts… | They must offer | vs their $3.1M |
|---|---:|---:|
| Their Exhibit A as written | **$3,314,675** | +$214,675 |
| The Class V equipment correction ($650,000, per the register) | **$3,261,550** | +$161,550 |
| That **plus** putting the $400,000 in goodwill since you're retiring | **$3,176,550** | +$76,550 |

Two honest riders: add ~$10,000 if they leave the Hardaway/warranty tail with you, and if you count Hensley's note interest ($56,700 after tax, ignoring time value — the library has no discounting rule), every threshold rises $70,875.

**How to say it to Lone Star:** "Fix the equipment number to the documented $650,000, treat my $400,000 as goodwill given I'm retiring, and we're at $3,176,550 — or your all-cash $3,100,000 is competing with a deal that nets me $61,240 more."

This walkthrough is now on the record: memo **§10.5** ("Plain English: why the bigger offer still nets less"), the break-even table in `comparison.json` → `break_even_vs_buyer_B`, and a line in `STATUS.md`. Arithmetic machine-checked.