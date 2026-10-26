# Entity and tax structure — Natarajan Herrera Advisory
**Founders:** Priya Natarajan (US citizen, San Diego, single) · Tomás Herrera (Mexican citizen, TN visa, no green card pending; Monterrey + San Diego)
**Prepared:** October 25, 2026. Assumes formation **November 2, 2026** (see QUESTIONS.md — this date is an assumption).

---

## 1. Executive summary

1. **The founders' plan as stated — LLC + S election, 50/50, $40,000 salaries — is not legally available.** Tomás is a nonresident alien for 2026 under the substantial presence test, and a nonresident alien cannot be an S corporation shareholder. An S election made now would never be effective (or would terminate immediately), leaving the company as a C corporation — the *worst* of the options analyzed.
2. **Recommended structure:** a single **California LLC taxed as a partnership**, split 50/50:
   - Priya contributes the PriceLab tool (FMV $120,000, basis $31,000) for a 50% **capital interest** — nonrecognition under IRC §721 (no control test).
   - Tomás contributes $20,000 cash (capital account) and receives his remaining 50% economics as a **profits interest** for services, vesting 3 years / 1-year cliff — not a taxable event under Rev. Proc. 93-27, with a **protective §83(b) election due December 2, 2026** (30 days, no extension).
3. **Form in California, not Delaware.** A Delaware LLC doing business in California must register as a foreign LLC and pays the *same* $800 annual tax and gross-receipts fee as a California LLC — Delaware buys no state-tax advantage, only extra registration and (unquantified) Delaware costs.
4. **The friend's self-employment-tax saving is an illusion at this income level.** Even if Tomás *were* a US resident and the S election valid, reasonable-compensation doctrine (*Watson*) puts salaries near $130,000 each in year 1 — which exhausts the $260,000 profit and produces payroll tax ≈ identical to partnership self-employment tax. A $40,000 salary invites recharacterization of distributions as wages plus payroll tax, penalties and interest.
5. Revisit S election (or anything else) only if Tomás becomes a US *resident* for tax purposes (he may tip into residency in 2027 at 128+ US days — see §3) **and** profits grow large enough to justify the compliance burden.

---

## 2. Why the plan as stated fails

### 2.1 Tomás's residency status (the gating fact)

Substantial presence test, IRC §7701(b)(3)(A) [library: `irc_7701b_substantial_presence.md`]: current year + ⅓ × prior year + ⅙ × second-prior year ≥ 183, with ≥31 days in the current year.

Using the travel calendar (`documents/tomas_travel_calendar.csv`):

| Year | Weighted days | Resident? |
|---|---|---|
| 2025 | 96 + 66/3 + 0/6 = **118.0** | No |
| 2026 (projected 118 days) | 118 + 96/3 + 66/6 = 118 + 32 + 11 = **161.0** | **No** (31-day floor of 118 is met, but 161 < 183) |

Tomás would need **140 days** in the US in 2026 to reach 183. The client has now confirmed he is in the US "**maybe a third of the year**" (≈120 days): weighted = 120 + 96/3 + 66/6 = **163.0** — still short of 183, and the NRA conclusion is robust across every plausible count (118–122 days → 161.0–165.0). He holds no green card and has **no application pending** (client-confirmed). Absent a first-year election under §7701(b)(4) (mechanics beyond what the library excerpt covers — **unverified**), Tomás is a **nonresident alien (NRA)** for 2026 and for the formation year. This is no longer an assumption-dependent conclusion — it is the confirmed pattern.

### 2.2 The S election is void

IRC §1361(b)(1)(C) [library: `irc_1361_excerpt.md`]: a small business corporation may not "have a nonresident alien as a shareholder." Tomás would own 50%. A Form 2553 election is therefore **ineffective from inception** (and per §1362(d)(2), an election terminates the day the corporation ceases to qualify — the entity becomes/ remains a C corporation). There is no way to run a 50/50 S corporation while Tomás is an NRA. Late-election relief (Rev. Proc. 2013-30, cited in the Form 2553 library item) requires *all shareholders to have been eligible the entire period* — that condition is unfixable here.

### 2.3 Even setting the NRA problem aside, $40,000 salaries are indefensible

