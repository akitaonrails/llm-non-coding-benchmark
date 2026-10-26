# MEMORANDUM

**To:** General Counsel, Meridian Robotics, Inc.
**From:** Outside counsel
**Date:** October 25, 2026
**Re:** Enforceability of §8 (24-month nationwide non-compete) against Wei-Lin Zhao; whether to file in Travis County
**Privileged & confidential — attorney work product**

---

## 1. Question Presented

May Meridian enforce §8 of Zhao's employment agreement — a 24-month, nationwide bar on working for any business that designs or sells warehouse-logistics autonomous mobile robots — against a software engineer who resided and worked full-time in California, signed the form agreement by DocuSign two hours after receiving it without counsel, and is now employed in California by a competitor; and should Meridian file suit in Travis County, Texas, given that §14 chooses Texas law and a Travis County forum?

## 2. Brief Answer

**No on both counts. Do not file in Travis County, and do not send a demand letter threatening §8.**

- **Probability that California law governs the §8 question: ~87.5% (range 70%–98%).** Two independent routes get Zhao there: Cal. Lab. Code §925 (which, at his election, voids *both* halves of §14 and statutorily assigns California law and a California forum), and the Restatement §187 analysis that Texas and California courts both apply (under which California's §16600 policy is "fundamental" and California has the materially greater interest).
- **Probability Meridian obtains usable §8 relief (interim or job-affecting order) from any court: ~3% (range 1.5%–7.2%).**
- **Probability Meridian obtains relief that actually stops the Kestrel Autonomy job: under 1% (range 0.3%–2.0%).** Even a Texas injunction would face non-recognition in California on public-policy grounds (`library/tx_jurisdiction_note.md`), so the realistic product of suit is an unenforceable order and two forums' worth of fees.
- **Probability Meridian §8 is held void/unenforceable as to Zhao if litigated: ~90% baseline (grid range 80%–95% — and the 90% baseline is itself generous to Meridian; see §7.1).** Under California law §8 is void on its face — §16600 as amended voids it "no matter how narrowly tailored," and the escape hatches (narrow-restraint, rule-of-reason) are foreclosed by *Edwards* and *Ixchel*.
- **Probability Meridian creates affirmative liability for itself by filing: ~85% (range 65%–97%), essentially one-way.** §16600.5 makes the *attempt to enforce* a void contract a civil violation, and makes a fee award to a prevailing employee mandatory. Meridian's exposure starts the moment it files — before it can lose.
- **Expected net cost of filing: roughly −$540k** (range −$230k to −$800k on the cost side, before any company-wide notice/UCL claims; the relief probability barely moves it). Arithmetic in §7.

The bad news stated plainly: §8 is not merely hard to enforce against this employee — **Meridian's own conduct has already generated liability independent of the lawsuit, and the client's 10/25 answers have now confirmed it.** Meridian (i) put a clause in a California employee's contract that California makes unlawful to include (§16600.1(a); §16600.5(c)); (ii) **never sent the statutory AB 1076 notices to anyone** — legal ops ticket LO-233 was closed "**won't do**," a documented, knowing non-compliance decision, not an oversight; and (iii) runs a uniform no-negotiation, same-day-signing form ("nobody negotiates"), which forecloses any individual-negotiation defense for **any** California engineer. And Meridian's stated objection is that Zhao is *competing* — with no evidence he took anything — which is precisely the injury California law refuses to redress. Zhao's departure is now a compliance-and-remediation problem, not a litigation problem.

---

## 3. Facts

From `documents/employment_agreement_excerpt.pdf`, `documents/hr_timeline.md`, `documents/resignation_email.txt`.

| Date | Event |
|---|---|
| 2024-02-28 | Offer letter emailed by Austin HR to the candidate **in Oakland, CA**; states "**fully remote from California**." |
| 2024-02-14 | *(Company-wide)* AB 1076 notice deadline; notice project "deprioritized" per legal-ops ticket **LO-233**, which the client confirms was later **closed "won't do"**; **no notice ever sent to anyone**. |
| 2024-03-04 | Agreement sent 9:12 a.m.; **signed via DocuSign 11:05 a.m.** (≈2 hours). No negotiation; no attorney review requested or offered; **standard form for all engineers**. |
| 2024-03-04 → 2026-09-30 | Worked from Oakland. **Two** trips to Austin HQ (onboarding, Mar. 2024; offsite, Oct. 2025). |
| 2026-09-16 | Resignation email: joining **Kestrel Autonomy, Fremont, CA**; has consulted a **California employment attorney**; states he will honor confidentiality and take nothing. |
| 2026-09-30 | Termination effective. §8's 24-month clock would run to **2028-09-30**. |
| 2026-10-13 | Kestrel start date (**assumed to have occurred — see §8 item 1**). |
| 2026-10-02 | GC question. **Today is 2026-10-25 — 25 days post-termination, ~12 days post-start.** |

**Key contract terms.** §8: 24 months, "anywhere in the United States," any business "engaged in the design or sale of autonomous mobile robots for warehouse logistics." §9: 12-month employee/customer non-solicitation. §10: standard confidentiality/inventions. §14: Texas law; exclusive jurisdiction and venue in Travis County. §15: "Employee acknowledges having had the opportunity to consult counsel" — contradicted by Meridian's own HR file note in the same exhibit ("Employee signed via DocuSign 2 hours after receipt; **no counsel involved**").

**Facts Meridian created for Zhao.** The offer letter's "fully remote from California" line is Meridian's own proof that Zhao "primarily resides and works in California" (§925(a)). The two-hour DocuSign turnaround, "standard form for all engineers," and "no negotiation" are Meridian's own proof that the clauses were **required as a condition of employment** (§925(a)) and were not individually negotiated (§925(e)). The §15 recital does not help and hurts: it is contradicted by the HR file in the same document set, which reads as papering over the §925(e) exception.

**Client confirmations received 2026-10-25 (now facts, not assumptions).** (1) The §8 form is uniform and **never negotiated** — "engineers sign the same day. Nobody negotiates." That forecloses the §925(e) "individually negotiated with counsel" exception not just for Zhao but for **every** engineer on the form. (2) **No §16600.1(b) notice was ever sent to anyone**; LO-233 was **closed "won't do."** (3) **No evidence Zhao took anything** ("No evidence he took anything. He said he wouldn't."), and Meridian's grievance is **the competition itself** ("It's the competing itself we object to"). (4) On everything else the client has no additional information; the remaining unknowns are flagged in §8 and `QUESTIONS.md`.

---

## 4. Analysis

### 4.1 Which law applies, and why

**Both states use the same test, so the clause is analyzed identically whichever court sits.** Texas applied Restatement (Second) of Conflict of Laws §187 in *DeSantis v. Wackenhut Corp.*, 793 S.W.2d 670 (Tex. 1990) (`library/desantis_v_wackenhut.md`); California follows §187 in *Nedlloyd Lines B.V. v. Superior Court*, 3 Cal.4th 459 (1992) (`library/nedlloyd_v_superior_court.md`). Under §187(2) the chosen law applies **unless** (a) the chosen state has no substantial relationship to the parties/transaction, **or** (b) application of the chosen law would be contrary to a **fundamental policy** of a state with a **materially greater interest** that would supply the law absent the clause (`library/restatement_187.md`).

- **Prong (a) probably does not help Zhao.** Texas has a substantial relationship: Meridian's HQ, the offer issued by Austin HR, the chosen law, the chosen forum. Assume this prong fails.
- **Prong (b) is where Meridian loses.** California's policy against employee non-competes is expressly "fundamental" (`library/application_group_v_hunter.md`), and it has been codified and *hardened* since 1998: §16600(b)(1) now directs broad reading in line with *Edwards* and voids non-competes "no matter how narrowly tailored" (`library/cal_bpc_16600.md`), while §16600.5(a)–(b) makes the voidness apply "regardless of where and when the contract was signed" and forbids attempts to enforce "regardless of whether the contract was signed and the employment was maintained outside of California" (`library/cal_bpc_16600_5.md`). Those two clauses are the California Legislature's own assertion of a materially greater interest, aimed at exactly Meridian's fact pattern.
- **The mirror image of *DeSantis* is the problem.** In *DeSantis* the Texas Supreme Court **refused to honor a Florida choice-of-law clause** in a non-compete because the state where the employee worked (Texas) had the materially greater interest and a fundamental contrary policy. A California court applying *Nedlloyd* + *Application Group* will run that same machine in reverse and land on §16600. A Texas court applying *DeSantis* is being asked to distinguish its own precedent — it can do so (Zhao worked in California, not Texas; in *Application Group* the employee had been recruited to work **for a California employer**), but it must first explain why the materially-greater-interest state is Texas when the employee lived, worked, and will compete in California for the entire two years.
- **§188 contacts are split, but the center of gravity is California:** residence and place of performance (24 of 24 months) = CA; place of contracting = mixed (offer issued from Austin; executed electronically in CA); employer domicile = TX; locus of the alleged competitive injury = CA; the restraint's entire geographic target includes CA.
- **The decisive point is that §187 is not the only route.** Cal. Lab. Code §925(b) makes §14 **voidable by Zhao**, and once voided at his request, "the matter shall be adjudicated in California and **California law shall govern the dispute**" (`library/cal_lab_925.md`). That is a statutory assignment of law and forum that does not depend on winning the §187 argument. See §4.3.

**How confident can this estimate be?** The choice-of-law question cannot be resolved inside this library — it has no case applying §925 (or §16600.5) to an out-of-state employer of a California-resident remote employee, and no recent Texas §187 non-compete case. My staged estimate: **P(California law) ≈ 87.5%** (sensitivity 70%–98%). It is not higher because prong (a) probably favors Meridian, no library authority extends §925 to a Texas-headquartered employer, and Texas courts do not surrender their choice-of-law clauses happily. It is not lower because §925's text is not expressly limited to California-domiciled employers, §16600.5(b) was drafted to defeat the extraterritoriality argument, *Nedlloyd* supplies the shared §187 framework both states apply (its file in this library records no holding actually displacing a Texas clause), and Zhao personally resides, works, and competes in California. Even under Texas law, Meridian's realistic best case is a temporary injunction that California courts will refuse to enforce (`library/tx_jurisdiction_note.md`) — a pyrrhic "win."

**Conclusion:** build on California law. My working probability is **87.5%** (grid: 70%–98%); "substantially more likely than not" understates it and "certain" overstates it. Any litigation plan should be built on that assumption, not on §14.

### 4.2 Enforceability under each law

**Under California law (most likely applicable): §8 is void.**

- §16600(a) voids every contract restraining "a lawful profession, trade, or business of any kind," and (b)(1) requires it be "read broadly, in accordance with *Edwards*," voiding any employment non-compete "no matter how narrowly tailored" that does not satisfy a statutory exception (`library/cal_bpc_16600.md`).
- *Edwards v. Arthur Andersen LLP*, 44 Cal.4th 937 (2008) (`library/edwards_v_arthur_andersen.md`) forecloses the intuitive argument that a field-specific carve-out is a "narrow restraint": "Noncompetition agreements are invalid under section 16600 in California even if narrowly drawn, unless they fall within the applicable statutory exceptions." *Edwards* expressly disapproved *Campbell v. Board of Trustees*, 817 F.2d 499 (9th Cir. 1987) and *General Commercial Packaging*, 126 F.3d 1131 (9th Cir. 1997) — both of which are in this library flagged **superseded** and must not be argued (`library/campbell_v_stanford_1987.md`, `library/general_commercial_packaging_1997.md`).
- *Ixchel Pharma v. Biogen*, 9 Cal.5th 1130 (2020) closes the other door: the rule of reason applies to **business-to-business** restraints; the employment context is governed by *Edwards* and non-competes are void (`library/ixchel_v_biogen.md`). §8 is squarely an employment restraint.
- **Residual uncertainty, flagged:** §16600 voids restraints "[e]xcept as provided in this chapter," and the chapter's exceptions (sale of business/dissolution-type carve-outs) are **not in this library**. Nothing in our facts suggests one applies (Zhao sold no interest), so this is a formality, not a route. I also cannot state with library support whether §9 (12-month non-solicit) is void; *Edwards*'s library summary addresses non-competition agreements, and §16600(b)(1) speaks to noncompete clauses. Treat §9 as at material risk but unresolved, and note that if it functions as a de facto restraint on taking the Kestrel role it invites the same §16600.5 exposure.

**Under Texas law (the fallback Meridian is hoping for): §8 clears the threshold and then probably fails on scope — and the statutory remedy is reformation with no pre-reformation damages.**

- **Ancillary element — probably satisfied.** §§15.50(a) requires the covenant be "ancillary to or part of an otherwise enforceable agreement at the time the agreement is made" (`library/tex_bcc_15_50.md`). *Light v. Centel Cellular*, 883 S.W.2d 642 (Tex. 1994) set the two-part test but its **timing** requirement was overruled/modified by *Sheshunoff* (`library/light_v_centel_1994.md`, status: **modified** — and the library expressly warns it "should not be cited for the proposition that a unilateral at-will agreement cannot support a covenant"). *Sheshunoff Management Services v. Johnson*, 209 S.W.3d 644 (Tex. 2006) holds the covenant is enforceable where the employer's promise (e.g., to provide confidential information) is **performed**, even if not performed at contracting, and redirects the "core inquiry" to §15.50 reasonableness (`library/sheshunoff_v_johnson.md`). *Marsh USA v. Cook*, 354 S.W.3d 764 (Tex. 2011) rejected a narrow "give rise" requirement and accepted consideration reasonably related to protecting goodwill (`library/marsh_usa_v_cook.md`). So §10's confidentiality/invention promises, performed, likely get §8 past the ancillary gate. **This is Meridian's best Texas point and it only gets to the second question.**
- **Reasonableness — the likely failure.** §15.50(a) requires limitations as to **time, geographical area, and scope of activity** that are reasonable and impose "no greater restraint than is necessary" to protect the promisee's goodwill. §8 is 24 months × the entire United States × the entire field of warehouse-logistics AMRs, for one perception engineer, with no carve-out for non-competing work. Under §15.51(b), **Meridian bears the burden** because the agreement's primary purpose is personal services. A restraint covering an entire industry nationwide, entered on a form with no negotiated confidentiality-specific consideration tied to Zhao, is on its face broader than "necessary."
  - *Flagged as unverified:* **this library contains no Texas case assessing a 24-month, nationwide, industry-wide restraint.** My conclusion that the scope is unreasonable is an inference from the text of §15.50(a), not a cited holding. Do not let it be presented in a brief as case-supported on this library.
- **Remedy ceiling even if Meridian wins:** §15.51(c) — the court **shall reform** an over-broad covenant and enforce it as reformed, **but may not award damages for breach before reformation**. So the Oct. 13 start at Kestrel generates **no damages** in the branch where Meridian "wins" by reformation. §15.52 makes §§15.50–15.51 procedures and remedies **exclusive and preemptive** of other criteria, which also forecloses laundering the claim as a common-law restraint-of-trade or choice-of-law-breach theory.
- §8's clock: termination 2026-09-30 → 24 months runs to **2028-09-30**; a reformed 12-month covenant would end **2027-09-30**, and 25 days (≈3.4% of the period) have already run. Texas courts cannot give the time back.

### 4.3 Cal. Lab. Code §925 — the clause that ends the plan

Every element is satisfied on Meridian's own documents (`library/cal_lab_925.md`):

| §925 element | Fact | Assessment |
|---|---|---|
| Employer "require[s]" the provision **as a condition of employment** | Standard form for all engineers; sent 9:12 a.m., signed 11:05 a.m.; "no negotiation" | Met |
| Employee "**primarily resides and works in California**" | Offer states "fully remote from California"; two years of Oakland work; two short trips | Met |
| Provision requires adjudication **outside California** of a claim arising in California | §14 exclusive Travis County forum | Met |
| Provision **deprives** the employee of California's substantive protection | §14 chooses Texas law over §16600 | Met |
| §925(f): contract entered/modified/extended **on or after 1/1/2017** | Executed 2024-03-04 | Applies |
| §925(e) exception: employee "**in fact individually represented by legal counsel** in negotiating" the venue/choice-of-law terms | HR file: "no counsel involved"; nothing requested or offered | **Exception unavailable.** §15's recital of an "opportunity" to consult counsel is not actual representation, and is contradicted by Meridian's own HR note in the same exhibit. Representation retained in 2026 does not retroactively satisfy a formation-date test. |

**Consequences.** §925(b): the offending provisions are **voidable by the employee**, and if voided at his request "the matter shall be adjudicated in California and California law shall govern." §925(c): a court **may** award Zhao fees for enforcing §925 rights. Zhao has already stated, through counsel, that he will void both the forum and choice-of-law clauses.

**Knock-on effect on jurisdiction.** Our own practice note is candid: the forum clause "generally supplies consent to personal jurisdiction; **but if the clause is voided under Cal. Lab. Code §925** at the employee's election, the Texas court must find **independent minimum contacts**," and "two short business trips to Austin and a contract with a Texas employer **may or may not suffice**" (`library/tx_jurisdiction_note.md`, citing Tex. Civ. Prac. & Rem. Code §17.042 and *Michiana Easy Livin' Country v. Holten*, 168 S.W.3d 777 (Tex. 2005)). So losing §925 does not just move the case — it may mean Meridian cannot even hale Zhao into Travis County.

**The one real defense here, and its limits:** §925's text is not expressly limited to California-domiciled employers, and this library contains **no authority** on whether §925 reaches a Texas employer of a California-resident remote employee. That is a genuine open question and I cannot verify it in the library. Relatedly, the firm's 2024 memo relies on *Westbrook Systems v. Ng* for the proposition that §16600.5 lacks extraterritorial reach over out-of-state employers — but (i) that case is **not in this library**, (ii) the firm's own 2025 memo records that the Ninth Circuit **granted rehearing en banc** (argued Jan. 2025) with **no disposition in our file**, and (iii) §16600.5(b) is drafted to negate exactly that argument ("regardless of whether the contract was signed and the employment was maintained outside of California"). Treat the extraterritoriality defense as a lottery ticket, not a plan.

### 4.4 §16600.5 exposure — suing creates the liability

`library/cal_bpc_16600_5.md`:

- **(c)** "An employer shall **not enter into** a contract with an employee or prospective employee that includes a provision that is void under this chapter." Meridian did that in March 2024 — **already complete, before any lawsuit.**
- **(b)** An employer "shall **not attempt to enforce**" a void contract, regardless of where signed or where employment was maintained. Filing in Travis County *is* the attempt. So is a demand letter that threatens §8 (reading; the library does not define "attempt").
- **(d)** Entering into **or** attempting to enforce a void contract "commits a **civil violation**."
- **(e)(1)** Zhao may bring a **private action** for injunctive relief and/or actual damages. **(e)(2)** a prevailing employee "**shall** be entitled to recover reasonable attorney's fees and costs" — **mandatory**, not discretionary.

Two features make this asymmetric. First, **the clock runs against Meridian from the filing date**: it cannot settle out of the exposure by declining to win; declining to *file* is the only thing that caps it. Second, **continuing** to prosecute after §925 voids §14 is itself an ongoing "attempt to enforce."

**Company-wide.** §8 is the **standard form for all engineers**. Every California-resident engineer hired on that form since §16600.5 took effect on 1/1/2024 has the same (c) claim, and — if they were current employees on 2024-02-14 — the same notice claim. Zhao is one instance of a program defect, and a public lawsuit is the most likely way the rest of the population learns about it. **Quantifying this requires headcount data we do not have** (QUESTIONS.md Part II item 4).

*Flagged:* whether Zhao's §16600.5(e)(1) "actual damages" are anything beyond nominal for an employee who simply kept working are unknowable here; the **fee award**, not damages, is the driver. Also flagged: the library does not contain the text of Bus. & Prof. Code §17200 or its remedies, so I cannot opine on UCL remedies beyond §16600.1(c)'s incorporation (below).

### 4.5 AB 1076 / §16600.1 notice — a real problem, with one genuine wrinkle

`library/cal_bpc_16600_1.md`:

- **(a)** "It shall be **unlawful to include a noncompete clause in an employment contract**, or to require an employee to enter a noncompete agreement, that does not satisfy an exception." Subdivision (a) has **no date qualifier**. Zhao's contract includes §8. That is a violation on the face of the statute, and (c) makes it "an act of unfair competition within the meaning of" §17200. This limb is **not** cured by notice and does **not** depend on the notice project.
- **(b)(1)** The **notice** duty runs to "**current employees**" and "former employees who were employed after January 1, 2022," and was due "**by February 14, 2024**," in individualized writing to last known mailing **and** email addresses.
- **The wrinkle — and it is narrower than it looks.** Zhao was **not** an employee on 2024-02-14: the offer is dated 2024-02-28 and the agreement took effect 2024-03-04. He was therefore neither a "current employee" on the deadline date nor a "former employee employed after January 1, 2022" at that time. On the text in this library, the **February 14, 2024 notice obligation arguably never attached to Zhao**, and the library contains **no authority** resolving whether §16600.1(b) creates an ongoing notice duty for employees hired *after* the deadline. That is the *only* place Meridian has a defense in this whole file, and it is narrow:
  1. It defends **only** the (b) notice limb — not (a), and not §16600.5.
  2. It **cuts against** Meridian elsewhere: for any California engineer who *was* a current employee on 2024-02-14 and had §8 in their contract, the LO-233 "deprioritized" decision is a clean, documented (b) violation → (c) unfair competition. **Meridian's exposure is to that population, not to Zhao.**
- **The documents are the problem — now worse.** LO-233 records that legal identified the obligation and the company chose to deprioritize it; the client's 10/25 answer confirms the notices were **never sent to anyone** and the ticket was **closed "won't do."** That is not a missed deadline; it is a documented, knowing decision not to comply. In a fee-and-unclean-hands narrative, it is the worst kind of exhibit. Two immediate operational consequences: (i) **litigation-hold LO-233 and the notice project now** — do not let anyone "clean up," re-word, or close anything; (ii) do not let the "won't do" decision travel into a filing.

**Remediation judgment call (needs your decision, not mine):** sending §16600.1(b)-style notices now to current and qualifying former California employees is cheap, is the conduct the statute asks for, and mitigates; but it also memorializes that §8 is void in California and hands California-resident engineers a roadmap. My recommendation in §6 is to send them, and to stop using §8 for California-resident hires immediately — the (a) limb keeps accruing with every new California hire on the form.

**Your 10/25 instruction to keep LO-233 out of writing — how I am handling it, and why I cannot handle it as asked.** I will not omit the LO-233 facts from this memo, and I will not soften "won't do" to "deprioritized": (1) **the fact already exists in writing** — in the ticket itself and in your own 10/25 email — so leaving it out of the analysis does not hide it, it just leaves the company holding a memo that understates its own exposure (and a lawyer who did not say what she knew); (2) **deleting, re-wording, or "cleaning up" the ticket is off the table** — that converts a curable compliance gap (un-sent notices: expensive, fixable) into evidence-destruction and credibility problems that no budget fixes; the litigation hold stands and LO-233 is frozen exactly as it is; (3) what your concern legitimately points at is *new* paper: keep further discussion of the decision inside privileged channels (this memo and our correspondence are legal advice; privilege protects the advice, **not the underlying facts** — LO-233 remains discoverable), and do not generate new business-records chatter re-litigating why the notices were skipped. Note that the instruction itself arrived by email: the instinct is right in general and too late in particular. The move that actually reduces this exposure is remediation (notices + form change), not documentation management.

### 4.6 Remedies and fee exposure

**What Meridian can realistically get, even in its best branch** (path shares; the full outcome tree and arithmetic are §7.1):

| Path | P | What happens on it |
|---|---|---|
| California law applied — via §925 election or §187 | 87.5% | §8 void as to Zhao in 90% of these (≈79% of all scenarios); no relief; Zhao's §16600.5 claims live; §925(c) discretionary fees to Zhao |
| Texas law applied | 12.5% | Ancillary gate probably cleared (*Sheshunoff*/*Marsh*); Meridian bears the reasonableness burden (§15.51(b)); reformation is the statutory remedy (§15.51(c)); **no damages before reformation**; any order still faces non-recognition in California |
| — of which Meridian actually obtains **usable** relief (interim or job-affecting order) through the Texas branch | ≈0.7% of all scenarios (0.125 × 5.4%; the §7.1 total across both branches is 3.1%) | see §7.1 |
| §14 voided and no independent minimum contacts | ≈2% (judgment estimate; not part of the §7.1 probability tree) | dismissal for want of jurisdiction |

- **Injunction:** requires an independently enforceable covenant plus irreparable harm. Zhao has affirmatively stated he will honor confidentiality and take nothing; there is **no trade-secret misappropriation allegation in this file**. (Note: trade-secret law is **not in this library** — no UTSA/DTSA — so any such claim must be researched before anyone drafts it; I express no view.)
- **Damages:** barred before reformation by §15.51(c). Zhao's actual competitive harm to Meridian is speculative.
- **Fees:** the agreement excerpt contains **no prevailing-party fee clause**, so Meridian has no contractual fee route. §15.52 makes §§15.50–15.51 remedies exclusive. Zhao, by contrast, has **two** statutory fee bases: §16600.5(e)(2) (mandatory) and §925(c) (discretionary). The fee-shifting is strictly one-directional.
- **Delay already incurred:** 25 days have passed since termination and ~12 days since the Kestrel start. Emergency relief depends on showing immediate, irreparable injury; a plaintiff who waits through the start date invites the response that the harm is neither imminent nor irreparable. (General practice point; no library authority speaks to it.)
- **Personal jurisdiction:** only if §14 survives; otherwise Meridian must prove minimum contacts on two short trips (`library/tx_jurisdiction_note.md`).
- **Parallel-litigation reality:** *Advanced Bionics Corp. v. Medtronic*, 29 Cal.4th 697 (2002) says California courts should **generally not enjoin a party from litigating in another state's courts** (`library/advanced_bionics_v_medtronic.md`). To be fair to the pro-filing view: this means Zhao probably cannot simply enjoin Meridian out of Travis County, so a Texas case can be kept alive. But *Advanced Bionics* "does not retreat from §16600's policy," and a Texas injunction "would in any event face non-recognition in California on public-policy grounds" (`library/tx_jurisdiction_note.md`). The realistic product is not leverage — it is **Meridian funding two courts to litigate the same clause to the same result.**

**No federal shield.** The FTC Non-Compete Rule is **vacated** — set aside nationwide in *Ryan LLC v. FTC*, 739 F. Supp. 3d 496 (N.D. Tex. 2024); the FTC dismissed its appeal in September 2025; it never took effect (`library/ftc_noncompete_rule_16cfr910.md`, status **vacated**; `library/ryan_llc_v_ftc.md`, in force). It cannot be cited for anything except the fact that it is gone. **Correction to the file:** the 2025 firm memo says "the FTC rule [was] **enjoined**." That is wrong and it matters — vacatur under the APA erases the rule; an injunction binds only the parties. Whoever relied on "enjoined" in another matter should be corrected. (The 2025 memo's bottom line — state law controls — is right.)

---

## 5. The strongest argument for each side

**Meridian's best case.** (1) §187(2)(a) is satisfied and prong (b) is not: this is not *Application Group*, where the employee had been recruited to work **for a California employer in California**; Zhao contracted with a Texas employer whose goodwill, HQ, and competitive stake sit in Austin, and §188's place of contracting points to Texas. *DeSantis* protects the policy of the state with the greater interest — and a Texas court is entitled to ask whether California's interest is materially greater than Texas's merely because the employee chose where to live. (2) *Application Group* predates SB 699, and §16600.5's extraterritorial reach is contested (*Westbrook*, per the firm's own file, under en banc review) — so the statute doing the work is not settled law. (3) On the merits, *Sheshunoff* and *Marsh USA* clear the ancillary gate, §15.51(c) makes **reformation** the statutory answer rather than invalidation, and no Texas statute caps 24 months or nationwide geography. (4) §15 recites an opportunity to consult counsel. (5) *Advanced Bionics* means California should not enjoin the Texas suit.

*Why it still loses:* points 1 and 2 are unverifiable in this library; point 3 gets to the merits only to reach a reasonableness problem under §15.50(a) on a burden Meridian carries (§15.51(b)), with damages foreclosed pre-reformation; point 4 is contradicted by Meridian's own HR note — and now by the client's own 10/25 confirmation ("nobody negotiates," same-day signing, form-wide), so it evidences the §925(e) problem for **every** engineer instead of curing it for any; and point 5 buys forum, not outcome.

**Zhao's best case.** (1) §925(a)–(b) is a statutory kill shot on §14 built out of Meridian's own documents — offer letter ("fully remote from California"), HR file ("standard form," "no negotiation," "no counsel involved"), executed 2024 — and §925(e) is unavailable because he was not **in fact** individually represented in negotiating §14. Void §14 and California law and a California forum follow by statute, with a discretionary fee award under §925(c). (2) §16600(a) + (b)(1) + *Edwards* void §8 "no matter how narrowly tailored"; *Ixchel* bars the rule-of-reason recharacterization; *Campbell* and *General Commercial Packaging* are dead. (3) §16600.5(a)–(b) removes "you signed it in Texas / employment was in Texas" from the argument. (4) §16600.5(b)+(d) convert Meridian's own lawsuit into a civil violation with **mandatory** fees. (5) §16600.1(a) makes including §8 unlawful *per se*, actionable as unfair competition. (6) And Meridian has now conceded in writing the two facts that drain any residual case: **no evidence he took anything**, and the objection is "**the competing itself**." Under §16600 as amended, competing is not a cognizable injury — so on the client's own framing of its grievance, there is nothing for a court to award.

---

## 6. Recommendation

1. **Do not file in Travis County. Do not assert §8.** Probability of usable relief ≈ 3% (1.5%–7.2%); probability of relief that actually stops the Kestrel job <1% (0.3%–2.0%); probability of creating §16600.5 liability by filing ≈ 85% (65%–97%); expected net cost ≈ −$540k (−$230k to −$800k). Even the "deterrence" rationale is thin: a case this likely to be dismissed on jurisdiction and choice of law does not deter other engineers; a fee award against Meridian that other engineers' counsel read about does the opposite.
2. **Do not send a §8 demand or cease letter.** Under §16600.5(b), the threat is the violation. If a letter has already gone out, tell me today — it changes the exposure analysis (§8 item 2; QUESTIONS.md Part II item 1).
3. **Protect what is actually protectable — and nothing more.** Enforce §10: written recall/certification-of-deletion demand for Meridian data and devices, device-return audit, revoke access. The client has now confirmed there is **no evidence Zhao took anything**, so a trade-secrets claim has no factual predicate today and should not be pleaded or threatened; if the audit unexpectedly surfaces egress evidence, that is a separate engagement (trade-secret law is not in this library). What Meridian actually objects to — "the competing itself" — is not a legally cognizable injury in California, and no filing can monetize it.
4. **Do not build a case around §9 either.** Its California status is unresolved on this library, and asserting it as a stand-in for §8 re-creates the same §16600.5 exposure.
5. **Stop using the §8 form for California-resident hires — today.** The client has confirmed the form is uniform, same-day, never-negotiated company-wide: there is no defensible negotiated variant anywhere in the population, so the "case-by-case" instinct does not save it. Every California hire on this form is a fresh §16600.5(c) violation. Substitute confidentiality, invention-assignment, non-solicit where lawfully usable, and — for future Texas-based hires only — a genuinely ancillary, role-tailored covenant with real consideration and real time to review. (Paid notice-period/"garden leave" structures are **not** covered by this library; flag if you want that analyzed.)
6. **Send the §16600.1-style notices** to current California employees and qualifying former employees (employed after 1/1/2022) whose contracts contain §8, by individualized writing to last known mailing **and** email address; document it; and re-open LO-233 with a compliance record replacing the "won't do" closure. The client has confirmed **no notice was ever sent to anyone**, so the (b) violation is complete and documented for every California engineer who was current on 2024-02-14; late notices do not undo (b), but they stop it compounding and they are the cheapest mitigation on the table. On Zhao specifically the duty arguably never attached (he was hired after 2/14/2024) — that narrow wrinkle is the *only* thing separating him from the population, and the (b) exposure lives with the population.
7. **Litigation-hold and preserve**: LO-233 **exactly as it stands, including the "won't do" closure** (no edits, no "cleanup," no re-wording — see §4.5), the notice project, the DocuSign metadata (9:12 a.m./11:05 a.m. is already in your own file), the "standard form for all engineers" template history, and the §15 recital's drafting history. Nothing gets deleted. Route all further discussion of the notice decision through counsel (this memo and our correspondence are privileged; the underlying ticket is not, and will not become so by silence).
8. **Quantify the population.** Report: number of California-resident engineers on the §8 form, by hire date relative to 2024-02-14 and 2024-01-01, and whether any §8 has been asserted or a notice sent for them. Exposure per §7 is roughly linear in that headcount.
9. **Audit the two internal memos.** They are background, not authority; the authorities inside them (*Calderon*; *Westbrook*) are **not in this library** and *Westbrook* was, as of the last entry in the file, under **en banc rehearing with no recorded disposition**. The 2024 memo's recommendation of suit "in the Alvarez matter" rests on those cases — please confirm Alvarez's status, because if Meridian sued there, the §16600.5 analysis above may already be live on an existing docket.
10. **Rebuild the memo bank**: correct "enjoined" → "vacated/set aside nationwide, never took effect"; obtain the *Westbrook* en banc disposition; label *Calderon* and *Westbrook* unverified until pulled and Shepardized by someone with a subscription.

**If you decide to file anyway** (I advise against it): file, do not serve a demand letter first; brief §925 and personal jurisdiction up front rather than assuming §14 carries the day; plead §10 confidentiality claims as the primary theory and §8 as a reformation claim under §15.51(c); budget ~$250–500k; and expect a California cross-action within weeks.

---

## 7. The arithmetic

Inputs are **stated estimates**, not library facts, and are labelled as such. Money inputs are illustrative planning figures with no support in this library; correct them with your budget data.

**7.1 Probability tree (two stages: choice of law, then outcome on the merits)**

Stage 1: `P(California law governs §8) = 0.875` (range 0.70–0.98; §4.1), `P(Texas law) = 0.125`.

Stage 2 — outcomes are exhaustive within each branch and sum to 100%:

| Outcome | if CA law (87.5%) | if TX law (12.5%) |
|---|---|---|
| §8 void / unenforceable as to Zhao (§16600 per se + *Edwards*/*Ixchel*; in TX: overbroad nationwide covenant) | 90.0% | 87.7% |
| Enforced but unreasonable → reformed, no interlocutory relief | 7.2% | 6.9% |
| Enforced but unreasonable → reformed, temporary relief, then loses at final | 1.8% | 1.7% |
| 24-month nationwide covenant held "reasonable" but the order does not end the Kestrel job | 0.5% | 1.8% |
| Injunction that actually ends the Kestrel job | 0.5% | 1.8% |
| **usable relief to Meridian (interim or job-affecting order)** | **2.8%** | **5.4%** |

"Usable relief" counts an interlocutory order or a final ruling holding the covenant enforceable, whether or not it ends the job. A reformation-only ruling (row 2) is technically a court order too, but it gives Meridian nothing it can use while Zhao works at Kestrel — which is why §7.3's no-practical-relief row is 96.9%, not 90%. (The TX column's rounded rows sum to 99.9%.)

```
P(usable relief)     = 0.875 x 0.028 + 0.125 x 0.054  = 0.025 + 0.007  = 3.1%
P(order ends job)    = 0.875 x 0.005 + 0.125 x 0.018  = 0.0044 + 0.0023 = 0.7%
```

Branch inputs are themselves estimates: P(enforced | CA law) = 10% (generous to Meridian — under *Edwards* and *Ixchel*, and §16600 as amended in 2024, a lower number is defensible); P(enforced | TX law) = 12.3%; P("reasonable" | enforced) = 10% under CA law / 30% under TX law; P(order actually ends the job | "reasonable") = 50% in both branches; P(interim relief | enforced but not "reasonable") = 20% in both branches. The sensitivity columns scale the **CA branch only**; the TX branch is fixed.

Sensitivity grid — `P(usable relief | filing)`, with `P(order ends job)` in parentheses; rows = P(CA law), columns = P(enforced | CA law), with P(reasonable | enforced) pushed to 20% at the most Meridian-friendly corner:

| pCA \ enf | 5% | 10% (base) | 20% + "reasonable" pushed to 20% |
|---|---|---|---|
| 0.70 | 2.6% (0.7%) | 3.6% (0.9%) | 6.7% (2.0%) |
| **0.875** | 1.9% (0.4%) | **3.1% (0.7%)** | 7.0% (2.0%) |
| 0.98 | 1.5% (0.3%) | 2.9% (0.5%) | 7.2% (2.0%) |

Across the full grid: **P(usable relief) 1.5%–7.2%; P(order that ends the Kestrel job) 0.3%–2.0%; P(Meridian loses on §8, any theory) never below 92.8%.** **Ranges carried into the Brief Answer: ~3% (1.5%–7.2%) for usable relief; under 1% (0.3%–2.0%) for relief that actually works.**

**7.2 Exposure if Meridian files**

```
(a) §16600.5 "entered/include" violation re Zhao: already complete before
    any suit is filed.      P = P(CA law)                    = 87.5%
(b) §16600.5 "attempted to enforce" violation: created the moment
    Meridian files (or serves a §8 demand letter).
    P = P(CA law) x P(no practical relief | CA)
      = 0.875 x 0.972                                        = 85.0%
P(CA-law exposure across grid)                                = 65%-97%
      corners: 0.70 x (1-0.072) = 65.0%  |  0.98 x (1-0.014) = 96.6%
```

Zhao will assert these even if Meridian never files a §8 count: suing first in Texas does not make the California claim optional for him — a California lawyer's reflex is to file the §16600.5 claim, not waive it. Practical P(an affirmative California claim is adjudicated) ≈ (b) ≈ 85%.

**7.3 Cost/benefit of filing (all $ figures are planning assumptions, not library facts)**

| Scenario | P (unconditional) | Net cost | Stack |
|---|---|---|---|
| No practical relief | 96.9% | −$532k | own fees 220 + Zhao's mandatory fee award 240 + §16600.5 exposure 30 + lost engineering time 30 + misc 12 |
| Some order, no practical benefit (longer fight, ends in settlement) | 3.1% | −$652k | fees 350 + 240 + 30 + opportunity 20 + misc 12 |

```
EV(filing) = 0.969 x (-532) + 0.031 x (-652) = -515.5 - 20.2 = -$535.7k  -> ~-$540k
optimistic (fees 160k, early settlement, no fee award):        -$232k
pessimistic (fees 300k + Zhao 400k + exposure 60k + 12 + 30):  -$802k
```

Even the modeled "wins everything" branch does not pay: the 1% × $15M lost-profits theory is worth +$150k, less retained comp $212k, fees $150k, opportunity $8k = **−$220k even on a total win**. Filing never gets close to breaking even on any plausible input, and the §16600.5 fee award to a prevailing employee is **mandatory**, not discretionary.

**7.4 Pattern exposure (headcount unknown)**

Per California-resident engineer on the §8 form, assume $20k–$60k resolution value (§16600.5 claims are fee-driven, so this is crude):

| N engineers | at $20k | at $60k |
|---|---|---|
| 5 | $100k | $300k |
| 12 | $240k | $720k |
| 25 | $500k | $1,500k |

**Post-confirmation calibration (10/25).** The client's answers removed every fact that could have mitigated this table on a contract-by-contract basis: the form is uniform and never negotiated ("nobody negotiates"), so no engineer's §8 was individually bargained (§925(e) is out for the whole population); and LO-233's "won't do" closure is a written, knowing non-compliance record as to (b). For planning, **treat the $60k column as the working number**, not the optimistic one. Headcount remains unknown — the client reports no additional information — so this table stays illustrative and linear in N; pull N from HR records (hire date vs. 2024-01-01 and 2024-02-14) rather than from anyone's recollection.

**7.5 Dates**

```
§8 period if enforced as written : 2026-09-30 + 24 months = 2028-09-30
§8 if reformed to 12 months      : 2026-09-30 + 12 months = 2027-09-30
Days elapsed as of 2026-10-25     : 25 days = 3.4% of the 24-month period
```

**Not reconciled, deliberately:** I have not forced 7.4 into 7.3, because 7.4 depends on headcount we do not have and on whether a public filing triggers the other employees' claims at all. Both numbers are left open.

---

## 8. Assumptions, and what I could not verify

**Assumptions as of 2026-10-25, after the client's answers (answer history in `QUESTIONS.md`):**
1. **STILL UNCONFIRMED — Zhao's Kestrel start.** He began work at Kestrel on or about 2026-10-13 (per the HR timeline) and Kestrel designs/sells warehouse-logistics AMRs (so §8 is facially implicated). The client could add nothing; the assumption survives by default from the HR file.
2. **STILL UNCONFIRMED — no demand letter has been sent.** I flagged this as the file's most urgent question (Q2); the client did not answer it. Meridian's Travis County HQ is assumed from the documents. **If a §8/§9 demand ever went out, §7.2's exposure is not prospective — it already accrued**, and the advice shifts from "don't file" to "don't make it worse, and remediate the letter."
3. **STILL UNCONFIRMED — fee/arbitration clauses.** The excerpt is assumed complete as to fee-shifting (no prevailing-party fee clause anywhere in the full agreement). A mutual fee clause would resize §7.3; an arbitration clause would change §4.1's forum math.
4. **STILL UNCONFIRMED — no pre-2024 Meridian employment.** Zhao had no earlier Meridian contract that §8 was added to (the documents' first engagement is 2024-02-28/03-04). If wrong, the §16600.1(b) timing wrinkle in §4.5 — the *only* defense in this file — collapses for Zhao too, because he would then have been a "current employee" on 2024-02-14.
5. ~~Assumption~~ **CONFIRMED 10/25 — no evidence of taking:** "No evidence he took anything. He said he wouldn't. It's the competing itself we object to."
6. **NEWLY CONFIRMED facts (now in §3, no longer assumptions):** the §8 form is uniform, same-day, never-negotiated company-wide ("nobody negotiates"); no §16600.1(b) notice was ever sent to anyone; LO-233 was closed "**won't do**"; Meridian's grievance is the competition itself.

**Things I believe but could NOT verify in this library — labelled, not cited:** the §16600 statutory exceptions; the text and remedies of Bus. & Prof. Code §17200; any Texas case on the reasonableness of a 24-month nationwide industry-wide covenant; whether §925 or §16600.5 apply to an out-of-state employer of a California-resident remote employee; whether "attempt to enforce" includes a pre-suit demand; whether §16600.5(e)'s private action reaches a §16600.1(a) violation ("this chapter"); the California status of customer/employee non-solicitation clauses; trade-secret law; standards for TRO/TPI, anti-suit injunctions, or forum non conveniens; all limitations periods; and *Calderon* and *Westbrook* (not in the library at all).

**Authority-status audit of what I relied on:** *Campbell* (superseded by *Edwards*), *General Commercial Packaging* (superseded by *Edwards*), and the FTC Rule (vacated, *Ryan*) are discussed **only** for the proposition that they are no longer available; *Light v. Centel* (modified by *Sheshunoff*) is discussed only for its ancillary test with the timing holding disclaimed. Every other authority relied on is marked in force in `library/INDEX.md`. Full mapping in `citations.json`.

## Appendix A — Answers to Dana's follow-up (2026-10-25)

**"Our outside counsel's 2024 memo says *Calderon* and *Westbrook* support exactly this. Why aren't you relying on them?"**

Because of what they are, what they'd say, and what happened to them since 2024.

1. **Neither case is in this library.** They exist only as citations *inside* the firm's own 2024 memo — which the engagement rules make background, not authority. I cannot read them, confirm they exist as cited, check what they actually hold, or check their subsequent history. This is a lawsuit where the downside branch is **mandatory** fee-shifting (§16600.5(e)(2); §925(c) fees are discretionary but also available); "a case I cannot read" is not a basis on which to file.
2. ***Westbrook* is pending — the firm's own 2025 memo says so.** The 2025 update records the Ninth Circuit's grant of rehearing **en banc** (argued Jan. 2025) with **no disposition in our file**, and keeps the 2024 position only "pending further guidance." A granted en banc rehearing ordinarily vacates the panel disposition (flag: that procedural rule is outside this library). Either way, outside counsel's current *written* position is "our view awaits further guidance" — a hedge, not support. Twenty-one months after the en banc argument (argued Jan. 2025; today is Oct. 2026), nobody in this file knows whether the holding survived.
3. **Taken at face value, they don't get you where you need to go.** *Westbrook*'s reported holding — §16600.5 lacks extraterritorial reach over out-of-state employers — is contradicted by the enacted text I *can* read: §16600.5(a)–(b) voids the clause and penalizes enforcement attempts "regardless of whether the contract was signed and the employment was maintained outside of California." And *Westbrook* isn't even the last line of defense: it addresses §16600.5, not §925. Zhao wins his motion without ever reaching §16600.5 — §925 (by its terms not limited to California employers; nothing in this library holds otherwise) voids both of §14's clauses — choice-of-law and forum, and once California law applies, §16600/*Edwards* voids §8.
4. **The *Calderon* theory is statute-papered even if it is real.** As the 2024 memo itself summarizes it, *Calderon* (2023) enforced Texas law because a remote employee "availed himself" of Texas benefits. That consent/availment framework is exactly what §925 abolished for condition-of-employment forms: void unless the provision was **in fact** individually negotiated with counsel — and your 10/25 answer ("nobody negotiates") forecloses that exception across the entire engineer population. And a 2023 decision could not have considered §16600.5 or §16600.1, which took effect 1/1/2024.
5. **Track record in this file.** The 2024 memo recommended filing in Travis County in the *Alvarez* matter on these exact two cases — Alvarez's status is still unconfirmed (QUESTIONS.md Part II item 7), and if that suit was filed, this theory is already on a docket somewhere and its real-world performance is one docket check away (Q13). And the same memo bank gets the one federal issue in this area wrong: the 2025 memo says the FTC rule was "enjoined" when the library's own authority sets it aside vacated nationwide (*Ryan*). A memo bank that mislabels its lead authority is not a basis for leaning on cases it never attached.

**"The FTC rule is dead, so what's the problem?"**

The FTC rule was never the reason — nothing in this analysis leans on it, and I cite it once, only for the proposition that it is gone (vacated nationwide in *Ryan*, never took effect, FTC dismissed its appeal). The problem is California state law, which is **in force and untouched by** ***Ryan****:*

- **§16600(a) + *Edwards*** — §8 is void "no matter how narrowly tailored"; *Ixchel* forecloses re-importing reasonableness.
- **§16600.1(a)** — including §8 in a California employee's contract is **unlawful in itself**; that violation completed on hire.
- **§16600.5** — the Texas clause is unenforceable "regardless of whether the contract was signed and the employment was maintained outside of California," and an **attempt to enforce** is an independent civil violation with mandatory fees: the lawsuit *is* the violation.
- **§16600.1(b)** — the AB 1076 notice: never sent, company-wide, ticket closed "won't do."
- **§925** — voids the Texas choice-of-law/forum for a California-resident employee, imposed as a condition of employment, no negotiated-agreement exception here.

None of those rests on the FTC rule, so *Ryan* removed none of them. The firm's own 2025 memo has the one sentence that is exactly right: **"state law controls."** The controlling state law is California's — the most hostile in the country to this covenant, amended in 2023–24 precisely to punish employers who try to enforce out-of-state non-competes against California workers. If anything, the FTC rule's death makes Meridian's position *worse*, not better: there is no federal floor or ceiling in play at all, so it is purely California law v. this form — and California wrote its 2024 amendments with this exact fact pattern in mind.
