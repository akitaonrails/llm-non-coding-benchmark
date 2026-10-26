# Written report of unusual / unsupported / policy-inconsistent transactions

**To:** Dr. R. Patel, DDS — Chair, Partnership Finance Committee, Harlow Dental Group PLLC
**Copy:** Partnership Finance Committee (as the body charged with governance)
**From:** Bookkeeping and monthly close service (preparation/bookkeeping engagement)
**Date:** October 25, 2026
**Re:** Q1 2026 close (Jan 1 – Mar 31, 2026) — irregularities report under paragraph 4 of the engagement letter
**Deliverable reference:** `q1_close.json`, `q1_close_worksheet.md`, `QUESTIONS.md`

---

## 1. Why this is addressed to you and not to the Managing Partner

Paragraph 4 of the engagement letter requires irregularities to be reported in writing to the Managing Partner, **but** where the matter "involves or may involve the Managing Partner," we report instead to the Chair of the Partnership Finance Committee and will not discuss it with the Managing Partner until the Committee directs otherwise.

The items in §2 and §3 below were created, approved, and authorized by **Dr. K. Harlow, DDS, Managing Partner** (vendor setup, sole invoice approval, purchase-order waiver, and a related-party address link). We therefore treat paragraph 4 as triggered: this report goes to you, we have not raised it with Dr. Harlow, and we will not do so until the Committee directs otherwise. This handling also follows the escalation rule in the reference library — report to those charged with governance, excluding persons who may be involved, and document the communication (`library/ssars_responsibilities.md`, AR-C §70; AR-C §90.A, paraphrased).

We are **not** making a legal determination that fraud has occurred, and our procedures were not designed to detect fraud (engagement letter ¶1 and ¶5; `library/ssars_responsibilities.md`). We are reporting facts and policy inconsistencies, and we have not knowingly associated ourselves with information we believe to be materially false — which is why the "consulting" payments are not quietly labeled as supplies or management fees in the close file.

## 2. Related-party vendor payments: Summit Supply LLC (vendor V-017) — $44,250.00 in Q1

Nine checks cleared this account, each matched to a numbered invoice clearing two days earlier:

| Invoice | Invoice date | Check cleared | Description | Amount | Approved by |
|---|---|---|---|---|---|
| SS-100 | 2026-01-04 | 01-06 | Consulting — practice optimization | $4,900.00 | K. Harlow |
| SS-101 | 2026-01-14 | 01-16 | Supplies — misc | $4,950.00 | K. Harlow |
| SS-102 | 2026-01-22 | 01-24 | Consulting — practice optimization | $4,900.00 | K. Harlow |
| SS-103 | 2026-02-04 | 02-06 | Equipment maintenance | $4,900.00 | K. Harlow |
| SS-104 | 2026-02-14 | 02-16 | Supplies — misc | $4,950.00 | K. Harlow |
| SS-105 | 2026-02-22 | 02-24 | Consulting | $4,900.00 | K. Harlow |
| SS-106 | 2026-03-04 | 03-06 | Consulting | $4,900.00 | K. Harlow |
| SS-107 | 2026-03-14 | 03-16 | Supplies — misc | $4,950.00 | K. Harlow |
| SS-108 | 2026-03-22 | 03-24 | Equipment maintenance | $4,900.00 | K. Harlow |
| **Total** | | | | **$44,250.00** | |

Observations against the practice's own written **Disbursement approval policy (adopted 2022)** — `documents/approval_policy.md`:

1. **Amounts sit just under the approval threshold.** The policy requires two partners plus a purchase order at **$5,000.00 and above**. Every one of the nine invoices is $4,900.00 or $4,950.00 — $100 or $50 below the threshold — and none has a purchase order.
2. **No W-9, and no second-partner acknowledgment.** `documents/vendor_master.csv` shows V-017 `w9_on_file = no`, `created_by = "Dr. K. Harlow"`, and `po_required = "no (exempted by KH)"` — the PO requirement was waived by the same partner who created the vendor and approves every invoice.
3. **Approver = creator = PO waiver.** All nine approvals are K. Harlow alone; no receiving document exists on any invoice.
4. **Address link to a Managing-Partner relative.** V-017's address is *4471 Ridgeway Ct, Plano TX 75093*. The HR emergency-contact excerpt for **K. Harlow DDS** lists **Kevin Marsh (brother-in-law)** at the **same address** (`documents/hr_emergency_contact_forms_excerpt.txt`); the same name and address appear on the forwarded invoice e-mail signature (`documents/email_signature_capture.txt`). The vendor contact and the Managing Partner's relative appear to be the same person at the same address.
5. **Pattern.** Round amounts, vague descriptions ("Supplies — misc", "Consulting"), sequential invoice numbers SS-100…SS-108, and evenly spaced invoice dates (the 4th, 14th, 22nd of every month).

