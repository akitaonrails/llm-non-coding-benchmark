# RouteWise MSA v7.3 — Redlines for hard-rule violations

Cobalt Logistics — Vendor Contract Playbook (rev. 2026-03), rules A1–A5. Replacement text is
drop-in; deletions/strike-overs are noted where an existing clause is replaced.

**Verification note.** The only legal authorities cited here are the items in `library/INDEX.md`
(`gdpr_art28.md`, `contract_interpretation_notwithstanding.md`). The UCC excerpt in the library
covers sales of goods and does not apply to this SaaS agreement, so it is not relied on. Statements
of negotiation practice are judgment, not law. See STATUS.md.

**Client confirmations (2026-10-25), incorporated below:** both named affiliates will use the
Services (Europe → Rotterdam/Hamburg ops; Brokerage → carrier routing) and Holdings signs in its
own name; EU data in scope = driver names, locations, working hours, and customer addresses.
Remaining unknowns are flagged in §2 and STATUS.md (controller entity, EU go-live
date, RouteWise's standard DPA form, fleet size vs. the 350-vehicle cap).

---

## 1. Cap must not swallow the IP indemnity — breaks A1 (§9.1, §9.3, §10.1)

**Problem.** §10.1 calls Provider's IP indemnity "uncapped," but §9.1 caps all aggregate liability
at 12 months' fees "NOTWITHSTANDING ANYTHING TO THE CONTRARY IN THIS AGREEMENT," and §9.3's
carve-outs do not include §10.1. Per the library (Restatement (2d) §203; Delaware cases on
"notwithstanding anything to the contrary," `contract_interpretation_notwithstanding.md`), the cap
controls over the conflicting "uncapped" statement **unless the cap clause itself carves the
obligation out**. Delaware law governs (§13.1). So the fix must sit inside Section 9 — amending
only §10.1 would not work.

**§9.1 — replace (new text in caps only at the changed lead-in):**

> 9.1 NOTWITHSTANDING ANYTHING TO THE CONTRARY IN THIS AGREEMENT, AND EXCEPT AS PROVIDED IN
> SECTION 9.3, IN NO EVENT SHALL EITHER PARTY'S AGGREGATE LIABILITY ARISING OUT OF OR RELATED TO
> THIS AGREEMENT EXCEED THE FEES PAID OR PAYABLE BY CUSTOMER IN THE TWELVE (12) MONTHS PRECEDING
> THE EVENT GIVING RISE TO THE CLAIM.

**§9.3 — replace:**

> 9.3 The exclusions and limitations in this Section 9 shall not apply to: (a) a party's liability
> for its gross negligence, willful misconduct, or fraud; (b) Customer's payment obligations; and
> (c) Provider's defense, payment and settlement obligations under Section 10.1, which are not
> subject to any limitation or exclusion in this Agreement.

*(Keep the existing GN/WM/fraud carve-outs — they are Cobalt's preferred position, playbook B1.)*

**§10.1 — replace the final sentence:**

> …; Provider's obligations under this Section 10.1 are uncapped, are expressly excluded from the
> limitations and exclusions of Section 9 (including Sections 9.1 and 9.2) notwithstanding
> Section 9.1, survive termination of this Agreement, and amounts payable under this Section 10.1
> (including amounts paid to third parties by settlement or award, and related attorneys' fees) are
> deemed direct damages of the indemnified party.

---

## 2. DPA executed at signing — breaks A2 (§5.3 and Exhibit C)

**Problem.** Exhibit C is "[To be attached.]" while §1.2 and the GC's email confirm EU driver and
customer personal data will be processed. GDPR Art. 28(3) (library: `gdpr_art28.md`) requires a
binding contract stipulating items (a)–(h); **absent it, Cobalt as controller is in breach from the
first day of processing**. Playbook A2: "'To be attached' is not acceptable."

**§5.3 — replace:**

> 5.3 Provider and Customer shall execute the Data Processing Addendum attached as Exhibit C
> concurrently with this Agreement. Exhibit C is incorporated into and forms part of this Agreement
> as of the Effective Date. Provider shall not process any personal data subject to the GDPR or UK
> GDPR on Customer's behalf until Exhibit C is in effect.

**Exhibit C — replace "[To be attached.]" with an executed DPA on the following skeleton**
(clause numbers keyed to Art. 28(3)(a)–(h) as summarized in the library):

> **EXHIBIT C — DATA PROCESSING ADDENDUM (effective at signing).**
> 1. *Roles.* Customer is controller; Provider is processor. Where Affiliate personnel or
> customers generate personal data, the applicable Affiliate acts through Customer under §2.2;
> where an Affiliate acts as an independent controller, that Affiliate joins this DPA as a party
> (or third-party beneficiary) and Provider processes its personal data on that Affiliate's
> documented instructions.
> 2. *Particulars.* Subject-matter, duration, nature and purpose of processing, types of personal
> data and categories of data subjects are set out in Annex 1 below, which the parties confirm
> **before** any EU/UK personal data enters the Services.
> 3. Provider processes personal data **only on documented instructions** from Customer, including
> with regard to international transfers [(a)].
> 4. Provider ensures persons authorized to process are bound by confidentiality [(b)].
> 5. Provider implements appropriate technical and organizational security measures, which shall at
> least satisfy §5.2 and shall be documented [(c)].
> 6. Provider does not engage a sub-processor without prior specific or general written
> authorization, flows down equivalent obligations, and remains liable for sub-processor failures
> [(d)].
> 7. Provider assists Customer in responding to data-subject requests and in meeting its own
> obligations, including notifying Customer **without undue delay** after a personal-data breach
> [(e)–(f)].
> 8. At Customer's choice, Provider returns and/or deletes personal data at the end of the Services,
> subject to §12.2 [(g)].
> 9. Provider makes available information reasonably necessary to demonstrate compliance and permits
> audits [(h)]. Provider's use under MSA §5.4 is limited to data rendered **irreversibly
> non-attributable** to an identified or identifiable person.
>
> **Annex 1 — Processing particulars** (populated from the client's 2026-10-25 confirmation):
> — *Subject-matter:* routing and fleet-optimization Services for Customer and its Affiliates,
> including the Rotterdam/Hamburg operations and Brokerage carrier routing.
> — *Duration:* the Subscription Term plus the §12.2 export period; ends on return/deletion under
> clause 8.
> — *Nature and purpose:* hosting, analysis and route optimization on data submitted to the Services.
> — *Types of personal data:* driver names, driver locations, driver working hours; customer
> addresses from the EU operations.
> — *Categories of data subjects:* drivers; EU customers with delivery addresses.

*Flagged unknown (not cited as law): the client could not confirm whether Holdings or Cobalt Freight
Europe B.V. is the Art. 28 controller for the Rotterdam/Hamburg data; clause 1 is drafted to work in
either case. Any controller-to-controller transfer mechanics sit outside the library and are flagged,
not cited.*

*(Audit/breach-notice mechanics should follow RouteWise's standard DPA if one exists — the client does
not know; ask RouteWise in the redline exchange. Art. 28(3) is the only statutory text in the library;
no other GDPR articles are cited here.)*

---

## 3. Kill the unilateral price increase — breaks A3 (Exhibit A ¶4)

**Problem.** Order Form ¶4 permits one mid-term increase (greater of 8% or CPI-U, 60 days' notice)
and uncapped renewal increases; §14.1 makes the Order Form control over the MSA (playbook note C1).
Playbook A3: no mid-term increases; renewal increases ≤ the **lower** of 5% or CPI, 90 days' notice.

**Exhibit A ¶4 — replace:**

> 4. Pricing adjustments. Fees for the Initial Subscription Term are fixed, and Provider may not
> increase the fees during the Initial Subscription Term. For any renewal term, Provider may
> increase the monthly fee by no more than the **lower of (a) five percent (5%) or (b) the trailing
> twelve-month change in CPI-U**, and only upon at least ninety (90) days' prior written notice to
> Customer; absent timely notice, the fees remain unchanged for the renewal term.

*(Arithmetic: 8% of $18,500/mo = +$1,480/mo = +$17,760/yr; earliest application after 60 days'
notice (≈ month 3) costs up to +$50,320 over the remaining 34 months; a renewal-year increase of 8%
lifts annual fees from $222,000 to $239,760.)*

---

## 4. Renewal length and notice — breaks A4 (§3.3)

**Problem.** 24-month auto-renewals on 90 days' notice vs. playbook limits of 12 months / ≤30 days.

**§3.3 — replace:**

> 3.3 Each Subscription Term shall automatically renew for successive renewal terms of twelve (12)
> months unless either party gives written notice of non-renewal at least thirty (30) days before
> the end of the then-current term.

*(Exposure removed: one missed deadline under the current text commits ≈ $444,000
($18,500 × 24), or ≈ $479,520 if a +8% renewal increase applies first.)*

---

## 5. Affiliates under the license — breaks A5 (§2.2)

**Problem.** §2.2 excludes Affiliates unless "named on an Order Form at additional fees"; playbook
A5 names Cobalt Freight Europe B.V. and Cobalt Brokerage LLC and requires coverage at no fee (or
signing by Holdings on behalf of affiliates). Client confirmed (2026-10-25) that **both** affiliates
will use the Services — Europe for Rotterdam/Hamburg, Brokerage for carrier routing — and that
Holdings signs in its own name, so the "signs on behalf of affiliates" alternative is not available
without re-papering the signature block; fixing §2.2 is the route.

**Knock-on.** Two definitions are keyed to "Customer" alone and would leave affiliate use outside the
contract even after §2.2 is fixed: §1.6 "Users" (Customer's employees and contractors only) and §1.2
"Customer Data" (personal data of "Customer's drivers and customers"). Both must be amended together
with §2.2 — otherwise affiliate personnel are unlicensed users and affiliate driver/customer data
falls outside the DPA scope.

**§2.2 — replace:**

> 2.2 The license granted hereunder extends to Customer and its Affiliates (including Cobalt
> Freight Europe B.V. and Cobalt Brokerage LLC) at no additional fees. Customer is responsible for
> its Affiliates' and Users' use of, and compliance with, this Agreement.

**§1.6 — replace:**

> 1.6 "Users" means employees and contractors of Customer or its Affiliates authorized to use the
> Services.

**§1.2 — add at the end:**

> References in this Agreement to Customer's drivers, customers, employees, contractors and Users
> include those of Customer's Affiliates.

---

## Appendix — preferred-position fixes (not hard-rule breaks; ask in the same redline)

- **Exhibit B (B5):** "If monthly availability falls below the target in any three (3) calendar
  months during any rolling six (6) month period, Customer may terminate the affected Order Form on
  thirty (30) days' notice and Provider shall refund all prepaid, unused fees; termination is in
  addition to accrued credits." (Credits-as-sole-remedy is acceptable to Cobalt only with this
  exit right.)
- **§8.1 (B4):** "…for **undisputed** past-due amounts upon fifteen (15) days' prior written
  notice, provided Provider shall not suspend, and shall promptly reinstate, if the undisputed
  past-due amount is paid before the suspension takes effect. Amounts disputed in good faith are not
  grounds for suspension."
