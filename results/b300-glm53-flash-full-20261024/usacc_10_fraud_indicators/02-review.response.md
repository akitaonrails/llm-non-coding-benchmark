I'll do a systematic re-review: re-verify every number, every library citation, and re-read the deliverables for overstatements. First, let me pull up the current texts and re-check a few source details.

I'll apply the self-review fixes. First, let me read the current exact texts of the three files that need edits.

I need the full notes text of q1_close.json (it was truncated in the read). Let me extract it:

Now let me verify two supporting documents before I add claims that reference them (QUESTIONS.md numbering, approval_policy.md exemption coverage):

QUESTIONS.md confirmed (5 items as expected). I mistyped the policy path — retrying:

Both confirmed: QUESTIONS.md has the 5 questions as expected, and the approval policy contains **no vendor-level PO exemption provision** — so the new "no basis for a vendor-level exemption" sentence is supported. Now applying all fixes:

All 9 communication edits applied. Now the JSON notes and STATUS.md fixes:

All edits applied. Now the final validation pass — JSON validity, leftover-phrase check, and re-verification of the two new arithmetic figures:

All checks pass. The only remaining "evenly spaced"/"amounts structured just under" text is the verbatim quotation of the library's indicator list, which is correct as a citation. A quick read of the edited sections to confirm flow:

The self-review is complete and all fixes are applied and verified. Final state:

**Validation results**
- `q1_close.json` loads as valid JSON; all monthly figures, category ties, and the statement tie (−118,735.42) unchanged and re-verified in Python.
- Both newly added figures confirmed: ADP PAYROLL averages $87,785.65/pay date; payroll-alone exceedance = 526,713.92 − 393,456.90 = **$133,257.02**; combined = $673,050.48.
- Every removed phrase confirmed gone; the only remaining "evenly spaced"/"structured" wording is a verbatim quotation of the library's indicator list, which is correct.

**What changed — `communication_to_dr_r_patel.md`** (9 edits)
1. "Threshold structuring." → factual label "Amounts sit immediately below the two-partner approval threshold," with an explicit "we report the pattern only and do not assert intent" (library indicator quoted).
2. Item 1.2 now also states the approval policy contains no provision for a vendor-level PO exemption (verified against the policy text), so the "exempted by KH" entry is the only support for it.
3. W-9 sentence qualified: trade vendors show W-9s; the utility's entry is marked n/a.
4. Invoice spacing corrected from "even ~8–10-day spacing" to **8–13 days (eight gaps, median 10)** — the 01/22→02/04 gap is 13 days, so "even" was wrong.
5. Item 2 library reference rewritten precisely: the file directly shows 3 of 5 ghost-employee indicators, the fourth is partially present (who hired E-22 is not in the file), and the fifth — address matching another party — is **not** present (E-22's Plano 75094 P.O. box is the same city but a different address/ZIP from the vendor's Plano 75093; proximity noted, no conclusion drawn).
6. Item 3's closing assertion ("the register evidently does not cover all persons paid") removed — replaced with the payroll-only exceedance of $133,257.02 (avg $87,785.65 vs. $65,576.15) and balanced explanation of possible causes; conclusion now reads "the register as provided does not fully evidence the debits."
7. "its sole operating account" → "the operating account" (other accounts unknown; cross-referenced to QUESTIONS.md #2).
8. Summary table: "Policy circumvention" → "Single-person control; amounts immediately below the approval threshold; onboarding documents missing; related-party address match — indicators only, no intent asserted."
9. Summary table payroll row: "register appears incomplete" → "register as provided does not evidence the debits."

**What changed — `q1_close.json`** (3 edits, notes only)
- "amounts structured at 98%-99%" → "amounts at 98%-99% … (pattern consistent with the library's indicator; no intent asserted)."
- "sequential, evenly spaced invoices" → "sequential invoice numbering (SS-100 to SS-108) at 8-13-day intervals (median 10)."
- "no deliverables" → "no deliverables identified on the file." (carried in notes)

**What changed — `STATUS.md`** (3 edits)
- "the 9 'consulting'/'supplies' invoices" → "the 9 invoices (described as consulting, supplies, or equipment maintenance)."
- The assumption-impact line corrected: it no longer says payroll figures "would not" change — the payroll/other allocation of ADP debits could shift once ADP journals decompose them (QUESTION #1); revenue could change per questions 2 and 4.
- Added a 6th open item (QUESTIONS.md #4–5 remain open) and a review note documenting the self-review.

**Fixes from earlier review rounds** (already in place before this round): hourly-staff timeclock range corrected to 468–480, and transaction count corrected to 48 in both remaining spots.

**What changed — nothing**: `QUESTIONS.md` was re-checked fact-by-fact and needed no corrections; P&L figures required no changes anywhere — all edits were accuracy/overstatement fixes to narrative text. Status remains **COMPLETE WITH OPEN ITEMS** with six disclosed open items.