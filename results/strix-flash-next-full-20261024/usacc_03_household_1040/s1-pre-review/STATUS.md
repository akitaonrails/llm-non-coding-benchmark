# STATUS: COMPLETE WITH OPEN ITEMS

The 2025 federal return is fully prepared and internally consistent: **MFJ, AGI $91,350, taxable income $59,850, federal total tax $6,408, withholding $8,730 → federal refund $2,322.** Every federal figure is computed from the file plus the seven library documents, with the arithmetic shown in `return.md` and the reasoning in `judgment_calls.md`. Nothing was forced to balance; the items below stay open on their face.

**Client responses received (October 2026): no figures changed.** Every answer confirmed a position already taken — unrelated broker-found tenant with never-raised rent (rental loss allowed), no post-2021 contributions or loans and Pike guarantees the bank line (basis $11,500 locked), employee-convenience remote work at both jobs (wages 100% NY source), Form 8332 signed for Leo (CTC $2,200), employer plan from July 1 (8962 covered months = 6). The questions those answers closed are recorded in `QUESTIONS.md`; for everything else the client has no additional information, and those points are flagged as stated assumptions below.

## Bottom line

| Item | Amount |
|---|---:|
| Total income (W-2s 122,000 + interest 400) | $122,400 |
| Allowed pass-through losses (S-corp 11,500 + rental 19,550) | ($31,050) |
| **AGI** | **$91,350** |
| Standard deduction (MFJ) | ($31,500) |
| **Taxable income** | **$59,850** |
| Tax (Tax Table, MFJ 59,850–59,900) | $6,708 |
| Form 8962 excess APTC repayment (capped) | $1,900 |
| Child tax credit (Sofia only) | ($2,200) |
| **Total tax** | **$6,408** |
| Federal withholding | ($8,730) |
| **Federal refund** | **$2,322** |

Suspended/carryforward: S-corp loss $16,500 (basis); rental loss $1,468 (§469).

## Open items

1. **NY tax due / IT-203 refund — NOT COMPUTED (unavailable from the library).** The NY part-year *framework* and sourcing rules are in the library and have been applied: resident period 1/1–6/30/2025 (181 days, assumed — item 4), both spouses' wages 100% NY-source for the full year under convenience-of-the-employer (now client-confirmed), Brooklyn rental is NY-source realty. But the library excerpt contains **no NY rate schedule, deduction, or subtraction modifications**, so `ny_tax_est`/`ny_refund_est` are left null in `return.json` rather than estimated from outside sources. NY withholding of $6,752 (3,842 + 2,910) is fully creditable on IT-203; a refund is directionally likely but unquantified here. Related gap: the NY-source treatment of the S-corp passthrough loss is indeterminate from the library excerpt (the K-1 carries no NY allocation data).
2. **Brooklyn lease document not in the file (documentation risk only — judgment call 5).** The underlying facts are now **client-confirmed**: the tenant is a stranger (a nurse found through a broker in 2019) and the rent was simply never raised, so the library's carve-out applies and the $19,550 allowance stands on client testimony. If the position were nevertheless lost, AGI → $110,900 and TI → $79,400, which is **outside the library's tax-table excerpt**, so that variant cannot even be finished with the library. A copy of the 2019 lease would convert testimony into documentation.
3. **Form 8962 household size (client has no additional information).** Used 4 — the 1095-A lists four covered individuals and Leo lives primarily with Elena; the FPL $31,200 (family of 4) is the only figure the library supplies. A 3-person household would raise the repayment cap from $1,900 to $3,150, but the family-of-3 FPL is not in the library, so that variant is not computable with verifiable sources. Stated assumption, flagged.
4. **NY residency end date (client has no additional information).** Used 6/30/2025 (181 resident days) — the library gives no rule for fixing the date. Alternative 7/3 (closing/move-in) = 184 days; impact limited to day-counted items only. Stated assumption, flagged.
5. **Completeness of information (client has no additional information).** Assumed none exist: no 1099-DIV/1099-INT/brokerage or retirement forms beyond the file, no 2025 estimated payments or prior-year overpayment applied, no IRA/HSA, child-care, student-loan, or Tampa property-tax items, no prior-year depreciation schedule or placed-in-service documentation for the condo, and no condo 1098 (interest $11,900 taken from the client summary). None of these change the figures above if confirmed, but they are unverified inputs.
6. **S-corp reasonable compensation (Q10 remainder).** Whether the $68,000 S-corp W-2 is reasonable for Marcus's services is unverified. It changes no figure on this return; flagged for the file.

Closed by the client's answers (previously open here): Leo/Form 8332 (signed for 2025 — CTC locked at $2,200), 8962 covered months (Jan–Jun confirmed), convenience-of-the-employer necessity facts (confirmed for both spouses), below-market rent *facts* (confirmed — only the lease document remains, item 2), and Marcus's contribution/loan history (matches the basis note; $11,500 basis and $16,500 suspension locked).

## Deliverables

- `return.json` — figures, contract schema (federal + NY fields; NY set `not-computed`; client-confirmation block included)
- `return.md` — every figure with its arithmetic and library citation, plus a "not in the library" section
- `judgment_calls.md` — 19 calls with rejected alternatives and dollar impacts
- `QUESTIONS.md` — Q&A log: 6 closed by client answers, 6 remaining flagged assumptions/gaps
- `STATUS.md` — this file

Citations are limited to `workspace/library/` (see `library/INDEX.md`); everything else is labeled unverified or assumed. No outside sources were used.
