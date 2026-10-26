Client answered two items (refinance uncertainty; husband's bonuses are recurring, 2025 ≈ $40k). Recomputing the affected numbers before editing deliverables:

Now updating the deliverables. First `division.json`:

The edit tool hit a wrong-path error. Let me verify the actual deliverable paths first.

Path resolved: the real location is `/work/workspace/deliverable/` (the `/workspace` alias is gone). Reading current deliverables to make targeted edits:

Now updating `division.json` — first the `undisclosed_income` recurrence evidence:

Now the refinance contingency in Alternative A and the new Alternative D:

Now `child_support.json` — adding the 2025-level bonus scenario and recurrence finding:

Now reading `advice.md` to rework §2 into a decision tree:

Now reworking `advice.md`. First §1 (recurring bonus):

Now replacing §2 with the decision tree:

Now §4, §6, and §7:

Now reading the current `QUESTIONS.md` before rewriting it as a registry:

Now updating `STATUS.md`:

Now validating JSON syntax and citation integrity:

Validation is clean — both JSON files parse, and the only non-INDEX `.md` mention is deliverables referencing themselves, not a citation. Quick final check that Alternative D landed correctly:

Engagement continued and all deliverables updated through the client's reply. Summary of this turn:

**What the client's answers changed**

1. **`division.json`**
   - `undisclosed_income`: now records the recurrence evidence ("always gets a bonus"; 2025 ≈ $40,000, client recollection, flagged unverified) and cites the child-support guidelines alongside the equitable-distribution rule.
   - Alternative A: added a **refinance contingency** (fixed window; deed passes only at/after refinance; explicit warning not to default to quitclaim-then-solo-later-sale) plus a fallback pointer to B/D.
   - **New Alternative D — deferred co-owned sale**: both parties stay on title after the decree, Wife gets exclusive occupancy under the divorce instrument, sale at children's exit (3–6 years). Per §121(b)(1) + §121(d)(3)(A) as excerpted in the library, each still-owner claims $250,000 → combined $500,000 exclusion without a joint return: gain 734,000 ÷ 2 = 367,000 each − 250,000 = 117,000 × 18.8% = 21,996 each, total 43,992; **each side 619,484** — identical to a sale-now-joint-return, but the kids stay put, and ≈$47,000 better than her owning alone at a later sale.

2. **`child_support.json`** — added the 2025-level bonus scenario (gross 208,000 → share **2,004/mo**) and the recurrence finding; noted the month-35/36 step-down when maintenance ends.

3. **`advice.md`** — §2 rebuilt as a decision tree: Step 1 pre-approval (26% of inflow years 1–3 vs **44% in years 4–6** after the support/maintenance cliff) → Plan 1 refinance → Plan 2 Alternative D → Plan 3 sell now; the "refuse" structure (full title transfer, no contingency, ~$47,000 tax gift) is called out. §1, §4, §6, §7 updated with the recurring-bonus finding and revised unknowns.

4. **`QUESTIONS.md`** — rewritten as a **registry**: Part 1 answers (refinance uncertainty, recurring bonus) mapped to their effects; Part 2 eight explicitly flagged unknowns (lender qualification, 2025 amount, decree timing, her tax rate, housing costs, 16.2(e) quantum, September-money tracing, value drift). No new outbound questions, per the client's instruction.

5. **`STATUS.md`** — **COMPLETE WITH OPEN ITEMS**, with the revised core findings (now including Alternative D) and the numbered open-items list.

Verification: both JSON files parse; all 6 library citations resolve against `library/INDEX.md`; the path confusion from earlier is resolved (edits used `/work/workspace/deliverable/`).