Good checkpoint. Let me re-read the deliverables in full, scrutinize citations against `library/INDEX.md`, and re-check every number.

The structural defect and text fixes are queued. First, let me re-verify the exact library wording for the three statements I suspect are under-supported (monitória rito, art. 202 rol, protesto effects).

Structure fixed. Now the authority-flagging and arithmetic/typo fixes:

Two remaining precision fixes inside §5-bis itself:

Now the full verification pass plus a stale-text scan:

Section order is correct; my check script guessed the wrong JSON key. Re-running against the actual structure:

Review done. I re-verified every citation against `library/INDEX.md`, recomputed every number, and repaired the file structure. Changes made to `memorando.md`:

**Structural (real defect)**
1. **§5-bis was sitting in the middle of §5** — the "Total estimado sem IPCA", "Premissas sinalizadas" and "### 5.3 Parcelas 5–6" blocks dangled *after* it. Reordered to: 5.1 → 5.2 (table, total, premissas) → 5.3 → 5-bis → 6. No content lost (duplicate-paragraph counts verified = 1 each).

**Unsupported authority — downgraded to "not verified in library" (3 cases)**
2. §4: "monitória preferível **por converter a prova escrita em título executivo judicial** (fase de mandamento inicial)" — the CPC file in the library holds only art. 700 caput and the cobrança alternative; the conversion/rito is **not in the library**. Rewritten: preference stated as strategic judgment, with the conversion/embargos expressly flagged as off-library.
3. §7: "O protesto **não tem efeito de interromper prescrição**" — the art. 202 excerpt in the library lists items I and VI but truncates the rest with "…", so the closed library cannot prove protest is absent from the full rol. Rewritten: "não verifiquei causa interruptiva relacionada a protesto na library — não contem com ele".
4. §7: "constituição em mora pública" via protesto — no such effect appears in the Lei 9.492 entry; removed as a claimed effect, kept only probative/pressure value (flagged).
5. §5-bis(ii): "o rol do art. 202 **exige** ato de fora do credor" — same truncation issue; rephrased to what the excerpt actually verifies, with the flag.

**Arithmetic**
6. §8: "+R$ ~**1.287** de juros por mês" was wrong — 1% a.m. × R$ 110.000 saldo = **≈ R$ 1.100/mês** (still sem IPCA). Corrected.
7. §5-bis: "11 meses a mais" → **~10 meses e meio** (02/08/2028 − 15/09/2027), precise.

**Text/typos**
8. "aval/**cisão** de cheque-fiança" → "aval, fiança ou caução" (kept off-library flag).
9. "meses **intes**" → "meses inteiros".

**Schema clarity**
10. §3: added a reading note — in `analise.json` the key `novo_termo` records the **final** term of the re-counted period (2027-09-15); the re-count starts from the interrupting act (15/09/2022, art. 202 par. único). JSON itself untouched (fixed schema).

**Verified clean, no change needed:** all cited authorities (CC 189/202/206 §5 I; CPC 700/784 III; Súmulas 299/385/503; REsp 1.438.263 and 1.792.700; Lei 9.492/97; CDC 43 §5º; Temas 1.264 and 1.247; CC 389/406 + Lei 14.905/2024) each map to a library file; juros sum 17.796,67+21.320+21.020+20.720 = **80.856,67**; total **193.256,67**; JSON reconciles (110k+10k+60k = 180k; 110k+70k = 180k); section order and `STATUS.md`/`QUESTIONS.md` consistency confirmed.

No conclusion changed. `STATUS.md` now carries the QA pass as item 0-bis; engagement remains **COMPLETE WITH OPEN ITEMS** with the same four residual gaps (IPCA series, PIX imputation rule, post-interrução filing mechanics, assumed absence of confession/guarantee).