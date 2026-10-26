# MEMORANDUM

**To:** Meridian Robotics, Inc. (General Counsel; VP Engineering)
**From:** outside counsel
**Date:** October 25, 2026
**Re:** Enforceability of §8 (non-compete) against Wei-Lin Zhao; §§14–15 (Texas law / Travis County venue); Meridian's own exposure
**Status:** Rev. 2 — complete rewrite. Rev. 1 used a fact pattern that does not match the source documents and has been superseded in full. Facts from Meridian's answers of October 25, 2026 are labeled **[client-admitted]**.

**Correction notice, stated up front.** Rev. 1 described Zhao as based in Meridian's Austin office, signing on January 10, 2024, resigning February 24, 2026, and joining a San Jose competitor, and described §9 as a 24-month covenant and §8 as covering "any competitive business." **None of that is in the file.** The agreement excerpt, HR timeline, and resignation email establish the opposite: Zhao was hired into a role whose stated work location was his residence in Oakland, California, and he worked from Oakland for his entire tenure. That correction makes the analysis materially worse for Meridian, not better. Every figure below was recomputed from the documents.

---

## 1. Question Presented

Meridian wants to stop Wei-Lin Zhao from working for Kestrel Autonomy. Can Meridian enforce §8 of his employment agreement — 24 months, anywhere in the United States, no employment with or services to any business "engaged in the design or sale of autonomous mobile robots for warehouse logistics" — by suing in Travis County, Texas, as §14 provides?

## 2. Brief Answer

**No. Filing in Travis County is close to the worst option available, and it is worse than doing nothing.** On Meridian's own contract language, Zhao "primarily reside[d] and work[ed] in California" when he signed, which puts Cal. Lab. Code §925 directly on point and gives Zhao a statutory route to void both the Texas choice of law and the Travis County venue clause — in which case California law applies and §8 is void. On the independent Texas-law branch, Meridian's answers (standard form, same-day signature, nothing negotiated, no reciprocal employer promise) mean Meridian probably cannot carry its statutory burden of showing §8 is "ancillary to or part of an otherwise enforceable agreement," which is a threshold failure that reformation cannot fix.

Separately, and independent of anything Meridian does next, **Meridian has existing exposure of its own**: including §8 in a California employee's contract in March 2024 appears to violate Cal. Bus. & Prof. Code §16600.1(a) and §16600.5(c), and you have confirmed the AB 1076 notice was never sent to anyone.

