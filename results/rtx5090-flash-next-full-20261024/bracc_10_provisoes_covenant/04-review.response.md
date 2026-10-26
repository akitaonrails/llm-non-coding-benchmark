Good discipline. I'll re-verify everything against the closed library and source documents — first the authorities (every citation must exist in `library/` with the item numbers cited), then the schema, then the arithmetic.

All four authorities check out verbatim. Now the source documents — verifying every factual detail I asserted (law firm name, dates, amounts, clause numbers):

All document facts match. Now the schema compliance check against CONTRACT.md and a full re-read of the deliverables:

Continuing the QA review — I still need to finish the full re-reads (nota was truncated, plus carta, QUESTIONS, STATUS, JSON) and confirm the exact working-rule wording on file naming in CONTRACT.md:

Nota, JSON, and CONTRACT rules are now fully visible. Issues spotted: the "mutuário" typo in nota §3, accent inconsistency ("mutuo" vs. "mútuo" — library uses "mútuo"), the filename mismatch, and PERGUNTAS.md missing. Reading the remaining two files before fixing:

All five deliverables are now re-read end to end. The authority audit and fact audit are clean; what remains are real fixes. Let me locate every occurrence of the items I flagged:

Applying the fixes now. First, let me get the exact current text of every spot I need to edit:

Now the three precision refinements in the letter (amortization amounts and the expert-letter characterization):

Indentation mismatch — the lines carry three leading spaces, not four. Retrying:

Now the filename fixes: rename the JSON, update cross-references, update STATUS, and create the contract-named `PERGUNTAS.md`:

Rename done and cross-refs updated. Now creating `PERGUNTAS.md` as the contract-named mirror:

All green: JSON valid with exact schema keys, recomputed indices match (29.1/9.8 = 2.9694; 27.1/11.0 = 2.4636), zero leftovers of `mutuo`/`mutuário`/`classifications`, and the amortization wording is now consistent everywhere.

## Review complete — QA pass done

The audit itself confirmed the substance: every citation was verified verbatim against `library/INDEX.md` files (no outside authority, nothing labeled unverified that shouldn't be), all facts trace to the client documents, and all arithmetic re-computes correctly. **No conclusion changed.** What I fixed:

1. **Filename compliance** — renamed `classifications.json` → **`classificacoes.json`** (the contract's exact deliverable name) and updated the two cross-references to it in `carta_diretoria.md` and `STATUS.md`.

2. **Missing deliverable name** — created **`PERGUNTAS.md`** (the contract's optional deliverable), a verbatim mirror of `QUESTIONS.md` with a header explaining the dual naming (the contract's deliverable list says `PERGUNTAS.md`, its working rules say `QUESTIONS.md`). `STATUS.md` now lists both.

3. **Wrong legal term** — nota §3 said the AFAC balance is "**mutuário** dos sócios"; `mutuário` is the borrowing party (the company), not the instrument. Corrected to "**mútuo** dos sócios".

4. **Accent consistency** — normalized `mutuo(s)` → `mútuo(s)` across all five files (15 occurrences), matching the library's own spelling.

5. **Fact precision in the letter** — "sentença de procedência" → "sentença de **procedência parcial**" (matches the court document: partial judgment, 02/09/2025).

6. **Precision in Complemento 2's scenario section** — "a provisão que a única carta do especialista diz ser provável" was loose; now states exactly what the letter says: **provável** (equiparação, with a first-instance partial judgment on file) and apenas **possível** (horas extras).

7. **Precision on the amortization figures** (two places) — the old "≥ R$ 0,15–2,15 mi a depender da leitura" and "0,15 mi se o AFAC for capitalizado" blurred two different things. Now explicit: **R$ 2.15 mi** is what the 31/12/2025 test requires under the correct recording (DL cap 26.95 mi); **~R$ 0.15 mi** applies only (a) under the most favorable reading that excludes AFAC from DL, or (b) in 2026+ tests after an effective capitalization — since the January 2026 AGE is a non-adjusting subsequent event (CPC 24) and doesn't move the 2025 test.

Final deliverable set in `workspace/deliverable/`: `classificacoes.json`, `nota_explicativa.md`, `carta_diretoria.md`, `QUESTIONS.md`, `PERGUNTAS.md`, `STATUS.md` — status remains **COMPLETE WITH OPEN ITEMS** (the open items are permanently unknown facts, all logged; they can only worsen, never improve, the numbers).