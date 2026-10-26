# Demonstrativo Mensal nº 1 — mês do pedido

**Devedor:** Atlas Distribuidora S.A. — RJ, TJSP proc. 1012xxx-xx.2026.8.26.0100
**Apresentação:** ao Administrador Judicial **AJ Reorganiza Ltda.** — obrigação do art. 52, IV ("*contas demonstrativas mensais* enquanto perdurar a RJ", sob pena de destituição dos administradores — `lei11101_excertos.md`).
**Período de referência:** mês do pedido (primeiro ciclo de 4 semanas após o pedido). **Assunção destacada:** a data exata do pedido não consta nos documentos — a decisão de processamento é de 12/03/2026 e os rótulos do cliente indicam pedido entre 03/02/2026 e 12/03/2026; adota-se o mês de **março/2026** como mês 1 até confirmação (QUESTIONS.md, item 1).

---

## 1. Caixa

Fonte: `documents/fluxo_caixa_13_semanas.csv`. O arquivo é intitulado "13 semanas", mas **contém apenas as semanas 1–4** — pendência registrada em QUESTIONS.md (item 2); as 4 semanas apresentadas assumem-se como o primeiro mês.

| Semana | Saldo inicial | Recebimentos | Pagamentos pós-pedido | Saldo final | Conferência |
|---|---:|---:|---:|---:|---|
| 1 | 820.000 | 1.450.000 | 1.380.000 | 890.000 | 820.000+1.450.000−1.380.000 = 890.000 ✓ |
| 2 | 890.000 | 1.390.000 | 1.420.000 | 860.000 | 890.000+1.390.000−1.420.000 = 860.000 ✓ |
| 3 | 860.000 | 1.510.000 | 1.400.000 | 970.000 | 860.000+1.510.000−1.400.000 = 970.000 ✓ |
| 4 | 970.000 | 1.420.000 | 1.550.000 | 840.000 | 970.000+1.420.000−1.550.000 = 840.000 ✓ |
| **Mês** | **820.000** | **5.770.000** | **5.750.000** | **840.000** | 5.770.000−5.750.000 = +20.000; 820.000+20.000 = 840.000 ✓ |

- Saldo final do mês: **R$ 840.000**; geração líquida de caixa do período: **+R$ 20.000**.
- A coluna "pagamentos pós-pedido" não discrimina a composição por credor; se alguma parcela corresponder a credor concursal (p. ex., pagamento ao Fornecedor Norte por fora, instruído pelo diretor financeiro), caberá correção e prestação de esclarecimentos ao AJ (QUESTIONS.md, item 5). Orientação emitida ao diretor: vedado (`sessao1/resposta_diretor.md`, ressalvado no adendo) — a diretoria confirmou a política de pagamentos à vista para fornecimentos novos.

## 2. Obrigações pós-pedido (extraconcursais — art. 67)

| Obrigação | Valor | Base |
|---|---:|---|
| Fornecedor Norte Ltda — entrega de 20/03/2026 | 310.000 | fornecimentos pós-pedido são extraconcursais (art. 67, `lei11101_excertos.md`) |
| Composição dos pagamentos semanais correntes (1,38–1,55 mi/semana) | s/ discriminação | ver QUESTIONS.md item 5 |

- A entrega de 20/03/2026 é paga **sem deságio** e não é alcançada pela suspensão; sem registro nos documentos do seu pagamento ou prazo — assumida como a pagar (assunção; QUESTIONS.md, item 4).
- Nota: Banco Alfa e Banco Beta não têm obrigações novas pós-pedido identificadas; qualquer fornecimento futuro de capital de giro (ex.: do Norte) será pós-pedido e por fora do plano, conforme política emitida na `sessao1/resposta_diretor.md` e confirmada pela diretoria (adendo).

## 3. Concursais (passivo sujeito ao plano)

### 3.1 Quadro por classe (valores da data do pedido — art. 49, caput)

| Classe | Credor | Valor | Tratamento (minuta) | A pagar pelo plano (nominal) |
|---|---|---:|---|---:|
| I — Trabalhista | 112 empregados | 960.000 | integral, até 18 meses da homologação | 960.000 |
| III — Quirografário | Banco Alfa | 4.200.000 | deságio 60%, 120p, carência 24m | 4.200.000×40% = 1.680.000 |
| III — Quirografário | Fornecedor Norte (atraso 15/01/2026) | 1.850.000 | deságio 60%, 120p, carência 24m | 1.850.000×40% = 740.000 |
| IV — ME/EPP | Fornecedor Sul S.A. | 420.000 | deságio 60%, 120p, carência 24m | 420.000×40% = 168.000 |
| **Total** | | **7.430.000** | | **3.548.000** |

