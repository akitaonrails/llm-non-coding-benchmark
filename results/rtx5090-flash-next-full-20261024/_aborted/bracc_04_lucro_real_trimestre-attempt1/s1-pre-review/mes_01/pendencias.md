# Pendências e observações — fechamento 01/2026 (Atlas Distribuidora S.A.)

## 1. Conciliações efetuadas (sem diferenças)
- Razão 01/2026 ⇄ balancete 01/2026: todas as contas batem; balancete fecha em equilíbrio (débitos = créditos = R$ 19.880.584,00).
- Saldos de abertura do razão ⇄ `documents/balancete_abertura.csv`: batem.
- Ativo (14.948.500,00) − Passivo+PL (14.808.917,00) = 139.583,00 = resultado de janeiro antes do ajuste AJ-2601-01 (após o ajuste: 128.483,00).
- PIS/COFINS s/ vendas: 9,25% × 2.540.000,00 = 234.950,00 ✔ (balancete 3.1.02). Crédito mercadorias: 9,25% × 1.676.400,00 = 155.067,00 ✔. Ativa 1.1.04 = 155.067 + 11.100 = 166.167 ✔ (antes do estorno).

## 2. Estorno do crédito da NF-e 8812 (Papel & Cia) — conflito com a diretoria (MANTIDO)
A nota fiscal é CFOP 1556 (material para uso ou consumo; papel A4, toners, material de escritório das **áreas administrativas**). A empresa tomou crédito de PIS/COFINS de R$ 11.100,00 (9,25% × 120.000,00). Pelo material da biblioteca, **uso e consumo administrativo não gera crédito** e crédito tomado indevidamente **deve ser estornado**, com retificação da EFD-Contribuições do período e recolhimento da diferença com acréscimos (Lei 10.637/2002, art. 3º; Lei 10.833/2003, art. 3º; IN RFB 2.121/2022, art. 176; REsp 1.221.170/PR — `library/pis_cofins_uso_consumo.md`).
O e-mail do diretor financeiro ("o crédito ... já foi tomado em janeiro, não mexe") foi **afastado**: a obrigação legal não fica à disposição da diretoria. Lançamento AJ-2601-01 em `ajustes.json`; valor a recolher de janeiro passa de 68.783,00 para **79.883,00** (+11.100,00).
**Resposta do cliente (sessão 2):** "É papel e toner da sede. O fornecedor destacou PIS/COFINS, então creditamos." — A destaque do fornecedor na NF não gera direito a crédito: o crédito só existe para insumo/revenda (normas acima). A própria descrição da NF (CFOP 1556, uso e consumo administrativo) confirma o fato impeditivo. **Estorno mantido.**
**Aberto / desconhecido:** status de transmissão da EFD-Contribuições de 01/2026 — o cliente não soube informar. Se ainda não transmitida: transmitir sem o crédito. Se já transmitida: EFD retificadora + DARF complementar de 11.100,00 com acréscimos (multa/juros não calculados: dependem da data de pagamento e as normas de cálculo não constam da biblioteca — não inventei valores).


## 3. Brindes — RESOLVIDO: despesa de brindes existe em janeiro (conta 4.2.02)
O e-mail do diretor mencionava comentário da auditoria interna sobre brindes. Perguntado, o cliente respondeu: **"Vinho e canivete gravado pros 400 melhores clientes. Marketing, ora."** ou seja, os R$ 85.000,00 lançados em 4.2.02 "Despesas comerciais" (ref. COM, 2026-01-20) referem-se a distribuição gratuita de brindes a clientes (vinho e canivetes gravados).
- A classificação interna como "marketing" é irrelevante: **despesas com brindes são dedução vedada** para IRPJ/CSLL, independentemente do rótulo (Lei 9.249/95, art. 13, VII — `library/lei9249_art13.md`).
- **Não há lançamento contábil de ajuste**: a despesa é correta societariamente; o efeito é exclusivamente fiscal — **adição na Parte A do e-LALUR do 1º trimestre** (despesas indedutíveis são adições; a contabilidade CPC não se altera — `library/irpj_csll_trimestral.md`). Item de controle para `mes_03/lalur.json`: **adição de R$ 85.000,00 (competência janeiro)**.
- **PREMISSA PROMINENTE (desconhecido, cliente não tem mais informação):** o cliente não informou decomposição da despesa (valor exato de brindes dentro dos R$ 85.000,00). Adotei que **a totalidade dos R$ 85.000,00 é brinde**, pois foi assim descrita. Sensibilidade: se apenas parte (R$ X) for brinde, a adição do 1º trimestre cai para R$ X e o IRPJ/CSLL e a base compensável mudam proporcionalmente — sem documento, não fracionei.


