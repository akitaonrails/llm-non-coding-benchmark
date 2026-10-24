# Status

**COMPLETE WITH OPEN ITEMS**

Delivered:
- `return.json` — federal Form 1040 (MFJ), Form 7203, Form 8582, Form 8962, dependents, NY allocation
- `return.md` — every figure with arithmetic and library authority
- `judgment_calls.md` — all judgment calls with rejected alternatives
- `QUESTIONS.md` — Q1 (S-corp debt-basis loan option) asked and answered by client: **no additional information** → option not elected; return stands as prepared

Results at a glance (final, as prepared):
- S-corp loss: $11,500 deducted (basis-limited), **$16,500 suspended** (7203)
- Rental loss: $19,550 allowed via the $25,000 special allowance (MAGI $110,900), **$1,468 carryforward** (8582)
- AGI $91,350; taxable income $59,850; tax $6,708 (Tax Table); CTC $2,200 (Sofia only); excess-APTC repayment $1,900 (8962)
- **Federal refund: $2,322**
- NY part-year: resident Jan 1–Jun 30 (181 days); Marcus $68,000 NY wages (convenience-of-employer rule); Elena $26,778 (181/365 of wages; employer-permitted remote work not NY source)

Open items / remaining unknowns (cannot be closed with the closed library or the client's file):
1. **NY tax due / refund on IT-203 not computed** — the library contains the IT-203 allocation rules but no NY rate tables. The allocation in `return.json` feeds IT-203; NY withholding of $6,752 ($3,842 + $2,910 per the W-2s) must be netted against NY tax due (excess refunded on IT-203 per IT-203-I) using the official rate schedule outside this library. Unknown, not estimable here.
2. **S-corp debt-basis option left undecided by the client** — no information was provided on a direct 2025 loan to Reyes & Pike. The return was prepared **without** it ($11,500 deducted / $16,500 suspended). If Marcus actually lends the company money in 2025 before filing, the return must be recomputed (each loaned dollar creates debt basis); the estimate in `QUESTIONS.md` Q1 (refund ≈ $8,480 at a full $16,500 loan) is **unverified** — the exact Tax Table rows for the resulting lower bracket are not in the library and must be checked against the full table.
3. **Carryforwards to track in future years:** $16,500 S-corp basis carryforward (7203) and $1,468 rental passive loss (8582 Part VII); both release as basis/participation is restored.
4. **Minor unverified facts (immaterial — documented in `judgment_calls.md`):** exact remote-work start dates for Marcus and Elena (client provided none; every plausible date leaves the NY allocation unchanged); SALT/state-tax itemization amounts (not in library; standard deduction $31,500 used — itemized could not approach it).
5. **Leo's Form 8332** for the father's odd-year claim is a procedural duty of Elena under the custody stipulation; it is not part of this return.