| Question | Answer | Confidence |
|---|---|---|
| Does §925 void the §14 choice-of-law and Travis County venue clauses at Zhao's election? | Yes, most likely; ~75–90% | Medium-high |
| Will a Texas court nonetheless apply Texas law to §8? | Probably not; ~5–15% (Rev. 1's 15–25% was built on the false "he worked in Austin" premise) | Low |
| If California law applies, is §8 void? | Yes; ~95%+ | High |
| If Texas law applies, does §8 clear §15.50(a)'s ancillarity threshold? | Probably not; ~25–40% | Low-medium |
| End-to-end odds of an injunction that actually keeps Zhao out of Kestrel | **~0.3%–3%** | Low |
| Could Meridian reach Travis County at all if §14 is voided? | Contacts-only fight; ~30–50% | Low |
| Is Meridian already in violation of California law (independent of filing)? | Yes on the library text: entering into §8 and the missed AB 1076 notice | Medium-high |
| If Meridian files, odds it pays Zhao's fees or draws a §16600.5 finding | ~60–75% | Medium-high |

Bottom line: expected cost of filing is roughly **$362,000** (Section 7) against a **well under 3%** chance of the relief you actually want. Do not file, send no demand letter, and spend the next 60 days on compliance: cure the notice failure company-wide and scrub §8 from the engineer form.

## 3. Facts

All facts are from `workspace/documents/` unless labeled otherwise.

**The agreement (excerpt, effective March 4, 2024).** Position: **Senior Perception Engineer**. Work location, in the agreement itself: **"Remote — Employee's residence (Oakland, California)."**

- **§8 (Non-Competition):** "For a period of twenty-four (24) months following termination of employment for any reason, Employee shall not, anywhere in the United States, be employed by or provide services to any business engaged in the design or sale of autonomous mobile robots for warehouse logistics."
- **§9 (Non-Solicitation):** "For 12 months Employee shall not solicit Company employees or customers." (Not 24 months, as Rev. 1 stated.)
- **§10 (Confidential Information and Inventions):** standard.
- **§14 (Governing Law; Venue):** "This Agreement is governed by the laws of the State of Texas. The parties consent to exclusive jurisdiction and venue in the state and federal courts located in Travis County, Texas."
- **§15 (Acknowledgment):** "Employee acknowledges having had the opportunity to consult counsel." The agreement's own HR-file note adds: "Employee signed via DocuSign 2 hours after receipt; no counsel involved."

**Timeline (HR timeline; resignation email).**

- 2024-02-28: offer letter emailed by Austin HR to the candidate **in Oakland, CA**, stating "fully remote from California."
- 2024-03-04: agreement sent 9:12 a.m., signed by DocuSign 11:05 a.m. the same day — a **113-minute** window; "No negotiation; no attorney review requested or offered. Standard form for all engineers." Five days elapsed from offer to signature.
- 2024-03-04 → 2026-09-30: **worked from Oakland** the entire tenure. Two trips to Austin HQ: onboarding week (March 2024) and an offsite (October 2025).
- 2024-02-14 (entered in the HR timeline as a **company-wide** entry, on the day of the statutory deadline): Legal's AB 1076 notice project — "**no notice was sent to California employees**"; project "**deprioritized**" per legal-ops ticket **LO-233**. February 14, 2024 is exactly the §16600.1(b)(1) deadline.
- 2026-09-16: resignation email — resigning effective September 30, "accepted a role at **Kestrel Autonomy in Fremont**," has "consulted a California employment attorney" who advises §8 is void under California law and that he "may void the Texas forum and choice-of-law clauses," and states "I will honor my confidentiality obligations and won't take anything with me."
- 2026-10-13: started at Kestrel Autonomy (**Fremont, CA**), warehouse AMRs.
- 2026-10-02: GC asked, "Can we enforce §8? File in Austin?"

**[client-admitted, October 25, 2026]**

- §8 sits in Meridian's **standard form for all engineers**; engineers **sign the same day** it is issued; **nobody negotiates** it, and no engineer — including Zhao — was represented by counsel.
- Meridian's legal operations **never sent** the §16600.1(b) notice to **any** California employee, and the ticket was ultimately closed "**won't do**." (The never-sent fact and the "**deprioritized**" label for legal-ops ticket **LO-233** appear in the HR timeline; the "won't do" disposition is your answer of October 25.)
- Meridian has **no evidence** Zhao took anything. Meridian's objection is "**the competing itself**."

**Arithmetic we computed, shown so you can check it.**

- SB 699 and AB 1076 took effect 2024-01-01. Zhao signed 2024-03-04 = **63 days later** (31 days January + 29 days February 2024 (leap year) + 3 = 63). The statutes were in force before this contract was made.
- The §16600.1(b)(1) notice deadline was **2024-02-14**. Zhao's contract was made **19 days later** (Feb. 14 → Mar. 4 = 15 + 4 = 19).
- Tenure: 2024-03-04 → 2026-09-30 = **940 days**, about **30.9 months**. **All of it in California** by the agreement's own terms.
- §8's restraint (24 months) is **77.7%** of his tenure (24 ÷ 30.9). He would be restrained for four-fifths of the period he worked for Meridian, plus two more years.
- The restraint runs to about **2028-09-29/30**; at Kestrel's start (2026-10-13), **718 days** remained.
- As of today: Zhao has been separated **25 days** (Sept. 30 → Oct. 25), he has been at Kestrel **12 days** (Oct. 13 → Oct. 25), and Meridian has had the enforcement question in front of it for **23 days** (Oct. 2 → Oct. 25).

**Two facts that cut against Meridian and should not be argued around.** First, Kestrel Autonomy builds warehouse autonomous mobile robots — §8 covers that job on its face, so there is no "the clause doesn't reach this role" defense. Second, the document that proves Zhao was a California-resident, California-based employee at formation is **Meridian's own agreement**.

## 4. Framework

Four questions stand between Meridian and "Zhao leaves Kestrel." Each must resolve in Meridian's favor; any one failure ends it.

1. **Jurisdiction.** Can a Travis County court exercise power over Zhao? §14 supplies consent — unless §925 voids §14 at Zhao's election, after which Meridian needs independent contacts.
2. **Choice of law.** Will Texas law govern §8? §14 selects it; §925(b) and conflicts doctrine can displace it.
3. **Merits under the governing law.** §8 void under California law; under Texas law it must be ancillary *and* reasonable, with the burden on Meridian.
4. **Remedy and execution.** Even a favorable order must be an emergency injunction, and then enforced against a man working in Fremont.

There is a fifth consideration that is not a gate but a cost: under §§16600.1 and 16600.5, Meridian's **own conduct** — entering into the contract, and any attempt to enforce — creates liability **regardless of how a Texas court rules**.

## 5. Analysis

### 5.1 §925 is the load-bearing problem, and it turns on Meridian's own contract

Cal. Lab. Code §925(a): "An employer shall not require an employee who **primarily resides and works in California**, as a condition of employment, to agree to a provision that would … (1) Require the employee to adjudicate outside of California a claim arising in California. (2) Deprive the employee of the substantive protection of California law with respect to a controversy arising in California."

Every element is met on the face of Meridian's documents:

- **"Primarily resides and works in California"** — at formation. The agreement lists his work location as "Remote — Employee's residence (Oakland, California)"; the offer letter went to him "in Oakland, CA" and said "fully remote from California"; HR records he "worked from Oakland" for the whole tenure. Rev. 1's premise that he was Austin-based was wrong, and it was the only thing that made §925 contestable.
- **"As a condition of employment"** — the §14 clauses are in the standard form issued to every engineer, signed the same day, with no negotiation permitted. A take-it-or-leave-it term of a standard form is a condition of employment.
- **"Adjudicate outside of California" / "deprive … of the substantive protection of California law"** — §14 does both: Travis County exclusive venue, and Texas law governing.
- **Timing** — §925(f) applies to contracts "entered into, modified, or extended on or after January 1, 2017." This one was entered into 2024-03-04.
- **Consequence** — §925(b): the provision is "**voidable by the employee**," and "if a provision is rendered void at the request of the employee, **the matter shall be adjudicated in California and California law shall govern the dispute**." That is not a soft preference; it is a statutory instruction that, on Zhao's motion, resolves gates 1 and 2 in his favor at once. Zhao's resignation email already says his counsel told him he "may void the Texas forum and choice-of-law clauses" — he knows the lever exists.

**The §925(e) exception is unavailable, and your answers made that company-wide.** §925(e) exempts "a contract with an employee who is **in fact individually represented by legal counsel** in negotiating the terms of an agreement to designate either the venue or forum … or the choice of law." You have confirmed nobody negotiates, nobody uses counsel, and the signature came 113 minutes after the envelope was sent. §15's boilerplate — "Employee acknowledges having had the opportunity to consult counsel" — is an acknowledgment of *opportunity*, not the fact of individual representation in negotiation; the agreement's own HR note ("no counsel involved") sits inches from it. The safe harbor is therefore unavailable **across Meridian's entire California engineer population**, which matters in both directions: Zhao wins §925, and Meridian cannot point to a single California colleague whose venue clause was individually negotiated.

**Meridian's best answer on §925, and its limits.** §925(a)(1) reaches "a claim arising in California," and §925(a) speaks in the present tense about where the employee resides and works. Meridian will argue the contract was made with a Texas employer, is paid by a Texas entity, and any claim "arises" from a Texas-law contract negotiated in Texas. Two problems. First, the performance, the residence, the restrained conduct, the competitor (Fremont), and the AB 1076 obligation are all California-side, so "arising in California" is the natural reading. Second, even if §925 somehow did not reach him, §925(a)'s premises are also the strongest evidence in the case for the conflicts analysis in 5.2, which Meridian has to win anyway. **P(§925 voids §§14 and, with it, Travis County venue): ~75–90%.**

**One procedural caveat we cannot verify.** §925(b) attaches its consequences once a provision is "rendered void at the request of the employee," but the library does not tell us whether Zhao gets that ruling by moving in Meridian's Travis County case or must first obtain it in a California proceeding. The library's own practice note assumes a Texas court would face the question directly ("if the clause is voided under Cal. Lab. Code §925 at the employee's election, the Texas court must find independent minimum contacts"), which is why we treat it as one linked fight rather than two. Either way the substance is the same, and what §925 does to Meridian is add months and cost before anyone reaches the merits — while every month that passes makes an emergency injunction harder to justify and Zhao more settled in Fremont. Flagged as unverified (Section 10).

Note the discretionary fee provision too: §925(c) — a court "**may** award an employee who is enforcing his or her rights under this section reasonable attorney's fees." A §925 motion is therefore not free for Zhao, but it is one-way in the same direction as everything else here.

### 5.2 If a Texas court reaches choice of law, Meridian's own controlling authority defeats §14

Texas courts do not simply honor choice-of-law clauses. Per *DeSantis v. Wackenhut Corp.*, 793 S.W.2d 670 (Tex. 1990), Texas applies Restatement (Second) of Conflict of Laws §187, and the library's §187(2) text is explicit: the chosen state's law applies **unless** (a) the chosen state has no substantial relationship to the parties or transaction, or (b) applying the chosen law "would be **contrary to a fundamental policy** of a state which has a **materially greater interest** than the chosen state in the determination of the particular issue and which, under §188, would be the state of the applicable law in the absence of an effective choice."

*DeSantis* is squarely against Meridian on the facts as they actually are: the Texas Supreme Court "refused to apply a Florida choice-of-law clause to a non-compete for an employee working in Texas, because Texas had a materially greater interest and application of Florida law would contravene fundamental Texas policy on non-competes." Substituting the real facts:

| | *DeSantis* | Meridian / Zhao |
|---|---|---|
| Employee worked in | Texas | **California** (all 940 days, per Meridian's own agreement) |
| Law chosen by the employer | Florida (permissive) | Texas (permissive) |
| State with the fundamental contrary policy | Texas | **California** |
| Result | Chosen law displaced; forum state's law applied | Same structure |

Meridian's real *DeSantis* problem is that the analogy is now exact rather than strained: the state whose policy is contrary is also the state where he worked and lived, which is precisely the §188 default §187(2)(b) points to. The contacts point everywhere but Texas: offer letter to Oakland; "fully remote from California"; work performed from Oakland; the restrained conduct is employment by a Fremont company; the confidentiality he promises to honor is centered in California; the notice obligation Meridian breached is a California statute protecting California employees. Texas' connections are that the employer is a Texas entity, two short trips to Austin, and a signature on a DocuSign envelope.

California's parallel authority confirms the outcome in any forum: *Application Group, Inc. v. Hunter Group, Inc.*, 61 Cal.App.4th 881 (1998) (California had a materially greater interest in applying §16600 to a Maryland employer's non-compete with an employee recruited to work for a California employer; "California's policy against non-competes is 'fundamental'") and *Nedlloyd Lines B.V. v. Superior Court*, 3 Cal.4th 459 (1992) (California follows §187; chosen law yields to a fundamental California policy where California has a materially greater interest). California's fundamental-policy status is statutory, not just doctrinal: §16600.5(a) — a contract void under the chapter "is unenforceable **regardless of where and when the contract was signed**," and §16600(b)(1) directs that §16600 "shall be read broadly, in accordance with *Edwards*" **to void any noncompete agreement in an employment context, "no matter how narrowly tailored."**

**P(Texas law governs §8): ~5–15%.** Rev. 1's 15–25% assumed two Texas work-years. That premise is false, so the number came down.

### 5.3 If California law applies, §8 is void — and tailoring is irrelevant

- **§8 is void.** §16600(a): "Except as provided in this chapter, every contract by which anyone is restrained from engaging in a lawful profession, trade, or business of any kind is to that extent void." §8 bars him from being "employed by or provide[ing] services to" any warehouse-AMR business in the United States for 24 months — a near-total occupational bar in his field.
- **Narrow tailoring buys nothing.** §16600(b)(1) codifies the broad reading; *Edwards v. Arthur Andersen LLP*, 44 Cal.4th 937 (2008), held §16600 voids employment non-competes "even if narrowly drawn, unless they fall within the applicable statutory exceptions," expressly **rejecting the Ninth Circuit's "narrow restraint" exception** and disapproving *Campbell v. Board of Trustees* and *General Commercial Packaging*. So Meridian's honest characterization of §8 as a product-specific, industry-defined restraint — which is fairer than Rev. 1's "any competitive business" — is legally irrelevant in a California forum, and is worth saying plainly rather than leaning on.
- **The exceptions cannot be argued on this library.** §16600's operative text here excepts only what "this chapter" allows, and the library does **not** contain the chapter's exception provisions. The one case that preserves a reasonableness analysis, *Ixchel Pharma, LLC v. Biogen, Inc.*, 9 Cal.5th 1130 (2020), applies a rule of reason to **business-to-business** restraints and, per the library, "distinguished the employment context, where *Edwards* governs and non-competes are void." Zhao is an at-will engineer with no ownership interest, so *Ixchel* is not a path. We flag the missing exception text as an unverified gap (Section 10) but note that no employee exception is even arguable on these facts.
- **§9 is exposed the same way.** Its 12-month bar on soliciting "Company employees or customers" is narrower than §8, but §16600's text is not limited to clauses labeled "non-compete," and we could not verify California law on employee non-solicits from this library (flagged, not cited). Assume §9 is at least as vulnerable as §8.
- **Signing date does not help.** §16600.5(a) makes the void contract unenforceable "regardless of where and when the contract was signed" — the March 2024 signing is after the statutes took effect (63 days), so there is not even a retroactivity argument.

### 5.4 If Texas law does apply, §8 most likely fails at the threshold — and reformation cannot rescue it

Tex. Bus. & Com. Code §15.50(a): a covenant not to compete "is enforceable if it is **ancillary to or part of an otherwise enforceable agreement** at the time the agreement is made" and only "to the extent that it contains limitations as to **time, geographical area, and scope of activity** … that are **reasonable** and do not impose a greater restraint than is necessary to protect the goodwill or other business interest of the promisee."

**(a) Ancillarity is now Meridian's threshold problem.** §15.51(b): because the primary purpose of this agreement is to obligate Zhao to render personal services, **Meridian bears the burden** of proving ancillarity and reasonableness. Consider the record Meridian would carry that burden with:

- *Alex Sheshunoff Management Services, L.P. v. Johnson*, 209 S.W.3d 644 (Tex. 2006), is the case that made at-will employment covenants workable: the covenant was enforceable where the employer's promise (e.g., to provide confidential information) was **performed**. The excerpt we have contains **no employer-side promise** — §10 is Zhao's obligation, not Meridian's — and you confirmed the form is standard, signed the same day, and never negotiated. Nothing in the file shows Meridian promised or delivered anything in exchange for §8. On that record the *Sheshunoff* route is closed. **This is the one fact that would move our number:** if the complete agreement (we have only the excerpt) contains a Meridian promise — confidential information, specialized training, a payment tied to it — that Meridian actually performed, ancillarity becomes a live fight rather than a probable loss. You had no further information on this (QUESTIONS.md Q1), so we have not adjusted the estimate.
- *Marsh USA Inc. v. Cook*, 354 S.W.3d 764 (Tex. 2011) is Meridian's best support: stock options "were reasonably related to the employer's interest in protecting goodwill" and the Court "rejected a narrow 'give rise' requirement." But *Marsh* worked because there **was** consideration tied to a protectable interest. On the record we have, Meridian has no equity, no documented training commitment, no confidentiality-for-covenant exchange, no separate consideration, and — your word — no negotiation. "Ancillary to **or part of**" is the ambiguous phrase Meridian would lean on — that §8 is simply one term inside an otherwise enforceable employment contract. That reading is available and we do not dismiss it; it is, however, in tension with a statute that conditions enforceability on the covenant being ancillary *at the time the agreement is made*, which is exactly when the record shows Meridian promised nothing.
- *Light v. Centel Cellular Co. of Texas*, 883 S.W.2d 642 (Tex. 1994), is not a fallback for Zhao either: its timing requirement was modified by *Sheshunoff*, and the library expressly warns it "should not be cited for the proposition that a unilateral at-will agreement cannot support a covenant." Meridian should not expect a clean, decided Texas case voiding a form covenant for lack of a reciprocal promise — this specific question is genuinely unsettled on the library. That is a hedge, not a win.

**P(§8 clears the ancillarity threshold): ~25–40%.**

**(b) Scope.** Assume ancillarity is cleared. §15.50(a) then requires reasonable limits on time, geography, and scope, no greater than necessary to protect goodwill or other business interest. Against Meridian: 24 months across the entire United States; a bar on being *employed by* any such business, not merely on competing using Meridian information; a restraint equal to **77.7%** of his tenure; no evidence of misappropriation, and Meridian's stated interest is "the competing itself," which is the definition of a naked restraint. For Meridian: the clause is industry-specific (warehouse AMRs) rather than "any business," and Zhao is a perception engineer, so a court could rationally re-form it to, say, six or twelve months limited to AMR competitors. Expect reformation, not outright voiding, on this branch.

**(c) Reformation gives you almost nothing you want.** §15.51(c): if the limitations are unreasonable the court "**shall reform**" the covenant and enforce it as reformed, "but may not award damages for breach before reformation." Reformation addresses unreasonable time, geographic-area, and scope limits — it **cannot manufacture a missing ancillary basis**, so it is unavailable if Meridian loses (a). And §15.52 makes the §15.51 "procedures and remedies … **exclusive** and preempt any other criteria for enforceability." The best realistic Texas outcome is therefore a forward-looking, narrowed injunction with **no damages for the Kestrel months that have already run** — and Meridian would reach it only after winning conflicts and ancillarity.

**Chain, with arithmetic shown:** 0.05 × 0.25 × 0.25 = **0.31%** at the low end; 0.15 × 0.40 × 0.50 = **3.0%** at the high end. Call it **under 3%** that Meridian obtains a meaningful Texas injunction, before execution problems (5.6) are layered on.

### 5.5 Gate 1, if §14 falls: the contacts record is thin

Per the library's practice note (`tx_jurisdiction_note.md`, Tex. Civ. Prac. & Rem. Code §17.042; *Michiana Easy Livin' Country v. Holten*, 168 S.W.3d 777 (Tex. 2005)): a forum-selection clause consenting to Travis County "generally supplies consent to personal jurisdiction; but if the clause is voided under Cal. Lab. Code §925 at the employee's election, the Texas court must find independent minimum contacts. Two short business trips to Austin and a contract with a Texas employer may or may not suffice." That is the honest state of the library, and it describes this fact pattern almost exactly: **onboarding week plus an offsite**, against a California resident who never worked in Texas. **P(jurisdiction on contacts alone): ~30–50%.** Because §925, choice of law, and jurisdiction are linked, losing the first tends to cost Meridian months and money before anyone reaches the merits.

