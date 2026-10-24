

Good question — let me walk through it, because the answer is mechanical and it's exactly the part where your buddy's situation almost certainly differs from yours.

## Why $16,500 is suspended

An S-corp loss is deductible only to the extent of your **adjusted stock basis + debt basis** (IRC §1366(d), per `library/form7203_instructions_excerpt.md`). It's not a judgment call — it's a cap.

Your basis trail (from your own note):

| Year | Income/(loss) | Distributions | Ending basis |
|---|---:|---:|---:|
| 2021 | (2,100) | 0 | 7,900 |
| 2022 | 6,400 | 0 | 14,300 |
| 2023 | 9,800 | (12,000) | 12,100 |
| 2024 | 4,600 | (5,200) | **11,500** |

So at 1/1/2025 you had **$11,500** of stock basis and **$0** debt basis. The 2025 loss is $28,000, so only $11,500 fits and **$16,500 is suspended**.

The big driver here is the **distributions** — the $12,000 (2023) and $5,200 (2024) you took out reduced your basis. Income *adds* to basis, distributions *subtract* from it, and by 2025 you'd drawn down to $11,500.

## "My buddy's CPA let him take his whole loss"

That's a different fact pattern, not a different law. The cap is identical for everyone. Your buddy's CPA could deduct the full loss only if your buddy's **basis was at least as big as the loss** — e.g. a bigger initial contribution, more accumulated income, far fewer distributions, or real debt basis. I don't have his numbers, so I can't say which, but there's no rule that lets one shareholder skip the basis test. If you want, get your buddy's basis worksheet and we'll compare side by side — it usually makes it obvious.

## Can we count Pike's guarantee?

**No — and this is spelled out in the library, not my opinion:**

> "A guarantee of corporate debt does **not** create debt basis; only a direct loan from the shareholder to the corporation does." — `library/form7203_instructions_excerpt.md` (IRS Form 7203 Instructions 2025)

Two problems with the guarantee:
1. It's **Pike's** guarantee, not yours — a third party standing behind the debt doesn't give *you* any basis.
2. Even **your** personal guarantee of the bank line wouldn't count. The only thing that creates debt basis is **you actually lending the company money** (a direct shareholder loan).

Per your note you "never lent the company money (we have a bank line, Pike personally guarantees it)" — so debt basis = $0, confirmed.

## The good news

The $16,500 **isn't gone** — it's suspended and **carried forward indefinitely** (same Form 7203 authority). It becomes deductible in a future year when your basis is restored, i.e. when Reyes & Pike generates enough income (or you contribute more capital) to rebuild basis. I've flagged it in `STATUS.md` and `judgment_calls.md` (item 1) to track for 2026 and beyond.

If you genuinely want to pull more of the loss into 2025, the only legitimate lever is a **direct loan from you to the corporation** — but that has to be an actual 2025 loan to count for 2025, and it changes your cash position, so it's a business decision, not a tax maneuver I'd recommend retrofitting.

**Bottom line:** no change to the return — the $11,500 / $16,500 split is correct under the library authority. Want me to add a short "basis & suspended loss" explainer as an appendix to `return.md` you can hand to Marcus?