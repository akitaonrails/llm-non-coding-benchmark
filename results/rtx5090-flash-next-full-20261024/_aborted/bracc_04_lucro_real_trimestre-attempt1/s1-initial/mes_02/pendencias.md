# PENDÊNCIAS — 02/2026 (Atlas Distribuidora S.A.)

## 1. Status do mês: BLOQUEADO — não fechado
Não existem em `documents/` balancete, razão ou quaisquer documentos de **fevereiro/2026** (o arquivo contém apenas `mes_01/` + abertura). Em **três sessões sucessivas** o cliente declarou **não ter informação adicional** — inclusive sobre a existência dos registros.
Por isso, `ajustes.json` e `pis_cofins.json` deste mês foram gravados como marcadores **BLOQUEADO**, com valores `null` — fevereiro **não** foi apurado como "zero": zerar sem registros seria inventar fato (contrato: não inventar fatos; não reportar completo se falta entregável).

## 2. Como destravar
Entregues em `documents/mes_02/`: balancete + razão de 02/2026 e documentos de suporte (NFs de vendas/compras, EFD-Contribuições, folha, depreciacão, brindes/marketing, juros). Alternativas aceitas, com premissas sinalizadas: livros fiscais, extratos bancários, relatórios gerenciais com receita/custo detalhados. O pedido formal foi feito e encerrado: o cliente não tem informação adicional (`deliverable/QUESTIONS.md`, sem perguntas pendentes) — o mês permanece nesta condição até que registros sejam fornecidos; ver `../RELATORIO_FINAL.md`.

## 3. Procedimento pronto para quando os registros chegarem
1. Conciliar razão ⇄ balancete de fev e balancete de fev ⇄ posição de janeiro (fechamento de 01/2026 como abertura).
2. PIS/COFINS não cumulativo (alíquota 9,25% aplicada nos documentos de janeiro): débito sobre receita; créditos apenas de insumo/revenda; **testar todo material de uso e consumo administrativo — não gera crédito; se tomado, estornar e retificar** (Lei 10.637/2002, art. 3º; Lei 10.833/2003, art. 3º; IN RFB 2.121/2022, art. 176; REsp 1.221.170/PR — `library/pis_cofins_uso_consumo.md`; cf. AJ-2601-01 de janeiro).
3. Identificar brindes, doações e demais despesas indedutíveis de fev para **adições no e-LALUR do 1º trimestre** (Lei 9.249/95, art. 13, VI/VII — `library/lei9249_art13.md`).
4. Verificar reflexos de janeiro em aberto: DARF de 79.883,00 e situação da EFD-Contribuições 01/2026 (normal vs. retificadora + DARF complementar de 11.100,00 com acréscimos) — `mes_01/pendencias.md`, item 8.

## 4. Herança conhecida para a apuração do trimestre
- Lucro líquido contábil de janeiro pós-ajustes: 128.483,00 (será somado a fev/mar quando existirem).
- Adição de brindes de janeiro: 85.000,00 (premissa: 100% da conta 4.2.02).
- Trava de 30% para compensar o prejuízo fiscal (900.000,00) e a base negativa da CSLL (900.000,00): Lei 9.065/95, arts. 15/16 — `library/lei9065_art15_trava.md`. O pedido do diretor de compensar tudo é vedado.
- Apuração de IRPJ/CSLL é **trimestral** (fechada em `mes_03/`), não mensal — `library/irpj_csll_trimestral.md`.
