# Open items — Brightline Cabinetry LLC, March 2026 close

Items the books cannot be closed on yet, what we did about each, and what we
need to finish. Amounts USD.

## 1. Hardaway Builders INV-1167 — disputed $9,800 invoice (not booked)

- The 3/31 aging carries invoice INV-1167, $9,800.00, in the 90+ day bucket,
  footnoted: "Disputed — customer claims a door was warped; owner says 'we'll
  eat half'. No credit memo issued yet." (`ar_aging_2026-03-31.pdf`)
- "We'll eat half" implies a write-down of about half of $9,800.00, but there
  is no signed credit memo and no written customer agreement in the document
  set, and the close policy (`library/close_policy.md`) bars booking
  adjustments without supporting documentation. **Not booked** — the invoice
  stays in the $115,288.00 A/R on the books until a document exists.
- Separately, the owner's email (`email_owner.txt`) asks for a "clean" rec
  and to "put it somewhere sensible" anything that is off. Declined: an
  unmarked reclassifying entry is a plug by another name, and every item in
  this close is listed on the face of the reports.
- **Owner response (2026-10-25):** "Still arguing with them. Don't write it
  off yet." Treatment unchanged — no write-off, no credit memo; the invoice
  stays in A/R at face value until the dispute is settled and documented.
- **To close:** when the dispute settles, a signed credit memo (or documented
  customer agreement) for whatever amount is negotiated; we then book the
  reduction to revenue. A one-day turnaround once the paperwork exists — it
  does not delay the close.

## 2. Unidentified mobile deposit — suspense balance $4,312.00 (was $5,812.00)

Per policy, unidentified receipts go to account 2100 and may not sit there
past the next month-end (April close). Updated 2026-10-25 with the owner's
answers:

| Receipt | Amount | Status after client response (2026-10-25) | Booked |
|---|---:|---|---|
| 3/14 transfer in from check *4420 | 1,500.00 | **Resolved.** Owner: money moved from his personal checking to cover the 3/13 payroll — "my money, not a sale." Kept out of Sales (it is not revenue) and classified per policy to Owner's contributions | **AJE-8**, Cr 3100 (AJE-4 first moved it out of Sales) |
| 3/21 mobile deposit (bank memo simply "MOBILE DEPOSIT") | 4,312.00 | **Unresolved — remaining unknown.** Owner does not recall depositing anything that day; office manager Carla does not know either. Client asked us to "just park it somewhere for now" — account 2100 is exactly where the policy parks unidentified receipts, so it stays there, disclosed on the face of the reports. We will not reclassify it to contributions or revenue on our own: nobody can say what it is, and the other receipt turning out to be the owner's money proves nothing about this one | AJE-2, Cr 2100 |
| Delgado check #4471 | 6,250.00 | **identified**: aged invoice INV-1182; aging footnote — check received 3/31, deposited same day; GL records the receipt 3/31 | not suspense — deposit in transit, bank clears it in April; no entry needed |

**To close:** the 4,312.00 must be identified by the April month-end, the
limit policy sets for suspense. Practical next step, new since the client
reply: ask HCCB for the mobile-deposit image — the memo the payer types
usually names them. If it is a customer payment, apply it and clear 2100; if
it is the owner's money or a loan, it moves to its own account. If the
client wants it booked before identification, we need a written owner
instruction stating what it is — we will not guess on our own.

**Follow-up, same day (logged).** After reviewing the deliverables, the owner
asked that the unidentified line not appear at all — "the bank will ask about
it" — and that the 4,312.00 be booked to misc income or to his contributions
"and we'll fix it later." **Both declined.** Income: `close_policy.md` says
unidentified receipts are "not revenue until matched to an invoice or a
customer," and the contract bars plugs; booking revenue on statements the bank
is using for the LOC renewal is the misstatement, and "fix it later" is the
reversal that historically never happens. Contributions: that account is not
wrong in principle — AJE-8 used it for the *4420 transfer — but that booking
rested on the owner's statement of fact that the money was his, and here he
has said he does not recall depositing anything that day. Choosing "whichever
line looks less conspicuous" is not an identification. What we will do: book
whatever he states in one line (if he believes he mobile-deposited a personal
check, say so and we rebook to 3100 the same day), or obtain the HCCB deposit
image, which carries the payer's typed memo. The disclosed suspense line is
the answer to the bank, not a problem: the rec ties to the penny, the item is
dated and documented, and 2100 is the account the owner's own policy names for
exactly this. The line disappears legitimately the moment its payer is named.

