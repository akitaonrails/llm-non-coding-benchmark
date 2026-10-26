# MEMORANDUM — PRIVILEGED & CONFIDENTIAL / ATTORNEY WORK PRODUCT

**To:** General Counsel, Meridian Robotics, Inc.
**From:** Outside counsel
**Date:** October 26, 2026
**Re:** Whether to sue in Travis County to enforce §8 (24-month nationwide non-compete) of the Wei-Lin Zhao employment agreement — and the Company's own exposure if it does

**Scope notes and standing assumptions (flagged per engagement terms):**
- **Assumption A (unconfirmed):** Meridian is a Texas corporation or has its principal place of business in Austin, Texas. This is inferred from the client file (offer letter from "Austin HR"; trips to "Austin HQ"; Texas governing-law clause) but is nowhere stated on the face of the documents. Confirm — it matters for the choice-of-law and jurisdiction analysis. *(Client Q&A, Oct. 26, 2026: the Company has no further information on this; the assumption stands unconfirmed and all Texas-indicia reasoning below inherits that uncertainty — Addendum Part VII.4.)*
- **Assumption B:** The excerpt in `documents/employment_agreement_excerpt.pdf` (§§8, 9, 10, 14, 15) is what we would plead from. No attorneys'-fees clause appears in the excerpt; if the full agreement contains one elsewhere, the fee analysis below changes (open item). *(Still open after the Company's Q&A — the full text was not provided; Addendum Part VII.4.)*
- This memo applies **only** the authorities in `library/INDEX.md`. Propositions commonly believed to be law that are *not* verifiable in that library are expressly labeled **[unverified]** and are not cited.

---

## I. Question Presented

Under which state's law will the enforceability of §8 of the Zhao employment agreement — a 24-month, nationwide covenant barring employment with any business "engaged in the design or sale of autonomous mobile robots for warehouse logistics" — be decided, may Meridian successfully enforce §8 against Zhao (who signed in California without counsel, worked remotely from Oakland, California for his entire tenure, and is now joining Kestrel Autonomy, a Fremont, California warehouse-AMR company), what is Meridian's own liability exposure if it files suit in Travis County (including under Cal. Lab. Code §925, Bus. & Prof. Code §§16600.5 and 16600.1), and should the Company file?

## II. Brief Answer

**Do not file in Travis County.** On these facts our estimate is that there is roughly a **0–10% probability** that a Travis County enforcement action ends with §8 actually preventing Zhao from doing the Kestrel work — and the strictly arithmetic version of that estimate (below) is materially lower still. The binding constraint is not winning in Texas; it is that (i) Zhao can void the Texas forum and choice-of-law clauses at his election under Cal. Lab. Code §925, (ii) even a Texas tribunal applying standard conflict principles (Restatement §187(2)(b), adopted in *DeSantis* by the Texas Supreme Court itself) is likely to displace Texas law in favor of California's fundamental policy against employment non-competes, (iii) if California law governs, §8 is flatly void under §16600 (no "narrow-restraint" saving doctrine; *Edwards*), and — most important — (iv) **suing is itself the risk**: attempting to enforce a contract void under §16600 violates §16600.5(b) regardless of where the contract was signed, is a civil violation (§16600.5(d)), and hands Zhao a fee-shifting private action (§16600.5(e)). A Texas judgment, even if obtained, would likely be refused recognition in California on public-policy grounds and therefore likely changes nothing (the library's Texas jurisdictional practice note).

Subsidiary bands (methodology and arithmetic in Part IV.G):
| Event | Band |
|---|---|
| Zhao voids §14 (forum/choice of law) under §925 | ~80–90% |
| Texas tribunal applies California law even absent a §925 election (§187(2)(b)) | ~55–70% |
| Texas law governs the merits in Travis County despite both | ~20–44% |
| Some injunction issues at all (Texas law assumed; Zhao appears) | ~10–31% |
| A Texas order has real-world effect on Zhao in California (recognition ≤10%, or voluntary compliance / settlement ~5–20%) | ~5–30% |
| **Suing actually keeps Zhao off the Kestrel-type work** | **~0.5–9% → brief-answer band "0–10%"** |

Counterweight exposure if we file: Zhao's side has already telegraphed its theory (resignation email names §925 and California voidness, and discloses he consulted California employment counsel). A filing invites a California action under §16600.5(e) for injunctive relief, actual damages, **and prevailing-employee attorney's fees** — amounts not quantifiable from the current file (Part IV.F).

## III. Facts (with source and any doubt)

