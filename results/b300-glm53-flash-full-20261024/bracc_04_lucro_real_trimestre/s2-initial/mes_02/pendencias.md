# Pendências — mês 02/2026 (Atlas Distribuidora S.A.)

## 1. Retificação de janeiro não contabilizada pelo cliente — A-2026-01-01 repetida em fevereiro

- **Fato detectado por conferência aritmética:** o balancete de fev/2026 (cumulativo jan+fev) traz
  1.1.04 (Tributos a recuperar) = **323.676,00** = 155.067,00 (créditos válidos de jan) +
  **11.100,00 (crédito indevido NF 8812, ainda embutido)** + 157.509,00 (créditos válidos de fev).
  Prova de que o lançamento A-2026-01-01 (estorno: Dr 3.1.02 / Cr 1.1.04 — `deliverable/mes_01/ajustes.json`)
  **não foi postado** nos livros do cliente entre os fechamentos.
- **Tratamento:** o ajuste é repetido em `deliverable/mes_02/ajustes.json` (A-2026-02-01) como
  **retificação de lançamento do mês anterior**, conforme o contrato ("incluindo retificações de meses
  anteriores se necessário"). Fundamento inalterado: `library/pis_cofins_uso_consumo.md` — material de
  uso e consumo administrativo não é insumo; crédito tomado indevidamente deve ser estornado.
- **Efeito:** 1.1.04 passa de 323.676,00 para **312.576,00**; lucro líquido cumulativo jan+fev passa de
  332.666,00 para **321.566,00**. A apuração isolada de fev/2026 (LL 193.083,00) não é alterada por
  este lançamento, pois o efeito pertence a janeiro.
- **Pendência operacional:** o cliente precisa postar o ajuste nos livros (uma vez; o A-2026-02-01 é a
  mesma partida). Pergunta de processo registrada em `deliverable/QUESTIONS.md`.

## 2. Brindes NF 4410 — R$ 48.000,00 (adição fiscal do trimestre; quantificação da incógnita de janeiro)

- **Fato:** NF-e 4410 (Brindes Prime Ltda, 12/02/2026): **400 kits-presente (vinho + canivete gravado)
  para clientes — campanha 'Parceiros Atlas' — R$ 48.000,00**, CFOP 1949. Contabilizado como despesas
  comerciais (razão 12/02: Dr 4.2.02 48.000,00 / Cr 1.1.01; cf. relatório da auditoria interna sobre
  "R$ 48 mil em um único fornecedor").
- **Confere com a resposta do cliente (rodada 2)**: "vinho e canivete gravado pros 400 melhores
  clientes" — a incógnita de valor pendente desde janeiro fica **resolvida: R$ 48.000,00**, registrado
  em **fevereiro/2026** (em janeiro não há nenhum lançamento de brinde nos documentos).
- **Tratamento fiscal:** **adição de R$ 48.000,00 na Parte A** do e-LALUR do 1º trimestre —
  `library/lei9249_art13.md` (Lei 9.249/95, art. 13, VII: vedadas as deduções de despesas com brindes).
  O argumento "marketing" do cliente/diretor não altera o resultado conforme a mesma biblioteca: as
  exceções do § 2º cabem a **doações** tipificadas, não a brindes, e nenhuma exceção a brindes existe
  no texto. Classificação contábil como despesa comercial permanece — a biblioteca orienta que a
  despesa indedutível vira adição **sem mudar a contabilidade societária**
  (`library/irpj_csll_trimestral.md`).
- Consequência praticável: **nenhum lançamento em fev/2026**; a adição soma R$ 48.000,00 aos R$ 30.000,00
  da doação = **R$ 78.000,00 de adições identificadas até fevereiro** (item 4).

## 3. Doação R$ 30.000,00 — Associação Beneficente Luz (adição fiscal; sem enquadramento no § 2º)

- **Fato:** doação de R$ 30.000,00 em 18/02/2026, contabilizada como despesa comercial (razão: Dr 4.2.02 /
  Cr 1.1.01); recibo da entidade — CNPJ regular, associação civil sem fins lucrativos registrada em
  cartório.
- **Tratamento fiscal:** **adição de R$ 30.000,00 na Parte A** — `library/lei9249_art13.md`
  (art. 13, VI: doações vedadas "exceto as referidas no § 2º"). O § 2º, II deduz doações a entidades
  civis sem fins lucrativos que prestem serviços gratuitos a empregados/comunidade **e que sejam
  reconhecidas de utilidade pública federal ou qualificadas como OSCIP** (limite: 2% do lucro
  operacional). O recibo é explícito: a entidade **"não possui título de OSCIP nem certificação de
  utilidade pública federal"** — não preenche a condição da própria regra, logo não entra no § 2º e o
  limite de 2% nem se analisa.
- **Nota honesta:** a natureza dos serviços da entidade (empregados/comunidade) não veio detalhada nos
  documentos; decidimos pelo critério objetivo do recibo (ausência de OSCIP/utilidade pública),
  suficiente por si só para vedação conforme o texto em vigor.
- **Reclassificação contábil:** a auditoria interna recomendou "verificar a adequação da classificação
  contábil". Reclassificar a doação para conta própria (sair de 4.2.02) melhoraria a rastreabilidade,
  mas: (i) nenhum quadro de contas existe na biblioteca/workspace; (ii) o tratamento fiscal é idêntico
  por qualquer conta; (iii) a introdução de conta nova é decisão do cliente. **Recomendação registrada,
  não implementada** — o efeito no lucro é nulo (despesa permanece a mesma).

## 4. PIS/COFINS fev/2026 — apuração limpa; complemento de janeiro é separado

- Débitos: 9,25% × 2.580.000,00 = **238.650,00** ✓ (razão e balancete).
- Créditos: compras mercadorias p/ revenda 15/02: 9,25% × 1.702.800,00 = **157.509,00** ✓ — 
  único crédito do mês, **válido** (insumo/revenda), nenhum crédito de uso e consumo no mês.
- **a_recolher = 238.650,00 − 157.509,00 + 0,00 = 81.141,00** (`deliverable/mes_02/pis_cofins.json`).
- **Não incluído aqui:** o complemento de **R$ 11.100,00** pertence à retificação da EFD de jan/2026
  (com acréscimos, hoje ainda não calculados — ver `deliverable/mes_01/pendencias.md` item 4 e §5);
  misturá-lo na apuração de fev desfiguraria ambas as obrigações. Dualidade documentada:
  (i) obrigação fiscal de jan (11.100 + acréscimos); (ii) obrigação de fev (81.141,00).

## 5. Painel do trimestre — estado até fevereiro (apuração definitiva é da sessão 3)

- Lucro líquido cumulativo jan+fev: contábil 332.666,00; **após retificação (estorno 11.100,00):
  321.566,00** (jan 128.483,00 + fev 193.083,00 isolado).
- Adições identificadas até fev: brindes 48.000,00 (art. 13, VII) + doação 30.000,00 (art. 13, VI) =
  **78.000,00**. Exclusões conhecidas: **nenhuma** até agora.
- Prévia LLA (só para painel, não fechada): 321.566,00 + 78.000,00 = **399.566,00** → trava 30%
  = 119.869,80 compensáveis no máximo — se a suposição "prejuízo integralmente pós-1995" for correta
  (`library/lei9065_art15_trava.md`; Lei 9.065/95, art. 15 e 16; STF RE 591.340, Tema 117). Pedido do
  diretor de "compensar todo" (900.000,00) continua impossível neste trimestre.
  **Nada disso está fixado**: dados de março podem mudar adições/exclusões e o LLA; a apuração é
  entregue em `deliverable/mes_03/`.
- **Pendências herdadas:** acréscimos do complemento (sem taxa/data), quitação do complemento,
  parcelamento pós-1995 (suposição assumida) — todas em `deliverable/QUESTIONS.md`.

## 6. Documentos recebidos nesta sessão (fev/2026) e conferências (Python, nada forçado a balançar)

- **Documentos:** `balancete.csv`, `razao.csv`, `nf_4410_brindes_prime.md`, `recibo_doacao_luz.md`,
  `relatorio_auditoria_interna.md` — sessão 2 desbloqueada.
- **Balancete 02/2026 (cumulativo):** débitos 23.299.010,00 = créditos 23.299.010,00 ✓.
- **Reconstrução do razão (partindo dos saldos de jan):** caixa 3.094.800,00 ✓; estoques 4.973.200,00 ✓;
  clientes 3.920.000,00 ✓; fornecedores 3.593.676,00 ✓; obrigações trabalhistas 1.030.000,00 ✓;
  tributos a recolher 1.572.000,00 ✓; depreciação acumulada 2.583.334,00 ✓; tributos a recuperar
  323.676,00 ✓; despesas comerciais 248.000,00 ✓ (= 85.000 jan + 48.000 brindes + 30.000 doação +
  85.000 ordinárias fev).
- **Taxas:** PIS/COFINS 9,25% × 2.580.000,00 = 238.650,00 ✓; ICMS 7% × 2.580.000,00 = 180.600,00 ✓;
  crédito compras 9,25% × 1.702.800,00 = 157.509,00 ✓.
- **DRE:** LL fev isolado **193.083,00**; cumulativo jan+fev nos livros 332.666,00;
  após lançamentos de ajuste (estorno 11.100,00) **321.566,00**.
- Despesa comercial fev 163.000,00 detalhada no razão: 48.000 (NF 4410) + 30.000 (doação) + 85.000
  (ordinárias) ✓ — tudo conferido; nenhuma divergência restante entre razão e balancete.

## 7. Sem outras matérias no mês

- A revisão exaustiva da documentação de fevereiro não revelou outras matérias: sem novos créditos
  de uso e consumo, sem exclusões do e-LALUR identificadas (juros são regulares e dedutíveis;
  nenhuma receita de exclusão consta), sem dividendos ou distribuições. A apuração IRPJ/CSLL final
  (com e-LALUR) é da sessão 3; para tanto o **pacote de documentos de março** precisa ser entregue
  (pedido em `deliverable/QUESTIONS.md`).
