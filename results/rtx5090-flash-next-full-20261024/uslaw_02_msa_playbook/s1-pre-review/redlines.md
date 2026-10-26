# RouteWise MSA v7.3 — Redlines for hard-rule violations

Replacement text for each playbook hard-rule break (A1–A5). Struck text is the current provision; the replacement is drafted to slot into RouteWise's numbering so it can be sent straight back to their counsel. Ranking rationale is in `issues.json`.

---

## 1. A1 — IP indemnity must escape the liability cap (§9.1/§9.3/§10.1)

**Problem.** §10.1 calls the indemnity "uncapped," but §9.1 caps all liability "NOTWITHSTANDING ANYTHING TO THE CONTRARY," and §9.3's carve-outs omit Section 10. Under the interpretive rule in the library (Restatement (Second) of Contracts §203; Delaware cases on "notwithstanding anything to the contrary," `library/contract_interpretation_notwithstanding.md`), the cap controls unless **the cap clause itself** carves the obligation out. The fix therefore must be made in Section 9, not in §10.1 alone.

**Current §9.3:**
> 9.3 The exclusions and limitations in this Section 9 shall not apply to a party's liability for its gross negligence, willful misconduct, or fraud, or to Customer's payment obligations.

**Replace §9.3 with:**
> 9.3 The exclusions and limitations in this Section 9, including the cap in Section 9.1 and the exclusion in Section 9.2, shall not apply to: (a) a party's liability for its gross negligence, willful misconduct, or fraud; (b) Customer's payment obligations under Section 4; or (c) Provider's indemnification obligations under Section 10.1.

**Replace the opening of §10.1 with (belt-and-suspenders):**
> 10.1 Notwithstanding Section 9 (including Section 9.1), Provider shall defend Customer against any third-party claim alleging that the Services infringe a patent, copyright or trademark or misappropriate a trade secret, and shall pay all damages, costs and attorneys' fees finally awarded or agreed in settlement; Provider's obligations under this Section 10.1 are not subject to any limitation or exclusion of liability in this Agreement, and this Section 10 survives termination or expiration of this Agreement.

*(§9.1's mutual 12-month cap and §9.3's gross-negligence/willful-misconduct/fraud carve-outs are playbook-compliant under B1 and are deliberately left in place.)*

---

## 2. A2 — DPA executed at signing, not "to be attached" (§5.3 / Exhibit C)

**Problem.** Playbook A2: DPA must be executed at signing whenever EU/UK personal data is processed; "to be attached" is not acceptable. GC confirms EU driver data will run through the platform. Under GDPR Art. 28(3) (`library/gdpr_art28.md`), absent a compliant contract the **controller** (Cobalt) is in breach from the first day of processing.

**Current §5.3:**
> 5.3 To the extent Provider processes personal data subject to the GDPR or UK GDPR on Customer's behalf, the parties shall enter into a data processing addendum in the form to be attached as Exhibit C.

**Replace §5.3 with:**
> 5.3 The parties execute concurrently with this Agreement the Data Processing Addendum attached as Exhibit C (the "DPA"), which is incorporated into this Agreement by reference and acknowledged as executed as of the Effective Date. The DPA governs all processing by Provider of personal data subject to the GDPR or UK GDPR on Customer's behalf and shall stipulate each element required by Article 28(3) of Regulation (EU) 2016/679, including that Provider: (a) processes such data only on Customer's documented instructions; (b) ensures personnel confidentiality; (c) implements the security measures described in Article 32; (d) respects the sub-processor authorization and flow-down conditions; (e) assists Customer with data-subject requests; (f) assists Customer with security incidents and impact assessments; (g) deletes or returns all such data at Customer's election on termination; and (h) makes available all information necessary to demonstrate compliance and permits audits. Provider shall not process any such personal data until the DPA is in effect.

**Replace Exhibit C placeholder "[To be attached.]" with:**
> EXHIBIT C — DATA PROCESSING ADDENDUM
> [DPA in the form attached hereto, executed by the parties as of the Effective Date.]

**Open item (flagged in STATUS.md):** Cobalt's standard DPA form must be produced and physically attached before signature; no DPA template exists in the workspace, so the substantive DPA text itself is outside this redline package.

---

## 3. A3 — No unilateral increases in the initial term; renewal cap at lesser of 5% or CPI (Exhibit A ¶4)

**Problem.** Playbook A3. Current Order Form allows one increase **during** the 36-month initial term and renewal increases by the **greater** of 8% or CPI-U on 60 days' notice. Under §14.1 the Order Form controls its subject matter (playbook C1), so this must be fixed in the Order Form.

**Current Order Form No. 1, ¶4:**
> 4. Pricing adjustments. Provider may increase the fees for any renewal term, and once during the Initial Subscription Term upon sixty (60) days' notice, by up to the greater of 8% or the change in the CPI-U.

**Replace with:**
> 4. Pricing adjustments. Fees are fixed for the Initial Subscription Term and shall not be increased. For any renewal term, Provider may increase the fees upon at least ninety (90) days' prior written notice, by no more than the lesser of (a) five percent (5%) and (b) the percentage change in the CPI-U (All Items, U.S. City Average, All Consumer Expenditure), measured for the twelve (12) calendar months immediately preceding the start of the renewal term; if the CPI-U has decreased or the increase is otherwise unused for a renewal term, it does not carry forward to later terms.

---

## 4. A4 — Renewal terms ≤12 months, ≤30 days' notice (§3.3)

**Problem.** Playbook A4. Current §3.3 auto-renews in 24-month terms on 90 days' notice.

**Current §3.3:**
> 3.3 Each Subscription Term shall automatically renew for successive renewal terms of twenty-four (24) months unless either party gives written notice of non-renewal at least ninety (90) days before the end of the then-current term.

**Replace §3.3 with:**
> 3.3 Each Subscription Term shall automatically renew for successive renewal terms of twelve (12) months each, or, at Customer's election exercised at or before the start of any renewal term, for successive renewal terms of one (1) month each, unless either party gives written notice of non-renewal at least thirty (30) days before the end of the then-current term.

---

## 5. A5 — Affiliates covered at no additional fee (§2.2)

**Problem.** Playbook A5 names Cobalt Freight Europe B.V. and Cobalt Brokerage LLC as required covered affiliates; §2.2 excludes all affiliates unless named on an Order Form at additional fees, and Order Form No. 1 names none.

**Current §2.2:**
> 2.2 The license granted hereunder is to Customer only and does not extend to Customer's Affiliates unless named on an Order Form at additional fees.

**Replace §2.2 with:**
> 2.2 The license granted hereunder extends to Customer and Customer's Affiliates, including without limitation Cobalt Freight Europe B.V. and Cobalt Brokerage LLC, at no additional fee. All use by Customer's Affiliates counts against Customer's quantity and usage allocations under the applicable Order Form, and Customer is responsible for its Affiliates' compliance with this Agreement. The Parties confirm that Order Form No. 1 covers use by the affiliates named above within its stated vehicle allocation, and no additional Order Form fee applies to such use.

*(Playbook's alternative — Holdings signing on behalf of the affiliates — is acceptable under A5 but more cumbersome for an EU affiliate; the license-extension text above implements the playbook's primary fix.)*
