# APA redline — Brightline Cabinetry / Lone Star Millwork (seller's markup of buyer draft)

**Working assumptions (prominent, per engagement rules):**
- **Purchase Price is not stated in the draft excerpt.** Escrow §9.3 says "$310,000 (10%)", implying a Purchase Price of **$310,000 ÷ 0.10 = $3,100,000**. All dollar caps below use that figure. Confirm actual price and allocation (QUESTIONS.md Q1).
- Payroll-tax rates used below (employer FICA 7.65%; FUTA 0.6% on first $7,000/employee) are **not in the library and are unverified**; the library establishes that the liability categories exist and that §3509 reduced rates apply if non-willful (`worker_classification_tx_irs.md`).
- Every citation below is to a file listed in `library/INDEX.md`; anything else is labeled unverified.

---

## §2.4 Earn-Out — **CHANGE (mechanics and economics)**

**Proposed language (replaces the EBITDA sentence; new (b)-(e) added):**

> "EBITDA" means, for the Measurement Period, the earnings of the Business before interest, taxes, depreciation and amortization, determined in accordance with GAAP applied on a basis consistent with Seller's accounting principles, methods and practices as used in the 2025 management accounts, consistently applied throughout the Measurement Period, and without giving effect to: (i) allocations of Buyer's or its Affiliates' corporate overhead, management fees or shared-services charges; (ii) transaction, financing, integration, synergy-capture, restructuring and purchase-accounting charges, and any accounting changes required by the Transaction; and (iii) costs of expanding the Business beyond its operation as of Closing.
> (b) From Closing through the Measurement Period, Buyer shall operate the Business in the ordinary course consistent with past practice and shall not take any action, or omit to take any action, the purpose or effect of which is to reduce or avoid the Earn-Out, including diverting customers, orders or revenues to any business of Buyer or its Affiliates.
> (c) Buyer shall deliver to Seller, within 45 days after each of the first four fiscal quarters, an unaudited statement of the Business's EBITDA. Seller may, on reasonable notice, audit through an independent accounting firm of its selection at Seller's expense.
> (d) Any dispute over EBITDA shall be referred, exclusively and finally, to a nationally recognized independent accounting firm jointly selected by the parties; its determination governs; its fees are allocated in inverse proportion to the degree it sustains each party's position.
> (e) If Buyer sells the Business or substantially all of its assets or equity during the Measurement Period, the maximum Earn-Out amount becomes immediately due and payable at the time of that sale.

**Why.** "As determined by Buyer in good faith in accordance with Buyer's accounting policies" lets the buyer allocate overhead, management fees, integration costs and purchase-accounting adjustments against the Business and zero the earn-out; the practice-note protections are exactly the list above (`earnout_definitions.md`; *Lazard Technology Partners v. Qinetiq*, 114 A.3d 193 (Del. 2015)). **Economics, shown:** threshold $700,000; 2025 EBITDA $740k (seller-prepared) pays 0.40 × (740,000 − 700,000) = **$16,000**; full $400,000 requires EBITDA of 700,000 + 400,000 ÷ 0.40 = **$1,700,000** (~2.3× current); EBITDA net of the disclosed add-backs (740,000 − 180,000 owner salary − 42,000 legal = $518,000) pays **$0**. As drafted the earn-out is close to worthless. Negotiation: either lower the threshold or convert the earn-out headline into the fixed Closing Payment. Do not let the buyer bank the $400k "contingent consideration" while paying nothing. **Hensley overhang:** Hensley is 38% of revenue, has not consented (and see §3.3 on outreach sequencing); if it leaves or re-prices post-closing, EBITDA drops and the $700,000 threshold is unreachable — the earn-out pays $0 on the downside while the buyer keeps the upside. That asymmetry strengthens the convert-to-fixed ask.

## §3.3 / Schedule 3.3 Required Consents — **CHANGE (schedule is false as drafted)**

**Proposed Schedule 3.3 (replaces "None."):**

> 1. Hensley Homes Master Supply Agreement §18 — consent, may be withheld in sole discretion. Seller to use commercially reasonable efforts to obtain written consent prior to Closing.
> 2. Shop Lease (7700 Burleson Rd) §22 — landlord consent to assignment, not to be unreasonably withheld. Seller to use commercially reasonable efforts to obtain written consent prior to Closing.

**And add a closing condition (Article VII):**

> Receipt of the written consents listed on Schedule 3.3, in each case without modification of the underlying contract's economic terms; provided that if Hensley Homes conditions its consent on modified commercial terms, the parties shall in good faith consider a corresponding purchase-price adjustment, and either party may decline to close on that basis.

