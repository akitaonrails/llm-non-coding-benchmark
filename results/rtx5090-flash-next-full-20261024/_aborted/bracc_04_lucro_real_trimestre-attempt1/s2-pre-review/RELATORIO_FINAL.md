# RELATÓRIO FINAL — engajamento Controller — Atlas Distribuidora S.A., 1º trimestre/2026

> **Documento vivo — sessão 6 (encerramento definitivo nesta base documental).** Esta versão **substitui** o relatório da sessão 5: o cliente foi perguntado novamente sobre os registros de **março/2026** e sobre o status de transmissão das EFD-Contribuições de jan/fev e respondeu que **não tem informação adicional** (2ª confirmação — a 1ª foi na sessão 3). As duas perguntas foram encerradas em `QUESTIONS.md`. Status do engajamento: **BLOCKED em caráter definitivo nesta base** — os entregáveis de `mes_03/` (mês) foram lavrados como marcadores **BLOQUEADO** e o e-LALUR do trimestre permanece **PRELIMINAR jan+fev** (piso firme). Nada será inventado. (Justificativa e itens firmes em `STATUS.md`.)

## 1. Base documental e o que falta

| Mês | Registros em `documents/` | Status do fechamento |
|---|---|---|
| 01/2026 | razão, balancete, NF-e 8812, balancete de abertura, saldos fiscais | **FECHADO** — `deliverable/mes_01/` |
| 02/2026 | razão, balancete **acumulado** (jan+fev), NF-e 4410 (brindes), recibo de doação, relatório de auditoria interna | **FECHADO** — `deliverable/mes_02/` |
| 03/2026 | **inexistentes — cliente confirmou (sessões 3 e 6) que não possui** | **BLOQUEADO** — entregáveis lavrados como marcadores BLOQUEADO; única causa remanescente |

Conciliação verificada por script (Python): abertura + razão jan (excluídas linhas ABERT) + razão fev reproduzem o balancete acumulado de fev em **22/22 contas, zero divergência**; balancete fecha em equilíbrio (**23.299.010,00 = 23.299.010,00**). Passos e exemplos em `mes_02/pendencias.md` §1.

## 2. Janeiro/2026 (firme — não reaberto)

- PIS/COFINS (não cumulativo, 9,25%): receita 2.540.000,00 → débito **234.950,00**; créditos contábeis 166.167,00; **estorno 11.100,00** da NF-e 8812 (papelaria/toners administrativos, CFOP 1556 — uso e consumo não gera crédito: Lei 10.637/2002 art. 3º; Lei 10.833/2003 art. 3º; IN RFB 2.121/2022 art. 176; REsp 1.221.170/PR — `library/pis_cofins_uso_consumo.md`); créditos válidos 155.067,00; **a recolher 79.883,00**.
- Ajuste **AJ-2601-01** (D 4.2.04 11.100,00 / C 1.1.04 11.100,00, data 31/01/2026) — **o cliente ainda não o escriturou** (evidência: 1.1.04 = 323.676,00 no balancete de fev; deveria ser 312.576,00). Reiterado em `mes_02/ajustes.json`.
- Lucro contábil pós-ajuste: **128.483,00**. Premissa proeminente: 4.2.02 de janeiro (85.000,00) = 100% brindes.

## 3. Fevereiro/2026 (fechado nesta base)

- PIS/COFINS: receita 2.580.000,00 → débito **238.650,00**; créditos válidos 9,25% × 1.702.800,00 = **157.509,00**; **estornos 0,00** (na NF-e 4410 a empresa nunca tomou crédito); **a recolher 81.141,00**. Amarração: 1.1.04 fev = 166.167,00 + 157.509,00 = 323.676,00 ✓.
- **NF-e 4410 — brindes (48.000,00)**: 400 kits-presente (vinho + canivete) a clientes, CFOP 1949, lançado em 4.2.02. Classificação contábil correta e mantida; para IRPJ/CSLL é **dedução vedada** (Lei 9.249/95, art. 13, **VII** — `library/lei9249_art13.md`) → **adição no e-LALUR**, sem lançamento contábil.
- **Doação Associação Luz (30.000,00)**: entidade sem título de utilidade pública federal nem OSCIP → exceção do § 2º do art. 13 inaplicável → **indedutível** → **adição** (art. 13, VI).
- Lucro contábil de fevereiro: **193.083,00**; acumulado jan+fev (pós-AJ-2601-01): **321.566,00**.
- Auditoria interna (brindes acima do padrão + doação): **procedente quanto aos reflexos fiscais**; a observação não foi dispensada.

