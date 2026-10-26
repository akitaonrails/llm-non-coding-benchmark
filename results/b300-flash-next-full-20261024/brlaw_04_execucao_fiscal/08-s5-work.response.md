

A proposta do S5 traz números concretos que preciso reconciliar com o JSON atual (cotações 1,2%/2,5% + 30%, SELIC 3,9% até 30/11/2026, edital vigente). Vou conferir as fontes da biblioteca antes de regravar:





Fontes confirmadas na biblioteca (cobertura +30% — Portaria PGFN 164/2014 art. 3º; faixas típicas; transação 65%/70% limitadas ao principal). A proposta da Sessão 5 traz dois dados que o JSON anterior tratava como indisponíveis — **SELIC acumulada 10/07→30/11/2026 = 3,9%** e **cotações reais (seguro 1,2%; fiança 2,5%)**. Vou refazer o `garantia.json` com o valor efetivamente intimado.

Arithmetic first, all verifiable:

- **Remanescente atualizado:** 591.000 × 1,039 = **614.049,00** (591.000 × 0,039 = 23.049)
- **Cobertura (+30%):** 614.049 × 1,3 = **798.263,70** (614.049 × 0,3 = 184.214,70)
- **Seguro 1,2%:** 798.263,70 × 0,012 = **9.579,16** | **Fiança 2,5%:** 798.263,70 × 0,025 = **19.956,59** (diferença 10.377,43 a.a.; ambas as cotações caem nas faixas da biblioteca — seguro 0,8–1,5%: 6.386,11–11.973,96; fiança 2–3%: 15.965,27–23.947,91 ✔)
- **Transação (base atualizada):** multa 239.479,11 (230.490×1,039) + juros 55.264,41 (53.190×1,039) = 294.743,52; 65% = **191.583,29** ≤ principal atualizado 319.305,48 (307.320×1,039 — limite não vincula); pós-desconto **422.465,71**; 70% (se ME/EPP) = 206.320,46 → 407.728,54. Soma-confira: 319.305,48+239.479,11+55.264,41 = 614.049,00 ✔
- **Fallback sem exceção:** 1.100.000 × 1,039 = 1.142.900; ×1,3 = 1.485.770; seguro 1,2% = 17.829,24; gap de garantia = 528.851 ✔





Schema e aritmética validados. Agora atualizo os ledgers — primeiro releio as linhas exatas a editar:





Sessão 5 concluída — `deliverable/sessao5/garantia.json` regravado com os dados do próprio acervo (a proposta trazia a SELIC e as cotações que a versão anterior tratava como indisponíveis), validado contra o schema do contrato e com a aritmética conferida. STATUS e QUESTIONS atualizados.

## Os valores (toda a conta demonstrada)

**Base: o juízo intimou a garantir o "remanescente atualizado"** — R$ 591.000 da CDA (1T+2T/2021, após a decadência dos 509.000 de 2020), atualizados pela SELIC de 10/07→30/11/2026 informada na proposta (3,9%):

| Item | Conta | Valor |
|---|---|---|
| **Remanescente atualizado** | 591.000 × 1,039 | **R$ 614.049,00** |
| **Cobertura obrigatória** (débito + 30% — Portaria PGFN 164/2014 art. 3º) | 614.049 × 1,3 | **R$ 798.263,70** |
| **Seguro-garantia** (cotação 1,2% a.a.) | 798.263,70 × 0,012 | **R$ 9.579,16/ano** |
| **Fiança bancária** (cotação 2,5% a.a.) | 798.263,70 × 0,025 | **R$ 19.956,59/ano** |
| **Transação — desconto-teto 65%** sobre multa+juros atualizados (239.479,11 + 55.264,41 = 294.743,52) | × 0,65 | **R$ 191.583,29** |
| **Transação — valor pós-desconto** | 614.049 − 191.583,29 | **R$ 422.465,71** |

Conferências: componentes atualizados fecham exatos (319.305,48 + 239.479,11 + 55.264,41 = 614.049 ✔); o desconto teto fica abaixo do limite do principal (191.583,29 ≤ 319.305,48 — limite não vincula); as cotações da proposta caem dentro das faixas típicas da biblioteca (seguro 0,8–1,5%; fiança 2–3%); se ME/EPP se confirmar, 70% → desconto 206.320,46, pós 407.728,54.

## Recomendação

**1. Garantir já, com seguro-garantia.** A intimação (LEF art. 9º) dá dois caminhos — garantia ou comprovação de transação — e os embargos só abrem com a garantia feita (30 dias contados dela; sem garantia, inadmissíveis — LEF 16 e §1º). Entre as cotações reais, o seguro custa **10.377,43/ano menos** que a fiança e não consome caixa; depósito de 614.049 em dinheiro está descartado (inviabiliza a operação); penhora de 5% do faturamento é medida excepcional e, sem o faturamento mensal (dado que não temos), não dá nem para calcular em quantos meses cobriria o débito — serve de complementação, não de rota principal. Ressalva honesta: se a seguradora exigir contragarantia real de monta equivalente, a vantagem some — prática de mercado não verificável na biblioteca, confirmar antes de fechar.

**2. Transação: não agora.** Três razões concretas: (a) **débito decaído não se transaciona** — e adesão implica **confissão irrevogável + desistência das defesas**; correr para transar antes da decisão da exceção seria misturar os 509.000 mortos na confissão; (b) os **DARFs de 145.000** (61k + 84k) ainda não foram conferidos na memória de cálculo — transar antes pode ser confessar valor inflado; (c) o desconto **efetivo** depende de CAPAG e classificação do crédito (dados indisponíveis) — os 191.583,29 são **teto de regra, não oferta**. Feito isso, transar a base depurada em até 120 meses é opção legítima, pois o mérito de 2021 (origem dos depósitos) é nosso ponto fraco.

**3. O que recalcula estes números** (já mapeado no JSON): CDA substitutiva ainda não junta (requerimento 1); eventual **aditamento escrito** pós-audiência elevando a multa ao §1º (o "sonegação" oral do procurador, hoje, não muda nenhum valor — o título está no art. 44, I, 75%); SELIC na data real do depósito (os 3,9% são **projeção até 30/11/2026**, data futura — a conta final sai da contadoria e os custos escalam na proporção); e, se a exceção for rejeitada, o fallback: 1.100.000 × 1,039 × 1,3 = **1.485.770** de cobertura, seguro 17.829,24 — gap de garantia de **528.851** frente ao ora intimado.

**Decisão que falta do cliente:** a escolha real está entre **~9,6 mil e ~20 mil por ano** — a tolerância de custo dos sócios (já pedida na carta ao Bruno, §4.1) e autorização escrita apenas para **consulta** de transação (sem adesão).