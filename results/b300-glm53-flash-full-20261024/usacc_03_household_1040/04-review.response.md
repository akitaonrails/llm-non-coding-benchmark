Starting the final review pass. I'll re-read all deliverables and the citation index first.

All six library texts check out against the citations used. Now I'll re-verify the source-document numbers from the earlier extractions and re-run the arithmetic.

The extracted texts were cleared from /tmp/opencode — re-extracting the PDFs and reading the text-native files.

W-2s and K-1 verified — notably, both W-2s show **box 16 full-year NY state wages** ($68,000 / $54,000) and both employers are New York entities, which directly corroborates the convenience-rule treatment. Continuing with the rest of the file.

All library texts and source documents verified. Now running the full arithmetic verification, including the exact PTC computation and JSON schema check.

Test-script sign error (the JSON stores the loss magnitude as a positive number):

Another bug in my own test script (line 55: meant `1720 > monthly contribution`, wrote `6 >`). Re-running the tail checks:

All delivered figures verified. Two internal inconsistencies confirmed in the counterfactual narratives. Now the citation-hygiene sweep:

Citations resolve cleanly: only the six indexed library files are cited as authority; `$26,690` appears only in withdrawn/superseded contexts. The verify pass found **five substantive fixes** (all presentational/counterfactual — none changes a delivered figure):

1. `return.md` PTC block: displayed arithmetic mixes the rounded 5.7115% with the unrounded-precision product ($5,217.49) — self-inconsistent.
2. `judgment_calls.md` §1 counterfactual numbers (MAGI $91,750 / AGI $74,850) don't reconcile — the consistent full-loss counterfactual is MAGI 94,400 → full $25,000 allowance → $21,018 rental allowed → AGI 73,382.
3. `judgment_calls.md` §8 counterfactual allowance "16,750" doesn't reconcile — MAGI 122,400 → allowance 13,800.
4. Garbled clause in §2(b) ("— intern nobody's days or wages turn on it").
5. Missed corroboration for Elena's NY-source conclusion: the W-2 itself is New York employer (230 Park Ave S NY) + box 16 full-year NY wages — worth adding since the library's convenience rule is keyed to "a New York employer."

Applying fixes:

Resuming the review fixes. Let me read the remaining pieces I need: the rest of judgment_calls.md, the Elena line in return.md, `ny.method` in return.json, and STATUS.md.

I have everything I need. Applying all remaining fixes in one pass:

Path typo on my part — the files are under `/work/workspace/deliverable/`. Retrying:

All five text edits applied. Now the last two files — `return.json` `ny.method` and the final-review note in `STATUS.md`:

All edits applied. Final validation — JSON integrity and confirming no residual bad strings:

The review pass is complete and everything is now delivered. `return.json` validates, and the only remaining traces of the corrected errors are in the change log itself (where they belong).

## Pre-delivery review — results

**What I checked:** every delivered figure recomputed in Python against the source re-extractions; every citation traced to one of the six files in `library/INDEX.md`; rejected-alternative narratives recomputed for internal consistency; JSON schema against `CONTRACT.md`; cross-checks of W-2 figures and the custody/basis documents.

**What I found:** all delivered *figures* verified correct — the errors were in the supporting narrative. Fixed:

1. **Counterfactual arithmetic (`judgment_calls.md` §1)** — the "what if the full $28,000 S-corp loss were deducted" story was wrong. Correctly recomputed: MAGI would be $94,400 (under $100,000), so the full $25,000 allowance applies and the entire $21,018 rental loss is allowed → AGI $73,382, a cut of **$17,968** (not $16,500), PTC rises materially (~235% FPL). Shows *why* the basis limitation has larger knock-on effects — while the conclusion stands.
2. **Wrong allowance figure (`judgment_calls.md` §8)** — the rejected "exclude S-corp loss from MAGI" branch: MAGI $122,400 → allowance = 25,000 − 50%×22,400 = **$13,800** (was misstated 16,750); AGI would be $97,100.
3. **NY corroboration added** (`return.md`, `judgment_calls.md` §3, `return.json` `ny.method`) — both employers are New York entities (Reyes & Pike: 1 Liberty Plaza; Halvorsen: 230 Park Ave S) and both W-2s report full-year box 16 NY state wages ($68,000 / $54,000). This is the key external support for the convenience-rule treatment.
4. **PTC presentation (`return.md`)** — added the exact unrounded chain (292.788…% FPL → 5.711538…% → 5,217.49/yr → 1,255.21/mo → 7,531.25 ≈ 7,531; excess 2,368.745 ≈ 2,369 → capped at 1,900).
5. **Typos** — stray word removed (§2), "exemption's"→"excerpt's", "superceded"→"superseded".

**Confirmed unchanged, re-verified:** tax $6,708; excess-APTC repayment $1,900; total tax $6,408; withholding $8,730; **refund $2,322**; rental allowance $19,550 / carryforward $1,468; basis $11,500 / $16,500 suspended; CTC $2,200 (Sofia only).

**Citations:** clean — only the six indexed library files are cited; all unverified items (SALT cap, CTC phase-out, 8812 mechanics, NY-source of the condo rent, NY tax computation) are labeled as judgment/unverified, never cited as authority.

**Still open (unchanged, logged in `STATUS.md`/`QUESTIONS.md`):** the NY tax due/refund cannot be computed — the library contains no NY rate table.

All four deliverables are final under `workspace/deliverable/`: `return.json`, `return.md`, `judgment_calls.md`, `QUESTIONS.md`, plus the review log in `STATUS.md`.