## 4. Apuração do 1º trimestre — PRELIMINAR (jan+fev; março `null`)

**Não usar para recolhimento nem para escrituração definitiva do e-LALUR** (livro fiscal — IN RFB 2.004/2021). Valores de março faltantes estão como `null`, nunca zero.

| Linha | Valor (R$) |
|---|---:|
| Lucro líquido contábil (jan 128.483,00 + fev 193.083,00) | 321.566,00 |
| Adições — brindes jan 85.000,00 + brindes fev 48.000,00 + doação fev 30.000,00 | 163.000,00 |
| Lucro líquido ajustado (antes da compensação) | 484.566,00 |
| Compensação de prejuízo — **trava de 30%** (Lei 9.065/95, arts. 15-16; RE 591.340 — `library/lei9065_art15_trava.md`) | 145.369,80 |
| **Lucro real** | **339.196,20** |
| IRPJ 15% | 50.879,43 |
| Adicional de 10% (excedente a 60.000,00 no trimestre — Lei 9.430/96 — `library/irpj_csll_trimestral.md`) | 27.919,62 |
| CSLL 9% | 30.527,66 |
| Parte B — prejuízo fiscal / base negativa CSLL: 900.000,00 − 145.369,80 | **754.630,20** cada |

O saldo de 900.000,00 **não** é o limitante nesta faixa: a trava só o consumiria integralmente com ajustado acima de 3.000.000,00.

## 5. Sensibilidade — cenários com **março** como única variável

Jan e fev estão fechados (piso fixo de 321.566,00 de lucro e 163.000,00 de adições). **O cliente confirmou (sessão 6) que não possui os registros de março — os cenários abaixo são a moldura completa do que se pode afirmar nesta base, não uma etapa pendente do fechamento.** Cada R$ 1,00 de lucro contábil de março: ajustado +1,00 → compensação +0,30 → lucro real +0,70 → IRPJ +0,105, adicional +0,07, CSLL +0,063. **Premissa de cenário:** março sem novas indedutíveis nem exclusões.

| Lucro contábil mar/2026 (R$) | Ajustado trim. | Compensado (30%) | Lucro real | IRPJ total (15%+adic.) | CSLL 9% |
|---:|---:|---:|---:|---:|---:|
| −700.000,00 | −215.434,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| −484.566,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| −300.000,00 | 184.566,00 | 55.369,80 | 129.196,20 | 26.299,05 | 11.627,66 |
| 0,00 (piso atual) | 484.566,00 | 145.369,80 | 339.196,20 | 78.799,05 | 30.527,66 |
| +193.083,00 (repete fev) | 677.649,00 | 203.294,70 | 474.354,30 | 112.588,58 | 42.691,89 |
| +500.000,00 | 984.566,00 | 295.369,80 | 689.196,20 | 166.299,05 | 62.027,66 |
| +1.000.000,00 | 1.484.566,00 | 445.369,80 | 1.039.196,20 | 253.799,05 | 93.527,66 |
| +2.515.434,00 (trava atinge o saldo) | 3.000.000,00 | 900.000,00 | 2.100.000,00 | 519.000,00 | 189.000,00 |

Limiares: **adicional zera** se o ajustado ≤ 85.714,29 (março ≤ −398.851,71); **lucro real zera** se ajustado ≤ 0 (março ≤ −484.566,00 — as adições de jan+fev ainda somam); a **trava de 30% consome o saldo integral** de 900.000,00 quando ajustado > 3.000.000,00 (março > 2.515.434,00). Nota: para março entre −484.566,00 e −321.566,00 o lucro contábil do trimestre é negativo mas o **ajustado** (com as adições) é positivo — a compensação incide sobre o ajustado (Lei 9.065/95, art. 15); as linhas acima evitam essa faixa para não misturar cenários.

## 6. Diretivas da diretoria e auditoria — decisão documentada

