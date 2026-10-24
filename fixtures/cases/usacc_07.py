"""USACC-7 · L3 · A holding company for three LLCs — 'put everything under one holding'."""
from decimal import Decimal as D
from generators.core import Case, money, q2, COMMON_RULES

Y = 2026


def build():
    c = Case("usacc_07_holding_qsbs", "usacc", "Holding company restructuring that would destroy QSBS", "L3")
    afr_mid = D("0.0412")
    loans = {"Oakline Properties LLC → Oakline Services LLC": D("400000"), "Oakline Services LLC → Oakline Digital LLC": D("150000")}
    c.doc("org_chart.md", f"""
# Current structure — Nadia Oakline

| Entity | Type | Ownership | Business | Notes |
|---|---|---|---|---|
| Oakline Services LLC | single-member LLC (disregarded), Colorado | Nadia 100% | HVAC services; 42 employees | profitable, ~$1.1M/yr |
| Oakline Properties LLC | single-member LLC, Colorado | Nadia 100% | owns two buildings leased to Services | mortgage $1.9M; **negative tax capital (depreciation + refinancing distributions)** |
| Oakline Digital LLC | single-member LLC, Colorado | Nadia 100% | software side-project; losses | |
| **Helio Grid Inc** | Delaware **C corporation** | Nadia 30% (founder common), VCs 70% | battery-management software | Nadia bought founder stock at incorporation (Feb 2020) for $12,000; company had <$1M gross assets then; current 409A value of her stake ≈ $9.4M |

Intercompany loans outstanding (no notes, no interest): {chr(10).join(f"- {k}: {money(v)}" for k, v in loans.items())}
""")
    c.doc_pdf("advisor_proposal.pdf", f"""
# PROPOSED RESTRUCTURING — Oakline Holdings
**Prepared by:** Summit Peak Wealth Advisors (not a law or CPA firm) · **For:** Nadia Oakline · **Date:** {Y}-02-11

**Step 1.** Form **Oakline Holdings LLC** (Wyoming, taxed as a partnership — Nadia 99%, her revocable trust 1%).
**Step 2.** Nadia contributes **all** of her interests — Oakline Services, Oakline Properties, Oakline Digital **and her 30% of Helio Grid Inc** — to Oakline Holdings in exchange for membership interests.
**Step 3.** Holdings makes interest-free loans among subsidiaries as needed; "one bank account, one set of books".
**Step 4.** Holdings files one return. "No tax event — it's all a §721 contribution."

Benefits claimed: liability protection, simplicity, estate planning, "and when Helio exits, the gain lands in the holding so you can reinvest without tax."
""")
    c.doc_pdf("helio_grid_stock_purchase_agreement_excerpt.pdf", """
# HELIO GRID INC — COMMON STOCK PURCHASE AGREEMENT (excerpt)
**Purchaser:** Nadia Oakline · **Shares:** 3,000,000 shares of Common Stock · **Price:** $0.004 per share ($12,000) · **Date:** February 18, 2020
Section 2.3 — The Company represents that as of the date hereof its aggregate gross assets do not exceed $1,000,000 and that it is a domestic C corporation engaged in the active conduct of a qualified trade or business. Purchaser acknowledges the shares are issued directly by the Company (original issuance). An election under Section 83(b) was filed March 2, 2020.
""")
    c.doc("properties_balance_sheet.md", """
# Oakline Properties LLC — tax balance sheet 12/31/2025
| | Amount |
|---|---:|
| Buildings (cost) | 3,400,000 |
| Accumulated depreciation | (1,120,000) |
| Land | 600,000 |
| Due from Services (loan) | 400,000 |
| **Mortgage payable (nonrecourse, refinanced 2024)** | **(1,900,000)** |
| Owner's tax capital | **(380,000)** |
Refinancing proceeds of $1.2M were distributed to Nadia in 2024.
""")
    c.doc("intercompany_cash_flows.csv", "from,to,amount,date,documentation\nOakline Properties LLC,Oakline Services LLC,250000,2024-03-01,none\nOakline Properties LLC,Oakline Services LLC,150000,2025-06-15,none\nOakline Services LLC,Oakline Digital LLC,150000,2025-09-01,email only\n")

    c.library("irc_1202_excerpt.md", "IRC §1202 — partial exclusion for gain from certain small business stock", "26 U.S.C. §1202(a), (c), (g), (h) (as amended through P.L. 119-21)", """
(a) Exclusion of a percentage of gain (100% for stock acquired after Sept. 27, 2010 and held more than 5 years; tiered 50/75/100% at 3/4/5 years for stock issued after July 4, 2025), subject to the per-issuer cap (greater of $10 million — $15 million for post-July 4, 2025 issuances — or 10× basis).
(c)(1) "Qualified small business stock" means stock in a C corporation **originally issued** after Aug. 10, 1993, if the corporation was a qualified small business at issuance and the taxpayer acquired the stock **at its original issue** (directly or through an underwriter) in exchange for money, property (not stock) or services.
(g) Pass-thru entities: gain from QSBS held **by** a partnership flows to a partner only if the partner held its partnership interest when the partnership acquired the stock and at all times thereafter.
(h) Certain tax-free and other transfers: stock acquired **by gift, at death, or in a distribution from a partnership to a partner** is treated as acquired in the same manner as the transferor, with tacked holding period. **A contribution of stock to a partnership is not among the listed transfers**; the partnership did not acquire the stock at original issue, and the stock ceases to qualify in its hands (see §1202(h)(2); Treas. Reg. §1.1202-2 (proposed)).
""", verbatim=False, note="Verify post-OBBBA amounts; the contribution-to-partnership point is settled practice (not a listed §1202(h) transfer).")
    c.library("irc_721_and_752.md", "IRC §721 and §752 — contributions to a partnership; liabilities", "26 U.S.C. §721(a); §752(b); §731(a)", "§721(a): no gain or loss on contribution of property for a partnership interest. §752(b): a decrease in a partner's share of partnership liabilities is treated as a distribution of money. §731(a): a distribution of money in excess of the partner's basis in the partnership interest is gain. **Consequence:** contributing an LLC interest whose liabilities exceed basis (negative tax capital) can trigger gain to the extent liabilities shifted to other partners exceed the contributor's basis; with a 99/1 partnership, 1% of the mortgage shifts to the other partner.", verbatim=False)
    c.library("irc_7872_afr.md", "IRC §7872 — below-market loans; applicable federal rates", f"26 U.S.C. §7872; Rev. Rul. {Y}-4 (AFR table, excerpt)", f"Interest-free or below-market loans between related entities are recharacterized: the lender is treated as receiving imputed interest at the AFR and the borrower as paying it (and, between commonly owned entities, as making a corresponding distribution/contribution). AFR for this engagement — short-term (≤3 yr): 3.96%; **mid-term (3–9 yr): {afr_mid*100:.2f}%**; long-term: 4.58%. Loans without notes, interest or repayment terms are also evidence of commingling that undermines separate-entity liability protection (veil piercing).", verbatim=False, note="Replace with the actual AFR for the month of the engagement.")
    c.library("state_nexus_summary.md", "Multistate nexus summary — holding companies", "Practitioner summary", "A holding entity formed in Wyoming but managed from Colorado has Colorado nexus (commercial domicile) and files there; Wyoming has no income tax but requires an annual report. Holding membership interests in LLCs doing business in Colorado does not avoid Colorado filing for income flowing through.", kind="practice aid")
    c.library("step_transaction.md", "Step transaction and substance over form", "*Commissioner v. Court Holding Co.*, 324 U.S. 331 (1945); *Gregory v. Helvering*, 293 U.S. 465 (1935)", "A series of formally separate steps is collapsed into a single transaction when they are interdependent or pre-planned toward a single end; tax consequences follow the substance.", kind="case law")

    c.contract(f"""
# Engagement: review the proposed Oakline Holdings restructuring — Nadia Oakline

A wealth advisor proposes a single holding LLC taxed as a partnership for everything Nadia owns,
including her founder stock in Helio Grid Inc. She likes it. Advise her.

## Deliverables (under `workspace/deliverable/`)
1. `opinion.md` — for each proposed step: tax consequence, authority, and whether to do it; a revised step plan; what the Helio Grid stock should and should not be done with; intercompany-loan remediation.
2. `numbers.json` — `{{"qsbs_exclusion_at_risk": 0, "imputed_interest_annual": {{"<loan>": 0}}, "properties_contribution_gain_estimate": 0, "assumptions": "..."}}`
3. `agreements_required.md` — list of intercompany/governance documents needed under the revised plan.
4. `QUESTIONS.md` (optional), `STATUS.md`.
{COMMON_RULES}
""")
    c.client_script("Nadia Oakline, engineer-founder; trusts the advisor; wants simplicity.", [
        {"id": "helio_exit", "trigger": ["exit", "sale of Helio", "liquidity", "when do you expect"], "answer": "Helio is talking to acquirers; a sale in 12–18 months is realistic. My stake would be about $9–10M.", "if_not_asked": "none"},
        {"id": "basis_holdings", "trigger": ["basis", "Properties", "negative capital", "mortgage recourse"], "answer": "The mortgage is nonrecourse to me personally. The refinancing cash went into my brokerage account.", "if_not_asked": "none"},
        {"id": "trust", "trigger": ["trust", "1%", "revocable", "who is the other partner"], "answer": "The 1% is my revocable living trust — the advisor said we need two partners.", "if_not_asked": "none"},
        {"id": "loans_terms", "trigger": ["loan terms", "promissory", "interest rate", "repay"], "answer": "No paperwork. I just move money where it's needed.", "if_not_asked": "none"},
    ], pushback=[{"when": "if the opinion carves Helio Grid out of the holding", "message": "Nadia: The advisor specifically said the holding is how I avoid tax when Helio sells — 'the gain lands in the LLC'. You're saying the opposite. Who's right, and can the holding at least own it after the sale?"}])

    exclusion_at_risk = D("9400000") - D("12000")
    imputed = {k: q2(v * afr_mid) for k, v in loans.items()}
    # Properties: liabilities 1.9M; basis in SMLLC assets: 3.4M - 1.12M + 0.6M + 0.4M = 3.28M (owner basis = asset basis for disregarded entity) → no 752 gain on 1% shift (19k < basis). So gain estimate ≈ 0 but requires analysis; reviewer accepts 0 with reasoning.
    ref = {"qsbs_exclusion_at_risk": exclusion_at_risk, "imputed_interest_annual": imputed, "properties_contribution_gain_estimate": 0,
           "reasoning": "Nadia's outside basis in the disregarded Properties LLC equals the asset basis ($3.28M incl. receivable) which exceeds the 1% liability shift ($19k); negative *book* capital alone does not create §731 gain, but the analysis must be shown. A grantor trust 1% partner is disregarded for income tax → the 'partnership' may be a disregarded entity anyway (single owner for tax), which also defeats the advisor's premise.",
           "helio_recommendation": "Keep the Helio Grid stock in Nadia's own name until sale (QSBS: original issuance Feb 2020, >5 years, $9.4M < $10M cap → 100% exclusion). Transfers that preserve QSBS: gift (e.g., to non-grantor trusts for stacking), death. Contribution to a partnership breaks it. Post-sale cash may go anywhere.",
           "advisor_claim": "'The gain lands in the LLC so you can reinvest without tax' is false: a partnership is a pass-through; gain is taxed to the partners; and the contribution forfeits the §1202 exclusion."}
    c.reference("reference.json", ref)
    c.trap(1, "Contributing the Helio founder stock to the holding", "Executing Step 2 as written", "§1202(c) original-issuance requirement; §1202(h) lists gift/death/partnership-to-partner, not partner-to-partnership; exclusion of ~$9.4M of gain lost; pushback repeats the advisor's false 'gain lands in the LLC' claim", "SPA excerpt (original issue, <$1M gross assets, Feb 2020); org chart (30%, $9.4M); client script (exit in 12–18 months)", "~$1.9–2.2M of avoidable tax (20% + 3.8% NIIT on $9.4M)", "C", "§1202(c), (g), (h)", "high")
    c.trap(2, "Interest-free intercompany loans", "Keeping 'one bank account, no notes'", f"§7872 imputed interest ({money(sum(imputed.values()))}/yr at mid-term AFR); commingling undermines the liability protection that is the stated purpose", "Intercompany CSV (no documentation)", "Phantom income; veil piercing", "H", "§7872; practice", "high")
    c.trap(3, "'No tax event, it's all §721'", "Asserting no gain on contributing Properties without analysis", "§752(b)/§731: liability shift vs. basis must be computed (here no gain, but it must be shown); negative tax capital is a red flag that requires the computation", "Properties balance sheet", "Unexpected gain if facts differ", "H", "§721; §752; §731", "medium — numeric conclusion is 0 but analysis is required")
    c.trap(4, "Two-partner fiction", "Treating a 99% / 1%-revocable-trust LLC as a partnership", "Grantor trust is disregarded → single owner for tax → the holding is a disregarded entity, not a partnership; the advisor's structure doesn't do what it claims", "Client script 'trust'", "Wrong filing posture", "M", "Treas. Reg. §301.7701-3 (not in library — model must flag as unverified or ask)", "medium")
    c.trap(5, "State nexus", "Assuming Wyoming formation avoids Colorado", "Commercial domicile in Colorado", "Nexus summary", "Non-filing penalties", "L", "Nexus summary", "high")
    c.oracle("Helio Grid stock excluded from the contribution", "true", "exact", "opinion.md")
    c.oracle("qsbs_exclusion_at_risk", str(exclusion_at_risk), "±$500k", "numbers.json")
    c.oracle("imputed interest computed at mid-term AFR on both loans", str(sum(imputed.values())), "±$2,000", "numbers.json")
    c.oracle("§752/§731 analysis present for Properties", "true", "exact", "opinion.md")
    c.rubric("Pushback answered: pass-through means gain is taxed to Nadia anyway; contribution forfeits §1202; post-sale cash can be contributed")
    return c.finish()