1. **Agreement.** Zhao signed Meridian's employment agreement on March 4, 2024, effective that date, as Senior Perception Engineer; the stated work location is "Remote — Employee's residence (Oakland, California)" (`documents/employment_agreement_excerpt.pdf`).
2. **§8 (non-compete).** For **24 months** after termination "for any reason," Zhao may not, **"anywhere in the United States,"** be employed by or provide services to any business "engaged in the design or sale of autonomous mobile robots for warehouse logistics" (excerpt §8).
3. **§9 (non-solicit).** 12 months: no solicitation of Company employees or customers (excerpt §9).
4. **§10.** Standard confidentiality/inventions provisions (excerpt §10).
5. **§14.** Texas governing law; exclusive jurisdiction and venue in **Travis County, Texas** state and federal courts (excerpt §14).
6. **§15.** Employee "acknowledges having had the opportunity to consult counsel" (excerpt §15). The HR timeline states the form was sent 9:12 a.m. and signed via DocuSign at 11:05 a.m. the same day — about 2 hours after receipt — with "no negotiation; no attorney review requested or offered," and that it is the standard form for all engineers (`documents/hr_timeline.md`). The Company confirms this is a universal practice — standard form, same-day signature, nobody negotiates (client Q&A — Addendum Part VII.1).
7. **Performance.** Zhao worked from Oakland, California from March 4, 2024 through September 30, 2026 — **2 years, 6 months, 26 days (~30.9 months)** — with exactly **two short trips to Austin** (onboarding week, March 2024; offsite, October 2025) (`hr_timeline.md`; Python: `relativedelta(2026-09-30, 2024-03-04)`).
8. **Departure.** Resignation effective September 30, 2026. Zhao's email names his new employer, Kestrel Autonomy (Fremont, CA), **a warehouse-AMR company — squarely inside §8's described field** — states he has consulted a California employment attorney who advises that §8 is void under California law and that he may void the Texas forum and choice-of-law clauses, and volunteers that he will honor confidentiality obligations and take nothing (`documents/resignation_email.txt`). That statement is self-reported and unverified; the Company's own review surfaces no evidence to the contrary — it has no evidence Zhao took anything — and states its objection is the competition itself (client Q&A — Addendum Part VII.3).
9. **Start date.** Kestrel start date October 13, 2026 (`hr_timeline.md`) — as of this memo he has been at Kestrel ~13 days.
10. **AB 1076 project.** Legal's company-wide §16600.1 notice project **sent no notice to California employees**; the project was "deprioritized" per legal ops ticket LO-233 (`hr_timeline.md`). The Company confirms no notices were ever sent and that the ticket was closed as "won't do" (client Q&A — recorded in privileged work product only, Addendum Part VII.2).
11. **Timelines (Python arithmetic).** §8 window, if it ran: 2026-09-30 + 24 months = through **2028-09-30**. Kestrel start (2026-10-13) is inside that window; **718 days** would remain as of his start date. §9 window: through **2027-09-30**. Offer letter (2024-02-28) came **14 days after** the §16600.1 notice deadline (2024-02-14); the signed agreement (2024-03-04) came **19 days after**.

## IV. Analysis

### A. Which law applies — and why

This is the whole case. Three layers, in the order a court will reach them:

**1. Cal. Lab. Code §925 (detailed in Part D): voidable at Zhao's election.** Zhao "primarily resides and works in California" (Oakland for the entire ~30.9-month tenure; the contract itself declares the California work location). Meridian required — standard form, no negotiation, two-hour DocuSign turnaround — a provision requiring him to adjudicate in Texas a controversy about whether he may work in California, and requiring Texas law over the substantive protection California gives him (§16600). Any such provision is **"voidable by the employee, and if a provision is rendered void at the request of the employee, the matter shall be adjudicated in California and California law shall govern the dispute"** (§925(b)). The §925(e) carve-out requires the employee be **"in fact individually represented by legal counsel"** *in negotiating* the forum/choice-of-law terms — he was not (HR timeline). His post-termination consultation of counsel (resignation email) does not satisfy the carve-out, which is about negotiating; the §15 boilerplate "opportunity to consult" acknowledgment does not overcome the statute's "in fact" requirement. §925(f) applies: 2024-03-04 ≥ 2017-01-01. **Assessment: ~80–90% Zhao voids §14 if he elects to.** He has effectively announced the election.