Rev. Rul. 74-44; *Watson v. Commissioner*, 668 F.3d 1008 (8th Cir. 2012); IRS Fact Sheet FS-2008-25 [library: `reasonable_compensation.md`]: a shareholder performing substantial services in a personal-services firm generating essentially all revenue must receive reasonable compensation before distributions; *Watson* recharacterized distributions where a ~$24,000 salary was paid against ~$200,000 of distributions. This firm is pure consulting earning $610,000 of revenue from the founders' own work; a $40,000 salary is squarely in *Watson* territory. "Payroll taxes, penalties and interest follow."

### 2.4 Delaware adds cost and no benefit

Cal. Rev. & Tax. Code §§17941, 17942, 23153; Cal. Corp. Code §17708.02 [library: `ca_llc_franchise.md`]: every LLC doing business in California pays the $800 annual tax and the gross-receipts fee, **and a Delaware LLC doing business in California pays the same amounts** plus foreign-qualification compliance; failure bars suit in California courts and adds penalties. Year-1 fee: revenue $610,000 → $500k–$999,999 band → **$2,500**, plus $800 = **$3,300/yr** (Year 2: $820,000 → same $3,300). Delaware's own franchise cost is **not in the library** — treat as unquantified added expense.

---

## 3. Recommendation in detail

### 3.1 Entity: California LLC, taxed as a partnership

- One LLC registered in California (operations are in CA and Nuevo León; no CA benefit to a DE wrapper — §2.4). If venture financing becomes likely later, convert/domesticate then — do not pay the DE/CA duplicate cost now.
- Multi-member LLC classified as a **partnership** for federal income tax. **Unverified in library:** the default-classification regulation is not among the library items; the partnership regime itself is what the library supports (§721, Rev. Proc. 93-27, §199A guaranteed-payment rule). If the client wants certainty on how classification is elected, note the gap.
- **Priya's tool:** contribution of property for a partnership interest is nonrecognition under **§721(a)** — "no 80% control requirement" (contrast §351, needed only for the corporate route). Her $120,000 FMV becomes her capital account; the $31,000 basis carries into the asset. (Basis-carryover rule §722 and holding-period tacking §1223 are *not* in the library — labeled **unverified**, though standard.)
  - Note: Priya deducted $89,000 of development costs; her $31,000 basis means the *entity* gets only $31,000 of the remaining cost to work with, and on any future sale of the tool the gain is $89,000+ — no step-up from the contribution.
- **Tomás's "client relationships and selling" are services, not property.** In a corporation this is the §351(d) trap [library: `irc_351_excerpt.md`]: stock issued for services is *not* issued for property, so it is compensation income at FMV when substantially vested — Tomás would owe tax on ~$50,000 of spread as his shares vest (50% of $140,000 capital, less his $20,000 cash). **In a partnership the route is clean:** a **profits interest** received for services is not a taxable event (Rev. Proc. 93-27 §4.01), provided it gives him **nothing on an immediate liquidation at FMV** — the operating agreement's waterfall must implement exactly that (§3.2). A capital interest for services would be taxable at receipt or vesting — that is what we are avoiding.
- **199A posture:** consulting is a **specified service trade or business** (§199A(d)(2)) [library: `irc_199a_sstb.md`]. Priya's year-1 allocable income (~$130,000) is below the ~$200,300 single threshold (library figure, "verify"), so the SSTB bar should not bite her yet and the 20% deduction (~$25,670 → ~$6,161 of tax at our assumed rate) may apply. **Tomás's QBI entitlement as an NRA is not addressed in the library — open item.** Related and now confirmed by the client: he performs services **mostly from Monterrey** while clients are all over the US. The portion of his 50% allocation that is US-source effectively connected income, and any US–Mexico treaty relief, are outside the library — unresolved, for a specialist engagement (see §3.5 and QUESTIONS.md).

### 3.2 How each contribution becomes equity

