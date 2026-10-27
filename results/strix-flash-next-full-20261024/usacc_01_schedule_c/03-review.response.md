Running a full pre-delivery audit: (1) verify every cited authority actually exists in `library/`, (2) re-extract all PDFs fresh and re-tie every asserted number, (3) sweep the bank rows for anything I mis-described:

Bank-PDF↔CSV cross-check plus the remaining asserted rows (phone/internet, gift/gym/streaming), email text, and a stale-reference scan of QUESTIONS/STATUS:

All CSV-level assertions tie. The PDF↔CSV comparison regex failed on layout — fixing that, and reading QUESTIONS/STATUS in full before edits:

Header totals tie perfectly (credits $72,053.65, debits $43,308.83, ending balance computes). The one parse diff is my sign-capture regex, not a data diff — re-checking by (date, description, running balance):

Checking the exact current wording of those sections:

Verifying my paraphrases against the exact library wording for lines 20b/24a, then continuing with the remaining md edits:

Library wording confirmed — tightening my two quotes to be verbatim, and applying the remaining paragraph fixes:

Markdown done. Now the JSON — reading its full current content to apply the same corrections:

Applying JSON fixes programmatically (parse → edit → re-dump guarantees validity), and reading STATUS.md for its edits:

JSON validated with all figures asserting. Now the STATUS.md updates:

All edits applied. Final verification sweep — stale-token scan across all five deliverables, re-check row identity and distributions, JSON validity, and a visual check of the edited md regions:

One last check — confirming the verbatim line-10 quote matches the library excerpt exactly:

Review complete. **No dollar figures changed** — every correction was a citation, wording, or date fix. Here's the full accounting:

## Errors found and fixed

**Unsupported authority (biggest issue).** Nine citations referenced statutes/regs that are *not* in `workspace/library/`, violating the contract's citation rule. Replaced with the library excerpt text that actually supports each treatment:
- IRC 61(a) (line 1) → the library's line-1 instruction language (report income actually received; include 1099-K/NEC amounts once)
- IRC 162(a) ×5 (lines 10, 15, 20b, 24a, 27a) → verbatim quotes from the instructions excerpt ("Deduct premiums paid for business insurance"; "Rent paid for office space, including coworking memberships…"; "Lodging and transportation while away from home overnight on business"; "other ordinary and necessary expenses not listed elsewhere")
- IRC 164(f) ×3 (SE write-up + JSON) → the library Schedule SE excerpt's own statement that half of SE tax is deductible on Schedule 1 line 15
- Kept IRC 262(a) and Reg. 1.263(a)-1(f) — both are literally named in the library

**Misstatement of record.** The line-10 write-up claimed the $1,199.15 fee "matches 1099-K box 4." Box 4 is *federal income tax withheld* and reads **$0.00** — I re-checked the form. The fee is supported by the bank tie-out ($41,350.00 gross − $40,150.85 payouts = 2.9%), which is what the write-up now says. Also renamed the line-10 header to the library's own label, "Commissions and fees."

**Wrong dates.** Tessaro direct ACH deposits were dated 03-14/06-02/08-19/11-04 in the write-up; the bank export says **2025-03-19 / 06-19 / 09-19 / 11-19**. Amounts ($9,400 total) were always right.

**Omission.** The bank export's 2024-12-30 H-E-B debit ($84.12) was classified `prior_year` but never listed in the exclusions — added to the write-up and JSON (now 7 `not_on_schedule_c` entries).

**Phantom categories.** "Personal shopping" and "transfers between own accounts" were named as personal categories — no such rows exist. Replaced with the actual ones (rent, H-E-B, Netflix, Orangetheory, DEN flight, wedding-gift Venmo).

**Mileage labels** now match the notebook's own wording ("Orchard — Round Rock 38", "Tessaro — Dripping Springs 58").

**Federal ES treatment** relabeled honestly: the library addresses neither income-tax deductibility nor credit placement, so the 1040-credit treatment is marked **UNVERIFIED** (the exclusion from Schedule C itself stands).

## Verified as correct
- Bank PDF ↔ CSV export: all 149 rows identical; header totals recompute exactly (begin $4,210.33, debits $43,308.83, credits $72,053.65, end $32,955.15)
- `classification.csv` row-for-row identical to the export (63 biz_exp / 50 personal / 16 other_schedule / 15 biz_income / 3 tax_payment / 2 prior_year)
- Every component sum ties: PayHub 11 payouts = $40,150.85; rent 12 × $1,650; BCBS 8 × $380; coworking 8 × $350; utilities 12 × $85/$70; line 28 = $11,778.63; net $38,971.37; SE $35,990.06 → $5,506.48 → $2,753.24
- Mileage math: 1,428 × $0.70 = $999.60 (0.655 correctly rejected as the 2023 rate per Notice 2025-5)
- All remaining authority tokens in the deliverables are library-supported; JSON re-validated with figure asserts

Files changed: `schedule_c.md`, `schedule_c.json`, `STATUS.md` (new "Pre-delivery review corrections" section). `classification.csv` and `QUESTIONS.md` needed no changes.