| Pedido da diretoria | Decisão | Fundamento |
|---|---|---|
| "Não mexe no crédito de janeiro" (NF 8812) | **Afastado** — estorno AJ-2601-01 mantido (ainda não escriturado pelo cliente) | `library/pis_cofins_uso_consumo.md` |
| "Compensar todo o prejuízo (900.000,00)" | **Vedado** — trava de 30% do ajustado; compensação máxima 145.369,80 no piso atual | `library/lei9065_art15_trava.md` |
| "Brinde é despesa comercial, sempre foi" | Contabilmente correto (4.2.02 mantido), **sem efeito** contra a vedação fiscal → adição devida | `library/lei9249_art13.md` art. 13, VII; `library/irpj_csll_trimestral.md` |
| Dispensar a observação da auditoria interna | **Não aceito** — observação procedente quanto aos reflexos fiscais (adições de 48.000,00 e 30.000,00) | idem + `mes_02/pendencias.md` §4 |

## 7. Pendências e desconhecidos (nada inventado)

1. **Março/2026**: registros **CONFIRMADAMENTE INEXISTENTES** — o cliente foi perguntado duas vezes (sessões 3 e 6) e declarou não ter informação adicional. Pergunta ENCERRADA em `QUESTIONS.md` sem resposta útil; entregáveis de `mes_03/` (mês) lavrados como marcadores BLOQUEADO com checklist para o caso de os registros surgirem.
2. **EFD-Contribuições jan/fev**: status de transmissão **DESCONHECIDO — pergunta encerrada sem resposta útil** (cliente não tem a informação; sessão 6). Risco a verificar internamente pelo cliente: se a EFD de jan foi transmitida com o crédito da NF 8812: EFD retificadora + DARF complementar de 11.100,00 + acréscimos.
3. **AJ-2601-01 ainda não escriturada** no razão do cliente (1.1.04 fev = 323.676,00 em vez de 312.576,00; lucro de jan nos livros ainda 139.583,00 em vez de 128.483,00).
4. **Recolhimentos**: nada pago — DARFs PIS/COFINS em aberto jan 79.883,00 + fev 81.141,00; passivo 2.1.03 acumulado em fev = 1.572.000,00 (amarração verificada: abertura 740.000,00 + PIS/COFINS jan 234.950,00 + ICMS jan 177.800,00 + PIS/COFINS fev 238.650,00 + ICMS fev 180.600,00). Acréscimos de mora **não calculáveis** com a biblioteca autorizada.
5. **Decomposição dos 85.000,00 de 4.2.02 de janeiro** (premissa 100% brindes; fevereiro está documentado).
6. **NFs das compras** jan/fev (créditos 155.067,00 e 157.509,00 aceitos com base no razão).
7. ICMS (jan 177.800,00; fev 180.600,00) fora do escopo dos entregáveis; usado apenas na amarração de 2.1.03.

## 8. Como destravar (apenas se os registros de março/2026 surgirem algum dia)

O cliente confirmou (na 2ª vez que a questão foi colocada) que **não possui informação adicional** sobre março/2026 nem sobre as EFD-Contribuições de jan/fev — as duas perguntas foram encerradas em `QUESTIONS.md` sem resposta útil. Não há, portanto, como destravar o engajamento nesta base documental; nada será inventado. Se os registros de março vierem a existir no futuro, o caminho é:

1. Entregar `documents/mes_03/` (razão + balancete de março e documentos do mês) e aplicar o mesmo protocolo de janeiro/fevereiro — tie-out (abertura + razões ⇄ balancete acumulado), PIS/COFINS 9,25% com varredura de créditos indevidos (uso e consumo), varredura de indedutíveis do art. 13 da Lei 9.249/95 — e só então emitir a versão **definitiva** dos entregáveis de `mes_03/` (a estrutura de marcadores BLOQUEADO já está lavrada lá, com checklist).
2. Confirmar o status de transmissão das EFD-Contribuições de jan/fev (se a de jan foi transmitida com o crédito da NF 8812: EFD retificadora + DARF complementar de 11.100,00 + acréscimos).
3. Escriturar AJ-2601-01 (data 31/01/2026) e recolher os DARFs em aberto (ou confirmar recolhimento para calcular acréscimos).
4. Até lá, o engajamento permanece **BLOCKED** e o e-LALUR de `mes_03/` permanece marcado **PRELIMINAR** — os valores do trimestre em `mes_03/lalur.json` e na Seção 3 são o piso firme jan+fev, não uma apuração definitiva.
