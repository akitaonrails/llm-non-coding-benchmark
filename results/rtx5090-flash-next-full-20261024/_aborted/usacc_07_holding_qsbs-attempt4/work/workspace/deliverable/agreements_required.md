# Agreements and documents required under the revised plan

Prepared 2026-10-25 for Nadia Oakline. This is a checklist of the intercompany and governance paperwork the revised
plan in `opinion.md` §4 requires. It is a **list of what is needed and why**, not drafted instruments; the entity,
securities, and estate items should be engaged out (they sit outside the tax library available for this opinion).

Legend: **R** = remediation (do first) · **H** = holding-company formation/contribution · **S** = separateness
maintenance · **E** = Helio-specific · **O** = out-of-scope referral.

> **Update after the client's 2026-10-25 response (`opinion.md` §8).** Sections **A**, **D** and **E** and the new
> **Section G** are the work that should happen now. Sections **B** and **C** (forming Holdings and contributing the
> LLC interests) are **deferred until after the Helio exit** unless there is a non-tax reason to do them sooner
> (`opinion.md` §8.6). Note also that the 99/1 design in item 9 should be **abandoned** — the 1% member is Nadia's own
> revocable living trust, so there is no second partner (§8.2).

---

## A. Phase 0 — intercompany-loan remediation (do before anything else)

| # | Document | Purpose / authority | Status today |
|---|---|---|---|
| 0 | **Execution-status memo** — has Holdings been formed, has any assignment/contribution agreement or membership certificate been signed, has **any Helio share** been assigned or pledged, have accounts been merged? `documents/org_chart.md` carries a "Step 1: Wyoming" note dated **2025-11-04** | Determines whether this opinion is prospective or remedial. If the Helio shares have already moved, the §1202 analysis must be redone immediately — `QUESTIONS.md` G1 | **Unknown — most urgent item in the file** |
| 1 | **Intercompany loan schedule & reconciliation** (Properties↔Services↔Digital, by date, amount, direction) | Establishes what the $400,000 and $150,000 actually are; needed to close the $1,760,000 balance-sheet gap (`opinion.md` §6) | Missing — `intercompany_cash_flows.csv` is the only record |
| 2 | **Capital contribution resolutions** converting Properties→Services $400,000 and/or Services→Digital $150,000 to equity (member/manager consents of each entity), with corresponding ledger entries | Removes the loans from IRC §7872 recharacterization (`library/irc_7872_afr.md`) | Missing |
| 3 | **Or: promissory notes** for each intercompany loan — stated principal, maturity in the 3–9 year band, interest **≥ 4.12%** (mid-term AFR for this engagement), amortization schedule, default and prepayment terms, governing law | If the loans are kept, they must not be below-market: §7872 (`library/irc_7872_afr.md`) | Missing ("none" / "email only") |
| 4 | **Payment evidence protocol** — cancelled cheques / bank transfers per scheduled payment, recorded in each entity's books | A note that is never paid is still evidence of commingling (`library/irc_7872_afr.md`) | Missing |
| 5 | **Annual imputed-interest true-up workpaper** — imputed interest $16,480 (Properties→Services) + $6,180 (Services→Digital) = $22,660/yr, and the deemed distribution/contribution entries | §7872 recharacterization; needed for the tax returns if any loan survives | Missing |
| 6 | **Prior-year (2024–2025) imputed-interest computation**, day-count from 2024-03-01, 2025-06-15, 2025-09-01, plus any amended-return decision | Open years; methodology left open pending the CPA records requested in `QUESTIONS.md` R2 — indicative partial-year figures are in `numbers.json` ($13,669.37 Properties / $2,048.71 Digital) | Open |
| 7 | **Written policy: no new intercompany advances without a signed note at ≥ AFR and member consent** | Prevents recurrence | Missing |
| 7a | **Memorandum documenting the 2024 refinancing** — $1,200,000 of Properties' mortgage proceeds distributed to Nadia personally, with the date and bank evidence, plus a standing instruction that entity expenses are **not** paid from her personal brokerage account and that the money is not relent to the entities without documents | Client confirmed the destination of the cash on 2026-10-25; commingling that "undermines separate-entity liability protection" (`library/irc_7872_afr.md`); also accounts for most of the negative tax capital — `opinion.md` §8.7. Date is not in `documents/properties_balance_sheet.md`; get it from the bank records | Missing |
| 7b | **Capital-contribution resolutions (post-exit)** funding Properties with $1,900,000 of member equity and retiring the mortgage, with the ledger entries and the §752(b)/§731(a) check — partnership branch: $1,881,000 deemed distribution vs basis $5,161,000 / $3,401,000 → no gain; disregarded branch: §752/§731 do not apply → no gain | Cheapest way to remove the §752 trap permanently: equity, not new paper debt — `opinion.md` §8.7; `numbers.json` → `mortgage_payoff_after_exit` | For after the Helio exit |

