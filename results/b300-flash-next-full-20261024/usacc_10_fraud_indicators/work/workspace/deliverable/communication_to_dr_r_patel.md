# CONFIDENTIAL — Report of unusual transactions

**To:** Dr. R. Patel DDS, Chair, Partnership Finance Committee, Harlow Dental Group PLLC
**From:** Bookkeeping and monthly close preparer (Q1 2026 engagement)
**Date:** 2026-10-25
**Re:** Q1 2026 close — disbursements requiring Committee attention

**Why this letter goes to you and not to the Managing Partner.** Section 4 of the engagement letter requires that irregularities involving or that may involve the Managing Partner be reported in writing to the Chair of the Partnership Finance Committee, and not discussed with the Managing Partner until the Committee directs otherwise. The matters below involve payments authorized by Dr. K. Harlow (Managing Partner) and a vendor linked to Dr. Harlow's family, so this report is addressed to you alone. Please do not distribute it to the Managing Partner without Committee direction.

**Nature of this report.** This is a bookkeeping/preparation engagement — no audit or review, no assurance, and we make no legal determination of fraud (AR-C §70; AR-C §90.A, paraphrased, in `library/ssars_responsibilities.md`). Per that library item, an accountant who becomes aware of information indicating fraud *should* bring it to those charged with governance excluding persons who may be involved, and should document the communication; engagement letter §4 additionally *requires* us to report irregularities of this kind to you in writing. We set out facts and indicators only; the indicators correspond to published red-flag categories (`library/fraud_indicators_reference.md`, ACFE summary).

---

## Matter 1 — Summit Supply LLC (vendor V-017): $44,250.00 paid in Q1

Nine checks cleared the operating account (Jan 6/16/24, Feb 6/16/24, Mar 6/16/24): six at $4,900.00 and three at $4,950.00. Arithmetic: 6 × 4,900 + 3 × 4,950 = 29,400 + 14,850 = **$44,250.00**; checks agree to invoices SS-100 through SS-108 in `summit_supply_invoices.csv`.

Facts from the client file, and the library red-flag categories they match (`fraud_indicators_reference.md`):

| Fact (source: client file) | Indicator matched (library) |
|---|---|
| Every invoice is $4,900 or $4,950 — just under the $5,000 two-partner/PO threshold in `approval_policy.md` | amounts structured just under an approval threshold |
| Vendor created 2025-07-02 by **Dr. K. Harlow** and every invoice approved by **K. Harlow**; PO requirement marked "exempted by KH" | created by the approver; no PO |
| **No W-9 on file**, contrary to the policy requirement of W-9 + second-partner acknowledgment before first payment | shell vendors: no W-9/PO |
| Vendor address 4471 Ridgeway Ct, Plano TX 75093 is identical to the emergency-contact address of **Kevin Marsh (brother-in-law)** on Dr. Harlow's HR form; the vendor's invoice email signature also reads "Kevin Marsh \| Summit Supply LLC \| 4471 Ridgeway Ct" | vendor address matching an employee or relative |
| Invoices at evenly spaced dates (4th, 14th, 22nd of each month), near-round amounts, vague rotating descriptions ("Consulting — practice optimization", "Supplies — misc", "Equipment maintenance"), **no PO and no receiving document on any invoice** | round-number invoices; vague descriptions; sequential/evenly spaced invoices |
| "Consulting" payments to an unlicensed third party with no deliverables in the file | Texas: may constitute unlawful fee splitting or an unlicensed-ownership arrangement (Tex. Occ. Code §251.003; 22 TAC §108.70, in `tx_dental_fee_splitting.md`) — legal characterization is for counsel, not us |

## Matter 2 — Employee E-22 "T. Nguyen", Regional coordinator: $17,100.00 Q1 gross payroll

From `payroll_register_q1.csv` and HR excerpt — indicators matched:

- **0 time-clock hours** in Q1 for a salaried "Regional coordinator" (no time records);
- **not enrolled in benefits**; hired 2025-08-01, with **no onboarding documentation in the file** (the policy in `approval_policy.md` requires a signed offer letter, I-9, and time-clock enrollment for payroll additions; staff report Dr. Harlow as the sole source for this role — Supplement No. 1 — but the file does not document who hired the employee);
- paid by **paper check** (all other employees are direct-deposit);
- address on file is a **PO Box** ("PO Box 9142, Plano TX 75094") — the same Plano ZIP-7509x area as the Summit Supply / Kevin Marsh address (75093); we note the zip-code proximity but have **not** verified who controls the PO Box;
- emergency-contact **form not on file** for this employee.

Q1 gross cost: 2,850.00 × 6 pay periods = **$17,100.00** (this amount is inside the register gross used in Matter 3; whether it actually flowed through the ADP lines is unconfirmed because the employee receives paper checks).

## Matter 3 — Open reconciliation difference (unrelated to the matters above, left open)

