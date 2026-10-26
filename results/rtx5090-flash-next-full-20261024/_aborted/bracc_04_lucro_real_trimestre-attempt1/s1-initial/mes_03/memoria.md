# MEMORIA — e-LALUR do 1º trimestre/2026 (Lucro Real trimestral) — Atlas Distribuidora S.A.

## 0. Status desta apuração: PRELIMINAR / INCOMPLETA
Só existem registros de **janeiro/2026** em `documents/` (`mes_01/` + abertura). Fevereiro e março não foram fornecidos e o cliente declarou, em **três sessões**, não ter informação adicional (encerramento: `../RELATORIO_FINAL.md`). Os números de `lalur.json` foram apurados **apenas com janeiro** e são **piso**: serão reapurados quando chegarem os registros de fev/mar. **Não usar para recolhimento definitivo.** Nada foi inventado; campos sem dado estão `null` (não zero).

## 1. Lucro líquido contábil (Parte A — ponto de partida)
- Jan/2026 pós-ajustes: **128.483,00** = 139.583,00 (antes de ajustes) − 11.100,00 (AJ-2601-01, estorno do crédito indevido de PIS/COFINS da NF-e 8812, contra custo de materiais).
- Fev + mar/2026: **desconhecidos** (sem razão/balancete) → lucro líquido contábil do trimestre = 128.483,00 + (fev+mar, pendente).

## 2. Adições (Parte A)
### 2.1 Brindes — R$ 85.000,00 (competência janeiro/2026)
- Fato: o cliente confirmou que a conta 4.2.02 "Despesas comerciais" (ref. COM, 2026-01-20, R$ 85.000,00) é a distribuição de brindes ("vinho e canivete gravado pros 400 melhores clientes").
- Direito: **despesas com brindes são dedução vedada** para IRPJ e CSLL (Lei 9.249/95, art. 13, VII — `library/lei9249_art13.md`). As exceções do §2º daquele artigo tratam de doações (cultura, entidades beneficentes/OSCIP, ensino/pesquisa) e **não** alcançam brindes. O rótulo interno de "marketing" é irrelevante: a vedação independe da classificação contábil.
- Tratamento: **adição na Parte A do e-LALUR**, sem ajuste contábil societário — despesas indedutíveis alteram só a apuração fiscal, não a contabilidade CPC (`library/irpj_csll_trimestral.md`).
- **PREMISSA PROEMINENTE:** o cliente não tem a decomposição da despesa; adotei 100% (R$ 85.000,00) como brinde, pois foi assim descrita. Sensibilidade: se apenas R$ X for brinde, a adição cai para X e todo o resto muda proporcionalmente (fórmulas no item 9).
- Fev/mar: provável existência de novas indedutíveis não avaliável — sem documentos (`null` no `lalur.json`, não zero).

## 3. Exclusões (Parte A)
Nenhuma identificada nos documentos do arquivo. Deixado em aberto: receitas excluíveis de fev/mar só serão testadas com os registros.

## 4. Estorno do crédito PIS/COFINS da NF-e 8812 — por que NÃO é adição no lalur
- AJ-2601-01 (D 4.2.04 custos / C 1.1.04 PIS/COFINS a recuperar, 11.100,00) desfaz crédito tomado indevidamente: material de **uso e consumo administrativo** (CFOP 1556) não é insumo/revenda e não gera crédito; o destaque de PIS/COFINS pelo fornecedor na NF não cria direito a crédito (Lei 10.637/2002, art. 3º; Lei 10.833/2003, art. 3º; IN RFB 2.121/2022, art. 176; REsp 1.221.170/PR — `library/pis_cofins_uso_consumo.md`).
- O efeito no IRPJ/CSLL já está embutido no lucro líquido contábil (custo +11.100,00) e é dedutível → nenhuma adição na Parte A.
- Lado PIS/COFINS: a recolher de janeiro = 79.883,00 (234.950,00 débito − 155.067,00 créditos válidos + 11.100,00 estornado) — `mes_01/pis_cofins.json`.