## B. Phase 2 — holding company formation (Oakline Holdings LLC) — **deferred; see §8.6**

| # | Document | Purpose |
|---|---|---|
| 8 | **Certificate of formation** in Colorado (or, if Wyoming is insisted on, WY formation + Colorado foreign-qualification filings) | The nexus summary: WY entity managed from CO has Colorado nexus and files there; WY has no income tax but requires an annual report (`library/state_nexus_summary.md`) |
| 9 | **Operating agreement** — **not** the advisor's 99/1 with her own revocable trust. Either (a) a single-member holding LLC (sole member Nadia), described honestly as disregarded for federal tax, or (b) an agreement reflecting a **real** second owner who actually took the interest by a gift-tax-advised transfer | The advisor's stated reason for the 1% was "we need two partners"; her own revocable trust is not a second partner — `opinion.md` §8.2. **[UNVERIFIED]** grantor-trust / partnership-status point |
| 10 | **Written member consents electing classification** — only if she actually transfers a real interest to a second owner; do **not** try to paper over the trust point with an election | Classification must follow the facts. A real second owner also starts the §7872 exposure ($22,660/yr) and moves the §752 liability share (`opinion.md` §8.2, §8.7) |
| 11 | **Registered-agent and annual-report calendar** (WY annual report if WY is kept; CO annual reports) | `library/state_nexus_summary.md` |
| 12 | **Exclusion schedule** naming the Helio Grid Inc shares as **not** contributed | Protects IRC §1202 — see sections E and G below (`library/irc_1202_excerpt.md`) |
| 13 | **Capital-account and outside-basis workpapers** at formation for each contributed interest (inside basis, liabilities, resulting §752(b) deemed distribution of $19,000 — or $0 if Holdings is disregarded — and resulting outside basis) | §721(a)/§752(b)/§731(a) (`library/irc_721_and_752.md`); also the record needed to resolve the balance-sheet gap later |

## C. Phase 3 — contributions of Services, Properties, Digital — **deferred; see §8.6**

