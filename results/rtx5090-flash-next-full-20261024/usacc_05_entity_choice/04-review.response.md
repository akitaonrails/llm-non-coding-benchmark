I'll do a systematic pre-delivery audit: (1) re-verify every cited authority against the actual library text, (2) re-derive every number independently, (3) check cross-document consistency against the client documents and the contract spec. Reading everything fresh:

Now reading all 10 library files to verify every attribution:

Library verification complete for 9 files (plus `irc_1361_excerpt.md` and INDEX from earlier). Now the remaining deliverables:

Now let me pull the exact text of the passages I need to fix, plus the truncated tail sections (JSON assumptions, QUESTIONS, STATUS) to finish the audit:

All targets located. Applying the nine fixes (8 identified + the QBI wording appears in two files) in parallel:

All nine edits applied. Now the final validation pass — JSON integrity, component sums, citation sweep against INDEX.md, and cross-file consistency:

Confirmed clean — those are deliverable cross-references, not authority citations. Last step: note the audit in STATUS.md (open items unchanged):

Self-audit complete. Here is what I found and did.

## What I checked (and found correct)

- **Every citation** in all five documents + JSON was traced back to a file in `library/INDEX.md`, and each cited proposition was re-read against the actual library text (SPT formula, §1361(b)(1)(C) + §1362(d)(2) parenthetical, §351(d)/§83, §721 + Rev. Proc. 93-27 §4.01 + 2001-43, §83(b) "30 days, no extension," §199A SSTB/wages-vs-distributions, *Watson* $24k-vs-$200k, Form 2553 2-months-15-days + Rev. Proc. 2013-30, CA $800/$900/$2,500 bands, buy-sell checklist phrases). All match. The only non-library `.md` references are cross-links between my own deliverables, not authority claims.
- **All arithmetic** re-run: the four JSON options parse and each component sums exactly to `total` ($97,680 / $104,183.10 / $102,180 / $104,183.10); SPT day-count math (161.0–163.0 for 2026; 140-day threshold; 127/128 for 2027; ≈123 for 2028); CA fee-band sensitivity ($103,211.90); QBI/half-SE adjustments; *Watson* comparison ($39,780 vs $39,275.10). All client-document facts (66/96/118 days; $610k/$820k; $260k/$370k; $120k/$31k/$89k appraisal figures) re-verified.
- **Conclusion holds**: nothing in the audit changes the recommendation or the open-items list. STATUS.md remains `COMPLETE WITH OPEN ITEMS`, now with a short audit paragraph recording the pass.

## What I changed

| # | File | Fix |
|---|---|---|
| 1 | `term_sheet.md` §2 | **Real error**: vesting said "25% cliff + 1/36th/month through Nov 1, 2030" — that sums to 125% *and* spans 4 years. Corrected to 25% at the Nov 2, 2027 cliff + **1/32nd (3.125%) per month for months 13–36, fully vested Nov 1, 2029** (= a true 36-month schedule). My first correction attempt used 1/24/month, which the re-validation script caught as wrong (25% + 24×1/24 = 125%); the shipped text now verifies at 100.0%. |
| 2 | `recommendation.md` §4 | Year-2 SE tax "≈$28,305 each" omitted the $3,300 CA tax+fee deduction; restated **$28,052.55 each** (K-1 = (370,000 − 3,300)/2 = $183,350 × 15.3%). |
| 3 | `recommendation.md` §1 item 5 | "2027 at **128+** US days" → **127+** (the test is "equals or exceeds 183," and 127 + 40 + 16 = 183 exactly) — now consistent with §3.3 and the register. |
| 4 | `recommendation.md` §3.6(ii) | Cross-reference for the $50,000 spread fixed: §3.2 → **§3.1**. |
| 5 | `compliance_calendar.md` §A | Dec-2026 row "SPT 2026 = 161 < 183" → **161.0–163.0** (118 projected / ≈120 confirmed). |
| 6 | `compliance_calendar.md` §B | Garbled "2 months 15 days after Jan 1, **2027**-style year start" → "2 months 15 days after the **Jan 1, 2028** tax-year start" (= Mar 16, 2028). |
| 7 | `compliance_calendar.md` §A Dec 2 row | "Copy to the company" was marked ✔ library-backed; the copy requirement is **not** in the `irc_83b.md` excerpt text (Treas. Reg. §1.83-2 appears only in its citation line). Re-labeled ⚠ with a verify note; the 30-day deadline / "no extension" stay ✔. |
| 8 | `term_sheet.md` §7 + `compliance_calendar.md` §D | "QBI is driven by allocations, not distributions" is my interpretation of the library's wages-vs-distributions contrast, not library text — both spots now labeled as **inference**, with a pointer to the actual library language. |
| 9 | `STATUS.md` | Added a pre-delivery self-audit paragraph summarizing the verification pass and fixes; open items unchanged. |

**Final validation after the edits**: JSON re-parsed (schema conforms to CONTRACT.md, all four `total`s reconcile), citation sweep against INDEX clean, and cross-file consistency checks pass (127 threshold, 161.0–163.0, Nov 1 2029 vesting end, no stale "1/36th / 2030 / $28,305 / 128+ / 2027-style" strings anywhere).

The deliverable set is internally consistent and delivery-ready, with the two deliberately conservative gaps (option (a)'s understated total; excluded QBI/half-SE benefits) still explicitly flagged rather than forced to reconcile.