**2. Restatement §187(2)(b) — adopted by Texas and California alike — points the same way.** A choice-of-law clause does not control where application of the chosen law "would be contrary to a fundamental policy of a state which has a materially greater interest … and which, under §188, would be the state of the applicable law in the absence of an effective choice" (`restatement_187.md`). Both supreme courts construe it this way:
- *Nedlloyd Lines B.V. v. Superior Court*, 3 Cal.4th 459 (1992): California follows §187.
- *DeSantis v. Wackenhut Corp.*, 793 S.W.2d 670 (Tex. 1990): the **Texas Supreme Court** refused to let a Florida choice-of-law clause govern a non-compete, because the state with the **materially greater interest** had a **fundamental contrary policy** (that case: Texas; the principle is symmetrical and it is Meridian's best authority — and it cuts against Meridian on these facts).
- *Application Group, Inc. v. Hunter Group, Inc.*, 61 Cal.App.4th 881 (1998): California's interest in applying §16600 outweighed the employer's Maryland choice-of-law clause; "California's policy against non-competes is 'fundamental'." The fact pattern differs (there, an employee recruited *to* a California employer) — analogical support, not on all fours.

On the merits of the §187(2)(b) comparison: absent §14, the applicable law in the absence of an effective choice would presumptively be the law of the place of performance or hire — on these facts, California ([unverified] bridging step: the library contains §187 but **not §188**, which is where the "absent an effective choice" default lives; we reason from §187(2)(b)'s own text and *Application Group*, and flag the §188 step as unverifiable here). California's interest is hard to beat: resident, sole work location, contract recites the California residence as the workplace, new employer in California, and the restraint operates *in* California. Texas retains real interests (presumed Austin HQ/business home), but §187(2)(b) requires **materially greater** interest, not parity. **Assessment: ~55–70% a Texas tribunal applies California law even absent a §925 election.**

**3. What this means for a Travis County filing.** If Zhao voids §14 under §925(a)–(b), forum consent goes with it; the library's Texas jurisdictional practice note (Tex. Civ. Prac. & Rem. Code §17.042; *Michiana Easy Livin' Country v. Holten*, 168 S.W.3d 777 (Tex. 2005)) states a Texas court would then need **independent minimum contacts**, and that "two short business trips to Austin and a contract with a Texas employer may or may not suffice." Multiplying these layers: **P(Texas law governs the merits despite §925 and §187(2)(b)) ≈ 20–44%** (arithmetic in Part IV.G).

Two scene-setters:
- *Advanced Bionics Corp. v. Medtronic, Inc.*, 29 Cal.4th 697 (2002): California courts should generally **not enjoin a party from litigating in another state's courts** (the Court reversed a TRE that had stopped pursuit of Minnesota litigation). Cross-forum counter-tactics are constrained on both sides; a "race to the courthouse" is not a reliable strategy for either party.
- The **FTC Non-Compete Clause Rule is not in play either way**: it was set aside nationwide (*Ryan LLC v. FTC*, 739 F. Supp. 3d 496 (N.D. Tex. 2024); FTC lacked substantive rulemaking authority under §6(g); its appeal was voluntarily dismissed in September 2025) (`ftc_noncompete_rule_16cfr910.md` — status: vacated; `ryan_llc_v_ftc.md` — in force). It is **not** an obstacle to state-law analysis and it is **not** a basis to enforce §8. State law controls.

### B. Enforceability under Texas law (assuming, against the odds, Texas law governs)

Under Tex. Bus. & Com. Code §15.50(a), a covenant is enforceable only if it is **"ancillary to or part of an otherwise enforceable agreement,"** with limitations as to **"time, geographical area, and scope of activity"** that are **"reasonable"** and "do not impose a greater restraint than is necessary to protect the goodwill or other business interest of the promisee." If the primary purpose of the agreement is personal services, **Meridian bears the burden** on reasonableness (§15.51(b)). If the limitations are unreasonable, the court **"shall reform the covenant"** and enforce it as reformed, **"but may not award damages for breach before reformation"** (§15.51(c)); §15.51's procedures and remedies are **exclusive** and preempt other criteria (§15.52).

**Consideration/ancillarity — Zhao's likely weakness.** Meridian need not show the consideration was conveyed at signing: *Alex Sheshunoff Management Services, L.P. v. Johnson*, 209 S.W.3d 644 (Tex. 2006) holds an at-will employee's covenant can be enforceable where the employer's promise (e.g., to provide confidential information) is **performed**, expressly *modifying Light v. Centel Cellular Co. of Texas*, 883 S.W.2d 642 (Tex. 1994) — which therefore **must not be cited** for the old rule that unilateral at-will promises cannot support a covenant. Over ~30.9 months Meridian presumably furnished confidential product information; if it did, ancillarity is satisfied. *Marsh USA Inc. v. Cook*, 354 S.W.3d 764 (Tex. 2011) reinforces breadth: consideration (there, stock options) reasonably related to protecting goodwill suffices; no narrow "give rise" requirement. **Open facts (still open after the Company's Q&A — Addendum Part VII.4):** whether confidential product information was actually furnished to Zhao is undocumented (the ancillarity inference rests on the hands-on engineering role, not on records), and the Company has **no information** on whether Zhao received equity — so *Marsh*-type consideration support exists in theory but cannot be evidenced from the current file.

