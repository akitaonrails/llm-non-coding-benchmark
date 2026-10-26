

Let me do a systematic review pass: re-verify every date/weekday assertion in the deliverables with Python, and cross-check every citation against the library text.





Citation check resolved: `art. 1.026` **is** in `cpc_prazos_recursais.md` — my earlier checker mangled the search string; the citation is supported. Now re-reading the memoria to apply the fixes I identified:





I have the full picture now. Before applying fixes, let me re-verify the two hypothetical "dobro" dates and check STATUS.md and prazos.json:





Now the ANEXO fixes — labeling the unsupported consequences as unverified and adding the illustrative-dates caveat:






Review complete — everything now verifies cleanly (JSON valid, 0 weekday errors across all three files, all citations resolve inside `library/`, arithmetic re-counted in Python). Here is what I found and changed:

## Fixes applied

**`deliverable/memoria.md`**
1. **Date error (§1, closing line):** the hypothetical "prazo em dobro" for the contestação was stated as falling "19/01/2027+recesso" — which did not reconcile with the verified recount or the ANEXO table. Corrected to **05/02/2027 (sex)**, the actual 30th business day from 24/11/2026 (cross-checked in Python).
2. **Confusing sentence (§1, Passo 1):** "Publicação = 23/11 ✔ (e não 20/11 nem 23/11 'a contar do dia 19')" was self-contradictory on its face. Reworded: publication is not on 20/11 (holiday) and the count does not start from 19/11 itself.
3. **Unsupported authority (§2, embargos effect):** the library states only that embargos *interrupt* the appeal period (art. 1.026); the resumption trigger ("após a intimação da decisão") is an inference. Now expressly labeled **não verificado**.
4. **Unsupported authority (ANEXO):** "protocolar antes do prazo nunca é intempestivo" now carries an unverified label (notion inherent to the concept of a deadline; no library norm). In the risk table, "perde-se o recurso" was softened to "**intempestiva**" with a footnote: the **revelia** consequence stays anchored (the despacho at fls. 88 itself says "sob pena de revelia"), while the appeal-sanction consequence is flagged as not found in the library.
5. **Illustrative-dates caveat (ANEXO):** added a note that the hypothetical dobro dates are risk-sizing only — the library's 2027 calendar does **not** list Ash Wednesday 2027 (10/02); if it were observed, the hypothetical dobro apelação would be 01/03/2027, not 26/02. The conclusion is unaffected: the true deadline (03/02/2027) passes before any of those dates.
6. **Arithmetic wording (Conferência):** "6 fins de semana" / "5 fins de semana" → "dias de fim de semana" (they are days, not weekends).

**`deliverable/STATUS.md`**
7. Item 1: added the same resumption-trigger caveat.
8. Item 4: extended to state exactly which consequences are labeled unverified (appeal sanction, embargos-resumption trigger, ratio of art. 229 §2º) — none cited as authority.

## Checked and confirmed correct (no change needed)
- **All day-of-week labels** in memoria/STATUS (≈40 assertions): 0 errors against the real calendar.
- **Core arithmetic**: contestação 22−6−1=15 ✔; embargos 5 ✔; apelação 52−32 (recesso) −5 (fins de semana) =15 ✔; holiday traps 20/11/2026, 08/12/2026 (Campinas), 25/01/2027 counted ✔.
- **Every article cited** (219, 220, 224, 229 §1º/§2º, 231 VII, 335 III, 1.003 §5º, 1.023, 1.026, Lei 11.419 art. 4º §§3º-4º, Lei 14.759) exists in the library files — including art. 1.026 in `cpc_prazos_recursais.md` (an earlier "not found" was a bug in my own checker, not a phantom citation).
- **prazos.json**: valid JSON, schema-compliant, dates consistent with memoria; the earlier stray CJK character is gone; no other non-Latin artifacts.
- **Document facts** (e-SAJ on both PDFs, fls. 61/70/88, "sob pena de revelia") all trace to `documents/`.

Final dates unchanged: **contestação 15/12/2026**, **embargos 18/12/2026**, **apelação 03/02/2027**, all in **simplo** (art. 229, §2º). Status remains **COMPLETE WITH OPEN ITEMS** — the open items are the declared assumptions (no DJe outage; no embargos filed), now documented with their unverified labels intact.