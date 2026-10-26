Good practice — let me re-read the full deliverable against the library, and audit citations and arithmetic.

Com a correspondência exata em mãos, aplicando todas as correções identificadas na revisão — erros gramaticais, uma referência cruzada incorreta, duas afirmações muito fortes e o alinhamento com a redação literal da biblioteca:

All nine edits have been applied. Now the remaining four: the wording of §5 (the library says "IRPFM," not "IRPF annual"), the two overly strong cells in the §8 table, and the §9 premise that claims a fact the client has never confirmed:

All 13 edits have been applied. Now doing a final consistency check of the entire document and an audit of citations in a single pass:

Picking up where the review left off: the citation audit passed (INDEX line 8 confirms "redação da Lei 11.051/2004"; CTN 151-III is properly attributed to the e-CAC report and the library file itself). Now I need the exact current text for the two known typos and the remaining wording items:

Both typos have been confirmed, and the wording issue in "instrução/exigida pelo arquivo" (lines 31/36, ambiguous phrasing) is also confirmed. The uses of "pedimos/perguntamos" (lines 40, 58, 105) are factually correct in the past tense — these questions were actually sent and remain unanswered, so there's no need to touch them. Applying the final corrections now:

Final verification sweep — residual artifacts, JSON validity, and STATUS note in one pass:

Review complete — all fixes applied, nothing left unreconciled. Here is the full change list:

## Fixed in `parecer.md` (17 edits, redaction/precision only)

**Unsupported or over-strong authority claims (softened to what the library actually says)**
1. **§4** — "garantia/depósito/parcelamento é o que *afasta a vedação*" → now "afasta **o gatilho literal**", with an explicit flag that *no library item expressly treats the effect of guaranteeing* — it's a textual reading of "não garantido", not cited authority.
2. **§8 table, "Distribuir no futuro"** — "*elimina* o litígio do art. 32" (overclaim) → "afasta o gatilho literal do art. 32… leitura textual, ver §4".
3. **§8 table, "Pró-labore / compensos"** — replaced with "Pró-labore (remuneração de sócio-administrador)" and marked the "outside art. 32" point as *inferência textual, não item da biblioteca* (art. 32 literally covers "bonificações" and "participação de lucros", not remuneration).
4. **§9 item 2** — removed "(sem atualização de valor, sem decisão)", a fact the client never confirmed → "o cliente **não informou** decisão, parcelamento ou atualização do valor".
5. **§4** — "≈2 anos na DRJ em janeiro/2026" (invented precision) → "entre um e dois anos na DRJ — o mês da impugnação não foi informado".

**Does-not-reconcile fixes**
6. **§4 penalty cap** — added an explicit "Leitura do teto" bullet: the library wording "limitada a 50%…" agrees with "multa", so the natural reading is **per-fine** (400k + 400k = 800k, adopted as max in `numeros.json`); if the cap were read as **global**, max = 740k. Both figures now shown (§1 item 3 cross-references §4).
7. **§3.1** — "(§4 acima)" → "(§4 abaixo)" — wrong cross-reference direction.

**Language/typos**
8. "para a RFB, *sufficientes* para a vedação" → "isso basta para a vedação"; also "está suspensa a exigibilidade" → "tem a exigibilidade suspensa".
9. "a escrituração é o próprio régua" → "a própria régua legal".
10. "se quiseram distribuir" → "se quiserem distribuir antes de superada a controvérsia".
11. "**Lucuros** futuros" → "Lucros futuros" (§3.1 d.4).
12. "para **delibirar**" → "deliberar" (§5).

**Literal library wording**
13. **§5** — "antecipação do IRPF anual" → "antecipação do **IRPFM** (redação literal de `library/lei15270_2026.md`)" — the library says IRPFM; the annual-return treatment is outside the library.
14. **§2/§3** — "presunção 32% mantida por instrução do arquivo / exigida pelo arquivo" (ambiguous) → "conforme registrado no arquivo".

## Checked and deliberately **not** changed
- **Citation audit passed**: every statute cited maps to the 5 `library/INDEX.md` items; "Lei 11.051/2004" is itself part of the INDEX citation (line 8); "CTN art. 151, III" is only ever attributed to the e-CAC report and `library/lei4357_art32.md`, never cited as direct authority. IOF table beyond art. 13, IRPF progressive brackets, pró-labore/INSS remain labeled **não verificado**.
- **`numeros.json`**: re-validated against the contract schema — valid JSON, all keys present, **zero values changed** (0 / −310.000 / 1.120.000 / 80.000 / 800.000 / mutuo não recomendado).
- Arithmetic re-verified earlier (2.048.000; 1.494.400; −41.600; 80.000; 740.000/800.000; IOF 13.328; Δ760.000) — all correct.
- The R$ 760.000 balance-sheet divergence remains flagged, never forced — conclusion (distributable = 0) holds under every hypothesis.

**Bottom line:** no number and no conclusion changed — the answer remains *não distribua os 800 mil; mútuo não recomendado*. `STATUS.md` now records the review pass. Ready to deliver.