I'll do a full final review: re-read every deliverable, re-verify the arithmetic, and check every authority against `library/INDEX.md`.

The POC table has a real reconciliation flaw (rows sum to $161,800 invoiced but the Total row says $210,000 — the fully-paid MS-7701 row is missing). Let me read the rest of the advice file to finish the audit:

All issues identified. Applying the fixes now — all edits are independent, so I'll batch them:

**Fix 1 — `advice_to_ceo.md`: remove the uncited §549 number (library rule: nothing outside the library gets cited, even flagged):**
**Fix 2 — garbled "wire-week" phrase (Feb 10 was ACH; the wire was Feb 27):**
**Fix 3 — mangled formatting in the exposure-range sentence:**
**Fix 4 — §503(b)(9) priority claim ("paid before general unsecured") is NOT in the library — must be flagged:**

Now the JSON fixes (garbled "44/45" label, stray `interval_id` field, the mis-stated insolvency presumption date, and the notice-date anomaly), plus the POC reconciliation fix and wording cleanups:

Now `STATUS.md` — it carries the same unverified-but-cited "§549" reference, and needs the notice-date anomaly logged as an unreconciled item:

Final validation — JSON parse, independent re-check of every headline number, and a last sweep for garbled text or uncited authority:

All arithmetic validates. The grep used a wrong path — retrying with the correct one:

One leftover: `claim_analysis.json` caveat (b) still names "§550" — a statute not in the library. Removing the number, keeping the unverified label:

Review complete. Every deliverable re-read, arithmetic re-verified independently in Python, every authority checked against `library/INDEX.md`. **All headline numbers survived validation** — nothing about the analysis changed.

## What I found and fixed

**`proof_of_claim_draft.md` — genuine reconciliation error (the most important catch):**
1. The invoice table's Total row said $210,000 invoiced / $85,000 paid, but the listed rows only summed to $161,800 / $36,800 — the fully-paid MS-7701 invoice was missing from the table. Added the MS-7701 row ($48,200 invoiced / $48,200 paid / $0 claimed); columns now reconcile exactly: $210,000 − $85,000 = $125,000.
2. Cleaned two vague execution notes: "file on the side of caution" → "file out of caution"; replaced the unsupported "trade-agreement election" bullet with "follow any additional election or designation instructions in the bar-date order."

**`claim_analysis.json` — one garbled label, one stray field, one mis-stated presumption, one document anomaly:**
3. Reclamation rationale said "44/45-day rule" — garbled; corrected to the 45-day rule (§546(c)(1)).
4. Removed a leftover junk field (`"interval_id": "outside ordinary-course band? NO"`) from the Dec 18 transfer record; replaced with a clean `ordinary_course_band` note.
5. The insolvency assumption read "insolvent on 2026-03-09" — wrong; fixed to the presumption spanning the full 90-day window (Dec 10, 2025 – Mar 10, 2026) under §547(f).
6. **New unreconciled item documented** (`notice_anomaly` key): the notice of commencement prints "Notice dated: April 2, 2026" — *after* both today (March 19) and the petition. Operative dates (petition, Dkt. 44 hearing, §341, June 11 bar date) are taken from the notice body; flagged for re-verification if a corrected notice issues.

**`advice_to_ceo.md` — unsupported authority removed, garbled text fixed:**
7. Removed the "§549" citation (accord corrected in `STATUS.md` and the §550 mention in `claim_analysis.json` caveat (b)) — those statutes are **not in the library**; the points remain, labeled "unverified, no authority cited," consistent with the contract's labeling rule.
8. "The Feb 10 wire-week payment" — garbled and factually wrong method (Feb 10 was ACH; the wire was Feb 27) → "the Feb 10 accelerated payment (29 days after invoice, $48,200, ACH)."
9. Fixed a mangled sentence in the exposure-range walkthrough ("**" + "**" artifact).
10. **Hedged the §503(b)(9) advantage:** the file claimed it's "paid in full before any general unsecured dividend" — that priority ordering is *not* in the library (no §507 authority). Reworded: the library's rule text says only "an administrative expense for the value of the goods"; the payment-priority expectation is flagged unverified.

**`STATUS.md`:**
11. Added the notice-date anomaly as an explicit open item; aligned the §549 wording.

## What re-validated cleanly
Python re-check: invoiced $210,000 / paid $85,000 / claim $125,000 (✓); §503(b)(9) $78,100 + GUC $46,900 = $125,000 (✓); 90-day transfers $180,000 = $95,000 protected + $85,000 exposed (✓); offsets $48,200 + $36,800 → net exposure **$0** (✓); windows — 90 days = Dec 10–Mar 10, 20-day window opens Feb 18, Feb 4 delivery = 34 days pre-petition, demand deadline Mar 21 / 20-day cap Mar 30 (✓); JSON parses (✓); final grep finds no garble, stray Cyrillic, or out-of-library citations (✓).

`STATUS.md` remains **COMPLETE WITH OPEN ITEMS**. Deliverables are ready for delivery.