**Why.** A clause barring assignment "by operation of law, merger, sale of assets, change of control or otherwise" is enforced as written; the unconsented asset-sale transfer is a breach and the transfer **void** (`anti_assignment_change_of_control.md`: *SQL Solutions v. Oracle*, 1991 WL 626458 (N.D. Cal.); Restatement (Second) of Contracts §§317, 322). Hensley is 38% of revenue and consent is in its "sole discretion," which the library notes is leverage to renegotiate price. Keeping the risk allocation seller-protective: the condition is **mutual** and tied to *unmodified* terms, so the buyer cannot use Hensley's response as a walk-away/reprice option. Cascade Builders (§1.2) needs **notice only** — put it on a notice schedule as a closing deliverable. The 22 residential contracts are silent: rights are generally assignable; obligations need consent only where performance is personal (Restatement §§317, 322) — notice/novation, no condition.

**Sequencing clause to add (consent process).** This account is a personal-relationship account; a consent letter arriving from a stranger is the fastest way to convert "sole discretion" into "no." Control the process in the contract, without disclosing anyone's posture:

> The parties acknowledge that the consent processes identified on Schedule 3.3 involve material customer and landlord relationships of the Business. Prior to Closing, all contacts with such counterparties regarding the Transaction or any required consent shall be initiated and led by Seller, shall occur on a confidential basis (with any Buyer participation pre-agreed in advance and subject to customary confidentiality undertakings), and shall be preceded by such direct owner-to-principal communications as Seller determines appropriate. Buyer shall not independently solicit any consent prior to Closing.

**Risk note for negotiation (not for the draft):** if Hensley responds badly, expect the buyer to reach for a Hensley-specific holdback or price re-trade. The condition as drafted already caps that: the adjustment is "corresponding," considered in good faith, and **either party may walk** — so the buyer's downside is walking, not repricing at will. If the buyer insists on a dedicated Hensley holdback, keep it a separate escrow released on consent, sized to the contract's margin, and refuse to let it consume the general $310,000 escrow.

## §4.12 Employees and Contractors — **CHANGE (cannot sign clean; Ray knows)**

**Proposed language (replaces §4.12; pairs with §7.4(b) below):**

> 4.12 Employees and Contractors. Except as set forth on Schedule 4.12, all individuals providing services to the Business have been classified as employees or independent contractors as required by applicable law, and Seller has withheld, remitted and paid all employment, payroll and withholding taxes required to have been withheld or paid. **Schedule 4.12** shall disclose, at a minimum: the nine installers paid on Form 1099 (exclusive service, Seller-provided trucks and tools, daily scheduling by the shop foreman, hourly rates of $34-41, average tenure 3.4 years, no written agreements). (The Hardaway Builders dispute and the open warranty log are deliberately **not** on Schedule 4.12 — they are not employee/classification-rep subject matter, and misfiling them there would qualify nothing they touch; they belong on the litigation/disputes schedule, where the §7.4(c) disclosed-matters exclusion does reach them.)
> 4.12A Classification Special Indemnity. Seller shall indemnify Buyer for Losses arising from employment-tax assessments or wage-and-hour claims relating to the individuals disclosed on Schedule 4.12, in each case only for services rendered prior to Closing, subject to a cap of **$[225,000-300,000]** (sizing below), with no Basket applying, surviving until 60 days after expiration of the applicable limitations period. Such Losses shall not count toward the Basket or the §7.4(b) Cap, and Buyer shall not bring a §7.1 claim in respect of the disclosed arrangement itself.

