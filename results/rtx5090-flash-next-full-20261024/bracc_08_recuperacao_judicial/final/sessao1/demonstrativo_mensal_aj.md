# Contas Demonstrativas Mensais — Março/2026 (mês do pedido)

**Atlas Distribuidora S.A. — Recuperação Judicial**
Processo TJSP 1012xxx-xx.2026.8.26.0100 — 2ª Vara de Falências e Recuperações Judiciais
**Ao Administrador Judicial:** AJ Reorganiza Ltda.
**Obrigação:** art. 52, IV da Lei 11.101/2005 (contas demonstrativas mensais enquanto perdurar a RJ, sob pena de destituição dos administradores) — conforme item (i) da decisão de processamento de 12/03/2026.

> **Premissas e limitações (importantes):**
> - O **pedido** foi deferido para processamento em **12/03/2026**; a relação de credores trata a entrega de **20/03/2026** como pós-pedido, logo assumo o pedido em data anterior a 20/03/2026. **Confirmado com o cliente: a data exata não está disponível** — tratada como premissa, não como fato.
> - O fluxo de caixa de 13 semanas fornecido cobre apenas as **semanas 1–4**; as semanas 5–13 não existem no arquivo do cliente — o demonstrativo cobre somente as 4 primeiras (pendência explícita).
> - Os valores abaixo vêm de `documents/relacao_credores.csv` e `documents/fluxo_caixa_13_semanas.csv` e **não foram conciliados com a contabilidade da empresa**; divergências devem ser ajustadas com o AJ.

---

## 1. Caixa e fluxo operacional (semanas 1–4)

| Semana | Saldo inicial | Recebimentos | Pagamentos pós-pedido | Saldo final |
|---|---:|---:|---:|---:|
| 1 | 820.000 | 1.450.000 | 1.380.000 | 890.000 |
| 2 | 890.000 | 1.390.000 | 1.420.000 | 860.000 |
| 3 | 860.000 | 1.510.000 | 1.400.000 | 970.000 |
| 4 | 970.000 | 1.420.000 | 1.550.000 | 840.000 |
| **Total** | **820.000** | **5.770.000** | **5.750.000** | **840.000** |

**Conferência:** 820.000 + 5.770.000 − 5.750.000 = **840.000** ✔ (bate com o saldo final da semana 4)

- Fluxo livre do período: 5.770.000 − 5.750.000 = **+20.000** (geração praticamente neutra).
- Caixa é suficiente para o giro pós-pedido, mas **não suporta** pagamento relevante de créditos antigos sem afetar o operacional (o caixa total do período seria incapaz de absorver, isoladamente, os R$ 1,85 mi do Norte: 840.000 de saldo final < 1.850.000).

## 2. Obrigações pós-pedido (extraconcursais — art. 67 da LRF)

| Obrigação | Origem | Valor (R$) | Situação |
|---|---|---:|---|
| Fornecedor Norte Ltda — entrega 20/03/2026 | compra durante a RJ | 310.000 | Em aberto na data do relatório; **pagável fora do plano** (art. 67) |
| Fornecimentos/operacional contínuo | semanal | 5.750.000 (4 semanas) | Já liquidados no fluxo da seção 1 |

**Total de obrigação extraconcursal em aberto (estimado): R$ 310.000.**
⚠ *Não reconciliado*: não sei se os R$ 310 mil já estão incluídos na linha "pagamentos_pos_pedido" das semanas 1–4 ou permanecem no passivo. Deixo em aberto e peço confirmação (ver QUESTIONS.md).

📌 *Nota de visibilidade*: a segregação acima é intencional — pagamentos de créditos **concursais** (ex.: qualquer valor sobre os R$ 1,85 mi pré-pedido do Norte) não têm onde "entrar" neste demonstrativo sem aparecer como favorecimento (art. 172). Um pagamento antigo rotulado de "adiantamento de fornecimento" apareceria como adiantamento sem entrega correspondente na reconciliação adiantamento × entregas — o AJ confere exatamente isso (art. 52, IV, sob pena de destituição).