Bank ADP PAYROLL debits Q1 = 88,175.55 + 87,372.10 + 86,583.69 + 88,791.51 + 86,791.65 + 88,999.42 = **$526,713.92**. Payroll-register gross = 65,576.15 per period × 6 periods = **$393,456.90** (assumes each listed employee's gross is paid in each of the six ADP payroll runs — pay frequency is not stated in the register). Difference **$133,257.02** (33.9% of gross) — most plausibly employer taxes/benefit costs funded in ADP's payroll line, but no ADP billing statements were provided, so we have **not** forced this to balance. Sensitivity: if T. Nguyen's paper checks were funded outside the ADP lines, register gross falls to (65,576.15 − 2,850.00) × 6 = **$376,356.90** and the difference rises to **$150,357.02**. In `q1_close.json` ADP PAYROLL is shown as "payroll" and ADP TAX (Q1 $146,336.56) is shown separately under "other".

Also noted: the account went overdrawn during Q1 — first negative on 02/28, briefly positive on 03/12, negative every statement day from 03/15 on; ending balance **($118,735.42)** vs. beginning $212,440.18; Q1 net cash −$331,175.60. Liquidity, not fraud, but the Committee should be aware.

---

## What we did and did not do

- We recorded Summit's Q1 checks in the simplified P&L as a separate flagged category, not as "supplies", because accepting the invoice descriptions would mean knowingly associating with information we regard as unreliable (AR-C §70 / §90.A paraphrase in the library).
- We performed no procedures designed to detect fraud and express no opinion (engagement letter §5).

## Suggested next steps for the Committee (not accounting advice)

1. Engage independent counsel and a forensic accountant before confronting any individual.
2. Have someone other than the Managing Partner obtain: Summit's contract/deliverables, W-9, bank signature cards; T. Nguyen's offer letter, I-9, direct-deposit form, canceled check images; all ADP billing statements.
3. Preserve records (email, bank images, vendor master change logs).
4. Direct us in writing on whether/when the Managing Partner may be informed; until then we will not raise these matters with him, per engagement letter §4.

Prepared and documented pursuant to engagement letter §4 and the library items cited above; no other authorities were available to this engagement.

---

# Supplement No. 1 — received client information, 2026-10-25

Same distribution: **Finance Committee Chair only; not to be discussed with the Managing Partner** (engagement letter §4). The client responded to our information requests through staff member "Carla" (her role is not established from the client file, so treat her statements as a witness account to be formalized). Her statements, quoted in substance, corroborate both matters:

**On Summit Supply LLC:**
- *"Dr. Harlow set that vendor up himself and said to just pay those when they come in."* — Confirms the vendor master (`created_by: Dr. K. Harlow`) and adds that payments were made on the Managing Partner's **direct instruction**. Because each check was under $5,000, one partner could approve it under the policy; what was omitted is the **new-vendor control** (W-9 + second-partner acknowledgment before first payment, which her statement indicates did not occur) and the PO requirement marked "exempted by KH."
- *"I've never seen a delivery from them."* — Corroborates the absence of receiving documents on all nine invoices, including the three "Supplies — misc" and two "Equipment maintenance" invoices. Q1 amount at issue remains **$44,250.00** (6 × 4,900 + 3 × 4,950).

**On employee E-22, T. Nguyen:**
- *"I've never met T. Nguyen. Dr. Harlow said they work from home on 'regional projects.' The checks get mailed to a P.O. box."* — The employee is **known to no one at the office**; the only source of information about the role is the Managing Partner himself; paper checks go to a PO Box.

Mapping against the ghost-employee indicators in `library/fraud_indicators_reference.md`: **no time records** ✔ (0 hours); **no benefits** ✔; **paper checks and P.O. box** ✔ (both); **hired by one person without HR documentation** — partially met: no HR documentation exists in the file and Dr. Harlow is the sole sponsor, though the file does not name who hired the employee; **address matching another party in the file** — **not met**: PO Box 9142, Plano 75094 does not match the Summit/Marsh address (4471 Ridgeway Ct, 75093); only ZIP proximity is observed, and PO Box control is unverified. Q1 gross at issue remains **$17,100.00** (2,850.00 × 6).

**What remains unknown — the client states it has no further information:** no ADP billing statements (so the $133,257.02 payroll-line difference stays unreconciled); no contract, deliverables, or W-9 for Summit; no offer letter, I-9, or time-clock record for T. Nguyen; no confirmation that account 0441 is the only account; no direct-deposit form or identity behind the PO Box. These are flagged as open unknowns in `STATUS.md` and `QUESTIONS.md`.

**Added suggested steps (not accounting advice):**
1. Obtain Carla's **written, signed statement** promptly (vendor setup instruction; "never seen a delivery"; never met T. Nguyen) — she has expressed reluctance to be involved, so timely documentation by the Committee or counsel matters.
2. Preserve any email or messages in which Dr. Harlow instructed "just pay those when they come in."
3. Before any confrontation, have counsel confirm how to secure canceled check images and payee deposit details for the T. Nguyen checks and the nine Summit checks.

We remain bound to raise nothing of this with the Managing Partner until the Committee directs otherwise.
