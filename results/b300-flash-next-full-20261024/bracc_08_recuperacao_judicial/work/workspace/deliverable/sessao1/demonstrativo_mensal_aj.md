# Contas Demonstrativas Mensais — Mês 1 (mês do pedido)

**Atlas Distribuidora S.A. — Recuperação Judicial**
Processo 1012xxx-xx.2026.8.26.0100 — 2ª Vara de Falências e Recuperações Judiciais do TJSP
**Para:** AJ Reorganiza Ltda. (administrador judicial nomeado na decisão de processamento)
**Obrigação:** apresentação de contas demonstrativas mensais enquanto perdurar a RJ (Lei 11.101/2005, art. 52, IV), sob pena de destituição dos administradores.
**Competência:** março/2026 — mês do pedido/processamento (deferimento em 12/03/2026).

> **Premissas e limites desta 1ª entrega** (detalhadas em "Aberturas" ao final): (a) o arquivo `fluxo_caixa_13_semanas.csv` traz apenas **4 das 13 semanas** — presumimos que sejam as 4 primeiras semanas pós-pedido (≈12/03 a 09/04/2026); (b) a data exata do protocolo do pedido não consta do arquivo — usamos a data do deferimento do processamento (12/03/2026) como referência, o que é consistente com a classificação dos créditos (origens ≤ 03/02/2026 = pré-pedido; entrega Norte = 20/03/2026 = pós-pedido); (c) tributos sobre fatos geradores pós-pedido presumidamente pagos no curso normal e já incluídos na coluna "pagamentos_pos_pedido".

---

## 1. Caixa (disponibilidades)

| Semana | Saldo inicial | Recebimentos | Pagamentos pós-pedido | Saldo final |
|---|---:|---:|---:|---:|
| 1 | 820.000 | 1.450.000 | (1.380.000) | 890.000 |
| 2 | 890.000 | 1.390.000 | (1.420.000) | 860.000 |
| 3 | 860.000 | 1.510.000 | (1.400.000) | 970.000 |
| 4 | 970.000 | 1.420.000 | (1.550.000) | 840.000 |
| **Total (4 semanas)** | **820.000** | **5.770.000** | **(5.750.000)** | **840.000** |

**Conferência aritmética (semana a semana):**
- S1: 820.000 + 1.450.000 − 1.380.000 = 890.000 ✔
- S2: 890.000 + 1.390.000 − 1.420.000 = 860.000 ✔
- S3: 860.000 + 1.510.000 − 1.400.000 = 970.000 ✔
- S4: 970.000 + 1.420.000 − 1.550.000 = 840.000 ✔
- Consolidação: 820.000 + 5.770.000 − 5.750.000 = **840.000** (= saldo final informado) ✔

Leitura: fluxo operacional aproximadamente neutro no período (recebimentos − pagamentos = 5.770.000 − 5.750.000 = **+20.000**); caixa encerra em R$ 840 mil, sem consumo de saldo.

## 2. Obrigações pós-pedido (extraconcursais — art. 67)

Obrigações contraídas **durante** a recuperação são extraconcursais (Lei 11.101/2005, art. 67), pagáveis no curso normal:

| Item | Data | Valor (R$) | Situação |
|---|---|---:|---|
| Fornecedor Norte Ltda — fornecimento pós-pedido | 20/03/2026 | 310.000 | Em aberto; caixa de R$ 840 mil comporta o pagamento (840.000 ≥ 310.000) |
| Pagamentos do curso normal (semanas 1–4) | semanas 1–4 | 5.750.000 | Já liquidados (coluna "pagamentos_pos_pedido") |
| Tributos sobre fatos geradores pós-pedido | — | não informado | **Presunção:** pagos no curso normal, dentro dos R$ 5.750.000 acima (ver Aberturas) |

Observação ao AJ: o fornecimento pós-pedido do Norte (**R$ 310 mil**) deve ser pago normalmente; já o saldo **pré-pedido** do mesmo credor (R$ 1.850.000, concursal — art. 49) **não** comporta pagamento fora do plano (favorecimento de credor — art. 172; afastamento de administradores — art. 64; risco de convolação em falência, conforme excertos da biblioteca). Ver `resposta_diretor.md`.

## 3. Créditos concursais (sujeitos à recuperação — art. 49)

