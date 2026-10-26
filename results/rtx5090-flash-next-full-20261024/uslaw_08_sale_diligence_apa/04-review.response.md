I'll run a full audit: every legal authority cited in the deliverables against the library, every number recomputed, and cross-references checked. Starting by pulling the full library text and the deliverables:

Full library captured. Now reading all six deliverables to audit:

All three remaining deliverables partially shown — I need the full text of each to make exact edits. Reading them completely now:

Now the remaining four files in full:

All six deliverables fully re-read and cross-checked against the seven library files. The audit turned up five real problems. Applying fixes now, starting with the redline:

Now the other four files in full so I have exact strings:

All five markdown files are current in view. I need the full JSON for exact edit strings:

Continuing with the remaining edits. First, re-reading the exact current text around each pending edit so the replacements match:

Exact strings confirmed for redline, reply, and note. Applying the next round of fixes (one edit per file) while pulling the remaining three files:

All strings confirmed. Applying the next batch — one edit per file:

Next batch — cross-reference fixes, JSON fixes, note amounts, STATUS unverified bullet:

Next batch — §9.3 escrow amounts, JSON finding 7, note fix list, STATUS deliverable bullet:

Final content edits — §9.3 Why note and STATUS audit record:

One more STATUS bullet (the advocacy-only item), then validation:

All fixes applied. Running the validation sweep — JSON schema/parse check plus stale-value grep across all deliverables:

All remaining hits are legitimate (the $75,000 basket is a deal fact; the STATUS hits are the deliberate audit record of withdrawn figures). Final leak check on the outbound reply:

All checks pass. The pre-delivery audit is now fully applied. Here is the complete list of what I found and what I changed:

## Audit findings fixed

**1. Negotiation ladder leaked into the outbound letter (most serious)**
- `reply_to_buyer_counsel.md` previously told buyer's counsel our fallback ("$150,000 escrow-backed, **$200,000 at the outside**") — it handed them our ceiling. Removed. The reply now states a single firm number ($200,000, exclusive absent fraud) in all three places it appears (§3, §4, closing package). Ladder figures ($200k hold / $250k ceiling) now live only in the internal docs (redline, note_to_ray, STATUS, JSON).

**2. Internally broken §3509 math → rebuilt as labeled scenarios, and the indemnity re-anchored**
- The old single-point estimate ($18,543.60/yr) mixed the §3509(a) 1.5% rate with the §3509(b) 20% rate applied to the wrong base, and the "willful = 2% + full FICA" figure was wrong (willful means *no* §3509 relief at all). Replaced everywhere with a scenario set (rates flagged UNVERIFIED — library cites §3509 but not its percentages): non-willful $32,589/yr ≈ $130,356/4yr; employer-FICA-share-not-abated $79,407/yr ≈ $317,628/4yr; negligent $145,809/yr ≈ $583,236/4yr; willful = no relief, higher.
- Combined band re-anchored: old ≈$115,000–$210,000 → **≈$170,000–$450,000** (non-willful scenarios + overtime $40,500–$135,000).
- Special-indemnity ladder re-anchored from $150k/$200k to **hold $200,000 (6.5%) / ceiling $250,000 (8.1%)** — the old pair fell below every coherent scenario. Updated in the redline (7.4(b) clause + sizing notes + 9.3 clause + Why note), reply, note_to_ray, JSON findings 2 and 7, QUESTIONS, and STATUS.
- Dropped the claim that "the cap covers the credible range" — no deliverable now asserts the cap covers the full band; internal docs say plainly the cap is a negotiated limit, not coverage.
- §9.3 Why note now shows the escrow residual arithmetic: $310,000 − $200,000 = $110,000 general escrow; at the $250,000 fallback only $60,000 remains, so pair any move with added escrow funding.
- The outbound letter presents only the seller-favorable non-willful reading (≈$130,000 tax + overtime ≈ $170,000–$265,000) and labels the percentages "illustrative" instead of stating them as fact.

**3. Orphan cross-references**: two redline citations to "Section 7.5" — the buyer's draft has no §7.5. Fixed to §7.4(b) (line 55) and to "Sections 7.4(a) and (b), including the Worker Classification Special Indemnity" (7.4(c) replacement clause).

**4. Soft argument removed from reliance**: the "court asked to reform or police an unconscionable carve-out" point was pulled from the outbound letter and relabeled in the redline as **advocacy framing only, UNVERIFIED** (outside the library). It's replaced by the library-backed argument: `baskets_caps.md` *expressly* names worker classification as the operational rep whose full-price carve-out is off-market — plus a pre-buttal to buyer's likely "it's covered by the taxes exception" retort (the exposure flows from classification, which is the library's own named example).

## Validation results
- `diligence_findings.json` parses; 13 findings; every object has exactly the five schema keys; all `deal_impact` values in the enum (consent/indemnity/price/timing/none all valid).
- Stale-value sweep across all six deliverables (`150,000`, `115,000`, `74,174`, `18,543`, `59,058`, `2%/100%`, `7.5`, `unconscionab`, ladder language): zero stale hits. Remaining matches are the $75,000 basket (a real deal fact) and the STATUS.md audit record documenting the withdrawn figures.
- Outbound reply leak check: no "fallback/ceiling/at the outside/$250,000" anywhere in `reply_to_buyer_counsel.md`.

`STATUS.md` now carries a "Pre-delivery self-audit" paragraph recording all five fixes, plus a new UNVERIFIED bullet (cap reformation/unconscionability = advocacy only). Status remains **COMPLETE WITH OPEN ITEMS** — the ten flagged assumptions (price inference, busy-season length, willfulness posture, etc.) are unchanged in substance, only re-sized where the §3509 rebuild touched them.