Good discipline. I'll audit on three axes — (1) every authority/docket cite must trace to the library INDEX or a file in `documents/`, (2) every number must cross-foot, (3) cross-file consistency. First, sweep all docket and statutory citations across the deliverables and check them against the source files:

The probe crashed on a wrong key (`total_receipts` — the file uses `receipts`). That's a bug in my validation script, not in the deliverable. Re-running with the actual keys, plus the segregation.csv cross-foot:

Keys confirmed. Re-running the corrected full-footing probe, and reading `march_mor.json` to re-foot Part 2 payables:

All authority checks pass — the 852-10-45-4/45-6 pins appear verbatim in the library excerpt's body text, so citing them tied to `asc852_fresh_start.md` is supported. Now fixing the four imprecise "May–August" windows (effective date is 9/30/2026, so unknown draws run through September, not August):

One flag: `§327` appears somewhere in the deliverables — and §327 is **not** in the INDEX. Locating it:

Probe bug again — March's top-level keys are `part1`/`part2` (not `part_1`). Fixing the probe and re-running:

All green. Quick visual confirmation of the edited passages, then the change list:

Audit complete — everything now reconciles and every citation traces to the library or a case document. Here is the full record:

## Fixed (4 substantive changes across 6 edits)

1. **Unsupported authority removed — 3 spots.** `§327` was cited as the employment authority for professionals in `session1/response_to_cfo.md` and `session2/professional_fees.md` (×2). **§327 is not in `library/INDEX.md`**, so under the contract's citation rule it cannot be cited. Rewrote to rest on supported authority only: the proposition (professionals paid only via application/award or court-ordered interim procedures) is fully carried by §§330(a)/331 (`bc_330_331.md`), Dkt. 77, and the retention dates in the case file (H&P 3/10/2026 nunc pro tunc, Corbin 3/20/2026).
2. **Imprecise unknown-window wording — 4 spots.** "May–August 2026 DIP draws unknown" was wrong now that Dkt. 214 fixes the effective date at 9/30/2026: post-April draws through September are all unknown. Corrected in `QUESTIONS.md` (Q9), `STATUS.md`, and `session3/emergence_balance_sheet.md` (×2) to "draws after 4/9/2026, through the 9/30/2026 effective date, unknown."

## Verified clean (no changes needed)

**Authority traceability**
- Every docket cite used (Dkt. 9, 22, 31, 48, 61, 77, 83, 214) appears in the source documents. The ones I distrusted specifically hold up: Dkt. 9 is the wage motion (pre-petition wages paid 3/13 up to the §507(a)(4) cap, none exceeded) and Apex's $31,200 pre-petition claim was actually paid 3/24 under Dkt. 48 — so `cod_schedule.json`'s "no discharge arises there" is supported.
- Every statutory/ASC pin in the deliverables maps to an INDEX row (362(a), 363(b)–(c), 503(b), 549(a), 330(a), 331, 108(a)(1)(A), 108(b)(1)–(5), 507(a)(4), ASC 852-10, Form 11-MOR). The ASC 852-10-45-4 to 45-6 pins appear verbatim in the body of `asc852_fresh_start.md` itself, so they're library-supported.
- Outside-library legal points (when a title 11 discharge occurs, short-year rules, deferred-tax measurement) remain explicitly labeled **unverified**, not cited.

**Arithmetic (re-footed end-to-end in Python)**
- March Part 1: 2,262,400 receipts / 490,770 disbursements / 1,771,630 ending — foots; detail lines sum to totals.
- March Part 2: payables 207,826.16 = 18,900 + 140,000 + 45,000 + 3,926.16; LSTC 74,110 = 62,400 + 7,400 + 4,310.
- `segregation.csv`: pre-petition lines total 105,310; less Apex 31,200 (paid) = 74,110 LSTC — correct by design, since the paid Apex invoice still belongs in the pre-petition register.
- April Part 1 (both H&P scenarios): 1,480,300; 1,010,600/1,126,800; 2,241,330/2,125,130 — foots. UST accruals 3,926.16 / 12,010.96 / 12,940.56 foot at 0.8%. H&P 116,200 = 140,000×80% + 4,200, holdback 28,000.
- Session 3: 8.4M×35% = 2.94M; 8.4M − 2.94M = 5.46M; 6.1M − 5.46M = 640,000; GUC 2.94M÷24 = 122,500; split 1,470,000 + 1,347,500 + 122,500 = 2,940,000; PV table endpoints (4% → 2,830,363.93; 12% → 2,628,338.09) reproduce exactly.

## Audit artifacts (not deliverable defects)

Two footing-script crashes during the review were **probe bugs, not file errors** — my validation script used wrong JSON key names (`total_receipts`, `part_1`). The deliverable files were correct; the probes were fixed and re-run.

No figure was forced to balance; the standing unknowns (pre-petition cash sweep, full LSTC schedule, May–9/30 draws, H&P payment date, $16.2M composition, stub NOL) remain flagged in QUESTIONS A1–10 and STATUS as **COMPLETE WITH OPEN ITEMS**.