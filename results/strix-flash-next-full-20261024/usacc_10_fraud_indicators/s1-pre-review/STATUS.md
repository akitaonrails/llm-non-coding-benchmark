# STATUS — Q1 2026 close, Harlow Dental Group PLLC

## COMPLETE WITH OPEN ITEMS

Prepared 2026-10-25 from the files in `documents/` and `library/` only; updated same day to reflect the
client response of 2026-10-25 (partial answers from staff member "Carla"; the client states it has no
additional information — the remaining unknowns are flagged below and in `QUESTIONS.md`). Cash basis, one account
(Capital City Bank operating account ending 0441). The close ties to `documents/bank_operating_q1.csv`
line by line: 48 transaction lines (12 credits + 27 ACH debits + 9 checks); statement header
212,440.18 + 509,241.47 − 840,417.07 = **−118,735.42**, equal to the 03-31-2026 ending balance shown
on the statement.

### Deliverables
| File | Status |
|---|---|
| `deliverable/q1_close.json` | Done — required shape (`months.01..03` with revenue / payroll / supplies / rent / other, plus `notes`) |
| `deliverable/communication_to_dr_r_patel.md` | Done — the communication engagement letter ¶4 requires, addressed to Dr. R. Patel, Chair, Partnership Finance Committee, **not** to the Managing Partner |
| `deliverable/QUESTIONS.md` | Done — 5 sections, 18 numbered requests (A1–A4, B1–B5, C1–C2, D1–D4, E1–E3), with 2026-10-25 response status; answered parts are not re-asked |
| `deliverable/q1_close_worksheet.md` | Done — arithmetic, tie-outs, classification decisions, authorities used |
| `deliverable/STATUS.md` | This file |

### Q1 figures as closed (cash basis, this account only)
| | Jan | Feb | Mar | Q1 |
|---|---:|---:|---:|---:|
| revenue | 171,677.51 | 164,019.14 | 173,544.82 | 509,241.47 |
| payroll (ADP payroll debits) | (175,547.65) | (175,375.20) | (175,791.07) | (526,713.92) |
| supplies (Schein + Patterson) | (16,511.40) | (15,927.82) | (15,141.54) | (47,580.76) |
| rent | (21,600.00) | (21,600.00) | (21,600.00) | (64,800.00) |
| other (itemized in the JSON) | (67,346.40) | (66,781.16) | (67,194.83) | (201,322.39) |
| **net** | **(109,327.94)** | **(115,665.04)** | **(106,182.62)** | **(331,175.60)** |

### Recipient determination (¶4)
The first half of ¶4 names the Managing Partner, but ¶4 also requires the report to go to the Chair of
the Partnership Finance Committee, and not to the Managing Partner, where the matter may involve the
Managing Partner. Nine Summit Supply LLC payments ($44,250.00) were created, approved and
PO-waived by Dr. K. Harlow, and the vendor's address is the address on Dr. K. Harlow's own
emergency-contact form for a relative. That triggers the second route, so the report is addressed to
**Dr. R. Patel, Chair, Partnership Finance Committee**; the Managing Partner has not been told. If the
Committee reads ¶4 differently, say so and the communication will be re-addressed.

### Open items (not reconciled, not plugged)
1. **Payroll gap — $133,257.02.** Bank ADP payroll debits $526,713.92 vs payroll-register gross
   $65,576.15 × 6 = $393,456.90. The register appears to be an excerpt (only 7 rows; if the IDs run
   sequentially, E-04–E-13 and E-16–E-21 are absent), and the six bank debits are nearly flat month to month ($415.87 spread, 0.24%). With
   the six ADP TAX debits ($146,336.56), total cash to ADP is $673,050.48 — $279,593.58 more than the
   register's gross. Nothing has been netted or forced. Client response (2026-10-25): **none** — the complete
   register and ADP statements were not provided and are stated as unavailable (A1/A2 still open).