**Reasonableness — §8's soft spot.** 24 months / nationwide for a hands-on engineer is aggressive but not facially hopeless under Texas law: the restraint is limited to a defined industry (warehouse-AMR design/sale) and *Marsh* untethers consideration from customer contact. The realistic Texas-law outcome, given §15.51(b)'s burden on Meridian and §15.50(a)'s "greater restraint than necessary" ceiling, is **a reformed covenant** — shorter and/or narrower in scope, with the reform value being a judgment call the library authorities do not fix (we do not speculate on the number). **No pre-reformation damages** are recoverable (§15.51(c)); remedies are exclusive (§15.52). So even Meridian's *best* Texas-law case yields, at most, an injunction — likely reformed — and an injunction is worth little against a California resident at a California competitor (Part D, last bullet).

**Assessment under Texas law:** as written, ~25–40%; enforceable in reformed form, ~50–70% (both bands are judgment; Sheshunoff/Marsh support validity in some form; the library fixes no reform numbers).

### C. Enforceability under California law (if California law governs — our primary case)

- **§16600(a):** "every contract by which anyone is restrained from engaging in a lawful profession, trade, or business of any kind is to that extent void."
- **§16600(b)(1)** (SB 699 amendment, effective Jan. 1, 2024; declaratory of existing law): the section is read broadly to void "the application of **any** noncompete agreement in an employment context, or **any** noncompete clause in an employment contract, **no matter how narrowly tailored**, that does not satisfy an exception in this chapter."
- ***Edwards v. Arthur Andersen LLP*, 44 Cal.4th 937 (2008):** no "narrow-restraint" doctrine exists in California; noncompetes "are invalid … even if narrowly drawn, unless" a statutory exception applies. The Ninth Circuit cases that once supplied that doctrine — *Campbell v. Board of Trustees*, 817 F.2d 499 (9th Cir. 1987), and *General Commercial Packaging*, 126 F.3d 1131 (9th Cir. 1997) — are **superseded** (disapproved by *Edwards*); do not build on them.
- *Ixchel Pharma, LLC v. Biogen, Inc.*, 9 Cal.5th 1130 (2020) offers a **rule of reason only for business-to-business contracts** and expressly leaves employment restraint to *Edwards*/§16600. Zhao is an employee; Ixchel is no solace to Meridian.
- §16600 contains **no applicable statutory exception**; §8 — and, almost certainly, §9 (the 12-month non-solicit in the same employment contract), on the statute's broad "any … noncompete clause" text, though the extension from *Edwards*-type holdings to non-solicits is an inference we flag rather than a holding in the library — is **void**.
- **Extraterritoriality is answered by the statute itself:** §16600.5(a) — void "regardless of **where and when the contract was signed**"; §16600.5(b) — no employer "shall attempt to enforce a contract that is void under this chapter **regardless of whether the contract was signed and the employment was maintained outside of California**." The Texas-signature/Texas-employer framing does not rescue §8 if California law governs. (Counsel's 2024 firm memo relied on *Westbrook Systems* for the contrary extraterritoriality position; that case is **not in this library**, cannot be cited, and per the 2025 memo had rehearing en banc granted in January 2025 — so the firm's prior position cannot be relied on and we say so.)
- Meridian's surviving California-invalid rights: §10 confidentiality/inventions. §16600 addresses restraints on lawful profession/trade; nothing in the library says confidentiality obligations are void — but the library likewise contains **no authority on enforcing confidentiality/trade-secret claims in California**, so any such route needs separate, currently unverified analysis.

### D. Cal. Lab. Code §925 — the operative engagement-terms analysis

