# Redlines — RouteWise MSA v7.3 (for Cobalt Logistics)

Replacement clause text for every hard-rule break (playbook A1–A5), plus the preferred (B5) fix and one conformity note (§5.4).
Strikethrough = RouteWise draft; **bold** = Cobalt replacement/rejects language.

---

## R1. §5.3 / Exhibit C — Data Processing Addendum not executed (hard break of A2)

**Current §5.3:**
> ~~To the extent Provider processes personal data subject to the GDPR or UK GDPR on Customer's behalf, the parties shall enter into a data processing addendum in the form to be attached as Exhibit C.~~ (Exhibit C reads "[To be attached.]")

**Replacement §5.3:**
> "Provider shall process personal data subject to the GDPR or UK GDPR on Customer's behalf solely under the Data Processing Addendum attached hereto as **Exhibit C and executed by both parties concurrently with this Agreement**, which is incorporated into and forms part of this Agreement for all purposes. **Neither party shall permit or perform any processing of such personal data before Exhibit C has been executed.**"

**Exhibit C rider (to replace "[To be attached.]"):**
> "Exhibit C shall be a complete DPA, executed at signing, setting out: the subject-matter, duration, nature and purpose of the processing; the type of personal data and categories of data subjects; and stipulating that the processor (a) processes only on documented instructions; (b) ensures confidentiality; (c) takes security measures; (d) respects sub-processor conditions; (e)–(f) assists the controller; (g) deletes or returns data at the end of service; and (h) makes available information and allows audits."
> — content per library/`gdpr_art28.md` (Regulation (EU) 2016/679, Art. 28(3)). Authority basis: absent such a contract, the controller is in breach of Art. 28 from the first day of processing (library/`gdpr_art28.md`).

---

## R2. §9.1 + §9.3 — Liability cap swallows the uncapped IP indemnity (hard break of A1; drafting note C2)

**Current §9.1:**
> ~~NOTWITHSTANDING ANYTHING TO THE CONTRARY IN THIS AGREEMENT, IN NO EVENT SHALL EITHER PARTY'S AGGREGATE LIABILITY ARISING OUT OF OR RELATED TO THIS AGREEMENT EXCEED THE FEES PAID OR PAYABLE BY CUSTOMER IN THE TWELVE (12) MONTHS PRECEDING THE EVENT GIVING RISE TO THE CLAIM.~~

**Replacement §9.1 (append the exception):**
> "SECTION 9.1 AND SECTION 9.2 SHALL NOT APPLY TO PROVIDER'S INDEMNITY OBLIGATIONS UNDER SECTION 10.1 (INTELLECTUAL PROPERTY INDEMNITY), TO A PARTY'S LIABILITY FOR ITS GROSS NEGLIGENCE, WILLFUL MISCONDUCT, OR FRAUD, OR TO CUSTOMER'S PAYMENT OBLIGATIONS."

**Current §9.3:**
> ~~The exclusions and limitations in this Section 9 shall not apply to a party's liability for its gross negligence, willful misconduct, or fraud, or to Customer's payment obligations.~~

**Replacement §9.3:**
> "The exclusions and limitations in this Section 9 shall not apply to **(a) Provider's obligations under Section 10.1 (intellectual property indemnity)**, (b) a party's liability for its gross negligence, willful misconduct, or fraud, or **(c)** Customer's payment obligations."

**Note for the GC / opposing counsel:** the §9.3 change is **additive only**. The existing gross-negligence / willful-misconduct / fraud and payment-obligation carve-outs are Cobalt's own preferred position (playbook B1) and are carried through **unchanged**; they are accepted, not flagged as an issue (see "Positions accepted" table below). Item (a) is new — it is the A1 carve-back so the §9.1 cap cannot swallow the IP indemnity.

**Why the carve-out must be written into Section 9 itself:** per library/`contract_interpretation_notwithstanding.md` (Restatement (Second) of Contracts §203; Delaware cases on 'notwithstanding anything to the contrary'), a 'notwithstanding anything to the contrary' clause overrides conflicting provisions — including a more specific 'uncapped' statement elsewhere — unless the cap clause itself carves the obligation out. As drafted, §10.1's 'uncapped' statement is ineffective and Provider's IP indemnity is capped at 12 months' fees = $222,000 ($18,500 × 12) at current pricing. The redline places the carve-out inside the cap clause so the §9.1 'notwithstanding' can no longer reach it. §12.3 survival already includes Section 10 — no survival change needed.

---

## R3. Exhibit A (Order Form No. 1) §4 — unilateral mid-term price increase; wrong cap formula; 60-day notice (hard break of A3)

**Current:**
> ~~4. Pricing adjustments. Provider may increase the fees for any renewal term, and once during the Initial Subscription Term upon sixty (60) days' notice, by up to the greater of 8% or the change in the CPI-U.~~

**Replacement:**
> "4. Pricing adjustments. **Fees during the Initial Subscription Term shall not increase.** Provider may increase fees for a renewal term only upon at least **ninety (90) days'** prior written notice, and only by up to the **lower of (a) five percent (5%) or (b) the percentage increase in the CPI-U over the immediately preceding twelve (12)-month period**. Any increase exceeding that amount will not take effect and fees will remain at the then-current level."

