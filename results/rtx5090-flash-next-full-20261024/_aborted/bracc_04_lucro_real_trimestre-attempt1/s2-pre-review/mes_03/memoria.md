# MEMORIA — e-LALUR do 1º trimestre/2026 (Lucro Real trimestral) — Atlas Distribuidora S.A.

## 0. Status desta apuração: PRELIMINAR / INCOMPLETA (base jan+fev)
Existem registros de **janeiro/2026** (`mes_01/`) e **fevereiro/2026** (`mes_02/`) em `documents/`; os dois meses foram fechados (ver `../mes_01/` e `../mes_02/`). **Março/2026 não existe no arquivo** — e o cliente **confirmou, em duas rodadas (sessões 3 e 6)**, não ter informação adicional sobre os registros de março (`../QUESTIONS.md`, perguntas encerradas) → a apuração do trimestre é **preliminar em caráter definitivo nesta base** e os campos de março estão `null` (não zero). Não usar para recolhimento definitivo nem para escrituração do e-LALUR (livro fiscal — e-LALUR/ECF: IN RFB 2.004/2021, citado em `library/irpj_csll_trimestral.md`). Nada foi inventado.

## 1. Lucro líquido contábil (Parte A — ponto de partida)
- Jan/2026 pós-ajustes: **128.483,00** = 139.583,00 − 11.100,00 (AJ-2601-01, estorno do crédito indevido da NF-e 8812, contra custo de materiais — ainda não escriturado no razão do cliente; a apuração já o considera: ver `../mes_02/pendencias.md` item 5).
- Fev/2026: **193.083,00**, do razão/balancete (receita 2.580.000,00 − PIS/COFINS s/ vendas 238.650,00 − ICMS s/ vendas 180.600,00 − CMV 1.419.000,00 − pessoal 210.000,00 − comerciais 163.000,00 − administrativas 96.000,00 − depreciação 51.667,00 − financeiras 28.000,00), sem ajustes contábeis.
- Mar/2026: **desconhecido** (`null`) → lucro líquido contábil do trimestre ≥ 321.566,00.

## 2. Adições (Parte A) — Lei 9.249/95, art. 13 (`library/lei9249_art13.md`)
### 2.1 Brindes — R$ 85.000,00 (janeiro)
- Fato: conta 4.2.02 (ref. COM, 2026-01-20, R$ 85.000,00) descrita pelo cliente como distribuição de brindes ("vinho e canivete gravado pros 400 melhores clientes").
- Direito: **despesas com brindes são dedução vedada** (art. 13, **VII**). As exceções do § 2º tratam de doações qualificadas e **não** alcançam brindes; o rótulo interno é irrelevante ("independentemente do disposto no art. 47 da Lei 4.506/64" — caput).
- **PREMISSA PROEMINENTE:** sem decomposição da despesa, adotei 100% (85.000,00) como brinde. Sensibilidade no item 9.
### 2.2 Brindes — R$ 48.000,00 (fevereiro — documentado)
- NF-e 4410 (Brindes Prime, 12/02/2026, CFOP 1949): 400 kits-presente (vinho + canivete gravado), campanha "Parceiros Atlas". Mesma vedação do art. 13, VII → adição. Classificação contábil em 4.2.02 mantida (efeito só na apuração — `library/irpj_csll_trimestral.md`).
### 2.3 Doação — R$ 30.000,00 (fevereiro — documentado)
- Doação à Associação Beneficente Luz (18/02/2026). Doações são vedadas pelo art. 13, **VI**, **exceto** as do § 2º: I projetos culturais; II entidades **com utilidade pública federal ou OSCIP** (até 2% do lucro operacional); III ensino/pesquisa (até 1,5%). O recibo registra que a entidade **não tem título de OSCIP nem certificação de utilidade pública federal** → nenhuma exceção se aplica → **indedutível** → adição. (Não há que se falar em limite de 2%: a hipótese do § 2º, II sequer se instala.)
### 2.4 Total jan+fev: 85.000,00 + 48.000,00 + 30.000,00 = **163.000,00**. Março: `null`.

## 3. Exclusões (Parte A)
Nenhuma identificada em jan/fev. Março: só testável com registros.

## 4. Estorno do crédito PIS/COFINS da NF-e 8812 — por que NÃO é adição no lalur
- AJ-2601-01 (D 4.2.04 / C 1.1.04, 11.100,00) desfaz crédito tomado indevidamente: material de **uso e consumo administrativo** (CFOP 1556) não é insumo/revenda e não gera crédito (Lei 10.637/2002, art. 3º; Lei 10.833/2003, art. 3º; IN RFB 2.121/2022, art. 176; REsp 1.221.170/PR — `library/pis_cofins_uso_consumo.md`).
- O efeito no IRPJ/CSLL já está embutido no lucro líquido (custo +11.100,00) e é dedutível → nenhuma adição na Parte A.
- Lado PIS/COFINS: a recolher jan = 79.883,00; fev = 81.141,00 (sem estornos) — `../mes_01/pis_cofins.json`, `../mes_02/pis_cofins.json`.

