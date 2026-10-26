# March 2026 MOR workpaper — draft, not ready for signature

The JSON uses `null` where the supplied records cannot support a numeric balance. No missing amount has been treated as zero. The MOR requires all estate-account cash activity, separate pre-petition liabilities and post-petition payables, professional-fee status, and answers to the payment questions; it is signed under penalty of perjury. [UST Form 11-MOR instructions](../../library/ust_mor_instructions.md)

## Part 1 — cash

- Receipts: $1,212,400 customer collections + $600,000 March 12 DIP draw + $450,000 March 26 DIP draw = **$2,262,400**. The collections were on pre-petition receivables; their use is authorized by Dkt. 22 according to the activity summary.
- Disbursements: $412,000 payroll + $19,570 post-petition vendor invoices ($2,120 Grainger + $9,800 Apex + $7,650 Front Range) + $31,200 pre-petition Apex invoice + $28,000 utilities deposit = **$490,770**.
- Net cash increase from listed activity: $2,262,400 − $490,770 = **$1,771,630**. Ending cash = March 10 opening estate cash after the sweep + $1,771,630, assuming no omitted activity. The swept balance and complete account reconciliation were not provided, so `ending_cash` is `null`. The sweep between estate accounts is an internal transfer, not an additional receipt, if both accounts belong to the estate.
- The $412,000 is listed as both gross payroll and a disbursement in the activity summary. The MOR uses it as the stated cash disbursement; the payroll register and actual bank debit are unavailable.
- Estimated UST quarterly fee accrual: 0.8% × $490,770 = **$3,926.16**. It is an accrual, not a March cash disbursement, on the records provided.

## Part 2 — liabilities

- Identified pre-petition vendor invoices still apparently unpaid: $62,400 Mesa + $7,400 Front Range + $4,310 Grainger = **$74,110**. Apex's $31,200 pre-petition invoice was paid. This is an identified invoice subtotal, not the total liabilities subject to compromise. The full claims and pre-petition liability ledger was not supplied. The pre-/post-petition split of the $412,000 straddling payroll was not supplied, though the activity states the full amount was paid under Dkt. 9 within the per-employee cap. [11 U.S.C. §507(a)(4)](../../library/bc_507a4_wages.md)
- Identified post-petition invoices without a listed March payment: $18,900 Mesa + $140,000 Holland & Pierce + $45,000 Corbin = **$203,900**. If all remain unpaid and the estimated UST fee is accrued and unpaid, the identified amount is $203,900 + $3,926.16 = **$207,826.16**. Neither an AP aging nor a complete accrued-liabilities ledger was supplied. Professional invoices also require fee approval before payment. [11 U.S.C. §§330(a), 331](../../library/bc_330_331.md)
- The DIP draws total **$1,050,000** of post-petition borrowing; the provided JSON field is for payables, and no complete Part 2 debt schedule or repayments were supplied. It must be reported in the appropriate MOR liability/debt line when the full form is prepared. [UST Form 11-MOR instructions](../../library/ust_mor_instructions.md)

## Parts 5 and 7 — orders and unresolved authorization

- No professional-fee payment appears in the supplied disbursements, so `paid` is **$0**. The invoices total $185,000, but invoices are not fee awards. No March fee application, award, or holdback record was provided; approved and holdback amounts remain `null`. The referenced interim order was entered April 14, after the March reporting period. [11 U.S.C. §§330(a), 331](../../library/bc_330_331.md)
- The answer to payments on pre-petition debt is **yes**: Apex $31,200 (Dkt. 48) and a not quantified pre-petition portion of the March 13 payroll (Dkt. 9). Dkt. 48 required Apex to agree **in writing** to Customary Trade Terms before payment. That written agreement is not in the supplied file. Without it, authorization for the March 24 Apex transfer cannot be established; an unauthorized post-petition transfer may be avoided. Thus the outside-ordinary-course-without-approval answer is **unknown**, pending verification of that condition. [11 U.S.C. §549(a)](../../library/bc_362_363_503_549.md)

## Segregation basis and open items

The invoice dates place four invoices before March 10 and six on or after it. The file confirms a post-petition delivery for Mesa's March 18 invoice; underlying delivery or service dates for the other invoices were not supplied. Classification of those other invoices is provisional based on invoice date and the stated activity, subject to confirming when goods or services were provided. The March payments of Grainger, Apex, and Front Range match their post-petition invoice totals of $19,570. The Mesa February invoice is outside Dkt. 48; Dkt. 61 does not authorize its payment from DIP proceeds or netting against a returned-coil claim. [11 U.S.C. §§363(b)–(c), 503(b), 549(a)](../../library/bc_362_363_503_549.md)

Outstanding records: swept opening cash and complete bank activity; payroll register and petition-date wage allocation; complete pre-petition liability and post-petition AP/accrual ledgers; Apex's written trade-terms agreement and funding trace; March professional-fee applications, awards, and holdback record. Until reconciled, this draft should not be signed as a final MOR. [UST Form 11-MOR instructions](../../library/ust_mor_instructions.md)
