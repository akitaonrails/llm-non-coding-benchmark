# Notas de cálculo — efeito_tributario_desagio.json

Os campos `null` são **desconhecidos que não devem ser inventados**: o cliente declarou não ter a informação (ver `../QUESTIONS.md`). A fórmula e os cenários estão abaixo; preencher quando vier o saldo de prejuízo fiscal.

## ganho_desagio = 3.882.000 (verificado)

Deságio de 60% incide **somente** sobre os créditos válidamente submetidos ao plano que sofrem deságio na minuta:

| Classe | Credor | Crédito (R$) | Deságio 60% (R$) |
|---|---|---:|---:|
| III | Banco Alfa | 4.200.000 | 2.520.000 |
| III | Fornecedor Norte (pré-pedido) | 1.850.000 | 1.110.000 |
| IV | Fornecedor Sul (EPP) | 420.000 | 252.000 |
| **Total** | | **6.470.000** | **3.882.000** |

Aritmética: (4.200.000 + 1.850.000 + 420.000) × 0,60 = 6.470.000 × 0,60 = **3.882.000**; saldo nominal do novo passivo = 6.470.000 − 3.882.000 = 2.588.000.

**Excluídos do cálculo (e por quê):**
- **Trabalhistas (960.000):** pagamento integral na minuta ⇒ ganho zero sobre o principal (só eventual efeito de valor presente do prazo, taxa desconhecida).
- **Banco Beta (3.100.000):** cláusula de submissão ao plano é **ilegal** (art. 49, §3º) — o "deságio 40%" hipotético (1.240.000) **não** pode ser registrado; se houver acordo bilateral, registra-se quando firmado.
- **União (2.700.000):** não sujeita ao plano (CTN 187; art. 68) — os 50% de "deságio" da minuta (1.350.000) são **inexistentes juridicamente**; eventual desconto real virá de transação (Sessão 3).
- **Norte pós-pedido (310.000):** extraconcursal (art. 67), fora do plano.

**Divergência contábil x fiscal (premissa relevante):** pelo CPC 48/IFRS 9 (`library/cpc_contabil_rj.md`), o ganho contábil na novação é mensurado pelo **valor presente** das 120 parcelas com carência de 24 meses ⇒ o ganho contábil será **maior** que 3.882.000 em R$ |PV − nominal|; a **taxa de desconto do plano não foi informada** (desconhecida) — o número acima é o ganho **nominal** do deságio, base defensável para o efeito fiscal. Ajustar quando houver taxa.

## pis_cofins_sobre_ganho = 0 (verificado)

Art. 50-A, I: "a receita obtida pelo devedor não será computada na apuração da base de cálculo do PIS e da COFINS" nas renegociações em RJ (`library/lei11101_excertos.md`). Condição: o art. 50-A **não se aplica a dívidas com pessoas ligadas** (parágrafo único) — relação societária dos credores com os controladores **desconhecida**; se algum credor for ligado, o ganho correspondente sai do benefício.

## trava_30_aplicavel = false (verificado)

Art. 50-A, II: o ganho com redução da dívida **não se sujeita** ao limite dos arts. 42 e 58 da Lei 8.981/95 e 15 e 16 da Lei 9.065/95 (a "trava de 30%"). Atenção: a trava **também não** se aplica a ganho de capital em alienação judicial de bens em RJ (art. 6º-B). Alerta não verificado (não citável): tenho ciência de alterações legislativas posteriores a 2024 sobre compensação de prejuízos fiscais que **não constam da biblioteca** — validar com a consultoria tributária antes de reliance.

## prejuizo_fiscal / compensacao / base_irpj_csll / irpj_csll = null (desconhecidos)

O e-mail afirma que há prejuízo fiscal ("usa o prejuízo fiscal"), mas o **saldo não foi informado** e o cliente declarou não ter a informação — não invento número. Fórmulas (regime geral; **alíquotas de IRPJ/CSLL não constam da biblioteca ⇒ valores abaixo são ilustrativos e NÃO VERIFICADOS**):

- `compensacao = min(ganho, prejuizo_fiscal_disponivel)`
- `base_irpj_csll = ganho_desagio − compensacao`
- `irpj_csll ≈ base × ~34%` (IRPJ 15% + adicional ~10% + CSLL ~9% — alíquotas **não verificadas**)

**Cenários (ganho = 3.882.000):**

| Cenário | PF disponível | Compensação | Base | IRPJ/CSLL (~34%, ilustrativo) |
|---|---:|---:|---:|---:|
| A | ≥ 3.882.000 | 3.882.000 | 0 | 0 |
| B | 2.000.000 | 2.000.000 | 1.882.000 | ≈ 639.880 |
| C | 0 | 0 | 3.882.000 | ≈ 1.319.880 |

Disputa pelo PF: a opção B do parcelamento da União consome mais 810.000 de PF (ver `../sessao3/passivo_fiscal_solucao.md`) ⇒ para o Cenário A pleno é preciso PF ≥ **4.692.000** (3.882.000 + 810.000).

Despesas com o plano são **dedutíveis** (art. 50-A, III).
