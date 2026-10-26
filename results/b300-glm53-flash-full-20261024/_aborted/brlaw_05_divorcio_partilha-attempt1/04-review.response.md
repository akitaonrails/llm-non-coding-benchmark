Full pre-delivery QA pass. First, re-reading the contract, the library files (the sole citable authority), and the source documents to verify every number and citation:

Correcting the path and reading everything needed for the QA pass in parallel:

 CONTRACT, index and sources verified. Now the library files (the actual content of the cited ones) and the deliverables:

Library content captured — key nuance: `cc_comunhao_parcial.md` defines 1.660, V as "frutos **dos bens** comuns ou dos particulares" (not "frutos do trabalho"), and it's the STJ file itself that bridges lucros reinvestidos → 1.660, V for quotas. Also casa Atibaia entry was 620.000 in the 2019 inventário (relevant to the reforma analysis). Also there's EREsp 1.623.858 and Súmula 358 in the index — I need to check that deliverables don't cite them with invented content (the file bodies don't explain them).

Now reading all six deliverables:

partilha.json e alimentos.json lidos — já veio algumas coisas para corrigir ("(aluéis)", "sugir", "Arithmetic:", "cliente não respondeu suficiente informação", e a alegação de que 30%/25% "praticamente se igualam" sem os brutos). Agora os arquivos restantes:

proposta_acordo.md read — found real issues: the "praticamente converge / se igualam" claim (line 52/67/93 — arithmetically false: 25%×39.000 = 9.750 vs 30%×39.000 = 11.700 on the same base), a weakened CC 1.660,V attribution for FGTS in §5-A (library ties FGTS to REsp incorporation, not 1.660,V), "contorno de zero", "despido de propósito", "(aluéis)"/"sugir" typos, "Arithmetic:" in partilha.json. Checking STATUS and the QUESTIONS/PERGUNTAS sync:

Retomando a rodada de correções de QA — preciso dos textos exatos de cada linha problemática para editá-los. Buscando todos em paralelo:

Exachs exact text captured. Now I need the remaining bits: line 57-60 of proposta (the "(cliente informou não ter essa informação)" smoothing), full QUESTIONS.md (to mirror the FGTS-de-Fernanda open item into STATUS), and the §5-A header context around line 74-75:

Todo exato capturado. Aplicando as correções agora — lote 1: partilha.json, alimentos.json, STATUS.md:

Batch 1 aplicado. Agora o lote 2 — proposta_acordo.md:

All edits in. Final validation pass — JSON parsing with arithmetic checks, mirror-file diff, and a sweep for any leftover garbled word or unsupported claim:

Code Mode não tem `shell` no catálogo — chamando a ferramenta shell diretamente:

Two things: the "match: False" flags are my check comparing the rows-only sum against the net TOTAL (debts live in the DIVIDAS row) — I'll verify the correct invariant — and one leftover "Arithmetic" in proposta_acordo.md line 19. Reading that section:

One leftover anglicism on line 19, and then the corrected invariant check:

Retomando a validação final após a última edição — verificação invariante corrigida (linhas + DÍVIDAS == TOTAL), nova varredura de erros e verificação de espelho:

Everything reconciled and the sweep is clean. Two last citation sanity checks — confirm `AgInt no AREsp`, `REsp 1.698.774/RS` and `REsp 1.332.808` have bodies in the library, and that INDEX-only authorities (EREsp 1.623.858, Súmula 358, CC 1.661) stay absent from deliverables:

所有引用均指向实际库文件（alimentos/stj 文件中为 AgInt/1.698.774/1.332.808），并且仅索引的权限未分配任何内容。最后确认一下 `STATUS` 标题：

QA pass concluído e validação final limpa. Status: **COMPLETE WITH OPEN ITEMS**, mantido em STATUS.md.

# Relatório final de QA — o que foi revisto e corrigido

## 1. Erros de texto / palavras truncadas (5 correções)

| Arquivo | Estava | Ficou |
|---|---|---|
| `partilha.json` | "(al**ué**is)" | "(aluguéis)" |
| `partilha.json` | "contraprestação **para não sugir** doação" | "contraprestação, para que não **surja** doação (ITCMD 4%)" |
| `proposta_acordo.md` §3 (tabela, recusa da casa) | "**Também é despido** de propósito tributário: sairia como excesso de meação…" | "Atribuir metade também **traria custo tributário**: seria excesso de meação → ITCMD 4% (se gratuito) ou ITBI 3% (se oneroso, sobre imóvel) na parte dela" |
| `proposta_acordo.md` §5 | "inegociável tecnicamente | inegável" — trocado por "mas é **inegável** que saiu dinheiro comum" |
| `STATUS.md` item 8 | "Saldos correntes de FGTS (140.000 informados; **sem correnteza confirmada**)" | "**FGTS de Marcelo:** saldo de 140.000 e depósitos de 2.400/mês — até quando persistem? (sem **extrato** confirmado)" |

## 2. Anglicismos (3)

