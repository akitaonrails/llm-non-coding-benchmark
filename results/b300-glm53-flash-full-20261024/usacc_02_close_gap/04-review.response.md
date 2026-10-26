I'll do a full pre-delivery review: re-read every source document, re-verify the library authorities, recompute the rolls independently, and re-read each deliverable. Starting with the library and extracting the PDFs to text:

Now reading the extracted statement texts, the library authorities, and the CSVs in parallel:

The bank statement resolves the "missing 2,000" — my earlier quick-sum in review notes was wrong: the parenthetical itemization (3,188.22 + 4,500 + 7,315 + 4,860 + 2×(7,100+653.20) + 318.75) genuinely sums to 35,688.37, and total debits 35,723.37 including the 35 fee check out. Cleared checks are exactly #2036/#2038/#2040. Statement balances and running 13,054.43 movement all tie. Now the library authorities and CSVs:

All source numbers verified — both of my "suspects" from the checkpoint turn out to be arithmetic slips in my own review notes, not in the deliverables:

- The §B parenthetical genuinely foots to **35,688.37** (I had dropped one 7,100.00 Gusto run when quick-summing), and total debits 35,723.37 (incl. $35 fee) and credits 50,362.00 tie to the statement panel; running balances check line-by-line; the only cleared checks are exactly #2036/#2038/#2040.
- Recomputed independently from GL + Feb TB: 4000 = 138,720, revenue 154,920, expenses 124,975.77, **NI 29,944.23**, TB **424,932.07 both sides** (re-added by account — ties), A/R 115,288, A/P 29,505.40, card 2,306.12, 2100 = 4,312 CR, 1300 = 4,738. All deliverable figures match.

Library quotes are verbatim accurate (suspense rule, draws/contributions rule, prepaid >1 month → 1300, "reported — not a reason to record an entry", "may constitute a false statement"; INDEX lists exactly the two citable files). COA confirms no misc-income account and 2100's name.

Now the full read-through of every deliverable plus the Cascade evidence and checklist:

§C has a real error: the statement line-by-line table omits **CHECK #2038 (03/15, −7,315.00)** and even asserts "03/15 — no item", contradicting the statement and the table's own foots line. Everything else in the rec checks out against the statement, and both Cascade copies confirm the AJE-1 duplicate (same invoice CH-7731, total 4,860.00; email 02/24 vs mailed-in-March stamped copy). Reading the rest before fixing:

Continuing the pre-delivery review. I still need the two JSON files end-to-end and the full text of the two files I'm about to edit:

