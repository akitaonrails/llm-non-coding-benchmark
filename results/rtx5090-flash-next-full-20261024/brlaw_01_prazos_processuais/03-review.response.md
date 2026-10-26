I'll do a systematic cross-check: recompute everything with an independent script that parses the library calendar table directly, then audit every date/weekday claim in the deliverables.

Syntax slip in the audit portion — rewriting it cleanly:

Careless here-doc typo again. Writing the audit as a proper file:

All 10 JSON milestones independently reproduced. The weekday-audit branch had a capture-group miscount (the weekday class is itself a group). Fixing:

Final consistency pass — re-running the audit to confirm the new text didn't introduce any wrong weekday/date claims:

Review done. Everything was re-verified with an independent script (`/tmp/opencode/audit.py`) that parses the library's calendar table directly rather than reusing my earlier logic.

## What checked out (no changes needed)
- **All 10 milestones in `prazos.json`** reproduced exactly by the independent recomputation: publicação 23/11 and 11/12, início 24/11 and 14/12, contestação **16/12/2026**, embargos **21/01/2027**, apelação **04/02/2027**.
- **Every weekday label** in `memoria.md`/`STATUS.md`/`prazos.json` cross-checked against the real calendar: 0 errors.
- **Arithmetic statements** in the memória (22 − 6 fins de semana − 1 feriado = 15; 4 + 11 = 15) verified.
- **Authorities**: every citation maps to a file indexed in `library/INDEX.md` — nothing imported from outside the closed library. The art. 1.026 mention stays attributed to its location inside `cpc_prazos_recursais.md`.

## What I found and fixed
1. **A real non-reconciling item, previously mis-described.** The sentença was disponibilizada 10/12/2026 and published 11/12/2026 — **5 days before the contestação deadline (16/12/2026) even closes**. That's procedurally atypical unless the defenses were filed early (likely, since the sentence condemns "as rés" and there's sucumbência recíproca — but **no certidão in the documents proves it**). The old alerta in §3 described this order backwards.
   - Rewrote the §3 alerta and added **§4.1** in `memoria.md` stating the anomaly plainly. Per the contract, I did **not** force a reconciliation: the counts still use the DJe publication dates (primary source); the anomaly is flagged, not explained away. If the DJe dates are right, the delivered deadlines don't change — only the procedural narrative does.
2. **Unsupported-authority nuance:** the library's CPC art. 231 excerpt is truncated ("… VII") — only item VII is available. Added a caveat in §4.2: we applied VII because the despacho shows citação/intimação via DJe na pessoa do advogado, the mode the library covers; if a different citation mode had been used, the start date could differ and we couldn't verify it from the library.
3. **Created `deliverable/QUESTIONS.md`** — 3 targeted client questions: (a) proof/date of contestação filings and whether revelia was decreed (resolves the anomaly); (b) any DJe/e-SAJ unavailability on 19/11, 23–24/11, 10–11/12, 14/12/2026 (would trigger art. 224 §1º shifting); (c) intent to file embargos (the 04/02/2027 apelação date holds only if none are filed).
4. **`STATUS.md` flipped from COMPLETE to COMPLETE WITH OPEN ITEMS** and its body corrected: the stale "Sem QUESTIONS.md" line now lists the three questions, and the vague "Ressalvas" section was replaced with the concrete open items (anomaly §4.1, the art. 224 §1º presumption, the embargos interruption condition) plus a review log.

Honest status: the two deadline blocks are fully computed, double-verified and citation-backed; the chronology anomaly is left open rather than papered over, and answering it can only *explain* the case posture — it cannot move the delivered dates unless one of the DJe dates in the PDFs turns out to be wrong.