

A proper review pass. I'll audit three axes: (1) every cited authority against the actual library files, (2) every document-derived figure against the source PDFs/CSV, (3) internal arithmetic including sensitivity numbers. Starting with the library — that's where unsupported authority would hide:





The INDEX lists exactly five citable files — and my deliverable cites **Reg. §1.263(a)-1(f)**, which is not among them. Reading all five files to check every other claim:






W-2 reveals something: **box 2 federal withholding $2,310** — income tax withheld at source, which belongs in the 1040 payments discussion alongside the estimates, and isn't in my `not_on_schedule_c` list. Now verifying every bank-derived figure and date:





All merchant sums verify except issues noted below. One gap: payroll deposits ($19,502.80) vs W-2 — checking the client email for storage-unit and payroll facts:





All bank-side figures now traced. Running final numeric verification for the fix list (sensitivity case, payroll reconciliation, mileage amounts), then applying corrections:





All findings confirmed. Applying the fixes across the four files:














Now STATUS.md:









All corrections are applied. Running one final consistency check across all four text deliverables to confirm nothing broke:





Review complete. I re-derived every number from source documents, audited every citation against the five library files, and cross-checked the JSON, markdown, CSV, and STATUS for mutual consistency. Here is everything the review found and what I changed.

## Errors found and fixed

**1. Unsupported authority — the 1,150 "pg 2" mileage exclusion.** The markdown claimed the miles failed "Pub. 463 substantiation requirements," but the library's Pub. 463 excerpt contains **no recordkeeping rule** — so that citation was unsupported. The exclusion itself is right, but on *factual* grounds: with notebook page 2 gone, nothing verifies those miles as business miles. Reframed in `schedule_c.md`, `QUESTIONS.md` R1, and `STATUS.md` item 2, with the believed IRS rule explicitly labeled **unverified, not cited**. (All other citations re-audited and confirmed against the five library files.)

**2. Wrong sensitivity number.** The 0%-business-use case said SE tax = $5,785.42. Recomputed: Line 28 $9,857.63 → Line 31 $40,892.37 → ×0.9235 = $37,764.10 → ×15.3% = **$5,777.91**. Corrected in the markdown.

**3. Missing item — W-2 federal withholding.** Box 2 $2,310.00 was never disclosed anywhere. Added to the `not_on_schedule_c` list (JSON and markdown table): it's a Form 1040 payment alongside the $6,500 estimates, not a deduction.

**4. Payroll didn't reconcile — and my earlier reasoning was wrong.** Recomputed the 8 Larkspur deposits: $19,502.80 actual vs. box 1 $24,800 − box 2 $2,310 − FICA $1,897.20 = $20,592.80 implied take-home → **$1,090.00 gap** of undocumented payroll deductions. (An earlier draft treated box 12a code DD $1,960 as an employee deduction — it's the informational employer health-coverage cost, not withheld from pay.) Disclosed in the markdown limitations and STATUS item 10; W-2 box 1 governs; no Schedule C effect.

**5. Unsupported fact — "storage unit $95/mo."** I grep-tested it: **zero** $95.00 debits in the bank export, no mention in the email or mileage notebook. It appeared only in my own R7/STATUS text — nothing sourced it. Removed; home office is now stated as "no facts establishing a dedicated workspace anywhere," Line 30 = $0.

**6. Wrong date — MacBook.** QUESTIONS R6 said "(Nov 2)"; the bank export shows the $2,149 Apple debit on **2025-09-14**. Corrected.

**7. Incomplete cash-expense disclosure.** The mileage log lists four business trips with **no matching bank debit**: camera rental (8/21), print shop (3/3) — already disclosed — plus **client dinner with Beacon (10/20)** (a meal, 50%-limit) and **office-supplies run (12/3)**, which I had missed. Added to markdown, R2, and STATUS item 4. All four remain unclaimed (no amounts available).

**8. Precision nit.** R5's excluded coworking mileage now reads $1,562.40 (2,232 × $0.70), not "$1,562."

## Verified correct (unchanged)

- **Line 1 $50,750** = 1099-K $41,350 + Tessaro ACH $9,400; Beacon/Orchard NECs confirmed inside the 1099-K via PayHub payout records (counted once) — the sum-of-1099s error stays avoided.
- **PayHub fees $1,199.15 = 41,350 × 2.9%** exactly; Feb payout tie-out $1,866.68 × 97.1% = $1,812.55 ✓.
- **Line 9**: 278 itemized client-trip miles × $0.70 = $194.60; Larkspur commute and coworking round-trips excluded per the Pub. 463 commuting excerpt (supported).
- Every merchant sum re-traced to the 149-row CSV (H-E-B 2025 = $2,102.95; phone/internet $1,860 × 60%; BCBS May–Dec $3,040; coworking $2,800; rent excluded).
- **Bottom line unchanged**: Line 28 $10,973.63 → Line 31 **$39,776.37** → SE base $36,733.48 → SE tax **$5,620.22**, half $2,810.11 to Schedule 1 line 15; wage test passes.

Final automated check passes: JSON math, md/STATUS/QUESTIONS figures, and citation language are all mutually consistent. Remaining open items (60% estimate unverified, missing notebook page 2 worth +$805 if found, export ends 12/12, the four cash items, MacBook 100%-use assumption, unverified BCBS limit) are each listed in QUESTIONS/STATUS.