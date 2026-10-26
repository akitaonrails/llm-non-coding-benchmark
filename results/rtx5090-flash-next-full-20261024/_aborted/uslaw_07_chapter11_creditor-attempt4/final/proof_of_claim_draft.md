# DRAFT — Proof of Claim (Official Form 410 content)

> **DRAFT v2, prepared 2026-03-19 by counsel — total is ledger-supported and ready for final
> authorization (see "Reconciliation — resolved" below).** File by electronic filing with the
> claims agent (or by mail) **on or before June 11, 2026, 5:00 p.m. MT**
> (Notice of Ch. 11 Case and Bar Date, `documents/notice_of_commencement_and_bar_date.pdf`).
> **Form caveat:** Official Form 410 itself is **not in the engagement library**; item numbers and
> checkboxes below follow the familiar form — conform them to the current official form on filing.

## Caption

**United States Bankruptcy Court — District of Colorado**
*In re Redwood Fabrication, Inc.*, Case No. **26-11842-TBM**, Chapter 11
Petition filed: **March 10, 2026**

## 1. Creditor (holder of claim)

Mesa Steel Supply
Address / phone / e-mail: **[TO BE COMPLETED — not in client file]**
Whether creditor is the debtor's attorney or employee: **No**
Preferred claim (check all that apply): **☑ other priority — administrative expense under 11 U.S.C. §503(b)(9)** (see Item 4)

## 2. Debtor and case

Redwood Fabrication, Inc. — Chapter 11 — District of Colorado — Case No. 26-11842-TBM

## 3. Amount of claim as of the date of the petition (March 10, 2026)

| Category | Amount |
|---|---:|
| **3.1 Total claim** | **$125,000.00** |
| 3.2 — asserted as §503(b)(9) administrative expense (priority portion) | $78,100.00 |
| 3.3 — general unsecured (non-priority) | $46,900.00 |

Check box for §503(b)(9) priority under Item 3.1/3.2 and state separately:
the priority portion is $78,100.00 (goods received within 20 days before the petition).
Per the bar-date practice note in the library (Fed. R. Bankr. P. 3003(c)(2)-(3); 3002(c)), the
§503(b)(9) assertion should be made **separately** — by motion or by the procedure the bar-date
order specifies — in addition to being identified on this claim.
**Action item:** confirm the §503(b)(9) procedure set by the bar-date order at filing — the order
is not in the client file and the client has no further information (see remaining unknowns in
`STATUS.md`).

Arithmetic check: 41,300 (MS-7788) + 36,800 (MS-7815) = **78,100**;
25,600 (MS-7740 balance) + 6,900 (MS-7802) + 14,400 (MS-7819) = **46,900**;
78,100 + 46,900 = **125,000**. ✔

## 4. Basis of the claim

Sale and delivery of goods (steel coil, structural steel) and related freight/cutting services
to Debtor in the ordinary course of the parties' dealings. Invoices remain wholly or partly
unpaid as of the petition date.

| Invoice | Invoice date | Delivery (receipt) date | Description | Amount | Paid to date | Unpaid at petition | §503(b)(9)? |
|---|---|---|---|---:|---:|---:|---|
| MS-7740 | 2026-02-02 | 2026-02-04 | steel coil (goods) | 62,400 | 36,800 (2026-02-27, partial) | 25,600 | No — received 34 days pre-petition, outside 20-day window |
| MS-7788 | 2026-02-19 | 2026-02-20 | structural steel (goods) | 41,300 | 0 | 41,300 | **Yes** (received 18 days pre-petition) |
| MS-7802 | 2026-02-24 | 2026-02-26 | freight & handling | 6,900 | 0 | 6,900 | No — freight/handling is not "goods" (library: bc_503b9_546c.md) |
| MS-7815 | 2026-03-02 | 2026-03-04 | steel coil (goods) | 36,800 | 0 | 36,800 | **Yes** (received 6 days pre-petition) |
| MS-7819 | 2026-03-06 | 2026-03-09 | cutting services | 14,400 | 0 | 14,400 | No — services are not "goods" (library: bc_503b9_546c.md) |
| **Total unpaid at petition** | | | | **161,800** | **36,800** | **125,000** | priority: **78,100** |

