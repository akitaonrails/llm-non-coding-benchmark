

Now let me read the remaining library files.






I have the full picture now. Let me verify all calculations with Python before writing the deliverables.





The execute tool choked on the code; I'll run it as a script file instead.





All calculations check out. Now I'll write the deliverables.





Let me validate the JSON and do a final consistency check.





Engagement complete. All deliverables are written under `workspace/deliverable/` (reachable via the root `deliverable/` alias), calculated with Python and cross-checked against the library.

## Headline results

**The S-corp loss does NOT "come straight off."** Marcus's stock basis at 1/1/2025 was **$11,500** (10,000 − 2,100 + 6,400 + 9,800 − 12,000 + 4,600 − 5,200), with zero debt basis (Pike's guarantee doesn't count — Form 7203 instructions). So only **$11,500** of the $28,000 K-1 loss is deductible; **$16,500** is suspended.

| Item | Result |
|---|---|
| **Form 7203** | Basis begin $11,500 → loss allowed $11,500, suspended $16,500, ending basis $0 |
| **Form 8582** | Rental loss $21,018; MAGI $110,900 (includes the S-corp loss, excludes the passive rental loss); allowance $25,000 − 50%×(110,900−100,000) = **$19,550** → loss allowed $19,550, carryforward $1,468 |
| **Form 1040** | AGI $91,350; standard deduction $31,500 (beats $13,232 itemized); taxable income **$59,850** → tax **$6,708** (2025 Tax Table, MFJ, 59,850–59,900 bracket); CTC $2,200 (Sofia only) |
| **Form 8962** | Household income $91,350 = 292.79% FPL → applicable figure 5.7115% → annual PTC **$4,923** vs APTC $9,900 → excess $4,977 capped at **$1,900** (MFJ 200–300% tier) |
| **Bottom line** | Total tax $8,608; withholding $8,730 + CTC $2,200 → **refund $2,322** |
| **NY** | Part-year resident, **181 days** (1/1–6/30). Convenience-of-the-employer rule makes **100% of both W-2s NY-source** (both are NY employers, both went remote for personal convenience) — no day-count allocation; matches the W-2 box 15/16 reporting |

**Key judgment calls** (each documented with the rejected alternative in `judgment_calls.md`): basis limit on the S-corp loss; below-market rent treated as a bona fide unrelated-tenant lease under the 8582 carve-out (rejected §280A(d) personal-use treatment that would have killed the loss); Leo not claimed — the custody decree gives him to the father in odd years; standard over itemized; MAGI ordering for the phase-out.

**Status: COMPLETE WITH OPEN ITEMS** — the only open item is the NY source of the $400 Chase interest for the nonresident period (payer location/date not on the 1099-INT); it doesn't affect the federal return or the requested NY fields. Carryforwards ($16,500 S-corp, $1,468 rental) are flagged for 2026.