### 5.6 Even a Texas win would not move Zhao out of Fremont

The same practice note states that "an injunction entered in Texas would in any event face non-recognition in California on public-policy grounds for the non-compete." We flag that the note supplies no statutory hook for non-recognition — the library's §16600.5(c) is about employers **entering into** void contracts, not judgment recognition, so the recognition rule itself is unverified (Section 10). But §16600.5(b) is directly on point for the practical point: an employer "shall not attempt to enforce a contract that is void under this chapter **regardless of whether the contract was signed and the employment was maintained outside of California**."

*Advanced Bionics Corp. v. Medtronic, Inc.*, 29 Cal.4th 697 (2002), cuts one way in Meridian's favor and should be stated accurately: California courts "should generally not enjoin a party from pursuing litigation in another state's courts," so Zhao probably cannot obtain an anti-suit injunction to stop a Travis County filing. That is not protection. It means the Texas case proceeds while Zhao pursues his California remedies — §§16600.5 and 925 — against Meridian, including fees. What Meridian needs, Zhao out of Kestrel, is the one remedy neither state will deliver: Texas because the covenant is probably non-ancillary and overbroad, California because it is void.

### 5.7 Meridian's own exposure exists now, independent of filing

This is the bad news, stated plainly.

**(a) Entering into the contract was itself a violation.** §16600.1(a): "It shall be unlawful to include a noncompete clause in an employment contract, or to require an employee to enter a noncompete agreement, that does not satisfy an exception in this chapter." §16600.5(c) prohibits an employer from **entering into** a contract that includes a void provision, and §16600.5(d) makes entering into or attempting to enforce such a contract a **civil violation**, with §16600.5(e)(1) giving an employee or former employee a private action for injunctive relief or actual damages, and §16600.5(e)(2) making fees and costs mandatory for a prevailing employee: he "**shall be entitled** to recover reasonable attorney's fees and costs." Meridian did exactly this on 2024-03-04, 63 days after the statutes took effect. The only escape would be an exception "in this chapter," and the library does not contain the exception text (flagged, Section 10) — while §16600(b)(1) and *Edwards* point the other way.