(MS-7701, $48,200, was paid in full 2026-02-10 and is not part of the claim; the payment is
analyzed separately for preference exposure.)

No interest is claimed at this time (no contract interest term in the file; if the parties'
terms provide for late interest, amend Item 5 before filing).
Secured claim: **No** (no lien held by Mesa). Setoff: **Not asserted** on this claim — any setoff
of pre-petition mutual debts would require relief from the automatic stay (library: bc_502d_setoff.md).
Waiver of lien: N/A.

## 5. Reconciliation — RESOLVED (2026-03-19)

Mesa's 2026-03-12 demand letter referenced **$210,000**; the invoice ledger supports **$125,000**
unpaid at the petition. The figures reconcile arithmetically: the gross of the six ledger
invoices is

> 48,200 + 62,400 + 41,300 + 6,900 + 36,800 + 14,400 = **210,000**

i.e., the letter quoted the **gross invoiced** amount and ignored the **$85,000 already paid**
(MS-7701 paid in full 2026-02-10: $48,200; MS-7740 partial payment 2026-02-27: $36,800):

> 210,000 − 85,000 = **125,000** ✔

The claim is therefore filed at **$125,000**, fully supported by the ledger. Corollary worth
knowing: the stay-violating 3/12 letter demanded $85,000 that Redwood had **already paid** —
one more reason all AR contact with the debtor must run through counsel. If any ledger item
outside these six invoices later surfaces, amend before the bar date; nothing in the client
responses contradicts the ledger.

## 6. Supporting documents to attach (Form 410 requires documentation substantiating the claim)

1. Invoice/delivery ledger (`invoices_and_deliveries.csv`), invoices MS-7740, MS-7788, MS-7802, MS-7815, MS-7819 (with delivery receipts/bills of lading).
2. Payment history, 12 months (`payment_history_12m.csv`) showing applied payments and the 2026-02-27 partial payment.
3. Purchase orders / terms of sale (if any exist — the only terms document in the file is the 2026-01-20 terms-change e-mail; whether the parties have a master supply agreement is an open unknown, see `STATUS.md`).
4. Reclamation demand under §546(c)(1) once served (due 2026-03-30) — attach as evidence of preserved rights.

Preserve but **do not volunteer** as attachments: the 2026-01-20 terms e-mail and the client's
2026-03-19 admissions (net-15 cut, oldest-first payment condition, wire demanded as a shipping
condition). They are §547(c)(2) facts the estate will use against the ordinary-course defense;
they matter for the new-value/settlement posture, not for substantiating the claim amount.
If any invoice outside the six ledger items surfaces before June 11, 2026, file an amended
claim — nothing in the client responses indicates one exists.

## 7. Signature block (to be executed on filing)

I (we) declare under penalty of perjury that the information provided in this claim is true
and correct.
Signature: ____________________ Name/Title: [authorized signatory, Mesa Steel Supply]
Date: __________  Bar/case number of signatory if required locally: [TO BE COMPLETED]

## Internal notes (not part of the filed claim)

- Priority posture: §503(b)(9) makes the $78,100 an *administrative expense* (library); that
  administrative expenses are paid ahead of general unsecured claims is standard practice but is
  **not restated in the library** — treat as unverified and confirm against the plan's priority
  terms. The claim asserts the priority regardless; asserting it costs nothing.
- A §502(d) problem can get this **entire claim disallowed** until Mesa returns any avoidable
  preference; see `claim_analysis.json` (gross preference exposure 85,000; net estimate ~0 after
  new value) — resolve before distribution or by negotiation with the estate (library: bc_502d_setoff.md; bc_547.md).
- If Redwood schedules Mesa in Schedules of Assets and Liabilities as a non-disputed,
  non-liquidated creditor, filing may be optional in some districts, but the notice here directs
  ALL non-governmental creditors to file by 2026-06-11 — **file regardless**; late claims require
  excusable neglect (Rule 3002(c); library: frbp_3002_3003.md).
- Notice anomaly: the notice recites "Notice dated: April 2, 2026," a date **after** today
  (2026-03-19); the client cannot resolve it (no further information). We calendar the bar
  date as recited (**2026-06-11**), file well before it, and confirm the operative bar-date
  order when we pull the docket via the claims agent.
