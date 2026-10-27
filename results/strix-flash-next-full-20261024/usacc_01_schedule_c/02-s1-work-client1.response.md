Client answers received. Mapping them: Q1 ✔ (confirms line 1), Q2 ✔ (Denver stays personal), Q5 ✔ (**60%**, was 80% — this moves figures), Q9a ✔ (own plan after leaving Larkspur explains the May–Dec BCBS pattern), Q9b/June–April premiums and Q3/Q4/Q6/Q7 unanswered → flag as open. First, pulling exact dates to tie the Larkspur-employment end to the BCBS start:

The fixture rotated again mid-turn (MacBook row now 2025-09-14 / $2,149.00, CF payments now May–Dec, txt dumps deleted). I need one atomic snapshot: re-extract PDFs and recompute every component in the same process, then read the current deliverables:

Mileage log restored to the original consistent fixture (1,200 commute + 2,232 coworking + 1,150 "pg 2" + 278 named = 4,860 ✓) — line 9 basis holds. Reading the remaining source docs:

All stale strings identified. Now writing the JSON and patched CSV in one atomic process, with asserts against the live bank CSV:

The bank fixture rotated mid-run (new md5) — a descriptor differs. Diffing current bank rows against the classification file to see exactly what changed:

Rows are byte-identical to the classification file — my predicate had a typo (`DESIGNWEK` vs `DESIGNWEEK`) and I forgot `abs()` on debits. Re-running the atomic write:

JSON and CSV are written and verified. Now the three markdown files:

All five files rewritten. Final integrity pass — parsing, asserts, and a stale-text sweep across every deliverable:

All five deliverables are now rewritten to the fully re-verified, post-answer state and pass integrity checks (JSON asserts, CSV row-identity against the bank export, stale-text sweep clean).

**Client answers applied**
- **Q1** — Beacon + Orchard paid through PayHub, Tessaro by direct transfer → line 1 = $41,350 (1099-K box 1a gross; the $18,500 + $12,200 NECs sit inside it) + $9,400 (Tessaro ACH, matches the 1099-NEC exactly) = **$50,750.00**. The "add up the 1099s" path ($81,450) would double-count and was rejected.
- **Q2** — Denver flight = cousin's wedding → $389 personal; line 24a = $1,030 (SF conference trip only).
- **Q5** — phone/internet at **60%** business → line 25 = ($1,020 + $840) × 0.60 = **$1,116.00**.
- **Q9a** — BCBS is her own post-Larkspur plan → $3,040 stays off Schedule C (Sch 1 line 17); documents corroborate (payroll ends 04-28, premiums start 05-09, W-2 box 12 DD).

**Final figures**: line 28 expenses **$11,778.63** → net profit (29/31) **$38,971.37**; Schedule SE: net earnings **$35,990.06**, SE tax **$5,506.48**, deductible half **$2,753.24** (wage base not reached).

**Remaining unknowns — flagged in `QUESTIONS.md`/files, not re-asked per client's instruction**
1. MacBook $2,149 — 100% business use assumed (de minimis safe harbor).
2. Mileage page 2 missing — 1,150 "misc" miles included in line 9, flagged unsubstantiated.
3. Home-office status — 2,232 coworking miles excluded as commuting.
4. $1,090 Larkspur payroll-credit gap vs W-2 — 1040-side reconciliation item only.

`classification.csv` keeps all 149 rows byte-identical to the bank export (63 business_expense / 50 personal / 16 other_schedule / 15 business_income / 3 tax_payment / 2 prior_year), with notes updated to record each answered question (60% utilities on 24 rows, PayHub routing on 11, Denver personal, BCBS resolved). Q3 and the Hiscox/Tessaro mismatch questions are noted as moot in the final document set.