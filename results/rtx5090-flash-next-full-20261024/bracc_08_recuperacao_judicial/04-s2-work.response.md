Sessão 2 entregue em `deliverable/sessao2/` — `analise_plano.md` (cláusula a cláusula) e `efeito_tributario_desagio.json` (schema do contrato, cálculos validados em Python). Resumo:

## 1. Análise da minuta (`plano_minuta.md`) — 5 cláusulas: 2 ilegais, 1 condicionalmente ilegal, 2 legais

**Cláusula 1 — Trabalhistas: integral em até 18 meses → CONDITIONALMENTE ILEGAL.**
Art. 54: o plano **não pode prever prazo superior a 1 ano** para créditos trabalhistas vencidos até o pedido. O §2º admite até 2 anos somente com **garantias + aprovação da classe + integralidade**. A minuta só tem integralidade (✓ R$ 960.000); garantia não prevista, aprovação da classe I incerta. Recomendação: 12 meses (R$ 80.000/mês) — a economia dos 18 meses (R$ 53.333/mês, diferença de R$ 26.667) não vale o risco de impugnação.

**Cláusula 2 — Quirografários + ME/EPP: deságio 60%, 120 parcelas, carência 24 → LEGAL.**
Nenhum excerto da biblioteca veda deságio/alongamento dessas classes (o art. 50 não consta da biblioteca — estrutura completa não verificável, sinalizado). Fluxo sustenta: 6.470.000 × 40% = 2.588.000 ÷ 120 = **R$ 21.567/mês** pós-carência.

**Cláusula 3 — Fiduciários "sujeitos ao plano, deságio 40%" → ILEGAL/INEFICAZ contra o Beta.**
Art. 49, §3º: proprietário fiduciário **não se submete aos efeitos da RJ**; prevalece o direito de propriedade. O ganho de R$ 1.240.000 (40% × 3.1M) dessa cláusula **não se materializa** — e por isso ficou fora do cálculo tributário. A proteção real é temporária: durante a suspensão do art. 6º, §4º (180 dias, prorrogável) é **vedada a venda/retirada de bens de capital essenciais** — e o cliente confirmou que as máquinas são a linha de separação de pedidos. Corrição: excluir o Beta do plano, acordo bilateral lícito (extraconcursal não é favorecimento), e destinar o galpão (R$ 4,5 mi − R$ 3,1 mi = R$ 1,4 mi de sobra) à quitação **dentro da janela de suspensão**.

**Cláusula 4 — União "no plano, deságio 50%, 180 parcelas" → ILEGAL em três frentes.**
(i) CTN 187: crédito tributário não se sujeita a concurso/habilitação; (ii) art. 68: **não se sujeita ao plano**; (iii) art. 6º, §7º-B: execução fiscal **não se suspende** — a União penhora enquanto o plano "parcela". Detalhe extra: "180 parcelas" não existe — o teto da via correta (Lei 10.522 arts. 10-A a 10-C) é **120**. Bloqueio adicional: **art. 57 + CTN 191-A — sem certidão (CPEN via parcelamento/transação) a recuperação não é concedida**. Solução com prazos/valores: `sessao3/passivo_fiscal_solucao.md`.

**Cláusula 5 — Fonte: operação + galpão R$ 4,5 mi → LEGAL, condicionada.**
Alienação judicial → ganho de capital fora da trava de 30% (art. 6º-B). Valor contábil do galpão desconhecido (ganho não calculável — premissa). Recomendação: reescrever a cláusula com **destinação expressa à quitação do Beta** — é o que decide se a empresa opera após a suspensão.

## 2. Efeito tributário do deságio (`efeito_tributario_desagio.json`)

| Campo | Valor | Base |
|---|---:|---|
| ganho_desagio | **3.882.000** | 60% × (Alfa 4.200.000 + Norte 1.850.000 + Sul 420.000) = 0,60 × 6.470.000. Trabalhistas integrais (sem ganho); Beta e União **excluídos** — cláusulas ineficazes, ganhos fictícios de 1.240.000 e 1.350.000 |
| pis_cofins_sobre_ganho | **0** | Art. 50-A, I — receita da renegociação fora da base do PIS/COFINS |
| prejuizo_fiscal / compensacao | **0 / 0** | Cliente não forneceu o estoque — premissa proeminente; se houver prejuízo, compensa **sem limite** (fórmula: base = max(0; 3.882.000 − prejuízo)) |
| base_irpj_csll | **3.882.000** | 3.882.000 − 0 |
| irpj_csll | **1.317.880** | IRPJ 15% = 582.300 + adicional 10% × (3.882.000 − 20.000) = 386.200 + CSLL 9% = 349.380. **Alíquotas não constam da biblioteca — rotuladas como NÃO VERIFICADAS** |
| trava_30_aplicavel | **false** | Art. 50-A, II — o ganho da redução de dívida em RJ não se sujeita à trava de 30% (com trava, a compensação seria limitada a 1.164.600) |

Ressalva registrada no JSON: art. 50-A, parágrafo único — se Alfa/Beta/fornecedores forem **pessoas ligadas**, os benefícios fiscais caem; o cliente não informou.

Nada foi forçado: os ganhos irrealizáveis da minuta (fiduciário e União) ficaram explicitamente fora dos números, e as alíquotas de IRPJ/CSLL estão marcadas como não verificáveis dentro da biblioteca fechada.