- `partilha.json` TOTAL: "Arithmetic:" → "**Aritmética:**" (e a frase da dívida reescrita: "dívidas comuns = 360.000 (registradas como **−360.000** na linha DIVIDAS)" — antes dizia "+360.000", contrariando o sinal da linha).
- `proposta_acordo.md` §1, linha 19 (achado na re-varredura): "Arithmetic (executada em Python):" → "**Aritmética (executada em Python):**".
- `alimentos.json` PLR: "cliente não respondeu **suficiente informação**" → "dados insuficientes (cliente não informou hábito nem valor); mantida fora da base até informe".

## 3. Autoridade sem lastro na biblioteca (2 correções)

- `proposta_acordo.md` §5-A (FGTS): a justificativa citava **CC 1.660, V** para "depósitos incorporados" — mas a 1.660, V da biblioteca trata de frutos/lucros reinvestidos, não de FGTS. Reescrito com o que o arquivo `stj_fgts_quotas_previdencia.md` realmente suporta: depósitos na constância **integram o patrimônio comum e comunicam**, e o **REsp 1.399.199/RS** registra que o art. 1.659, VI **não afasta a partilha de valores já incorporados**, ainda que o saque fique diferido.
- `proposta_acordo.md` tabela §3: "PLR… (controvérsia **contra**)" → "(**incidência controvertida** — `alimentos_base_calculo.md`)"; e `alimentos.json` (i): "(descontos de IR e INSS **mencionados no resumo**)" → "(o resumo reporta valores líquidos; a **biblioteca define** líquido como rendimento após os descontos legais de IR e INSS)".

## 4. Alegação que não reconciliava (convergência numérica falsa) — eliminada em 4 pontos

A matemática real: sobre a mesma base líquida de 39.000, nossa 25% = **9.750/mês**; o 30% dela = **11.700/mês** (+1.950). Não há igualação, e 30% "do bruto" é incomputável sem contracheques. Corrigidos:

1. `proposta_acordo.md` §3 (linha 52): "25% ≈ o que a peça oposta alcança de 30% sobre líquidos puros — argumento de fechamento" → versão quantificada e honesta (9.750 vs 11.700; bruto incomputável; fechamento = base correta + teto da faixa + velocidade e certeza).
2. `proposta_acordo.md` §3 tabela (linha 67): "131.000/ano — **praticamente o mesmo valor** que a peça oposta alcançaria… o que esvazia a briga" → "A briga se resolve na base e na incidência (biblioteca), não na igualação de valor…".
3. `proposta_acordo.md` §7 (iv): removed "praticamente **converge**, o que encerra a briga"; "(≈ 131.000/ano)" → "= **131.000/ano**" (a conta é exata) + defesa reformulada (base lícheck líquidos / incidência fora / topo da faixa 15–30%).
4. `alimentos.json` fundamento (iii): "25% e a peça oposta **praticamente se igualam** em valor" → (iii) 25% alto e defensável pelo binômio; (iv) comparação numérica impossível sem contracheques; incentivo de fechamento = velocidade e certeza.

## 5. Registro e terminologia (3)

- `proposta_acordo.md` §3 (linha 58): "(cliente informou não ter essa informação)" → "(sem informe do cliente)".
- "convida **a prima** a persistir" (proposta §5-B) e "pretensão **da prima** persistida" (STATUS C) → "**da advogada da Fernanda**" (2×).
- `proposta_acordo.md` §5-B: "o conselho informal **compra, na melhor hipótese, contorno de zero**" → "**rende, na melhor hipótese, ganho líquido de zero**".

## 6. Pendência nova do turno 3 incorporada (1)

- `STATUS.md`: incluído o item 9 — "**FGTS de Fernanda:** há saldo vinculado em nome dela? … meação cruzada (REsp 1.399.199/RS) — pendência surgida da objeção do turno 3" (espelha a linha 24 de QUESTIONS.md). QUESTIONS/PERGUNTAS não mudaram neste passe, então o espelho permaneceu idêntico automaticamente.

## Validação final (tudo reconfirmando em Python + diff + grep)

- `partilha.json`: linhas (2.650.000 bruto / 1.325.000 meação) + DIVIDAS (−360.000 / −180.000) = TOTAL (**2.290.000 / 1.145.000 = TOTAL÷2**) ✓; soma geral 3.850.000 ✓. *(O "match: False" do meio do caminho era artefato da minha checagem — comparava a soma bruta das linhas com o TOTAL líquido; não era erro do arquivo.)*
- `alimentos.json`: 25% × 39.000 = **9.750/mês** ✓; 12×9.750 + 6.000 + 8.000 = **131.000/ano** ✓; pagamento 1.055.000 e Fernanda 1.205.000 continuam fechando ✓.
- `diff QUESTIONS.md PERGUNTAS.md` → idênticos ✓.
- Varredura de termos ("sugir", "Arithmetic", "se igualam", "converge", "contorno de zero", "despido", "inegociável", "correnteza", "a prima", "suficiente informação"…) → **limpa**.
- Auditoria de citações: toda autoridade citada tem corpo em arquivo da biblioteca (AgInt no AREsp / REsp 1.698.774/RS / REsp 1.332.808 confirmados nos tópicos); EREsp 1.623.858, Súmula 358 e CC 1.661 (só no INDEX) **não** recebem conteúdo atribuído em nenhum entregável.

Entregáveis prontos para a entrega em `workspace/deliverable/`, com as 9 pendências de informação documentadas em STATUS/QUESTIONS.