These are exactly the disbursement/vendor red flags listed in the reference library — vendor address matching an employee or relative, no W-9/PO, created by the approver, round-number invoices, vague descriptions, **amounts structured just under an approval threshold**, sequential or evenly spaced invoices (`library/fraud_indicators_reference.md`).

Beyond the disbursement question, four invoices totalling **$19,600.00** ($4,900 × 4) are labeled "Consulting" / "Consulting — practice optimization" with **no engagement letter, deliverable, report, or statement of work in the file**. In a Texas dental practice, payments to an unlicensed third party computed as a share of fees, or for "consulting" with no deliverables, may constitute unlawful fee splitting or an unlicensed-ownership arrangement (`library/tx_dental_fee_splitting.md`, Tex. Occ. Code §251.003; 22 TAC §108.70). To be precise about what we do **not** know: nothing in the file tells us whether Summit Supply LLC or Kevin Marsh holds any Texas licence, and nothing shows any payment being computed as a percentage of fees — the nine amounts are flat. We raise the authority because the second limb of it, "consulting with no deliverables," matches what is in the file, not as a finding of fee splitting. **Whether the arrangement is lawful is a legal question for counsel — we do not decide it.** We raise it because it affects how the payments should be characterized and whether continued payment is appropriate.

## 3. Payroll register does not reconcile to bank payroll debits — $133,257.02 unexplained

Arithmetic (see `q1_close_worksheet.md` for the full table):

- Bank payroll debits (6 ADP runs, Jan 15 / Jan 28 / Feb 15 / Feb 28 / Mar 15 / Mar 28): **$526,713.92**
- Payroll register gross, 7 listed employees: $19,230.77 + $17,307.69 + $17,307.69 + $3,360.00 + $3,280.00 + $2,850.00 + $2,240.00 = **$65,576.15 per period** × 6 periods = **$393,456.90**
- Difference: **$526,713.92 − $393,456.90 = $133,257.02** (the register covers only **74.7%** of the bank's payroll outflow. The comparison is conservative **on the assumption**, which the ADP statements would confirm, that the `ADP PAYROLL` debits are net pay and therefore less than gross. Including the six ADP tax/deduction debits totaling $146,336.56, total cash to ADP was **$673,050.48**, i.e. **$279,593.58** more than the register's gross).
- The register's employee IDs are E-01, E-02, E-03, E-14, E-15, E-22, E-23 — only **7 rows**, and since the highest ID supplied is E-23, an unbroken numbering would mean **E-04 through E-13 and E-16 through E-21 are missing**. On that basis we believe the file we were given is an excerpt rather than the complete register (we have asked the client to confirm the numbering). We have **not** forced this to reconcile.

