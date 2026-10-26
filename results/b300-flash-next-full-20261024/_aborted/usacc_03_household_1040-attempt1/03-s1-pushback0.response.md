

The library's 7203 excerpt speaks to this exact question head-on. Pulling our basis rollforward to answer with the numbers:





Fair question — and it's the single most common misunderstanding about S-corp losses. Here's the answer, straight from the library rules we're required to work under:

## 1. The loss allowance is capped at *your own* basis — not the company's loss, not your friend's

The rule in force here: a shareholder's share of losses is **"allowed only to the extent of the shareholder's adjusted stock basis plus debt basis… Losses in excess of basis are suspended and carried forward indefinitely until basis is restored"** **[7203]** (IRC §1366(d)).

Marcus's stock basis on 1/1/2025, using the library's ordering (income and contributions first, then distributions, then losses), from his own note — which he confirmed is complete:

| Item | Amount |
|---|---:|
| Capital contribution (2021) | 10,000 |
| Share of company income 2022–2024 (6,400 + 9,800 + 4,600) | +20,800 |
| Distributions taken 2023–2024 (12,000 + 5,200) | −17,200 |
| 2021 loss already used | −2,100 |
| **Basis entering 2025** | **11,500** |

Loss share $28,000 − basis $11,500 = **$16,500 suspended**. That's arithmetic, not a judgment call.

## 2. Pike's guarantee doesn't help — twice over

The library rule is categorical: **"A guarantee of corporate debt does not create debt basis; only a direct loan from the shareholder to the corporation does"** **[7203]**. So even if the guarantee were *Marcus's*, it would create zero basis. And it isn't his — it's Pike's, and basis is shareholder-specific anyway. Marcus has never loaned the company money (he confirmed this), so debt basis = $0.

## 3. Why the buddy's CPA could take the full loss

Because basis is a **per-shareholder** fact. The friend's CPA didn "beat" the rule — the friend presumably *had* the basis: bigger contributions, years of company income building basis before the loss year, or **direct loans the friend made to his S-corp**. None of those exist for Marcus. (Alternatively the friend's return is simply wrong — but we can't see it, and it changes nothing on Marcus's K-1.)

## 4. The $16,500 is suspended, not lost

It carries forward **indefinitely** **[7203]** and gets released whenever basis comes back. Mechanically: if the 2026 K-1 shows Marcus's share of income, that income increases basis *first*, and the carryforward then absorbs it — e.g., $10,000 of 2026 income → Marcus reports **$0** from the company and burns $10,000 of the carryforward. Same if he contributes capital.

**Forward planning lever (consistent with the library):** if the company will keep generating losses, a *direct written loan* from Marcus to the corporation — not another guarantee — creates debt basis that can absorb future losses **[7203]**. Worth raising with him before the company books more losses; it's too late to change the 2025 answer.

---

Logging the objection and response in the judgment calls file so the file trail shows it was tested:





No numbers move: refund stays **$2,322.00**, with 11,500 allowed / 16,500 suspended on Form 7203. The objection and its rejection (with the guarantee point) are now recorded under judgment call #1 in `judgment_calls.md`, so the file shows we pressure-tested it rather than just repeating our answer.

If Marcus wants to act on the planning point, the concrete next step is: any future funding of Reyes & Pike should be structured as a **direct written loan or capital contribution from Marcus himself** — a guarantee by either partner does nothing for basis, no matter who the bank required it from.