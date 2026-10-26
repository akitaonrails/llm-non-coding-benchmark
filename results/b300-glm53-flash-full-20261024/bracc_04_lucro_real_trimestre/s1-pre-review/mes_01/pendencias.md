# Pendências — mês 01/2026 (Atlas Distribuidora S.A.)

## 1. Correção confirmada: estorno do crédito PIS/COFINS da NF 8812 — R$ 11.100,00

- **Fato:** NF-e 8812 (Papel & Cia, 09/01/2026), R$ 120.000,00 de material de uso e consumo de
  áreas administrativas (CFOP 1556). Crédito de 9,25% × 120.000,00 = **R$ 11.100,00** foi tomado
  (razão, ref. NF8812, Dr 1.1.04) e está no balancete (1.1.04 = 166.167,00 = 155.067,00 válidos + 11.100,00 indevido).
- **Tratamento:** material de uso e consumo de área administrativa **não é insumo e não gera crédito**
  nos regimes não cumulativos — `library/pis_cofins_uso_consumo.md` (Lei 10.637/2002, art. 3º;
  Lei 10.833/2003, art. 3º; IN RFB 2.121/2022, art. 176; REsp 1.221.170/PR).
- **Lançamento de ajuste:** Dr 3.1.02 (−) PIS/COFINS sobre vendas 11.100,00 / Cr 1.1.04 11.100,00
  (`deliverable/mes_01/ajustes.json`, A-2026-01-01). Saldo 1.1.04 passa a 155.067,00.
- **Obrigação consolidada PIS/COFINS jan/2026:** débitos 234.950,00 − créditos tomados 166.167,00
  + estorno 11.100,00 = **79.883,00 a recolher** (conferência: 234.950,00 − 155.067,00 = 79.883,00).
  O crédito de 155.067,00 sobre compras de mercadorias para revenda é **válido e preservado**
  (mesma biblioteca: insumo/revenda gera crédito).
- **Não feito aqui (pendente):** acréscimos do complemento (multa/juros). As taxas não constam da
  biblioteca e a data de transmissão da EFD original não foi informada — ver item 4 e QUESTIONS.md.
- **Conflito de instrução registrado:** o diretor financeiro mandou "não mexer" no crédito. A biblioteca
  é a autoridade única do engajamento (CONTRACT.md) e determina estorno com retificação e recolhimento
  da diferença com acréscimos. Instrução do cliente não prevalece sobre o ajuste; encaminhado em
  QUESTIONS.md para que o cliente decida formalmente como elevar.

## 2. Brindes — adição fiscal pendente de quantificação (efeito no trimestre)

- A auditoria interna comentou gastos com **brindes**; o diretor afirma que "é só comentário, não é erro".
  A biblioteca discorda do diretor: `library/lei9249_art13.md` (Lei 9.249/95, art. 13, VII) veda a dedução
  de despesas com brindes — a despesa é registrada contabilmente como comercial (tratamento societário
  correto, que **não se altera**: `library/irpj_csll_trimestral.md`), mas exige **adição** na Parte A do
  e-LALUR do 1º trimestre (`deliverable/mes_03/lalur.json`).
- **Resposta do cliente (rodada 2):** são cestas de **vinho + canivete gravado para os 400 melhores
  clientes**, contabilizadas como comercial ("marketing, ora").
