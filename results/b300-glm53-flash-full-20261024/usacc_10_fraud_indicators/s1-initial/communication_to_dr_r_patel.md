# Written report of unusual, unsupported, and policy-inconsistent transactions

**Date prepared:** October 25, 2026
**To:** Dr. R. Patel DDS, Chair, Partnership Finance Committee, Harlow Dental Group PLLC
**From:** The outside accountant performing the bookkeeping and monthly close services under the engagement letter effective January 1, 2026 (Q1 2026 close)
**Re:** Q1 2026 bookkeeping and close — matters required to be reported under Section 4 (Irregularities)

Dear Dr. Patel,

Section 4 of the engagement letter requires us to report in writing to the Managing Partner any transactions that appear unusual, unsupported, or inconsistent with the Client's written policies; **if a matter involves or may involve the Managing Partner, we are to report instead to you as Chair of the Partnership Finance Committee and not discuss it with the Managing Partner until the Committee directs otherwise.** The items below involve or may involve the Managing Partner, so this report is addressed to you. We are not sending a copy to the Managing Partner and will not discuss these matters with the Managing Partner until the Committee directs otherwise.

These matters came to our attention in the ordinary course of the Q1 2026 close from documents the Client provided: the bank operating-account statement (Jan 1 – Mar 31, 2026), the vendor master, the Summit Supply invoice file, the payroll register, the HR emergency-contact file excerpt, an invoice email signature capture, and the Client's disbursement approval policy. We also state the limitations from Section 5 of the engagement letter: **our procedures are not designed to detect fraud, and we are not concluding that fraud occurred.** None of the language below is a legal determination; where a library reference is cited, we cite only the closed reference library.

---

## Item 1 — Checks to Summit Supply LLC: $44,250.00 in Q1, with multiple indicators of a potential related-party or shell vendor

**The disbursements.** Nine checks cleared the operating account in Q1, each $4,900.00 or $4,950.00:

| Bank date | Amount | Invoice | Invoice description |
|---|---|---|---|
| 01/06, 01/16, 01/24 | 4,900.00 + 4,950.00 + 4,900.00 = 14,750.00 | SS-100, SS-101, SS-102 | Consulting — practice optimization; Supplies — misc; Consulting — practice optimization |
| 02/06, 02/16, 02/24 | 4,900.00 + 4,950.00 + 4,900.00 = 14,750.00 | SS-103, SS-104, SS-105 | Equipment maintenance; Supplies — misc; Consulting |
| 03/06, 03/16, 03/24 | 4,900.00 + 4,950.00 + 4,900.00 = 14,750.00 | SS-106, SS-107, SS-108 | Consulting; Supplies — misc; Equipment maintenance |

Arithmetic: 6 checks × $4,900.00 = $29,400.00 plus 3 checks × $4,950.00 = $14,850.00 → **$44,250.00**, which agrees in total and invoice-by-invoice with the bank activity. No other Summit Supply transactions appear in Q1.

**Why this matters (facts on the file, not conclusions):**

1. **Threshold structuring.** The Client's approval policy requires invoices ≥ $5,000 to be approved by two partners and supported by a purchase order. Every Summit Supply invoice is $4,900.00 (98.0% of the threshold) or $4,950.00 (99.0% of the threshold). Nine of nine invoices fall just under the two-approval requirement.
2. **Single-person control in all three roles.** The vendor master shows Summit Supply LLC (V-017) was **created by Dr. K. Harlow on 2025-07-02**; the purchase-order requirement was recorded as **"no (exempted by KH)"**; every invoice in the file is **approved only by Dr. K. Harlow**; and payment is by check. The approver, vendor creator, and grantor of the PO exemption are one person.
3. **Vendor onboarding policy not followed on the file.** The policy requires a W-9 and a second-partner acknowledgment for new vendors. The vendor master shows **W-9 not on file** for V-017, and no second-partner acknowledgment is in the file. (The other vendors show W-9s on file.)
4. **Vendor address matches a relative of the Managing Partner.** The vendor address is 4471 Ridgeway Ct, Plano TX 75093. The HR emergency-contact file lists Dr. K. Harlow's emergency contact as **Kevin Marsh (brother-in-law), 4471 Ridgeway Ct, Plano TX 75093** — the same address. A forwarded invoice email signature reads "Kevin Marsh | Summit Supply LLC | 4471 Ridgeway Ct, Plano TX 75093."
5. **Invoice-pattern indicators.** The nine invoices are sequentially numbered SS-100 through SS-108, dated at even ~8–10-day spacing, in round recurring amounts, with vague, changing descriptions ("Consulting — practice optimization," "Consulting," "Supplies — misc," "Equipment maintenance") and **no receiving documents** for any of them. No deliverable, report, or work product accompanies any consulting invoice in the file.

**Library context.** These facts match the indicators listed in the reference library for shell-vendor schemes (`library/fraud_indicators_reference.md`: vendor address matching an employee or relative; no W-9/PO; created by the approver; vague descriptions; amounts structured just under an approval threshold; sequential or evenly spaced invoices). Separately, under `library/tx_dental_fee_splitting.md`, payments by a dental practice to an unlicensed third party for "consulting" with no deliverables may constitute unlawful fee-splitting or an unlicensed-ownership arrangement — noted as context; we make no legal determination.

## Item 2 — A second Plano-linked payee in the payroll: employee E-22 (T. Nguyen) shows multiple indicators listed in the reference library for ghost employees

