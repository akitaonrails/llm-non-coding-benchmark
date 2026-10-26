# April MOR — workpaper notes (why the MOR is a placeholder)

**The client file contains no April activity records.** `workspace/documents/` holds only March records
(petition_month_activity.md, vendor_invoices_march.csv) plus the court orders and plan term sheet —
verified by directory listing 10/25/2026. The April MOR cannot be completed without April receipts,
disbursements, and the 4/30 cash balance; inventing them would violate the engagement's working rules,
so `april_mor.json` carries null figures plus what is knowable from existing records. New asks are in
`deliverable/QUESTIONS.md` (§ "Session 2 — new").

## What April is known to contain (authorities in the file)

1. **Interim compensation order entered 4/14/2026** — 80% interim / 100% holdback (note in
   documents/vendor_invoices_march.csv). Effect on Part 5 and payable amounts: see
   `professional_fees.md`. Maximum payable to H&P on the invoiced period: 140,000.00 × 0.80 =
   **112,000.00**; nothing to Corbin absent an order. Whether an application was filed, awarded, or
   paid in April is not in the file.
2. **March MOR due April 21** (DIP order Dkt. 61 ¶ 4, documents/dip_financing_order_excerpt.pdf) —
   administrative event, no cash effect.
3. **Q1 UST fee**: March accrual 3,926.16 (0.8%-of-disbursements estimate from the client file) —
   expect a payment in April; amount/date pending. Payment reverses the accrual, so it moves Part 1
   disbursements and Part 2 payables, not net equity.
4. **Mesa Steel**: not payable in April. Payment of the Feb pre-petition invoice remains barred
   (Dkt. 61 ¶¶ 2–3; § 549(a); session1/response_to_cfo.md). The ~11,000.00 coil receivable is an
   estate asset to bill and collect — if collected it belongs in April **receipts**.

## Roll-forward (to complete when records arrive)

```
April beginning cash   1,771,630.00   (March ending; assumes $0 swept pre-petition balance — open item)
+ April receipts                  ?   (collections, incl. any Mesa 11,000.00 coil receivable)
− April disbursements             ?   (incl. any 112,000.00-cap H&P interim fee, Q1 UST fee,
                                       post-petition vendors, payroll)
= April ending cash               ?
```

Part 2 and Part 5 known-fact carry-forwards are recorded in the `_known` fields of april_mor.json.

## Part 7 method (unchanged from March)

Flag every payment on account of pre-petition debt with docket authority (expected: none in April),
and every out-of-ordinary-course payment without court approval (expected: none). Interim fee
payments made under the 4/14 order are court-approved administrative expenses, not pre-petition debt.