**(b) The AB 1076 notice failure is a documented company-wide failure.** §16600.1(b)(1) required the employer, "**by February 14, 2024**," to notify "**current employees, and … former employees who were employed after January 1, 2022**," whose contracts include a non-satisfying noncompete clause, that it is void; §16600.1(b)(2) prescribes the **form** — "a written individualized communication … delivered to the last known address and the email address." Rev. 1's claim that a file note in the library said "no notice was due here" was wrong; **no such note exists** in `cal_bpc_16600_5.md`, and we delete that assertion.

As to Zhao personally: his contract was made 19 days **after** the February 14, 2024 deadline, so the (b)(1) notice obligation arguably never attached to him (whether (b)(1) reaches contracts made after the deadline is unverified — flagged). As to everyone else, your answer is the exposure: the notice was **never sent to anyone**, the project was "**deprioritized**," and LO-233 was closed "**won't do**." Every California-resident or California-working engineer on the §8 form — including anyone hired before the statutes — is a potential claimant, and §16600.5(a)'s "regardless of where and when the contract was signed" removes the "we signed it before the law changed" defense. A ticket opened and then closed "won't do" is contemporaneous documentary evidence that the deadline was known and compliance was declined, which is materially harder to defend than an oversight. And §16600.1(c) is express: "A violation of this section constitutes an act of unfair competition within the meaning of Chapter 5 (commencing with Section 17200)." The UCL characterization is therefore **citable**; the UCL's remedies, limitations, and class mechanics remain unverified (flagged).

