I'll re-verify everything against source data and the library, rather than trusting my own earlier pass.

A cross-deliverable discrepancy just surfaced in line 27a. Let me audit the CSV rows behind each line and recompute:

This is worse than a labeling issue — the line 27a items in my narrative don't match the CSV or the bank. Let me pull the full document inventory and the complete classification table:

Critical finding: the narrative cites documents that do not exist in `documents/` (invoices, an expense notebook, a mileage CSV, a PayHub summary, a client letter), and its line 27a itemization doesn't match the bank. Let me extract the real PDFs to establish what the evidence actually shows:

The mileage notebook confirms the 278 business miles. Now let me read all four deliverables in full to fix them precisely:

The md on disk is cleaner than I recalled — its 27a itemization does match the bank. Let me now verify the JSON structure and every stated figure arithmetically:

"±$28.62" and the fake-document citations aren't on disk — good. Remaining fixes: the monthly-fee overstatement (md ×2, STATUS, QUESTIONS) and the line 30 attribution. Let me verify the February deposit detail and read STATUS/QUESTIONS:

Now applying the fixes. First, the line 10 monthly-fee overstatement in `schedule_c.md`:

Now a final end-to-end verification pass — JSON validity, sums, CSV integrity, citations, and the full md read-through for consistency:

Sign error in my sensitivity check (deducting mileage lowers net profit). Re-verifying with correct signs, plus how the md names its sources:

One last segment of the md I haven't re-read this pass (lines 22–40):

Self-review is done. I went through every deliverable against the raw `documents/` files (re-extracted all PDFs, re-parsed the bank CSV, and re-ran every total in Python). No dollar figure changed; five statements were wrong or overstated and are now fixed.

## Changes made

1. **`schedule_c.md` — line 10 paragraph (fee reconciliation overstatement).** It claimed grossing each payout up "reproduces exactly a 2.900% fee in all 11 months." That's more than the evidence supports: the 1099-K prints only box 5a (Jan $0.00) and box 5b (Feb $1,866.68) — boxes 5c–5l say "see payee portal." Reworded to exactly what the file shows: the Feb box ties to the 2/6 payout (1,866.68 × 0.971 = 1,812.55, fee $54.13 = 2.900%), the $0.00 Jan box matches the first payout landing 2/6, and the annual tie-out is exact (40,150.85 ÷ 0.971 = 41,350.00 to the cent); other months are not independently verifiable without the portal export.
2. **`schedule_c.md` — "unverified beliefs" bullet.** Same fix: "…and month by month at 2.900%" replaced with the annual reconciliation plus the one February box tie.
3. **`schedule_c.md` — line 30/31 section (unsupported authority).** It said "No home-office deduction (line 30) is claimed," implying the library defines line 30 as a home-office line. The library excerpt defines only lines 1, 9, 10, 13, 15, 18, 20b, 24a, 24b, 25, 27a — nothing for lines 28–31. Reworded: line 30 is reported as line 1 − line 29 under the engagement's convention, no §280A deduction is claimed because no qualifying facts are in the file, and the numbering is labeled as convention, not cited authority.
4. **`schedule_c.json`** — added a matching `line_notes` entry for line "30" with the same caveat.
5. **`STATUS.md` and `QUESTIONS.md`** — removed the parallel "every month grosses to 2.900%" / "each month grosses to 2.900%" claims, replaced with the annual tie plus the Feb-box tie.

## Checked and found correct (no change)

- **Arithmetic:** expense lines sum to line 29 = $10,973.63; line 1 − 29 = line 30 = line 31 = $39,776.37; Schedule SE: $36,733.48 net earnings, $5,620.22 tax, $2,810.11 half. Every sensitivity endpoint re-derived exactly ($5,399.46 / $5,506.48 / $5,515.10 / $5,646.50 / net $38,651.37; SE moves ±$26.28 per 10 points of utilities — an earlier bad "±$28.62" figure does not appear in any file on disk).
- **Line 27a = $4,058.88** matches the bank exactly: Figma 540 + Adobe 719.88 + DesignWeek 650 + MacBook 2,149. (An earlier scare about a $4,108.88 itemization with camera/print/dues/day-rate items was not present in the written files.)
- **`classification.csv`:** 149 rows + header, 1-for-1 match to the bank export, all classifications within the allowed set; 24b (gross $190 → $95) and line 25 (gross $1,860 → $1,116 at 60%) differ from line values only as their notes explain; line 9 has no bank row by design (mileage comes from the notebook photo), explained in the md.
- **Citations:** grep across all five deliverables found zero references to documents that don't exist in `documents/` (no invoice PDFs, expense notebook, mileage CSV, PayHub summary, or client letter are cited) — only the nine real files and library `INDEX.md` entries are referenced.
- **Source facts re-extracted and re-verified:** W-2 boxes 1 = 3 = 5 = $24,800 (bank: 8 deposits × $2,437.85 = $19,502.80); 1099-K box 1a $41,350, 61 transactions; NECs $18,500 / $12,200 / $9,400; notebook total 4,860 mi = 278 claimed + 1,200 Larkspur + 2,232 coworking + 1,150 page-2, 278 × $0.70 = $194.60; 11 PayHub payouts = $40,150.85.

`STATUS.md` stays **COMPLETE WITH OPEN ITEMS** — assumptions A1–A4 and the eight open items are unchanged; this pass only corrected statements about what the evidence actually shows.