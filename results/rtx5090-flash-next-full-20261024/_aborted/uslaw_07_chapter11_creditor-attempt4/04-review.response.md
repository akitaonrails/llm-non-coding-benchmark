I'll do a full verification pass: re-read the library (authority check), re-run every calculation against the source data, then audit each deliverable.

Library and source documents are now fully re-read. Now let me re-read all five deliverables and rerun the arithmetic.

All window dates and totals confirmed. One flag: new value after 02/27 is $51,200 counting services, not just the goods-only $36,800. Now reading the deliverables in full.

Now the remaining deliverables and the contract spec.

JSON updated. Now the CEO advice memo.

One nuance to tighten: the library's §362(k) text covers "an individual injured," while Redwood is a corporation — I should mirror the library's §105 bridge rather than overstate (k).

Continuing the audit fixes. Let me re-read the current state of `advice_to_ceo.md` §2 and §4 to apply the remaining corrections precisely.

Now applying the remaining §2 and §4 fixes to the advice memo.

Advice memo done. Now STATUS.md — let me read the current full text.

STATUS.md done. Now the proof-of-claim draft — reading the middle section to place the Form 410 caveat.

All four main files updated. Now verifying QUESTIONS.md for consistency with the corrected figures, and validating the JSON.

Audit complete — every figure re-verified against the source CSVs, every citation checked against `library/`, and all fixes applied. Here is what changed and why.

## Errors found and fixed

**1. Legal error: new value was understated as goods-only (material mistake)**
§547(c)(4) in the library does not limit "new value" to goods, but the earlier drafts credited only steel. Corrected in all three analytic files:
- After the **Feb 10** transfer: **$99,400** unpaid new value (goods 78,100 + freight MS-7802 6,900 + services MS-7819 14,400)
- After the **Feb 27** transfer: **$51,200** (steel 36,800 + services 14,400) — and since nothing was paid after 2/27, the "otherwise unavoidable transfer" cutback never applies
- Kept the goods-only fallback (78,100 ≥ 48,200; exactly 36,800 = 36,800) so the defense works either way; net stays ~$0, worst case ~$36,800 under the last-transfer sequencing rule, which is **not in the library** and is labeled unverified
- `claim_analysis.json`: `new_value_defense` corrected **85,000 → 99,400**; JSON re-validated (schema keys unchanged)

**2. Missing statutory point: §547(f) insolvency presumption**
The memo told the CEO the estate "has to prove insolvency" energy it doesn't need. Added the 90-day presumption (library bc_547) to `advice_to_ceo.md` §2, `claim_analysis.json`, and STATUS assumptions — and contrasted it with §546(c), where the library states **no** presumption for reclamation, so insolvency-at-receipt there stays an open fact (U5).

**3. Reclamation "why" was sloppy**
It read as if $103,700 included paid amounts. Reworded: 103,700 is the **unpaid value** of the three in-window goods invoices (the 36,800 already paid on MS-7740 is not reclaimable); added the DIP-blanket-lien hollowness caveat and the traceability caveat (traceability not addressed in the library → flagged unverified).

**4. §502(d) mis-stated as discretionary**
"Can disallow" → the library's mandatory "**shall disallow**" (and "must disallow" in the memo). This matters — it's the single biggest threat to the $125,000 claim.

**5. Payment-history phrasing inflated**
"Matching 12-month history: 8 payments" double-counted the in-window payments. Now everywhere: the **six pre-window payments (Apr–Nov 2025) were all 43–47 days, all ACH**, and Dec 18/Jan 22 continue that pattern.

**6. Overstated facts in the critical-vendor section**
"Monthly shipments across 12 months" → **eight invoice-and-payment cycles Apr 2025–Feb 2026, with gaps in June and October**; and the essentiality evidence (single-source grades, lead times) was flagged as **not in the file** — it must be built from Mesa's records before Apr 2, not asserted.

**7. Unsupported authority: *Kmart***
The memo paraphrased Kmart as "blocks payments without supply justification." Restated strictly from the practice-note text: designation is for essential, non-replaceable vendors on customary trade terms, at the debtor's discretion with court approval — nothing beyond what the note says.

**8. Stay-sanctions willfulness reasoning**
Rewritten to the bridge the library actually supports (§362(k) "individual" + §105) rather than implying §362(k) plainly covers corporations — conclusion unchanged, reasoning now honest about being an interpolation.

## New caveats added (things our drafts implied but the library doesn't prove)
- Proof-of-claim draft: **Official Form 410 is not in the library** — item numbers/checkboxes must be conformed to the current official form at filing.
- §503(b)(9)'s practical effect of paying $78,100 **ahead of general unsecured claims** is standard but not restated in the library → flagged unverified (we assert the priority anyway; costs nothing).
- Freight MS-7802 now explicitly counted in new value but not as §503(b)(9) goods.

## Checked and clean (no changes)
- All arithmetic: 125,000 = 78,100 + 46,900; 210,000 − 85,000 = 125,000; reclamation 103,700; transfers 180,000; split 95,000/85,000; window opens 12-10, 01-24; demand deadline 03-30 — every number re-computed in Python against the CSVs.
- `QUESTIONS.md` (U1–U10) verified consistent with the corrected files; answered questions still not repeated.
- Cross-reference grep sweep: no stale phrasings remain in any deliverable.

## Final state
`deliverable/STATUS.md` = **COMPLETE WITH OPEN ITEMS** — proof of claim ready to file at **$125,000** (bar date 2026-06-11, filing early), reclamation demand due **2026-03-30**, critical-vendor course correction due before the **2026-04-02** hearing.