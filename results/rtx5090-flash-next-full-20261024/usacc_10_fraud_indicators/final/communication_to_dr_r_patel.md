# Written report of irregular transactions — Q1 2026 close

**To:** Dr. R. Patel, Chair, Partnership Finance Committee, Harlow Dental Group PLLC
**From:** Bookkeeping & monthly close service (per Engagement Letter, effective January 1, 2026)
**Date:** Prepared with the Q1 2026 close (Jan–Mar 2026)
**Re:** Transactions in Q1 2026 that appear unusual, unsupported, or inconsistent with the Client's written policies

---

## Why this is addressed to you, not to the Managing Partner

Engagement Letter ¶4: if a matter **involves or may involve the Managing Partner (Dr. K. Harlow)**, we report to the Chair of the Partnership Finance Committee and will not discuss it with the Managing Partner until the Committee directs otherwise. Items 1 and 2 below were created or directed by Dr. Harlow himself; Items 3 and 4 concern the payroll funding and account balance of a practice whose managing partner is he. Because the matters involve or may involve the Managing Partner, this report is directed solely to you. **We have not discussed these matters with Dr. Harlow.** This document is our written record of the communication.

Under our engagement we provide no assurance and our procedures are not designed to detect fraud (Engagement Letter ¶5). Consistent with AR-C §70 and AR-C §90.A (paraphrased) *(library/ssars_responsibilities.md)*, we are not making any legal determination that fraud has occurred; we are bringing these items to the appropriate level of governance because we became aware of information indicating possible irregularity, and we must not be associated with information we have reason to believe is materially false *(library/ssars_responsibilities.md)*.

---

## Item 1 — Summit Supply LLC: payments with multiple disbursement-fraud indicators

**Facts from the Client's own files** (bank statement, `vendor_master.csv`, `summit_supply_invoices.csv`, `approval_policy.md`, `hr_emergency_contact_forms_excerpt.txt`, forwarded email signature):

- Vendor V-017, Summit Supply LLC, 4471 Ridgeway Ct, Plano TX 75093 — **created in the vendor master by Dr. K. Harlow on 2025-07-02**; no W-9 on file; PO requirement "exempted by KH" (the written policy provides no exemption mechanism); payment method: check.
- Q1 2026: nine invoices, SS-100 through SS-108, each **$4,900 or $4,950 — just under the $5,000 threshold** at which the Client's own approval policy requires two-partner approval and a purchase order. All nine were approved **solely by K. Harlow**. None has a PO or a receiving document.
- Descriptions are vague and inconsistent month to month: "Consulting — practice optimization," "Supplies — misc," "Equipment maintenance," "Consulting."
- Invoices fall on a fixed cadence (the 4th, 14th, 22nd of each month) with sequential numbers, and every invoice was paid by check within days (checks on 01/06, 01/16, 01/24, 02/06, 02/16, 02/24, 03/06, 03/16, 03/24): **9 checks = 6 × $4,900.00 + 3 × $4,950.00 = $44,250.00**; each month's three checks are $4,900.00 + $4,950.00 + $4,900.00 = $14,750.00.
- The vendor's email signature identifies the contact as **"Kevin Marsh"** at the **same address, 4471 Ridgeway Ct, Plano TX 75093**. The HR emergency-contact form lists **Kevin Marsh as Dr. K. Harlow's brother-in-law at that same address**.

**Why this is sensitive.** These are the classic indicators in the ACFE reference in our library — vendor address matching an employee or relative; vendor created by the approver; no W-9 or PO; round-number invoices; vague descriptions; **amounts structured just under an approval threshold**; sequential, evenly spaced invoices *(library/fraud_indicators_reference.md)*.

**Additional context beyond internal control.** Several payments are labeled "Consulting" with no deliverables in the file, and the vendor's listed contact appears to be the Managing Partner's relative; nothing in the file indicates any dental licensure or professional credential for Summit Supply LLC. The library reference describes payments computed as a share of fees, or "consulting" with no deliverables, **to an unlicensed third party** as potentially constituting unlawful fee splitting or an unlicensed-ownership arrangement under Tex. Occ. Code §251.003 and 22 TAC §108.70 *(library/tx_dental_fee_splitting.md)* — whether the statute applies here (including whether Summit is in fact unlicensed) is a legal question for counsel; we flag the regulatory sensitivity, we do not decide it.

**Bookkeeping treatment.** We have **not** buried these checks in supplies/consulting expense. They sit in the P&L under `other.summit_supply_llc_checks_unresolved` ($14,750.00/month, $44,250.00 Q1) pending the Committee's review.

## Item 2 — Employee E-22 "T. Nguyen": payroll indicators consistent with ghost-employee risk

Facts: hired 2025-08-01 (one month after the Summit vendor record was created); "Regional coordinator," salary $2,850.00/pay period → **$17,100.00 Q1 (6 × $2,850.00)**; **0 time-clock hours** in Q1; **not enrolled in benefits**; paid by **paper check**; address on file is **PO Box 9142, Plano TX 75094** — the same city as the Summit Supply / Kevin Marsh address (the ZIPs differ, 75094 vs 75093; we note the proximity, not an exact match); **HR emergency-contact form "not on file."** The Client's approval policy requires a signed offer letter, I-9, and enrollment in the time-clock system for payroll additions; the register shows **0 time-clock hours** for E-22 in Q1, and no offer letter or I-9 appears in the file.

**The $17,100.00 is register-based and not bank-evidenced.** The bank statement provided contains **no check payable to T. Nguyen** — all nine checks on it are payable to Summit Supply LLC — so we cannot verify in this account that Nguyen was paid at all. The payees or the paying account (if different) are unknown.

