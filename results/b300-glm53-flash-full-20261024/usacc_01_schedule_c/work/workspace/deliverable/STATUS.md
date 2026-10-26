# STATUS — Okafor 2025 Schedule C / SE engagement

**Status: COMPLETE WITH OPEN ITEMS**

All required deliverables are written:

| Deliverable | State |
|---|---|
| `deliverable/schedule_c.json` | Final figures: line 1 $50,750.00; line 28 $10,962.43; line 31 $39,787.57; SE tax $5,621.80 |
| `deliverable/schedule_c.md` | Per-line explanations with arithmetic and library citations |
| `deliverable/classification.csv` | All 149 bank transactions classified (business_income 15, business_expense 39, other_schedule 16, personal 75, prior_year 1, tax_payment 3; zero transfers — none exist in the export) |
| `deliverable/QUESTIONS.md` | 10 questions asked; 5 answered by client (commuting, 60% phone/internet, Denver=wedding, PayHub dedupe, own health plan); remaining pre-opened items carried below |
| `deliverable/STATUS.md` | This file |

Verification performed: bank export reconciles exactly to its own header (credits 72,053.65 / debits 43,308.83 / ending 32,955.15); PayHub payouts sum 40,150.85 and 40,150.85 ÷ 0.971 = 41,350.00 exactly (1099-K gross, 2.9% fee); Feb 1099-K monthly-detail box 5b 1,866.68 − payout deposit 1,812.55 = 54.13 = 2.9%; Tessaro ACH totals 9,400 = NEC line 1; every Schedule C line recomputed independently before filing the JSON.

## Open items / prominent assumptions (client gave "no additional information")

1. **Revenue after 12/12/2025 is unknown.** The bank export is labeled through 1/31/2026 but stops 12/12/2025; no record covers 12/13–12/31. No income assumed for that window; a late PayHub payout or receipt would increase line 1 and the filing would need updating.
2. **MacBook business-use percentage undocumented.** Client answered with nothing. **Assumed 100% business** (no usage record exists; client provided none); the $2,149.00 de minimis item on line 27a would scale down pro-rata on any lower actual business use. The de minimis safe harbor **election statement must accompany the return**.
3. **Phone/internet 60% is a client estimate without a usage log**, while the instructions call for a documented percentage; flagged and recommended a log for the future. Also noted on line 25: the "first line into your home" nondeductibility was read as limited to basic local landline service (Dana has none — wireless only); reading it otherwise would zero the $612.00 phone share.
4. **1,150 "misc (see pg 2)" miles excluded** — log page 2 missing; ~$805.00 at 70¢/mi would be added if later substantiated.
5. **2,232 coworking commute miles excluded** — no qualifying principal-place-of-business home office is established and none was claimed (no Form 8829 opened). A qualifying home office would change both mileage and rent/utilities allocations.
6. **Oct 20 client-dinner trip (16 miles) excluded** — the meal-transport rule is outside the reference library (unverified), and no matching meal purchase exists in the bank data.
7. **W-2 box 12a DD $1,960.00** — Form 2441 treatment unverified; no dependent information exists in the file.
8. **Hiscox premium ($480.00) treated as 100% business insurance** — policy declaration not in file; purchased 2/20/2025 during Dana's final employed months, taken as covering the design practice.
9. **Space between export label and content** — the export's stated date range does not match its contents (see item 1); Dana was asked directly and had no information.

## Pre-delivery review (Oct 25) — corrections made

No figure on Schedule C or Schedule SE changed; these are accuracy and supportability corrections:

1. **Mileage table descriptions now match the log exactly** — Mar 3 is "Print shop — mockups," Aug 21 "Camera rental — North Austin," Dec 3 "Office supplies run" (the draft had generic "client site visit / client work" labels and wrongly tied Dec 3 to Capital Factory). Miles, rate, and line 9 ($183.40 on 262 miles) unchanged; an arithmetic check tying 262 to the log total 4,860 was added.
2. **Line 18 note rewritten** — the draft claimed the Dec 3 supplies run was "the same day as a Capital Factory coworking visit"; neither the log nor the bank data support that (12/3–12/5 debits are recurring Figma/Adobe/Netflix subscriptions only). Line 18 stays $0.00; the 9 miles stay in line 9.
3. **Line 20b note rewritten** — the draft's sentence attributing the May start of the coworking charges to a change in the Zelle rent pattern was garbled and irrelevant (home rent has nothing to do with coworking). Correct support: charges and the log's coworking entries both begin in May; Dana gave no answer on an earlier membership (Q9).
4. **1099-K precision** — "February gross box" corrected to "February monthly-detail box 5b."
5. **Unsupported authority removed** — draft said net profit "flows to Schedule 1, line 3"; that line number is not in the library and is now labeled unverified rather than asserted. Line 31 is tied instead to the Schedule SE excerpt's "net profit from Schedule C."
6. **Invented rationale removed** — the draft justified the line 27a deduction with the claim that the MacBook was Dana's only work computer as a solo designer; no source says that. The 100% business-use figure now rests only on the stated assumption (no usage record exists, see `schedule_c.md`), and STATUS item 2 was corrected to match.
7. **Form placements labeled unverified** — Form 1040 lines 1a/25a/26, Form 2441, and Form 8829 placements are standard-form convention, not in the library; now flagged in `schedule_c.md` and in the JSON "where" strings. Also flagged: the library's Schedule 1 line 17 redirect is its only health-premium rule; eligibility conditions for that deduction are unverified (noted in the JSON BCBS entry).
8. **Full two-way bank reconciliation added** to `schedule_c.md` (credits 72,053.65 and debits 43,308.83 each reconcile exactly, incl. the single 2024 H-E-B row $84.12), confirming `classification.csv` covers 100% of the export's rows and dollars.
9. **classification.csv corrections** — the prior-year Tessaro row's `schedule_c_line` was misleadingly "Schedule C line 1" and is now blank; the 2024-12-30 H-E-B note now identifies it as a 2024 transaction.

Nothing outside `workspace/library/INDEX.md` was used as authority for any deduction or rule; every library-cited position is quoted in `schedule_c.md`, and everything outside it is labeled unverified.
