# Pendências e ressalvas — fechamento 01/2026 (Atlas Distribuidora S.A.)
*(atualizado com as respostas do cliente — sessão 1)*

## 1. Crédito de PIS/COFINS da NF-e 8812 (Papel & Cia) — estorno CONFIRMADO e mantido
- Cliente confirmou o fato: "É papel e toner da sede" → material de uso e consumo de área administrativa.
- O argumento do cliente ("o fornecedor destacou PIS/COFINS, então creditamos") **não sustenta o crédito**: o destaque do fornecedor (CST 01) é condição necessária mas não suficiente — o crédito só existe se o bem se enquadra nas hipóteses legais (insumo na produção/revenda). Uso e consumo administrativo (papelaria, toners) não gera crédito e o crédito tomado deve ser estornado (Lei 10.637/2002, art. 3º; Lei 10.833/2003, art. 3º; IN RFB 2.121/2022, art. 176; REsp 1.221.170/PR — library/pis_cofins_uso_consumo.md).
- Ajuste mantido: AJ-2026-01-001 (déb. 4.2.04 / créd. 1.1.04, R$ 11.100,00). PIS/COFINS a recolher em janeiro: **R$ 79.883,00**.
- **Desconhecido remanescente (cliente não tem a informação)**: se a EFD-Contribuições/DCTF de 01/2026 já foram transmitidas. Mantidas as duas rotas em `pis_cofins.json`: não entregues → escriturar sem o crédito; entregues → retificar EFD/DCTF e recolher a diferença com acréscimos. O valor (R$ 79.883,00) não muda.

## 2. Brindes — EXISTÊNCIA CONFIRMADA pelo cliente; VALOR NÃO INFORMADO (pendência para o e-LALUR do trimestre)
- Resposta do cliente: "Vinho e canivete gravado pros 400 melhores clientes. Marketing, ora."
- **Caracterização fiscal**: a entrega de itens (vinho, canivete personalizado) a clientes é **despesa com brindes**, cuja dedução é **vedada** para IRPJ/CSLL (Lei 9.249/95, art. 13, VII — library/lei9249_art13.md). O rótulo "marketing" não muda a natureza: não se trata de publicidade/propaganda, e sim de distribuição de bens a clientes. O valor será **adição** no e-LALUR do 1º trimestre (sem alteração na contabilidade societária — library/irpj_csll_trimestral.md).
- **Falta o valor**: no razão de janeiro não há conta de marketing; o único lançamento candidato é 4.2.02 "Despesas comerciais" — R$ 85.000,00 (20/01, "despesas comerciais ordinárias"). Como o cliente não fornece decomposição, **premissa assumida e sinalizada com destaque**: salvo comprovação documental em contrário, a parcela de brindes será tratada como **até R$ 85.000,00** (teto = saldo integral da 4.2.02 de janeiro), adicionada no e-LALUR. Se vier decomposição (de janeiro e dos demais meses), a adição é recalculada no valor real.
- Nada foi "forçado" no mês: a adição é da apuração trimestral (março), não do balancete de janeiro.

## 3. Compensação do prejuízo fiscal — trava de 30% (apurar em mes_03)
- Diretor quer "compensar todo o prejuízo" (R$ 900.000,00). A compensação é limitada a **30% do lucro líquido ajustado pelas adições e exclusões** (Lei 9.065/95, arts. 15 e 16 — library/lei9065_art15_trava.md; STF RE 591.340, Tema 117). Para compensar R$ 900.000,00 seria preciso lucro real antes da compensação ≥ R$ 3.000.000,00 no trimestre — projetado muito acima do que os números de janeiro indicam (resultado líquido ajustado de janeiro: R$ 128.483,00). A apuração correta vai em `mes_03/lalur.json`, com saldo remanescente na Parte B.

## 4. IRPJ/CSLL de janeiro
- Regime trimestral: sem apuração/provisão mensal (Lei 9.430/96, arts. 1º–2º — library/irpj_csll_trimestral.md). Insumo para março: **resultado líquido contábil de janeiro ajustado = R$ 128.483,00**.

## 5. Conferências e demais desconhecidos sinalizados
- Razão de janeiro fecha em partida dobrada (R$ 27.379.384,00/lado) e bate com o balancete conta a conta (verificado em Python).
- **ICMS (desconhecido remanescente)**: cliente não forneceu memória de cálculo. Mantido R$ 177.800,00 (7% líquido) como registrado pela empresa, sem ajuste — conferência fiscal de ICMS está fora do escopo dos entregáveis contratuais.
- 2.1.03 em 31/01: R$ 1.152.750,00 = 740.000,00 + 234.950,00 (PIS/COFINS bruto) + 177.800,00 (ICMS); apuração por dentro (líquido PIS/COFINS 79.883,00 + crédito remanescente 155.067,00) confere; nenhuma reclassificação forçada.
- Saldos de abertura da Parte B (prejuízo fiscal e base negativa CSLL: R$ 900.000,00 cada) serão controlados no e-LALUR de março.