**(c) Aggregate exposure is unknown but not small.** Zhao alone is one former employee. The population of affected California engineers is a question you could not answer (QUESTIONS.md Q5). Fee exposure under §16600.5(e)(2) is per prevailing claimant, and the library contains no cap. The prior firm memo also refers to a Travis County filing recommended "in the Alvarez matter" (Section 10), which suggests enforcement attempts against other employees may already have occurred. Treat company-wide exposure as an open, potentially class-scale number, not a Zhao-sized one.

### 5.8 Meridian's best arguments, stated at their strongest

1. **Texas has a substantial relationship** — Texas employer, Texas-signed contract, Austin HQ, two trips — so §187(2)(a) is no help to Zhao and the fight is only (2)(b).
2. §15.50(a)'s own phrase is "ancillary to **or part of** an otherwise enforceable agreement," and *Marsh USA v. Cook* "rejected a narrow 'give rise' requirement for the consideration" — so, Meridian would argue, §8 need only be *part of* the same agreement rather than purchased by separate consideration; §8 is an integral term of an otherwise enforceable at-will agreement.
3. *Sheshunoff* confirms at-will agreements can support covenants where the employer's promise is performed; Meridian can point to §10's confidentiality obligations as the mutual element. (Weak: §10 is Zhao's obligation, not a Meridian promise, and the record we have shows Meridian promised nothing in exchange for §8.)
4. §15.50(a)'s reasonableness inquiry is fact-driven, and §8 is industry-specific rather than "any business," supporting reformation to a shorter, narrower restraint.
5. *Advanced Bionics* means Zhao cannot enjoin the Texas filing, so Meridian keeps the forum initiative.
6. §16600.5(b)'s "attempt to enforce" is undefined in the library; Meridian might argue a Texas filing is not an "attempt" reachable by California. Weak given §16600.5(b)'s own "regardless of whether the contract was signed and the employment was maintained outside of California," but not frivolous.
7. §925(a)(1)'s "claim arising in California" could be contested by Meridian on the theory that a Texas-made contract generates a Texas claim.
8. Zhao affirmed in writing that he will honor confidentiality and "won't take anything with me," which helps Meridian if the case were ever about trade secrets — but Meridian's stated objection is the competition itself, which makes that argument unusable in practice.

None of these opens all four gates. Points 2, 3 and 4 collide head-on with your admissions that the form is standard, un-negotiated, same-day, and contains no reciprocal Meridian promise.

## 6. Your Request Not To Put This In Writing

You asked us to avoid documenting the notice failure in writing "if you can avoid it." We have to answer this directly, because it is now the most consequential instruction in the file.

- **We will not help keep this fact out of writing, and we advise strongly against trying.** LO-233 is a Meridian business record. In a §16600.1(c)/§17200 or §16600.5 case it is discoverable, and "won't do" after a documented deadline is close to an admission on intent. Deleting, editing, re-wording, archiving, or suppressing that ticket — or telling anyone to — would create spoliation exposure far more damaging than the underlying notice failure, and would convert a compliance problem into a litigation-ending one.
- **Litigation is now reasonably anticipated.** Zhao has California counsel, says he will void the Texas clauses, and Meridian is considering filing. Issue a **litigation hold today** covering LO-233 and the legal-ops queue, DocuSign envelopes and metadata, the engineer form template and its version history, the offer-letter template, and HR communications about Zhao and Kestrel.
- **The mitigation is compliance, and it must be written down.** The response to a missed §16600.1(b) notice is to **send the notices** in the §16600.1(b)(2) form (individualized written communication to last known address and email) and to remove §8 from the go-forward form. The record of the cure is the defense; the absence of a record of the failure is not.
- **What we will do.** This memorandum is privileged legal advice and stays in privileged channels; we will not editorialize about culpability in operational tickets, and we will not volunteer this analysis to third parties. What we will not do is help you keep a fact out of existence.

## 7. Economics

Cost figures are **our assumptions**, not client-supplied numbers (nothing in the file prices this work; QUESTIONS.md Q10). Nothing below should be relied on as a budget.

- Meridian's own fees through a contested TRO and merits fight: **$250,000** (assumption).
- Zhao's fees, if he prevails and fees are shifted: **120–300 hours × $550–$850 = $66,000–$255,000**; midpoint **$160,500**. §16600.5(e)(2) makes fees mandatory for a prevailing employee; §925(c) adds discretionary fees.
- P(fee award or §16600.5/§16600.1 finding against Meridian if Meridian files): **60–75%**. Expected fee exposure: 0.60 × $66,000 = **$39,600** to 0.75 × $255,000 = **$191,250**; at the midpoint (0.70 × $160,500) = **$112,350**.
- **Expected total cost of filing: about $362,350** (midpoint), range **$296,200–$428,500**.
- Break-even value of an injunction that works, at P(win) = EV cost ÷ P(win): **0.5% → $72.5M; 1% → $36.2M; 2% → $18.1M; 3% → $12.1M.** Against a ~0.3–3% chance, Meridian would have to value keeping one perception engineer out of Fremont for the remaining 718 restraint days at eight figures to justify filing.
- Not in the model: company-wide §16600.1/§16600.5 exposure (Section 5.7(c)), the §925(c) fee risk on a motion, and the reputational and recruiting cost of a Texas suit against a remote California engineer.

## 8. What Zhao's California Counsel Will Argue

1. §8 is void under §16600(a); §16600(b)(1) and *Edwards* make tailoring, the industry-specific wording, and the trade-secret rationale irrelevant.
2. §925(a) applies on Meridian's own contract; §925(e) is unavailable because nobody negotiated and no engineer has counsel; under §925(b) the matter "shall be adjudicated in California and California law shall govern."
3. If conflicts are reached, *DeSantis* and §187(2)(b) displace §14 — fundamental California policy plus materially greater interest, with California as the place of work and residence; *Application Group* and *Nedlloyd* in a California forum.
4. Without §14, no Travis County jurisdiction: two trips and a remote hire do not clearly establish contacts (*Michiana*, per the practice note).
5. §15.50(a) ancillarity fails because Meridian promised nothing and negotiated nothing, and Meridian bears the burden under §15.51(b); 24 months nationwide at 77.7% of tenure is unreasonable; §15.51(c) yields no pre-reformation damages; §15.52 caps remedies.
6. Meridian violated §16600.1(a) by including §8, §16600.5(c)–(d) by entering into it, and §16600.1(b) company-wide — with LO-233 as the proof — and §16600.1(c) makes that unfair competition under §17200.
7. Filing in Texas is itself an "attempt to enforce" under §16600.5(b), "regardless of whether the contract was signed and the employment was maintained outside of California," and fees are mandatory under §16600.5(e)(2).
8. Meridian's own admission — no evidence of misappropriation, "the competing itself" — is a naked restraint.
9. *Ixchel* is business-to-business and does not rescue an employee covenant; *Light* and the Ninth Circuit narrow-restraint cases are superseded and cannot be revived.

## 9. Recommendation

**Do not file in Travis County. Send no §8 or §9 demand letter.** The direction of Rev. 1's advice is unchanged; the corrected facts and your answers remove what little support it had. Meridian has no covenant-based path in Texas or California.

In order:

1. **Stand down on enforcement.** Under §16600.5(b) the trigger is the *attempt*, not the judgment. A demand letter buys the same exposure at a fraction of the cost of a suit — and Meridian is the side with the more vulnerable documents.
2. **Issue a litigation hold today** (LO-233, legal-ops queue, DocuSign metadata, form template and version history, offer-letter template). Do not alter, re-word, or close anything further. See Section 6.
3. **Cure §16600.1(b) company-wide, in writing.** Send §16600.1(b)(2)-compliant individualized written notices, to last known address **and** email, telling affected current and former California employees that their non-compete clause is void. This includes former employees employed after January 1, 2022. Document the population, the send, and the receipt channels.
4. **Fix the form.** Delete §8 from the engineer form; narrow or delete §9; stop applying §14 to California-resident employees; and record that §925(e) has never been available at Meridian because nothing is negotiated. On this library, there is no law that would let Meridian obtain an enforceable employee non-compete against a California-resident hire — §16600 is categorical and §16600(b)(1) is explicit — so treat this as a contracting-structure question, not a drafting trick.
5. **Use the channels that actually work.** Zhao agreed in writing to honor confidentiality and not to take anything. §10 is intact. If facts ever change and misappropriation appears, trade-secret claims are a different case with materially better prospects and are not an attempt to enforce a void covenant. Preserve his written assurance.
6. **Do not treat Texas reformation as a fallback.** §15.51(c) gives a forward-only narrowed covenant with no pre-reformation damages, and it is unavailable if ancillarity fails — which we think it does.
7. **Get the exposure number.** Company-wide headcount of California engineers on the §8 form (Q5) is the one fact that most changes Meridian's risk posture. We can prepare the §16600.1(b)(2) notice and a revised form on request, and advise on the trade-secret channel if evidence develops.

## 10. Assumptions, Unknowns, and Unverified Law

Per the engagement rules, only authorities listed in `library/INDEX.md` are cited, and only for what they hold. Anything we believe is law but cannot verify in the library is labeled **unverified** and **not cited**. Where you told us you have no further information, the item is recorded as a permanent flagged unknown rather than an open question.

**Assumptions (ours, not in the documents):**
- **We have only the excerpt** of the employment agreement, plus the HR timeline and resignation email. Every statement above about what the agreement does and does not contain — in particular the absence of an employer-side promise — is limited to what the excerpt and the HR note show.
- Cost and fee figures in Section 7 (Q10). **All dollar figures are counsel assumptions.** Nothing in the file prices this work.
- Zhao continues to reside in Oakland and remains at Kestrel; his stated residence is unverified independently.
- Meridian designs or sells autonomous mobile robots for warehouse logistics, so Kestrel competes with Meridian. Nothing in the file establishes Meridian's product line; if Meridian is not in warehouse AMRs, §8 may not even reach the Kestrel job — a factual question worth resolving.
- No equity or ownership interest, so nothing resembling a sale-of-interest situation exists.
- Nothing in the file shows Meridian has contacted Zhao or Kestrel about §8 or §9, so we treat today as the first enforcement contact. If a letter, email, or call has already gone out, §16600.5(b) exposure may already exist and we need to know immediately (QUESTIONS.md Q7).

**Facts not obtainable (flagged; client has no further information):**
- Headcount and geography of California engineers on the §8 form; whether any pre-2024 hires remain (drives §16600.1(b)(1) exposure).
- Whether anything was ever communicated to Kestrel Autonomy about §8 (that would be an "attempt to enforce").
- Outcome of the "Alvarez matter" referenced in the prior firm memo, and whether other California employees have been contacted about §8.
- Whether Zhao signed any amendment, renewal, or bonus agreement containing §§8/14 (relevant to §925(f)'s "modified, or extended").
- Meridian's own document-retention practices for the LO-233 ticket and DocuSign records.

**Law believed to govern but NOT in the library — unverified, not cited:**
- The §16600 chapter's **exception provisions** other than §16600(a)/(b) as excerpted here. We therefore do not assert that any specific exception (sale of goodwill, partnership dissolution, etc.) exists or is unavailable; we say only that none is arguable for an at-will engineer on these facts.
- **Restatement (Second) §188** as a stand-alone contacts test. The library's §187(2)(b) cross-references §188 ("which, under §188, would be the state of the applicable law in the absence of an effective choice"), so §188's *role* is described through §187, and we do not quote §188.
- **Recognition/non-recognition of out-of-state judgments.** The library's practice note asserts non-recognition "on public-policy grounds" without a statutory hook; §16600.5(c) in the library addresses *entering into* void contracts, not judgments.
- **Cal. Bus. & Prof. Code §17200** — its remedies (including injunctive relief and restitution), limitations periods, and class mechanics. §16600.1(c) is citable for the *characterization* of a violation as unfair competition; the consequences under Chapter 5 are not.
- **Whether California law voids employee non-solicitation clauses** (§9). Not in the library.
- **Whether §16600.1(b)(1)'s notice duty reaches contracts made after the February 14, 2024 deadline**, and whether (b)(2)'s form requirements reach former employees.
- **How §925(b)'s voiding is obtained procedurally** — whether the employee moves to void §14 in the responding forum or must first obtain a California ruling, and whether a Texas court applies §925 of its own force. The library's §925 text says nothing about procedure; our §925 analysis states the statute's terms, not a procedural holding.
- **What conduct counts as an "attempt to enforce"** under §16600.5(b) — including whether a pre-suit demand letter qualifies.
- **Texas standards for temporary injunctive relief** (irreparable harm, likelihood of success, bond), laches, and how Texas courts split "ancillary to **or part of**."
- **Texas and California trade-secret statutes** (UTSA as enacted in each state) and the DTSA.
- **Personal-jurisdiction doctrine beyond §17.042 and *Michiana*** (consent, general vs. specific jurisdiction, Due Process limits).
- **Federal law.** The FTC non-compete rule is **vacated** (*Ryan LLC v. FTC*, 739 F. Supp. 3d 496 (N.D. Tex. 2024); FTC dismissed its appeal in September 2025) and is a basis for nothing here, in either direction.

**Memo-bank materials are internal background and are not cited.** Two of them deserve a specific warning, because they are the source of the instinct to file in Texas:

- The 2024 firm memo, "Enforcing Texas non-competes against remote California employees," recommends suit in Travis County "in the Alvarez matter" and rests on ***Calderon v. Pacific Dynamics Corp.*, 48 Cal.App.5th 1120 (2023)** and ***Westbrook Systems, Inc. v. Ng*, 91 F.4th 1033 (9th Cir. 2024)**. **Neither case appears in `library/INDEX.md`,** and the 2025 update indicates the *Westbrook* line is under further review. Under this engagement's rules those authorities are unverifiable and cannot support any recommendation. Their stated holdings (Texas choice-of-law enforced against a remote California employee; §16600.5 has no extraterritorial application) point in the opposite direction from every library authority we can verify — *DeSantis*, *Application Group*, §925, §16600.5(a)–(b). Treat the prior recommendation as unreliable and, separately, as a possible source of **pre-existing §16600.5 exposure** from the Alvarez filing, which we cannot assess on this record.
- The 2024 memo's operative premise is that enforcement is supported "where the employee voluntarily accepted a Texas forum," and its *Westbrook* authority is described as "holding §16600.5 does not apply extraterritorially to contracts with out-of-state employers." Both collide with the library's text: §16600.5(a) makes a void contract unenforceable "regardless of where and when the contract was signed," §16600.5(b) bars an employer from attempting to enforce "regardless of whether the contract was signed and the employment was maintained outside of California," and *DeSantis* plus §187(2) displace a chosen law on these facts. The 2025 update adds only that, with the FTC rule out, "state law controls" — correct, and that sentence points at §16600, not away from it. We relied on none of it.

**Where our probabilities are genuinely contestable:** the ancillarity estimate (5.4(a)) and the contacts-only jurisdiction estimate (5.5). The California-law merits (5.3) and the fee exposure if Meridian files (5.7) are, on the library, close to certain. We did not force these into a single number.

**Citations.** Every authority relied on, with its citation, verified proposition, and library status, is in `deliverable/citations.json`.
