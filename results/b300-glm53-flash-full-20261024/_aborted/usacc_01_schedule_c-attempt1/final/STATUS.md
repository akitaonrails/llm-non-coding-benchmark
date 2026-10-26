# STATUS — **COMPLETE WITH OPEN ITEMS** (post-audit)

The client's answers have been received and reconciled. A full internal audit was then performed: all source material re-read, every form line and every quoted alternative scenario re-derived independently (Decimal ROUND_HALF_UP), and the bank export re-tied row by row. The audit found **one substantive arithmetic error (in an alternate scenario, not in the filed figures)** plus stale wording — all fixed in place. Headline figures are **unchanged** by the audit. Open items remain as flagged below.

## Deliverables

| File | Status |
|---|---|
| `deliverable/schedule_c.json` | COMPLETE (figures unchanged by audit; 2 text fields corrected — BCBS "where", DEN item) |
| `deliverable/schedule_c.md` | COMPLETE (11 audit corrections applied; per-line arithmetic + citations + flagged assumptions) |
| `deliverable/classification.csv` | COMPLETE (149 rows, 1:1 with bank export; 27 row-note strings updated to resolved state; classes/amounts unchanged) |
| `deliverable/QUESTIONS.md` | COMPLETE, unchanged (Q1–Q8 as sent) |
| `deliverable/STATUS.md` | this file (rewritten post-audit) |

## Answers received and disposition

| Q | Client answer | Disposition |
|---|---|---|
| Q1 | "Beacon and Orchard both pay me through PayHub. Tessaro pays by bank transfer." + "PayHub takes 2.9% off the top." | **Incorporated as confirmation.** Line 1 stays $50,750.00 (1099-K gross $41,350.00 + Tessaro $9,400.00, include-once rule); Line 10 stays $1,199.15 = $41,350.00 × 2.9%. |
| Q3 (partial) | "The rest is client stuff and the coworking space" (re: miles other than the ~1,200 Larkspur commute) + confirms the Larkspur miles were commuting ("I guess that's commuting?" — yes). | **Incorporated as attestation.** Line 9 stays 1,428 mi × $0.70 = $999.60. Coworking home→office trips (936 + 1,296) stay excluded as commuting absent a home office (Q7 open). Remaining unknown: the 1,150 × $0.70 = $805.00 has log label + attestation but no page-2 per-trip support. |
| Q4 | "Phone and internet are maybe 60% work. I don't have a separate line." | **Incorporated.** Line 25 = 60% × $1,860.00 (T-Mobile $1,020.00 + Spectrum $840.00) = **$1,116.00**. Flagged: client estimate without separate records; each 10pp = $186.00. |
| Q5 (partial) | "Denver was my cousin's wedding, nothing work-related." | **Incorporated.** Denver flight $389.00 + wedding gift $200.00 confirmed personal (as classified). SF trip/Tartine: no further information → stand as drafted (line 24a $1,030.00; line 24b $95.00). |
| Q8 | "That's my own health plan after I left Larkspur. Not through my employer." | **Incorporated.** BCBS $3,040.00 (May–Dec) stays on Schedule 1 line 17; no BCBS premiums were paid Jan–Apr (W-2 employer coverage, box 12 DD $1,960.00). SEHI limitation rule itself remains unverified in the library (noted in MD). |
| Q2 | No additional information. | **Open — data gap.** Figures end 2025-12-12. Late-December receipts would add to Line 1 (+$141.30 SE tax per $1,000.00); a 2026-01-15 payment for TY2025 would add beyond the $6,500.00 on Form 1040 line 26. |
| Q6 | No additional information. | **Open.** MacBook $2,149.00 expensed on line 27a at 100% business use; each 10% personal = $214.90. |
| Q7 | No additional information. | **Open.** No home office claimed: line 30 = $0.00, rent $19,800.00 personal (IRC §262(a)), home→coworking 2,232 mi excluded. If a qualifying exclusive/regular space exists: line 30 opens and up to 2,232 × $0.70 = $1,562.40 could move onto line 9. |

## Final headline figures (unchanged by audit)

- Line 1 gross receipts **$50,750.00** (= $41,350.00 + $9,400.00, client-confirmed)
- Line 9 **$999.60** (1,428 × $0.70; commuting 3,432 mi excluded)
- Line 10 **$1,199.15** (PayHub 2.9% of $41,350.00)
- Line 25 **$1,116.00** (60% × $1,860.00 — client estimate, flagged)
- Line 28 **$11,778.63** = 999.60 + 1,199.15 + 0 + 480 + 0 + 2,800 + 1,030 + 95 + 1,116 + 4,058.88
- Line 29/31 net profit **$38,971.37**
- Schedule SE: net earnings **$35,990.06** (× 0.9235); SE tax **$5,506.48** (× 0.153); ½ SE tax **$2,753.24** → Schedule 1 line 15. Wage base: $24,800.00 + $35,990.06 = $60,790.06 ≤ $176,100.

## Audit findings and fixes (this round)

