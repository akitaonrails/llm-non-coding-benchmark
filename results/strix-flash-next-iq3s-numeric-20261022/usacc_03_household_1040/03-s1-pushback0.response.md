Marcus is pushing back on the biggest judgment call. Let me re-check the library's exact 7203 language and the K-1 before answering, so the explanation is precise and cites verbatim.

K-1 box 16 confirms 2025 distributions = $0.00, so nothing reduced basis before the loss — the computation is airtight on the file as it stands. Here's the answer for Marcus, then I'll log it.

---

## Marcus — why $16,500 is suspended, and why Pike's guarantee doesn't help

**The rule (Form 7203 instructions, our library):** an S-corp shareholder's loss "is allowed only to the extent of the shareholder's adjusted stock basis plus debt basis. Losses in excess of basis are suspended and carried forward indefinitely until basis is restored."

**Your basis, from your own note (which you confirmed on 10/22):**

| Year | Beginning | + Income | − Dist. | Ending |
|---|---:|---:|---:|---:|
| 2021 | 10,000 | (2,100) | 0 | 7,900 |
| 2022 | 7,900 | 6,400 | 0 | 14,300 |
| 2023 | 14,300 | 9,800 | (12,000) | 12,100 |
| 2024 | 12,100 | 4,600 | (5,200) | **11,500** |

The 2025 K-1 shows **distributions of $0.00** (box 16), so nothing dropped basis before the loss hit. Allowed loss = lesser of 28,000 and 11,500 = **11,500**; suspended = **16,500**. **[7203]**

**Why the guarantee can't count — two independent problems:**
1. The library is explicit: *"A guarantee of corporate debt does not create debt basis; only a direct loan from the shareholder to the corporation does."* A guarantee means the bank *might* come after the guarantor later; until then Marcus has put no money at risk in the company, so there is no basis to deduct against.
2. It's **Pike's** guarantee, not Marcus's. Even in a world where guarantees counted, they'd belong to Pike, not to Marcus's basis.

**Why the buddy's CPA let his whole loss through — probably different facts, and basis is per-shareholder, per-year.** The friend may have: higher stock basis (retained profits never distributed, or contributions), an actual **direct loan** he made to his company (that *does* create debt basis), a Schedule C / partnership situation with no §1366(d) limit, or a suspended-loss carryforward from earlier years. None of those exist in your confirmed file. It's also possible the friend's return simply takes a position that wouldn't hold up — I can't audit his return from here, and I can't copy it onto yours.

**The $16,500 is not lost.** It carries forward indefinitely and becomes usable when basis is restored — next year's company income, or a contribution. **[7203]**

**The one lever that could legitimately change this:** if your real 1/1/2025 basis is higher than the note says. That's why the missing **2024 as-filed return / Form 7203** matters (open item B) — that's the only document that could raise the allowed loss. Also: if you ever put money into the company *as a loan* with any paperwork at all, tell me — you said no, but that's the fact that would change the answer.

Logging this exchange in the deliverables:

Now elevating open item B into a concrete ask in QUESTIONS.md and STATUS.md:

All updated. Summary of where things stand:

## The answer to Marcus (plain version)

- **The limit is your basis, not your opinion of the loss.** Form 7203 instructions (our library): losses are "allowed only to the extent of the shareholder's adjusted stock basis plus debt basis," and the excess is "suspended and carried forward indefinitely until basis is restored." Your own note — which you confirmed on 10/22 — puts your 1/1/2025 basis at **$11,500**, and the 2025 K-1 shows **$0.00 distributions** (box 16), so nothing else touched basis. Allowed: 11,500. Suspended: 16,500.
- **Pike's guarantee can't count, twice over.** The library is explicit: a guarantee of corporate debt does **not** create debt basis — only a direct loan from the shareholder to the corporation does. And even if guarantees counted, it's Pike's, not Marcus's.
- **The buddy's return isn't comparable.** Basis is per-shareholder, per-year. His CPA likely had different facts — higher basis from retained profits, an actual direct loan to his company, or a different entity type. What works on someone else's return doesn't transfer, and I won't copy a position that fails on our documents.
- **The $16,500 isn't lost** — it carries forward and unlocks when basis comes back (next year's company income or a contribution).
- **The one real lever is paperwork:** if the 2024 as-filed Form 7203 shows basis higher than the note says, more of the 28,000 is allowed. I've turned that open item into a direct ask.

## Record updates (no figures changed — refund stays $2,322)

- `judgment_calls.md` #1 — logged the turn-3 challenge, the verbatim rule, the re-verified K-1 box 16 = $0.00, and that the decision stands.
- `return.md` §1 — added the box-16 confirmation to the arithmetic.
- `QUESTIONS.md` B / `STATUS.md` B — elevated the 2024 Form 7203 from a verification gap to the **only legitimate action item** that could change the suspension; STATUS retitled to turn 3.

If Marcus produces the 2024 return, I'll re-run the roll-forward and cascade everything (7203 → 8582 MAGI/allowance → AGI → 8962). Until then, 11,500 allowed / 16,500 suspended stands.