| Founder | Contributes | Receives | Tax treatment |
|---|---|---|---|
| Priya | PriceLab tool — FMV **$120,000** (Coastline Valuation, Jan 15 2026), basis **$31,000** | 50% **capital + profits interest**; capital account **$120,000** | §721 — no gain; no 80% test to worry about |
| Tomás | **$20,000** cash; services (client relationships, sales) | Capital account **$20,000** (from cash) + **50% profits interest** vesting 3 yrs / 1-yr cliff | Cash: contribution. Profits interest: **not taxable at grant** (Rev. Proc. 93-27 §4.01); treated as held from grant if treated as partner from grant (Rev. Proc. 2001-43); file **protective §83(b)** |

Waterfall that makes it a true profits interest: on any liquidation, **first** return capital accounts ($120,000 to Priya, $20,000 to Tomás), **then** split the remainder 50/50. On day one the LLC is worth exactly the contributed capital, so Tomás's profits interest is worth $0 at grant — the safe harbor is satisfied on its face. Do not let the agreement give him a fixed 50% of *existing* capital; that converts it to a taxable capital interest.

- **Protective §83(b) election for Tomás: due December 2, 2026** (30 days after the Nov 2 transfer; "no extension is available," §83(b) / Treas. Reg. §1.83-2 [library: `irc_83b.md`]). Because it is a profits interest the election costs nothing now and locks the §2001-43 treatment.
- Priya's interest: fully vested at formation (she put in the property).
- **Vesting protection:** unvested profits-interest units repurchase **at cost** on departure [library: `llc_buy_sell_checklist.md`: "vesting of founder units with repurchase at cost for unvested units"]. See `term_sheet.md`.

### 3.3 If Tomás later becomes a US resident — and when

On the client-confirmed pattern (≈120 US days/yr), he crosses into residency if 2027 US days ≥ **127** (127 + 120/3 + 96/6 = exactly 183; the test is "equals or exceeds"), with 2027 weighted ≈ **176.0** at 120 days — he stays NRA, but by a margin of only about **7 days**; the 2028 threshold drops to **123** days (120 + 120/3 + 120/6 pattern). With no green card and none pending (confirmed), absent a new immigration strategy he likely remains NRA; **monitor day counts annually**. If (and only if) he becomes a resident shareholder, an S election becomes *legally possible*; then:
- Salary must be **reasonable**, not $40,000 — model ~$130,000+ each in year 1 terms (*Watson*).
- W-2 wages are **not QBI**; distributions are (§199A library item). At $260,000 of net, $130,000 salaries exhaust the profit → **zero distributions, zero QBI deduction, payroll tax ≈ the partnership's SE tax** (see comparison). The S election only starts to "save" self-employment tax where net substantially exceeds the reasonable-compensation level (roughly Year-2 scale of $370,000+ with ~$150,000 salaries — direction only, not modeled here), and by then Priya's taxable income may hit the SSTB threshold anyway.
- **Recommendation: stay partnership; re-evaluate annually.** Revisit only after Tomás's residency is certain and net > ~$400,000.

### 3.4 What we explicitly rejected

| Alternative | Why rejected |
|---|---|
| **LLC + S election now (the stated plan)** | Void: NRA shareholder bars S status, §1361(b)(1)(C); result is a C corporation (see computation — plus IRS exposure for the bad election). |
| **C corporation (the forced outcome of that plan)** | Double tax: 21% (assumed) entity + dividend-level tax; no QBI deduction available to owners of a C corp at all; NRA withholding exposure on distributions to Tomás (rate not in library — unverified). Also the $40,000 salaries create the *Watson* recharacterization problem in a different form. |
| **Delaware LLC + CA foreign qualification** | Same CA $800 + fee either way (library); added DE cost (unquantified) and registration risk (loss of CA court access). No advantage for a two-founder consulting firm. |
| **S corp with Priya 100% + Tomás as contractor/employee — incl. the "list Priya as sole shareholder now, add Tomás later" variant (client follow-up, Oct 25)** | Preserves S status only while Tomás owns **nothing**; adding him later either (i) while still NRA → election **terminates the day he becomes a shareholder** (§1362(d)(2) parenthetical [library]) → C corp from that day, or (ii) only after he becomes a resident (earliest plausibly 2028, day-count-dependent) → his shares-for-services are **compensation income at FMV spread** (§351(d)/§83 [library]) at a value **above** day one. Destroys the 50/50 ownership the founders want in the meantime, strands Tomás's equity at a worse tax point, and raises its own recharacterization/immigration questions. Full analysis §3.6. Contrary to stated intent. |
| **Corporation with §351 formation (if residency were solved)** | §351 works for Priya + cash, but Tomás's services-for-stock is §351(d): compensation income on ~$50,000 spread as it vests under §83. The partnership profits-interest route achieves the same economics with **no** income at grant (Rev. Proc. 93-27). |