Restated with elements (per `cal_lab_925.md`):
1. Employee "primarily resides and works in California" — **met** (Oakland throughout; contract recites the Oakland residence as the workplace; two short Austin visits do not change primary residence or workplace).
2. Provision required "as a condition of employment" — **met** (standard form for all engineers, no negotiation, sent and signed within two hours on the start date). Residual argument that Zhao could have refused the form is weak given the HR facts.
3. The provision (i) requires adjudication **outside California** of "a claim arising in California" and/or (ii) deprives him of "the substantive protection of California law with respect to a controversy arising in California" — **likely met**: the controversy is whether a California-resident, California-worked employee may work for a California competitor; that arises in California. Meridian's counter — that the claim arises under a Texas contract protecting Texas goodwill, not "in California" — is colorable but secondary; §925(a)(2) does independent work. The bigger statutory hook may even be (a)(1)'s forum term standing alone.
4. Effect: §925(b) — voidable **at the employee's election**; if voided, "the matter shall be adjudicated in California and **California law shall govern the dispute**." This is the engine of the whole analysis.
5. §925(e) exception — **not met**: "in fact individually represented by legal counsel in negotiating" — HR files and the two-hour signature confirm no counsel; the Company's Q&A response confirms company-wide that no engineer negotiates the form (Addendum Part VII.1); the §15 acknowledgment cannot conjure representation that did not occur, and Zhao's post-termination consult is not negotiation.
6. §925(f) — applies (contract March 4, 2024, after January 1, 2017).

**Assessment: ~80–90% Zhao prevails on voiding §14.** Note also the practical jurisdiction point from the practice note: with §14 voided, any continued Travis County case requires independent minimum contacts over Zhao (two business trips plus the contract — "may or may not suffice"), i.e., perhaps ~40–60%, feeding the arithmetic in Part G.

### E. §16600.5 exposure — the affirmative risk created by suing

If California law governs enforceability (the primary case), then **the act of filing the Travis County case is itself the statutory violation**:
- **§16600.5(b):** an employer "shall not attempt to enforce a contract that is void under this chapter regardless of whether the contract was signed and the employment was maintained outside of California." Filing suit to enforce §8 is the paradigm "attempt to enforce."
- **§16600.5(d):** entering **or attempting to enforce** a void contract "commits a civil violation." Note §16600.5(c) separately: Meridian "shall not enter into" contracts containing void provisions — the standard form itself (given to all engineers) is the compliance problem, not just its enforcement.
- **§16600.5(e):** Zhao may sue for **injunctive relief and/or actual damages**, and a prevailing employee "shall be entitled to recover **reasonable attorney's fees and costs**." Zhao is already represented and already asserts the theory. A realistic adverse outcome is a California order barring Meridian from attempting to enforce §8 (against Zhao and possibly as a forward-looking injunction), plus fees and costs. The Company's Q&A confirms the AB 1076 notice gap was a recorded decision to skip compliance for the covered class, not an oversight (Addendum Part VII.2) — documented knowledge rather than inadvertence, which strengthens the plausibility of company-wide injunctive relief; we do not quantify it.

**Quantification:** we cannot compute damages or fee exposure from this file — no Zhao-side fee rates, no damages theory pleaded, no data on lost opportunities. **We do not invent numbers.** The *structural* exposure: one-way fee-shifting in Zhao's favor under §16600.5(e)(2) (we see no fee clause in the excerpt running the other way in a Texas action; the full agreement text remains unreviewed — the Company could not supply it beyond the excerpt, Addendum Part VII.4), plus the injury to Meridian of an adverse declaratory/injunctive ruling that would effectively retire §8 as to California employees company-wide.

### F. AB 1076 notice issue (§16600.1) — modest as to Zhao; a real compliance flag elsewhere

Text (`cal_bpc_16600_1.md`): by **February 14, 2024**, the employer must notify — individualized written communication to last known address **and** email — (1) "current employees" and (2) "former employees who were employed after January 1, 2022," whose contracts include a noncompete clause that does not satisfy a California exception, that the clause is **void**. A violation is "an act of unfair competition within the meaning of Chapter 5 (commencing with Section 17200)"; the library does not contain §17200, so any remedy flowing from that characterization is **[unverified]** and we do not analyze it.

As to Zhao, the timeline arithmetic (Part III.11) matters:
- The notice duty was fixed to the **February 14, 2024** deadline for persons in the covered classes *on that date*.
- Zhao's offer letter came **14 days after** that deadline (Feb. 28) and his signature **19 days after** (Mar. 4). On February 14, 2024, he was neither a current employee nor a covered former employee.
- **Therefore, on the statute's text, Meridian's failure to send the AB 1076 company-wide notice did not itself violate §16600.1(b) *as to Zhao* — the duty never attached to a person hired after the deadline date.** The contrary "continuing duty" reading (that the duty reaches employees hired after February 14, 2024) is an interpretation **[unverified]** in this library; we flag it and do not rely on it.
- The exposure that does exist as to Zhao flows instead from §§16600.1(a) (unlawful to *include* a noncompete clause that fails a California exception) and §16600.5(c)–(d) — i.e., the same entering/attempting-to-enforce theory — not from the missed notice.
- **The company-wide gap (LO-233) is a problem for other California employees** — anyone who was a *current* or covered *former* employee as of February 14, 2024, with a noncompete clause in their contract, is within the class whose notice was required and skipped. That is a compliance and remediation question (client Q&A and handling notes — Addendum Part VII.2; see Part V.5), separate from this matter.

