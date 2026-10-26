

I'll start by reading the contract and exploring the workspace structure.





I have all the library and document contents. Now let me run the probability and exposure arithmetic.





Now I'll write the deliverables. First, the memo:





The deliverables are drafted. Before closing, let me make the §7 arithmetic fully self-consistent (rows must sum to 100%) and regenerate every number from one clean model.





The script accumulated dead branches — let me rewrite it clean and run it.





The memo's §7 is the older first-pass model. Let me compute the exact cost-side endpoints, then rewrite §7.1–7.3 and align §2 with the final model.





All numbers are final. Now I'll check every stale reference in the memo before rewriting §7 and §2.





Now I'll rewrite §7.1–7.3 with the final model and update the four §2 lines and the §6 line.





One grid cell needs correcting (the 0.875/20% cell must use the friendly-corner reas=20% value, 7.0%, not 5.6%).





Now the §2 Brief Answer lines and the §6 recommendation line.





I need to repair §4.1 — one of my parallel edits clobbered the prediction paragraph — and fix a typo in §7.3.






STATUS.md is already current. Final validation pass:





Aligning the §4.6 remedy-path table with the final model so the memo has one arithmetic voice:





The deliverable is complete and internally consistent. This pass rebuilt the §7 arithmetic as a single fully-partitioned decision tree (`/tmp/opencode/calc3.py`) and reconciled every number in the memo to it.

**Final figures carried through the memo** (all shown with arithmetic and a sensitivity grid in §7):

| Quantity | Point | Range |
|---|---|---|
| P(California law governs) | 87.5% | 70–98% |
| P(any court order of any kind) | 3.1% | 1.3–7.2% |
| P(order that actually ends the Kestrel job) | 0.7% | 0.2–2.0% |
| P(§8 void as to Zhao, if litigated under CA law) | 90% | — |
| P(Meridian creates §16600.5 liability by filing) | 85% | 65–97% |
| EV(filing) | −$536k | −$232k to −$805k |
| "Wins everything" branch | still −$220k | — |

Every outcome cell now sums to 100% per branch, so no probability leaks; §7.4 (pattern exposure) remains deliberately unreconciled with §7.3 because it depends on the unknown California headcount.

**Also fixed this pass:** the §16600.5 typo in the old Recommendation text; the clobbered choice-of-law confidence paragraph in §4.1 (restored with the sensitivity reasoning: why 87.5% is not 99% — prong (a), no library authority extending §925 to out-of-state employers — and why it is not 50% — *Nedlloyd*'s substantiality holding, §16600.5(b)'s anti-avoidance text); the remedies path-table in §4.6 now matches the tree; `citations.json` `library_file` values normalized to verified `library/...` paths.

**Final validation:** JSON parses; 20 entries; every file exists and appears in `library/INDEX.md`; statuses within `in force|superseded|vacated`; the only uncited INDEX items are the two memo-bank memos (background, handled in memo §6.9–6.10); no stale numbers from the superseded earlier models remain anywhere in the memo.

**Bottom line unchanged:** don't file, don't send a §8 demand letter, enforce §10 and fix the form; Zhao's exit is a compliance problem (LO-233 + the §16600.1(a) inclusion violation), not a litigation opportunity. STATUS is **COMPLETE WITH OPEN ITEMS** — the conclusion is robust to all open items, but Q2 (has a demand letter already gone out?) and Q13 (the Alvarez matter) could reveal liability that already accrued, so those are flagged as urgent rather than closed.