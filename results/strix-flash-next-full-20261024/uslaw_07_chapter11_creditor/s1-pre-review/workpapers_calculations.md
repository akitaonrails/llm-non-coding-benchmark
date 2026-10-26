# Workpapers — Mesa Steel Supply / Redwood Fabrication, Inc. (Case No. 26-11842-TBM, Bankr. D. Colo.)

Prepared 2026-03-19. Petition date: **2026-03-10** (documents/notice_of_commencement_and_bar_date.pdf).
All figures computed in Python from `documents/invoices_and_deliveries.csv` and `documents/payment_history_12m.csv`.
Every legal proposition below is keyed to a file in `library/INDEX.md`; anything not in the library is labelled **[unverified]**.
Client Round-1 answers (Lori – credit manager; Frank – CEO), logged 2026-03-19, are used where tagged **[client]**; verbatim quotes are in `client_answers_round1.md`. For every other open question the client has no additional information, so the remaining unknowns are flagged, not asked again.

Key dates computed from the petition date:

| Cutoff | Date | Source |
|---|---|---|
| §503(b)(9) 20-day goods window | received on/after **2026-02-18** | library/bc_503b9_546c.md |
| §546(c) 45-day goods window | received on/after **2026-01-24** | library/bc_503b9_546c.md |
| §546(c) written demand deadline | **2026-03-30** (20 days after petition, because each 45-day-after-receipt date falls after commencement) | library/bc_503b9_546c.md |
| §547(b)(4) 90-day preference window | payments on/after **2025-12-10** | library/bc_547.md |
| Proof of claim bar date | **2026-06-11, 5:00 p.m. MT** | documents/notice_of_commencement_and_bar_date.pdf |
| Critical vendor hearing (Dkt. 44) | **2026-04-02** | documents/notice_of_commencement_and_bar_date.pdf |
| Creditors' meeting (called the "Meeting of Creditors" under section 341 in the notice — factual, not a legal citation) | **2026-04-21, 10:00 a.m. MT** | documents/notice_of_commencement_and_bar_date.pdf |

---

## 1. Pre-petition claim — $125,000

MS-7701 was paid in full and drops out. Invoice amounts less payments:

| Invoice | Delivered | Description | Invoiced | Paid | Unpaid at petition | Days pre-petition | Goods? | In 20-day window? | Class |
|---|---|---|---:|---:|---:|---:|---|---|---|
| MS-7701 | 2026-01-14 | steel coil | 48,200 | 48,200 (2026-02-10) | 0 | 55 | yes | no | paid — no claim |
| MS-7740 | 2026-02-04 | steel coil | 62,400 | 36,800 (2026-02-27) | **25,600** | 34 | yes | no | general unsecured |
| MS-7788 | 2026-02-20 | structural steel | 41,300 | 0 | **41,300** | 18 | yes | yes | **§503(b)(9)** |
| MS-7802 | 2026-02-26 | freight & handling | 6,900 | 0 | **6,900** | 12 | no | (yes, but excluded) | general unsecured |
| MS-7815 | 2026-03-04 | steel coil | 36,800 | 0 | **36,800** | 6 | yes | yes | **§503(b)(9)** |
| MS-7819 | 2026-03-09 | cutting services (on-site) | 14,400 | 0 | **14,400** | 1 | no | (yes, but excluded) | general unsecured |

Arithmetic:
- Total pre-petition unpaid = 25,600 + 41,300 + 6,900 + 36,800 + 14,400 = **125,000**
- §503(b)(9) (goods received on/after 2026-02-18) = 41,300 + 36,800 = **78,100**
  - MS-7740 is goods but was received 2026-02-04 = 34 days pre-petition → outside the 20-day window.
  - MS-7802 freight & handling and MS-7819 on-site cutting services are **not** "goods" (library/bc_503b9_546c.md expressly excludes services, freight and handling).
- General unsecured = 125,000 − 78,100 = **46,900** (= 25,600 + 6,900 + 14,400) ✔ reconciles.

Reconciliation note: the 2026-03-12 dunning letter demanded **$210,000**. Total invoiced 2026-01-12 → 2026-03-09 is 48,200 + 62,400 + 41,300 + 6,900 + 36,800 + 14,400 = 210,000, but 48,200 + 36,800 = **85,000** was already paid, so the true open balance was **125,000**. The letter overstated the debt by 85,000.

