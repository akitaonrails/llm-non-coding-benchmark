# STATUS — 2025 Schedule C / Schedule SE, Dana Okafor

**COMPLETE WITH OPEN ITEMS**

All five deliverables are written: `schedule_c.json`, `schedule_c.md`, `classification.csv`
(149/149 bank rows classified, header row added), `QUESTIONS.md`, `STATUS.md`. Figures are ready to
file, subject to the stated assumptions and record gaps below; the client has confirmed there is no
further information available, so each open item is closed by a stated position rather than left blank.

## Figures as computed
Line 1 gross receipts **$50,750.00** (PayHub 1099-K gross $41,350.00 + Tessaro direct ACH $9,400.00;
the Beacon $18,500 and Orchard $12,200 1099-NECs are the same PayHub money and are counted once).
Line 9 $194.60 · line 10 $1,199.15 · line 15 $480.00 · line 20b $2,800.00 · line 24a $1,030.00 ·
line 24b $95.00 · line 25 $1,116.00 · line 27a $4,058.88 → line 29 **$10,973.63**; line 30/31 net
profit **$39,776.37**. Schedule SE: net earnings **$36,733.48**, SE tax **$5,620.22**, deductible half
**$2,810.11** (Schedule 1 line 15). Also off Schedule C: BCBS $3,040 → Schedule 1 line 17, W-2 wages
$24,800 → Form 1040 line 1a, estimated payments $6,500 nondeductible.

## Resolved by client answers
- Beacon/Orchard pay through PayHub; Tessaro pays by bank transfer → line 1 confirmed at $50,750.00
  (the "add up the 1099s" figure of $81,450 would double-count $30,700).
- 1,200 Jan–Apr miles were drives to the Larkspur office → commuting, not deductible ($840).
- June 13 Denver airfare $389 was a cousin's wedding → personal, excluded.
- BCBS is her own plan after leaving Larkspur → Schedule 1 line 17, not line 15 (limit vs. SE earnings
  satisfied: 3,040 ≤ 36,733.48).
- Phone/internet 60% business → line 25 falls from $1,860.00 to $1,116.00; net profit rises from
  $39,032.37 to $39,776.37; SE tax from $5,515.10 to $5,620.22.
- **This turn:** PayHub "takes 2.9% off the top before paying out; the 1099-K number is before their
  cut" → the gross-before-fee treatment on line 1 and the $1,199.15 on line 10 are now client-stated, not
  inferred, and they reconcile exactly (41,350.00 × 0.029 = 1,199.15; 41,350.00 × 0.971 = 40,150.85 =
  the 11 payouts; every month grosses to 2.900%). 1099-K box 5a (Jan) $0.00 and box 5b (Feb) $1,866.68
  × 0.971 = $1,812.55 = the 2/6 deposit confirm same-month payout timing, so the full 1099-K gross is
  captured by deposits already in the bank export. Figures unchanged.

## Open items (stated positions, not blockers)
1. **Coworking miles (2,232, $1,562.40) excluded as commuting** — no home office that is a principal
   place of business appears in the file. Largest single exposure; flips to deductible if that fact is
   ever established (sensitivities in `schedule_c.md`).
2. **1,150 notebook miles on missing page 2 ($805) not claimed** — page never provided, no dates,
   destinations or business purpose; client has no additional information.
3. **60% phone/internet split is the client's estimate, not documented** — the instructions excerpt
   asks for a reasonable, documented percentage; $744.00 personal share excluded.
4. **SF trip assumed primarily business** ($1,030 travel + $95 meals); Denver remains out as personal.
5. **MacBook $2,149 expensed under the de minimis safe harbor at assumed 100% business use** — the
   election statement must be attached to the return.
6. **Bank export ends 2025-12-12** despite a nominal period through 2026-01-31. The PayHub 1099-K gross
   reconciles fully to the deposits in the file, so the gap no longer threatens processor income; what it
   can still hide is non-PayHub receipts Dec 13–31, 2025 (another Tessaro or direct transfer, cash) and
   December business purchases. Nothing has been assumed for either.
7. **$3,000 Tessaro invoice of 2024-12-27 excluded as prior-year income** — should be confirmed as
   reported on the 2024 return.
8. Unverified legal beliefs used (cell phone outside the first-line telephone disallowance; federal
   tax nondeductibility; Form 1040 line 1a placement; the Schedule 1 line 17 eligibility conditions) are
   labeled as unverified in `schedule_c.md`. The 2.9% PayHub fee is no longer an inference — the client
   stated it, and the bank export confirms it to the cent.

No figure is forced to balance; every sensitivity is quantified in `schedule_c.md`.
