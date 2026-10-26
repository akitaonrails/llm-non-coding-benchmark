Good instruction — I'll do a full pre-delivery audit: re-read the contract schema, the library (to verify every cited authority actually exists *in* the library), all five deliverables, and re-check every number.

INDEX confirms the case names are library authorities — but the key audit is whether each library file actually supports the propositions I attributed to it. Reading all six:

Library verified — six files, each short. Two propositions I've been asserting are **not in the library** and one sentence is affirmatively contradicted by it. Now reading all deliverables in full to find and fix those:

JSON reads clean and its propositions match the library. Now I need to (a) re-verify the underlying facts against the source documents, and (b) read the remaining deliverables in full — I already spotted two problems in `advice_to_hr.md` §7 from the library read. Getting the source docs and remaining deliverables:

`advice_to_hr.md` §7 confirmed as containing the two problem sentences (the "dissuade a reasonable worker" attribution and the "months later" proximity claim — both unsupported or contradicted by the library). Before fixing, let me re-verify the factual claims against the source documents and read the remaining deliverables:

All client facts verified against the source documents — attainment, ages, dates, email quote, and the form's term numbering (both OWBPA defects indeed sit in term 7). Now the remaining deliverables:

Continuing the audit — I need the untruncated remainder of each file before making the fixes:


Dropped the `/work` prefix — retrying with full paths:

All JSON content verified. Now I need the exact middle sections of the remaining files (unseen in this session) to make precise edits:

All files read. Remaining edits are in `advice_to_hr.md` — I need the exact text of lines 13–29 (§1.4–§3) before editing:

Complete picture obtained. The audit confirms these defects to fix:

1. **§7 PIP bullet (line 47)** — attributes a "dissuade a reasonable worker" adverse-action standard to `title_vii_704a.md`, which doesn't contain it
2. **§7 last question (line 54)** — "keeps the temporal-proximity story alive months later" contradicts the library (proximity = *days to a few weeks*)
3. **§7 sequence (line 56)** — asserts a negative ("the law does not require waiting") as positive law instead of library absence
4. **§6 (line 41)** — "96% → 92% → 88%, 'Meets' every year" misstates the record (88% is unrated 2026 YTD; "Meets" ratings are 2023–2025, and 101% is omitted)
5. **§2.2 (line 22)** — "24 days" is stale as of today (43)
6. **FMLA remedy wording** (JSON, advice §5.3, QUESTIONS) — "2 × lost base pay [liquidated damages]" conflates the loss and the liquidated add-on; library says lost wages + equal liquidated (double) amount
7. **JSON timing entry** — 24 days should be marked as outer edge of the "few weeks" window, not lumped with the 4-day gap

Applying all fixes:

All 9 edits applied. Final validation — checking the remaining §7 summary text in STATUS.md for consistency with the corrected statements, validating the JSON, and re-running the arithmetic:

STATUS.md's §7 summary is consistent with the corrected text (no proximity claim repeated). One last sweep — arithmetic re-check and a citation-resolution check across all deliverables:

Pre-delivery audit complete. Three defects were caught and fixed, plus four refinements; everything else reconciled cleanly.

## Errors fixed (substantive)

**1. Unsupported authority — §7 of `advice_to_hr.md`** — I had attributed an adverse-action standard ("actions that would dissuade a reasonable worker") to `library/title_vii_704a.md`. That standard is **not in the library** — the file covers only causation routes (proximity, pretext, direct evidence) and never defines which actions are "adverse." Rewrote the bullet: the PIP's independent actionability is now explicitly flagged as **unverified** and logged in QUESTIONS.md's analytic limits, and the verified direct-evidence/pretext basis is what now carries the point.

**2. Wrong legal direction — §7 last-question paragraph** — I wrote that a post-leave action "keeps the temporal-proximity story alive months later," which contradicts the library (proximity helps only when it's *days to a few weeks*). Replaced with the correct analysis: months-later timing makes the proximity route drop out (favorable to the company), but Hale's 10/2 email and the comparator pretext don't age out — so waiting helps only if the eventual decision is genuinely record-based, not calendar-based.

**3. Overclaimed negative rule — §7 sequence** — "the law does not require waiting for her leave to end" asserted positive law beyond the library. Reframed as what the evidence actually supports: nothing *in this library* requires waiting; what it requires is that no action rest on grounds influenced by the leave or complaint.

## Reconciliations fixed (accuracy)

4. **§6 of advice memo** — "(96% → 92% → 88%, 'Meets' every year)" misstated the personnel file: 88% is unrated 2026 YTD, and it omitted the 101% (2023). Now reads 101 → 96 → 92 → 88 YTD, rated "Meets" 2023–2025, after the 2022 "Exceeds" at 118%.
5. **"24 days" staleness — §2.2** — the complaint-unanswered count is 24 days as of the contemplated 10/6 date but 43 and counting as of today; both now stated.
6. **FMLA remedy wording** (JSON, advice §5.3, QUESTIONS.md) — "2 × lost base pay [liquidated damages]" conflated the loss and the liquidated add-on. Now mirrors `library/fmla_2615.md` precisely: lost wages + equal liquidated (double) amount + fees + reinstatement, with base pay clearly labeled a proxy until pay data exist.
7. **JSON proximity entry** — the 24-day gap was lumped with the 4-day gap as "very close proximity"; now marks 4 days as squarely inside the window, 24 days at its outer edge (and gone entirely if postponed months).
8. **§7 sequence lead-in** — "decided by a decision-maker independent of..." tightened to the library's actual prohibition (no decision on leave/complaint-influenced grounds).

## Verified clean

- **JSON structure**: parses; `terminate_today: no`; 5 claims high/high/high/medium/low; 9 recommended-course items; 8 defect entries; hold basis cites `library/litigation_hold.md`; all case names (Oubre, Zubulake, Burlington Northern, Faragher/Ellerth) trace to library file content.
- **Citations**: the sweep shows exactly the six `INDEX.md` files, nothing outside the library.
- **Facts**: every quoted figure re-checked against source documents (attainment, ages, dates, the 10/2 email verbatim, term 7 contents, hire date, no-prior-discipline).
- **Arithmetic**: all 17 computations re-run programmatically — all verified (4/24/43-day gaps, 6/3/4-day gaps, PIP day 39 of 60 expiring 11/15, 14-/4-day OWBPA shortfalls, 13-pt total decline, 2nd-of-5 ranking margins).
- **STATUS.md** reflect the corrected §7 accurately (no proximity claim propagated elsewhere).

The engagement remains **COMPLETE WITH OPEN ITEMS** — the three client-side unknowns (base pay/entitlements, complaint custodians, pipeline-hygiene data) and the library-gap flags (FMLA-waiver validity, §703 elements, ADEA liability elements) stay open, and no supported client fact changes the recommendation.