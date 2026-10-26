Good call — a full pre-delivery audit. I'll re-verify the primary sources (not trust my earlier reads), re-check every figure against the deliverables, and fix discrepancies. Starting with the contract spec and the document inventory:

Sources re-verified. Found several issues already (described below). Let me check `QUESTIONS.md` next since my md references its answers:

Now let me read the current deliverables to apply the fixes:

The generation script is gone, so I'll patch the CSV directly. Let me first look at the rows I need to fix:

Let me verify two facts I'm about to write into the md (the 12/3–12/5 bank rows and the statement's beginning balance):

The balance confirms $4,210.33 / 43,308.83 / 72,053.65 / 32,955.15. The literal flag broke my date regex — retrying:

12/3–12/5 debits are indeed only Figma/Adobe/Netflix recurring subscriptions, and the statement header confirms the tie-out. Let me check the rest of QUESTIONS.md (to make sure my line-20b rewrite matches what was actually asked):

In `QUESTIONS.md`, Q9 asked whether the Capital Factory membership runs Jan–Dec and referenced no earlier charges, so my 20b rewrite will mirror that phrasing exactly. Now applying all fixes — CSV first, then the markdown:

All markdown and CSV fixes applied. Now the JSON `where`-strings and STATUS.md:

All edits applied. Now the final end-to-end verification script — recompute every figure from source and compare against the written deliverables:

Two loose ends from the verification run: the "credits total" check omission (script didn't count the Larkspur net-pay rows classified as `other_schedule`) and the STATUS.md wording of review item 6. Let me look at the exact item-6 text first:

Now rewriting item 6 so the removed phrase doesn't appear in the review log, then rerunning the full verification with the corrected credits formula (business income + prior-year credit + net payroll credits held in `other_schedule`):

95 of 97 checks pass; both failures are check-script artifacts, but let me confirm by looking at the actual text — item 3's quote in STATUS, and how questions are formatted in QUESTIONS.md:

Both are quote-vs-content artifacts: STATUS item 3 quotes the removed garbled phrase, and questions are numbered `1.`–`10.` rather than `**Q`. Fixing the wording and the checks, then rerunning:

Only my own wording expectation for the QUESTIONS.md closing line remains. Let me check what it actually says:

QUESTIONS.md correctly ends at Q10 — the client's "no additional information" statement is engagement context recorded in STATUS.md, not content for the question list, so my check expectation was wrong. Removing it and doing the final clean run:

Pre-delivery review is done and every check now passes (97/97 in an automated re-verification from the raw sources). Status remains **COMPLETE WITH OPEN ITEMS**.

## Conclusion: figures were right; the wording/support around them wasn't

Re-verified everything from origin — re-extracted all source PDFs, re-read the library files, re-ran the two-way bank tie-out — then fixed 14 items. **Not one dollar figure changed**; all edits are accuracy, citation, and supportability corrections.

## What changed

**`classification.csv`** — 2 fixes (149 rows intact)
1. Prior-year Tessaro row (12/27/2024): `schedule_c_line` wrongly said "Schedule C line 1" → now blank, note adds "not on the 2025 Schedule C."
2. The 12/30/2024 H-E-B row: note now identifies it as a **2024 transaction** in the pre-2025 history window (no effect on the 2025 return).

**`schedule_c.md`** — 11 fixes
3. **Mileage table now matches the log verbatim**: Mar 3 "Print shop — mockups," Aug 21 "Camera rental — North Austin," Dec 3 "Office supplies run" (the draft had generic "client site visit / client work" labels and wrongly tied Dec 3 to Capital Factory). Added an arithmetic check: supported 262 = 4,860 − 1,200 Larkspur − 936 − 1,296 coworking − 1,150 misc pg 2 − 16 dinner ✓.
4. **Line 18 note rewritten** — removed the fabricated claim that the Dec 3 supplies run was "the same day as a Capital Factory coworking visit." The 12/3–12/5 debits are recurring Figma/Adobe/Netflix only. Line 18 stays $0.00; the 9 miles stay in line 9.
5. **Line 20b note rewritten** — removed the garbled "Zelle pattern change" sentence (home rent has nothing to do with coworking). Correct support: charges and the log's coworking entries both begin in May; Dana gave no answer on an earlier membership (Q9).
6. **Removed an unsupported authority claim** — "net profit flows to Schedule 1, line 3" isn't in the library; now tied to the Schedule SE excerpt's "net profit from Schedule C," with the Schedule 1 line number labeled unverified instead of asserted.
7. **Removed an invented rationale** — "Dana's sole work computer as a freelance designer" (line 27a). The 100% business-use figure is a stated assumption with no usage record; nothing more.
8. **1099-K precision** — "February gross box" corrected to "February monthly-detail **box 5b**" (1,866.68 − payout deposit 1,812.55 = 54.13 = 2.9%).
9. Coworking-commute bullet now shows the arithmetic: 936 + 1,296 = 2,232.
10. **Added a full two-way bank reconciliation**: credits 72,053.65 = net payroll 19,502.80 + PayHub 40,150.85 + Tessaro 2025 ACH 9,400 + prior-year Tessaro 3,000; debits 43,308.83 = 8,558.88 business charged + 6,500 ES + 3,040 BCBS + 1,020 T-Mobile + 840 Spectrum + 19,800 rent + 185.88 Netflix + 588 OTF + 2,102.95/84.12 H-E-B + 389 Denver + 200 gift; 4,210.33 + credits − debits = 32,955.15 ✓ — proving `classification.csv` covers 100% of rows and dollars.
11. **Added a "Labeling of form placements" section** — Form 1040 lines 1a/25a/26, Form 2441, and Form 8829 placements are standard-form convention, not in the reference library, now labeled **unverified**; also flags that the library's only health-premium rule is the Schedule 1 line 17 *redirect* (eligibility conditions unverified).

**`schedule_c.json`** — 5 `where`-string fixes (numbers untouched)
12. W-2 wages (1a), withholding (25a), and ES payments (26) entries each now carry "(form-line placement outside the reference library — unverified)"; same for the Form 2441 entry.
13. BCBS entry adds: eligibility conditions for the Schedule 1 line 17 deduction are not addressed in the library (unverified).

**`STATUS.md`** — 3 fixes
14. Box 5b precision (as above); assumption 2 rewritten to "(no usage record exists; client provided none)"; and a new **"Pre-delivery review (Oct 25)"** section logging all 9 corrections.

**`QUESTIONS.md`** — re-read, no changes needed (10 questions, 5 answered; Q9 still open).

## Final verification (all PASS)
- Every Schedule C line and SE figure recomputed from the raw CSV/bank/1099 data equals the JSON: line 1 **$50,750.00**, line 28 **$10,962.43**, line 31 **$39,787.57**, SE tax **$5,621.80** (half $2,810.90), cap check 24,800 + 36,743.82 < 176,100 ✓.
- Cross-checks: bridge 8,558.88 + 1,199.15 + 183.40 − 95 + 1,116 = 10,962.43 ✓; 40,150.85 ÷ 0.971 = 41,350.00 exact; banned phrases confirmed absent; unverified-labels confirmed present.

Remaining open items are unchanged and documented in `STATUS.md`: possible Dec 13–31 receipts (bank export stops 12/12), Q9's earlier coworking membership, the meal-transport rule behind exclusion of the Oct 20 dinner, SE health-insurance eligibility conditions, and the mileage log's missing page 2 (1,150 misc miles).