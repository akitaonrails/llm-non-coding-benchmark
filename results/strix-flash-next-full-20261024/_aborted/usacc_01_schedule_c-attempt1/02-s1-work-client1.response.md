Client answers applied; all five deliverables updated and re-verified.

**Figures now (verified in Python):**

| Line | Amount | Change this turn |
|---|---|---|
| 1 Gross receipts | $50,750.00 | **Confirmed** (Beacon/Orchard via PayHub → counted once inside the 1099-K gross; Tessaro ACH $9,400) |
| 9 Car/truck | $194.60 | Larkspur 1,200 mi now **confirmed commuting** (278 claimed mi × $0.70) |
| 10 Fees | $1,199.15 | PayHub 2.9% retained fee |
| 15 Insurance | $480.00 | Hiscox only |
| 20b Rent | $2,800.00 | Coworking |
| 24a / 24b | $1,030.00 / $95.00 | Denver $389 now **personal** (cousin's wedding) |
| 25 Utilities | **$1,116.00** | 60% × (1,020 + 840); $744.00 personal share removed |
| 27a Other | $4,058.88 | incl. MacBook via de minimis |
| 29 / 31 | **$10,973.63 / $39,776.37** | was $11,717.63 / $39,032.37 |
| Schedule SE | net **$36,733.48**, tax **$5,620.22**, half **$2,810.11** | wage-base test: 24,800 + 36,733.48 = 61,533.48 ≤ 176,100 |

BCBS $3,040 → Schedule 1 line 17 (own plan confirmed; 3,040 ≤ 36,733.48 limit satisfied); half-SE-tax $2,810.11 → Schedule 1 line 15; W-2 $24,800 → 1040 line 1a; $6,500 estimated payments nondeductible.

**Files touched** (`workspace/deliverable/`):
- `schedule_c.json` — line 25 → 1,116.00, lines 29/30/31 and `schedule_se` recomputed; `not_on_schedule_c` now lists 13 items including the $744 personal utilities share, $840 Larkspur and $1,562.40 coworking commuting mileage, and the $30,700 NECs flagged as counted-once (not dropped).
- `classification.csv` — 149/149 rows intact and matched to the bank export line-for-line; header row added; notes updated on 36 rows (12 T-Mobile, 12 Spectrum → 60% split with 612/504 amounts, 11 PayHub → Beacon/Orchard confirmed inside the 1099-K, 1 Southwest → confirmed personal) plus 8 BCBS and 2 meal rows.
- `schedule_c.md` — client-confirmed facts split from the five remaining labeled assumptions (A1 coworking miles = commuting, A2 60% is a client estimate not records, A3 SF trip primarily business, A4 MacBook 100% + election statement, A5 2.9% fee inferred); sensitivities re-quantified (coworking flip +$1,562.40 → SE tax $5,399.46; page-2 miles +$805; utilities ±$186 per 10 points).
- `QUESTIONS.md` — rewritten: no re-asked questions, only record requests (notebook page 2, PayHub portal export, Dec 13–31 bank gap, MacBook personal use, 2024 Tessaro confirmation) with the treatment that stands without them.
- `STATUS.md` — **COMPLETE WITH OPEN ITEMS**, with resolved-this-turn list and 8 stated-position open items.

Largest unresolved exposure: the 2,232 coworking miles ($1,562.40), excluded as commuting because no home office that is a principal place of business appears in the file — Dana has no further information, so it stays a stated position.