## 2. §503(b)(9) administrative claim — $78,100

Statutory test applied (library/bc_503b9_546c.md): value of goods received within 20 days before commencement, sold in the ordinary course of the debtor's business. Goods: yes for MS-7788/MS-7815 (steel). Ordinary course: yes — steel coil and structural steel are the subject matter of this 12-month, roughly monthly account. Assert separately from the general unsecured claim, by motion or per the bar-date order procedure (library/frbp_3002_3003.md). The notice in the file does not state a separate 503(b)(9) filing deadline → open item, see QUESTIONS.md.

## 3. §546(c) reclamation — right available, value likely near zero

Goods received within 45 days before the petition (on/after 2026-01-24):

| Invoice | Received | Unpaid value | 45 days after receipt | Demand deadline |
|---|---|---:|---|---|
| MS-7740 | 2026-02-04 | 25,600 | 2026-03-21 (post-commencement) | **2026-03-30** |
| MS-7788 | 2026-02-20 | 41,300 | 2026-04-06 (post-commencement) | **2026-03-30** |
| MS-7815 | 2026-03-04 | 36,800 | 2026-04-18 (post-commencement) | **2026-03-30** |

Gross reclaimable goods value = 25,600 + 41,300 + 36,800 = **103,700**. All three 45-day-after-receipt dates expire after commencement, so the statute's alternative deadline controls: not later than 20 days after the filing = **2026-03-30**. No demand has been served; 11 days remain.