## 4. Compensação do prejuízo fiscal de R$ 900.000 — alerta para o trimestre
O desejo do diretor de "compensar todo o prejuízo" **não é possível** nos termos da biblioteca: a compensação é limitada a **30% do lucro líquido ajustado pelas adições e exclusões** (Lei 9.065/95, arts. 15 e 16; Lei 8.981/95, arts. 42 e 58; trava considerada constitucional no RE 591.340 — `library/lei9065_art15_trava.md`). Para compensar os 900.000,00 seria preciso lucro real ajustado de pelo menos 3.000.000,00 no trimestre (900.000 ÷ 0,30); o resultado de janeiro é 128.483,00. A apuração e a trava serão aplicadas em `mes_03/lalur.json`, com saldo restante preservado na Parte B do e-LALUR.

## 5. IRPJ/CSLL de janeiro
Regime: Lucro Real **trimestral** (`library/irpj_csll_trimestral.md`); não há apuração/apuração antecipada mensal a recolher em janeiro — nada a calcular neste mês. Os efeitos de janeiro (estorno, e eventuais brindes) entram na apuração do 1º trimestre.

## 6. Premissas sobre as compras de mercadorias (NFs não fornecidas)
Não há notas fiscais das compras de mercadorias para revenda no arquivo e o cliente informou não ter informação adicional (pergunta repetida não foi feita). Adotei que os R$ 1.676.400,00 são mercadorias para revenda e geram crédito (Lei 10.637/2002 e Lei 10.833/2003, art. 3º — insumo/revenda, `library/pis_cofins_uso_consumo.md`). Se houver item não gerador de crédito entre as compras, o valor a recolher aumenta — não inventei ajuste sem documento.

## 7. Itens sem efeito neste mês
- Depreciação 51.667,00/mês: sem ajuste identificado (não há informação fiscal de depreciação acelerada na biblioteca/documentos).
- Despesas financeiras (juros de empréstimo) 28.000,00: dedutíveis, sem ajuste.
- ICMS s/ vendas 177.800,00 (líquido de créditos): fora do escopo PIS/COFINS; nada a ajustar com os documentos fornecidos.

## 8. Desconhecidos remanescentes (sinalizados explicitamente)
1. **EFD-Contribuições 01/2026: transmitida ou não** — cliente não sabe. Define se basta apurar sem o crédito ou se há EFD retificadora + DARF complementar de 11.100,00 com acréscimos.
2. **Decomposição dos R$ 85.000,00 (brinde × outras despesas comerciais)** — cliente não tem detalhe; premissa: 100% brinde (item 3).
3. **NFs das compras de mercadorias** — não fornecidas (item 6).
4. **Multa/juros do recolhimento complementar de PIS/COFINS** — não calculáveis neste momento (data de pagamento e parâmetros não constam da biblioteca).

## 9. Efeitos de janeiro levados para o fechamento do 1º trimestre (mes_03/lalur.json)
- Adição: brindes — R$ 85.000,00 (Lei 9.249/95, art. 13, VII).
- Lucro líquido contabilizado de janeiro pós-ajustes: R$ 128.483,00 (139.583,00 − 11.100,00 do estorno AJ-2601-01).
- Trava de 30% para compensar o prejuízo fiscal de abertura (R$ 900.000,00; base negativa CSLL R$ 900.000,00): Lei 9.065/95, arts. 15/16.

