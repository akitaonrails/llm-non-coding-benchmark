# Q1 2026 close — worksheet (arithmetic and tie-outs)

Client: Harlow Dental Group PLLC · Period: 2026-01-01 – 2026-03-31 · Source: Capital City Bank operating account ending 0441 (`documents/bank_operating_q1.pdf` and `documents/bank_operating_q1.csv` carry the same 48 transaction lines; the PDF also carries a summary header)

Companion deliverables: `q1_close.json` (the close), `communication_to_dr_r_patel.md` (the report required by ¶4 of the engagement letter, addressed to the Chair of the Partnership Finance Committee), `QUESTIONS.md` (open requests), `STATUS.md` (status and open items). Nothing here is forced to balance.

## 1. Statement tie-out (does the statement itself foot?)

| Item | Amount |
|---|---:|
| Beginning balance 2026-01-01 (PDF summary header; also first line 190,840.18 + 21,600.00) | 212,440.18 |
| Total credits (12 merchant deposits) | 509,241.47 |
| Total debits (36 items: 27 ACH + 9 checks) | 840,417.07 |
| Computed ending: 212,440.18 + 509,241.47 − 840,417.07 | **-118,735.42** |
| Statement ending balance | **-118,735.42** |

Every running balance on the statement was recomputed from the prior line; all 48 tie. The statement is internally consistent. (Note: the account has been **overdrawn** since 2026-02-28.)

## 2. Month-by-month classification of every line

| Category | Jan | Feb | Mar | Q1 | Lines |
|---|---:|---:|---:|---:|---:|
| revenue | 171,677.51 | 164,019.14 | 173,544.82 | 509,241.47 | 12 |
| payroll (ADP payroll debits) | -175,547.65 | -175,375.20 | -175,791.07 | -526,713.92 | 6 |
| payroll tax (ADP tax) | -49,150.50 | -48,347.72 | -48,838.34 | -146,336.56 | 6 |
| rent (property mgmt) | -21,600.00 | -21,600.00 | -21,600.00 | -64,800.00 | 3 |
| supplies (Schein + Patterson) | -16,511.40 | -15,927.82 | -15,141.54 | -47,580.76 | 6 |
| Summit Supply checks | -14,750.00 | -14,750.00 | -14,750.00 | -44,250.00 | 9 |
| software (Dentrix) | -1,290.00 | -1,290.00 | -1,290.00 | -3,870.00 | 3 |
| utilities (Austin Energy) | -2,155.90 | -2,393.44 | -2,316.49 | -6,865.83 | 3 |
| **Net cash flow** | -109,327.94 | -115,665.04 | -106,182.62 | **-331,175.60** | 48 |

Check: -331,175.60 = credits 509,241.47 − debits 840,417.07 = -331,175.60. No line is left unclassified.

### 2a. Addends behind each month
- **January revenue:** 40,288.65 + 38,294.49 + 46,841.15 + 46,253.22 = **171,677.51**
  Payroll: 88,175.55 + 87,372.10 = 175,547.65 · tax: 24,479.29 + 24,671.21 = 49,150.50
  Supplies: 11,649.87 + 4,861.53 = 16,511.40 · Summit: 4,900.00 + 4,950.00 + 4,900.00 = 14,750.00 · Rent 21,600.00 · Dentrix 1,290.00 · Utilities 2,155.90
  **Outflows 281,005.45; net -109,327.94**
- **February revenue:** 42,443.36 + 40,436.65 + 40,908.47 + 40,230.66 = **164,019.14**
  Payroll: 86,583.69 + 88,791.51 = 175,375.20 · tax: 24,217.06 + 24,130.66 = 48,347.72
  Supplies: 11,420.96 + 4,506.86 = 15,927.82 · Summit: 4,900.00 + 4,950.00 + 4,900.00 = 14,750.00 · Rent 21,600.00 · Dentrix 1,290.00 · Utilities 2,393.44
  **Outflows 279,684.18; net -115,665.04**
