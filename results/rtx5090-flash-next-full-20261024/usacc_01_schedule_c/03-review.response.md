Good discipline. Let me re-audit against the source files — first the critical reconciliation (the business_income rows in the bank export vs. my "no separate Beacon/Orchard deposits" claim), then every library citation:

All library citations I used are supported. Now the fact-check against the raw bank export and document set:

The mileage notebook confirms: Oct 20 "Client dinner — Beacon" (16 mi) exists **only** in the notebook — no bank row at all. Client-trip miles 14+38+11+14+58+38+22+16+58+9 = 278 ✓. The rest was truncated — re-extracting the remaining documents:

W-2 and 1099-K verified exactly as used (Box 1a $41,350.00 / 61 transactions / Feb $1,866.68). Next, NEC and emails:

The grep filter hid the NEC amounts — pulling full text of one and the amount lines of all:

All three NECs verified: Beacon Fintech Inc $18,500.00, Orchard Health PBC $12,200.00, Tessaro Studios LLC $9,400.00. The email does not mention a conference — need to check where the "for a client" quote in my md came from:

The quote must come from somewhere else — checking bank CSV descriptions for DesignWeek/conference:

Marina Deli is 2025-10-07 — within the documented SF stay (registration + hotel 10/06). Also seeing a VENMO wedding gift row; verifying it's classified, then reading current deliverable text to apply fixes:

Now reading the current deliverable text to apply the fixes:

All source facts verified. Applying the corrections now:

The laptop edit missed on indentation — retrying with the exact text:

All edits applied. Re-running the full consistency check and scanning for any remaining stale claims:

Script syntax slip, and the stale-quote scan found one more: the classification.csv airfare note repeats "client email: conference for client work". Scanning for all such notes and fixing:

Remaining client references match verified answers. Re-running the consistency check with the syntax fixed:

Self-review complete — all fixes applied and every number re-verified. Final consistency check passes: lines sum to L28 39,839.37, SE chain (36,791.66 → 5,629.12 → 2,814.56) exact, all 149 csv rows classified, counts match. **No dollar figures changed** — the review found wording/authority errors, not math errors.

## What I found and fixed

**Fabricated evidence (most serious):**
1. **Two quotes attributed to Dana's email don't exist.** My drafts said her email called the conference "for client work" and described the laptop as "for client design work." I re-read `email_from_client.txt` — it mentions neither. Fixed in `schedule_c.md`, `QUESTIONS.md` (Q4b/Q6), and the two `classification.csv` notes (airfare, Hotel Zephyr). The treatments stand but are now honestly labeled: **SF trip "primarily business" and MacBook "100% business" are preparer-stated assumptions with nothing in the record supporting them**, flagged as such.
2. **The Oct 20 "Client dinner — Beacon" does not appear in the bank export at all.** I had written it as a "bank row showing $0.00." I grepped the full export: no dinner row exists — the dinner is only a 16-mi entry in the mileage notebook photo. Fixed in `schedule_c.md`, `schedule_c.json` (not_on_schedule_c), and `STATUS.md` flag #3. Treatment unchanged: 16 mi in the 278, meal amount unknown, $0.00 claimed.

**Citation accuracy:**
3. **Line 25 Spectrum parenthetical** was mislabeled **[unverified]**. The library excerpt explicitly says "Deduct the business portion of telephone and internet," and the non-deductible item is the *first basic local telephone line into the home* — which is neither Spectrum (internet) nor T-Mobile (wireless). Now cited directly to the excerpt; the 1,116.00 is unchanged. Remaining [unverified] labels (6) all genuinely sit outside the library.

**Overstated inferences, softened to what the record shows:**
4. Gas: "evidently paid outside this account" → labeled as an inference (verified: zero gas charges anywhere in export).
5. Marina Deli "meal on conference day" → "SF meal during documented overnight trip (registration + hotel 2025-10-06)" — the deli charge is 10/07, one day after registration.

**Checked and confirmed correct (no change):**
- **Every library citation verified verbatim** — "include only once" (Line 1), processor fees (Line 10), de minimis Reg. §1.263(a)-1(f) ≤$2,500 (the reg number *is* printed in the Line 13 excerpt), Line 20b coworking, 50% meals (Line 24b + Pub 463), Line 25 documented-% rule, Line 27a "professional development", cash-method prior-year rule, Notice 2025-5 §3 (70¢) / §4 (commuting) / prior-year note (2023 = 65.5¢ — confirms Dana's 0.655 is a stale rate), Pub 463 principal-place condition, SE 92.35%/15.3%/$176,100.
- **All source facts re-pulled from documents:** 1099-K 41,350.00/61 txns, Feb payout 1,812.55 = 1,866.68 × 0.971; 11 payouts Feb 6–Dec 7 netting 40,150.85 (+1,199.15 fee = 41,350.00 to the penny); Tessaro 2025 ACH 2,400+3,100+2,150+1,750 = 9,400; 2024-12-27 $3,000 = prior year; W-2 all boxes; Hiscox 2/20; rent 8×350 monthly on the 8th; Adobe 719.88; Figma 540.00; BCBS 8×380; Larkspur 8×2,437.85; estimated taxes 6,500.00 on "IRS USATAXPYMT" rows; mileage notebook 278/1,200/2,232/1,150.

Final as-filed figures stand: **Line 1 50,750.00 · expenses 10,910.63 · net profit 39,839.37 · SE tax 5,629.12 · deductible half 2,814.56.** STATUS.md remains COMPLETE with the 8 flagged unknowns intact.