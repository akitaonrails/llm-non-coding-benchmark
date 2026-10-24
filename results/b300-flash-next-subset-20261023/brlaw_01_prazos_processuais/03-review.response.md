

Running an independent verification pass (different code path + GNU `date`, not reusing my earlier script), then a citation audit against `library/INDEX.md`.






Final end-to-end read of the corrected files:






Review complete. Here is the audit result and change list.

**What I re-verified (all passed, no changes needed):**
- **Dates & weekday labels** — recomputed with two independent methods (GNU `date` and a second algorithm written from scratch, not reusing my earlier script). Publication/start rules and all three deadlines confirmed: contestação **15/12/2026**, embargos **18/12/2026**, apelação **03/02/2027**. Weekday labels in every table (ter/qua/qui/sex/seg) checked one by one.
- **Arithmetic reconciliations** — contestação proof (22 calendar days − 6 weekend − 1 holiday = 15 business days ✓); apelação proof (52 days − 32 recess − 5 weekend = 15 ✓); the hypothetical doubled date 05/02/2027 also checked.
- **Facts vs. documents** — publication dates, "quinta-feira" labels, e-SAJ/electronic case status, and the two-law-firm fact all trace to the PDFs and procurações summary; nothing invented.
- **Citation sweep** — every other statute cited (CPC 219, 220, 224 §§1–3, 229 §§1–2, 231 VII, 335 III, 1.003 §5º, 1.023; Lei 11.419/2006 art. 4º §§3º–4º; Lei 14.759/2023 via the calendar) appears verbatim in a file listed in `library/INDEX.md`.
- **Schema** — `prazos.json` matches the contract's exact keys; parses as valid JSON. Artifact/garble scan on all three files: clean (earlier stray-token and garbled-proof fixes confirmed gone).

**Errors found and fixed (1 substantive issue, 3 locations):**

1. **`memoria.md` §7** — I had cited "CPC, arts. 1.023/1.026" for the embargos-interrupt-appeal rule. The INDEX lists only arts. 335, 1.003 §5º and 1.023 for that file; **art. 1.026 is not individually indexed** — the rule exists only as an annotation inside the indexed file. Reworded to cite the indexed file's annotation as the authority, with an explicit "Ressalva de autoridade" noting art. 1.026 was not verified at the primary source.
2. **`memoria.md` §2** (source list) — same citation tightened to "anotação ao art. 1.023 com remissão ao art. 1.026 — ver ressalva no §7".
3. **`STATUS.md` open item 1** — replaced the bare "(CPC arts. 1.023/1.026)" with the file-anchored citation and the same caveat.

**Left deliberately unreconciled (already flagged in STATUS, per the contract's "don't force anything to balance"):** the DJe publication dates (Nov/Dec 2026) post-date the environment date (23/10/2026); documents treated as the case data, discrepancy recorded. The embargos-dependent recalculation of the appeal date remains an open item by nature, not by omission.

Deliverables are final in `workspace/deliverable/` (`prazos.json`, `memoria.md`, `STATUS.md` — status: COMPLETE WITH OPEN ITEMS).