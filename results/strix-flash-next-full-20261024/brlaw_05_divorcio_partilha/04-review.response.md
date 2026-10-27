Reviewing before delivery. First, re-reading the library (the only citable authority) and the source documents to verify every citation and fact:

Library and documents confirmed. Now re-reading the deliverables to audit each citation and figure against them:

Re-reading the full deliverables to apply precise fixes:

Now verifying exact library wording for the passages I need to fix (1.659 I, Súmula 358, ITBI trigger, quotas/fruits):

Verifying the STJ library file's exact wording on quotas/fruits/profits before finalizing fixes:

All citations verified against the library — they match. Now applying the audit fixes. First the markdown memo:

Now the JSON deliverables:

Re-validating JSON integrity and all arithmetic after the edits:

Final sweep for stale numbers or leftover wording across all deliverables:

Checking the two question files for stale rev. 1 figures:

Final validation sweep:

Audit complete. All citations were checked line-by-line against `library/` (every REsp number, chamber, year and statutory paraphrase matches), and all sums were re-verified by script. Here is what the review found and what I changed:

## Fixed (errors / unsupported authority / reconciliation)

1. **`STATUS.md` — stale numbers (real error).** Still carried rev. 1 figures (partilhável 2.290.000; meação 1.145.000; equalização 995.000; pensão 7.166,67; 3.490.000 = 1.145.000 + 2.345.000). Rewritten with the current figures: 2.410.000 / 1.205.000 / 1.055.000 / 10.916,67; 3.490.000 = 1.205.000 + 2.285.000.
2. **`QUESTIONS.md` / `PERGUNTAS.md` — violated the "don't re-ask answered questions" rule and had a stale figure.** They still asked about pró-labore/profit distribution and whether there was a reform in Atibaia — all already answered. Removed; the reform question became a *proof* request (documents + whether the 800.000 appraisal already reflects it). Also corrected the payment figure **R$ 445.000 → ~R$ 505.000** at signing (rev. 1 number, before the 60.000 reform credit and 75.000 retentions).
3. **`proposta_acordo.md` §1 — misleading characterization of Fernanda's FGTS proposal.** Her proposal *concedes* the FGTS (leaves it with Marcelo); it doesn't "ignore" it. Reworded: she cedes an item case law would give her — the concession must be written into the agreement, not treated as "it's his."
4. **`proposta_acordo.md` §3 — unsupported factual assertion deleted/flagged:** "ITCMD da herança de Atibaia já recolhido no inventário (2019)" appears nowhere in the library or documents (the formal de partilha does not record payment) → now flagged **NÃO VERIFICADO**, with note that it has no effect on this partition.
5. **`proposta_acordo.md` §3 — ITBI trigger tightened.** The library only triggers ITBI on **excess of meação compensated with payment/other particular goods**. In the equalized partition there is no excess; applying ITBI to cash equalization is an *interpretation* — the 18.000 exposure estimate is now expressly labeled as such (NÃO VERIFICADO), not presented as a library rule.
6. **`partilha.json` (Benfeitorias) — incomplete paraphrase of CC 1.659, I.** My text said "só o bem recebido por sucessão e os sub-rogados"; the library's text also excludes goods possessed at marriage and those received by **donation**. Quoted accurately now.
7. **Atibaia "non-shareable appreciation" formulation refined** (partilha.json + proposta §2/§7): previously said the library "só comunica frutos (1.660, V)" — but the library *does* treat appreciation from common effort as communicable for **quotas**. Now stated precisely: no rule extends that to particular **real estate** → NÃO VERIFICADO, with the 90.000 negotiation ceiling preserved.
8. **Typo** "Meadia de cada cônjuge" → "Meação" (§2 table).
9. **`alimentos.json` wording:** "parcelas não tributáveis" → "parcelas que a biblioteca exclui da base de cálculo" — the exclusion of FGTS/verbas rescisórias is about calculation-base nature, not tax.
10. Memo header now marked **rev. 2.1** (pre-delivery consistency review; no values changed); STATUS.md records the audit.

## Considered and deliberately not added

- **Súmula 358** (in the library's citation line): the library lists it but does **not transcribe its content**, so citing its proposition would exceed the verified authority. Left out.
- **EREsp 1.623.858** (in the library): unused; not needed for any position taken.

## Verified clean (no changes needed)

- All citations match the library exactly: REsp 1.399.199/RS (2ª Seção, 2017), REsp 1.595.775/AP + CC 1.027, REsp 1.698.774/RS (3ª Turma, 2020, 4ª Turma contrary on VGBL), REsp 1.332.808, "AgInt no AREsp" (library itself gives no number), CC 1.658–1.662, 1.664, 1.583/1.584 §2º, IN RFB 84/2001, Lei 10.705/2000, CTN 35.
- Arithmetic re-run mechanically: 7 asset rows sum to TOTAL (3.850.000 / 2.410.000 / 1.205.000); meação = half; equalization 1.205.000 − 150.000 = 1.055.000 = 450+70+550+60−75 = 505+550; alimentos base 524.000/12 = 43.666,67 → 25% = 10.916,67 (anchors 8.733,33 / 13.100,00).
- No stale numbers ("445.000", "2.290.000", etc.) remain anywhere; both JSON files parse.