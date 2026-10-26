A pre-delivery audit is warranted. I'll re-verify every citation against the actual library texts, recomputes all arithmetic, and check cross-file consistency. Starting with the authorities and the files I haven't fully re-read:

The library texts confirm the quotes are faithful ("ceases to qualify in its hands," "not among the listed transfers," "tacked holding period," the §1202(g) condition, and the AFR table with 3.96/4.12/4.58). My earlier read of `agreements_required.md` used a bad path — retrying, along with the remaining files:

A pre-delivery audit is indeed due. I'll verify every citation against the actual library texts, recompute the arithmetic, and check cross-file consistency. Continuing with the files I haven't fully re-read:

The library texts and §1202 excerpt are confirmed. I've now spotted two issues so far: a typo ("aimable") and an unsupported parenthetical about §1202(g). I still need to see opinion.md lines 15–119 (the earlier read was display-truncated), plus the remaining deliverables and the two PDFs:

All four text deliverables are read. The PDFs can't be rendered by this model directly, so I'll extract their text via shell tooling, and in parallel run a full arithmetic re-verification of every figure:

All arithmetic verifies exactly, and the advisor's quoted language matches the proposal PDF verbatim ("when Helio exits, the gain lands in the holding so you can reinvest without tax"). Two citation-supporting library files I haven't re-read this pass, plus the second PDF:

Every library file is now verified verbatim — including the second PDF, which confirms every fact in the "Facts relied on" section (3,000,000 shares at $0.004, original issuance, February 18, 2020, the gross-assets and qualified-trade representations, §83(b) filed March 2, 2020). Cross-reading the library against the opinion surfaced three genuine findings to fix, all in `opinion.md`:

1. **Typo/error:** "interdependent and **aimable** at a single end" — not a word.
2. **Unsupported authority:** an Addendum 1 parenthetical describing §1202(g) as "(share of a partner acquired/sold around a QSBS-holding partnership)" — that's partition-rule detail that is **not** in the library's excerpt (which states only the hold-interest-from-acquisition-onward condition). Per the contract's closed-library rule it must be grounded in the excerpt or dropped.
3. **Arithmetic/logic slippage:** the deferral option says defer "until the mortgage amortizes below her capital contribution" — under the library's rule the trigger is the 1% *shift* (1% × outstanding mortgage) versus her basis, not the mortgage against a contribution. The comparison is wrong as written.

Fixing each:

All three fixes applied. Running the final verification sweep — typo/pattern greps, control-character check, JSON parse, and a citation-whitelist scan against the INDEX across all four deliverables:

All clean. The `[NOT-IN-INDEX]` hits are cross-references to our own companion deliverables (`opinion.md`, `agreements_required.md`) and the client's factual documents (`org_chart.md`, `properties_balance_sheet.md`) — not authority citations, so the INDEX restriction doesn't apply to them; every actual `library/` reference is whitelisted. Zero hits on the three removed error patterns, no control characters or mojibake, and `numbers.json` still parses.

Final check that the three edits landed intact:

The pre-delivery audit is complete. All three fixes are in place and verified.

## What I reviewed

- **All 5 library files** re-read verbatim and checked against every use in the deliverables — including the §1202(h) sentence, the §1202(g)/(c)(1) conditions, the AFR table (3.96/4.12/4.58), the veil-piercing note, and the *Court Holding* cite (324 U.S. 331 (1945)).
- **Both PDFs** (which I re-extracted via text tooling) — the advisor proposal confirms every quoted step and benefit **verbatim**, including "when Helio exits, the gain lands in the holding so you can reinvest without tax"; the Helio SPA excerpt confirms 3,000,000 shares × $0.004, original issuance, Feb 18, 2020, the gross-assets and qualified-trade reps, and the §83(b) filing date.
- **All arithmetic** recomputed from scratch: day counts (968/497/419), catch-up interest ($26,255.34 + $8,088.16 + $6,818.79 = $41,162.30 unrounded; $41,162.29 rounded — the 1¢ artifact stays flagged), annual imputed interest at all three AFRs, basis $12,000, gain range $8,988,000–$9,988,000, cap test, $19,000 Properties estimate, and the deliberately unreconciled $1,380,000 net-asset view. **Everything matches the deliverables exactly.**
- **Cross-file consistency** across `opinion.md`, `numbers.json`, `QUESTIONS.md`, `STATUS.md`, `agreements_required.md` — headline figures, dates, and statuses agree; citation-whitelist scan and mojibake/control-character scan clean; `numbers.json` parses.

## What I found and changed (all in `opinion.md`)

1. **Typo (line 124):** "interdependent and *aimable* at a single end" → "**aimed** at a single end."
2. **Unsupported authority (line 190, Addendum 1):** the parenthetical describing §1202(g) as "(share of a partner acquired/sold around a QSBS-holding partnership)" states partition-rule detail **not contained in the library excerpt** — replaced with the excerpt's own condition: the partner must hold its interest when the partnership acquires the stock and at all times thereafter, cited to `irc_1202_excerpt.md`.
3. **Logic error (line 98, Properties deferral option):** "defer until the mortgage amortizes below her capital contribution" compared the wrong quantities — under the library's §752(b)/§731(a) rule the recognized gain is the 1% *shift* (1% × outstanding mortgage) only insofar as it exceeds her basis. Rewritten to state the deferral test correctly: rebuilt basis superannuating the shrinking shift.

## What I did not change

- No figures moved — every number already verifies; the deliberate $1,380,000-vs-−$380,000 non-reconciliation remains flagged as designed.
- `STATUS.md` stays **COMPLETE WITH OPEN ITEMS**; none of the six open items is affected, so `QUESTIONS.md` and `numbers.json` need no edits.

The deliverable set is ready for delivery. The engagement remains open only client-side: no further questions to ask her, and the conditional true-ups (catch-up interest at actual note-signing, cap check on final proceeds, trust funding after estate counsel confirms it) fire only if deal milestones arrive.