- **March revenue:** 44,742.74 + 42,615.77 + 45,646.24 + 40,540.07 = **173,544.82**
  Payroll: 86,791.65 + 88,999.42 = 175,791.07 · tax: 24,257.41 + 24,580.93 = 48,838.34
  Supplies: 10,975.27 + 4,166.27 = 15,141.54 · Summit: 4,900.00 + 4,950.00 + 4,900.00 = 14,750.00 · Rent 21,600.00 · Dentrix 1,290.00 · Utilities 2,316.49
  **Outflows 279,727.44; net -106,182.62**

## 3. Payroll: bank debits vs. the payroll register (NOT reconciled)

| Employee | Role | Gross per period |
|---|---|---:|
| E-01 K. Harlow DDS | Managing partner | 19,230.77 |
| E-02 R. Patel DDS | Partner | 17,307.69 |
| E-03 S. Whitfield DDS | Partner | 17,307.69 |
| E-14 M. Alvarez | Hygienist | 3,360.00 |
| E-15 J. Okoro | Hygienist | 3,280.00 |
| E-22 T. Nguyen | Regional coordinator | 2,850.00 |
| E-23 L. Brandt | Front desk | 2,240.00 |
| **Gross per period (7 employees)** | | **65,576.15** |

Six ADP payroll runs: 88,175.55 (01/15) + 87,372.10 (01/28) + 86,583.69 (02/15) + 88,791.51 (02/28) + 86,791.65 (03/15) + 88,999.42 (03/28) = **526,713.92**
Register gross × 6 periods: 65,576.15 × 6 = **393,456.90**
**Gap: 526,713.92 − 393,456.90 = 133,257.02** (register covers 74.70% of bank payroll debits)
Six ADP tax debits: 24,479.29 + 24,671.21 + 24,217.06 + 24,130.66 + 24,257.41 + 24,580.93 = 146,336.56; tax ÷ payroll per run: 27.76%, 28.24%, 27.97%, 27.18%, 27.95%, 27.62%
Incl. tax: bank paid 673,050.48 vs register gross 393,456.90 → **279,593.58 unexplained**.

Gaps in the employee-ID sequence: the file supplies 7 rows, IDs E-01, E-02, E-03, E-14, E-15, E-22, E-23. Since the highest ID supplied is E-23, **if** the IDs are sequential then E-04–E-13 and E-16–E-21 (16 IDs) are absent — which is why we treat the file as an excerpt of the register rather than the register itself. Whether the numbering is sequential is a question for the client (`QUESTIONS.md` A1).
Per pay period, register gross 65,576.15 against the ADP payroll debit on the same pay date: 88,175.55 (74.37% covered), 87,372.10 (75.05% covered), 86,583.69 (75.74% covered), 88,791.51 (73.85% covered), 86,791.65 (75.56% covered), 88,999.42 (73.68% covered).
Monthly payroll debits are almost flat: 175,547.65 / 175,375.20 / 175,791.07, a spread of 415.87 (0.24% of the smallest), despite the register containing only 7 employees and no headcount data by month.
T. Nguyen (E-22): 0 time-clock hours, no benefits, paper check, PO Box address → 2,850.00 × 6 = **17,100.00** Q1 exposure; no such check appears in this account.

## 4. Summit Supply LLC: invoices vs. checks, and threshold headroom

