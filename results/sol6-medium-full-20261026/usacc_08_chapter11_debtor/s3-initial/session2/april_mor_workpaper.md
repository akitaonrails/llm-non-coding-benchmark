# April 2026 MOR workpaper — draft, not ready for signature

The JSON uses `null` for amounts the supplied records do not establish. The MOR covers all estate accounts, requires separate post-petition payables and pre-petition liabilities subject to compromise, and is signed under penalty of perjury. [UST Form 11-MOR instructions](../../library/ust_mor_instructions.md)

## Part 1 — reported cash activity

- Receipts: $500,000 DIP draw + $980,300 collections = **$1,480,300**.
- Listed disbursements: $398,000 April 10 payroll + $398,000 April 24 payroll + $214,600 post-petition vendor payments = **$1,010,600**.
- Listed net cash increase: $1,480,300 − $1,010,600 = **$469,700**. Actual net movement may differ if professional fees or other payments or receipts were omitted. Ending cash would be April 1 opening cash + actual April net movement. Neither opening cash nor a complete April bank reconciliation is available, and March ending cash was unresolved; `ending_cash` is therefore `null`.
- No UST quarterly fee accrual for April can be determined from a confirmed total disbursement figure. The March working file supplied a 0.8% estimate, but applying it to only the listed April payments would produce **$8,084.80** (0.8% × $1,010,600), an incomplete estimate if other payments occurred. It is not booked in the JSON as a verified payable or cash disbursement.

## Parts 2, 5, and 7

- Mesa's $62,400 February invoice remains a pre-petition unsecured claim under the April trade agreement (Dkt. 83). April 30 total pre-petition liabilities cannot be stated without a claims and liability ledger. No April 30 post-petition AP aging or accrual ledger was supplied. The $500,000 April DIP draw increases post-petition borrowing, but the outstanding DIP principal and its proper full-form line require a debt rollforward. [UST Form 11-MOR instructions](../../library/ust_mor_instructions.md)
- Dkt. 77 authorizes a procedure for interim payment after statement service and an objection window; it does not itself approve the billed fees. No April fee award, actual payment, or holdback ledger was supplied. [11 U.S.C. §§330(a), 331](../../library/bc_330_331.md)
- No April payment on pre-petition debt is reported. In particular, Dkt. 83 did not settle Mesa's February claim. Whether *any* such payment occurred, or whether any outside-ordinary-course payment lacked approval, cannot be answered yes or no from an unconfirmed partial activity summary. Both Part 7 answers are `unknown` pending a complete disbursement listing. [UST Form 11-MOR instructions](../../library/ust_mor_instructions.md)

The outstanding records are April opening and closing bank balances, a complete cash activity and payments register, April 30 AP and claims ledgers, fee applications and awards, actual professional payments and holdback entries, and detailed March time and expense records for both professionals. Until reconciled, this draft should not be signed as a final MOR. [UST Form 11-MOR instructions](../../library/ust_mor_instructions.md)
