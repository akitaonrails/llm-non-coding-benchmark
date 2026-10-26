Key new facts: (a) the dentist rental at R$ 8k/mês is now a **certainty** — and that decides the property question; (b) Luana has no money — the "work = 20%" vehicle is dead on arrival; (c) Marina's "administrar fora do expediente" is a misunderstanding that needs a hard correction. Let me run the updated arithmetic first.

The arithmetic is done. Now let me review the remaining files before updating everything for turn 2.

All deliverables reviewed. Now the final consolidated arithmetic for the turn-2 structure, plus a quick re-check of two library texts I'll quote in the correction of Marina's misunderstanding.

Everything is verified. Now I'll write the turn-2 updates across all seven deliverables, starting with `parecer.md` (header pointers + consolidation annex).

Now I'll add the turn-2 pointers throughout `parecer.md`.

Now the section 7 pointer and the full ANEXO A appended at the end:

Fixing a typo in the appendix:

Now the rewritten `contrato_social_ajustado.md` for the turn-2 structure:

Now the rewritten `checklist_registro.md`:

Typo fixed. Now let me read `numeros.json` to update only the ITBI `fundamento` text:

Now the remaining turn-2 rewrites. Let me read the current `QUESTIONS.md`, `PERGUNTAS.md`, and `STATUS.md`:

Let me check the documents folder for where the turn-2 client answers live, so the ledger cites the right source:

Now the `QUESTIONS.md` answer ledger:

Now the `PERGUNTAS.md` mirror and the `STATUS.md` rewrite:

All files updated. Final QA pass — JSON validity/schema, citation integrity vs `INDEX.md`, and a sweep for stray non‑Portuguese characters:

All citations check out against `library/INDEX.md` and the JSON schema matches `CONTRACT.md` exactly. Final arithmetic re-verification and typo sweep:

The grep hits are all false positives (`grep -i` matched the Portuguese word "todos" against "TODO") — no stray artifacts remain. The engagement is now fully consolidated for turn 2.

## Done this pass

1. **`checklist_registro.md`** — item 4.2 cleaned: now reads "Discriminar pró-labore × lucro em **toda a** escrituração/pagamento", with the self-correction note removed.
2. **`numeros.json`** — only the `itbi.fundamento` text rewritten (values and schema untouched): documents that under Estrutura A there is **no transfer → no ITBI taxable event**; `base: 420000` now framed as the **Variante B** basis (declaratory value, Tema 796 coverage, 96.000 ÷ 1.296.000 = 7,41% < 50% CTN art. 37, 3-year monitoring). Schema re-validated against `CONTRACT.md` — exact keys, no extras, valid JSON.
3. **`QUESTIONS.md`** — converted from questionnaire to **answer ledger**: 4 questions answered (regime, Marina's role, Luana's capital, dentist rental) + Felipe implicit, each with its legal consequence; the 6 unanswered themes are carried as **flagged unknowns with their treatment** (S1–S3 scenarios, contract reservations, PREMISSAs) — nothing re-asked.
4. **`PERGUNTAS.md`** — mirror rewritten to match (turn-2 state).
5. **`STATUS.md`** — rewritten: **COMPLETE WITH OPEN ITEMS**, Estrutura A conclusions, open items listed as flagged decisions (regime change = critical path; other Simples companies; Luana's credentials; 60% rent pricing; projection basis), plus the standing library-gap list.
6. Also fixed a loose citation in `parecer.md` item 3.4 (turn-2 answers referenced as the client's message record in ANEXO A.0, not a `documents/` file).

## Final QA (all green)
- All 7 deliverables present; 540 lines total (parecer 300 with governing ANEXO A).
- `numeros.json`: valid JSON, exact CONTRACT schema.
- Every `library/…` citation across all files ⊆ the 7 files in `library/INDEX.md`.
- Arithmetic re-verified in Python: 7.41% rent share; 12.000/mês premise; S2 23k / S3 5k; Variante B 20.83%; cliff 5.000,10; INSS 1.100; max 17.500/sócio.
- No garbled characters or leftover editing notes in any deliverable.

The deliverable set now tells one coherent story: **Estrutura A** (property out of capital, couple as lessors, Luana contracted, Marina cotista-only) with the CC 977 regime change as the single critical-path decision, and **Variante B** fully priced (loses Simples) as the documented alternative.