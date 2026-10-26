Reviewing the Session 3 package for arithmetic, citation support, and reconciliation. First, re-reading the deliverables as written and verifying every record citation against the actual documents:

There is no Exhibit C anywhere in the records — the 1,550,000 is derived from `april_activity.md` (April draw of 500,000 + March cumulative of 1,050,000). Also, the library's MOR instructions contain no statement that "the MOR is required while the DIP is unpaid" — that phrasing needs to be corrected. To apply the fix, I'll re-read all three deliverables for Session 3 in full:

All source facts confirmed. Now checking STATUS.md and QUESTIONS.md wording before applying fixes:

All facts traced. I found six issues; applying fixes now. First, the emergence balance sheet (three fixes: the t=0 installment split, the unsupported "Exh. C" citation, the ¶4 mischaracterization):

Now the cod_schedule.json DIP note and the fresh_start.md liability/gain distinction:

One more consistency edit in STATUS.md's session-3 summary bullet, then a final JSON validity + arithmetic check:

All arithmetic re-verified and the JSON is valid. Final sweep for any leftover unsupported strings:

Review complete. Everything checked against the actual record files this pass — including extracting both PDF orders (`pdftotext`) that hadn't been text-verified before. Six problems found and fixed; the rest of the arithmetic and citations verified clean.

## Errors found and fixed

**1. Emergence balance sheet — the effective-date installment was booked as a liability** (`session3/emergence_balance_sheet.md`). The Dkt. 214 stream pays the first installment **on** 9/30/2026, i.e., on the balance-sheet date itself. My draft carried the liability at 2,940,000 with the current split "including the effective-date payment" — wrong. Corrected: the recorded plan-payment liability is the **23 installments still unpaid after emergence** — 2,817,500.00 undiscounted in the monthly illustration (@8%: 2,726,598.54 − 122,500.00 = 2,604,098.54); current 1,470,000.00 (next 12) / noncurrent 1,347,500.00 (final 11); 1,470,000 + 1,347,500 = 2,817,500 ✓. Added a "gain ≠ liability" note to `fresh_start.md`: the gain table correctly discounts all 24 payments (full consideration for the discharge), while the balance sheet carries only amounts still to be paid.

**2. Unsupported citation — "Dkt. 61 Exh. C"** (`cod_schedule.json`, `emergence_balance_sheet.md`). The Dkt. 61 excerpt in the file references **only Exhibit B** (approved budget); there is no Exhibit C roll-forward anywhere in the record. The 1,550,000.00 cumulative draw actually comes from the activity files — replaced with the real sources: 3/12 draw 600,000.00 + 3/26 draw 450,000.00 (`documents/petition_month_activity.md`), 4/9 draw 500,000.00 (`documents/session2/april_activity.md`), authority 2,500,000.00 (Dkt. 61 ¶1, verified). Also flagged what the bad citation had papered over: **May–Sept draws are not in the record**, so the DIP payoff at emergence is not the 4/30 figure.

**3. Mischaracterized court order — Dkt. 61 ¶4** (three files). STATUS item K, QUESTIONS.md, and the emergence sheet said ¶4 "requires MORs while the DIP obligation is outstanding." Verified verbatim, ¶4 says: *"The Debtor shall file Monthly Operating Reports on the UST Form 11-MOR by the 21st of each month"* — no end condition. All three places now quote it verbatim; the May–Sept MORs (due 6/21–10/21/2026, all passed) are required on ¶4's face, and whether post-effective-date MORs are required is flagged as not addressed in the record.

**4. Unsupported UST statement** (emergence sheet): "post-emergence UST fees end with case administration" — the UST fee statute isn't in the library; downgraded to an unverified flag.

**5. Goodwill claim** (emergence sheet): "goodwill is NOT recognized" isn't language the library states; relabeled as an inference from the continue-at-carrying-amounts rule.

**6. DIP figure precision** (`fresh_start.md`, STATUS): 1,550,000.00 now consistently labeled "cumulative at 4/30/2026" with May–Sept draws flagged.

## Verified correct (unchanged)

- **COD schedule**: JSON valid, contract keys; 8,400,000 × 0.35 = 2,940,000; discharged 5,460,000; NOL 6,100,000 → 640,000; election alternative basis → 0, NOL → 3,840,000 — all recomputed.
- **PV/gain table** in `fresh_start.md`: every rate recomputed (5%: 2,803,886.94; 8%: 2,726,598.54; 10%: 2,676,802.05; 12%: 2,628,338.09; quarterly @8%: 2,745,956.72, gain 5,654,043.28) — matches.
- **Quoted authority**: Dkt. 48 (Apex-only Schedule 1, $35,000 cap), Dkt. 61 ¶¶1–3, Dkt. 77 (80/100, 14-day, retention bar), Dkt. 214 (dates, 35%/2,940,000, first installment on effective date, 14.0M/16.2M/60%), and the ASC 852 / §108 library wording — all confirmed against the actual files.

## Still open (disclosed, not fixed — facts not in the record)

Plan discount rate/frequency (gain stays unbooked, floor 5,460,000.00), exit facility terms, DIP rate/fees and May–Sept draws, the five overdue May–Sept MORs (item K), the 16,200,000.00 composition, final fee awards, tax rate/NOL vintages, §382 and imputed interest (tax counsel; not in library).