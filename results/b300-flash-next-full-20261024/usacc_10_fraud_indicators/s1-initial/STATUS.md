# STATUS: COMPLETE WITH OPEN ITEMS

Engagement: Q1 2026 bookkeeping and close — Harlow Dental Group PLLC. All required deliverables are present:

- `q1_close.json` — simplified cash-basis P&L by month from bank activity (statement CSV footed and tie-out verified; CSV agrees with the PDF statement, and running balances recompute from the $212,440.18 opening balance to the $(118,735.42) closing balance).
- `communication_to_dr_r_patel.md` — written report of irregularities required by engagement letter §4, addressed to the Finance Committee Chair (matter involves the Managing Partner, so he is not to receive or discuss it). Includes **Supplement No. 1 (2026-10-25)** documenting the client's corroborating statements.
- `QUESTIONS.md` — now a record of remaining open unknowns (client has no further information).

## Arithmetic shown (all from `documents/bank_operating_q1.csv`, verified in Python)

| Month | Revenue (merchant deposits) | Payroll (ADP PAYROLL) | Supplies (Schein+Patterson) | Rent | ADP tax | Summit checks* | Dentrix | Energy | Net cash |
|---|---|---|---|---|---|---|---|---|---|
| Jan | 40,288.65+38,294.49+46,841.15+46,253.22 = 171,677.51 | 88,175.55+87,372.10 = 175,547.65 | 11,649.87+4,861.53 = 16,511.40 | 21,600.00 | 49,150.50 | 14,750.00 | 1,290.00 | 2,155.90 | −109,327.94 |
| Feb | 42,443.36+40,436.65+40,908.47+40,230.66 = 164,019.14 | 86,583.69+88,791.51 = 175,375.20 | 11,420.96+4,506.86 = 15,927.82 | 21,600.00 | 48,347.72 | 14,750.00 | 1,290.00 | 2,393.44 | −115,665.04 |
| Mar | 44,742.74+42,615.77+45,646.24+40,540.07 = 173,544.82 | 86,791.65+88,999.42 = 175,791.07 | 10,975.27+4,166.27 = 15,141.54 | 21,600.00 | 48,838.34 | 14,750.00 | 1,290.00 | 2,316.49 | −106,182.62 |
| **Q1** | **509,241.47** | **526,713.92** | **47,580.76** | **64,800.00** | **146,336.56** | **44,250.00** | **3,870.00** | **6,865.83** | **−331,175.60** |

\* Summit Supply LLC held in a separate flagged category, not "supplies" — see the Patel communication. Q1: 6×4,900 + 3×4,950 = 44,250.00, tied to invoices SS-100…SS-108. Header cross-check: 212,440.18 + 509,241.47 − 840,417.07 = (118,735.42) ✔.

## Client responses received 2026-10-25

Office staff confirmed, in substance: (1) Dr. Harlow set up the Summit vendor himself and instructed "just pay those when they come in"; no delivery from Summit was ever seen; (2) no one has met T. Nguyen — the role is described solely by Dr. Harlow ("regional projects," work from home) and the checks are mailed to a P.O. box. These statements corroborate both reported matters and are documented in **Supplement No. 1** of `communication_to_dr_r_patel.md` (with a recommendation to secure a signed statement promptly and preserve the instruction emails). For everything else the client has **no additional information**.

## Open items and flagged unknowns (deliberately not forced to close)

1. **Payroll difference:** ADP PAYROLL debits 526,713.92 vs register gross 393,456.90 → difference **133,257.02**; client holds no ADP invoices, so composition is **unknown** — left unreconciled (Committee can pull ADP statements directly).
2. **Summit Supply LLC (44,250.00):** policy violations + red flags + direct-instruction and no-delivery testimony reported to the Finance Committee Chair per engagement letter §4; awaiting Committee direction. Substance of vendor relationship (Summit ↔ Kevin Marsh ↔ Harlow) not established beyond the file.
3. **T. Nguyen (E-22), Q1 gross 17,100.00:** all library ghost-employee indicators present or corroborated; identity behind the PO Box, onboarding documents, and funding path (ADP lines vs separate checks) **unknown**; classification of any correction pending Committee/forensic findings.
4. **Assumptions stated in `q1_close.json`:** cash basis; revenue = merchant deposits only; ADP TAX shown in `other`; operating account 0441 assumed complete (unconfirmed) — see `QUESTIONS.md`.
5. **Account overdrawn** at 3/31: (118,735.42) — flagged to the Committee.

Citations used: only `library/INDEX.md` items (`ssars_responsibilities.md` = AR-C §70, §90.A paraphrase; `fraud_indicators_reference.md` = ACFE summary; `tx_dental_fee_splitting.md` = Tex. Occ. Code §251.003, 22 TAC §108.70). No external legal authority was relied on; none was available.
