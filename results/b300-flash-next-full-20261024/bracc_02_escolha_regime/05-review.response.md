

Pre-delivery review it is. I'll re-read everything — contract, library sources, client documents, and all four deliverables — then re-run every calculation and audit each legal assertion against its cited source.








Sources and documents re-read. Now the deliverables themselves — full memo, JSON, and status files:






All totals reconcile exactly. Now I need the full memo text to pin down the wording fixes — the earlier read was truncated:






Now the remaining memo sections (§6 through Anexo A):





Full picture assembled. The arithmetic audit passes on every line; the findings are in authority support and consistency. One more look at the memo's first 19 lines so I can edit line 6 precisely:





Audit complete. All totals, deltas, and sensitivity numbers reconcile exactly against the library-sourced rates. Findings requiring fixes: **2 unsupported-authority issues** (the "≥28% Fator R" threshold and the "encargos/FGTS aren't CPP base" claim — neither is in any library file; the library only says CPP is computed "sobre a folha" without defining it), **1 unstated-default-rule claim** ("Real de ofício" — no library text), **1 arithmetic-precision error** (break-even payroll base stated "~715 mil" where it's actually R$ 717.429), plus three consistency/clarity items. Applying the fixes:









First five applied. Now the break-even precision, CPP-base authority labels, the sublimit-timing gap, and the §6 date cross-reference:









Now let me verify the full memo after all edits — and I want to double-check one line where I may have introduced a stray word:






All ten fixes are in place. Two final consistency catches: line 85 has a stray English word ("likewise") I introduced, and line 109 still phrases Q6 as an open confirmation request although round 4 closed it. Fixing both, plus adding the review note to STATUS:







Final check that `comparativo.json` is untouched and still schema-valid:





My quick-check used the wrong nested key names — let me look at the actual schema in CONTRACT.md and the file itself:





The file matches the contract schema exactly — my check script just used wrong key guesses. Re-running the reconciliation with the real field names:





Revisão pré-entrega concluída. Recalculei toda a aritmética em Python, conferi cada afirmação jurídica contra os arquivos da `library/` e validei o JSON contra o schema do contrato. **Nenhum total, delta ou classificação mudou** — os problemas encontrados eram de autoridade não suportada, precisão e consistência de redação.

## O que passou na auditoria sem correção
- **Aritmética fecha integralmente**: DAS 738.000 (17,5714% efetiva); Simples 916.500 · Presumido 1.079.620 (Δ +163.120) · Real 1.080.790 (Δ +164.290); PIS/COFINS 388.500 − 83.250; deltas do Anexo A (+20,6 / +1,2 / +118,2 mil); taxas de 25,71%/25,73%; datas 30/01/2026 (sáb 31/01) e 29/01/2027 (dom 31/01) verificadas.
- **`comparativo.json`**: chaves idênticas ao schema do contrato, todos os totais reconciliam — intocado.

## Correções aplicadas (`memorando.md`, 12 edições)

**Autoridade não suportada — 3 fixes:**
1. **§1, Fator R**: removeu "(≥ 28% → Anexo III)" — o limiar de 28% **não existe em nenhum arquivo da library**. O Anexo III agora é usado como fato documentado no balancete ("Fator R ≈ 31%"), e o limiar está rotulado *não verificado*.
2. **§5 e P1**: "encargos/FGTS não são base de CPP" era presented como fato — a library só diz "sobre a folha" **sem definir a base**. Relotulado *não verificado*; a premissa adotada (CPP sobre os 1,3 mi agregados) é agora explicitamente a leitura literal da fonte.
3. **§6, passo 2**: a regra residual "Real de ofício se não houver opção pelo Presumido" não consta da library — rotulada *não verificado* de forma destacada (antes a ressalva cobria só "a regra para 2026").

**Erro numérico — 1 fix:**
4. **§5, break-even**: base corrigida de "~R$ 715 mil" para **R$ 717.429 (~717,4 mil)** com CPP exato de **R$ 200.880** (−45% dos 1,3 mi); cenário de 904 mil rotulado *ilustrativo*.

**Consistência — 4 fixes:**
5. **TL;DR nº 1 e §6 passo 1**: agora referenciam a leitura alternativa dez/2026 (janela até 29/01/2027, Q6/Anexo A.1) — antes só o Anexo A carregava a dupla leitura.
6. **R4, nota de timing nova**: o ano em que o RBT12 cruzou os 3,6 mi não está nos documentos; se foi 2024, ISS/ICMS já estariam fora do DAS desde 01/01/2025. **Totais de 2026 não mudam em nenhuma leitura** — é questão de conformidade pretérita, somada à revisão R1.
7. **Anexo A.1**: linha que ainda pedia "confirmar a que dezembro (Q6)" atualizada — Q6 foi encerrada na rodada 4 como desconhecido definitivo.
8. Erro meu da própria revisão (palavra "likwise" perdida numa frase em português) corrigido.

**Precisão — 3 fixes:**
9. **§3/§4**: adicional de IRPJ agora nota que é apurado por trimestre (R$ 60 mil/trimestre; 4 trimestres uniformes ≡ 240 mil/ano, mesmo resultado).
10. **§1**: redação ambígua da linha de compras do CSV ("todos 'não' destacam ST" → "coluna ST destacado = 'não' nos três").

**`STATUS.md`**: parágrafo final registrando a auditoria e as correções; status permanece **COMPLETE WITH OPEN ITEMS** (os 5 desconhecidos definitivos + Q6 inalterados).

O que muda na substância para o sócio: nada na recomendação (permanecer no Simples, mudança em dezembro impossível, prazo 30/01/2026 com variante 29/01/2027), mas duas alegações que antes soavam como direito certo passaram a estar corretamente rotuladas como não verificáveis nesta biblioteca — e um novo item de conformidade (ano real do estouro do sublimite) foi adicionado à revisão sugerida de 5 anos.