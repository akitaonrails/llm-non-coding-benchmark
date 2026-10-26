# Pendências — Fechamento 03/2026 e apuração do 1º trimestre (Atlas Distribuidora S.A.)

## 1. EFD-Contribuições 01/2026 — retificação não executada (3º mês)
- Estorno do crédito da NF 8812 (R$ 11.100,00): a **retificação da EFD de janeiro e o recolhimento da diferença com acréscimos** continuam pendentes desde mes_01. Acréscimos não quantificados: o cliente não tem data/valor do pagamento original e a sistemática de cálculo não consta da biblioteca citável (não presumo).

## 2. Estorno contábil ignorado pela contabilidade do cliente pela 3ª vez → AJ-03-001
- Balancete de março ainda traz 1.1.04 = 483.627 e 4.2.04 = 120.000. Reproduzi o lançamento (D 4.2.04 11.100 / C 1.1.04 11.100) em janeiro, fevereiro e agora março. **A ECF do 1T/2026 não deve ser entregue enquanto o ativo contiver crédito sabidamente indevido** — registrar AJ-03-001 e retificar a EFD antes.
- O e-LALUR já parte do lucro correto (604.149,00, não 615.249,00 dos livros).

## 3. Nenhum recolhimento de tributos lançado no trimestre
- 2.1.03 fecha março em 1.997.750,00 = abertura 740.000,00 (12/2025) + accruals do 1T 1.257.750,00 (PIS/COFINS 715.950 + ICMS 541.800), **sem nenhuma baixa de pagamento**. Somam-se os DARFs de IRPJ/CSLL do 1T (176.581,47, a recolher conforme vencimento que não posso afirmar — fora da biblioteca). Se efetivamente pagos sem lançamento, a escrita está subavaliada no passivo e no caixa; se não pagos, há passivo em aberto com acréscimos não mensuráveis. Conferir extratos bancários com o financeiro (cliente declarou não ter os dados de pagamento).

## 4. Provisão de IRPJ/CSLL do 1T (AJ-03-002, R$ 176.581,47) — contas novas propostas
- O plano de contas (22 contas) não tem despesa nem passivo de IRPJ/CSLL. Propus **4.3.02 "Provisão para IRPJ e CSLL"** e **2.1.05 "IRPJ/CSLL a recolher"** — códigos sujeitos à aprovação do cliente; não usei conta existente inadequada.
- Dedutibilidade fiscal dessa provisão no 2T/2026: **não verificada na biblioteca** → levamos ao fechamento do 2º trimestre como premissa a confirmar.

## 5. Premissa final dos R$ 85.000,00 "comerciais ordinários" (20/01, 20/02, 20/03)
- Cliente foi perguntado e declarou não ter mais informação; premissa declarada **final** (não será re-perguntada): janeiro = 100% brindes (adição AF-01-001, por declaração escrita do próprio cliente); fevereiro/março = despesa normal dedutível (posição da auditoria interna de fevereiro).
- Sensibilidade fechada no trimestre (memoria.md item 8): adições 78.000 / 163.000 / 248.000 → IRPJ+CSLL 156.351,46 / 176.581,47 / 196.811,46 (delta B→C ≈ 40.460). Se aparecer documentação, retifica-se a linha de adição e a trava na ECF.

## 6. Compensação de prejuízo — pedido da diretoria formalmente negado (reafirmado e negado de novo)
- "Compensar todo o prejuízo" (R$ 900.000,00) é **juridicamente impossível**: trava de 30% do lucro líquido ajustado (Lei 9.065/95, arts. 15/16; STF RE 591.340, Tema 117 — library/lei9065_art15_trava.md). Compensação do 1T: **230.144,70**; saldos remanescentes na Parte B: 669.855,30 (prejuízo fiscal) e 669.855,30 (base negativa CSLL).
- **2º registro (reafirmação da diretoria após a entrega do 1T — "compensa tudo, se a Receita reclamar a gente discute"): recusa mantida.** O "discutir" já foi discutido e perdido no STF (Tema 117, constitucionalidade da trava). Além disso é aritmeticamente impossível: com lucro antes da compensação de 767.149, no máximo se absorveria 767.149 (restando 132.851); "tudo" jamais caberia no trimestre. O efeito prático da proposta não é "usar dinheiro parado" e sim **apagar o tributo do trimestre**: IRPJ+CSLL cairiam de 176.581,47 para zero — subfaturamento escriturado na ECF. Penalidades/juros sobre a diferença não constam da biblioteca citável → não afirmados. O saldo de 669.855,30 preserva valor: a regra permite compensar "em períodos subsequentes" (até 30% por período); a library/irpj_csll_trimestral.md define a Parte B exatamente como controle de saldos a compensar. lalur.json permanece com 230.144,70 — não entregamos apuração com compensação ilegal.
- Da mesma forma, "não mexer no crédito de janeiro" foi sobreposto pela evidência documental (library/pis_cofins_uso_consumo.md). Instrução da diretoria não prevalece sobre a lei; registrado para trilha de auditoria.

## 7. Premissas mantidas no fechamento de março
| Item | Premissa | Efeito se errada |
|---|---|---|
| Compra de 15/03 (R$ 1.729.200) com crédito de 159.951,00 | mercadoria para revenda → crédito lícito | estorno de crédito + EFD a retificar |
| 85.000 de março | despesa comercial normal (padrão de fev + auditoria) | +85.000 de adição (cenário C) |
| Saldos de abertura 900.000/900.000 | compensáveis, sempre sob a trava | base de compensação menor |
| Pagamentos de tributos | cliente sem dados; não presumo | acréscimos/passivo reais desconhecidos |

## 8. E-LALUR entregue — números do 1T (detalhe em lalur.json e memoria.md)
- LL contábil ajustado 604.149,00 + adições 163.000,00 = 767.149,00 antes da compensação; compensação 230.144,70 (trava); **lucro real 537.004,30**; IRPJ 128.251,08 (15%: 80.550,65 + adicional: 47.700,43); CSLL 48.330,39; total **176.581,47**; Parte B final: 669.855,30 / 669.855,30.