Créditos existentes na data do pedido, ainda que não vencidos (art. 49), **sem pagamento no período** (plano ainda não apresentado/homologado; execuções suspensas pelo art. 6º, §4º — 180 dias, prorrogável uma vez, conforme decisão):

| Classe | Credor | Valor (R$) |
|---|---|---:|
| I — Trabalhista | Trabalhistas (112 empregados) | 960.000 |
| III — Quirografário | Banco Alfa (capital de giro) | 4.200.000 |
| III — Quirografário | Fornecedor Norte Ltda (saldo pré-pedido) | 1.850.000 |
| IV — ME/EPP | Fornecedor Sul S.A. (EPP) | 420.000 |
| **Total concursal** | | **7.430.000** |

Aritmética: 960.000 + 4.200.000 + 1.850.000 + 420.000 = **7.430.000**. Detalhamento com fundamentos em `classificacao_creditos.json`.

## 4. Não concursais e não sujeitos ao plano

| Credor | Natureza | Valor (R$) | Tratamento |
|---|---|---:|---|
| Banco Beta (CCB c/ alienação fiduciária de máquinas) | Fiduciário — extraconcursal | 3.100.000 | Não se submete à RJ (art. 49, §3º); no prazo de suspensão é vedada a venda/retirada das máquinas essenciais do estabelecimento |
| União — IRPJ/CSLL/PIS/COFINS | Tributário — não sujeito | 2.700.000 | Não se sujeita a concurso/habilitação (CTN, art. 187) nem ao plano (art. 68); execuções fiscais não suspensas (art. 6º, §7º-B). Via: parcelamento/transação (Lei 10.522/2002, arts. 10-A a 10-C) para CND+ (art. 57; CTN 191-A) |
| **Total** | | **5.800.000** | 3.100.000 + 2.700.000 = 5.800.000 |

Reconciliação da relação de credores: concursais 7.430.000 + fiduciário 3.100.000 + pós-pedido 310.000 + tributário 2.700.000 = **13.540.000** (fecha com a soma da relação de credores) ✔

## 5. UPI — Unidade Produtora Isolada (galpão)

| Item | Situação no mês | Valor esperado |
|---|---|---:|
| Galpão identificado como UPI, previsto como fonte de recursos do plano (minuta) | **Não alienado** no período — nenhum recurso de venda aparece no fluxo de caixa das 4 semanas | 4.500.000 (pretensão, não realizado) |

Notas: (i) nenhum ingresso de venda de ativo consta dos recebimentos (1.450/1.390/1.510/1.420 mil são compatíveis com recebíveis operacionais), portanto a UPI permanece no ativo; (ii) o regime jurídico da alienação de UPI (creio estar no art. 60-A da Lei 11.101/2005 — **norma NÃO constante da biblioteca de referência; trate como não verificado**) e seus efeitos societários/trabalhistas serão analisados na Sessão 2; (iii) eventual ganho de capital em alienação judicial de bens em RJ não sofre a trava de 30% (art. 6º-B, verificado na biblioteca).

---

## Aberturas (pendências para a próxima competência)

1. **Fluxo incompleto:** o arquivo chama-se "13 semanas" mas só traz 4 (semanas 1–4). Solicitadas as 9 semanas restantes (`QUESTIONS.md`). Este demonstrativo cobre apenas as 4 semanas apresentadas.
2. **Data exata do pedido** (protocolo) não informada — necessária para fixar com precisão o corte do art. 49, embora a classificação corrente seja robusta a qualquer data entre 03/02/2026 e 20/03/2026.
3. **Composição detalhada dos R$ 5.750.000 pagos** (semanas 1–4): precisamos da abertura por natureza (fornecedores, folha, tributos, despesas fixas) para atestar que **nenhum valor** foi destinado a crédito concursal pré-pedido.
4. **Honorários do administrador judicial e da assessoria** — não informados; serão extraconcursais por lei (regime não detalhado na biblioteca — tratar quando informado).
5. Tributos pós-pedido sem comprovação de recolhimento em guia própria (presunção declarada acima).

*Base exclusiva: documentos do cliente e `library/` (INDEX: Lei 11.101/2005 arts. 6º, 6º-B, 49, 50-A, 52, 54, 57, 58, 67, 68; CTN 187 e 191-A; Lei 10.522/2002 arts. 10-A a 10-C; CPC 48/25). Afirmações doutrinárias ou artigos não listados no INDEX não foram utilizados como fundamento.*