**Arithmetic (per playbook A3 vs. draft):**
- Draft floor: 8% of $18,500/mo = **$1,480/mo** = **$17,760/yr** (assumes CPI-U change < 8%; if higher, the draft's 'greater of' formula is worse still).
- Playbook maximum: 5% = **$925/mo** = **$11,100/yr**.
- Excess: **$6,660/yr**.
- Mid-term single increase, worst case (effective near the start of the 36-month Initial Term; 60 days' notice): up to ~3 years × $17,760 ≈ **$53,280**. Prohibited outright by A3 under the redline.
- Precedence: §14.1 gives an Order Form control over the MSA on its subject matter, so the fix must sit in Exhibit A §4 (playbook note C1).

---

## R4. §3.3 — 24-month auto-renewals / 90-day notice (hard break of A4)

**Current:**
> ~~Each Subscription Term shall automatically renew for successive renewal terms of twenty-four (24) months unless either party gives written notice of non-renewal at least ninety (90) days before the end of the then-current term.~~

**Replacement §3.3:**
> "Each Subscription Term shall automatically renew for successive renewal terms of **twelve (12) months** unless either party gives written notice of non-renewal **at least thirty (30) days** before the end of the then-current term."

**Arithmetic:**
- Missed notice window under draft: 24 months × $18,500 = **$444,000** locked in (no increase assumed).
- Playbook terms: 12 months × $18,500 = **$222,000** per cycle.
- Draft renewal at the current 8% floor (if Exhibit A §4 were left as-is): 24 × $19,980 = **$479,520**, vs. playbook-style renewal 12 × $19,425 = **$233,100**.

---

## R5. §2.2 — Affiliates not covered without additional fees (hard break of A5)

**Current:**
> ~~The license granted hereunder is to Customer only and does not extend to Customer's Affiliates unless named on an Order Form at additional fees.~~

**Replacement §2.2 (route (a) — recommended):**
> "The license granted hereunder extends to **Customer's Affiliates, including Cobalt Freight Europe B.V. and Cobalt Brokerage LLC, as designated in Exhibit A (Order Form No. 1), at no additional fee**. Customer shall remain responsible for its Affiliates' compliance with this Agreement."

**Alternatively (route (b) — also permissible under A5):**
- Add to Exhibit A: "Named Affiliates (no additional fee): Cobalt Freight Europe B.V.; Cobalt Brokerage LLC." **and/or**
- Recital/signature block: "Cobalt Logistics Holdings LLC signs this Agreement **on behalf of itself and its Affiliates so designated in Exhibit A**."

Either route satisfies A5; route (a) is the cleaner paper.

---

## R6. Exhibit B — add chronic-failure termination right (preferred position, B5 — not a hard break)

**Addition to Exhibit B (after the credits paragraph):**
> "If the Services fail to meet the availability target in **three (3) calendar months within any rolling six (6)-month period**, Customer may terminate the affected Order Form upon **thirty (30) days' written notice** and receive a **pro-rata refund of prepaid, unused fees**."

Playbook B5 accepts credits-as-sole-remedy **only** with this chronic-failure exit; the draft lacks it, so the addition restores the condition. For context: 99.5% monthly target on a 30-day month = 43,200 min × 0.5% = 216 min (3.6 h) of permitted downtime monthly, plus up to 8 h/month excluded scheduled maintenance; max credits = 25% of monthly fees = $4,625/mo.

---

## R7. §5.4 — tie usage-data right to the DPA (note-level)

**Current:**
> ~~Provider may use aggregated, de-identified usage data for any purpose.~~

**Replacement §5.4:**
> "Provider may use aggregated, de-identified usage data **for its internal product purposes, provided such data is derived from Customer Data in accordance with the DPA (including processing only on documented instructions) and does not identify or re-identify any data subject**. Provider shall not sell Customer Data or publish it in identifiable form."

Instruction-basis: Regulation (EU) 2016/679, Art. 28(3)(a) as excerpted in library/`gdpr_art28.md`.

---

## Positions accepted — no redline (flagging these would over-deliver against the playbook)

| Clause | Position | Playbook basis |
|---|---|---|
| §9.1 12-month cap | Mutual 12–24 months' fees cap is acceptable as-is (the A1 problem is only that the cap is not carved out for the IP indemnity — see R2) | B1 |
| §9.3 GN/willful-misconduct/fraud carve-outs | Accept as offered — they cut both ways and protect Cobalt | B1 |
| §12.2 30-day export window | 30 days acceptable | B2 |
| §13.1–13.3 Delaware law, Wilmington venue, jury waiver | Acceptable | B3 |
| §8.1 15-day suspension notice for non-payment | 15 days acceptable because the notice period functions as the cure window (pay within 15 days, no suspension) | B4 |
| Exhibit B 99.5% target with credits | Acceptable, subject to R6 (chronic-failure exit) | B5 |

Also checked and rejected as non-applicable: warranty-disclaimer objections under U.C.C. Article 2 — the MSA is a hosted-services (SaaS) contract, and per library/`ucc_2_distractor.md` (U.C.C. §2-102), Article 2 governs goods and does not apply directly to hosted software subscriptions (§7.3's disclaimer is not an Article 2 issue on these facts).