## 5. Compensação de prejuízo fiscal (Parte A) — a trava de 30%
- Saldos de abertura: prejuízo fiscal 900.000,00 e base negativa CSLL 900.000,00 (`documents/saldos_fiscais_abertura.md`).
- O diretor pediu "compensar todo o prejuízo": **juridicamente impossível** — a compensação tem **limite máximo de 30% do lucro líquido ajustado pelas adições e exclusões**, e a mesma trava vale para a base negativa da CSLL (Lei 9.065/95, arts. 15 e 16; Lei 8.981/95, arts. 42 e 58; STF RE 591.340, Tema 117 — `library/lei9065_art15_trava.md`).
- Cálculo preliminar (janeiro apenas):
  - Lucro líquido ajustado = 128.483,00 + 85.000,00 (adições) − 0 (exclusões) = **213.483,00**
  - Trava = 30% × 213.483,00 = **64.044,90** (< saldo de 900.000,00, portanto limitada pela trava)
  - Lucro real = 213.483,00 − 64.044,90 = **149.438,10**
  - CSLL: mesma trava sobre a base ajustada (art. 16) → compensação 64.044,90 e base 149.438,10 (sem adições/exclusões específicas de CSLL nos documentos).

## 6. Apuração preliminar (base janeiro apenas) — aritmética
- IRPJ 15%: 149.438,10 × 15% = 22.415,715 → **22.415,72**
- Adicional de 10% sobre a parcela que exceder R$ 60.000,00 **no trimestre**: 149.438,10 − 60.000,00 = 89.438,10; × 10% = **8.943,81**
- CSLL 9%: 149.438,10 × 9% = 13.449,429 → **13.449,43**
- Fundamento: apuração trimestral no Lucro Real; IRPJ 15% + adicional 10%; CSLL 9%; estrutura Parte A/Parte B do e-LALUR (Lei 9.430/96, arts. 1º e 2º; Lei 9.249/95, art. 3º; IN RFB 1.700/2017, arts. 29 e 310; ECF — IN RFB 2.004/2021 — `library/irpj_csll_trimestral.md`).

## 7. Parte B — controle de saldos a compensar (preliminar)
| Item | Abertura | Compensado (jan apenas) | Saldo final |
|---|---:|---:|---:|
| Prejuízo fiscal | 900.000,00 | 64.044,90 | **835.955,10** |
| Base negativa CSLL | 900.000,00 | 64.044,90 | **835.955,10** |

## 8. Desconhecidos que impedem a apuração definitiva (sinalizados explicitamente)
1. Razão/balancete e documentos de **fev/2026 e mar/2026** — inexistentes no arquivo; cliente sem informação adicional.
2. Status de transmissão da **EFD-Contribuições 01/2026** (define EFD normal vs. retificadora + DARF complementar de 11.100,00 com acréscimos).
3. **Decomposição dos R$ 85.000,00** (brinde × outras despesas comerciais) — premissa 100% brinde.
4. **NFs das compras** de mercadorias de janeiro (crédito de 155.067,00 aceito com base no razão).
5. **Multa/juros** do DARF complementar de PIS/COFINS — parâmetros não constam da biblioteca; não calculei.
6. Brindes/doações, receitas/despesas financeiras, provisões e baixas de fev/mar — desconhecidos.

## 9. Sensibilidade (efeito de fev/mar quando chegarem)
Para cada R$ 1,00 adicional de lucro líquido contábil em fev/mar (sem outras mudanças): lucro ajustado +1,00; compensação +0,30 (trava); lucro real +0,70; IRPJ +0,105; adicional +0,07 (já acima de 60 mil no trimestre); CSLL +0,063. Se fev/mar fecharem no prejuízo, o lucro real do trimestre cai (e a trava/compensação caem junto). As fórmulas são de planejamento; os valores vêm dos registros reais. Tabela completa de cenários (fev+mar de −250.000,00 a +1.000.000,00, com os limiares de zeronamento do IRPJ/CSLL e do adicional) em `../RELATORIO_FINAL.md` §5 — rotulada como cenário, não como fato.

## 10. Pedidos da diretoria — decisão documentada
- "Não mexe no crédito de janeiro" → **afastado**: crédito indevido deve ser estornado (item 4; `library/pis_cofins_uso_consumo.md`).
- "Compensar todo o prejuízo (900.000,00)" → **vedado** pela trava de 30% (item 5; `library/lei9065_art15_trava.md`).
