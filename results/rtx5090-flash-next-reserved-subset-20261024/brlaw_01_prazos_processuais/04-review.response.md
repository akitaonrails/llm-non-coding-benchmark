Good discipline — let me run a systematic audit before closing: every authority cited against the library, every weekday label, every date claim, and internal reconciliation.

The table itself (memoria.md:75) is correct — the weekday error lives only in the U5 narrative in three files. Let me check the exact U5 blocks and the art. 1.026 citation wording before fixing:

The module lives in `workspace/` but needs cwd=/work for its relative library paths — re-run with PYTHONPATH, and redo the CJK check properly (grep brace syntax needed -P):

All checks pass. Review complete — here is what I audited, what I fixed, and what I confirmed.

## What I audited

1. **Every date×weekday pair** in all five deliverables (regex against the real calendar): **131 pairs, 0 errors**.
2. **Every statutory citation** against the library files only (CPC arts. 219, 220, 224, 229, 231, 335, 1.003 §5º, 1.023/1.026; Lei 11.419/2006 art. 4º §§3º–4º; Lei 14.759/2023 via the calendar file): no citations outside the library; no "art. 220, caput/§" (library shows a single-sentence art. 220); no Lei 13.925/2019 anywhere.
3. **Reconciliation** with `calculo_prazos.py::conferir()`: all trails re-assert clean — contestação **15/12/2026 (ter)**, embargos **18/12/2026 (sex)**, apelação **03/02/2027 (qua)**, dobro hypothesis 05/02/2027 (sex), 23 suspended recesso weekdays.
4. **Fact-check of prose claims** (holiday table dates, calendar-validity frontier, 52-day gap 15/12→05/02, etc.).

## What I found and fixed (1 real error + 1 imprecision)

1. **Real error — weekday/U5 claim**: I had written "**07/12/2026 é domingo**" and claimed the unlisted-holiday hypothesis had "nenhum impacto". Wrong on both counts: **07/12/2026 is a segunda‑feira** and it is the **10th computed day** of the contestação (my own day-by-day table at memoria.md:75 already had it right). If it were an unlisted local holiday, contestação would shift to **16/12/2026 (qua)**. Corrected in three places — `memoria.md` (§8 bullet + §9.1 U5 row), `STATUS.md` item 5, `QUESTIONS.md` U5 — now stating the possible shift and noting the risk direction stays favorable (working date 15/12/2026 would still be timely).
2. **Imprecision — art. 1.026 citation**: the library does not carry art. 1.026 as its own article; the interruption rule appears inside the art. 1.023 excerpt "(art. 1.026)". Changed the three loose "(art. 1.026, conforme a biblioteca)" cites to "(arts. 1.023/1.026, conforme a biblioteca)", matching how the memoria's source list already describes it.

## Re-verified after fixes

- Weekday audit re-run: 131 pairs, 0 errors (16/12/2026=qua and 07/12/2026=seg in new text confirmed).
- `prazos.json` parses; dates and `prazo_em_dobro: false` unchanged (json itself needed no fix).
- `conferir()` green; no placeholders/CJK; `PERGUNTAS.md` re-synced byte-identical to `QUESTIONS.md`.

Final state: `prazos.json` 2,890 B (md5 341d513f…), `memoria.md` 27,249 B (md5 50c53c91…), `STATUS.md` 3,676 B (md5 18ba844a…), `QUESTIONS.md`/`PERGUNTAS.md` 4,612 B each (md5 525d6fb8…). Status remains **COMPLETE WITH OPEN ITEMS** (U1–U5). Ready for delivery.