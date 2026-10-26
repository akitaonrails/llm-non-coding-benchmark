Sessão 3 entregue em `deliverable/sessao3/` — `lancamentos_novacao.json` (partidas conferidas: débito = crédito em todos os lançamentos) e `passivo_fiscal_solucao.md`. Resumo:

## 1. Novação e ganho do deságio (`lancamentos_novacao.json`)

**Critério (biblioteca `cpc_contabil_rj.md`):** a homologação opera novação (LRF art. 59); CPC 48/IFRS 9 — teste dos 10%: o passivo cai de 6.470.000 para 2.588.000 (mudança de 60% do nominal → substancialmente diferente) → baixa o original, reconhece o novo **a valor justo (PV das parcelas)**, diferença ao resultado como "receita de renegociação de dívidas em RJ", separadamente divulgada.

**Lançamento 1 — novação das classes III/IV (na homologação):**

| Conta | D | C |
|---|---:|---:|
| Fornecedores/Empréstimos quirografários — Alfa | 4.200.000 | |
| Fornecedores quirografários — Norte (pré-pedido) | 1.850.000 | |
| Fornecedores ME/EPP — Sul | 420.000 | |
| Dívida renegociada RJ — valor justo (120 parcelas, carência 24m) | | 2.588.000 |
| Receita de renegociação de dívidas em RJ (ganho do deságio) | | 3.882.000 |

D 6.470.000 = C 6.470.000 ✔ — *premissa proeminente: PV aproximado pelo nominal (2.588.000); sem taxa de desconto informada não há PV calculável — com curva de juros, PV < nominal aumentaria o ganho.*

**Lançamento 2 — trabalhistas (reclassificação, sem baixa):** D obrigações trabalhistas 960.000 / C "créditos concursais — classe I" (rubrica própria, exigida pela OCPC/CFC durante a RJ). Integral, sem deságio; ajuste ao PV das parcelas (12–18m) não calculável sem taxa.

**Lançamentos 3–5 — o que NÃO se lança:** Beta (fiduciário) fica fora — novação da cláusula de 40% é ineficaz (art. 49 §3º); se quitado com o galpão: D dívida fiduciária 3.100.000 / C caixa 3.100.000. União: sem novação — só reclassificação por adesão ao parcelamento (D tributos vencidos 2.700.000 / C passivo de parcelamento/transação). Pós-pedido (Norte 310.000): fica em passivo operacional normal, fora das rubricas concursais (art. 67).

**Efeito no resultado:** +3.882.000 de receita; PIS/COFINS = 0 (art. 50-A, I); IRPJ/CSLL estimado 1.317.880 (alíquotas rotuladas NÃO VERIFICADAS — fora da biblioteca); reduzível por prejuízo fiscal **sem trava de 30%** (art. 50-A, II) — estoque de prejuízo é desconhecido (premissa 0).

## 2. Passivo fiscal da União — R$ 2.700.000 (`passivo_fiscal_solucao.md`)

Por que o plano não resolve: CTN 187 (não vai a concurso), art. 68 (não se sujeita ao plano), art. 6º §7º-B (execução fiscal **não suspende** — risco de constrição contínua), e art. 57 + CTN 191-A: **sem certidão (CPEN) a recuperação não é concedida** — o parcelamento é condição do processo, não opção.

Via correta — Lei 10.522 arts. 10-A a 10-C (valores nominais, sem juros consolidados — taxas não estão na biblioteca, premissa sinalizada):

| Opção | Estrutura | Aritmética | Parcela/mês |
|---|---|---|---:|
| **A** — parcelamento padrão RJ (art. 10-A) | até 120 parcelas | 2.700.000 ÷ 120 | **R$ 22.500,00** |
| **B** — liquidação com prejuízo fiscal (art. 10-A §1º-B) | até 30% em prejuízo + 84 parcelas | 810.000 liquidados; 1.890.000 ÷ 84 | **R$ 22.500,00** (poupa 810.000 de caixa) |
| **C** — transação PGFN (art. 10-C; Lei 13.988/2020; Portaria PGFN 2.382/2021) | desconto até 70%, até 120 meses | pago 810.000 ÷ 120 | **R$ 6.750,00** |

**Sequência recomendada:** (1) adotar A imediatamente → CPEN destrava a concessão (art. 57); (2) negociar C em paralelo (60–90 dias) — cenário máximo de desconto = economia nominal de 1.890.000, e a transação consolida sobre A; (3) se houver prejuízo fiscal, decidir o trade-off: o mesmo estoque não serve aos dois — abater o ganho de 3.882.000 do deságio vale ~R$ 1,32 mi de tributos (sem trava), contra 810.000 de caixa na Opção B → prioridade ao ganho se o estoque for pequeno; decisão fica em aberto porque o estoque é desconhecido. Riscos monitorados: atos constritivos sobre as **máquinas essenciais** da linha de separação (competência do juízo da RJ, ressalva do próprio §7º-B) e ICMS/ISS eventuais (biblioteca só cobre a via federal — não verificável).

**Engajamento (3 sessões):** tudo entregue — `STATUS.md` fecha em **COMPLETE WITH OPEN ITEMS**, com os 8 desconhecidos sinalizados (datas de protocolo/homologação, semanas 5–13, R$ 310 mil, valor contábil do galpão, prejuízo fiscal, partes ligadas, alíquotas fora da biblioteca, ICMS/ISS).