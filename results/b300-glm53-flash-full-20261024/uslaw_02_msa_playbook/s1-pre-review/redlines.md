# Redlines — RouteWise MSA v7.3 (+ Exhibits)

Replacement text for each **hard-rule** violation (rules A1–A5), in ranked order, followed by the
one preferred-position redline. Rationale and dollars are in `issues.json`; this file is the drafting source.

---

## 1. A1 — Liability cap must not swallow the IP indemnity (§9.3, §10.1)

Per library `contract_interpretation_notwithstanding.md`: an "uncapped" promise elsewhere does not
defeat a cap that applies "NOTWITHSTANDING ANYTHING TO THE CONTRARY … IN THIS AGREEMENT" unless the
cap clause itself carves the obligation out. The fix must therefore live inside §9 (and be confirmed in §10.1).

**§9.3 — replace entire sentence with:**

> "The exclusions and limitations in this Section 9 shall not apply to: (i) a party's liability for its
> gross negligence, willful misconduct, or fraud; (ii) Provider's indemnification obligations under
> Section 10.1; or (iii) Customer's payment obligations."

**§10.1 — replace the final phrase ("…are uncapped.") with:**

> "Provider's obligations under this Section 10.1 are uncapped and are not subject to the limitations in
> Section 9."

*Note (drafting only, not a playbook issue): §9.2 excludes consequential damages "HOWEVER CAUSED," which
can undercut the gross-negligence/willful-misconduct carve-out Cobalt keeps under §9.3. Deleting
"HOWEVER CAUSED" is optional housekeeping; the playbook does not require it.*

**No change to §9.1 or §9.2 otherwise.** The 12-month cap and the §9.3 carve-outs as offered are within
what the playbook accepts (B1: 12–24 months' fees acceptable; mutual carve-outs "should be accepted when
offered").

## 2. A2 — DPA must be executed and attached at signing (§5.3, Exhibit C)

Per library `gdpr_art28.md` (Regulation (EU) 2016/679, Art. 28(3)); absent the processing contract the
controller is in breach from the first day of processing.

**§5.3 — replace with:**

> "To the extent Provider processes personal data subject to the GDPR or UK GDPR on Customer's behalf, the
> Data Processing Addendum attached as Exhibit C applies and is incorporated into this Agreement. Provider
> shall not process personal data subject to the GDPR or UK GDPR unless and until Exhibit C has been
> executed by both parties."

**Exhibit C — replace "[To be attached.]" with the executed DPA.** The library requires the DPA to set out
the subject-matter, duration, nature and purpose of the processing, the type of personal data and categories
of data subjects and the obligations and rights of the controller, and to stipulate that the processor:
(a) processes only on documented instructions; (b) ensures confidentiality; (c) takes security measures;
(d) respects sub-processor conditions; (e)–(f) assists the controller; (g) deletes or returns data; and
(h) makes information available and allows audits.

*Confirmed scope (client, this turn): driver names, locations, hours and EU customer addresses from the
Rotterdam/Hamburg operations, run through the Europe B.V. — which is a Customer party once the signing
structure in item 4 is implemented. The DPA must record these data types and data-subject categories and
identify each Customer party (Holdings, Europe B.V., Brokerage LLC) as a controller for the data it submits.
Exact controller mapping is an open item, flagged explicitly in `QUESTIONS.md` and `STATUS.md`.*

## 3. A3 — No mid-initial-term increase; renewal increases capped at lesser of 5% or CPI (Exhibit A ¶4)

The increase power appears **only in the Order Form**, and MSA §14.1 gives Order Forms priority over the
MSA for their subject matter (see also MSA §4.4); the fix must be made in the Order Form.

**Exhibit A, ¶4 "Pricing adjustments" — replace entire paragraph with:**

> "4. Pricing adjustments. Fees shall not increase during the Initial Subscription Term. Provider may
> increase the fees for a renewal term only if it gives Customer written notice at least ninety (90) days
> before the end of the then-current Subscription Term, and any such increase shall not exceed the lesser
> of five percent (5%) or the change in the most recent twelve-month change in the CPI-U."

## 4. A5 — Affiliates covered: Holdings signs on behalf of them (§2.2, §1.6, signature page)

Client confirmed (this turn): **both affiliates will use the platform** — Europe B.V. for Rotterdam/Hamburg
routing, Brokerage LLC for carrier routing — and elected the **Holdings-signs-on-behalf** compliance path.
Implement it and conform the definitions so affiliate use is genuinely licensed and authorized:

**(1) Signature page — sign as:**

> "COBALT LOGISTICS HOLDINGS LLC, on behalf of itself and its Affiliates Cobalt Freight Europe B.V. and
> Cobalt Brokerage LLC"

**(2) §2.2 — append one sentence:**

> "An Affiliate that is a party to this Agreement as part of the signing party above is covered by the
> license at no additional fee."

**(3) §1.6 "Users" — amend to read:**

> "1.6 'Users' means Customer's employees and contractors, and the employees and contractors of any
> Affiliate that is a party to this Agreement as part of Customer, authorized to use the Services."

*Why (3) matters: affiliate staff are not "Customer's employees and contractors" as defined, so without the
conforming edit their access would not be authorized even under the on-behalf signing. Why (2) matters: it
removes any residual reading of §2.2's "Customer only / Affiliates at additional fees" exclusion against the
named affiliates. Each tag-along edit can be dropped individually without breaking the other two; together
they satisfy both prongs of A5 (signed by Holdings on behalf of affiliates, and covered at no additional fee).*

## 5. A4 — 12-month auto-renewals, 30-day notice (§3.3)

**§3.3 — replace bolded sentence with:**

> "3.3 Each Subscription Term shall automatically renew for successive renewal terms of twelve (12) months
> unless either party gives written notice of non-renewal at least thirty (30) days before the end of the
> then-current term."

---

## Preferred position (B5) — chronic-failure exit right in the SLA

Not a hard rule; concede-able with Legal approval. Recommended text if the vendor resists nothing else:

**Exhibit B — append:**

> "If the availability target is missed in any three (3) calendar months within any six (6) consecutive
> calendar months, Customer may terminate the affected Order Form on written notice and receive a pro-rata
> refund of prepaid, unused fees."