### 3.5 Out-of-scope but material (flagged, not advised on)

- **Tomás's TN status and ownership/services for a company he owns:** the library contains **no immigration authority**. Client has confirmed TN status, no green card, and **no application pending** — so nothing in his own file resolves the work-authorization question. Whether performing services for, or owning, this LLC is consistent with TN status must be confirmed with qualified immigration counsel **before formation**. This could be as gating as the S-election problem; we do not opine.
- **Mexican community property (client-confirmed: Tomás married in Mexico, no prenuptial agreement):** the default community-property regime applies to his LLC interest unless Mexican law provides otherwise (not in library). The buy-sell checklist [library] prescribes transfer restrictions and **spousal consent**; with no prenup, spousal joinder is a **mandatory** formation condition, not a nice-to-have — see term sheet §5. Marital-property structuring under Mexican law is outside the library — local counsel.
- **Services sourcing (client-confirmed split):** Tomás works mostly from Monterrey; Priya from San Diego; clients all over the US. The US-source portion of Tomás's distributive share, NRA withholding mechanics, and any US–Mexico treaty are **not in the library** — open item (QUESTIONS.md).
- **Clients all over the US** may create registration/income-tax obligations in other states (nexus). The library covers **California only** — other-state exposure is **unaddressed and outside the library**; flag to an SALT adviser.
- Mexican-side obligations for the entity or for Tomás: not in library, not addressed.

### 3.6 Client follow-up (Oct 25, 2026): "The CPA does S corps for everyone — can't we just list Priya as sole shareholder now and add Tomás later?"

**(1) "Our CPA does this for everyone" is not authority.** The bar is statutory and categorical: §1361(b)(1)(C) — a corporation with "a nonresident alien as a shareholder" is not an S-eligible corporation [library: `irc_1361_excerpt.md`]. The likely reconciliation is mundane: other clients of that CPA have individual shareholders who are US citizens or resident aliens. Tomás's own confirmed pattern ("maybe a third of the year" ≈120 days → weighted 163.0 vs the required 183; 140 US days needed in 2026) puts him squarely on the wrong side of §1361(b)(1)(C). We have no facts about the friend's engagements and do not opine on them — but if any of those companies actually have an NRA shareholder, the same statute voids those elections too.

**(2) The "Priya 100% now, add Tomás later" variant was analyzed and rejected.** It has three timelines, all worse than the recommended structure:

- **(i) Add Tomás while he is still an NRA** (the realistic case through 2027, and possibly 2028 unless he clears ≈123 US days — no green card or application pending): the S election **terminates on the exact day he becomes a shareholder**, and the corporation is a C corporation from that day [library: `irc_1361_excerpt.md`, §1362(d)(2) parenthetical]. This is the same cliff the original plan walks into — just scheduled in advance, and *inside* the years the company is most profitable. (A five-year bar on re-electing after a terminated election is standard but **not in the library — unverified**; register row 14.)
- **(ii) Add Tomás only after he becomes a US resident.** The election survives, but the *addition itself* is a taxable event under library rules: stock issued to him for his services/relationships is stock not issued for property — §351(d) — so it is **compensation income at FMV** as it vests under §83 [library: `irc_351_excerpt.md`, `irc_83b.md`]. By 2028 the company has a revenue history, so the spread is **larger** than the $50,000 computed at formation (§3.2) — the delay *increases* the tax rather than avoiding it. If instead Priya transfers half her shares, she recognizes gain on stock with a $31,000 carryover basis (carryover rule standard but §362 not in library — **unverified**), or gift reporting applies (not in library). If he simply "buys in," he pays true FMV — well above his $20,000.
- **(iii) The interim years.** While Tomás owns nothing: he can't contribute his $20,000 as capital, and his economics come only as wages or contractor fees — payroll/withholding mechanics for an NRA performing services partly abroad are **not in the library** (cross-border specialist), and whether TN status covers work for this company at all is the open immigration item (§3.5). And there is no tax deferral to be had: option (c) in `year1_comparison.json` already shows the S-corp route at *defensible* comp pays ≈ the same payroll tax as the partnership ($39,780 vs $39,275.10) — the friend's $40,000-salary "saving" was never real (*Watson*, [library: `reasonable_compensation.md`]).
- **(iv) A filing that doesn't match the real deal is its own risk.** If Priya is the sole shareholder *on paper* while the two actually operate 50/50 under side agreements, the filings do not reflect the actual ownership and the election is exposed in audit. Substance-over-form doctrine is **not in the library — unverified**; we flag it and do not paper structures that contradict the founders' stated intent.