| Invoice | Date | Amount | Description | PO | Receiving doc | Check cleared | Days to pay | Headroom under $5,000 |
|---|---|---:|---|---|---|---|---:|---:|
| SS-100 | 2026-01-04 | 4,900.00 | Consulting — practice optimization | — | — | 2026-01-06 | 2 | 100.00 |
| SS-101 | 2026-01-14 | 4,950.00 | Supplies — misc | — | — | 2026-01-16 | 2 | 50.00 |
| SS-102 | 2026-01-22 | 4,900.00 | Consulting — practice optimization | — | — | 2026-01-24 | 2 | 100.00 |
| SS-103 | 2026-02-04 | 4,900.00 | Equipment maintenance | — | — | 2026-02-06 | 2 | 100.00 |
| SS-104 | 2026-02-14 | 4,950.00 | Supplies — misc | — | — | 2026-02-16 | 2 | 50.00 |
| SS-105 | 2026-02-22 | 4,900.00 | Consulting | — | — | 2026-02-24 | 2 | 100.00 |
| SS-106 | 2026-03-04 | 4,900.00 | Consulting | — | — | 2026-03-06 | 2 | 100.00 |
| SS-107 | 2026-03-14 | 4,950.00 | Supplies — misc | — | — | 2026-03-16 | 2 | 50.00 |
| SS-108 | 2026-03-22 | 4,900.00 | Equipment maintenance | — | — | 2026-03-24 | 2 | 100.00 |
| **Total** | | **44,250.00** | | | | all 9 matched | | |

Split by description for classification purposes: consulting/maintenance = 4,900.00 + 4,900.00 + 4,900.00 + 4,900.00 + 4,900.00 + 4,900.00 = 29,400.00; 'Supplies — misc' = 4,950.00 + 4,950.00 + 4,950.00 = 14,850.00

Vendor master (V-017): w9_on_file = **no**, created_by = **Dr. K. Harlow**, po_required = **no (exempted by KH)**, address 4471 Ridgeway Ct, Plano TX 75093 = address on K. Harlow's emergency-contact form for **Kevin Marsh (brother-in-law)**.
Policy (`documents/approval_policy.md`): ≥ $5,000 → two partners + PO; new vendor → W-9 + second-partner acknowledgment before first payment.

## 5. Vendor / policy checks on the other debits

| Payee | Q1 total | Vendor master | Invoices/PO on file | Policy note |
|---|---:|---|---|---|
| Henry Schein Inc (V-001) | 34,046.10 | yes, po_required=yes | none | each month ≥ $5,000 → two partners + PO required; no approval evidence |
| Patterson Dental (V-002) | 13,534.66 | yes, po_required=yes | none | $4,861.53 / $4,506.86 / $4,166.27 — all under $5,000, so one partner may approve, but po_required=yes and no PO is on file |
| Dentrix / Henry Schein One (V-003) | 3,870.00 | yes | none | recurring software, $1,290.00 × 3 |
| Summit Supply LLC (V-017) | 44,250.00 | **W-9 no; created and approved by same partner; PO waived** | 9 invoices | see §4 |
| Austin Energy (V-009) | 6,865.83 | n/a | none | utilities |
| PROPERTY MGMT RENT 3 LOCATIONS | 64,800.00 | **no vendor record** | no lease/PO | $21,600.00 × 3 months |

## 6. Liquidity

- Jan: in 171,677.51 − out 281,005.45 = -109,327.94; running balance 103,112.24; payroll+tax 224,698.15 vs receipts 171,677.51 → payroll+tax = 130.88% of receipts
- Feb: in 164,019.14 − out 279,684.18 = -115,665.04; running balance -12,552.80; payroll+tax 223,722.92 vs receipts 164,019.14 → payroll+tax = 136.40% of receipts
- Mar: in 173,544.82 − out 279,727.44 = -106,182.62; running balance -118,735.42; payroll+tax 224,629.41 vs receipts 173,544.82 → payroll+tax = 129.44% of receipts
- No loan, transfer-in, or owner-contribution credits appear in any month; the account ends at (118,735.42).
- Payroll alone vs receipts: Jan 102.25%, Feb 106.92%, Mar 101.29% — payroll exceeds collections every month before tax, rent and everything else.

## 7. Classification decisions (so the reader can reclassify without recomputing)