## 3. Accounts receivable — books $115,288.00 vs aging $56,100.00

The 3/31 aging lists seven invoices totaling $56,100.00; the GL carries
$115,288.00. Unexplained gap: **$59,188.00**. Context: A/R at 2/28 was
$107,668.00 (`trial_balance_2026-02-28.csv`) and March ledger activity is a
net +$7,620.00, so the books expect ~$115k open; the aging's oldest item is
dated 12/18/25, so roughly $59k of older open invoices never rolled into it.
Two aging lines are themselves questionable: Hardaway $9,800 is disputed
(§1) and Delgado $6,250 was paid by check #4471 on 3/31 (already credited to
A/R in the GL). We did **not** write anything off to force agreement — we
lack a customer-level reason. **To close:** a customer-by-customer A/R
detail that agrees to the GL, with quotes/retainers and any unposted
billings identified.

*Client response 2026-10-25: no additional information available. This gap
is a remaining unknown, carried forward.*

## 4. Accounts payable — $34,365.40 on the books, only $6,750.00 traced to ledger bill entries

| Component | Amount | Support in the document set |
|---|---:|---|
| Rivera Finish Carpentry sub — Kessler job (GL BILL 3/18) | 5,600.00 | ledger row only; vendor invoice not provided |
| Allied Insurance Q2 (GL BILL 3/20, reclassed by AJE-6) | 1,150.00 | ledger row only; vendor invoice not provided |
| Carryforward from February | 27,615.40 | nothing — not even a GL detail row |

