# Session 1 — Case Assessment
**Matter:** Juniper Health Staffing, LLC v. Pinecrest Senior Living, Inc.
**Agreement:** Staffing Services Agreement dated January 15, 2024 (with Schedule 1 and Exhibits A–C; Exhibit C = dispute resolution)
**Date:** October 25, 2026
**Status:** Pre-suit. Client instructs: $862,000 and a lawsuit. This memo states what the file supports and what it does not.

---

## 1. Bottom line, in plain words

The file supports a demand of approximately **$433,361.74** (through Oct 25, 2026, plus continuing interest), not **$862,000**. The gap is not a negotiating posture problem — roughly half of the CEO's claimed damages are barred by our own documents and by the governing authority:

| CEO's claim | Supported | Reason |
|---|---|---|
| Unpaid invoices $340,000 | **Yes, $340,000 principal** (of which $265,200 effectively conceded; $74,800 contested) | Contract §2 (pay in 30 days; 15-day dispute window); CJI 14.02 account stated |
| Conversion fees $112,000 | **Largely no — $80,000 (estimate), not $112,000** | Our own Feb 11 email waiver covers 2 of the 7 hires ("for Rosa and Tay as a one-off"); only 5 hires are claimable, and the comp base ($64,000 avg) is unverified |
| "Tortious interference" $410,000 | **No — do not plead** | Pinecrest is a party to the contract; a party cannot tortiously interfere with its own contract (library, Columbia tortious-interference). The only alternative theory (interference with Juniper's employees) is defeated by consent (Feb 11 waiver; Bell's "ha, we'll talk") and justification (corporate mandate to cut agency spend). The lost-profits figure is also excluded as consequential damages by §6 and double-counts the invoices |
| **Total** | **$433,361.74 + continuing interest** | vs. $862,000 (delta −$428,638.26) |

Also required candor: if we lose pieces in arbitration, Exhibit C.3 is a **mutual** prevailing-party fee clause — Pinecrest can seek its fees from us. See §7.

---

## 2. Forum: arbitration, not court

