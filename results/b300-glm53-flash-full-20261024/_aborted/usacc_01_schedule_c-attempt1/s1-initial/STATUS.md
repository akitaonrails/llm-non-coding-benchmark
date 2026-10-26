# STATUS — **COMPLETE WITH OPEN ITEMS** (post-questionnaire reconciliation)

The client's answers have been received and reconciled. Q1, Q4, Q5 (Denver/gift leg) and Q8 are resolved and incorporated; Q2, Q6, Q7 and the page-2 mileage itemization came back with **no additional information** and remain explicitly flagged open items. Deliverables are internally consistent at the figures below.

## Deliverables

| File | Status |
|---|---|
| `deliverable/schedule_c.json` | UPDATED & COMPLETE (post-reconciliation figures; 12 not_on_schedule_c items) |
| `deliverable/schedule_c.md` | UPDATED & COMPLETE (per-line arithmetic + citations; client-confirmation notes; remaining-flag section) |
| `deliverable/classification.csv` | COMPLETE, unchanged this round (149 rows, 1:1 with bank export; class sums verified) |
| `deliverable/QUESTIONS.md` | COMPLETE (Q1–Q8 as sent; answers recorded here and in schedule_c.md, not by rewriting the questionnaire) |
| `deliverable/STATUS.md` | this file |

## Answers received and disposition

| Q | Client answer | Disposition |
|---|---|---|
| Q1 | "Beacon and Orchard both pay me through PayHub. Tessaro pays by bank transfer." + "PayHub takes 2.9% off the top." | **Incorporated as confirmation.** Line 1 stays $50,750.00 (1099-K gross $41,350.00 + Tessaro $9,400.00, include-once rule); Line 10 stays $1,199.15 = $41,350.00 × 2.9%. |
| Q3 (partial) | "The rest is client stuff and the coworking space" (re: miles other than the ~1,200 Larkspur commute) + confirms the Larkspur miles were commuting ("I guess that's commuting?" — yes). | **Incorporated as attestation.** Line 9 stays 1,428 mi × $0.70 = $999.60. Coworking home→office trips (936 + 1,296) stay excluded as commuting absent a home office (Q7 open). Remaining unknown: the 1,150 × $0.70 = $805.00 has log label + attestation but no page-2 per-trip support. |
| Q4 | "Phone and internet are maybe 60% work. I don't have a separate line." | **Incorporated.** Line 25 = 60% × $1,860.00 (T-Mobile $1,020.00 + Spectrum $840.00) = **$1,116.00**. Flagged: client estimate without separate records; each 10pp = $186.00. |
| Q5 (partial) | "Denver was my cousin's wedding, nothing work-related." | **Incorporated.** Denver flight $389.00 + wedding gift $200.00 confirmed personal (as classified). SF trip/Tartine: no further information → stand as drafted (line 24a $1,030.00; line 24b $95.00). |
| Q8 | "That's my own health plan after I left Larkspur. Not through any employer." | **Incorporated.** BCBS $3,040.00 (May–Dec) stays on Schedule 1 line 17; no BCBS premiums were paid Jan–Apr (W-2 employer coverage, box 12 DD $1,960.00). SEHI limitation rule itself remains unverified in the library (noted in MD). |
| Q2 | No additional information. | **Open — data gap.** Figures end 2025-12-12. Late-December receipts would add to Line 1 (+$141.30 SE tax per $1,000.00); a 2026-01-15 payment for TY2025 would add beyond the $6,500.00 on Form 1040 line 26. |
| Q6 | No additional information. | **Open.** MacBook $2,149.00 expensed on line 27a at 100% business use; each 10% personal = $214.90. |
| Q7 | No additional information. | **Open.** No home office claimed: line 30 = $0.00, rent $19,800.00 personal (IRC §262(a)), home→coworking 2,232 mi excluded. If a qualifying exclusive/regular space exists: line 30 opens and up to 2,232 × $0.70 = $1,562.40 could move onto line 9. |

## Final headline figures

- Line 1 gross receipts **$50,750.00** (= $41,350.00 + $9,400.00, client-confirmed)
- Line 9 **$999.60** (1,428 × $0.70; commuting 3,432 mi excluded)
- Line 25 **$1,116.00** (60% × $1,860.00 — client estimate, flagged)
- Line 28 **$11,778.63** = 999.60 + 1,199.15 + 0 + 480 + 0 + 2,800 + 1,030 + 95 + 1,116.00 + 4,058.88
- Line 29/31 net profit **$38,971.37**
- Schedule SE: net earnings **$35,990.06** (× 0.9235); SE tax **$5,506.48** (× 0.153); ½ SE tax **$2,753.24** → Schedule 1 line 15. Wage base: $24,800.00 + $35,990.06 = $60,790.06 ≤ $176,100.

## Remaining unknowns (explicit, per contract)

1. **Q2 data gap** — export ends 2025-12-12; Dec 13–31 activity and any 2026-01-15 estimated payment unverifiable (quantified impact above).
2. **Q3 substantiation** — $805.00 of line 9 rests on the log label ("other client errands") + client attestation; page 2 of the notebook was never provided. If disallowed: line 9 = $194.60, line 28 = $10,973.63, line 31 = $39,776.37, SE tax = $5,620.22.
3. **Q5(SF)** — the October trip is treated as business on the bank record (DesignWeek registration $650.00) without an explicit written confirmation from the client.
4. **Q6 MacBook** — 100% business use assumed, unconfirmed.
5. **Q7 home office** — none claimed; reopening need quantified above.
6. **SEHI rule** — the employer-coverage eligibility limitation (Schedule 1 line 17) is still not verifiable from the library; the factual posture is resolved (own plan May–Dec; W-2 coverage Jan–Apr; no Jan–Apr BCBS premiums paid).

## Reminders / notes (unchanged)

1. **De minimis safe harbor:** attach the election statement to the return (MacBook, Reg. §1.263(a)-1(f), ≤ $2,500/item).
2. **Line numbering:** office expense is **line 18** per the library excerpt (an earlier working note said 16; the library controls).
3. **Rounding:** all amounts to cents, ROUND_HALF_UP; SE lines rounded sequentially as entered on the form (NE → tax → ½ = $2,753.24).
4. **Lines 2–7** are arithmetic pass-throughs on top of Line 1: 0 / 50,750.00 / 0 / 50,750.00 / 0 / 50,750.00.
5. **W-2 informational:** 8 × $2,437.85 = $19,502.80 net credits vs implied net $20,592.80 ($1,090.00 gap) — W-2 boxes control the 1040; no Schedule C impact.
6. **CSV vs form:** `classification.csv` records bank activity **gross** by design — the 24b group shows −$190.00 (50% rule yields $95.00 on the form) and the 25 group shows −$1,860.00 (60% client estimate yields $1,116.00 on the form). Not an inconsistency; the classes classify transactions, the form applies percentage rules.
7. **Authority scope:** only library files in `library/INDEX.md` cited; the SEHI limitation remains the one flagged unverified rule.

## Validation performed (post-reconciliation)

- `schedule_c.json` re-verified with Decimal ROUND_HALF_UP: line 25 = 1,860 × 60% = 1,116.00; line 28 = 11,778.63; 50,750.00 − 11,778.63 = 38,971.37; SE chain 35,990.06 → 5,506.48 → 2,753.24; wage-base check passes.
- Cross-checks JSON ↔ MD ↔ classification.csv agree on all shared figures; alternates quoted in the MD (no-1,150-miles and Tartine-personal scenarios) re-derived and matching.
- Classification class sums unchanged and still tie (business_income $49,550.85 = deposits = line 1 − line 10, etc.).
