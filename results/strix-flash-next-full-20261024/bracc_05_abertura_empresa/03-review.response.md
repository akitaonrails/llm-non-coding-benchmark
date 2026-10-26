I'll audit systematically: (1) every citation against the actual library files, (2) every fact against the client documents, (3) all arithmetic. Starting with the library index and files:

The CC file is thinner than my usage of it — noted. Reading the remaining library files:

Documents read. Now grepping my deliverables for facts that may not match the sources:

All files audited. Checking CONTRACT.md schema line before touching `numeros.json`:

Schema confirmed. Continuing contract fixes — citation of clause 2, names, and clause 3:

Clause 4ª (admin appointment language + Marina's agency), 5ª typo, 7ª imóvel:

Retry with exact original text:

Continuing the review fixes. Re-reading current file states to apply the remaining edits precisely:

Now applying the remaining contract and checklist fixes:

Now reading parecer, QUESTIONS, PERGUNTAS, and STATUS in full for exact edit targets:

Now the parecer fixes. First confirming the exact library wording of CTN art. 37 for the §2.2 correction:

Library wording confirmed. Applying the three parecer fixes:

Now fixing Q8 in both QUESTIONS.md and PERGUNTAS.md, and updating STATUS.md. Reading PERGUNTAS first to keep the mirror exact:

PERGUNTAS mirrors QUESTIONS. Applying Q8 fix to both files and the STATUS updates:

Adding the revision-round log to STATUS.md:

Now the `numeros.json` wording tweak — reading it fully first:

Applying the final `numeros.json` wording fix:

Now re-validating `numeros.json` against the exact CONTRACT.md schema and running the final forbidden-string sweep:

Schema validation passes. Final consistency check — confirming the "Anexos VI/VII" citation in the parecer matches the library's own citation line, and reviewing the final `numeros.json`:

All fixes are applied and re-validated. Here is the complete review outcome and list of changes.

## Review findings & corrections (round v3)

**Audit method:** every legal citation re-checked against `library/INDEX.md` + the 7 library files; every factual claim re-checked against the 3 files in `documents/`; all arithmetic recomputed.

### 1. Fabricated facts removed (worst class of error — replaced with document-sourced values)
- **Marina's agency:** "IBGE" → **Ministério da Saúde** (the questionnaire says "analista, Ministério da Saúde, 40h"). Fixed in `contrato_social_ajustado.md` (cláusula 4ª), `QUESTIONS.md` and `PERGUNTAS.md` (Q8).
- **Invented full names** ("Marina Alves da Costa", "Luana Barros de Moraes", "Felipe Gomes da Costa") → document names **MARINA COSTA / LUANA PRADO / FELIPE COSTA** + `[A DEFINIR: qualificação]` (cláusula 3ª table, cláusula 4ª, signature block).
- **Invented street address** ("Rua Maria Jaiba Siqueira, 32…") → matrícula wording: **"Sala comercial nº 1204, Ed. Aurora Office, 180 m²"** (cláusula 1ª e 7ª); the street was never given in the documents.

### 2. Unsupported legal authority corrected
- **CC art. 1.057 does not exist anywhere in the library.** Cláusula 8ª (cessão de quotas) and checklist item 1 rewritten as contractual practice with explicit `[NÃO VERIFICADO]` flags + 3 items for outside counsel.
- **"Decreto 731/1993 e IN DREI citados na biblioteca"** — they are **not** in the library (only IN DREI 81/2020, re preferred quotas). Cláusula 14ª corrected.
- **"IN DREI 81/2020, art. 34" as non-compete basis** (cláusula 9ª) — the file mentions IN DREI only re quotas preferenciais; corrected.
- **"Anexo VI" for CNAE 9602-5/02** → library literal says **Anexo III**.
- **CTN art. 37 "parágrafo único" numbering** — library doesn't transcribe paragraph numbering; replaced everywhere with the literal rule ("para empresa nova, apuram-se os 3 anos seguintes") — contrato A.2, checklist item 8, parecer §2.2, `numeros.json`.
- **CTN art. 36 paraphrase** ("não desmembra o imóvel") tagged `[NÃO VERIFICADO: texto não reproduzido na biblioteca]` in A.2.
- **Administrator as "ato separável"** → library only supports "designados no próprio contrato" (cláusula 4ª); apartado taggage NV.
- **GFIP/eSocial** (cláusula 12ª) — systems not mentioned in the library → tagged `[NÃO VERIFICADO]`.
- **§2.3 parecer:** "registrar CNAE sem exercer a atividade" now explicitly tagged as *interpretation* (the library bars the activity, not the bare registration).

### 3. Omission filled
- **Lei 15.270/2025 transitional rule** (profits accrued through 31/12/2025, approved by that date, stay exempt if paid through 2028 — library literal) added to parecer §4.3, noted as **inapplicable** (company opens only in 2026).

### 4. Text errors
- Garbled CTN-37 sentence in parecer §2.2 rewritten with literal library quote; "discriminación" → "discriminação" (5ª); "balanho" → "balanço" (checklist 12).

### 5. Validation
- `numeros.json`: wording tweak applied (itbi.fundamento); one transient JSON break from embedded quotes was caught and fixed — file now **parses and matches the exact CONTRACT.md schema** (keys/types verified by script; values unchanged: ITBI false/0; integralização 420.000 / ganho 0; pró-labore 0/5.000/8.000; pretensão 50.000; IRRF 0; `simples_possivel: false` = plan as presented).
- Final grep sweep: no unsupported strings remain except inside explicit `[NÃO VERIFICADO]` flags and the correction log.
- Arithmetic re-verified: 96.000 ÷ 1.296.000 = 7,4% < 50%; 13.000 × 11% = 1.430; capital 24.000 = 19.200 + 4.800. The **R$ 600 mil/ano de retiradas vs. R$ 420 mil de lucro** mismatch is deliberately left open in the parecer (not forced to reconcile).

The correction log is also recorded in `deliverable/STATUS.md` ("Revisão pré-entrega (v3)"). All seven deliverables are final and ready for the client.