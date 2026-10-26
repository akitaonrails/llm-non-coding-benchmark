O cliente respondeu dois pontos e esgotou as informações. Vou incorporar os fatos novos, refazer os números e avançar para as Sessões 2 e 3.

Fato novo importante: a linha de separação de pedidos (máquinas do Beta) é essencial. Vou corrigir os arquivos da Sessão 1 — inclusive um erro meu na Sessão 1 sobre o ganho contábil — e produzir as Sessões 2 e 3.

Agora as Sessões 2 e 3. Começo pela análise cláusula a cláusula:

Números fechados e salvos. Agora o item 5 (JSON do efeito tributário) e o arquivo de sensibilidade:

Agora atualizo a análise do plano com os fatos da 3ª rodada (Beta: garantias reais, aval, vencido desde 03/2025):

Descoberta crítica nos cenários. Reescrevo o §6.3 com a tabela correta (o prazo do CCB não muda o buraco de 10 anos, só a data em que o caixa acaba):

§6.3 corrigido. Agora reviso a coerência das seções seguintes (§6.1–6.2, §8, §9):

Sessão 2 fechada. Antes da Sessão 3, confirmo o schema exigido pelo contrato:

Autoridades confirmadas. Calculando os números exatos que entram nas peças da Sessão 3:

Agora o arquivo de lançamentos — gero por script para garantir JSON válido e débitos = créditos em cada lançamento:

Now I'll rewrite `QUESTIONS.md` with the canonical 1–22 numbering used by all three sessions.

The Via B row in the S3 comparison table doesn't reproduce — let me recompute it properly.

All table figures reproduce. Now the final verification pass.

The Via B row in the S3 comparison table doesn't reproduce — let me recompute it properly.

All table figures reproduce. Now the final verification pass.

As três sessões estão fechadas e auditadas. Status final: **COMPLETE WITH OPEN ITEMS** (registrado em `deliverable/STATUS.md`).

## Entregáveis (7, conforme o `CONTRACT.md`)

| Sessão | Arquivo | Conteúdo |
|---|---|---|
| 1 | `sessao1/resposta_diretor.md` | Não ao pagamento fora do plano (art. 49 + art. 172 + art. 64 + convolação); Não à União no plano (CTN 187, art. 68, art. 6º §7º-B); Não à trava de 30% (art. 50-A, II) |
| 1 | `sessao1/classificacao_creditos.json` | 7 credores, 13.540.000,00, esquema do contrato validado, confere com `relacao_credores.csv` |
| 1 | `sessao1/demonstrativo_mensal_aj.md` | Contas mensais do art. 52, IV: caixa, pós-pedido, concursais, UPI |
| 2 | `sessao2/analise_plano.md` | Cláusula a cláusula + teste de viabilidade: o caixa de 840.000 acaba entre o mês 3 e o mês 12 |
| 2 | `sessao2/efeito_tributario_desagio.json` | 7 chaves do esquema + sensibilidade em arquivo irmão |
| 3 | `sessao3/lancamentos_novacao.json` | L1–L9 (todos D == C), 6 itens não lançáveis, 6 reconciliações abertas; gerado por `workspace/documents/gen_lancamentos_sessao3.py` |
| 3 | `sessao3/passivo_fiscal_solucao.md` | Vias A/B/C da Lei 10.522/2002 com aritmética e sequência recomendada |

## Números que sustentam tudo

- Base do deságio 6.470.000 → passivo nominal 2.588.000 (120 × 21.566,67); VP a 1,5% a.m. = **837.295,77** → ganho **5.632.704,23**; teste dos 10% = **87,1%** → novação.
- Trabalhistas isoladas: 4,60% / 8,90% → **não** passam no teste dos 10% → sem ganho autônomo (L2).
- Deságios fantasmas (Beta 1.240.000 + União 1.350.000 = **2.590.000**) → **não lançar**.
- IRPJ/CSLL corrente sobre a base prudente (nominal 3.882.000 × 34% parâmetro) = **1.319.880**; DTL **595.239,44**.
- Federal: Via A **22.500/mês**; Via C (transação, até 70%) **6.750/mês** — economia de **1.890.000**. A transação legal dá mais desconto que a cláusula ilegal do plano.
- Déficit de 120 meses por via (reproduzi a tabela em Python, fechou): A 5.130.400 · B sem prejuízo 5.130.400 · B com prejuízo 4.320.400 · C 3.240.400 · C 50% 3.780.400.

## Itens abertos (falta de dado, não erro de análise)

Gaps deixados em aberto de propósito: 4.910.000 de desembolsos pós-pedido não explicados; 1.170.000 sem classificação pré/pós; 630.400 de gap só com o plano; **3.730.400 descobertos** servindo o CCB do Beta; valor contábil do galpão (L9 sem importe); despesas da recuperação e débitos estaduais/municipais. Registro canônico em `deliverable/QUESTIONS.md` (nº 1–22) e premissas P1–P11. Tudo que parece direito mas não está em `library/` está marcado **NÃO VERIFICADO** (inclusive a sede legal da trava de 30% fora dos dispositivos nomeados pelo art. 50-A, II) e nada disso baseia conclusão ou lançamento.

Nesta última rodada ainda corrigi três coisas de consistência: uma referência cruzada errada em `STATUS.md` (§5 → §4 da tabela comparativa), uma linha de cenários do CCB desatualizada em `workspace/documents/calculos_sessao2.txt` (os números 36.130.400/20.630.400/15.463.733 não reproduziam; agora consta 8.230.400 de esforço e 3.730.400 de gap em qualquer prazo, igual à tabela do §6.3 do `analise_plano.md`), e acrescentei ao mesmo arquivo a memória de cálculo do déficit por via federal que a tabela da S3 cita.

## O que só o cliente pode decidir agora

1. **Tirar a União do plano** (cláusula 4ª) e aderir a parcelamento/transação **antes da assembleia**, para obter a CND-E (art. 57 da LRF; art. 191-A do CTN).
2. **Renegociar o CCB do Beta por acordo**, com carência longa, protegendo a linha de separação de pedidos — não brigar com o fiduciário.
3. **Não pagar o sinal de 925.000 à Norte** (110,1% do caixa; leva a afastamento dos administradores e convolação) e levar o risco de desabastecimento ao juízo e à administradora judicial.
4. **Resolver galpão × linha de separação** antes de oferecer a venda no plano: se for o mesmo imóvel locado onde a operação roda, a fonte de recursos destrói a operação.

Se vier qualquer dado faltante (nº 1, 8, 9, 16, 17, 21, 22), basta rodar `python3 workspace/documents/gen_lancamentos_sessao3.py` — o JSON é regenerado a partir dele — e atualizar as tabelas afetadas de S2/S3.