**(3) Bottom line.** The partnership structure achieves the founders' actual goal **now** — 50/50 economics, Tomás's profits interest **tax-free at grant** (Rev. Proc. 93-27 [library]) with the protective §83(b) by Dec 2, 2026 — and keeps the S-corp door open: if Tomás's residency ever becomes real and net exceeds ~$400,000, they can elect S status *legally* at that time (§3.3). The "sole shareholder now" variant delays ownership, adds tax at the add-back step, and risks a void-or-terminated election in every branch. Recommendation unchanged.

---

## 4. Year-1 numbers (all shown in `year1_comparison.json`)

**Model assumptions — none of these rates are in the library; they are labeled assumptions, flat for comparability:** federal individual 24% flat on business compensation/allocations (illustrative only); qualified dividends 20%; corporate 21%; payroll/self-employment 15.3% (wage-base cap assumed above all amounts shown; cap not in library). Deliberately **excluded** (making the partnership look no better than it must): half-SE-tax deduction, Priya's possible QBI deduction, standard deductions, 0.9% additional Medicare, CA corporate franchise tax for (a)/(c) (statute cited in library, amount not stated), 2026 threshold verification.

| Option | Entity tax | Founder tax (P + T) | Payroll/SE tax | **Total** |
|---|---|---|---|---|
| (a) Stated plan → election void → **C corp** | $37,800 | $23,820 + $23,820 = $47,640 | $12,240 | **$97,680** ⚠ |
| (b) **Recommended: CA LLC / partnership** | $3,300 | $30,804 + $30,804 = $61,608 | $39,275.10 | **$104,183.10** |
| (c) S corp *if Tomás resident*, comp $130k each (unavailable in 2026) | $0 | $31,200 + $31,200 = $62,400 | $39,780 | **$102,180** |
| (d) Same as (b) but Delaware LLC + CA registration | $3,300 + **DE cost unquantified** | same as (b) | same as (b) | ≥ **$104,183.10** |

Arithmetic (year-1 net $260,000; revenue $610,000):

- **(a)** Salaries $80,000 → entity income $180,000 → ×21% = **$37,800**; after-tax profit $142,200 distributed $71,100 each. Founder tax each: wages $40,000×24% = $9,600 + dividend $71,100×20% = $14,220 → **$23,820**. Payroll: $80,000×15.3% = **$12,240**. **⚠ The total is deceptively low**: it assumes clean qualified-dividend treatment at 20%, ignores penalties/interest for the invalid election, ignores NRA withholding on distributions to Tomás (illustratively 30% would be $21,330 vs the $14,220 assumed — +$7,110), and ignores CA corporate franchise tax.
- **(b)** CA $800 + $2,500 = **$3,300** entity; K-1 each (260,000 − 3,300)/2 = **$128,350**; SE tax each 128,350×15.3% = **$19,637.55** (total $39,275.10); income tax each 128,350×24% = **$30,804**. Sensitivity *with* the excluded benefits: half-SE deduction (−$2,356.51 each) and Priya QBI (−$6,160.80) → ≈ **$93,309**, i.e., below every other column once the ignored rules are turned back on.
- **(c)** $130,000 each is the *Watson*-safe salary; wages $260,000 exhaust net → no distributions, no QBI; payroll $260,000×15.3% = **$39,780**; founder tax each $130,000×24% = $31,200. Gap vs (b): **$2,003 before** (b)'s QBI/half-SE benefits, which reverse it. **Conclusion: the "fortune in self-employment tax" is ~$0 at year-1 scale — and (c) is not even legally available while Tomás is an NRA.**
- **(d)** Identical CA burden to (b) — that is the point of `ca_llc_franchise.md` — plus unquantified Delaware cost. Nothing reconciles differently; the DE variant simply costs more.