| # | Document | Purpose |
|---|---|---|
| 14 | **Assignment and contribution agreements** — Nadia → Holdings, one per LLC interest, with recitals of §721(a) treatment, effective date, and assignment of the underlying assets | §721(a) (`library/irc_721_and_752.md`) |
| 15 | **Member/manager consents** of each of Services, Properties, Digital approving the change in ownership | Entity formalities |
| 16 | **Amended operating agreements (or single-member certificates of formation)** for the three subsidiaries showing Holdings as sole member | Records the new chain |
| 17 | **Mortgagee consent / lender acknowledgement** for the $1,900,000 nonrecourse mortgage (due-on-sale or change-of-control covenant), or written confirmation from the lender that none applies | The mortgage is the §752 driver; a change-of-control default would dwarf the tax analysis. Client has answered only the recourse question — this remains open, see `QUESTIONS.md` G2 / R3 |
| 18 | **Debt-allocation memorandum** — how the $1.9M nonrecourse mortgage is allocated between the 99% and 1% members (or that Holdings is disregarded and no allocation question arises), and the resulting deemed distribution ($19,000 at the library's 1% figure) | §752(b)/§731(a) (`library/irc_721_and_752.md`); must be re-run before **any** transfer of Holdings interests — a 30% transfer shifts $570,000 and a 99% transfer shifts $1,881,000, which on the pessimistic basis reading produces about $380,000 of §731(a) gain (`opinion.md` §8.7) |
| 19 | **Pre-distribution checklist adopted by the members** — no money distribution or refinancing distribution out of Holdings/Properties without a basis test | §731(a) gain control, given Properties' negative tax capital (`library/irc_721_and_752.md`) |
| 20 | **Lease amendment or confirmation** for the two buildings leased to Services (arm's-length rent, market evidence, separate signatures) | Properties↔Services is a related-party lease; it must be documented, not assumed |

## D. Phase 4 — separateness and "one bank account" replacement

| # | Document | Purpose |
|---|---|---|
| 21 | **Separate bank accounts per entity; account-closing memo** for any commingled account | "One bank account" is commingling evidence that undermines liability protection (`library/irc_7872_afr.md`) |
| 22 | **Separate books, chart of accounts, and monthly close per entity** | Same; also required to support the §752 and §7872 workpapers |
| 23 | **Intercompany services/lease/administrative agreement suite** with arm's-length terms and invoices | Replaces informal transfers with documented transactions |
| 24 | **Manager-member consents for any cross-guarantee, cross-collateral, or upstream pledge** (or a written prohibition) | Piercing risk between the HVAC business and the buildings; no library authority — practice recommendation |
| 25 | **Entity-level minute book / annual consent calendar** for Holdings and each subsidiary | Formalities that make the liability-protection claim real |
| 26 | **Insurance schedule** (GL, auto, workers' comp, umbrella for Services' 42 employees; property at Properties) and confirm Holdings is an additional insured where appropriate | Supports the liability-protection objective that Step 3 would have destroyed |

## E. Helio Grid Inc — what to keep (and never sign)

| # | Document | Purpose |
|---|---|---|
| 27 | **Permanent §1202 file**: Common Stock Purchase Agreement (2020-02-18), SPA §2.3 gross-asset and C-corp/QTIB representations, SPA "original issuance" recital, proof of the $12,000 payment, the §83(b) election (filed 2020-03-02) and the FMV/inclusion facts behind it, and each year's 409A | Establishes original issue, QSB-at-issuance, basis and holding period for the 100% tier (`library/irc_1202_excerpt.md`; `documents/helio_grid_stock_purchase_agreement_excerpt.pdf`) |
| 28 | **Written instruction in the family-office records: Helio shares are not to be contributed to any LLC, partnership, or holding entity** | §1202(h) does not list a contribution to a partnership; the stock ceases to qualify in the entity's hands (`library/irc_1202_excerpt.md`) — up to $9,388,000 of exclusion at stake |
| 29 | **Gift/deed-of-gift and estate-transfer documents** if she wants to move the shares for estate reasons — transfers by **gift or at death** carry over her acquisition character with a tacked holding period. Priority now: confirm her **will / revocable trust actually pass the Helio shares at death**, which needs no pre-sale transfer | §1202(h) (`library/irc_1202_excerpt.md`); gift-tax side is out of scope. **Caution:** a gift made *while a sale is being negotiated* is the classic step-transaction target (`library/step_transaction.md`) — see `opinion.md` §8.5(4) and `QUESTIONS.md` R4(2) on whether a donee gets a separate cap |
| 30 | **Transfer-restriction / ROFR / co-sale review memo** from securities counsel on the full Helio financing documents before any transfer, reorganization, or exit step | **O** — outside the library; the excerpt in the file does not show transfer restrictions (`QUESTIONS.md` R1(4)) |
| 31 | **Exit structuring memo, obtained BEFORE any LOI or term sheet is signed**: confirms the transaction is a sale or exchange of **her shares** and not an asset sale by Helio, a contribution/exchange/rollover of the shares into an acquirer entity, or a blocker structure; and sequences any partial sale against the $10,000,000 per-issuer cap | Preserves §1202(c)(1) original-issue status. With a $9–10M stake value the cap binds above **$10,012,000**, so the structure is worth real money — `opinion.md` §8.4–§8.5 |
| 32 | **Refusal record**: a short note in the file that the advisor's Step 2 inclusion of Helio and Step 4 "reinvest without tax" premise were rejected, with the reason | Creates the contemporaneous record if the exclusion is ever challenged |

## F. Also required (non-tax professionals)

| # | Item | Why |
|---|---|---|
| 33 | Estate plan review — what her revocable trust is actually for, how the three Oakline LLC interests are held by it, and whether the estate documents already pass the **Helio shares at death** without any pre-sale transfer — outside the library | **[UNVERIFIED]** grantor-trust / partnership-status point; §1202(h) covers "by gift, at death" only for the acquisition-character tack (`library/irc_1202_excerpt.md`) — `opinion.md` §8.2, §8.5(6) |
| 34 | Colorado/Wyoming filing map for the revised chain (one 1065 **only** if a genuine partnership exists; her 1040; CO returns; WY annual report if WY is kept) | `library/state_nexus_summary.md`; partnership status is open — `opinion.md` §8.2 |
| 35 | Engagement of a CPA for the imputed-interest true-up, the Properties capital-account reconstruction, and the $1,120,000 accumulated-depreciation position | The $1,760,000 gap must be closed from records, not assumed; recapture is not in the library |
| 36 | Securities counsel for Helio (item 30); insurance broker (item 26); **§1202 specialist** (items 37–41) | Outside the tax library |

## G. Helio exit / M&A execution — new, and time-critical

| # | Document | Purpose |
|---|---|---|
| 37 | **Pre-signing deal-structure review** — written tax sign-off on stock sale vs asset sale by Helio vs merger, and on the consideration mix, obtained **before** the LOI or term sheet is signed | §1202(a) excludes gain on a sale or exchange of **her stock**; the library says nothing about asset-sale or merger mechanics **[UNVERIFIED]** — `opinion.md` §8.5(3) |
| 38 | **Rollover / blocker refusal record** — a note in the file recording that she will not contribute Helio shares to an acquirer LLC, partnership, JV or blocker; if a rollover is unavoidable, a specialist determination that she holds **corporate stock** in her own name | A contribution is not a §1202(h) listed transfer; the rolled portion stops qualifying and cannot be put back (`library/irc_1202_excerpt.md`) — `opinion.md` §8.5(2) |
| 39 | **§1202 evidence file assembled now** from Helio's records: gross assets at 2020-02-18, continuous C-corp status, business lines (QTIB), every 409A with valuation dates, the 83(b) election as filed with the FMV reported, and proof of the $12,000 paid | Deal diligence will not wait for this; the SPA §2.3 representations are the file's only present support for the QSB-at-issuance test — `QUESTIONS.md` R1 |
| 40 | **Escrow / holdback / earnout gain-timing memo** from the §1202 specialist | Nothing in the library addresses installment sales, earnouts or escrows **[UNVERIFIED]** — `opinion.md` §8.4 |
| 41 | **Cap-utilization plan** — single closing vs tranches, and whether any donee holds a separate cap, confirmed by the specialist before structuring | The library states only "per-issuer cap" **[UNVERIFIED]**; the cap binds above a stake value of $10,012,000 — `opinion.md` §8.4 |
| 42 | **Post-closing funding plan for the Oakline entities** — capital-contribution resolutions (item 7b), a written prohibition on new leveraged distributions, and the §731(a)/§752(b) pre-clearance for any transfer of Holdings interests | Removes the §752 trap with equity instead of debt; prevents a repeat of the 2024 leveraged distribution — `opinion.md` §8.7 |
| 43 | **Contemporaneous file note: no entity restructuring between today and closing** (other than the Phase 0 / Phase 4 cleanup), and an acknowledged copy of the §1202 do-not-do list | Substance-over-form and step-transaction exposure is highest on the eve of the sale (`library/step_transaction.md`) — `opinion.md` §8.5(5), §8.6 |