1. **Tartine alternate scenario — WRONG and corrected** (`schedule_c.md`). The old alternate ("if Tartine alone were not a business meal: line 28 $11,841.63 / line 31 $38,908.37 / SE tax $5,497.58") moved line 28 *up* $63.00 and profit *down* — the opposite of the premise. Removing the Tartine 50% share ($63.00) lowers expenses: 24b = 64.00 × 50% = **$32.00**; 28 = **$11,715.63**; 31 = **$39,034.37** (net profit **up $63.00**); NE = **$36,048.24**; SE tax = **$5,515.38**; ½ = **$2,757.69**. All arithmetic now shown in the MD. The filed figures (primary scenario) were never affected.
2. **Wrong-direction subtraction in the mileage narrative — fixed** (`schedule_c.md`). "$999.60 − $3,183.30" read backwards; corrected to $3,183.30 − $999.60 = **$2,183.70** by which the client's claim overstates line 9.
3. **Unsupported payroll speculation — removed** (`schedule_c.md`). The unexplained $1,090.00 W-2 net-vs-bank gap had been smoothed over as "likely benefit/payroll detail"; it is now stated plainly as **not explained by anything in the export**.
4. **Mileage-log internal inconsistency — now documented (immaterial)** (`schedule_c.md`). The log's May–Aug block (936 mi, labeled "3×/wk, 9 mi r/t") only reconciles with its own label if the round trip is ~18 mi; the Sep–Dec block (1,296 mi) implies ~4.1 trips/wk at 18 mi r/t vs the "3×/wk" label. The MD quotes the log labels and states why the inconsistency is immaterial: every mile of both blocks is home↔coworking **commuting** and is excluded at any distance.
5. **Four log trips with no matching bank debits — flagged** (`schedule_c.md`, Line 18 + data-gap sections). Mar 3 print shop, Aug 21 camera rental, Oct 20 client dinner, and Dec 3 supplies run appear in the mileage log but have **no corresponding debit anywhere in the single-account export**. The log evidences trips, not expenditures; nothing is added to Schedule C for them (Q2-class documentation gap).
6. **Line 25 library carve-out — quoted verbatim.** The MD now quotes the excerpt's exact sentence ("the cost of basic local telephone service for the first line into your home is not deductible") and explains why it does not apply: T-Mobile is a wireless plan and Spectrum is home internet — neither is basic local telephone service for a first residential line. If such a line were inside the $1,860.00, it would be excluded 100%, not at 60%.
7. **Stale/broken prose fixed** (`schedule_c.md`): garbled "at $0 a pre-confirmation sensitivity alternative" removed; the Q1 assumption header de-escalated from "confirmation requested" to **confirmed by client (Q1)**; "qualifying qualifying-use home office" → "qualifying home office (exclusive and regular business use)"; "business casual" → "business is conducted"; "box 5a–l Feb" → "box 5b (Feb)"; "include-taxed-once rule" → "include-only-once rule".
8. **classification.csv — 27 row notes updated** so the CSV states the resolved, conventionalized position instead of pre-answer placeholders: 12 T-Mobile + 12 Spectrum rows ("$0 deducted pending" → Q4 answered, 60% applied, form shows $1,116.00, CSV records gross by design); Tartine row (Q5: stands as drafted, DesignWeek registration $650.00 corroborates); DEN flight row (client-confirmed wedding, no "confirm" tail); MacBook row (unconfirmed per Q6). **Class assignments and amounts untouched**; all sums still tie.
9. **schedule_c.json — 2 text fields updated**, figures untouched: BCBS "where" now records the client-confirmed posture (own policy after leaving Larkspur; no Jan–Apr BCBS premiums) while keeping the SEHI employer-availability rule flagged unverified; DEN item records the client's wedding confirmation.
10. **"transfer" classification: correctly unused.** The schema includes a `transfer` class, but it has **zero rows** — the export contains no internal transfers between the client's own accounts ("I only have the one checking account"). The two transfer-*looking* items (Venmo wedding gift, Zelle rent) are personal expenditures, classified `personal`. Class-sum totals tie with the class unused.

## Remaining unknowns (explicit, per contract)

1. **Q2 data gap** — export ends 2025-12-12; Dec 13–31 activity and any 2026-01-15 estimated payment unverifiable (quantified impact above). Also bounds expense matching: the four no-debit errand trips (audit item 5) cannot be costed from this file set.
2. **Q3 substantiation** — $805.00 of line 9 rests on the log label ("other client errands") + client attestation; page 2 of the notebook was never provided. If disallowed: line 9 = $194.60, line 28 = $10,973.63, line 31 = $39,776.37, SE tax = $5,620.22.
3. **Q5(SF)** — the October trip is treated as business on the bank record (DesignWeek registration $650.00) without explicit written confirmation from the client; stands as drafted after Q5.
4. **Q6 MacBook** — 100% business use assumed, unconfirmed.
5. **Q7 home office** — none claimed; reopening effect quantified above.
6. **SEHI rule** — the employer-coverage eligibility limitation (Schedule 1 line 17) is still not verifiable from the library; the factual posture is resolved (own plan May–Dec; W-2 coverage Jan–Apr; no Jan–Apr BCBS premiums paid).
7. **Mileage-log arithmetic** — internally inconsistent (audit item 4); noted in the MD as immaterial to the outcome, since both affected blocks are nondeductible commuting regardless of distance.

