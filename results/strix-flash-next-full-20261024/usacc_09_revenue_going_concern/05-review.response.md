I'll re-read every deliverable against the source documents and library, re-verify each number, and check every citation. First, recomputing the figures I asserted (especially the burn rates and the sensitivity table):

With this, I've grasped the full picture. Applying all the corrections — 4 instances in `revenue_memo.md`, 5 instances in `response_to_ceo.md`:

All nine edits applied. Final verification pass — structure, leftover bad strings, JSON validity, and a cross-file figure scan:

Clean. One last thing — logging the review pass in STATUS.md for the record:

Review complete. I re-verified every number by recomputation (cash-flow totals, sensitivities, lease math, covenant shortfall) and checked every citation against the four library documents. **Nine errors found and fixed — no conclusion or dollar figure in the corrected P&L changed.**

## What I changed

**`response_to_ceo.md`** (5 fixes):

1. **Burn-rate figures were wrong (real error).** Addendum 3 said "disbursements ≈ $1.4M/month against receipts ≈ $0.6M/month." Recomputed from `13_week_cash_flow.csv`: disbursements $2,545,000 / 13 wks = **$195,769/wk ≈ $851k/month**; receipts $1,424,000 / 13 wks = **$109,538/wk ≈ $476k/month**. Replaced with the correct weekly and monthly figures plus the totals.
2. **Misquoted the standard.** "Fails the identification and **no-substitution** tests" appeared twice (line 16 and Addendum 2) — "no-substitution" is lease language, not bill-and-hold. Replaced with the library's actual criteria: goods "identified separately as belonging to the customer" and entity "cannot use them or direct them to another customer" — now cited precisely as ASC 606-10-55-83(b), (d).
3. **Overstated the Trestle contrast (email body).** "Our facts are different on **every one** of those points" — not true: Saltline's request *was* in writing (email). Corrected to "fail two of those three outright — nothing was segregated or labeled, and the side letter hands Saltline a 180-day full refund."
4. **Misleading table row (Addendum 2).** "Requested — **but via email chain**" implied email isn't writing. Now: "Arguably met in form — documented in email; but the stated purpose 'invoice it 12/28 so it's in Q4' invites substantive-reason scrutiny." The "two of four absent" claim still holds.
5. **Criterion (a) overstated as met** (email body): "(yes — Saltline asked for it)" → "arguably… invites scrutiny over whether the reason is substantive."

**`revenue_memo.md`** (4 fixes):

6. **Unsupported authority removed.** "Capitalize as a **finance/operating** embedded lease" — finance-vs-operating classification criteria are not in the closed library. Now "capitalize as an embedded lease" with **[unverified — not in library]** noting no classification is asserted.
7. **Straight-line ROU amortization** was presented as required guidance — the library specifies only PV recognition. Now flagged as a stated assumption, and the "net income unchanged" claim is conditioned on the 0%/straight-line assumptions.
8. **Initial ROU = liability** now flagged as an assumption (initial-direct-cost mechanics not in the library; none in the file).
9. **Criterion (a)** in memo §2 softened from "is met" to "at best arguably met," citing the Q4-invoicing purpose.

## Verified, no change needed

- Arithmetic: 1,540,000 − 480,000 − 210,000 = **850,000**; NI 456,000 − 690,000 = **−234,000**; 612,000 + 1,424,000 − 2,545,000 = **−509,000**; first negative week **2026-02-20**; lease 36×18,000 = 648,000, 33×18,000 = **594,000**; sensitivities 6%/8%/10% → 546,327 / 531,617 / 517,454 (matches the ≈$531,600 in QUESTIONS.md); shortfall to Crestline **$650,000**.
- JSON: still valid; contains no classification claim; figures match the memo.
- Structure: body → Addendum 1 → 2 → 3 → citation note; four "Controller" signatures intact.
- Every quotation traced to a library or documents file; the two out-of-library items (legal exposure of false financials, lease classification) are explicitly labeled **[unverified — not in library]**.

`STATUS.md` now logs the review pass; status remains **COMPLETE WITH OPEN ITEMS** (five flagged unknowns unchanged).