# Status

**COMPLETE WITH OPEN ITEMS**

Delivered:
- `return.json` — federal Form 1040 (MFJ), Form 7203, Form 8582, Form 8962, dependents, NY allocation
- `return.md` — every figure with arithmetic and library authority
- `judgment_calls.md` — all judgment calls with rejected alternatives

No `QUESTIONS.md` was needed — every fact required was in the client file; no client information was missing.

Results at a glance:
- S-corp loss: $11,500 deducted (basis-limited), **$16,500 suspended** (7203) — Marcus's "straight off" expectation rejected
- Rental loss: $19,550 allowed via the $25,000 special allowance (MAGI $110,900), **$1,468 carryforward** (8582)
- AGI $91,350; taxable income $59,850; tax $6,708 (Tax Table); CTC $2,200 (Sofia only); excess-APTC repayment $1,900 (8962)
- **Federal refund: $2,322**
- NY part-year: resident Jan 1–Jun 30 (181 days); Marcus $68,000 NY wages (convenience-of-employer rule); Elena $26,778 (181/365 of wages; employer-permitted remote work not NY source)

Open items (cannot be closed with the closed library):
1. **NY tax due / refund on IT-203 not computed** — the library contains the IT-203 allocation rules but no NY rate tables. The allocation in `return.json` feeds IT-203; NY withholding of $6,752 ($3,842 + $2,910 per the W-2s) must be netted against NY tax due (excess refunded on IT-203 per IT-203-I) using the official rate schedule outside this library.
2. **Suspended loss carryforwards to track in future years:** $16,500 S-corp basis carryforward (7203) and $1,468 rental passive loss (8582 Part VII). Released as basis/participation is restored.