- **Pendência:** o cliente confirma a existência dos brindes, mas **não informou o valor** — nenhum
  documento quantifica (balancete: "Despesas comerciais 85.000,00" sem detalhamento; razão: "Despesas
  comerciais ordinárias"). O argumento "marketing" não muda o fim fiscal conforme a mesma biblioteca:
  o art. 13, VII, veda a dedução de despesas com brindes e o § 2º excepciona apenas doações tipificadas
  (projetos culturais; entidades sem fins lucrativos a serviço de empregados/comunidade ou OSCIP;
  ensino/pesquisa) — nenhuma se aplica. Sem o valor, a adição segue **incalculável**; incógnita
  registrada em QUESTIONS.md; se os documentos de fev/mar detalharem os lançamentos de brindes,
  quantifica-se nessa sessão.

## 3. Compensação do prejuízo fiscal — trava de 30% (efeito no trimestre)

- O cliente pediu "compensar todo o prejuízo" (R$ 900.000,00). A biblioteca limita a compensação a
  **30% do lucro líquido ajustado** — `library/lei9065_art15_trava.md` (Lei 9.065/95, arts. 15 e 16;
  Lei 8.981/95, arts. 42 e 58), igualmente para a base negativa de CSLL (art. 16), e declara a trava
  constitucional (STF, RE 591.340, Tema 117).
- Aritmética: para absorver 900.000,00 integralmente, o lucro líquido ajustado do trimestre precisaria
  ser ≥ 900.000,00 / 0,30 = **3.000.000,00**. Só jan/2026 dá lucro contábil de 128.483,00 (após ajuste),
  portanto o trimestre precisaria de lucro bem maior em fev/mar. A apuração efetiva pertence ao mês 03
  (`deliverable/mes_03/`). Compensação parcial é a saída pela biblioteca.
- **Resposta do cliente (rodada 2):** nenhuma informação adicional sobre o parcelamento. **Suposição
  adotada e destacada:** todas as parcelas foram apuradas a partir de 1º/01/1995 (o saldos informados
  referem-se à ECF de 31/12/2025), logo a trava de 30% se aplica à integralidade dos 900.000,00.
  Se existir parcela anterior a 1995, o tratamento seria diferente — incógnita registrada em QUESTIONS.md.

## 4. Acréscimos do complemento PIS/COFINS (jan/2026)

- Principal: 11.100,00. Multa e juros são exigíveis pela mesma biblioteca ("recolhimento da diferença
  com acréscimos"), mas: (a) as taxas/índices não estão na biblioteca; (b) a data de transmissão da
  EFD original de jan/2026 não foi informada. **Valor de acréscimos não calculável neste engajamento** —
  ver QUESTIONS.md. Nada foi forçado a fechar.

## 5. Registro das respostas do cliente (rodada 2) e seus efeitos

1. **Brindes** — existencia confirmada (cestas de vinho + canivete gravado, 400 melhores clientes,
   contabilizadas como despesa comercial). Valor **não informado** → adição art. 13, VII segue
   incalculável (ver item 2). Argumento "marketing" sem amparo na biblioteca.
2. **Crédito NF 8812 (R$ 11.100,00)** — justificativa do cliente: "o fornecedor destacou PIS/COFINS,
   então creditamos". A biblioteca condiciona o crédito ao **uso do bem pelo adquirente** (insumo na
   produção/revenda) e nega crédito a material de uso e consumo administrativo —
   `library/pis_cofins_uso_consumo.md`. Nota honesta: a biblioteca **não traz regra específica** sobre o
   destaque do fornecedor como hipótese de crédito; a regra operante (uso do bem) não depende do
   destaque e continua afastando o crédito. **Estorno A-2026-01-01 mantido**; divergência documentada;
   nenhuma instrução formal do cliente para reverter o ajuste foi recebida.
3. **Parcelamento do prejuízo (pós-1995?)** — sem informação do cliente; suposição todas-post-1995
   assumida e destacada (ver item 3).
4. **EFD original de 01/2026 (data de transmissão), índices de acréscimos e quitação** — sem informação;
   complemento segue no valor principal de 11.100,00, tratado como obrigação da Atlas a quitar
   (ver item 4 e §1). Índices não estão na biblioteca — permanece incalculável.
5. **Documentos de fev/2026 e do trimestre** — **não recebidos**; solicitados em QUESTIONS.md.
   Até a entrega, a sessão 2 (fechamento de fevereiro) está **bloqueada**.

## 6. Conferências feitas (Python, nada forçado a balançar)

- Balancete 01/2026: débitos 19.880.584,00 = créditos 19.880.584,00 ✓.
- Reconstrução do razão: estoques 4.689.400,00 ✓; caixa 2.504.600,00 ✓; clientes 3.920.000,00 ✓;
  fornecedores 3.436.167,00 ✓; obrigações trabalhistas 820.000,00 ✓; tributos a recolher
  1.152.750,00 ✓; depreciação acumulada 2.531.667,00 ✓; tributos a recuperar 166.167,00 ✓.
- Taxas: PIS/COFINS 9,25% × 2.540.000,00 = 234.950,00 ✓; ICMS 7% × 2.540.000,00 = 177.800,00 ✓;
  crédito compras 9,25% × 1.676.400,00 = 155.067,00 ✓; crédito NF 8812 9,25% × 120.000,00 = 11.100,00 ✓.
- Lucro líquido contábil jan/2026: antes do ajuste 139.583,00; após estorno **128.483,00**
  (a composição item a item está em `deliverable/mes_01/ajustes.json` → efeito, e na apuração do mês 03).
- O prejuízo fiscal de 900.000,00 (Parte B) não aparece no balancete societário ("Reservas / lucros
  acumulados 2.000.000,00"): coexistência normal entre base fiscal (e-LALUR, Parte B) e patrimônio
  contábil; nenhum lançamento exigido em janeiro pela biblioteca disponível.
