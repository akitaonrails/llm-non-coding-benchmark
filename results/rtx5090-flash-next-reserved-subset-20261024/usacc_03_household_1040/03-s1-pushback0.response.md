Good question — this one is worth walking through carefully. The short answer: it's not a judgment call on our side, it's arithmetic, and the library is explicit about the guarantee.

## Why $16,500 is suspended

Your share of losses can only be deducted up to your **stock basis plus debt basis** in the S-corp (`library/form7203_instructions_excerpt.md`, IRC §1366(d)). Your basis, from your own rollforward:

| Year | Activity | Basis |
|---|---|---:|
| 2021 | You contributed $10,000; 2021 loss (2,100) | 7,900 |
| 2022 | +6,400 income | 14,300 |
| 2023 | +9,800 income − **12,000 distributions** | 12,100 |
| 2024 | +4,600 income − **5,200 distributions** | **11,500** |

Loss $28,000 − basis $11,500 = **$16,500 with nothing left to absorb it**. The distributions you took ($17,200 over 2023–24) spent the basis that the loss would need. The excess isn't lost — the library says suspended losses **carry forward indefinitely until basis is restored**.

## Your buddy's CPA didn't apply a different rule

Same rule applies to him. The only way he "takes the whole loss" is if **his basis was ≥ his loss** — he contributed more, took fewer (or no) distributions, or had prior income build up basis. Basis is per-shareholder; his number says nothing about yours.

## Pike's guarantee: no, and the library says so in one sentence

> "A guarantee of corporate debt does **not** create debt basis; only a direct loan from the shareholder to the corporation does." (`form7203_instructions_excerpt.md`)

Pike personally guaranteeing the bank line is risk for *Pike* — it gives **Marcus** zero debt basis. It doesn't help your deduction at all.

## What *would* legally change the answer

The library identifies exactly two things that add basis: **capital contributions** and **direct loans from you to the corporation**. So if Marcus put real money into Reyes & Pike in 2025 — e.g. a **$16,500 direct loan documented with a note**, or a contribution — that restored basis would let the full $28,000 through ($11,500 stock + $16,500 debt). But that's a business decision, not a paperwork trick: it puts $16,500 of his own money at risk in the company. Also, the fine points (how the loan must be documented, how much timing matters within the year, how restored basis interacts with the prior-year suspension) go beyond what's in our reference set — we'd verify those against the full instructions before implementing.

**Bottom line:** the $16,500 suspension stands for 2025 as filed. It's parked, not thrown away — it comes back when basis is restored.

Let me log the pushback in the judgment file so the trail is complete.

Logged in `judgment_calls.md` §1. No figures changed — `return.json` still shows allowed $11,500 / suspended $16,500, refund $2,322. If Marcus decides he actually wants to fund the company $16,500 directly to unlock the loss, tell us and we'll work through how to document it properly.