From the payroll register: E-22, T. Nguyen, role "Regional coordinator," hired 2025-08-01 — approximately one month after Summit Supply LLC was created in the vendor master — is paid **$2,850.00 per pay period** by **paper check**, is **not enrolled in benefits**, and shows **0 time-clock hours** while all other hourly staff show 468–480 hours. The address on file is **P.O. Box 9142, Plano TX 75094** (same city as the Summit Supply vendor address; a different street address), yet the register's "location" field says Balcones. The HR file shows **no emergency-contact form for E-22**. The approval policy requires payroll additions to have a signed offer letter, I-9, and time-clock enrollment; none of these documents is in the file we received, and we cannot verify that they exist. `library/fraud_indicators_reference.md` lists the matching indicators: no time records, no benefits, paper checks or a P.O. box, hired without HR documentation, address matching another party in the file.

We point out that E-22's compensation is small relative to the red flags in Item 1 — we cannot confirm whether E-22 is a genuine employee; we only report that the onboarding documents required by policy are not on the file.

## Item 3 — Payroll debits do not reconcile to the payroll register: $279,593.58 unexplained in Q1

The payroll register's gross-per-period column totals $65,576.15 for the employees listed (E-01, E-02, E-03, E-14, E-15, E-22, E-23). Six pay dates occurred in Q1 (01/15, 01/28, 02/15, 02/28, 03/15, 03/28):

- Register gross × 6 periods = **$393,456.90**
- ADP PAYROLL ACH debits = **$526,713.92** ($88,175.55 + $87,372.10 + $86,583.69 + $88,791.51 + $86,791.65 + $88,999.42)
- ADP TAX ACH debits = **$146,336.56** ($24,479.29 + $24,671.21 + $24,217.06 + $24,130.66 + $24,257.41 + $24,580.93)
- Combined payroll debits = **$673,050.48**
- Difference: $673,050.48 − $393,456.90 = **$279,593.58 unexplained**

A bank statement shows gross funding, not wage detail, so part of the gap may be legitimate (additional employees not listed in the register; deferred deductions; benefit remittances). We have not been able to decompose it from the documents provided and are **leaving it open** rather than forcing it. We request ADP's payroll journals and pay registers for all six dates, and the complete employee roster. Even if the entire gap were innocent, the register provided evidently does not cover all persons paid, which by itself limits what the register can evidence.

## Item 4 — Operating-account statement ends at a negative balance of −$118,735.42

The statement is internally consistent and we verified it row by row: beginning balance $212,440.18 − total debits $840,417.07 + total credits $509,241.47 = −$118,735.42, and every running balance footed. However, the account turns negative on 02/28 (after an ADP TAX debit) and remains negative through 03/31, reaching −$118,735.42. A dental practice with $500,000+ per quarter in collections would not ordinarily allow its sole operating account to overdraw in this pattern. Possible explanations — missing deposit lines (in which case quarterly revenue is understated), an overdraft facility or line of credit, or a misstated/edited statement — cannot be distinguished with the file provided. We have not adjusted anything for this and are asking the Client to confirm the statement's completeness.

## Summary and suggested Committee next steps

| Item | Amount at issue in Q1 | Nature |
|---|---|---|
| Summit Supply LLC checks | $44,250.00 | Policy circumvention + related-party / shell-vendor indicators |
| E-22 payroll | $2,850.00/period (~$17,100.00 for 6 periods) | Missing HR documentation; ghost-employee indicators |
| Payroll reconciliation gap | $279,593.58 | Unreconciled; register appears incomplete |
| Negative ending balance | −$118,735.42 | Statement completeness / overdraft unconfirmed |

Suggested next steps (for the Committee's decisions; we take none of these unilaterally):
1. Obtain Summit Supply LLC's W-9, any contract or statement of work, deliverables for each "consulting" invoice, and the front and back images of checks for SS-100–SS-108 (endorsement and deposit trail).
2. Determine who authorized the purchase-order exemption for V-017 and restore the vendor master's approval controls (dual control over vendor creation/changes; second-partner review reaching the $5,000 threshold, including review for split invoices).
3. Obtain onboarding documents for E-22 (offer letter, I-9, time-clock enrollment) and confirm the position's duties and actual work location.
4. Request ADP payroll journals and complete pay registers for the six Q1 pay dates and reconcile the $279,593.58 gap.
5. Confirm with the bank whether the operating account has an overdraft facility and whether any transactions are missing from the Q1 statement.
6. Consider suspension (per Committee direction) of further payments to V-017 pending review — the cadence suggests approximately $14,750/month would otherwise continue in Q2.

Finally, we restate the limits of our role: this engagement is bookkeeping and a monthly close, not an audit or review; we do not express an opinion, our procedures are not designed to detect fraud, and nothing herein determines whether fraud occurred. Under the professional responsibilities summarized in our reference library (`library/ssars_responsibilities.md`), we have communicated what we became aware of to you as those charged with governance, because the appropriate recipients under Section 4 exclude the person who may be involved in these matters.

Please treat this report as confidential and direct the Committee's requests to us in writing. We will participate in any review the Committee directs and will hold this report and the underlying files confidential except as the Committee or law directs.

Respectfully submitted,

*The accountant under the engagement letter of January 1, 2026 (Q1 2026 bookkeeping and close)*