## Reminders / notes (unchanged)

1. **De minimis safe harbor:** attach the election statement to the return (MacBook, Reg. §1.263(a)-1(f), ≤ $2,500/item).
2. **Line numbering:** office expense is **line 18** per the library excerpt (an earlier working note said 16; the library controls).
3. **Rounding:** all amounts to cents, ROUND_HALF_UP; SE lines rounded sequentially as entered on the form (NE → tax → ½ = $2,753.24).
4. **Lines 2–7** are arithmetic pass-throughs on top of Line 1: 0 / 50,750.00 / 0 / 50,750.00 / 0 / 50,750.00.
5. **W-2 informational:** 8 × $2,437.85 = $19,502.80 net credits vs implied net $20,592.80 ($1,090.00 gap, unexplained in the export) — W-2 boxes control the 1040; no Schedule C impact.
6. **CSV vs form:** `classification.csv` records bank activity **gross** by design — the 24b group shows −$190.00 (50% rule yields $95.00 on the form) and the 25 group shows −$1,860.00 (60% client estimate yields $1,116.00 on the form). Not an inconsistency; the classes classify transactions, the form applies percentage rules.
7. **Authority scope:** only library files in `library/INDEX.md` cited; the SEHI limitation remains the one flagged unverified rule.

## Validation performed (post-audit)

Automated re-verification (`/tmp/opencode/validate_final.py`, Decimal ROUND_HALF_UP): **130/130 checks passed**.

- **Bank export:** 149 rows; running-balance chain exact on every row; implied opening $4,210.33 → closing $32,955.15; net +$28,744.82; PayHub payouts $40,150.85; Tessaro total $12,400.00 ($3,000 prior-year + $9,400 2025); 1099-K probe: box 5b Feb $1,866.68 × 0.971 = $1,812.55 = payout 2025-02-06 to the cent.
- **classification.csv:** 149 rows, 1:1 sequence (date, amount) with the bank export; class sums business_income $49,550.85 / business_expense −$10,418.88 / personal −$23,265.83 / prior_year $2,915.88 / tax_payment −$6,500.00 / other_schedule $16,462.80 / transfer $0; class totals equal net movement; CSV business_expense bridges to line 28 exactly (10,418.88 − 1,860 + 1,116 − 95 + 999.60 + 1,199.15 = 11,778.63).
- **All Schedule C lines re-derived:** L1 50,750.00; L10 1,199.15 (= 41,350 × 2.9%); errand miles 278; L9 (278 + 1,150) × 0.70 = 999.60; commuting blocks 936 + 1,296 = 2,232; client claim 4,860 × 0.655 = 3,183.30 and overstatement 2,183.70; L25 (1,020 + 840) × 60% = 1,116.00; L27a 4,058.88; L28 11,778.63; L29/31 38,971.37.
- **SE chain re-derived:** NE 35,990.06 → tax 5,506.48 → ½ 2,753.24; wage base 60,790.06 ≤ 176,100.
- **Every quoted alternate re-derived and matching:** Q1 base row (10,662.63 / 40,087.37 / 37,020.69 / 5,664.17 / 2,832.09); Q1 rows with Beacon outside (58,587.37 / 54,105.44 / 8,278.13 / 4,139.07), Orchard outside (52,287.37 / 48,287.39 / 7,387.97 / 3,693.99), both outside (70,787.37 / 65,372.14 / 10,001.94 / 5,000.97); Q3 disallow (194.60 / 10,973.63 / 39,776.37 / 36,733.48 / 5,620.22); **corrected Tartine alternate** (32.00 / 11,715.63 / 39,034.37 / 36,048.24 / 5,515.38 / 2,757.69).
- **W-2 checks:** SS 1,537.60 = 6.2%, Medicare 359.60 = 1.45%, implied net 20,592.80, bank payroll credits 19,502.80, gap 1,090.00.
- **JSON agreement:** 21-key lines dict matches recomputation; SE triple matches; 12 not_on_schedule_c items with matching amount set.
- **MD ↔ JSON ↔ CSV:** every headline and alternate figure present in `schedule_c.md`; zero stale strings across all three files (16-point scan incl. "****ASSUMPTION", "$0 deducted pending", "business purpose to confirm", "(confirm, Q6)", the superseded Tartine trio 11,841.63 / 38,908.37 / 5,497.58, "qualifying qualifying", "business casual", "include-taxed-once", "box 5a–l", "subject to open item").
- **Mileage-log diagnostics:** 936 mi May–Aug = 3.0 trips/wk at 18 mi r/t (label-consistent only at ~18 mi r/t, not 9); 1,296 mi Sep–Dec = 4.1 trips/wk at 18 mi r/t vs the label's 3×/wk — the documented inconsistency, immaterial as noted.