All deliverable numbers tie (TB 424,932.07 both sides, 2100 = 4,312 CR, 1300 = 4,738, AJE memos quote the owner's words accurately). Two fixes confirmed needed:

1. **`bank_reconciliation.md` §C line 70** — `| 03/15 | — | — | — | no item |` contradicts the statement, which has `03/15 CHECK #2038 −7,315.00`. The foots line (which includes 7,315.00) silently relies on a row that doesn't exist in the table.
2. **Allied "Q2 GL"** — the AJE-8 memo and open_items §6 assert the bill "is described as quarterly general-liability coverage for Q2 2026 (04/01–06/30)". "GL" → general liability and the span are **our inference**, not bill text; that's unsupported authority for a document quote.

Before editing, let me confirm the #2038 payee in the GL, check the actual Allied bill text, and find whether any script generates these strings (to avoid drift):

#2038 = Austin Lumber 7,315.00 (GL 03/13, cleared 03/15) — confirms the missing-row fix. The "general-liability" wording lives in exactly three places: `close_round2.py`, the generated `adjusting_entries.json`, and `open_items.md` (NOT in QUESTIONS.md or STATUS.md — good). Now let me see the Allied bill's actual text so the softened wording quotes it exactly, and check the generator script:

The Allied bill isn't in the extracted set or the documents glob — I need to locate the actual bill document before re-wording its citation. Let me check the full documents directory and search for "Allied":

Significant finding: **there is no Allied bill document in the file at all.** The only in-file occurrence of "Q2 GL" is the GL memo line (`Allied Insurance — Q2 GL`, 03/20). So the AJE-8 memo and open_items §6 attribute text to a bill that isn't in the file — a document reference that can't be verified. The GL memo is the actual citable evidence. Let me read QUESTIONS.md and STATUS.md in full to see exactly how they describe this (and check for the same overreach):

QUESTIONS.md Q7 line 20 has the same overreach ("the classification comes from the bill itself"), and STATUS.md lines 18/25 say "bill text". Before editing, two last verifications: the full GL (payees/memos for #2036/#2040/#2041/#2044, Rivera, Allied) and that open_items.md §1's long line is intact in the file (the earlier read truncated it for display):

The long line 19 is intact (ends "...parked in 2100, disclosed, and the rec still ties at 0.00." — 2,028 chars; earlier truncation was display-only). Now let me pull the exact text I need to edit — the Rivera GL row, and the precise wording in each file I'm about to touch:

All exact texts confirmed. Now applying the fixes — one to `bank_reconciliation.md` (restore the missing CHECK #2038 row) and the Allied re-basing edits across the four md files and the generator script:

All 8 edits applied. Now rerun the generator so `adjusting_entries.json` picks up the corrected AJE-8 memo and every tie re-verifies — snapshotting the trial-balance hash first to prove no numbers moved:

17/17 PASS, TB byte-identical (same hash). Final verification sweep — confirm no unsupported phrasing survives anywhere and the regenerated JSON is correct:

One leftover found: `open_items.md` line 91 still says "Prepaid per the bill's own text" in a summary table. Let me see its context and fix it:

Final sweep for any residual unsupported phrasing across all deliverables:

Everything is clean. The review is complete — here's the full report.

## What the review found

**Verified clean (no changes needed):** all arithmetic (rec ties 0.00; TB 424,932.07 both sides; A/R 115,288.00; A/P 29,505.40; NI 29,944.23), every owner quote, all library-rule citations, the "no client information" flags for the mobile deposit, pre-March A/R gap, legacy prepaid, depreciation, and A/P itemization, and the AJE support for all 8 entries.

**Two real defects found and fixed:**

### 1. `bank_reconciliation.md` §C — missing statement row
The line-by-line table asserted `03/15 | — | — | — | no item`, but the statement **does** have a 03/15 line: `CHECK #2038 −7,315.00`. The cross-foot only worked because the foots line silently summed a check that appeared nowhere in the table — and it flatly stated "no item" on a day that had one.
- **Fix:** restored the row: `| 03/15 | CHECK #2038 | −7,315.00 | Yes | A/P — Austin Lumber; cleared |` (payee per GL rows 03/13). The table now covers all 16 statement lines; foots line unchanged.

### 2. Allied "Q2 GL" — asserted a document that isn't in the file
The deliverables said the coverage was "described **on the bill** as quarterly general-liability coverage for Q2 2026 (04/01–06/30)". **There is no Allied bill in the file** — the only place "Q2 GL" appears anywhere is the GL memo (`Allied Insurance — Q2 GL`, keyed 03/20). Quoting an absent bill is an unverifiable document reference, and the "general-liability" expansion was presented as bill text when it's our inference.
- **Fix:** re-based every citation to the GL memo, stated plainly that the bill itself is not in the file, and marked "GL → general liability" as our reading pending the policy declarations page (proviso and April follow-up kept).

## What I changed

| File | Change |
|---|---|
| `deliverable/bank_reconciliation.md` | §C: "no item" row replaced with the real CHECK #2038 row |
| `deliverable/open_items.md` | §2 table: Allied answer now cites GL rows 03/20, "bill not in file"; §5: Rivera/Allied support now cited as GL rows (memo "Rivera Finish Carpentry sub — Kessler"), not sub bills; §6: full rewrite to GL-memo basis with inference flagged; round-2 summary table: "per the bill's own text" → "per the GL memo text" |
| `deliverable/QUESTIONS.md` | Q7 rewritten: classification sourced from the GL memo, "GL" reading flagged as ours, follow-up extended to coverage *type and* dates |
| `deliverable/STATUS.md` | AJE-8 bullet and round-2 summary re-based to GL memo ("bill text" wording removed) |
| `deliverable/adjusting_entries.json` | AJE-8 memo corrected (same edit as below, regenerated) |
| `close_round2.py` | AJE-8 memo source fixed identically; script rerun → **17/17 PASS**, retry made `trial_balance_2026-03-31.json` byte-identical (same SHA-256) — no numbers moved |

## Standing confirmation

Rec difference **0.00** · adjusted bank = adjusted book **10,318.30** · TB **424,932.07** balanced · NI **29,944.23** · suspense 2100 stays **4,312.00 CR** (round-3 "misc income / my contributions" request still correctly refused and documented). Final grep confirms zero occurrences of "bill text", "bill's own text", "sub bill", "no item", or unflagged "general-liability" claims anywhere in the workspace. The package is ready to deliver.