## 5. Compensação de prejuízo fiscal (Parte A) — a trava de 30%
- Saldos de abertura: prejuízo fiscal 900.000,00 e base negativa CSLL 900.000,00 (`documents/saldos_fiscais_abertura.md`).
- O diretor pediu "compensar todo o prejuízo": **juridicamente impossível** — limite máximo de compensação de **30% do lucro líquido ajustado pelas adições e exclusões**; mesma trava para a CSLL (Lei 9.065/95, arts. 15 e 16; Lei 8.981/95, arts. 42 e 58; STF RE 591.340, Tema 117 — `library/lei9065_art15_trava.md`).
- Cálculo preliminar (jan+fev):
  - Lucro líquido ajustado = 321.566,00 + 163.000,00 (adições) − 0 = **484.566,00**
  - Trava = 30% × 484.566,00 = **145.369,80** (saldo de 900.000,00 não é o limitante — só o seria com ajustado > 3.000.000,00)
  - Lucro real = 484.566,00 − 145.369,80 = **339.196,20**
  - CSLL: mesma trava sobre a base ajustada (art. 16) → compensação idêntica de 145.369,80; sem adições/exclusões específicas de CSLL nos documentos.

## 6. Apuração preliminar (jan+fev) — aritmética
- IRPJ 15%: 339.196,20 × 15% = **50.879,43**
- Adicional de 10% sobre a parcela que exceder R$ 60.000,00 **no trimestre**: 339.196,20 − 60.000,00 = 279.196,20; × 10% = **27.919,62** (IRPJ total = 78.799,05)
- CSLL 9%: 339.196,20 × 9% = 30.527,658 → **30.527,66**
- Fundamento: apuração trimestral no Lucro Real; IRPJ 15% + adicional 10%; CSLL 9%; Parte A/Parte B do e-LALUR (Lei 9.430/96, arts. 1º e 2º; Lei 9.249/95, art. 3º; IN RFB 1.700/2017, arts. 29 e 310; ECF — IN RFB 2.004/2021 — `library/irpj_csll_trimestral.md`).
- **Piso**: valores só crescem com março (exceto se março der prejuízo).

## 7. Parte B — controle de saldos a compensar (preliminar)
| Item | Abertura | Compensado (jan+fev) | Saldo final preliminar |
|---|---:|---:|---:|
| Prejuízo fiscal | 900.000,00 | 145.369,80 | **754.630,20** |
| Base negativa CSLL | 900.000,00 | 145.369,80 | **754.630,20** |

## 8. Desconhecidos que impedem a apuração DEFINITIVA (sinalizados explicitamente)
1. Razão/balancete e documentos de **março/2026** — inexistentes em `documents/` (único mês faltante).
2. Status de transmissão das **EFD-Contribuições de jan e fev** (define EFD normal vs. retificadora + DARF complementar de 11.100,00 com acréscimos).
3. **Escrituração da AJ-2601-01** no razão do cliente (saldo 1.1.04 em fev ainda contém os 11.100,00).
4. **Decomposição dos R$ 85.000,00 de 4.2.02 de janeiro** (premissa 100% brinde; a de fevereiro está documentada).
5. **NFs das compras** de mercadorias de jan/fev (créditos de 155.067,00 e 157.509,00 aceitos com base no razão).
6. **Acréscimos (mora)** dos DARFs em aberto (jan 79.883,00; fev 81.141,00) — parâmetros não constam da biblioteca; não calculados.

## 9. Sensibilidade (efeito de março quando chegar)
Jan/fev estão fechados — só resta a variável de março. Para cada R$ 1,00 de lucro contábil de março (sem novas indedutíveis/exclusões): ajustado +1,00; compensação +0,30 (trava); lucro real +0,70; IRPJ +0,105; adicional +0,07 (o trimestre já passa de 60 mil); CSLL +0,063. Limiares: adicional zera se ajustado ≤ 85.714,29 (março ≤ −398.851,71); lucro real zera se ajustado ≤ 0 (março ≤ −484.566,00, com as adições de jan+fev ainda somando); a trava de 30% passa a consumir o saldo integral de 900.000,00 quando ajustado > 3.000.000,00 (março > 2.515.434,00). Tabela de cenários em `../RELATORIO_FINAL.md` §5 — rotulada como cenário, não como fato.

## 10. Pedidos da diretoria e auditoria — decisão documentada
- "Não mexe no crédito de janeiro" → **afastado**: crédito indevido deve ser estornado (item 4; `library/pis_cofins_uso_consumo.md`).
- "Compensar todo o prejuízo (900.000,00)" → **vedado** pela trava de 30% (item 5; `library/lei9065_art15_trava.md`).
- "Brinde é despesa comercial, sempre foi" → correto no plano societário (classificação mantida), **sem efeito** contra a vedação fiscal do art. 13, VII (item 2).
- Dispensa da auditoria interna (brindes acima do padrão + doação) → observação **procedente quanto aos reflexos fiscais** (adições de 48.000,00 e 30.000,00 reconhecidas; item 2.2/2.3 e `../mes_02/pendencias.md` item 4).