## 3. Créditos concursais (sujeitos à RJ — art. 49) e créditos não sujeitos

**Base do mês do pedido**, conforme `relacao_credores.csv`:

### 3.1 Concursais — sujeitos ao plano (art. 49)

| Credor | Classe | Valor (R$) |
|---|---|---:|
| Trabalhistas (112 empregados) | I — trabalhista | 960.000 |
| Fornecedor Sul S.A. (EPP) | IV — ME/EPP | 420.000 |
| Fornecedor Norte Ltda (pré-pedido) | III — quirografário | 1.850.000 |
| Banco Alfa (capital de giro) | III — quirografário | 4.200.000 |
| **Total concursais sujeitos ao plano** | | **7.430.000** |

Aritmética: 960.000 + 420.000 + 1.850.000 + 4.200.000 = **7.430.000**
(Trabalhistas: R$ 960.000 / 112 ≈ R$ 8.571 média por empregado; eventual cisão trabalhista×quirografário pelo teto de 1,5 salário mínimo **não pode ser verificada** — art. 83 não consta da biblioteca. Assumido integralmente na classe I; a relação individual por empregado foi pedida em QUESTIONS.md.)

### 3.2 Não sujeitos à recuperação

| Credor | Natureza | Valor (R$) | Fundamento |
|---|---|---:|---|
| Banco Beta (CCB c/ alienação fiduciária de máquinas) | Fiduciário — extraconcursal | 3.100.000 | Art. 49, §3º: propriedade fiduciária prevalece. **Cliente confirmou: as máquinas são a linha de separação de pedidos (bem de capital essencial)** — não podem ser vendidas/retiradas durante a suspensão do art. 6º, §4º (180 dias, prorrogável uma vez — item (ii) da decisão de 12/03/2026; vencimento ≈08/09/2026 se não prorrogada — prorrogação não comprovada nos autos); após isso, risco de retomada pelo fiduciário. Plano de quitação: ver `deliverable/sessao2/analise_plano.md` |
| União — IRPJ/CSLL/PIS/COFINS | Tributário — não sujeito | 2.700.000 | CTN art. 187; LRF art. 68; execução fiscal não suspensa (art. 6º, §7º-B). Via: parcelamento/transação (Lei 10.522/2002, arts. 10-A a 10-C) — necessária também p/ certidão exigida pelo art. 57 / CTN 191-A |
| **Total não sujeitos** | | **5.800.000** | 3.100.000 + 2.700.000 |

### 3.3 Amostra da relação de credores (tudo)

7.430.000 (concursais) + 3.100.000 (fiduciário) + 2.700.000 (União) + 310.000 (pós-pedido) = **13.540.000** ✔ bate com a soma da planilha.

## 4. UPI (unidade produtiva isolada)

| Item | Situação contábil | Valor esperado (R$) | Observações |
|---|---|---:|---|
| Galpão — fonte de recursos do plano (minuta) | Valor contábil **não informado** | 4.500.000 (preço de venda previsto) | Ainda não vendido. Se alienado judicialmente, ganho de capital fora da trava de 30% (art. 6º-B). Venda de bens essenciais à atividade durante a suspensão do art. 6º, §4º exige cautela (art. 49, §3º, in fine) — submeter ao juízo/AJ antes de qualquer disposição. |

**Reconciliação pendente:** custo contábil e eventual ganho na alienação do galpão não podem ser calculados sem o valor patrimonial (solicitado em QUESTIONS.md).

---

*Elaborado pelo Controller quanto ao mês de março/2026 (mês do pedido; processamento deferido em 12/03/2026). Todas as citações legais referem-se exclusivamente a `library/INDEX.md`; itens não verificáveis na biblioteca estão marcados acima.*
