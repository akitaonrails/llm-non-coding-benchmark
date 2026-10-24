Client responses received. Let me verify how each answer lands, then update the deliverables.

All client answers map cleanly onto open items; no federal figures change. Updating the four narrative deliverables.

Now rewriting QUESTIONS.md as an answered log plus explicitly flagged unknowns (no re-asks), and STATUS.md with the narrowed open items.

Final verification pass:

All client answers are processed and the deliverables are updated. Summary:

## How each answer landed (no figures changed — the answers confirm what was computed)

| Answer | Effect |
|---|---|
| Tenant is a stranger (nurse, via broker 2019), rent never raised | §280A(d)(2)(C) carve-out facts now client-confirmed → $19,550 rental allowance stands. Lease copy unavailable — logged as a document gap, not a fact gap. |
| Marcus: no contributions since 2021, never lent; Pike guarantees the bank line | Beginning basis **$11,500** and **$0 debt basis** confirmed → allowed S-corp loss $11,500, suspended $16,500. |
| Both remote jobs were employee-initiated and approved | Convenience-of-the-employer rule locked in for both spouses → NY wages $68,000 / $54,000 all year on IT-203. The "employer necessity" branch (previously the weakest call) is closed. |
| Elena signed Form 8332 for Leo's dad, 2025 is his year | Leo not claimed confirmed; CTC stays $2,200 (Sofia only). Her "{TY}" placeholder read as 2025 — noted in `judgment_calls.md`. |
| "No additional information" to the rest | File complete: withholding $8,730 is the only federal payment; no prior 7203s or lease exist to obtain. |

## Remaining unknowns, explicitly flagged (not re-asked)

1. **8962 family size / family-of-3 FPL — reference gap; the only item that can move a federal figure.** Family-of-4 ($31,200, the library's only FPL) → repayment capped at $1,900. If the correct count is 3, library-band arithmetic shows repayment could rise to **$3,642.38** (uncapped at ≥400% FPL, i.e., FPL ≤ $22,837.50), cutting the refund from **$2,322 to as low as $579.62**. Any family-of-3 FPL amount is outside the library, so it is not assumed or cited.
2. **NY tax amount not computable** — no NY rate schedule in the library; allocation inputs are final (181 resident days; NY wages 68,000/54,000; NY WH $6,752; Brooklyn rental NY-source all year).
3. **Document gaps**: 2019 lease and prior-year Forms 7203 — client has neither; facts rest on client statements.

## Files updated
- `workspace/deliverable/return.md` — client-response source row; confirmed debt-basis, tenant, 8332, and convenience-rule facts; 8962 section now carries the quantified sensitivity.
- `workspace/deliverable/judgment_calls.md` — §1, §3, §4, §5, §7 updated with confirmations; §5 now shows the band-boundary math (300% at FPL $30,450, 400% at $22,837.50, max repayment $3,642.38).
- `workspace/deliverable/QUESTIONS.md` — rewritten as an answered-question log plus remaining unknowns; nothing re-asked.
- `workspace/deliverable/STATUS.md` — **COMPLETE WITH OPEN ITEMS**, narrowed to the three gaps above.
- `workspace/deliverable/return.json` — unchanged and re-validated; headline stays: AGI $91,350, TI $59,850, tax $6,708, +$1,900 8962 repayment, −$2,200 CTC, refund **$2,322**.