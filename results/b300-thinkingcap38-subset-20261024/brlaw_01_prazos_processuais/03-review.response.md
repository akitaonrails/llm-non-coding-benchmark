

I'll do a systematic review — re-reading each deliverable in full, then cross-checking every date, weekday, rule, and citation against the source PDFs and library.







I've confirmed both issues: the library only states that the motion for clarification **interrupts** the deadline for appeal (CPC Article 1.026, mentioned within the file), but line 110 says "do fim da suspensão (at the end of the suspension)" — this is an unsupported detail. Also, "a antecipação é sempre admitida (early filing is always permitted)" (§6) is not a rule in the library. Applying the fix now:






Now re-validating the JSON and confirming the edits landed cleanly:





Review complete. I re-read all three deliverables in full and cross-checked every date, weekday, rule, and citation against the two DJe PDFs, `procuracoes_resumo.md`, and the four library files. Findings and changes:

## Errors found and fixed (all in `memoria.md`)

1. **Unsupported legal detail — line 110 (§3.2, apelação note).** The note said the 15 days would "recomeçam do fim da **suspensão** determinada pelo art. 1.026." The library (`cpc_prazos_recursais.md`) only states that the motion for clarification **interrompe** (interrupts) the appeal deadline (art. 1.026, mentioned in the file's text). "Suspensão" is a different legal mechanism and is not supported by the library. Reworded to: the deadline is **interrompido** (art. 1.023; art. 1.026, *conforme referido no arquivo da biblioteca*), "caso em que o vencimento do recurso precisará ser recalculado" — no mechanism beyond what the library states.

2. **Uncited rule presented as fact — §6 risk table (line 147).** "a antecipação é sempre admitida" is not in the library, but the whole asymmetric-risk argument rests on it. Relabeled per the working rules: "protocolar antes do vencimento não torna o ato intempestivo (**premissa prática de gestão de prazos — não há regra sobre o ponto na biblioteca**)."

3. **Consistency with fix 2 — §6 closing paragraph (line 150).** Added "(com a ressalva da premissa prática acima: o protocolo antecipado é tempestivo)" so the "safe under either interpretation" claim carries the same label.

## Verified clean (no changes)

- **Dates and weekdays** — re-verified all against the library calendar: citação 19/11 (qui) → publicação 23/11 (seg, after 20/11 Zumbi holiday + weekend) → início 24/11 (ter) → contestação **16/12/2026 (qua)** (08/12 municipal holiday skipped); sentença 10/12 (qui) → publicação 11/12 (sex) → início 14/12 (seg) → embargos **21/01/2027 (qui)** and apelação **04/02/2027 (qua)** (recesso 20/12–20/01 honored; 25/01/2027 is Capital-only, counted as business day in Campinas). Day-by-day tables match the Python count.
- **Hypothetical double-period contestação** = 10/02/2027 (30 business days, Carnival 08–09/02 accounted for) — confirmed.
- **Citations** — every rule in `memoria.md` (R1–R9) and every statement in `prazos.json`/`STATUS.md` traces to one of the four indexed library files; art. 1.026 is now explicitly framed as "referido no arquivo da biblioteca," not an independent citation.
- **`prazos.json`** — parses, schema-conformant, all values correct; the `dias_suspensos` list covers every non-business day in the 14/12/2026–04/02/2027 window with no gaps.
- **`STATUS.md`** — accurate as-is; no edit needed.

**Net change: 3 edits, all in `memoria.md`; `prazos.json` and `STATUS.md` untouched.** Deliverables remain COMPLETE.