Conferência: 7.430.000 − 3.548.000 = **3.882.000** de deságio nominal (2.520.000 Alfa + 1.110.000 Norte + 252.000 Sul).
⚠ Teto do art. 54: prazo p/ trabalhistas é de 1 ano (art. 54, caput), prorrogável até 2 anos nas condições do §2º — os 18 meses da minuta exigem exame na Sessão 2 (garantias e aprovação da classe).
⚠ Juros/correção das parcelas: não informados na minuta; totais acima são nominais sem encargos.

### 3.2 Créditos que NÃO integram o quadro concursal (relatados ao AJ de ofício)

| Credor | Valor | Motivo |
|---|---:|---|
| Banco Beta (alienação fiduciária de máquinas) | 3.100.000 | proprietário fiduciário não se submete aos efeitos da RJ (art. 49, §3º); com a ressalva da vedação de venda/retirada de **bens de capital essenciais** durante o prazo de suspensão do art. 6º, §4º — **essencialidade confirmada pela diretoria** (adendo da `resposta_diretor.md`; QUESTIONS.md item 9 resolvido). A cláusula da minuta que sujeita fiduciários ao plano com deságio de 40% conflita com o art. 49, §3º — **condenada na Sessão 2** (`sessao2/analise_plano.md`) |
| União (IRPJ/CSLL/PIS/COFINS) | 2.700.000 | crédito tributário não ocupa posição no concurso (CTN art. 187; art. 68). Parcelamento/transação em curso? — não iniciado; recomendação n.º 2 da `resposta_diretor.md` (arts. 10-A a 10-C da Lei 10.522) |

### 3.3 Controle processual e suspensão

- Edital do art. 52, §1º: determinado pela decisão de 12/03/2026; publicação não evidenciada nos documentos — **pendência**.
- Suspensão das execuções (art. 6º, §4º): 180 dias desde 12/03/2026 → **vence 08/09/2026** (prorrogável uma vez). Execuções **fiscais** não aderem à suspensão (art. 6º, §7º-B) — principal urgência do parcelamento/transação (`sessao1/resposta_diretor.md`).

## 4. UPI

| Item | Valor | Situação |
|---|---:|---|
| Venda do galpão (fonte de recursos do plano) | 4.500.000 | **não executada** no período; sem registro nos caixas dos dados da seção 1 — planejamento da minuta |

- Cobertura nominal: 4.500.000 ≥ 3.548.000 (obrigações do plano, seção 3.1) → folga nominal de 952.000. A folga encolhe se a União for tratada pelas vias do parcelamento/transação (ex.: transação com desconto de 70% ⇒ até 810.000 de custo ⇒ folga cairia para 4.500.000 − 3.548.000 − 810.000 = **142.000**). Calibragens de calendário (carência de 24 meses dos quirografários vs. prazos da UPI e das parcelas trabalhistas) **não reconciliam com os dados disponíveis** — deixado aberto de propósito.
- Alienação judicial em RJ: eventual ganho de capital não sofre a trava de 30% (art. 6º-B, `lei11101_excertos.md`); valor contábil do galpão/laudo — QUESTIONS.md item 8.
- Bens do Banco Beta (máquinas em alienação fiduciária): não são UPI; vedada venda/retirada de bens de capital essenciais na pendência do art. 6º, §4º — essencialidade **confirmada pela diretoria** (adendo).

---

**Declaração de cumprimento:** demonstrativo apresentado conforme a obrigação mensal (art. 52, IV — sob pena de destituição dos administradores).
**Itens abertos:** itens de `deliverable/QUESTIONS.md` relevantes ao mês 1 (1, 2, 4 e 5 — o item 9 foi resolvido: essencialidade confirmada); pagamento da entrega de 20/03/2026 não evidenciado; publicação do edital do art. 52, §1º não evidenciada; livros/divulgações nºs contábeis não remetidos (CPC 48 a aplicar na novação futura).