- Exhibit C.1 is a broad, enforceable-looking arbitration clause: AAA Commercial Rules, single arbitrator, Capital City, Columbia; it expressly covers disputes "arising out of or relating to" the agreement, including breach and **arbitrability**, and survives termination (C.5). FAA §2 makes such a written commercial provision valid; §4 permits compelling arbitration; §3 requires a stay of court proceedings on referable issues.
- The small-claims carve-out (C.6) is unavailable: it covers only **undisputed invoices under $25,000**. Our smallest invoice is $59,450.
- **If we filed in court**, Pinecrest would (i) move to compel under §4/C.1, (ii) obtain a stay under §3, and (iii) — because C.3 expressly grants fees in "any action to compel arbitration" and contractual prevailing-party clauses are enforced as written (*Zuniga*, via `library/fee_shifting_and_candor.md`) — likely recover its fees on that motion. Filing in court is therefore not just wrong; it is expensive.
- C.4 permits court-provisional relief in aid of arbitration; that is our only appropriate court filing (if ever needed, e.g., to restrain further fee-free hiring within the covenant's reach while the arbitration is pending).

**Recommendation:** file the AAA arbitration contemplated by Exhibit C; do not touch a courthouse first.

---

## 3. Claim A — Unpaid invoices ($340,000 principal)

**Facts (from `documents/open_invoices.csv` and the email export):**

| Invoice | Period | Amount | Due | Status |
|---|---|---|---|---|
| J-4411 | 2026-03 | $68,400.00 | 2026-04-30 | no dispute notice |
| J-4452 | 2026-04 | $71,250.00 | 2026-05-31 | no dispute notice |
| J-4490 | 2026-05 | $66,100.00 | 2026-06-30 | no dispute notice |
| J-4533 | 2026-06 | $74,800.00 | 2026-07-31 | dispute notice 2026-07-09 ("hours padded, auditing") |
| J-4571 | 2026-07 | $59,450.00 | 2026-08-31 | no dispute notice |
| **Total** | | **$340,000.00** | | |

**Strengths**
- Contract §2: payment within 30 days of invoice; **dispute within 15 days of receipt or the invoice is "deemed accepted."** Four of five invoices drew no dispute at all. Under the account-stated principle (CJI 14.02), an invoice retained without objection for the contractually fixed period is *prima facie evidence* of the debt; Pinecrest's own May 2 email ("We'll finish out the current requests") and continued work into July corroborate.
- All five due dates are long past; §2 gives **1% interest per month** on "late amounts" (arithmetic below).
- Pinecrest has so far produced *no audit results* for J-4533 — its "padded shifts" assertion currently has no supporting document in our file.

**Weaknesses / open questions**
- **J-4533 ($74,800):** a genuine dispute is now on the record. (a) Whether the 7/9 notice was **within 15 days of receipt** depends on when the June invoice was issued/received — not in the file. (b) Even if timely, an audit-pending dispute is a substantive dispute; the arbitrator would hear it. We cannot assert J-4533 as an *undisputed* debt — doing so would contradict our own file and would, if repeated in a pleading, become a Rule 3.3 false-statement problem (`library/fee_shifting_and_candor.md`).
- Pinecrest's "corporate mandate" narrative (May 2 email) will color everything; it is not a defense to *payment for services already rendered*, but it may frame the arbitrator's view of the relationship.

**Arithmetic — Contractual interest (1%/month, pro rata days/30, through the letter date 2026-10-25):**
- J-4411: 2026-04-30 → 2026-10-25 = 178 days = 5.933 months → $68,400 × 1% × 5.933 = **$4,058.40**
- J-4452: 2026-05-31 → 2026-10-25 = 147 days = 4.900 months → $71,250 × 1% × 4.900 = **$3,491.25**
- J-4490: 2026-06-30 → 2026-10-25 = 117 days = 3.900 months → $66,100 × 1% × 3.900 = **$2,577.90**
- J-4533: 2026-07-31 → 2026-10-25 = 86 days = 2.867 months → $74,800 × 1% × 2.867 = **$2,144.27**
- J-4571: 2026-08-31 → 2026-10-25 = 55 days = 1.833 months → $59,450 × 1% × 1.833 = **$1,089.92**
- **Total interest to date: $13,361.74** (of which $11,217.47 sits on the four clean invoices; $2,144.27 on J-4533, claimed subject to the audit). Interest continues to accrue daily.

---

## 4. Claim B — Conversion fees (hires of Juniper personnel)

**Contract §3:** Pinecrest may not hire any Juniper-introduced Personnel except upon payment of a conversion fee = **25% of the Personnel's first-year annualized compensation**; Juniper may waive the fee **in writing**. Applies during the term and for 12 months after.

**Facts (`email_export_juniper.txt`, `text_messages_bell_lindqvist.txt`, CEO emails):** seven hires, none paid:
Rosa M. (CNA, Mar) · Tay W. (CNA, Mar) · Priya S. (RN, Apr) · Luis F. (RN, May) · Keisha B. (LPN, May) · Anne O. (RN, Jun) · Victor H. (CNA, Jun).

**Do NOT claim Rosa M. and Tay W.** Juniper itself waived their fees in writing on 2026-02-11 (Bell: *"consider the fee waived for Rosa and Tay as a one-off... Just keep the RN orders coming"*). Per the waiver authority (`library/columbia_account_stated_waiver.md`), a written waiver limited by its terms does **not** extend to later hires — but it also extinguishes our claim for those two. Asserting fees for them would assert facts our own file contradicts. Bell's 7/20 email to the CEO confirms: *"I only ever waived for Rosa and Tay back in Feb."*

**Claimable: five hires.** Fee-per-hire = 25% × that hire's first-year annualized compensation.

- **Base (assumption, flagged):** the only comp figure in our file is the CEO's **average of $64,000** — not verified by offer letters or payroll. Using it: 5 × 25% × $64,000 = **5 × $16,000 = $80,000**. This is an *estimate pending per-hire data* (QUESTIONS.md #1). If actual comps are meaningfully higher (Schedule 1 annualized bill rates as an upper bracket: 3 RN × $191,360 + 1 LPN × $141,440 + 1 CNA × $91,520 = $807,040 → 25% = $201,760 — presented only as a sensitivity band, **not** a claim, since the fee base is what Pinecrest pays the hire, not what Juniper bills), the demand would rise.
- **Strengths:** the covenant is in force; Pinecrest knew of it (it asked *"same deal as before?"* and *"I know there's a fee thing"*); Bell's written waiver was expressly limited to Rosa and Tay, so it protects them *only*. Anne O. and Victor H. are the cleanest — June hires, waiver had already been used and denied, no ambiguity anywhere in the file.
- **Weaknesses (do not sugar-coat to the CEO):** our own account manager's conduct creates implied-waiver/estoppel exposure on **Priya, Luis, and Keisha**: "Priya's starting Monday... same deal as before?" — Bell: *"ha, we'll talk"* (no follow-up, no fee collected); "two more coming over" — Bell: *"call me"* (a 6-minute call whose content is **not in the file**). Under the course-of-dealing authority (CJI 16.10; UCC §1-303 by analogy), acquiescence in later hires without objection can support implied waiver/estoppel as to *those* hires — a fact question. If an arbitrator finds implied waiver for those three, Claim B shrinks toward ≈ $32,000 (Anne + Victor, at the unverified $64k base).
- Interest on conversion fees: the contract's 1%/month sentence sits in the invoice-payment subsection and its timing for conversion fees is not defined. We claim principal and **reserve** interest on conversion fees rather than invent a start date (open item, QUESTIONS.md).

---

## 5. Claim C — "Tortious interference" ($410,000): recommend NOT to plead

Four independent reasons, each fatal by itself:

1. **Party-to-contract bar.** Pinecrest is a party to the staffing agreement; under the governing authority (`library/columbia_tortious_interference.md`), *a party to the contract cannot tortiously interfere with it* — the remedy is breach of contract, which is already Claim A/B. A motion under Rule 12(b)(6) (plausibility; documents incorporated into a complaint may be considered — `library/frcp_12b6.md`) would likewise dismiss an interference pleading that incorporates the Feb 11 email, which shows consent.
2. **Consent in our own file.** Juniper expressly invited and waived the first direct hires (Feb 11: followed by continued orders through July).
3. **No improper means / justification.** The alternative theory — interference with Juniper's relationships with its own employees through hiring them away — is actionable only if the *means are improper*; consent and legitimate business justification (§773: cutting agency spend under a corporate mandate) are **complete defenses**. Ordinary competitive hiring, with Juniper having a contract remedy (conversion fee) for exactly this conduct, is not improper.
4. **Damages are excluded and duplicative.** "Lost profits on the Pinecrest account for 12 months" ($410,000) are consequential damages — excluded for both parties by §6, which shields only unpaid fees and conversion fees from that exclusion. They also **double-count**: the same services billed in the $340,000 invoice claim would be counted again as "lost" revenue. And causation is unproven: Pinecrest says *it* decided to reduce agency use (May 2), a business decision; the file contains no estoppel or breach tied to an account loss beyond the two contract claims.

**Candor duty:** under Rule 3.1 (non-frivolous basis) and Rule 3.3 (via `library/fee_shifting_and_candor.md`), we cannot carry this claim into a demand, and certainly not into a pleading. Tell the CEO plainly: the $410,000 line item does not exist in a form we can assert. Any demand letter that quotes the $862,000 figure would embed a claim our own file destroys — and if later repeated in a complaint, it graduates from puffery to a false statement problem.

---

## 6. Damages reconciliation (show the arithmetic)

Principal:
- Undisputed invoices: 68,400 + 71,250 + 66,100 + 59,450 = **$265,200.00**
- Contested invoice J-4533: **$74,800.00** (subject to audit outcome)
- Conversion fees, 5 of 7 hires: 5 × 0.25 × 64,000 = **$80,000.00** *(assumed base — unverified)*
- Principal total: 265,200 + 74,800 + 80,000 = **$420,000.00**

Interest to 2026-10-25 at 1%/month (§2): **$13,361.74**
**Demand total: $433,361.74**, plus continuing interest.

Reconciliation to CEO's $862,000:
- $862,000 − $433,361.74 = **$428,638.26**, comprising:
  - −$410,000.00 interference line (not pleadable, §5);
  - −$32,000.00 Rosa & Tay conversion fees (waived in writing by us);
  - +$13,361.74 interest NOT in the CEO's spreadsheet (added);
  - [CORRECTION — November 6, 2026 (Session 4 review): the line originally printed here, "−$16,000.00 residual difference between the CEO's 7×16,000 = $112,000 and our 5×16,000 = $80,000," was a bookkeeping error, and the accompanying check line (−410,000 − 32,000 + 13,361.74 + 16,000) summed to −$412,638.26, not −$428,638.26. The 7 − 5 = 2 waived hires at 25% × $64,000 = $16,000 each are exactly the −$32,000 Rosa & Tay term above (2 × $16,000 = $32,000, and $112,000 − $32,000 = $80,000 exactly). No residual term exists; the correct decomposition is three terms, as checked below. The top-line delta of −$428,638.26 was always correct.]
- Check: −410,000 − 32,000 + 13,361.74 = −$428,638.26. ✔ Reconciles (three terms; corrected November 6, 2026 — Session 4 review). (The $64,000 average comp remains open; if the per-hire actuals are higher, the conversion line rises and our demand does too.)

---

## 7. Risk profile / counter-exposure

1. **Mutual fee clause.** Exhibit C.3 is reciprocal. If we win the clean claims and lose the contested pieces, fee exposure is modest; if the arbitrator finds implied waiver for three hires and upholds (part of) J-4533's dispute, Pinecrest could seek fees. Quantification deferred to session 5.
2. **Implied waiver / estoppel.** The "ha, we'll talk" / "call me" trail is our single biggest self-inflicted wound. Disclose it to the arbitrator; do not paper over it — a misstatement about it repeated in a pleading is a 3.3 problem, and our own emails are already in Pinecrest's hands.
3. **J-4533 audit.** If the audit is real and finds padding, we lose part of $74,800 + interest; that is why the demand letter treats it as open, not conceded.
4. **Term status unknown.** The §3 covenant runs through the term plus 12 months; if Pinecrest has served or is serving a 60-day termination notice (§4), we must track the tail precisely. Not in the file.
5. **No counterclaim on file from Pinecrest** beyond the audit assertion. Nothing about Pinecrest's potential fees beyond C.3 as noted.

---

## 8. What the contract requires (compliance checklist for our claims)

- **§2:** pay within 30 days of invoice ✔ overdue for all five; dispute within 15 days → four invoices deemed accepted ✘ pinecrest waives objection to four; interest 1%/month on late amounts ✔ claimed.
- **§3:** no hire without conversion fee ✔ breached as to 5 hires (7 minus the two we waived); Juniper may waive **in writing** ✔ ours (2/11) was written and expressly limited; no *other* written waiver in file.
- **§4:** one-year auto-renew; 60-day notice — status unknown (open question).
- **§6:** consequential damages barred both ways; unpaid-fee and conversion-fee liability expressly **not** limited ✔ supports Claims A/B.
- **Exhibit C:** AAA arbitration, Capital City, arbitrability to the arbitrator (C.1/C.5) — our forum; court only for provisional relief in aid of arbitration (C.4); fees to prevailing party incl. motions to compel (C.3); small-claims carve-out inapplicable to every invoice (C.6).

---

## 9. Recommended next steps for Session 1 → 2

1. Send the demand letter at `session1/demand_letter.md` (numbers as reconciled; truthful about the Rosa/Tay waiver — Pinecrest already holds that email).
2. Collect the answers in `deliverable/QUESTIONS.md` (per-hire comps; invoice-issue dates; the 6-minute call's content; audit results; termination/term status).
3. Prepare AAA demand: claims for unpaid invoices + interest (+ conversion fees once comp data arrives); do **not** plead interference; include a Rule-3.1-clean statement of what we concede (nothing beyond Rosa/Tay fees).
4. Client talking points: the recoverable core is $265,200 + interest immediately; conversion fees worth $80,000–$201,760 depending on comp evidence; J-4533 is genuinely at risk; mediation inside arbitration (AAA rules) after answers.