These align with the ACFE ghost-employee indicators: no time records, no benefits, paper check / P.O. Box *(library/fraud_indicators_reference.md)*. The file does not show who approved Nguyen's addition to payroll; that is one of our open questions below.

## Item 3 — Payroll does not reconcile to the bank (left open, not forced)

- Payroll register (7 employees; the register shows gross **per pay period** but does not state the number of periods — we assume **6**, matching the 6 ADP PAYROLL and 6 ADP TAX debits): gross $65,576.15/period × 6 = **$393,456.90** for Q1.
- Bank ACH DEBIT ADP PAYROLL (net-pay funding): 88,175.55 + 87,372.10 + 86,583.69 + 88,791.51 + 86,791.65 + 88,999.42 = **$526,713.92** (134% of register gross).
- The bank debits exceed the register's **gross** by **$133,257.02**. Net pay cannot exceed gross, so if the register is complete these debits cannot be its net pay — arithmetically impossible. Either the register provided to us is incomplete or ADP is paying people not on it. ADP TAX debits ($146,336.56) equal 37.2% of register gross, which is also inconsistent with the register.
- We have **not** forced this to reconcile. Please provide the complete ADP quarterly registers/summaries (see QUESTIONS.md).

## Item 4 — Liquidity

The account first went negative on 02/28/2026; it recovered to positive briefly on 03/12 ($31,874.17), turned negative again on 03/15 and on every day after, and closed Q1 **overdrawn at ($118,735.42)** (beginning 212,440.18 + credits 509,241.47 − debits 840,417.07 = −118,735.42). Q1 outflows exceed deposits every month. No overdraft or NSF fee appears on the statement despite the negative balances — noted for the Committee, not explained by us. The Committee may want to be aware regardless of the items above.

---

## What we recommend the Committee consider

1. Take custody of the Summit Supply question: obtain W-9, contracts, and any deliverables for the "consulting" invoices; copy of the signed checks; who physically signed/delivered them.
2. Obtain T. Nguyen's offer letter, I-9, time-clock records, and the identity of the person who authorized the hire; consider suspending the paper-check payments pending that review.
3. Obtain complete ADP registers for Q1 to resolve Item 3.
4. Consider independent legal advice (including on Tex. Occ. Code §251.003 / 22 TAC §108.70 questions) and an independent forensic review — outside the scope of this engagement.
5. Until the Committee directs otherwise, per Engagement Letter ¶4 we will continue not to discuss these matters with Dr. Harlow.

We have performed the Q1 close (see `q1_close.json`); the classifications above reflect the engagement letter's reporting requirements, not a conclusion that any law was broken.

---

## Addendum — Client responses received during close (documented per AR-C §90.A (paraphrased), library/ssars_responsibilities.md)

We asked the Client operational staff follow-up questions. Responses, as given (speaker: "Carla"; title not stated in the file, not assumed):

1. **Summit Supply LLC:** "Dr. Harlow set that vendor up himself and said to just pay those when they come in. I've never seen a delivery from them. I'd rather not get in the middle of it."
2. **T. Nguyen:** "I've never met T. Nguyen. Dr. Harlow said they work from home on 'regional projects'. The checks get mailed to a P.O. box."
3. For all other open questions (complete ADP registers, W-9/contracts/deliverables for Summit, check-signature details, second-partner acknowledgment, Nguyen's offer letter/I-9/time-clock, rent leases, other accounts, overdraft funding), **the Client has no additional information.**

What these responses corroborate (observations, not conclusions):

- Both flagged areas trace to a **single partner, Dr. K. Harlow**: he created the vendor record and directed staff to pay the invoices without documentation. For Nguyen, the file does **not** record who authorized the payroll addition (see Item 2), but Dr. Harlow is the only person apparently in contact with Nguyen. Staff report **no receipt of goods or services from Summit** and have **never met the employee**. This matches the ACFE patterns cited above — "created by the approver," "hired by one person without HR documentation," "paper checks or P.O. box" *(library/fraud_indicators_reference.md)*; the absence of receiving records is a client-file fact, not one of the cited library indicators.
- No independent verification of Nguyen's existence or work exists in the file; the reported P.O. Box mailing of checks is consistent with the register's "paper check / PO Box 9142, Plano" detail — but note that **no checks payable to Nguyen appear on the bank statement provided** (Item 2), so payment of Nguyen is not verified in this account.
- Staff indicate they will not provide further documentation; obtaining the missing items (W-9, offer letter, I-9, ADP registers, check images) is now solely a Committee action.

**Unverified facts we explicitly do NOT assert:** that any Summit payment is a personal benefit to Dr. Harlow or Marsh; that Kevin Marsh owns/operates Summit (email signature and address match only); that T. Nguyen is a fictitious person or the same person as Marsh (P.O. Box 9142 ZIP 75094 vs. Summit/Marsh ZIP 75093 — proximity only); the cause of the $133,257.02 payroll gap; whether any law was violated. These remain open for the Committee.

Per Engagement Letter ¶4 we still have not discussed these matters with Dr. Harlow, and staff report that **he** instructs payment directly — the Committee may wish to state, in writing, that staff route flagged disbursements to you rather than paying on a single partner's verbal instruction. Our bookkeeping treatment is unchanged: Summit checks remain `other.summit_supply_llc_checks_unresolved` ($44,250.00 Q1) and we will not reclassify them to supplies/consulting while unsupported; the payroll gap remains open.
