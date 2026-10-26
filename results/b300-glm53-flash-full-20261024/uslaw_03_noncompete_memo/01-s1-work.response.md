The PDF needs text extraction — let me try Python.

I have the full picture from the library and documents. Now let me run the date and scenario arithmetic with Python before drafting.

The offer-date arithmetic line printed awkwardly — let me re-run a clean version whose numbers I can quote verbatim in the memo.

All sources are consistent. Now I'll write the deliverables.

Let me check for stray non-ASCII characters that may have slipped into the memo text:

That last edit inserted unwanted text. Let me fix it properly:

Clean. Now let me proofread the full memo once through:

All prior work is intact (`memo.md` complete). The memo cites exactly 20 authorities, all of which appear in INDEX.md. Let me re-verify the library texts so each `proposition` in citations.json is faithful, then build the three remaining deliverables.

All 20 authority texts verified. Now checking the memo's assumption and question sections so `QUESTIONS.md` aligns exactly with what the analysis flagged as open:

Both assumptions and open items are clear. Writing the three remaining deliverables now:

Validating `citations.json` against `INDEX.md` programmatically:

Validation clean: 20/20 entries, statuses match INDEX verbatim, full coverage of the citable universe. Now `QUESTIONS.md` and `STATUS.md`:

Now `STATUS.md`:

Final QC pass — checking for stray tokens and verifying the status count I stated in STATUS.md:

One correction in STATUS.md (16 in force, not 15):

All deliverables are complete and verified. Engagement summary:

**Deliverables in `workspace/deliverable/`:**

| File | Contents |
|---|---|
| `memo.md` | Full six-part memo: Question Presented, Brief Answer, Facts, Analysis (choice of law, both states' enforceability, §925, §16600.5 exposure, AB 1076, remedies/fees), strongest arguments per side, Recommendation |
| `citations.json` | Exactly 20 entries — validated programmatically: every `library_file` maps to an `INDEX.md` row, every `status_checked` matches the index verbatim, all 20 citable authorities covered |
| `QUESTIONS.md` | 8 specific client questions (Assumption A corporate facts, confidential-info/supply records, equity, full agreement text, Kestrel role, LO-233 population, Zhao counsel posture, timing), each tied to the conclusion it could change |
| `STATUS.md` | Deliverable checklist, citation-integrity record, key conclusions, open items |

**Integrity checks passed:**
- Citations: 16 in force / 2 superseded (*Campbell*, *General Commercial Packaging*) / 1 vacated (FTC rule) / 1 modified (*Light v. Centel*, with the memo's instruction not to cite it for the old timing rule) — all verified against actual library texts, not just the index.
- No authority outside `INDEX.md` cited; unverified propositions (Restatement §188, §17200, trade-secret route, firm-memo cases) are flagged **[unverified]** in the memo only.
- Final CJK/typo grep across all four files: clean.

**Bottom line:** Do not file in Travis County — ~0–10% probability of an effective restraint, and the filing itself creates §16600.5(b)/(d) liability and §16600.5(e) fee-shifting exposure to Zhao, who has already telegraphed the theory through counsel.

Now ending the turn per the engagement protocol so the client can respond to `QUESTIONS.md`; on receipt I'll update the memo and probability bands if any premise changes.