Ghost-employee indicators in the register itself (`library/fraud_indicators_reference.md`): **T. Nguyen (E-22)**, Regional coordinator, hired 2025-08-01 — `timeclock_hours_q1 = 0`, `benefits_enrolled = no`, `pay_method = paper check`, address `PO Box 9142, Plano TX 75094` (**Plano — the same city as Summit Supply LLC's address, 75094 vs 75093**), and the HR excerpt states the emergency-contact form is **not on file**. At $2,850.00 per period, Q1 exposure is **$2,850.00 × 6 = $17,100.00**. No paper check of that description appears in this bank account, so we could not tell whether or how this person was paid; the staff response in §6 (checks mailed to the P.O. box, employee never met by staff) indicates either an account we have not been given or register rows that do not correspond to actual payments — both remain open and are flagged as unknowns. The policy also requires a signed offer letter, I-9, and time-clock enrollment for payroll additions; none of that documentation is in the file, and the client has now stated it has no more.

## 4. Liquidity — reported because the close cannot be completed without an answer

- Beginning balance $212,440.18; total credits $509,241.47; total debits $840,417.07; ending balance **($118,735.42)**. The account first went overdrawn on **2026-02-28** ($11,577.86 − $24,130.66 = −$12,552.80).
- Monthly cash deficits: Jan $171,677.51 − $281,005.45 = **−$109,327.94**; Feb $164,019.14 − $279,684.18 = **−$115,665.04**; Mar $173,544.82 − $279,727.44 = **−$106,182.62**.
- Payroll plus payroll tax ($224,698.15 / $223,722.92 / $224,629.41) exceeds **all** cash received in every month.
- The statement contains **no** loan proceeds, transfers in, or owner contributions, yet the balance is negative — so either another account, credit facility, or line of credit exists and was not provided, or the statement set is incomplete.

## 5. What we did to the numbers

We completed the close from the bank activity and left the discrepancies open rather than plugging them (`q1_close.json`): revenue $509,241.47, payroll $526,713.92, supplies $47,580.76 (distributors only), rent $64,800.00, other $201,322.39. ADP tax ($146,336.56) is kept out of payroll because it likely mixes employee withholdings — already inside gross pay — with employer taxes, and would double-count. The Summit payments are held out of "supplies" and shown separately as related-party "consulting / maintenance" ($29,400.00) and "Supplies — misc" ($14,850.00) until the Committee tells us how they should be characterized.

## 6. Client responses received 2026-10-25 (from staff, not from the Committee)

On 2026-10-25 we received responses from a staff member identified only as "Carla" (surname not in the documents we hold; we do not assume she is the "office mgr" named in `vendor_master.csv`). For every other item, the client states it has **no additional information**. The responses are relayed statements, not verified facts:

1. **Summit Supply.** Carla states Dr. Harlow set the vendor up himself and told staff to "just pay those when they come in" — no written PO-waiver authority and no second-partner acknowledgment has been produced, consistent with `vendor_master.csv` (`created_by = "Dr. Harlow"`, `po_required = "no (exempted by KH)"`) and with our having raised the matter only to the Committee. She also states she has **never seen a delivery from Summit Supply** — so nothing observed by staff corroborates that any "Supplies — misc" invoice ($14,850.00 of the $44,250.00) represents actual goods. She said she would "rather not get in the middle of it." We note that last point for the Committee without comment: the people who process these payments are staff reporting to the partner who controls them.
2. **T. Nguyen.** Carla states she has **never met** this employee; per Carla, Dr. Harlow said the person works from home on "regional projects"; the paper checks **get mailed to the P.O. box**. This changes our §3 position in one specific way: the $2,850.00-per-period payments appear to be real disbursements, yet no such check appears in the account we were given — so they must be funded from **an account we have not been provided** (or the register rows do not correspond to actual payments). Both possibilities remain open and are flagged as unknowns; we did not net or resolve them.

We did not ask Carla anything that would substitute for Committee direction: classification (Q B4), suspension of the vendor (Q B5), instruction-source and timing questions (Q E1) are the Committee's to answer, and remain open. We have still not discussed the reported items with Dr. Harlow, per ¶4; the statements above reached us from staff without any question being posed to him by us. The Committee may wish to direct how staff communications about this matter should be handled going forward, so that nothing done by staff or by us could be read as interfering with the Committee's review — we offer no view on that beyond noting it.

## 7. What we ask of the Committee

1. Direct us in writing on the items in `QUESTIONS.md` (complete Q1 payroll register and the six ADP billing statements; Summit Supply W-9, contract, and deliverables; the T. Nguyen personnel file; the funding source for the overdraft). The client states it has **no additional information** beyond §6, so these records now have to come from third parties — ADP, the bank, the merchant processor, the landlord — or be obtained through counsel/a forensic specialist (item 3). If they cannot be obtained, tell us in writing and the related items stay open as unresolvable unknowns.
2. Tell us whether you want the **Summit Supply** vendor record deactivated and further payments suspended pending review; we will not stop or release payments on our own authority.
3. Consider whether independent counsel and a forensic/fraud specialist should be engaged. Any duty or exposure beyond the three items in our closed reference library — IRS information-return and payroll-tax obligations, theft or embezzlement statutes, bank reporting duties, Texas professional-licensure consequences — is **outside the library we are permitted to rely on, and we label it unverified** rather than citing it.
4. Confirm who we should take instructions from while this report is open, and when we may discuss these items with the Managing Partner.

Until we receive the Committee's direction, we will continue only the mechanical close work on the documents provided and will not reclassify or "true up" the items above.

*This report is documentation of the communication required by ¶4 of the engagement letter and by AR-C §90.A (paraphrased, `library/ssars_responsibilities.md`). It contains no assurance, opinion, or legal conclusion.*