Why the dollar value is doubtful: reclamation is subject to prior liens, and the library records a DIP lender with a blanket lien in this case (library/bc_503b9_546c.md). Whether the steel is still identifiable (not fabricated into Redwood's product, not sold) is not in the file. Treat the demand as leverage for the critical-vendor discussion, and as an obligation of diligence, not as a recovery.

## 4. Preference exposure

### 4.1 Transfers inside the 90-day window (on/after 2025-12-10) = $180,000

| Payment | Amount | Applied to | Days after invoice | Days before petition | Method | In window? |
|---|---:|---|---:|---:|---|---|
| 2025-04-20 | 39,000 | MS-7310 | 44 | 324 | ACH | no |
| 2025-05-29 | 42,500 | MS-7355 | 46 | 285 | ACH | no |
| 2025-07-07 | 40,100 | MS-7402 | 45 | 246 | ACH | no |
| 2025-08-14 | 38,700 | MS-7451 | 43 | 208 | ACH | no |
| 2025-09-25 | 45,200 | MS-7498 | 47 | 166 | ACH | no |
| 2025-11-03 | 41,800 | MS-7560 | 44 | 127 | ACH | no |
| **2025-12-18** | **51,000** | MS-7612 | 45 | 82 | ACH | **yes** |
| **2026-01-22** | **44,000** | MS-7655 | 43 | 47 | ACH | **yes** |
| **2026-02-10** | **48,200** | MS-7701 | 29 | 28 | ACH | **yes** |
| **2026-02-27** | **36,800** | MS-7740 (partial) | 25 | 11 | **WIRE on demand** | **yes** |

51,000 + 44,000 + 48,200 + 36,800 = **180,000**.

Elements: (b)(1) transfer of the debtor's property (cash) ✔; (b)(2) antecedent trade debt ✔; (b)(3) insolvency **presumed** during the 90 days, §547(f) ✔; (b)(4) within 90 days ✔; (b)(5) a trade creditor would receive more than in a chapter 7 liquidation — likely ✔.

### 4.2 Ordinary course, §547(c)(2) — protected $95,000 / exposed $85,000

Baseline from the 12-month history: payments 43–47 days after invoice, every one by ACH, under net-45 terms.

- **Protected 95,000 = 51,000 (Dec 18, 45 days, ACH) + 44,000 (Jan 22, 43 days, ACH).** Both sit inside the parties' own pattern, and both were made before/at the point Mesa changed the terms (2026-01-20) — consistent with "ordinary course of business … of the debtor and the transferee", §547(c)(2)(A).
- **Exposed 85,000 = 48,200 (Feb 10, 29 days) + 36,800 (Feb 27, 25 days, wire on demand).** Mesa's credit department imposed **NET 15** and "oldest open invoice first" by email dated 2026-01-20 (documents/terms_change_email.txt). The Feb 10 payment was exactly the oldest open invoice, paid 14 days faster than any payment in the prior year; the Feb 27 payment was a **wire demanded by Mesa's credit manager**. The library: payments "made under **shortened terms, pressure, or unusual methods (wire on demand) compared with the parties' history** generally fall outside (c)(2)(A)" (library/bc_547.md). **Corroborated by Mesa's own witness [client]:** Lori — "In January I cut them to net-15 and made them pay the oldest invoice before I'd ship" (the Feb 10 payment) and, for the Feb 27 wire, "I told them no steel until it hit our account."
- §547(c)(2)(B) ("ordinary business terms", i.e. industry comparison) could still protect these, but there is **no industry-terms evidence in the file** and the client has none [client] → unproven; and §547(g) puts the burden of every (c) defence on Mesa.
- ~~Sensitivity: if the Feb 10 ACH is held ordinary, protected = 143,200 / exposed = 36,800.~~ **Superseded by the client statement [client]:** the same credit manager who set the NET-15 terms conditioned each new shipment on these payments, so the Feb 10 payment now reads as pressured/shortened-terms rather than ordinary; the split stands at **95,000 / 85,000**.

### 4.3 New value, §547(c)(4) — $99,400

Unsecured extensions of credit (goods/services delivered) **after** each transfer, on account of which Redwood made no otherwise unavoidable transfer. Nothing was paid to Mesa after 2026-02-27, so all post-2026-02-10 deliveries are still unpaid at the petition:

| Delivered | Invoice | Value | After which transfers? |
|---|---|---:|---|
| 2026-02-20 | MS-7788 | 41,300 | after Feb 10 |
| 2026-02-26 | MS-7802 | 6,900 | after Feb 10 |
| 2026-03-04 | MS-7815 | 36,800 | after Feb 10 and Feb 27 |
| 2026-03-09 | MS-7819 | 14,400 | after Feb 10 and Feb 27 |

Total new value after the two exposed transfers = 41,300 + 6,900 + 36,800 + 14,400 = **99,400**.
(MS-7740, delivered 2026-02-04, pre-dates the Feb 10 transfer, so its unpaid 25,600 is **not** new value for those transfers.)
New value after 2025-12-18 = 210,000 delivered, 125,000 of it unpaid at petition; after 2026-01-22 = 161,800 delivered — ample for those transfers in any event, and they are ordinary-course protected anyway.

Transfer-by-transfer, without double counting: Feb 27 transfer 36,800 is fully offset by the 51,200 delivered after 2026-02-27; the Feb 10 transfer 48,200 is offset by the remaining 99,400 − 51,200 = 48,200 of post-Feb-10 unpaid value. Aggregate surplus = 99,400 − 85,000 = 14,400.

**Caveat raised by the client's own account [client]:** Mesa conditioned each new shipment on prior payment — "I made them pay the oldest invoice before I'd ship" (the payment that produced the 2026-02-10 transfer) and "no steel until it hit our account" (the 2026-02-27 wire). On those facts a court could characterise the 48,200 and 36,800 payments as otherwise unavoidable transfers made **on account of the later new value** (they were, in substance, the price of the next truck of steel), which would erode the (c)(4) credit. The library quotes the §547(c)(4) text but says nothing about this application **[unverified]**. That risk is carried as Scenario E below; it does not change the 99,400 computation itself.

### 4.4 Net exposure scenarios (not forced to a single number)

| Scenario | Arithmetic | Exposure |
|---|---|---:|
| A — ordinary-course fails on Feb 10 + Feb 27; new value credit includes the 20-day goods | 85,000 − 99,400 → 0 | **$0** |
| B — as A, but 20-day goods that carry §503(b)(9) status cannot also count as new value (a real split in the case law, **not covered by the library → [unverified]**) | 85,000 − (99,400 − 78,100) = 85,000 − 21,300 | **$63,700** |
| C — only the wire payment is avoidable, new value fine | 36,800 − 51,200 → 0 | **$0** |
| E — as A, but the Feb 10 and Feb 27 payments are treated as otherwise unavoidable transfers made **on account of** the later new value, because Mesa itself made prior payment the price of each new shipment **[client] — doctrine not covered by the library, [unverified]** | 85,000 − 0 | **$85,000** |
| D — worst case: all defences fail | 180,000 | **$180,000** |

Headline estimate: **$0 if the new-value credit is allowed in full; recommended reserve now $85,000 (the realistic ceiling) while the Scenario E question is open**; $63,700 remains the mid-case if only the 20-day-goods overlap fails. Why it matters even so: under §502(d) the court **shall disallow** Mesa's claim until it pays any amount for which it is liable on a §547 recovery (library/bc_502d_setoff.md) — so an unresolved preference fight can freeze the whole 125,000 claim, including the 78,100 administrative piece.

## 5. Open / unreconciled items (deliberately left open)

Client Round 1 (2026-03-19) is in: Lori confirmed the terms change and the ship-only-on-payment conditions; Frank confirmed the automated dunning letter and reported two calls and an approach from Redwood's counsel. For everything else the client has **no additional information**, so the items below are flagged as unknowns, not re-asked.

1. The bar-date notice is internally inconsistent: it is **dated 2026-04-02**, i.e. 14 days in the future as of today, and it recites a critical-vendor hearing on the same date (2026-04-02). The bar date of 2026-06-11 is used as stated. The client has no copy of the operative order **[client]** — counsel must pull the order and the docket (claims agent / clerk).
2. No separate §503(b)(9) deadline appears in the notice; the library says the request is made "by motion or by the procedure the bar-date order specifies" — that order is not in the file and the client does not have it **[client]**. Plan: stand-alone §503(b)(9) motion (library/frbp_3002_3003.md permits the motion route).
3. Setoff (Form 410 Part 5) — **provisionally resolved by file re-read + Round 1.** The "you owe us" remark in the collection log was made by **Mesa's own AR clerk** (documents/dunning_after_petition.md, 2026-03-15: Redwood's AP said "we filed Chapter 11, talk to counsel"; the clerk replied "that's not our problem, you owe us"). Nothing in the file, and nothing in the client's answers, shows Redwood asserting a claim against Mesa or Mesa holding Redwood deposits or consigned goods. Form 410's offset box is answered **"No" (provisional)** — confirm with Mesa before signing that it holds no deposits/consignment/security. If setoff ever becomes live it needs stay relief (library/bc_502d_setoff.md).
4. No post-petition deliveries appear in the file (last delivery 2026-03-09) and the client has no additional information **[client]**, so none are assumed. If Mesa has shipped since 2026-03-10, those amounts are outside §503(b)(9) and the library has no authority covering payment for post-petition goods **[unverified]**.
5. No returns, credits, disputes or warranty claims are recorded and the client has none to report **[client]**; the 125,000 is computed on that assumption and must be reduced if anything surfaces.
6. **New (Round 1): the second call.** Frank: "Lori called them twice." The log records **one** call (2026-03-15). Obtain phone records; if the second call was post-petition it is an additional act to collect and belongs in the mitigation record.
7. **New (Round 1): the dunning system itself.** The 2026-03-12 final notice was auto-generated — the system "send[s] final notices to everyone who's 30 days late" **[client]**. The account is 40+ days late, so unless it is suppressed the system will fire again post-petition; audit what notices, statements or credit-bureau reports have already gone out since 2026-03-10.
8. **New (Round 1): the approach from Redwood's counsel.** Frank was asked whether Mesa would keep supplying on normal terms if the old invoices are paid; he answered "pay first", unaware of the pending critical-vendor motion (Dkt. 44, hearing 2026-04-02). The date and content of that contact are not logged — reconstruct them; the response must go lawyer-to-lawyer before the hearing (library/critical_vendor_practice.md).
9. **Exhibit G (signed delivery receipts) cannot be produced** **[client]**. The §503(b)(9) receipt dates then rest on Mesa's delivery spreadsheet (documents/invoices_and_deliveries.csv); MS-7788 sits only 2 days inside the 20-day window, so **41,300 of the 78,100 priority classification is at risk** if the 2026-02-20 receipt date is challenged.
