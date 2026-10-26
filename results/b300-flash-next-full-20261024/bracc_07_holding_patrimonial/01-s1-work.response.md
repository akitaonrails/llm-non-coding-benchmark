

Now let me verify the data and run the calculations.





Data reconciles with the client file. Now let me write the deliverables.





Now the numbers file, questions copy, and status.





The CSV column names differ from what I assumed — the per-property table I wrote needs to be rebuilt from the actual file. Let me verify the real rows and re-check every quoted passage.





The palestra summary is 6 lines — several "quotes" I attributed to it aren't in the file. I need to re-read every source verbatim and rewrite.





I have to start over: the real source files are a few lines each, and my drafts cited material that isn't in them. Recomputing everything strictly from the actual files.





Excellent — the CSV itself settles it: the rented properties sum to **14,430,000 / 4,220,000 / 84,900**, which matches `familia.md` exactly (my mental arithmetic was wrong, the script was right). Only the non-rented filter label was broken (`uso proprio/ferias`).





The per-property allocation had a units bug (monthly rent ÷ annual revenue). And I must re-read the exact IRRF/PF rule text before finalizing.





Now everything reconciles — the CSV totals **do** match `familia.md` exactly (14.430.000 locados + 2.000.000 próprios = 16.430.000; 4.220.000 + 500.000 = 4.720.000; aluguel 84.900). My earlier "divergence" was bad mental arithmetic. Let me lock in a clean computation.





Corrigindo um bug de dupla multiplicação no IRRF:





All figures now reconcile. Before writing deliverables, re-reading the exact source texts for verbatim quotes and the contract schema:







Key correction confirmed: os filhos são **Ricardo, Paula e Marcos** (não "Lucas/João" — esses nomes não existem nos documentos), e não há nenhuma doação de 25% nos fatos. Relendo as fontes citáveis para citações exatas:






Todas as fontes confirmadas. Escrevendo os entregáveis agora, começando por `numeros.json`:





Agora o parecer, parte 1 (dados + afirmações 1–3):





Confirmado: teto = 126,600; diferença em disputa = 306,300. Corrigindo o parecer e o JSON com esse significado correto.





Corrigindo os problemas de consistência e completando o parecer com as seções 4, 5, estrutura e limites:





JSON validado. Relendo o CONTRACT.md para escrever os arquivos finais conforme as especificações exatas:





Corrigindo dois pontos de aritmética no parecer (percentual da doação limitada à disponível e o cenário de usufruto no ITCMD).





O calc3.py em disco está quebrado (referencia `EXC_LUCAS` que não existe mais) e ainda tem o resíduo de 25%. Vou reescrevê-lo limpo.





Caminho incorreto — corrigindo para `/work/workspace/...`.






Últimos dois ajustes de fidelidade literal na linha 73 ("redutível" → "nula", como diz a library).






Entrega finalizada e autoconsistente. O que mudou nesta última revisão — motivada por verificar o texto literal de `cc_legitima_doacao.md` na library:

**Correção substantiva (Alegação 5).** A library **não contém nada** sobre impenhorabilidade oponible a credores, pauliana ou responsabilidade do sócio — o único ponto que ela toca sobre credores funciona *contra* a doadora (art. 549: doação que excede a disponível é **nula** no excedente). Então a parte "protege dos credores" não é "FALSA": é **sem fonte na library (não verificado)**. Onde a library é literal, deixei o texto dela: "não podem ser opostas a terceiros" (sem justa causa, sobre a legítima). O art. 549 diz "nula", não "redutível" — corrigido no §4.

**Desenho sucessório fechado com números.** Como Helena não quer deixar quotas a Marcos, a doação de **só até a disponível** (370.600) deixaria ~5,16 mi de quotas no inventário e Marcos entraria na sociedade — rejeitada. O desenho correto é **doar todas as quotas** a Ricardo e Paula com usufruto: pela imputação da library (avanço de legítima imputa primeiro na quota do beneficiário, art. 544; só o que sobra sai da disponível, art. 549), o excedente é 8.253.333,33 ≤ disponível 9.265.000 (**folga de 1.011.666,67**), e a legítima de Marcos fica coberta fora da PJ (4,1 mi ≥ 3.088.333,33). ITCMD: 384.800 agora + 192.400 na extinção do usufruto. A folga é o amortecedor contra valorização até a colação — registrado como premissa, não como certeza.

**Conferências finais feitas:**
- `cc_legitima_doacao.md` relido linha a linha: as 5 afirmações do §4/§5 agora têm suporte literal cada uma; o que a library não diz virou pergunta nova (**Q18**) ou limite explícito;
- `calc3.py` reescrito limpo e reexecutado — reproduz todos os números do parecer e do `numeros.json` (folga 1.011.666,67, cenários 384.800/192.400/370.600, banda 12,17–14,53%);
- `numeros.json`: schema exato do contrato validado, sem chaves extras;
- grep anti‑artefato nos 5 arquivos: sem "pauliana/CC 158" como fonte, sem "55%", sem cenários antigos; os únicos "306.300" restantes são o uso correto (diferença em discussão sob o teto do Tema 796);
- `STATUS.md`, `QUESTIONS.md` (18 itens) e `PERGUNTAS.md` alinhados entre si e com o parecer.

**Resultado — cinco alegações:** ① FALSA (ITBI devido: 432.900 no cenário central; teto 126.600 se litígio Tema 796). ② FALSA aqui (carga real 12,17–15,07%, não "11,33%"; o número só fecha com ≥2 sócios recebendo pouco). ③ ALÍQUOTA SIM, BASE NÃO (4% sobre mercado, não contábil). ④ FALSA (legítima de Marcos intocável; mas dá para tirá-lo **da sociedade** doando tudo a R&P com a legítima dele paga fora da PJ). ⑤ DEPENDE no testamento (justa causa) e **sem fonte** na parte "credores" — não prometer blindagem. Situação: **COMPLETE WITH OPEN ITEMS** (5 pendências documentais, todas em `QUESTIONS.md`).