

Good discipline before delivery. I'll do a systematic pass: (1) re-read all four deliverables in full, (2) re-read the entire library and verify every citation against the actual source text, (3) re-run all arithmetic from scratch, (4) reconcile cross-references and figures across files.






Library and documents are now fully re-read. Several real problems are already visible (a fabricated quote, a fabricated "R$ 850 mil" fact, a divergent-hours arithmetic that doesn't sum). Now the remaining deliverables and the contract PDF:






The contract PDF didn't yield its text layer on first pass; I need the full JSON/STATUS/QUESTIONS and the remaining documents. Reading everything now:







Now the source documents and the full library texts, for citation and arithmetic verification:







Now the library files to verify the two suspect quotations and formula sources:






Library texts confirm two citation problems. Before fixing, I must re-verify one arithmetic claim myself with Python — and read the remaining files:






Final verification pass — JSON parse, arithmetic sums, and residue greps:





All sums reconcile exactly with the text. Now residue greps:





All edits are in place and everything reconciles. Let me check whether `STATUS.md` should record this review round:





`STATUS.md` is consistent. I'll record the review round there (the file documents each round newest-first), then deliver the change list:





Reconhecimento completo. Re-executei todas as verificações em Python e reli os quatro entregáveis contra os documentos e a biblioteca. Aqui está o que descobri e o que mudei.

## O que estava errado e foi corrigido

**Autoridade/qualidade de fonte inventada (os dois erros mais graves):**
1. **`parecer.md` §7.1** — a notificação extrajudicial havia sido descrita como trazendo "planilha de R$ 850 mil". Nenhum documento indica qualquer valor. Substituí pelo teor real: notificação anunciando reclamação com reconhecimento de vínculo desde 01/10/2019 "com todas as verbas" (e disse explicitamente que a notificação não indica valor).
2. **§4.1.3** — uma citação em itálico atribuída ao arquivo da biblioteca do Tema 1.389 ("qualquer informação que afirme tese definitiva…") **não existe nesse arquivo**. Substituí pela regra metodológica do próprio parecer, sem fingir fonte.
3. **§4.1.2** — a citação da tese do Tema 725 estava truncada; restaurei o "no caso concreto," que consta do arquivo.
4. **§7.1** — a fórmula IPCA + SELIC−IPCA foi creditada a dois arquivos; `verbas_e_calculo.md` não a contém. Fonte agora restrita a `stf_tema_1389_pejotizacao.md`.
5. **§5** — as datas de vencimento 20/12/2021 e 29/09/2022 vêm de regra geral fora da biblioteca; agora marcadas **[não verificado]** (a sensibilidade de ≈ +R$ 49 mil em si confere: 44.500 × 1,112).
6. **§4.1.3** — "e-mails de RH" → "aprovação de ausência pelo RH" (há uma aprovação de ausência, não pluralidade de e-mails).

**Fato do arquivo distorcido:**
7. **§2** — eu havia escrito "registro de ponto em poder da reclamante". Os registros estão no arquivo da **própria empresa** — corrigido (o que inclusive afasta a presunção de registro ausente, mantendo as 135 h como prova contra a empresa).

**Aritmética de apresentação (valores finais não mudaram):**
8. Taxas por hora com precisão que reproduce os totais: 81,8182 / 122,7273 (com 122,73, 135 × taxa = 16.568,55, não 16.568,18); idem 81,8182 no cenário 12k.
9. Reflexo FGTS+40% sobre HE comprovadas: 2.210 → **2.216** (total de reflexos ≈ 10.077, como já afirmado).
10. **§6.1** — a linha de mix probabilístico só exibia HE ponderada no mix 75/25; agora mostra os dois completos: **648.045 (85/15)** e **625.306 (75/25)**, alinhados ao §7.
11. **`parecer.json` → `horas_extras`** — "sugere até ~R$ 19.600 extras **não registrados**" era enganoso: a média diária implica ~160 h no semestre (≈ R$ 19.612), dos quais só ~24,8 h (≈ R$ 3.044) estão **acima** das 135 h registradas. Reescrito.

**Erros de revisão/typos:** referência "(§5)" para a estimativa (é §6), "(§6)" para o acordo (é §8), "certainos" → "certos", "a distance" → "à distância".

## O que suspeitei, re-verifiquei e **não** mudei
- A "divergência planilha ~160 h × 135 h registradas" parecia erro aritmético meu de rodada. Re-derivei em Python: (9,1−8)×21 + (9,3−8)×19 + (9,0−8)×21 + (9,4−8)×20 + (9,2−8)×21 + (9,8−8)×21 = **159,8 h ≈ 160 h, +18,4% sobre 135 h** — o texto original estava correto (a "suspeita" é que tinha um termo a menos). Item permanece aberto como divergência legítima.
- Todos os totais re-conferidos: 665.584 · 682.152 · 160.159,09 · 943.580,69 · 443.722,67 · tabela de espera 102.322,80/219.994,02/355.315,92. `parecer.json` parseia e soma.
- Nenhuma súmula/OJ cancelada é invocada (as duas ocorrências de "Súmula 256/OJ 191" são apenas a nota de que **não** se usa).

**Nenhum número do caso central mudou**: probabilidade 70–80%, exposição R$ 665.584, provisão R$ 682.152, acordo R$ 500–700 mil. `STATUS.md` agora documenta a rodada de revisão; veredito segue **COMPLETE WITH OPEN ITEMS**, com apenas D-1 (decisão de acordo antes de 16/11/2026) pendente.