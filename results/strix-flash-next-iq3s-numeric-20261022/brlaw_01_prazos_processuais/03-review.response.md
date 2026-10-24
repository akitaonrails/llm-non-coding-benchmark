I'll re-verify everything: re-run the calendar math independently, check every citation against `library/INDEX.md`, and re-read the deliverables for internal consistency.

Fixing the script's formatting bug (single arg vs. two `%s`) and re-running the clean verification:

Now I'm going to apply the fixes. First, I'll get the exact wording of the despacho (court order) in order to solidly back up the application of Article 231, Section VII, and re-read STATUS.md:

Final consistency sweep across all three deliverables:

JSON keys differ from my guess — let me validate properly:

Review complete. Everything reconciles now; here's the accounting.

## What I re-verified (no change needed)

1. **All four dates, recomputed independently** with a fresh script that rebuilt the holiday set directly from `library/calendario_forense_campinas.md`: Contestação **15/12/2026 (ter)**, Embargos **18/12/2026 (sex)**, Apelação **03/02/2027 (qua)**, hypothetical dobro **05/02/2027 (sex)**.
2. **Every weekday label in the calendar file** checked against the real calendar — all truthful (incl. 20/11/2026 = sex, 19/11/2026 = qui as stated in the DJe extract).
3. **The 25/01/2027 trap**: a sensitivity run confirmed that wrongly treating it as a Campinas holiday (the calendar row says "feriado municipal **APENAS na Capital**") shifts Apelação to 04/02/2027. The deliverable's treatment (business day in Campinas) is correct.
4. **Every citation** (CPC 219, 220, 224, 229 §§1–2, 231 VII, 335, 1.003 §5º, 1.023, 1.026; Lei 11.419/2006 art. 4º §§3º–4º; Lei 14.759/2023) traced back to the four files in `library/INDEX.md` — no outside sources cited.
5. `prazos.json` is valid JSON and internally consistent with `memoria.md` (no stale dates anywhere).

## Errors found and fixed

1. **Unsupported authority — `memoria.md` §4**: I had written that embargos "interrompem, o prazo da apelação recomeça inteiro, e não de onde parou" as if settled. The library only says embargos "interrompem o prazo... (art. 1.026)"; it never defines interruption vs. suspension. Rewrote §4 with the library-supported rule, and the restart-from-zero reading now explicitly labeled ***interpretação não verificada***; also cleaned a garbled clause in the same paragraph. `STATUS.md` item 1 aligned with identical wording, plus "03/02/2027 vale apenas se não houver embargos."
2. **Arithmetic imprecision — `memoria.md` §0**: "quase 7 semanas de diferença" → "**52 dias** de diferença (≈ 7 semanas e meia)" — 15/12/2026 → 05/02/2027 is 52 days, verified.
3. **Under-grounded step — `memoria.md` §1.2**: the leap to art. 231, VII was asserted abstractly. Now anchored in the record: verbatim quote of the fls. 88 despacho ("Cite-se e intime-se... na pessoa de seu advogado constituído") + the exact statutory chain art. 335 III ("de acordo com o modo como foi feita a citação") → modo = DJe → art. 231 VII ("data de publicação... Diário da Justiça... eletrônico").

**Not changed**: `prazos.json` (schema and values all verified correct). Deliverables remain **COMPLETE WITH OPEN ITEMS** — the open items are genuine contingencies (conditional apelação date, regularity assumptions), not gaps in the work.