| Debit group | Q1 amount | Where it sits | Why |
|---|---:|---|---|
| ADP payroll (6) | 526,713.92 | `payroll` | the bank labels these six lines `ADP PAYROLL`; they are the cash the practice sent ADP to pay people, so they are the payroll line of the close. Whether each figure is gross or net pay is **not known** without the ADP billing statements (`QUESTIONS.md` A2) |
| ADP TAX (6) | 146,336.56 | `other.payroll_taxes_adp` | the bank labels these separately, and we cannot split them between employee withholdings (already inside the register's `gross_per_period`) and employer tax (not in the register). Folding them into `payroll` would risk double-counting the withholdings; leaving them out of the file altogether would lose $146,336.56 of cash. They are therefore reported, labelled, and left unallocated |
| Summit Supply (9) | 44,250.00 | `other.summit_supply_consulting_and_maintenance` (29,400.00) + `other.summit_supply_supplies_misc` (14,850.00) | invoices are labelled 'Consulting — practice optimization', 'Equipment maintenance' and 'Supplies — misc'; one invoice number range, one vendor, so the split is kept inside one vendor rather than part-supplies / part-other. **Not** in `supplies` pending Finance Committee direction (see `QUESTIONS.md` §B). If the Committee directs supplies, `supplies` rises by 44,250.00 across the quarter: 14,750.00 per month (4,900.00 + 4,950.00 + 4,900.00) |
| Henry Schein (3) + Patterson (3) | 47,580.76 | `supplies` | dental consumables/equipment vendors per vendor master |
| PROPERTY MGMT RENT (3) | 64,800.00 | `rent` | but the descriptor says 3 locations, and no lease identifies them — see `QUESTIONS.md` §D |
| Dentrix (3) + Austin Energy (3) | 10,735.83 | `other` | software subscription, utilities. The bank payee reads 'ACH DEBIT DENTRIX SOFTWARE'; matching it to vendor V-003 'Dentrix / Henry Schein One' is an identification **by name only** — no invoice or contract in the file |

**Response log — 2026-10-25.** Client responses received after the close was computed (staff member "Carla"; see `communication_to_dr_r_patel.md` §6 and the response-status table in `QUESTIONS.md`) corroborate the §3–§4 observations — Dr. Harlow set up Summit Supply himself with a verbal "just pay those when they come in" instruction, no Summit delivery has ever been seen by staff, and staff has never met T. Nguyen (checks mailed to the P.O. box, so the paying account is not the one provided) — but **change no figure and no classification above**. Every amount in this worksheet is still taken directly from `documents/bank_operating_q1.csv`.

## 8. Authorities relied on

Only files listed in `library/INDEX.md` are cited, and no others: (`library/ssars_responsibilities.md`) AR-C §70 and AR-C §90.A — in a bookkeeping/preparation engagement the accountant provides no assurance and is not required to perform fraud-detection procedures, but must not knowingly be associated with materially false information, should bring suspected fraud or noncompliance to the appropriate level of management **or those charged with governance, excluding persons who may be involved**, and should document the communication, and does not make legal determinations of fraud; (`library/fraud_indicators_reference.md`) ACFE shell-vendor and ghost-employee red flags; (`library/tx_dental_fee_splitting.md`) Tex. Occ. Code §251.003 and 22 TAC §108.70 — payments to an unlicensed third party computed as a share of fees, or for 'consulting' with no deliverables, may be unlawful fee splitting or unlicensed ownership. **No other authority is cited anywhere in the deliverables.** Topics outside the library — IRS information-return (Form 1099) and payroll-tax obligations, theft/embezzlement statutes, Texas corporate fiduciary duty, licensure consequences, bank reporting duties — are labeled **unverified** and are not asserted. Whether the Summit Supply arrangement or the payroll gap violates any law is **not** concluded on here; ¶1 and ¶5 of the engagement letter put this engagement outside audit, review and fraud-detection work.