Year-2 direction (not in JSON): net $370,000; CA fee still $3,300 ($500k–$999,999 band); partnership SE tax ≈ $28,305 each on full allocations. An S election could save something only with salaries well below reasonable comp — which is the *Watson* violation — or at net levels beyond the Year-2 projection.

**CA fee-band sensitivity (client answers):** Tomás performs services mostly from Monterrey, so some of the LLC's $610,000 gross receipts reflect activity outside California. If CA-allocable gross receipts fell into the $250,000–$499,999 band, the fee would drop to **$900** — but because the fee is a business expense that reduces allocations, founder tax rises: entity $800 + $900 = **$1,700**; K-1 each $129,150; SE each $19,759.95; income tax each $30,996 → **total $103,211.90** (vs $104,183.10 shown). The library states the bands but **not** any allocation rule — unverified; the base case keeps $3,300. Either way the structure recommendation is unchanged.

---

## 5. Assumptions and unverified items register

| # | Item | Status |
|---|---|---|
| 1 | Formation date Nov 2, 2026 | **Assumption** (drives 83(b) and election dates) |
| 2 | Tomás's actual 2026 US days | Client-confirmed "maybe a third of the year" (≈120): NRA either way (weighted 161.0–165.0 at 118–122 days). **2027 residency threshold 127 days; 2028 ≈123 days — monitor annually** |
| 3 | Tax rates (24% / 20% / 21% / 15.3%), wage-base cap, thresholds | **Not in library — assumed**; all figures labeled |
| 4 | LLC default partnership classification; Form 8832 mechanics | **Not in library — unverified** |
| 5 | §722 carryover basis, §1223 holding period | **Not in library — unverified** |
| 6 | First-year election §7701(b)(4) availability for Tomás | Mentioned by library; mechanics **unverified** |
| 7 | QBI deduction for an NRA (Tomás) | **Not in library — open** |
| 8 | NRA taxation of Tomás's K-1 income; US/Mexico sourcing; treaty | **Not in library — open.** Confirmed he performs services mostly in Mexico; US-source share of his 50% allocation must be quantified by a specialist |
| 9 | TN status permitting self-employment/ownership | **Not in library — must confirm with immigration counsel.** Client confirmed TN, no green card, no application pending |
| 10 | Delaware franchise costs; CA corporate franchise amount; CA filing due dates | **Not in library — unquantified** |
| 11 | CA gross-fee base = total revenue $610,000 (vs CA-sourced portion) | **Assumption**; some activity is now known to occur outside CA — possible drop to the $900 band (see §4 sensitivity); allocation rules not in library |
| 12 | 199A thresholds "≈$200,300 / $400,600" | Library figure itself says **verify** |
| 13 | Other-state registration/income-tax nexus (clients all over the US) | **Not in library — unaddressed**; SALT adviser |
| 14 | Five-year bar on re-electing S status after a terminated election (§1362(g)); §362 carryover basis in a §351 formation; gift-tax mechanics if Priya transfers shares to Tomás | **Not in library — unverified**; relevant only to the rejected "sole shareholder now, add later" variant (§3.6); §1362(d)(2) *termination itself* IS in the library |

Every citation above points to a file in `library/INDEX.md` (items: `irc_1361_excerpt.md`, `irc_7701b_substantial_presence.md`, `irc_351_excerpt.md`, `irc_721_and_revproc_93-27.md`, `irc_83b.md`, `irc_199a_sstb.md`, `reasonable_compensation.md`, `form_2553_deadline.md`, `ca_llc_franchise.md`, `llc_buy_sell_checklist.md`). No authority outside the library is cited; anything else is labeled above.
