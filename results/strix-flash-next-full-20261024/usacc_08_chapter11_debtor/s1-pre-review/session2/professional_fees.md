# Professional fees — what may be paid to each professional, and when

Status: **provisional**. The controlling limitation is statutory and settled; the *amounts* payable in April cannot
be computed because the 4/14/2026 interim compensation order text is not in the file and the client has no further
information (see `deliverable/QUESTIONS.md`). This memo does **not** fabricate an April MOR (`april_mor.json` is
blocked — no April activity data exists in `documents/`).

## The rule (all professionals)

Per `library/bc_330_331.md` (11 U.S.C. §§330(a), 331):

> Professionals employed under §327 are paid **only upon application and court award** (§330) or under **interim
> compensation procedures ordered by the court** (§331). **Payments outside those procedures are subject to
> disgorgement.**

Consequences for the books:

- An invoice from a professional is **not** a payment authorization. Accrue it in MOR Part 2 post-petition
  payables; MOR Part 5 records only what the court has **approved**, **paid**, and **held back**.
- DIP proceeds may fund court-awarded fees: Dkt. 61 ¶2 permits DIP proceeds for post-petition operating expenses,
  administrative expenses **ordered by the Court**, and the Carve-Out. An unapproved fee payment is not within ¶2
  and would be an unauthorized post-petition transfer (11 U.S.C. §549(a), library/bc_362_363_503_549.md).
- Timing mechanics of §331 (waiting periods between applications) are **not stated** in the library excerpt
  [unverified] — counsel owns the application calendar.

## Holland & Pierce LLP (debtor counsel) — invoice 3/31/2026, $140,000.00

- March: nothing granted, nothing paid → Part 5 all zero (correct as filed).
- **Interim compensation order entered 4/14/2026** per the vendor file note: "80%/100% holdback." The order text
  was requested (Q4) and is unavailable. Until the order is in hand, **pay nothing** — the payable amount is defined
  by the order, not by the invoice.
- Both defensible readings of the note, with the arithmetic ceiling each implies (ceiling = the order *could* allow
  at most this much of the $140,000 invoice; the actual award may be lower — courts commonly trim applications):
  - Reading A — *80% payable now, 20% held back*: payable ≤ 0.80 × 140,000 = **$112,000.00**; holdback ≥
    **$28,000.00** (typically held pending a final fee application).
  - Reading B — *interim award of 80% with 100% of the current-period fees held back*: payable could be as low as
    **$0.00** with **$140,000.00** held back to a later period.
- Do not split the difference: pay exactly what the order states. Before any remittance, confirm (i) the awarded
  period and amount, (ii) the holdback percentage and what it is held pending, (iii) whether payment may come from
  DIP proceeds (Dkt. 61 ¶2) and the effect on the Carve-Out (amount not provided — Q7).
- Risk if wrong: paying outside §§330/331 exposes the firm (and the payer facilitating it) to **disgorgement**
  (library/bc_330_331.md).

## Corbin Advisors (financial advisor) — invoice 3/31/2026, $45,000.00

- Vendor file note: "fee application required" — no interim order noted for Corbin.
- Nothing was granted as of 3/31/2026, so **$0.00 payable until** a fee application is filed and an order entered
  (§§330(a), 331). Accrued in Part 2; Part 5 stays zero until an award exists.

## April MOR Part 5 — what to report when the data arrives

| Field | Source needed | If Reading A holds | If Reading B holds |
|---|---|---|---|
| professional_fees_approved | 4/14 order text (amount actually awarded) | ≤ 112,000.00 | 0.00–140,000.00 per order |
| paid | April disbursement register (no April data in file) | amount the order permits | likely 0.00 |
| holdback | 4/14 order text | ≥ 28,000.00 | per order |

These are **illustrative ceilings under the two readings of the vendor-file note, not figures to file**. The April
MOR (due 5/21/2026 on the Dkt. 61 ¶4 "by the 21st" cycle) must be built from April activity data the file does not
yet contain.
