Good checkpoint. Let me re-verify every number and citation in the deliverables against the library, plus run reconciliation tests on the trial-balance profit figure.

The verification runs are done — now I'll apply the fixes. Let me re-read the exact passages in `memorando.md` I need to correct.

§8 step 5's credit list (energy, rent, depreciation of machinery in service provision) is supported by the file. Let me verify the remaining three library files:

All library content verified. Before applying fixes, let me confirm the reconciliation arithmetic precisely:

Let me re-read the full memo and the rest of STATUS.md to get exact text for the edits.

All content verified. Now applying the fixes. First, let me check QUESTIONS.md structure to decide where the new open reconciliation item goes:

Now applying all review fixes to `memorando.md`:

Four edits applied. Now the §5-bis reconciliation section, the U6–U8 additions, A4 refinement, and R1 update:

All verification checks pass — `creditos` is a deduction in the Real block (388.500 − 83.250 = 305.250 líquido; soma fecha em 1.080.790). A revisão está concluída e gravada em disco. Segue exatamente o que mudou:

## Revisão concluída — o que foi alterado

### `memorando.md`
1. **§2 (Fator R)** — removida a afirmação "Fator R 30,95% ≥ 28% → Anexo III" como fundamento: a regra que vincula Fator R ao Anexo III **não consta da biblioteca** (U2). O enquadramento em Anexo III agora se apoia apenas no dado explícito do balancete; o Fator R ficou como checagem de consistência.
2. **§3 (DAS Anexo III)** — o passo "alíquota efetiva da RBT12 aplicada à receita segregada de cada anexo" foi rotulado como **inferência** (a Res. CGSN 140, arts. 9º-12, é citada no arquivo mas não transcrita) → novo item **U7**.
3. **Novo §5-bis (conferência do balancete)** — o ponto que **não reconcilia**: 4,2M − 1,4M − 1,3M = 1,5M; para o lucro de 756.000 se sustentar, tributos embutidos + custos não listados têm de somar 744.000. Duas leituras descartadas por aritmética (carga Simples embutida → custos −164.460; CPP destacada → −103.750). Leitura adotada (A4): PIS/COFINS + ISS embutidos, CPP dentro de encargos → **260.250 de "demais custos" não itemizados**. Tabela de sensibilidade e **break-even LCRI = 249.147** (3× de margem vs. 756.000). Único cenário que inverteria o ranking: se a linha for "antes de todos os tributos" (LCRI −91.750 → Real 847.750, ~60,7 mil mais barato) — contradiz o rótulo, mas não descartável sem DRE itemizada; **item aberto, não forçado**.
4. **§6** — A4 refinada (CPP do Real dentro da linha de encargos; CPP destacada não conciliável, remete ao §5-bis); acrescentados **U6** (arts. 3º §§1º/9º, 20 e 30 citados mas não transcritos), **U7** e **U8** (nenhum excerto específico de Lucro Real na biblioteca; alíquotas gerais aplicadas ao LCRI sem adições/exclusões).
5. **§7 (R1)** — ressalva quantitativa: rank robusto enquanto DAS-IV ≤ ~214 mil (efetiva ~34%); break-even LCRI 249.147; ressalva do cenário de inversão (§5-bis).
6. **§8-ter (a)** — removida a alegação sem respaldo de que a exclusão por excesso (art. 26) seria "**a única** saída retroativa do sistema"; agora apenas: o acervo não contém regra de saída no meio do exercício, e o art. 26 não consta da biblioteca nem se aplicaria (não estouraram os 4,8 mi).
7. **§9** — registradas as divergências INDEX vs. corpo dos arquivos (`lc123` transcreve art. 3º II e 18 §4º IV, não listados no INDEX; `lei9249` transcreve o art. 26 da Lei 9.430, não listado); fechamento atualizado para U1-U8.

### `STATUS.md`
8. Itens **8 e 9** acrescentados (não conciliação do LCRI 756.000 + P8; e U7/U8). Total de abertos: 9. Situação permanece **COMPLETE WITH OPEN ITEMS**.

### `QUESTIONS.md` / `PERGUNTAS.md`
9. Nova seção "Rodada 3" com **P8**: pedido da DRE projetada itemizada por trás dos 756.000 (se PIS/COFINS/ISS estão descontados nessa linha; se a CPP está nos 1,3M de encargos; quais os ~260 mil não itemizados). `PERGUNTAS.md` atualizado para P1–P8.

### O que **não** mudou
- **`comparativo.json`** — intocado: todos os totais re-somados e batem (Simples 908.460; Presumido 1.074.580; Real 1.080.790 com créditos como dedução). A recomendação (permanecer no Simples) e os números do comparativo não mudaram em nenhum cenário testado compatível com o rótulo do balancete.

**O que não reconcilia e ficou aberto:** a linha "lucro antes de IRPJ/CSLL = 756.000" do balancete não fecha com as linhas de custo na leitura literal; adotei a única leitura aritmeticamente possível e sinalizei a única leitura alternativa que inverteria o ranking (pendente da P8).