**Why.** The nine installers "work exclusively for one business, on its schedule, with its tools and vehicles, paid hourly, for years" — the library's own facts pattern: **employees under the common-law control test regardless of label** (IRS Rev. Rul. 87-41; Treas. Reg. §31.3121(d)-1; `worker_classification_tx_irs.md`). A clean rep Ray knows to be false is both a sandbagged indemnity and a fraud risk (see §7.4(c) below). The library's seller protections apply verbatim: disclose, then size a special indemnity (`sandbagging.md`). **Sizing, shown.** *Payroll tax:* $612,000 × 7.65% = $46,818/yr employer FICA; FUTA 0.6% × $7,000 × 9 = $378/yr; ≈ **$47,196/yr**; average tenure 3.4 yrs → ~3 years ≈ **$141.6k** (7.65%/FUTA rates not in the library — unverified, labeled). *Overtime — now confirmed by client as live:* installers work **45–50 hrs/week in busy season, paid straight hourly**, so nothing has been paid on the half-time premium for hours over 40 (FLSA overtime is per-week, `worker_classification_tx_irs.md`). At the $37.50 midpoint of the disclosed $34–41 band, premium owed = 0.5 × $37.50 = **$18.75/hr**; midpoint OT = 7.5 hrs/wk → $140.63/installer/busy-season week; 20–30 busy weeks × 9 installers = **$25.3k–$38.0k/yr**; arithmetic ceiling (if every worked week were 47.5 hrs — total hours are bounded by $612,000 ÷ $37.50 = 16,320 hrs) = **$48.3k/yr**; ~3 years = **$75.9k–$144.9k**. *Combined ~3-year core exposure before penalties, interest, and any FLSA doubling/liquidated damages or longer lookback (those remedies/periods are not in the library — unverified; if a doubling applied to the wage component, the range would grow to roughly $293k–$431k):* **$217.5k–$286.5k**. Hence a **$225k–$300k** proposed cap (open with ~$250k; the old $150k–$200k guess is superseded — overtime was the missing variable and it was material). Still left open by the draft cap: any pre-2023 payment history and audit/willfulness history (remaining unknowns — QUESTIONS.md); if either surfaces, re-open the number. Section 3509 reduced rates should cut the FICA/FUTA component if non-willful (`worker_classification_tx_irs.md`; rates themselves not in library — unverified). "The workers like it" is legally irrelevant — the obligations run to the IRS, TWC and the wage statute, not to the workers' satisfaction, and their consent is not a defense. Texas UI successor provisions are the buyer's reason to *want* this structure (Tex. Lab. Code §201.041; 40 TAC §815.134; successor FLSA risk with substantial continuity, per the same library file) — the buyer's reclassification need is a pricing conversation, not a seller-rep conversation.

## §6.1–6.2 Pre-Closing Covenants (permit runway) — **ADD**

The buyer's draft excerpt contains no pre-closing environmental/permit covenant, but data room §4.1 — in the buyer's hands — says the City of Austin spray-booth permit is **non-transferable**, the buyer must **reapply**, and the City's stated processing time is **30–60 days**: longer than the "sign in two weeks" schedule the buyer's cover email proposes. Seller cannot cure this pre-closing (only the operator-in-name can file), so the protection is a buyer filing obligation plus seller cooperation, not a seller closing condition:

> **6.1 Permit Applications.** On or promptly following the Signing Date (and in any event within five (5) Business Days thereafter), Buyer shall file all applications, notices and reapplications required in Buyer's name to continue the operation of the Business at the Premises, including the air-permit reapplication covering the spray-booth operation; and Seller shall furnish, and shall cause Seller's environmental consultant and principals to furnish, commercially reasonable cooperation, access to the Premises before and after Closing, and copies of all correspondence with regulators, as Buyer reasonably requires to file and prosecute such applications.
>
> **6.2 Interim Operation.** Pending issuance of any permit described in Section 6.1, the parties shall cooperate in good faith as to lawful interim operation of the affected processes to the extent available under the applicable regulatory program, and Buyer shall be responsible for compliance with all environmental requirements applicable to its operation of the Business from and after Closing. Nothing in this Agreement obligates Seller to obtain, or conditions Closing upon the issuance of, any permit in Buyer's or any third party's name.

**Why.** The 30–60-day runway and non-transferability are **data-room facts (data room §4.1), not library propositions; this covenant structure is drafting judgment built on those facts, and no library citation is claimed.** The commercial point is sequencing: the filing must start at signing — before the deal becomes public — or the shop loses 4–8 weeks of production post-closing. Whether interim operation is actually allowed is a City/consultant question the deliverables flag rather than assume (QUESTIONS.md). This section is what the letter to buyer's counsel refers to ("our redline adds a signing-time covenant to file and cooperation").

## §7.4(a) Basket — **KEEP**

Deductible (not tipping) at $75,000 is seller-favorable. Deductible and tipping are the two basket structures the library records as in use, and the ABA study data in `baskets_caps.md` speaks to cap size and survival periods — not to which basket type is standard — so **no market claim is made for deductible-over-tipping**; the ask is simply that the buyer keep what its own draft gave us. $75,000 ÷ $3,100,000 ≈ **2.4%** of price. Known items (warranty $23,000 + Hardaway $9,800 = $32,800) stay under it. If the buyer proposes tipping or a below-basket "mini-basket" for the special indemnity, hold the line: the special indemnity already has no basket, which is its concession.

## §7.4(b) Cap — **CHANGE one carve-out**

**Proposed language (replaces the exception clause):**