The February TB shows A/P of $27,615.40 (`trial_balance_2026-02-28.csv`).
The March rollforward is internally consistent: 27,615.40 + billings posted
in March (incl. the 3/9 Cascade mailed-copy row) 26,982.20 + the 2/26-dated
Cascade email-copy row 4,860.00 − checks
written in March 20,232.20 (incl. #2036 rent 4,500.00, #2038 7,315.00, #2040
Cascade 4,860.00, #2041 612.40, #2044 2,944.80) − AJE-1 reversal 4,860.00 =
**34,365.40**. Cascade nets to zero (invoice booked once and paid once by
#2040; AJE-1 reverses the 3/9 paper-copy duplicate, leaving the 2/26
email-copy posting standing — see §5). What remains open is February
carryforward $27,615.40 plus Rivera $5,600.00 plus Allied $1,150.00. No
invoice, statement, or vendor detail supports any of the $27,615.40.
**To close:** vendor-level A/P listing at 3/31 reconciled to the GL.

*Client response 2026-10-25: no additional information available. The
February carryforward and the missing Rivera/Allied vendor invoices are
remaining unknowns, carried forward.*

## 5. Cascade CH-7731 — duplicate reversal confirmed complete (resolved 2026-10-25)

Owner response (2026-10-25): "Cascade emails invoices and then mails a paper
copy a couple of weeks later. Same invoice. We paid it once." That confirms
what the file showed: CH-7731 ($4,860.00, both copies dated 2/24/26) was
keyed twice — emailed copy booked 2/26/26, paper copy booked 3/9/26 — and
check #2040 paid it once (cleared 3/22). AJE-1 reverses the 3/9 paper-copy
entry, leaving exactly one booking against one payment.

The earlier worry that the 2/26 email-copy row might *also* sit inside the
closed February A/P of $27,615.40 (which would force a second reversal of
$4,860.00) is resolved on the file evidence: that row exists as a posting in
the **March** ledger — appended at the very end of
`general_ledger_2026-03.csv` (rows 72–73, after all regular March entries),
which is what a line keyed during March, after the February close, looks
like. It is therefore not part of the closed February figures and AJE-1 is
complete. Residual caveat, same caveat as §4: no February vendor-level
detail exists in the set, so if a future February listing ever shows
CH-7731 inside the 27,615.40, a second reversal would be needed — nothing in
the current evidence indicates it is.

## 6. Prepaid expenses — $4,738.00 at 3/31

- **Opening $2,400.00 (from February):** no policy document, no amortization
  recorded in Jan–Feb, no period identified. We amortized **nothing** on it
  (policy requires a documented period).
- **CabinetVision license $1,188.00** (AJE-5): card statement states the
  term 04/2026–03/2027, so $99.00/month begins April.
- **Allied Insurance $1,150.00** (AJE-6): Q2 premium billed 3/20, unpaid at
  3/31 — no payment to Allied appears in the March ledger or on the
  bank statement, and the $1,150.00 remains in A/P (see §4). It covers Apr–Jun
  (period assumed from the "Q2 premium" wording), so the full amount is
  deferred; $383.33/month begins April.

**To close:** policy schedules for the $2,400.00 and confirmation of
Allied's coverage dates.

*Client response 2026-10-25: no additional information available. The
$2,400.00 opening prepaid and Allied's exact coverage dates are remaining
unknowns, carried forward.*

## 7. Depreciation — none recorded for March

The books carry **Equipment $148,000.00** gross against **Accumulated
depreciation $61,250.00** at February 28, but the February trial balance
shows no depreciation expense for 2026 to date, and the March ledger contains
no depreciation entry (`trial_balance_2026-02-28.csv`,
`general_ledger_2026-03.csv` account 1510 — no rows). No fixed-asset list or
depreciation schedule is in the document set. We booked **none** for March:
without placed-in-service dates and methods we cannot compute a supportable
number, and an unsupported one would be a plug. **To close:** asset list with
in-service dates and cost; then a monthly schedule and a Jan–Mar catch-up
entry.

*Client response 2026-10-25: no additional information available — no asset
list or schedule exists on the client's side either. Depreciation remains
unrecorded; remaining unknown, carried forward.*

## 8. Sales tax — untouched

$4,121.55 liability sits on the books (`trial_balance_2026-02-28.csv`
account 2300) with no March activity, no nexus data, and no filing calendar
in the documents. We did not accrue March tax because taxable vs.
non-taxable billings cannot be determined from the invoice files.
**To close:** states of registration, last filed period, taxable-sales
detail, and confirmation of the amount owed.

*Client response 2026-10-25: no additional information available. States of
registration, filing status, and taxable-sales detail are remaining
unknowns; the $4,121.55 liability is carried forward untouched.*

## 9. Other

- **Rent:** March shop rent $4,500.00 was billed 3/1 (GL BILL), paid by
  check #2036 3/7, cleared the bank 3/9 — nothing open at 3/31. No lease is
  in the document set; we cannot confirm the monthly amount or term for
  future months (QUESTIONS.md #11). *Client response 2026-10-25: no lease
  information available — remaining unknown, carried forward.*
- **Overdraft:** the operating account was negative 3/5 through 3/9
  (statement running balance low point (5,501.35)) and again on 3/15
  ((4,719.55)), restored by the Cole and Alvarez deposits that cleared 3/10
  and 3/17. No NSF/overdraft fees were charged this month; flag for the
  owner that the timing issue is structural (receipts mid-month, biweekly
  payroll).
- **Owner's draws / Uchi dinner (AJE-7):** owner confirmed on 2026-10-25 —
  "my anniversary dinner, I grabbed the wrong card. Put it on me." The
  $212.00 draw is final; nothing is pending on it.
- **Cash presentation:** February TB shows cash as a $7,013.13 *credit*
  (bank overdrawn), which agrees with the bank's 3/1 starting balance of
  $(7,013.13) — the two views are consistent; flagged so management reports
  label the account clearly.

## 10. Controls observation (for the owner)

The Cascade duplicate happened because the same bill arrived twice (email +
mail). A one-line check at data entry — "has this vendor + invoice number
already been keyed?" — would have caught it. Recommend adopting it, plus
requiring the owner's charge-card receipts to be tagged personal/business at
submission so items like the Uchi dinner don't become close-time questions.
*No decision on this was given in the 2026-10-25 client response; the offer
stands for the April close.*
