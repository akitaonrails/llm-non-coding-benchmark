# Pendências — Fechamento 02/2026 (Atlas Distribuidora S.A.)

## 1. Ajuste de janeiro não registrado nos livros → executado em fevereiro
- O balancete de fevereiro ainda carregava o crédito indevido da NF 8812 (1.1.04 = 323.676; 4.2.04 = 120.000). Lancei **AJ-02-001** (D 4.2.04 11.100 / C 1.1.04 11.100, data 28/02) como retificação de mês anterior. Competência econômica é de janeiro (o LL do trimestre não muda: 128.483 + 193.083 = 321.566).
- A **retificação da EFD-Contribuições de 01/2026** e o recolhimento de R$ 11.100,00 **com acréscimos** (library/pis_cofins_uso_consumo.md) continuam pendentes na prática — a sistemática de cálculo dos acréscimos não consta da biblioteca e o cliente não tem a data/valor do pagamento original; não presumo nem quantifico.
- Os livros também não mostram **nenhum recolhimento** de PIS/COFINS/ICMS até fevereiro (2.1.03 cresce bruto: 1.572.000). Conferir com o financeiro.

## 2. Doação Associação Beneficente Luz — indedutível (adição de 30.000)
- Lei 9.249/95, art. 13, VI veda a dedução de doações, salvo as exceções do §2º (library/lei9249_art13.md). A entidade **não atende nenhuma**: não é projeto cultural (Lei 8.313/91); o próprio recibo registra que **não possui título de OSCIP nem certificação de utilidade pública federal** (é associação civil registrada em cartório); não é instituição de ensino e pesquisa. O limite de 2% do lucro operacional (§2º, II) nem se aplica, porque pressupõe doação qualificada.
- Registrei **AF-02-002** (adição de R$ 30.000,00, só no LALUR, sem lançamento contábil). Classificação contábil em 4.2.02 "Despesas comerciais" é tecnicamente inadequada (doação não é despesa comercial) — sem efeito no resultado; recomendo conta específica de doações, por sugestão ao cliente, por ora não lançada.

## 3. Brindes NF-e 4410 (R$ 48.000) — adição fiscal
- 400 kits vinho + canivete, campanha "Parceiros Atlas" (NF-e 4410, 12/02, CFOP 1949). Despesa com brindes: dedução vedada (art. 13, VII). **AF-02-001**, adição de R$ 48.000 no LALUR do trimestre, sem efeito contábil. Pago em caixa, sem crédito de PIS/COFINS tomado — nada a estornar.

## 4. Conflito não resolvido: os R$ 85.000 "ordinários" recorrentes
- Há um lançamento idêntico de R$ 85.000 em dinheiro contra 4.2.02 ("despesas comerciais ordinárias") em **20/01 e 20/02**. Em janeiro, o cliente descreveu a conta como "vinho e canivete gravado pros 400 melhores clientes"; mas a NF-e 4410 de fevereiro documenta exatamente isso — **400 kits** de vinho + canivete por R$ 48.000 — e a auditoria interna de fevereiro afirma que brindes no mês foram **só os 48 mil** ("acima do padrão histórico") e nada mais ("Sem outras observações").
- As duas versões não se reconciliam: ou os 85.000 de janeiro são brindes (adição AF-01-001 de 85.000 correta, e a "memória de cálculo" do cliente pode ter descrito na verdade a campanha de fevereiro), ou descrevem a compra da NF 4410 (aquisição registrada em fevereiro), caso em que a adição de janeiro está **superestimada** e os 85.000 recorrentes precisam de documentação.
- Tratei os 85.000 de **fevereiro** como despesas normais, dedutíveis (posição da auditoria), e mantive a adição de 85.000 de **janeiro** com a premissa já declarada. A pergunta foi feita e o cliente declarou **não ter mais informação** (rodada de 10/2026) — o item passa a **premissa declarada final**, não será re-perguntado.
- Sensibilidade no e-LALUR (sempre com March = pendente; valores até fev): cenário A (vigente, adições 163.000) → trava ≈ 30% × 484.566 = **145.370**; cenário B (85.000 de jan não são brinde, adições 78.000) → trava ≈ 30% × 399.566 = **119.870**; cenário C (85.000 de fev também são brinde, adições 248.000) → trava ≈ 30% × 569.566 = **170.870**. A base de IRPJ/CSLL pós-compensação se move na mesma proporção; em dinheiro, a diferença B→C passa de R$ 170.000 de base. Regras: library/lei9065_art15_trava.md e library/irpj_csll_trimestral.md.

## 5. Trava de 30% — alerta para o 1º trimestre
- Projeção apenas informativa (falta março): LL acumulado ajustado 321.566 + adições registradas 163.000 = 484.566 → limite de compensação ≈ 30% × 484.566 = **145.370**, muito aquém dos R$ 900.000 que a diretoria quer compensar (Lei 9.065/95, arts. 15/16; RE 591.340 Tema 117 — library/lei9065_art15_trava.md). Cálculo definitivo em mes_03.

## 6. Premissas mantidas
| Item | Premissa | Efeito se errada |
|---|---|---|
| Compra de 15/02 (R$ 1.702.800) | mercadoria para revenda → crédito 157.509 lícito | crédito indevido; estorno |
| 85.000 de fevereiro | despesa comercial normal (auditoria) | +85.000 de adição no LALUR |
| 85.000 de janeiro | 100% brindes (resposta do cliente) | −85.000 de adição (ver item 4) |
| Saldos fiscais de abertura | R$ 900.000/900.000 livres, sob a trava | base de compensação menor |
| Pagamentos PIS/COFINS | data/valor ignorados | acréscimos não calculados |

## 7. Evidenciação fiscal do trimestre (parcial, até fevereiro)
- LL contábil acumulado pós-ajustes: **321.566**. Adições permanentes registradas até agora: **163.000** (85.000 + 48.000 + 30.000). IRPJ (15% + adicional 10% sobre o que exceder R$ 60.000/trimestre), CSLL (9%), compensação com trava e Partes A/B do e-LALUR: apuração definitiva em mes_03 (library/irpj_csll_trimestral.md), após os documentos de março.