> ...except for Fundamental Representations, which shall be subject to a cap equal to the Purchase Price. Losses under §4.12A are subject solely to the Classification Cap.

**Why.** Keep general cap 10% of price (= $310,000, matching escrow) and fundamental reps at full price — both market (ABA Deal Points Study — `baskets_caps.md`). But carving the **operational** worker-classification rep out to a full-Purchase-Price cap "is off-market and should be resisted or replaced with a sized special indemnity" (`baskets_caps.md`, near-verbatim). As drafted Ray carries up to $3.1M against a ~$47k/yr problem. Delete "Section 4.12" from the exception; move classification to the §4.12A special indemnity.

## §7.4(c) Sandbagging — **CHANGE (reject as drafted)**

Buyer's counsel called this "market-standard knowledge language." It is the opposite: it is a **pro-sandbagging** clause — buyer keeps indemnity rights "regardless of knowledge acquired (or capable of being acquired) ... before or after execution." The library does not establish pro-sandbagging as market standard; both pro- and anti- clauses are in practice and the ABA study tracks the split (`sandbagging.md`).

**Proposed language (anti-sandbagging / disclosed-matters exclusion):**

> Seller shall have no liability under Section 7.1 for any Losses arising from (i) any fact or matter disclosed in the Disclosure Schedules or the data room, or (ii) any matter actually known to Buyer, by name of the individual(s) with actual knowledge, prior to the time of filing the claim. The parties' rights in respect of the matters disclosed on Schedule 4.12 are exclusively as provided in Section 4.12A.

**Why.** Library rule: a seller who discloses a known issue, then gives a clean rep subject to a pro-sandbagging clause, "has effectively agreed to indemnify for the disclosed issue"; the protections are an anti-sandbagging clause, a schedule exception, or a capped special indemnity (`sandbagging.md`; *Akorn v. Fresenius* (Del. Ch. 2018) (dicta) is the library's only case and it is dicta — cite with care). Our package combines (ii) schedule exception + (iii) special indemnity, so (c) as drafted only adds risk. If the buyer refuses the "actual knowledge" bar, minimum position is clause (i) — disclosed matters cannot be "breaches" of a rep that is expressly qualified "except as set forth on Schedule 4.12."

## §7.4(d) Survival — note (not in redline list)

18 months general is inside the 12-24-month market band (`baskets_caps.md`) — keep; the statute-plus-60-days tail for §4.12/taxes moves with the special indemnity, and the general items should not inherit that tail.

## §8.2 Non-Competition — **CHANGE (against Ray's instinct)**

**Proposed language:**

> Seller and Ray Brightline shall not, for five (5) years after Closing, own, manage, operate or provide custom cabinetry fabrication or installation services to customers located within the Trade Area, meaning Travis County and the contiguous Texas counties of Williamson, Hays, Bastrop and Comal. The parties agree this covenant is ancillary to the sale of the goodwill of the Business. If a court of competent authority finds the remaining period or area unenforceable, the covenant shall be reformed and enforced to the maximum extent enforceable.

**Why.** 7 years / 500 miles around Austin for a single-shop custom cabinetry business is "likely overbroad as to both" time and area; reformation under §15.51(c) is the remedy, and "3-5 years within the trade area is typical" (`tx_noncompete_sale_of_business.md`: Tex. Bus. & Com. Code §15.50; *Marsh USA v. Cook*, 354 S.W.3d 764 (Tex. 2011)). Ray says sign whatever — but the library's warning is the reason not to: an overbroad covenant to which a material share of the price is allocated "invites IRS scrutiny of the allocation as well" (same file). The county-band choice is a drafting judgment, not a legal requirement; the 5-year outer bound is the library's range. Confirm the price allocation before fixing the number (QUESTIONS.md Q1).

## §9.3 Escrow — **KEEP amount/term for general claims; resist extension**

**Proposed language:**

> $310,000 (10% of the Purchase Price) shall be escrowed for 18 months as security for claims under Section 7.1 other than Section 4.12A. [If Buyer requires security for 4.12A:] a separate escrow of up to $[special-indemnity cap] shall secure Section 4.12A claims and be released upon the earlier of resolution of pending claims and expiration of the §4.12A survival period. In no event shall the general escrow be extended beyond 18 months.

**Why.** $310,000 = 10% = the general cap, held 18 months = the general survival: internally consistent, keep it. The risk is the buyer using the §4.12/tax survival tail to hold the whole $310k for years; the fix is a second, smaller, correctly-sized holdback for the special indemnity only. (Escrow sizing percentages beyond "cap ~10%" are not in the library — no market claim made; labeled unverified.)
