

Before fixing anything, let me audit the deliverable line by line: recompute every figure, and check every legal assertion against the library text.






All figures reconcile. The audit found five authority/rigor issues to fix. Let me view the exact passages:





All figures reconcile. Before writing the fixes, let me verify the exact library wording for the passages I'm about to soften (the "ex.:" in Lei 7.713 art. 21, the CSLL line, and the dividend-exemption condition):





Library wording confirmed: `ex.:` is non-exhaustive, the CSLL line mentions only 9%, and the exemption is conditioned on approval until 31/12/2025. One last check on the criminal-type file, then I apply the fixes:





All library texts confirmed. Now I'll apply the fixes — nine edits to `memorando.md`, and read the other two files to get their exact current text:















Two anchors slightly off — fixing with the actual text:






All edits applied. Final read-through of the three files to make sure everything flows cleanly:






Minha verificação rápida usou os caminhos das chaves errados — o JSON tem um schema aninhado. Reexecutando corretamente:





Review complete. All arithmetic was re-verified in Python, every citation was checked against the six files in `library/`, and the JSON schema validation passes. Here is what I found and changed.

## What was already correct (re-verified, unchanged)
- All figures reconcile: GCAP R$ 585.000/sócio (15%, 1st bracket); IRPJ R$ 1.869.000; CSLL R$ 675.000; IRRF R$ 705.600; net A = R$ 7.830.000 vs B = R$ 6.350.400 (difference R$ 1.479.600); break-even ≈ R$ 12.090.909; hypothetical revaluation R$ 154.000/sócio. `comparativo.json` untouched.
- Every legal citation traces to a file in `library/` — no fabricated authority found.

## Fixes applied

**`memorando.md` (9 edits):**
1. **§4.2 item 1 and §4** — the library writes "(ex.: Lei 14.973/2024…)" — an example, not a closed list. Removed the claim that it is "the only applicable one"; now stated as: the library does not close the list, no other hypothesis is verifiable with the material, and the only confirmed one has its **deadline closed**.
2. **§2 IRRF note** — "potentially higher final rate than 10%" was one-directional and unsupported: IRPFM rates are not in the library. Now: the adjustment can be **higher or lower** than 10%, not quantifiable.
3. **§2 CSLL** — added note: the library mentions only 9%, no additional; if there is any additional not covered there, **B gets worse** (unverifiable).
4. **§4.2 item 3** — "the offense has no floor" was asserted as fact; the library only doesn't state a floor. Now attributed to the library's wording.
5. **§6 items 1 and 6** — equity collateral assignment, guarantee, escrow: flagged as market practices **not covered by the library (unverified)**, to be validated with counsel.
6. **Premise (ii)** — the text of Law 7.713 art. 21 refers to "monetary correction, if any"; interest is not addressed in the library — language aligned, with that point flagged.
7. **New §3 "Robustness"** — (a) even with **zero IRRF**, B caps at R$ 7.056.000 and A still leads by **R$ 774.000**, requiring ~70.6 months of drip distributions per partner while keeping the shell alive; (b) pre-2025 profits cannot flip the result: exemption requires distribution approved by 31/12/2025 — if approved, it is a partner credit in **both** proposals (cancels out); if not, the deadline is closed.

**`PERGUNTAS.md`** — added item 8 (pre-2025 reserves: no answer, open flag, but with no effect on the ranking for the dual logic above) and rewrote the closing: no unknown favors B, including the only theoretical candidate (item 8).

**`STATUS.md`** — review-round paragraph recording the fixes; open item 8 added; risk-direction line updated (items 2, 5, 6 + possible unaddressed CSLL additional can only worsen B; even with IRRF zero A leads by R$ 774.000). The "only revaluation hypothesis" wording in Round 3 was also softened to "as an example", consistent with fix 1.

Status remains **COMPLETE WITH OPEN ITEMS**; the recommendation (PF / Proposal A, DIRPF not amended) and the JSON figures did not change — the review only corrected overstatement of authority and made the recommendation's robustness explicit.