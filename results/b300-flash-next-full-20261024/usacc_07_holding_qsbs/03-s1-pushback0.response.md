

Direct answer, then I'll add it to the opinion file. Let me first verify what the library actually supports on the "gain lands in the LLC" mechanism.





I accidentally dropped the assumptions heading and mis-ordered the sections — fixing:





Fixed. Here's the direct answer, Nadia (full version in `deliverable/opinion.md` §6):

## Who's right? The advisor — on neither half of his claim.

**"The gain lands in the LLC" fails twice over:**

1. **The LLC can't hold gain hostage anyway.** An LLC taxed as a partnership isn't a container — the library's own §1202 language describes gain as *flowing out to the partners* (§1202(g)); members are taxed in the year the entity realizes the gain, whether or not you withdraw the cash. So "land it in the holding and reinvest without tax" doesn't describe how any partnership works. (The general pass-through rule isn't restated in the closed library — labeled UNVERIFIED there — but you don't even need it, because of point 2.)

2. **The contribution itself kills the only tax shelter you actually have.** Your stock is textbook §1202 QSBS: bought at original issue for $12,000 in Feb 2020, held 7–8 years by the expected exit → **100% excluded, up to the $10M per-issuer cap**. But §1202(h) preserves tacked treatment only for gift, death, and partnership distributions *to* a partner — a *contribution to* a partnership isn't on the list; the holding never "acquired at original issue," and the stock **ceases to qualify in its hands** (`library/irc_1202_excerpt.md`). His step converts:

| Exit stake | Stock sold by you (this plan) | His plan: contributed, then sold |
|---|---:|---:|
| $9.0M | **$0 taxable** | $8,988,000 taxable |
| $9.4M | **$0 taxable** | $9,388,000 taxable |
| $10.0M | **$0 taxable** (cap headroom just $12k) | $9,988,000 taxable |

The tell: **if the exclusion works, there's nothing to defer.** He's selling you a solution to a problem his own step 2 creates.

## Can the holding own "it" after the sale? Yes — but "it" won't be stock anymore.

After the sale there is no Helio stock — there's **cash**, and cash can go into the holding freely (§721(a) non-event; under the recommended single-member holding it's just moving between your own pockets). The rule that matters is **order**: sell in *your own name* through closing, funds land in *your* account, and *then* contribute the cash to the holding whenever you like. A genuinely later, unconditional cash contribution is a separate transaction. A contribution sequenced before the sale is precisely the §1202(h) poison step — and *Gregory*/*Court Holding* is the library's reason you don't try to race it ("days before the wires clear" is a contribution-before-sale in disguise). Where the cash sits afterward cannot change who was taxed on the sale — which is you, at closing, and via the exclusion, tax-free.

One flagged aside: if the exit will exceed ~$10.012M and some gain spills past the cap, there are rollover-style regimes some practitioners discuss for QSBS — **nothing in the closed library covers them, so I label that UNVERIFIED** and it's a CPA question before the LOI. No such regime runs through "park it in the family LLC."

**Bottom line:** hold Helio personally through closing; contribute the proceeds to the holding after. `opinion.md` §6 and `STATUS.md` updated; all deliverables remain complete with the previously flagged open items (R1–R3 on QSB certification, prior-share-sale history, and deal structure are the urgent ones now that a sale is live).