I'll do a systematic audit: re-read the entire library (the only citable authority), then every number and citation in the deliverables, then recompute all arithmetic.

Continuing the audit — re-reading the library formulas and the rest of `parecer.md` to verify each number and citation:

Saída truncada — executando novamente uma busca mais estreita para confirmar todas as ocorrências.

Todos os locais confirmados. Lendo as linhas exatas a serem corrigidas para edições precisas:

Aplicando correções. Primeiro, a derivação do teto — lendo a linha exata da sentença sobre horas extras:

Todas as linhas-alvo confirmadas. Aplicando as 7 correções em `parecer.md`:

Agora as duas correções no `parecer.json`:

Re-verification: JSON validity + schema + arithmetic, and residual grep for strings that have been deleted:

Grep limpo — nenhuma string residual. Verificação do JSON atingiu nomes de chave incorretos; inspecionando a estrutura real de `exposicao`:

Nomes das chaves localizados (`multa_40`, `total`). Executando novamente a validação completa:

Auditoria concluída — todas as verificações passam. Erros encontrados e corrigidos:

**Erros numéricos (2) — tabela de cenários §6.1, linha R$ 15.000 (ambas em `parecer.md:129`)**
1. Célula INSS: **293.970 → 293.475** (0,28 × 1.048.125; a linha só fecha em 606.990 com o valor corrigido).
2. Crédito ao reclamante: **313.020 → 313.515** (606.990 − 293.475 = 376.218 × 15/18).

**Citação não verificada (1) — `parecer.md:66` §4.1(c)**
3. A frase atribuída à biblioteca entre aspas, «congela o processo; não zera a exposição», **não existe na biblioteca**. Substituída pela redação verbatim real: "a exposição não desaparece — fica em aberto, com juros e correção correndo" (stf_tema_1389_pejotizacao.md).

**Erros de atribuição de fonte (2 no MD, 1 no JSON)**
4. `parecer.md:73` §4.1(d): "ônus de provar a validade do contrato… (Súmula 212/TST)" — a Súmula 212 trata do ônus do **término**. Corrigido: autonomia → art. 818 CLT; término → Súmula 212.
5. `parecer.md:24` §2: mesmo problema + arquivamento errado (art. 818 está em `clt_requisitos_vinculo.md`, não `tst_sumulas_ojs.md`). Corrigido e desdobrado.
6. `parecer.json` fundamentos[4]: mesma cisão 818/212 + typo "a afastamento" → "o afastamento"; fundamentos[9]: refs de arquivo erradas "cf_stf_tema_1389 + cf_art7_xxix" → "stf_tema_1389_pejotizacao.md + cf_art7_xxix_prescricao.md".

**Referência dangling (1)**
7. `parecer.md:73`: "(§6.2)" → "(§6)" (a seção §6.2 não existe).

**Divulgações adicionadas (4)**
8. §6 linha INSS: a base 1.257.750 **exclui aviso-prévio indenizado** (biblioteca não especifica; incluí-lo = +R$ 8.568).
9. §6 linha 13º: nov/2021 contado por proporcionalidade (1,5/12); na regra estrita de avos (mês ≥15 dias) seria 2/12, +R$ 750 — mantida a base de 58,5 meses.
10. §6 teto "R$ 0,9–1,1 mi": derivação agora explícita (728.388 + ~178.000 HE + ~27–44.000 reflexos + honorários 36–109.000 + multas ~18.000+).
11. Tabela de custo de carregar a suspensão §4.1(c): explicitada a capitalização anual implícita (24m = base×[(1+i)²−1]) — os valores 152.961/234.905 estão corretos nesse regime.

**Reconciliado sem alteração (verificado nesta auditoria)**
- Todas as demais células das linhas 18k e 12k da tabela de cenários; totais 728.388 / 485.592 / 606.990; provisão 655.549 (0,7/0,3); ancora do acordo 338.596; faixa [270.000, 480.000]; delta de extinção −70.848/−47.232; HE 18.225/177.694/118.463; prescrição 25,5/58,5; aviso 51 dias (30+3×7 anos completos — confere com a fórmula da biblioteca).
- Citações verbatim conferidas contra a biblioteca: teses dos Temas 725/1.389, art. 442-B ("desde que ausente a subordinação"), presunção da remuneração-base, INSS ≈28%, fórmula do aviso, cancelamentos da Súmula 256/OJ 191, multas 477/467 "discutíveis" + 791-A 5–15%, Lei 14.905/2024, ARE 709.212.
- `parecer.json`: JSON válido, conjunto de chaves = schema plano do CONTRACT, verbas somam 728.388, FGTS/multa/INSS reproduzíveis pelas taxas da biblioteca.

Grep final por "293.970", "313.020", "congela o processo", "cf_stf_tema_1389", "a afastamento", "§6.2": **zero resíduos** nos quatro entregáveis. `QUESTIONS.md` e `STATUS.md` permaneceram inalterados (sem novos desconhecidos — os dois últimos itens são premissas divulgadas, não lacunas do cliente).