A Sessão 3 já está escrita; vou verificar a integridade (regenerar pelo script-fonte e validar D == C) e sincronizar com a rodada mais recente antes de fechar o fechamento:

Sessão 3 verificada e fechada. Os dois entregáveis estão em `deliverable/sessao3/`, o JSON foi regenerado pela fonte única (`gen_lancamentos_sessao3.py`) e **todos os lançamentos fecham em débito == crédito**. Resumo consolidado:

## 1. Novação — `lancamentos_novacao.json`

| # | Lançamento | Valor | Tratamento |
|---|---|---|---|
| **L1** | Novação das classes III (6.050.000,00) + IV (420.000,00): baixa do passivo original e reconhecimento do novo a **valor presente** (120 × 21.566,67, carência de 24 meses, 1,5% a.m. — P9) | 6.470.000,00 baixado → **PV 837.295,77** | **LANÇAR** — teste dos 10%: 60,00% >> 10%, novação contábil configurada; ganho de renegociação **5.632.704,23** |
| **L2** | Classe I trabalhista (960.000,00): **só reclassificação** de prazo, sem baixa | 960.000,00 | **LANÇAR** — teste dos 10% **não atendido** (4,60% a 0,5%; 8,90% a 1,0% a.m.); não há redução de principal; nenhum ganho nessa classe |
| **L3** | Banco Beta (fiduciária, 3.100.000,00): **nenhuma novação** | 3.100.000,00 | Passivo permanece integral — art. 49, §3º: fiduciário não se submete à RJ |
| **L4** | União (2.700.000,00): reclassificado como **parcelamento federal** (Lei 10.522, art. 10-A) | 2.700.000,00 | **LANÇAR** a reclassificação; juros NÃO VERIFICADO (P10) |
| **L5** | Ganho de transação tributária (art. 10-C) | 1.890.000,00 | **MEMORANDO — não lançar** até a transação ser formalizada e o desconto concedido |
| **L6** | Extraconcursais pós-pedido da Norte (210.000,00 + 100.000,00) | 310.000,00 | **LANÇAR** — ficam fora da novação |
| **L7** | Provisão IRPJ/CSLL sobre o ganho (base prudencial nominal 3.882.000,00 × 34% — P7 NÃO VERIFICADO) | 1.319.880,00 | **LANÇAR** |
| **L8** | Tributo diferido passivo (diferença temporária PV × 34%) | 595.239,44 | **LANÇAR** |
| **L9** | Galpão para venda (reclassificação IFRS 5-like) | valor contábil **não informado** (Q21) | Reclassificação devida, importe **em aberto** |

**Passivo oneroso pós-homologação: 9.822.415,21** (PV 837.295,77 + trabalhistas 960.000 + Beta 3.100.000 + Norte 310.000 + federal 2.700.000 + IRPJ 1.319.880 + DTL 595.239,44).

## 2. O que NÃO lançar (7 itens)

1. Deságio fiduciário prometido (40% de 3.100.000) = **1.240.000,00** — ganho fantasma;
2. Deságio da União prometido (50% de 2.700.000) = **1.350.000,00** — inexistente;
3. PIS/COFINS sobre o ganho — **zero** (art. 50-A, I exclui da base);
4. Ganho sobre trabalhistas (124.130,09) — teste dos 10% não atendido;
5. DTA por prejuízo fiscal — saldo não confirmado (Q8);
6. Estorno de despesas do plano — valores não informados (Q22);
7. **"Adiantamento de fornecimento futuro" de 925.000,00 à Norte** (pedido da rodada 5) — incluído agora explicitamente no livro: sem contrato nem cronograma, é pagamento disfarçado de crédito quirografário pré-pedido fora do plano (art. 49; arts. 64 e 172 como sanção; o livro vai ao juízo mensalmente por 120 meses — art. 52, IV). A recusa está documentada em `sessao1/resposta_diretor.md` §8.

**Total de ganhos fantasmas bloqueados: 2.590.000,00.**

## 3. Reconciliações abertas (6, sem forçar fechamento)

Gap de funding do plano 630.400,00 | déficit servindo o CCB 3.730.400,00 (caixa esgota mês 3–12) | sinal Norte 925.000,00 (110,1% do caixa) | extraconcursais não classificados 1.170.000,00 | efeito da premissa P1 sobre L1 (210.000,00) | semanas 5–13 do fluxo ausentes.

## 4. Passivo fiscal — `passivo_fiscal_solucao.md`

A cláusula 4ª da minuta (deságio de 50% via plano) é **ilegal** — crédito tributário não entra em recuperação judicial (CTN art. 187; LRF art. 68). A rota legal:

- **Via A (piso): parcelamento ordinário — Lei 10.522/2002, art. 10-A**: 2.700.000,00 em até 120 meses = **22.500,00/mês**, viabiliza a CND necessária à homologação (LRF art. 57; CTN art. 191-A);
- **Via C (simultânea, recomendada): transação — art. 10-C**: desconto de até 70% → **6.750,00/mês**, economia nominal **1.890.000,00** vs. Via A;
- **Via B (art. 10-A, §1º-B, uso de prejuízo fiscal): só se o prejuízo for confirmado** (Q8) — sem ele seria a pior opção (32.142,86/mês).

O cap de 30% do art. 50-A, II **não** se aplica ao federal (os dispositivos 50-A só regem créditos concursais). Os 1.890.000,00 da Via C entram como memo L5 até a transação formalizar.

**Status: COMPLETE WITH OPEN ITEMS** — itens dependentes das perguntas 8, 9, 11, 14–19, 21–23; STATUS.md atualizado (7 itens não lançáveis).