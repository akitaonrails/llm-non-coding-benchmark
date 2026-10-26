

Pre-delivery audit: I'll re-read every authority file and source document, then every deliverable line by line against them.






All deliverables and authorities are now re-verified line by line. Confirmed supported: §547(g) burden, §547(f) presumption, full (c)(4) text, the OCU "shortened terms/pressure/wire on demand" language, Pioneer excusable neglect, Kmart "typically agree," and every date/amount. The audit findings to fix:

1. **Apr 2 hearing "10:00" is fabricated detail** — the notice states no time for the Dkt. 44 hearing (10:00 a.m. belongs to the Apr 21 §341 meeting). Error in `claim_analysis.json` and `STATUS.md`.
2. **Willfulness conclusion unsupported** — JSON asserts later acts *are* "willful"; the library never defines willfulness.
3. **Goods-identifiability condition** for reclamation is doctrine outside the library — must be flagged unverified.
4. **§507(a)(7) citation in the POC** — §507 is not in the library; must be labeled form boilerplate to verify.
5. **Overstatements**: POC "must be asserted separately" (library: *should*); advice "vendor must agree" (library: *must typically agree*); "only where the vendor agrees… not a deal a court can approve" (stronger than the practice note).
6. **Administrative-expense priority/plan treatment** stated in the advice memo as if sourced — it's outside the library; flag it.
7. **§362(k) damages wording** — library says actual damages *including* costs and fees; deliverables say "plus."

Applying fixes:









JSON and STATUS fixed. Now the advice memo, QUESTIONS, and POC:













Three edits missed on exact match — let me get the precise current text:





All edits have been applied. Final verification — JSON validity + schema + arithmetic assertions, stale figure scan, and confirming that the remaining references to "10:00"/§507 are only the legitimate ones:





Audit complete. Every citation was re-checked against the six library files and all five client documents, every number re-derived from the CSVs, and every fix re-validated (JSON parses, schema and arithmetic asserts pass, stale-figure scan clean). Here is what I changed:

## Audit findings and fixes

**1. Fabricated hearing time — `claim_analysis.json`, `STATUS.md`**
The notice states a hearing date of April 2 for the Dkt. 44 critical-vendor motion but **no time**. Both files had "10:00" — that time belongs only to the April 21 §341 meeting. Both now read "April 2 (notice states no time — confirm from the docket)." The three remaining "10:00" mentions are all the Apr 21 §341 meeting, which the notice does state.

**2. Unsupported willfulness conclusion — `claim_analysis.json`**
The JSON asserted the post-notice collection acts "are 'willful.'" The library never defines willfulness. Softened to: documented knowledge is "a fact bearing on whether later acts are 'willful' — UNVERIFIED as a legal conclusion." Also conformed the §362(k) damages wording to the library's exact phrasing ("actual damages, **including** costs and attorneys' fees") in the JSON and the advice memo (which had said "plus").

**3. Reclamation goods-identifiability flagged — `claim_analysis.json`, `QUESTIONS.md` (item 8(d)), `STATUS.md`, advice footer**
Our deliverables treated "uncut and identifiable" as a reclamation requirement; that traceability doctrine is **not in the library** (which only says goods may be reclaimed, subject to prior liens). Now explicitly flagged unverified — the practical advice (check the steel is still at Redwood by Mar 27) is unchanged.

**4. §507(a)(7) citation removed as authority — `proof_of_claim_draft.md`**
§507 is not in the library, so the Part 5 checkbox can't cite it. Relabeled as Official Form 410 boilerplate with an instruction to verify the current form's text at filing; no priority claimed beyond the §503(b)(9) portion.

**5. Two overstatements of authority — `proof_of_claim_draft.md`, `advice_to_ceo.md`, `QUESTIONS.md` (item 2)**
- POC said the §503(b)(9) portion "**must** be asserted separately" — the library says "**should**." Fixed.
- Advice memo and QUESTIONS said under *Kmart* the vendor "**must agree** to customary trade terms" and that "pay first" "cannot be approved by the court." The practice note says the vendor "**must typically agree** to customary trade terms for the case," so the phrasing now tracks it, and "pay first" is described as inconsistent with that posture rather than categorically unapprovable.

**6. Administrative-expense priority/plan treatment flagged — `advice_to_ceo.md` (§2), `QUESTIONS.md` (item 8(e)), `STATUS.md`, advice footer**
"Administrative claims outrank unsecured debts and are paid in full in plans" is standard practice but **not restated anywhere in the library**. Now flagged unverified in place and added to both unverified-lists.

## What the audit confirmed as accurate (unchanged)

- Claim **$125,000** = $78,100 §503(b)(9) (MS-7788 + MS-7815) + $46,900 GUC (MS-7740 balance $25,600 + freight $6,900 + cutting services $14,400); gross $210,000 − $85,000 paid — all re-derived from the invoices CSV.
- Preference math: 90-day window opens 2025-12-10; four transfers totaling $180,000; OCU protected $95,000 / exposed $85,000; new value $99,400 ≥ $85,000 with exact backward application (48,200 delivered between the Feb payments; 51,200 after the wire) → net exposure $0, worst case $85,000; §502(d) trap retained.
- Reclamation: $103,700 of goods in the 45-day window, written §546(c) demand deadline **2026-03-30**, DIP-lien caveat.
- Bar date 2026-06-11 5:00 p.m. MT; the "Notice dated: April 2, 2026" irregularity is flagged in place.
- Stay-violation facts (03-12 letter, 03-15 call, 03-18 email) and the "you owe us" attribution to our own AR clerk — verified verbatim against the dunning log.

Five unverified legal points now carry explicit flags (refusal-to-ship stay question; §503(b)(9)-payment effect on the new-value shield; DIP-lien priority specifics; goods identifiability; admin-expense priority/plan treatment) — listed in `QUESTIONS.md` item 8 and `STATUS.md`.

**Status: COMPLETE WITH OPEN ITEMS** — all five deliverables in `workspace/deliverable/` are audit-corrected, internally reconciled, and ready for delivery.