I'll do a thorough review. Let me re-read all deliverables and re-verify every claim against the library.



I've done a full re-read. Let me now independently re-verify the two newest dates I added (the double-deadline "hypothetical" dates and the conditional-scenario breakdown) before deciding what to fix.



The double-deadline dates (05/02 and 26/02) are verified correct. But I found an **error in the conditional-scenario breakdown** — my §3.5 parenthetical says "13: 02/02, 14: 03/02, 15: 12/02", but the actual count is 13: 10/02, 14: 11/02, 15: 12/02. Let me verify the remaining weekdays, then fix everything.



All dates, weekdays, and the 32-day recess are verified. I found **one real arithmetic error** in the conditional-scenario breakdown and **one false cross-reference**. Let me fix both.

**Fix 1 — the conditional-scenario day numbering is wrong** (I wrote 13: 02/02, 14: 03/02, 15: 12/02; the actual count is 13: 10/02, 14: 11/02, 15: 12/02):



Let me use the exact text from the file:



Now let me re-read the JSON to check it thoroughly:



All sources re-read. Now a fresh, independent arithmetic pass to re-verify every date in the deliverables before I make edits:



I've confirmed all arithmetic independently and found that `prazos.json` matches the script exactly. Now I'll fix the writing and authority issues.



Now the remaining memoria.md fixes:



The third edit was a no-op (that text was already correct). Now the §4 table header, the §5 reconciliation note (turning the papered-over anomaly into a flagged open item), and STATUS.md:



I spotted a typo I just introduced ("foi publicados" → "foi publicada"). Fixing:



Now I must renumber the open items in STATUS.md (old 2 and 3 became 3 and 4):



Let me check the current state of that section:



The first renumber succeeded; the second failed on indentation. Let me fix item 3→4 and the wording with exact text:



Now a final full re-read of both edited files to confirm consistency:



I've fixed the last remaining wording issue ("moot" → Portuguese).



Now a final consistency sweep of all deliverables:



Two small blemishes remain (the "Arithmetic" wording in STATUS.md and the clunky parenthetical at line 135), plus I'll normalize the §4 table row spacing.



Final verification of both files:



Review complete. Here's what I found and fixed:

## Errors found & fixed

**1. One arithmetic presentation error (memoria.md §3.5)**
The conditional-scenario day-by-day list in the apelação section mislabeled days 13–15 in its text (it listed days that had already been consumed). The final date (12/02/2027) was always correct, but the enumeration was wrong. Fixed to: `1: 21/01 … 10: 03/02, 11: 04/02, 12: 05/02, 13: 10/02, 14: 11/02, 15: 12/02`.

**2. One unsupported authority (memoria.md §3.5 + STATUS.md)**
Art. 1.026 is **not** in the INDEX citation line for `cpc_prazos_recursais.md` (only arts. 335, 1.003 §5º, 1.023). It appears only referenced *inside* the text of art. 1.023 in that file. I demoted it in both files: the interruption is now cited to **art. 1.023**, with art. 1.026 noted as "mentioned in the text of the library file" — no longer an independent citation.

**3. One non-reconciling item that I had papered over (memoria.md §5 + STATUS.md)**
The sentença was published **11/12/2026, *before* the contestação deadline of 15/12/2026** — procedurally unusual for an ordinary Procedimento Comum. I had written "Tudo reconciliado," which violated the flag-don't-force rule. Rewrote it as an explicit open item (now **item 1** in STATUS.md): calculations follow the two notices as given, but the procedural fact explaining the order should be confirmed in the case file.

## Minor wording fixes (all in memoria.md)
- "ambos os intimações" → "ambas as intimações" (grammar, §1)
- §1: fixed the garbled description of art. 229 §1º (it's the *cessation* rule, not an "exception to the caput"); "moot" → "irrelevante"
- §2.2: clarified that art. 231 VII sets the *reference date* (publication) and the count starts the following business day (§224 §3º / Lei 11.419 §4º) — previously conflated
- §3.2: tightened the clunky parenthetical about Christmas days/recesso
- §3.5: removed dangling "reproduzida no final desta seção" reference
- §4 table: normalized header/row spacing
- §5: "os dois trechos da apelação" → "todas as contagens (citação, sentença, cenário condicionado e hipótese de dobro)"
- STATUS.md: "Arithmetic executada" → "Cálculos executados"

## What did NOT change
- **`prazos.json`** — no changes needed. Re-verified: parses cleanly, matches the contract schema exactly, and every date matches a fresh independent Python pass:
  - Citação: publicação **23/11/2026** (20/11 feriado + s/f), início **24/11/2026**, contestação **15/12/2026** (08/12 feriado municipal excluded)
  - Sentença: publicação **11/12/2026**, início **14/12/2026**, embargos **18/12/2026**, apelação **03/02/2027** (32 recess days 20/12–20/01 suspended; 25/01/2027 counted — SP-capital holiday only per [Cal])
  - `prazo_em_dobro: false`
- Hypothetical double dates remain 05/02/2027 / 26/02/2027 (transparency table only).

**Status: COMPLETE WITH OPEN ITEMS** (4 non-blocking items in STATUS.md; the new date-divergence flag is #1).