

Client answers confirmed. Updating the deliverables to close those assumptions, then re-checking the remaining open items.





The confirmed affiliate use surfaces a drafting knock-on: §1.6 "Users" and §1.2 "Customer Data" only cover *Customer's* employees/drivers/customers — so the §2.2 fix must extend those definitions too. Updating all deliverables now.





Now updating `redlines.md` — the Exhibit C Annex detail (data types now confirmed) and the expanded A5 fix:





Now I have the exact text. Making the Exhibit C and §5 edits while pulling the remaining deliverables in parallel:










All three redlines edits landed. Now syncing the one-pager, QUESTIONS.md, and STATUS.md to the confirmed facts:











All edits applied. Final validation pass on `issues.json` and a cross-file consistency sweep:





All five deliverables now reflect the client's answers, and `issues.json` re-validates (8 items, schema OK, ranks 1–8, five hard / one preferred / two notes).

## What changed after the client's answers

**Closed by confirmation (2026-10-25):**
- **Affiliate use (rank 5, A5)** — firm, not theoretical. Both affiliates will use the platform and Holdings signs in its own name, so the "Holdings signs on behalf of affiliates" alternative isn't available; the §2.2 license fix is the only route.
- **EU data scope (rank 1, A2)** — driver names, locations, working hours, customer addresses are now hard-coded into Exhibit C **Annex 1**, which is no longer a blank skeleton but a populated processing-particulars annex.

**New drafting knock-on found from the confirmation:** §1.6 "Users" covers only *Customer's* employees/contractors and §1.2 "Customer Data" only *Customer's* drivers/customers — so fixing §2.2 alone would still leave affiliate personnel unlicensed and EU affiliate data outside the DPA. `redlines.md` §5 now contains drop-in replacements for **§2.2 + §1.6 + §1.2** together, and the DPA roles clause was rewritten to cover affiliate personnel and a belt-and-suspenders "affiliate as independent controller joins the DPA" alternative.

**Remaining unknowns — flagged explicitly, not re-asked** (QUESTIONS.md rewritten as an answered-log + flagged-unknowns file; STATUS.md and the one-pager footer mirror it):
1. Which entity is the Art. 28 controller (Holdings vs. the B.V.) — drafting works either way; controller-to-controller mechanics sit outside the library and are flagged unverified, not cited.
2. EU go-live date — defaulted to Service Start Date; the DPA-at-signing redline is date-independent anyway.
3. RouteWise's standard DPA — becomes a vendor ask in the redline exchange.
4. Fleet vs. the 350-vehicle cap — commercial check; if exceeded, must be fixed in the Order Form, which controls over the MSA (§14.1).
5. Leverage posture — default held: sign nothing until the DPA and cap carve-out land.

**STATUS: COMPLETE WITH OPEN ITEMS** — the review itself is done; what remains (RouteWise's DPA form, the fleet check) depends on the vendor/commercial side, not on this review. Send-ready package is in `workspace/deliverable/`.