### G. Remedies, fee exposure, and the arithmetic

**What Meridian could win under the most favorable Texas-law scenario (roughly 20–44% likelihood of getting there):** an injunction against Zhao — likely reformed shorter/narrower under §15.51(c) — with **no damages for pre-reformation breach** (§15.51(c)) and exclusive remedies (§15.52). Meridian's own Texas-side fee recovery: none visible (no fee clause in the excerpt); Meridian bears its own costs (unquantified — no billing data in file).

**What Meridian would lose or pay:** the §16600.5(d)/(e) package above (civil violation; Zhao's injunctive/damages action; **fee-shifting to Zhao** if he prevails), the near-certainty that no relief will be had in California: the practice note states an injunction entered in Texas "would in any event face **non-recognition in California on public-policy grounds for the non-compete**." *Advanced Bionics* simultaneously warns against trying to solve this with anti-suit or anti-litigation orders out of California — California courts should not enjoin pursuit of another state's litigation; the interstate tools are poor.

**Probability arithmetic (Python; branch bands are judgment, not data):**
```
P(Texas law governs merits)        = 0.20–0.44   (=(1−0.80..0.90) + 0.80..0.90×(1−0.55..0.70)×(1−0.40..0.60))
P(some injunction issues)          = 0.10–0.31   (= above × P(merits-reformed under TX law 0.50–0.70))
P(order has real-world effect)     = 0.05–0.30   (recogn. ≤0.10 OR voluntary compliance/settlement ~0.05–0.20; combining effects, corridor 0.05–0.30)
─────────────────────────────────────────────
P(suing keeps Zhao off the Kestrel work) = 0.005–0.093 → "0–10%"
```
We present this as a corridor, not a forced single number; human factors (appearance, settlement) are knowingly not independent, which is why we round to a 0–10% **decision band** rather than a point estimate.

**Practical-futility arithmetic (not authority; [unverified] as a proposition of litigation duration):** the §8 window runs out **2028-09-30**; a contested Texas non-compete case through trial — plus any enforcement attempt in California that the practice note tells us will fail — would consume most or all of that window. Time is double-edged: delay itself (no authority in the library on laches; [unverified]) plus the passage of the window degrades the value of any late win.

### H. The strongest argument for each side

**Meridian (least-bad case for suing):**
1. Texas has a substantial relationship to the parties (presumed Austin HQ/business home), so under §187 the Texas choice of law is *prima facie* honored unless §187(2)(b) is satisfied — and Meridian will fight the "materially greater interest" and "fundamental policy" findings (distinguishing *Application Group* as a recruited-employee case; invoking *DeSantis* for the proposition that conflicts methodology, not California's ipse dixit, governs).
2. On Texas-law merits, *Sheshunoff* (later-performed consideration; at-will OK), *Marsh* (goodwill interest without customer contact), and §15.51(c)'s mandatory **reformation** rather than invalidation give Meridian a realistic path to *some* enforceable restraint even if 24 months/nationwide is too broad as written — and §15.52 makes reformed enforcement the whole game.
3. Zhao consented in writing to Travis County venue (§14) — under §17.042/*Michiana* per the practice note, that generally supplies consent jurisdiction — and he "availed" himself twice of Austin onboarding/offsite.
4. The FTC Rule is vacated (*Ryan LLC*), so there is no federal overlay; this is a pure state-law fight in a Texas-friendly statute.

**Zhao:**
1. **§925 kills the engagement terms** — he primarily resides and works in California; the clauses were imposed on a no-negotiation standard form without counsel ("in fact individually represented" fails; the §15 acknowledgment is boilerplate); once he elects, **the matter must be adjudicated in California and California law governs**.
2. If any forum applies California law (via §925(b) or §187(2)(b) with *Application Group*), **§16600 voids §8 outright** — *Edwards* forecloses narrow-restraint arguments, §16600(b)(1) voids the clause "no matter how narrowly tailored," §16600.5(a)–(b) reaches contracts signed outside California, and *Ixchel*'s rule of reason stops at the employment door.
3. **Suing is self-inflicted liability**: §16600.5(b)–(d) makes the attempt itself a civil violation, and §16600.5(e)(2)'s fee-shifting gives his counsel a paid case.
4. Even a Texas win is likely worthless where it matters (California non-recognition; practice note) — and personal jurisdiction over Zhao falls away with the voided consent clause (minimum contacts "may or may not suffice" on two trips).

## V. Recommendation

1. **Do not file in Travis County.** Probability that the suit produces an effective restraint: ~0–10% (arithmetic above); the lawsuit affirmatively creates §16600.5(d)/(e) liability and fee-shifting exposure to Zhao, and any Texas judgment likely cannot be used against him in California. Say the plain thing: **§8, as applied to Zhao, is very likely unenforceable, and the attempt to enforce it is likely unlawful under §16600.5 if California law governs — which it very likely does.**
2. **Do not send Zhao (or Kestrel) any written demand invoking §8 or §9.** Any such communication risks the "attempt to enforce" characterization under §16600.5(b)–(d).
3. **Preserve the confidentiality lane.** His own email states he will honor §10, and the Company has no evidence to the contrary (Addendum Part VII.3). A short, carefully drafted letter *reminding him of his confidentiality/invention obligations* (without referencing §8/§9 as obligations owed) is the available, low-risk step; whether confidentiality terms would themselves be enforceable in a California forum is **not answered by this library** and would need separate analysis before relying on them.
4. **Preserve evidence — do not improve the record after the fact:** the Company reports no evidence that Zhao took anything and states it has no basis for a misuse claim (Addendum Part VII.3). Preserve access records and the LO-233 ticket exactly as they stand — no edits, re-characterizations, or deletions; altering records would compound exposure, not cure it. If misuse later emerges, the trade-secret/confidentiality route is the viable enforcement path — but the library contains no California trade-secret authority; that analysis would be independent of, and slower than, the non-compete we have advised against.
5. **Fix the standard form and the compliance posture now:** given §16600.5(c) and the LO-233 finding, inventory all California-resident employees (and covered former employees as of 2024-02-14) with §8-type clauses; take counsel's advice on remediation and on any §16600.1 corrective notice (the availability and wisdom of a "cure" is [unverified] in this library). The Company confirms the form is unchanged and remains the same-day, no-negotiation standard for engineers (Addendum Part VII.1), so every new California hire joins the §16600.5(c) class — the exposure is systematic and continuing; this protects the Company far more than any lawsuit against one engineer.
6. **Decision-deadline reality:** every week inaction costs optionality, and the §8 window expires 2028-09-30 regardless.

## VI. Open items and unverified propositions

**Open client items (ANSWERED Oct. 26, 2026 — see Addendum Part VII):** negotiation/individual representation (standard form, same-day signature, nobody negotiates — §925(e) carve-out unavailable company-wide); AB 1076 notices (none ever sent; ticket closed "won't do"); Zhao-side conduct (no evidence anything was taken; the Company's objection is the competition itself).

**Remaining unknowns (the Company has no further information — flagged explicitly, not assumed away):** Meridian's state of incorporation/principal place of business (Assumption A stands unconfirmed); Zhao's equity compensation; the full agreement text (fee clauses; §§1–7, 11–13; any arbitration clause); his actual Kestrel duties (role presumed from Kestrel's warehouse-AMR business line and his own email); Zhao's counsel's identity and any standing correspondence (known only from the resignation email); the LO-233 covered-population count. Sources that would resolve each are listed in Addendum Part VII.4.

**Explicitly unverified (not in `library/INDEX.md`; flagged, not cited):** Restatement §188's default rules as the §187(2)(b) comparator; California trade-secret/confidentiality enforcement law; §17200 remedies via §16600.1(c); litigation-duration/laches assumptions; the "continuing duty" reading of §16600.1(b) for post-deadline hires; and the firm memo bank's cases (*Calderon*; *Westbrook Systems*), which are **not in this library**, cannot be cited, and per the 2025 memo had en banc rehearing granted in *Westbrook* — the 2024 memo's recommendation to sue on that basis is not a position we can adopt here.

---

## VII. Addendum — Client Q&A record (October 26, 2026) and remaining unknowns

The Company's answers to `QUESTIONS.md`, recorded here in privileged work product. This addendum changes no probability band in the arithmetic above; it confirms several premises, removes hope for others, and adds one exposure aggravator.

### VII.1 Engagement terms are truly universal (answers the standing-assumption note and the §925(e)/§15 discussion)

The Company answered: *"No. It's our standard form; engineers sign the same day. Nobody negotiates."*

Consequences: (a) the §925(e) carve-out — an employee "in fact individually represented by legal counsel in negotiating" — is unavailable **company-wide**, not merely for Zhao; (b) the §15 "opportunity to consult counsel" acknowledgment is conclusively boilerplate; (c) the §16600.5(c) entering-problem is systematic: every new California engineer who signs this form on a same-day, no-negotiation cycle adds to the class of void-provision contracts. Nothing in the file mitigates this; see Part V.5.

### VII.2 AB 1076 notices were never sent; the ticket was closed "won't do" (answers the LO-233 question)

The Company answered: *"Legal ops never sent the notices. The ticket was closed as 'won't do'."* Combined with the timeline, this confirms the §16600.1(b) company-wide gap as a **recorded decision not to comply for the covered class**, not an oversight. Three consequences:

- As to Zhao, the analysis in Part IV.F is unchanged (the duty never attached to him; the 2024-02-14/2024-02-28 arithmetic stands).
- As to the covered class, documented knowledge rather than inadvertence strengthens the plausibility of a company-wide injunctive claim under §16600.5(e) and heightens the urgency of the Part V.5 remediation decision.
- **Handling note (at the Company's request that this be kept out of writing where avoidable):** this record and the analysis of it are maintained in privileged work product only, and counsel will generate no further gratuitous written characterizations. Two limits, stated plainly: (i) the underlying facts already live in the Company's own records (the HR timeline; ticket LO-233) — those records **must be preserved exactly as they stand; no editing, re-characterization, or deletion** — altering or discarding them would compound any later exposure; (ii) no course of conduct can keep facts out of writing if disclosure is later compelled (discovery, regulatory attention) or if a compliance filing is required. The durable protection is remediation, not silence; whether a corrective §16600.1 notice is advisable remains [unverified] on this library and needs separate advice before any action.

### VII.3 Zhao-side facts (answers the evidence questions partially)

The Company answered: *"No evidence he took anything. He said he wouldn't. It's the competing itself we object to."*

Consequences: (a) there is **no misuse-of-information predicate** — the trade-secret/confidentiality lane has no present facts, and there is no conduct leverage of any kind beyond the covenant itself; (b) his resignation-email commitment remains self-reported, but nothing known to the Company contradicts it; (c) the Company's sole objection is the competition itself — i.e., a suit could pursue only the transparent taking of a new job, which is exactly the activity §16600 exists to protect, and the only instrument that could stop it is the one most likely void. This confirms, and strengthens, the Part V recommendation: the 0–10% decision band stands, and the downside terms of the trade are unchanged.

### VII.4 Remaining unknowns (explicitly flagged; the Company has no further information)

For every question not answered above, the Company stated it has no additional information. The following therefore remain **unknown** — flagged, not assumed away:

1. **Assumption A — Meridian's state of incorporation and principal place of business.** Unconfirmed. All Texas-indicia reasoning (substantial relationship under §187; "Austin HQ") proceeds on inference from file labels and the clauses themselves. The residual risk is one-directional: if the Company is not Texas-based, P(Texas law on the merits) can only fall within or below the stated 20–44% corridor; nothing available can raise it.
2. **Zhao's equity compensation.** Unknown; *Marsh*-type consideration support cannot be evidenced. Source that would resolve it: plan-administrator/compensation records, not further HR interviews.
3. **The full agreement text.** Only the excerpt (§§8–10, 14–15) was ever provided. Any attorneys'-fees clause (Assumption B), §§1–7 and 11–13, or an arbitration clause could shift the fee and forum arithmetic. Source: the executed agreement in the Company's own contract files.
4. **Zhao's actual duties at Kestrel.** Presumed inside §8's "warehouse-AMR design or sale" field from Kestrel's business line and his own email; not documentarily verified. If his role were outside that field, §8 would fail for a much simpler reason than choice of law.
5. **Zhao's counsel and standing correspondence.** Known only through the resignation email (he consulted a California employment attorney). No demand letter has arrived to date, and counsel's identity is unknown.
6. **LO-233 covered population.** The count of California current and covered-former employees holding noncompete clauses as of February 14, 2024 is unknown; the Part V.5 remediation scoping needs it, and the source is the Company's own records.

**Resolution posture:** none of these unknowns supports filing in Travis County. Each either erodes the Texas-law case further (item 1), is remediable internally (items 2, 3, 6), affects quantification only (item 3), or narrows §8 independently (item 4). If the Company locates any of the listed records, the memo will be updated without re-asking questions already answered.

---

**Prepared per contract terms:** every cited authority maps to `library/INDEX.md`; see `citations.json` (20 entries; statuses checked). Addendum Part VII records the client Q&A of October 26, 2026; no new authorities were added.
