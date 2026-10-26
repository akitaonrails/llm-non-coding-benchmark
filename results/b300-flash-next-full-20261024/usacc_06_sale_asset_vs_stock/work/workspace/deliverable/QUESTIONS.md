# Open questions

Facts that are not in the file and that we were therefore not allowed to assume (per `CONTRACT.md`, rule 1). Each item states what turns on it and, where we can compute it, the dollar size of the unknown. Answers to items 1–6 change numbers; answers to items 7–14 change tactics or documents.

## A. Facts that change the numbers

1. **What is the company's basis in the $200,000 of accounts receivable?**
   The fixed asset register says the receivables "are collected on the cash method and have zero basis in the company" (`documents/fixed_asset_register.csv`) — but Exhibit A allocates them at face, the conversion schedule shows a $200,000 asset on the 1/1/2023 balance sheet, and the memo's base case models basis equal to face (no gain). Which is it: are these the cash-method receivables (gain on collection or sale — ordinary, up to **+$74,000 of tax**, which drops the Lone Star counter from $2,272,000 to **$2,198,000** and widens Hensley's lead from $92,000 to **$166,000**), or are they previously taxed / accrual amounts with face basis? Pull the 2023–2025 returns and the accounts-receivable aging. This is the single largest open item on the Lone Star side.

2. **How much cash will the company hold at closing, and is the Lone Star price inside or on top of it?**
   Exhibit A allocates the entire $3,100,000 to Classes III–VII and omits Class I (cash), while the LOI's financing section says the price is "adjusted for cash" (`documents/loi_buyer_a_asset_purchase.pdf`, §§2, 8). Under §1060 cash belongs in Class I at face (library: `irc_1060_form_8594`). If the cash is *within* the price, goodwill shrinks dollar-for-dollar and reallocates; if *on top*, the adjustment is tax-free cash. The exhibit cannot be completed — or filed on Form 8594 — without the number.

3. **What are the company's liabilities, scheduled and unscheduled?**
   Lone Star assumes *only scheduled trade payables* and requires "no other debt or tax" (`documents/loi_buyer_a_asset_purchase.pdf`, §2); anything unscheduled stays with the company, i.e., with you, and comes out of the asset-sale net dollar-for-dollar. Hensley assumes everything, known and unknown, subject to a 12-month / $285,000 indemnity (`documents/loi_buyer_b_stock_purchase.pdf`, §3). The file contains no liability schedule at all. We deliberately excluded liabilities from every net-after-tax figure in `comparison.json`; that exclusion can only be closed with a payables schedule, a debt list, and a contingent-liability inventory (warranty, employment, environmental, open tax years). This is also where the **Texas franchise tax** exposure lives — flagged in the memo, never computed, because the library has no authority for it (the LOI statements suggest amounts may be outstanding).

4. **Has the company distributed anything to you since 1/1/2023?**
   Your outside stock basis is $420,000 (`documents/tax_history_and_conversion.md`); inside aggregate asset basis is $580,000 (`documents/fixed_asset_register.csv`). The $160,000 gap matters only on the stock route (in the asset sale the inside basis is what gets used), and the library contains **no §§1367/1368 authority** to resolve it. Our labelled, unverified estimate — *if* inside basis exceeds outside basis at the sale and the difference is ordinary (unrecaptured receivables-type) items — is that the liquidation/wind-up cost is roughly **$32,000**, which would widen Hensley's lead from $92,000 to about **$124,000**. Distribution history and the final outside-basis computation settle it.

5. **How much goodwill and trade-name basis is left from the $100,000 held at 1/1/2023?**
   The conversion schedule shows $100,000 of adjusted basis in goodwill and trade name at 1/1/2023 (`documents/tax_history_and_conversion.md`); the file has no amortization history after that date. Every open question's number assumes **$0** remaining (conservative). Actual remaining basis is worth **$0.20 per dollar, up to $20,000**, in every Lone Star scenario and would trim the Class VII gain reported on Form 8594.

6. **What are the consulting terms actually contemplated — and will you sign the covenant?**
   Lone Star's §4 bundles a five-year non-compete **and a consulting agreement** into the single $400,000 line. Is consulting a real obligation (hours, rate, duration)? Compensation for services is ordinary income whatever the allocation says (library: `irc_197_and_noncompete`), so a real consulting arrangement should sit **outside** the purchase price at market rates — that is our counter's drafting condition. Conversely, if you would not sign even a $100,000 covenant, the counter changes shape and Lone Star's value rises by $17,000 (to $2,289,000) — but a signed covenant allocated at $0 invites recharacterization (memo §6.5), so the answer is a drafting fact, not just a preference.

## B. Status, negotiation and mechanics

7. **Is either deal still open?** Lone Star's exclusivity bound you for 45 days from 3/30/2026 — through roughly 5/14/2026 — and today is 10/26/2026. Nothing in the file records an extension, termination, or counter-offer on either LOI, and both prices are now six to seven months old (`documents/loi_buyer_a_asset_purchase.pdf`, §5; memo §7). Before any of this advice is executed, confirm both buyers are live and whether either LOI has been amended since.

8. **Will Hensley pay for §338(h)(10)/§336(e) consent, and does he even qualify to ask?**
   The election is worth roughly a $2,520,000 step-up to Hensley and costs you $276,700–$387,200 (memo §3.6); our recommended stance is consent priced at **+$400,000 minimum**. Confirm: (a) his reaction in term-sheet stage, before diligence leverage disappears; (b) that you are in fact the **100%** member — LOI B recites "100% of the membership interests," but the LLC operating agreement is not in the file, and if there is a second member the election needs their consent too (separate leverage, and it would change the deemed-sale math in `comparison.json`).

9. **Is Lone Star's "all cash" real?** The LOI says financed ("the purchase price is adjusted for cash") but the file contains no commitment letter or proof of funds (§8 of the LOI). A cash buyer who cannot close is worse than the unsecured note.

10. **Note mechanics with Hensley — and what is his balance sheet?**
    "5 years, 6% interest, annual principal" is modeled as $100,000 of principal a year (memo Table 6: $90,000 of total interest, $56,700 after tax). Confirm the amortization convention, annual interest due dates, and prepayment rights. More fundamentally: the note is **unsecured**, from a buyer with no disclosed balance sheet, taking the company you are selling. The memo recommends security, a guaranty, a reduced note, or all cash — each is a negotiating ask that needs a factual answer from the buyer.

11. **What are Lone Star's indemnity, escrow and survival terms?** The LOI is silent (it only says liabilities and taxes stay clean). Hensley offers a $100,000 escrow and a 12-month, $285,000-cap indemnity. A silent asset-sale LOI usually converts into a indemnity package with escrow and longer survival — those terms shift value and must be compared, not assumed.

12. **Are there liens or secured debt on the equipment or receivables?** Nothing in the file. A UCC search matters twice: it tests Lone Star's "no other debt" closing condition, and a secured lender's lien on the assets would sit on the very equipment Exhibit A is arguing about.

13. **Can the closing be moved past 12/31/2027 — with Lone Star?** After the §1374 period the counter's asset-sale net is $2,509,300, ahead of Hensley's $2,364,000 (memo §4). If Lone Star will accept a late-2027/2028 closing, or structure a deferral of the goodwill component, the ranking flips. This is a question for Lone Star, not a research task.

14. **Which tax year do you intend to report the consulting/covenant income in, and where will you reside after closing?** No state individual income tax now (memo §1); if you move, state tax on a 2027–2028 installment stream and on the consulting income could matter. Outside the library's scope — flagging, not advising.
