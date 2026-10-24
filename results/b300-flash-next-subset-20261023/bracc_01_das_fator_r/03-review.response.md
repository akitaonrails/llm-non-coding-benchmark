

Good practice. Let me re-verify everything from scratch: the contract schema, the library (sole citable authority), the source documents, and every number.






Library verified — key confirmations and one schema issue spotted. Now the source documents:









XML and PDF check out. Full numerical recomputation:





Now let me read the remaining deliverables before applying the edits:






All deliverables reviewed. Now applying the remaining fixes to `memoria.md`:






Review complete. Every citation was checked verbatim against the library, every number recomputed, and the reconciliation redone. The core result — **DAS maio/2026 = R$ 15.188,84 (Anexo V services + segregated locação)** — survived; five issues were found and fixed:

## What I fixed

1. **`apuracao.json` didn't match the contract's schema** (worst finding). I had invented key names (`faturacao_bruta_12m`, `das_a_pagar`, `ANEXO_V`, lowercase `irpj`…). Rewrote it with the contract's exact keys: `rbt12`, `folha_12m`, `fator_r`, `anexo: "V"`, `faixa`, `aliquota_nominal`, `parcela_deduzir`, `aliquota_efetiva`, `receitas{servicos,locacao}`, `das{servicos,locacao,total}`, `reparticao{IRPJ,…,ISS}`. Values unchanged; repartição now validated to sum exactly to the DAS total (15.188,84).

2. **False reconciliation note in the repartição** (`memoria.md` §4). I had written "centavo rounding adjustments absorbed in CPP" — untrue. The library's Anexo III 4ª-faixa cotas sum to **99,85%, not 100%**: strict cotas give locação CPP = 320,78 and a parts-sum of 505,36 vs the 506,49 actually paid → a structural **R$ 1,13 residual (0,15 pp gap)**. Rewrote the note honestly (residual allocated to CPP → 321,91, flagged as a disclosed methodological choice, not rounding), and recorded it as a new open item: §5 item 7, **U6** in QUESTIONS/PERGUNTAS, item 7 in STATUS. Also clarified that the services cotas sum to exactly 100,00% (no adjustment there).

3. **Unsupported precision in the April-DAS counterfactual** (§5 item 3). I asserted "RBT12 abr = 933.000" — but April's 12-month window requires **mai/2024, which isn't in any file**; 933.000 is an 11-month partial sum. Reworded: partial-window **floor** ≥ 933.000, 4ª faixa nevertheless guaranteed (11 months already > 720.000); the comparison figures (16.240,47 / 10.596,66 / ~10.359) relabeled as floors/approximations. U5 synced.

4. **Citation attribution error** (header). §5º-A was attributed to `lc123_art18_fator_r.md`, whose INDEX citation doesn't list it — it's cited by `locacao_bens_moveis_iss.md`. Corrected the attribution and noted that §4º (segregation) appears in the lc123 file's body rather than its citation line. All other cited provisions (§§1º, 1º-A, 5º-J/M, "valores pagos", estorno rule, cotas, tables, SV-31) re-verified verbatim.

5. **Stale cross-references**: "PERGUNTAS.md #4/#5", "pergunta 3/5 sem resposta" updated to the current identifiers (U2/U3/U4). QUESTIONS.md and PERGUNTAS.md confirmed byte-identical.

## Re-verified with no change needed

- RBT12 = 1.020.000 (4ª faixa); folha = 193.000 + 35.200 + 56.400 = 284.600; **Fator R = 27,9020% < 28% → Anexo V** (library says "igual ou superior a 28%" → III — direction confirmed); effective 18,823529% → 14.682,35; locação 12,505882% × (1−0,3250) = 8,441471% → 506,49.
- Estorno rule ("reduz a receita do mês em que ocorrer") — verbatim in the library; NFS-e 1188 treatment stands.
- Extrato: credits 88.000, debits 43.180,22, closing 86.100.33 = 41.280,55 + 88.000 − 43.180,22 ✓ (PDF text matches CSV); XML NF-e 512: natOp locação, CFOP 5949, 6.000, 26/05 ✓.
- Sensitivity: scenario D (pró-labore mar/26 → 287.800 → 28,22% → III → 10.261,08) still the only flip risk; U1–U5 remain open, none re-asked.

Nothing was force-balanced: the 1,13 gap, the missing mai/2024 month, the missing mar/2026 extrato and the unverified Anexo V cotas are all disclosed in §5, STATUS (**COMPLETE WITH OPEN ITEMS**), and U1–U6.