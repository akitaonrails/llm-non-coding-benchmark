

Let me do a thorough pre-delivery review. I'll re-read all deliverables and independently re-verify every calculation.







Now let me run an independent verification pass — re-deriving every deadline with a fresh implementation and cross-checking every date/day-of-week pair in the deliverables.





The deadline and JSON checks all pass. There's a group-index bug in the day-of-week check part of my verification script — let me fix it and re-run just that section.





The full verification passed — all deadlines, JSON consistency, and date/day-of-week pairs are consistent. Next, I'll apply the minor fixes identified in the audit. First, let me confirm the exact lines that need editing.






Everything is consistent. Now applying the three fixes from the audit:

**Fix 1** — Consolidate the calculation script into the workspace (so that the deliverables are self-contained and do not reference `/tmp`):





The workspace script reproduces every date in the deliverables exactly. Now the three text fixes:







Now let me update STATUS.md's deliverables list to include the script and document the review pass:





Final re-run of the full verification after the edits:





Pre-delivery review is complete. Everything reconciles; no calculation errors were found. Summary:

## What was checked
1. **Independent re-derivation** of all deadlines with a fresh script — all 7 real dates (publicações 23/11 and 11/12; inícios 24/11 and 14/12; **contestação 16/12/2026**, **embargos 21/01/2027**, **apelação 04/02/2027**) and the 3 hypothetical double dates (10/02, 28/01, 01/03/2027) recompute exactly.
2. **`prazos.json`** — valid JSON, all required keys present, all values match the re-derivation.
3. **`memoria.md`** — every date/day-of-week pair (30+ pairs) verified programmatically: zero mismatches.
4. **Citations** — every authority in the deliverables maps to a file in `library/INDEX.md` (`cpc_prazos.md`, `cpc_prazos_recursais.md`, `lei11419_art4.md`, `calendario_forense_campinas.md`); nothing external was used.
5. **Holiday set** cross-checked against the library calendar for the whole relevant window — complete (20/11 Zumbi, 08/12 Conceição, 24/12, 25/12, 31/12, 01/01, Carnaval 08–09/02/2027); 25/01/2027 correctly kept as a business day (Capital-only holiday).
6. **Legal logic re-audited** — publication (art. 224 §2º / Lei 11.419 §3º), start (art. 224 §3º / 231 VII), business days (art. 219), exclude-start/include-end (art. 224 caput), recess suspension 20/12–20/01 inclusive (art. 220), double-deadline exclusion (art. 229 §2º): all consistent with the library texts.
7. **Non-business-day coverage** in the sentença range matches the JSON list exactly.

## What was changed (cosmetic only — no numbers)
1. **`prazos.json`** — "NAO se aplica" → "NÃO se aplica" (accent consistency).
2. **New file `deliverable/calc_prazos.py`** — the calculation script consolidated into the workspace with full rule documentation, so the deliverables are self-contained and re-runnable (verified to reproduce every date).
3. **`memoria.md`** (closing note) — script reference changed from `/tmp/opencode/prazos_calc.py` to `deliverable/calc_prazos.py`.
4. **`STATUS.md`** — typo "Contestações" → "Contestação"; script added as deliverable item 3.

## Open item (flagged, not an error)
If embargos de declaração are filed by 21/01/2027, the apelação period restarts from the intimation of the embargos ruling (CPC arts. 1.023/1.026) — new date to be computed when that intimation issues.

Status remains **COMPLETE**.