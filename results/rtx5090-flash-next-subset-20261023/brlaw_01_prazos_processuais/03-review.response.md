I'll re-verify everything with an independent second pass: recompute all counts with a different implementation, cross-check the tables embedded in `memoria.md` against the recomputed sequences, verify every weekday label in the calendar and deliverables, and audit each citation against the library.

Now the reconciliation note (§6). Let me check how memoria.md currently ends:

I introduced two typos in that edit — fixing them now:

Now the questions files and the updated STATUS.md — creating them in parallel, and verifying the §6 text in the same pass:

Review complete. Full report:

## What held up (verified, no changes needed)
- **Arithmetic**: recomputed all three deadlines with a second, independent implementation (day-by-day walk over every calendar date). Identical results — **contestação 15/12/2026, embargos 18/12/2026, apelação 03/02/2027** — and all 35 counted days in the three tables of `memoria.md` match line-for-line, including every weekday label and the calendar's own labels (20/11 sex, 08/12 ter, 25/01 seg, Carnival 08–09/02/2027 seg/ter).
- **Schema**: `prazos.json` parses and contains exactly the contract's required keys, ISO dates.
- **Citations**: every article cited in the deliverables (CPC 219, 220, 224, 229, 231, 335, 1.003 §5º, 1.023; Lei 11.419 art. 4º §§3º–4º; Lei 14.759/2023; Campinas/SP calendar entries) appears in `library/`. Art. 1.026 exists **only in the body** of `cpc_prazos_recursais.md` and I always cite it that way.

## What I found wrong and changed
1. **Timeline that does not reconcile** (the big one): the sentence's intimação (disponibilização **10/12/2026**) is *earlier* than the contestação deadline (**15/12/2026**), with the case jumping from fls. 88 to fls. 212/219 in ~3 weeks. I had not flagged this. Fixed: new **§6 "nota de reconciliação"** in `memoria.md` — dates remain valid *as counts from the two intimações provided*, but the sequence is left open, not forced; possible consequences labeled as unconfirmable (library has no citation/nullity norms). Created **`QUESTIONS.md`** (4 targeted questions) and **`PERGUNTAS.md`** as a pointer (contract's optional name).
2. **Overstated margin in §5**: "~7–8 semanas" was only true for contestação. Corrected to exact figures: **52 dias (≈7,4 sem)** on contestação, **23 dias (≈3,3 sem)** on apelação (hypothetical dobro dates unchanged: 05/02/2027 and 26/02/2027).
3. **Unsupported authority in §3.2**: I had stated embargos reopen the appeal clock "a partir da juntada/intimação da resposta aos embargos" — that reopening mechanism is *not* in the library (which says only that embargos **interrompem**, art. 1.026). Rewritten; the reopening marker now explicitly labeled not defined in library nor in the record.
4. **§4 assumption 2** now cross-references §6.
5. **`STATUS.md`** downgraded **COMPLETE → COMPLETE WITH OPEN ITEMS**, listing the reconciliation item and the two stated assumptions, plus a changelog of this review.

**Unchanged: the three calendar dates** — 15/12/2026, 18/12/2026, 03/02/2027 remain the dates to diary. Open items are factual (answers 1–2 in `QUESTIONS.md` decide whether the contestação date still has practical utility; they do not change the computed counts unless the PDFs' dates are wrong).