Client answers received. Folding them in: phone/internet at client-stated 60% → line 25; Denver flight confirmed personal; income figure now client-confirmed; home-office question remains unestablished (client has no answer) so coworking miles stay $0 with an explicit flag.

All 24 phone/internet rows now classified (12 T-Mobile + 12 Spectrum). Updating the JSON:

Now updating `schedule_c.md`. Let me re-read it to make targeted edits:

Final consistency check across deliverables:

Typo in my check script (`L['schedule_se']` instead of `j['schedule_se']`). Rerunning:

All deliverables finalized and cross-checked. The client answers materially moved four items:

## Updates folded in

| Change | Before → After | Driver |
|---|---|---|
| Line 25 utilities | 0.00 → **1,116.00** | Client-stated 60% business use: phone 1,020.00×60% = 612.00 + internet 840.00×60% = 504.00; personal 40% (744.00) stays off C — flagged as her estimate, no usage records |
| Line 28 net profit | 40,955.37 → **$39,839.37** | total expenses now 10,910.63 |
| Schedule SE tax | 5,786.81 → **$5,629.12** | 39,839.37 × 0.9235 = 36,791.66 × 15.3% (24,800 W-2 SS wages + 36,791.66 still well under the $176,100 base → full rate) |
| Deductible half → Sch 1 l15 | 2,893.41 → **$2,814.56** | |
| June AUS–DEN $389 | pending → **confirmed personal** | "cousin's wedding" — IRC §262, permanently out |
| Line 1 = 50,750.00 | inference → **client-confirmed** | Beacon + Orchard pay through PayHub (double-reporting treatment validated); Tessaro by ACH |

The health plan answer ("my own plan, not through any employer") confirms the BCBS $3,040 sits on Schedule 1 line 17 rather than Schedule C line 15 — but the SE-health *eligibility* rule (especially the Jan–Apr employed months, W-2 box 12 DD) is **not in the library**, so that stays labeled for preparer verification; no line 15 amount claimed.

## Remaining unknowns — flagged, held at $0, not estimated
- **Mileage stays 194.60** (278 mi × $0.70). The client confirmed the 1,200 Larkspur mi are commuting (correctly excluded), but never established a regular-and-exclusive **home office** — so the 2,232 home→coworking miles fail the Pub 463 principal-place condition and the 1,150 "see pg 2" miles remain undocumented. Potential if ever documented: +1,562.40 and +805.00 respectively.
- Oct 20 Beacon dinner (bank row is $0.00, no charge anywhere), SF return airfare, Dec 12–31 bank rows, print-shop/gas purchases outside the account — all unresolvable, flagged with what each would change.
- W-2 net-pay gap $1,090.00 left open (informational; box 1 controls Form 1040 1a).

Consistency checks pass: JSON lines tie to line 28 and SE math to the penny; all 149 CSV rows carry contract-legal classifications; QUESTIONS.md now logs each Q, the verbatim answer, and its disposition. **STATUS.md: COMPLETE.**