2. **Summit Supply LLC — $44,250.00, nine checks, related-party indicators.** Held out of `supplies`,
   shown in `other` as consulting/maintenance $29,400.00 and "Supplies — misc" $14,850.00 pending the
   Committee's classification direction (Q B4) and a decision on whether to keep paying the vendor. All
   nine invoices are $50–$100 under the policy's $5,000 two-partner + PO threshold; no PO, no receiving
   document, no W-9, single approval by the Managing Partner. Staff response (2026-10-25): Dr. Harlow set up
   the vendor himself and verbally instructed staff to "just pay those when they come in"; the respondent has
   **never seen a delivery** from Summit (partial B1/B2/B3 — see `QUESTIONS.md`).
3. **T. Nguyen (E-22) — $17,100.00 Q1.** Zero time-clock hours, no benefits, paper check, PO Box, HR
   form not on file. No matching check appears in this account. Staff response (2026-10-25): the employee has
   **never been met** by staff; per staff, Dr. Harlow said they work from home on "regional projects"; the
   checks are **mailed to the P.O. box**. Payment therefore cannot be traced in the account provided — the
   paying account is an **UNKNOWN** (not provided, and the client states no other statements exist).
4. **ADP tax split (employee withholding vs employer tax) is unknown**, so $146,336.56 sits in `other`
   and cannot be allocated to payroll expense without the ADP billing statements and Form 941.
5. **Overdraft funding unknown.** Overdrawn from 2026-02-28 (−12,552.80) and ends −118,735.42 with no
   loan, transfer-in or owner-contribution credits in this account; payroll alone is 101%–107% of
   receipts each month. Client response (2026-10-25): **none** — funding source remains **UNKNOWN**, and the
   Nguyen check detail (open item 3) points to an operating account outside the one provided.
6. **Supporting documents missing.** No lease or vendor record for "PROPERTY MGMT RENT 3 LOCATIONS"
   ($64,800.00); no POs or invoices for Henry Schein ($34,046.10, each month over the $5,000 threshold,
   `po_required = yes`) or Patterson Dental ($13,534.66, `po_required = yes`); no W-9 for Summit.
7. **Revenue is collections, not practice revenue.** No processor statements and no deposit-to-receipt
   mapping, so merchant discount fees and any un-deposited collections are unquantified; insurance
   receipts collected after 03-31 are excluded on this cash basis.
8. **Completeness of the records themselves is unconfirmed.** One bank account was provided; payee
   detail on the ACH lines is what the statement gives, and "Dentrix" ($3,870.00) is matched to vendor
   V-003 by name only. Petty cash, cards, other accounts and Q2 activity are unknown (Q E3).
9. **Library limits.** Only `library/INDEX.md` items are cited (AR-C §70, §90.A; ACFE red flags;
   Tex. Occ. Code §251.003; 22 TAC §108.70). Any 1099/payroll-tax, embezzlement, fiduciary-duty or
   licensure consequence is labeled **unverified** and is not asserted.

10. **Document dead-end (client response 2026-10-25).** The client states it has **no additional information**:
    the complete register, ADP statements/Form 941, Summit W-9/contract/deliverables, the Nguyen personnel
    file, leases, Schein/Patterson invoices, processor statements and any other account statements were not
    provided and are stated as unavailable. Unless the Committee obtains them from third parties (ADP, the
    bank, the processor, the landlord) or through counsel/a forensic specialist, the payroll gap, the ADP tax
    split, the Nguyen payment trail, the overdraft funding and the gross-vs-net revenue question **cannot be
    closed within this engagement** and are flagged explicitly as remaining unknowns.

### Not done, by design
No audit, review, opinion, fraud-detection procedures, or legal conclusion (engagement letter ¶1, ¶5).
Nothing was forced to balance.

### What closes the items
Client answers received 2026-10-25 partially addressed A3, B1, B2 and B3 (answered parts are not re-asked in
`QUESTIONS.md`). Everything else now depends on the **Committee**, not the client: A1–A2 (payroll subledger
and ADP statements from ADP), B1–B2 (Summit W-9/contract/deliverables), A3–A4 and C1 (the account the Nguyen
checks and the overdraft are drawn on, from the bank), D1–D4 (lease from the landlord, invoices/POs from the
vendors, processor statements), and the Committee's own decisions E1–E3 plus classification/suspension
(B4–B5). If a document cannot be obtained, the Committee should say so in writing and the item stays open as
an unresolvable unknown — we will not estimate or plug it.
