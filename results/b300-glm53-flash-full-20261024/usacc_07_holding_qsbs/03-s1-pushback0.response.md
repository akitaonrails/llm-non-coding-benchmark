The advisor's claim and my verdict are in direct conflict, so this deserves a precise, library-grounded written answer. Let me re-check the exact §1202 language and the step-transaction authority before responding:

The library settles this precisely, so I'll answer it fully in the opinion file — the client deserves the written reasoning, and the advice needs to be defensible against what her advisor told her. Let me record it:

The scope line is updated. Now let me get the exact anchor text for the remaining edits — the end of `opinion.md`, the assumptions block in `numbers.json`, and the current state of `QUESTIONS.md` and `STATUS.md`:

I have all the anchors I need. Executing the updates — appending Addendum 2 to `opinion.md`, updating `STATUS.md`, and reading the full tail of the `numbers.json` assumptions string for its edit:

`opinion.md` and `STATUS.md` are updated. Now the `numbers.json` assumptions extension and the `QUESTIONS.md` ledger entry (item 4 first, then the header retitle, since they're the same file):

Now the `QUESTIONS.md` header retitle, then I'll verify everything — JSON validity, the tail of `opinion.md`, and a scan for stray characters in the new text:

The JSON parses cleanly and the append is in place. One phrase on line 209 is garbled ("added after paying for the structure") — fixing that while I read the rest of the addendum to its end:

The addendum is complete and coherent. Final verification — the ledger file and a cross-check that every citation in the new text stays on the library whitelist:

All citations in the new content are within the whitelist. The last grep used a malformed character class (it caught plain `"` quote characters — false positives from my own pattern), so let me run a proper stray-character check to close out:

DONE — mojibake scan clean across all four files. The follow-up is fully answered and recorded. Summary of what went where:

## Direct answer to your question (now in `opinion.md`, Addendum 2)

**Who's right: the written opinion, and the difference is the entire exclusion.**

| | Sell personally (recommended) | Advisor's "gain lands in the LLC" |
|---|---|---|
| Gain at your $9–10M exit | $8,988,000 – $9,988,000 | same |
| Stock qualifies in the holder's hands (§1202(c)) | Yes — you bought at original issue, Feb 2020 | No — contribution isn't a preserving transfer (§1202(h)); the stock *ceases to qualify* in the partnership's hands |
| Excludable | Full gain (under the $10M cap at both ends) | **$0** |
| Where tax lands | Excluded | Flows through and is taxed at your level anyway (plus 1% to the trust), with Colorado filings |

Why the advisor is backwards: **§1202(g)** — the real partnership rule his claim gestures at — only passes the exclusion through when the *partnership itself buys the stock at original issue* with your membership in place from day one. A partnership that *receives* your personal stock never qualifies for it. And a pre-planned contribute → sell → distribute sequence risks being collapsed by the step doctrine — if collapsed, you just did paperwork to get the same direct sale; if not collapsed, the exclusion is already gone. No upside either way.

**Can the holding own it after the sale?** After closing, there *is* no stock — you'd hold cash. Yes: the proceeds can go into Holdings once the exclusion is banked (§721(a), nonrecognition, harmless) — just don't expect the holding to be a tax-avoidance device; its income flows through to you annually. Same rule applies to any future founder stock: stay outside until *that* exclusion is banked.

## Files updated
- `workspace/deliverable/opinion.md` — scope line + **Addendum 2** (question verbatim, the four-gate analysis, side-by-side table, paired with the narrow legitimate §1202(g) pattern and the post-sale answer)
- `workspace/deliverable/QUESTIONS.md` — Resolved item 4 (the follow-up), header now "answers and follow-up"
- `workspace/deliverable/STATUS.md` — deliverables note mentions Addendum 2
- `workspace/deliverable/numbers.json` — assumption note extending the 0-vs-full-exclusion contrast (JSON still parses clean)

All citations remain within `library/INDEX.md`; the unverified flags (demand-loan AFR rule, full-statute conditions at 1202(g), sale-time conditions beyond the excerpt) are carried forward unchanged. Status: **COMPLETE WITH OPEN ITEMS**, as before.