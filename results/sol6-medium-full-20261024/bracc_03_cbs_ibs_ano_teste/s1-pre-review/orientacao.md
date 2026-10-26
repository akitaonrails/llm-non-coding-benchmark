# Orientação ao gerente fiscal — agosto de 2026

**Há trabalho a fazer em 2026.** A Horizonte, no regime regular, deve destacar CBS e IBS nos documentos eletrônicos, escriturar e fazer a apuração mensal de teste. As alíquotas de teste são CBS **0,90%** e IBS estadual **0,10%** (IBS municipal **0,00%**). O recolhimento é **dispensado somente se as obrigações acessórias forem cumpridas**; o caráter educativo e a ausência de penalidade em 2026 pelo não preenchimento não asseguram essa dispensa. Com as falhas encontradas, **não é possível afirmar que a condição já foi cumprida**. [LC 214/2025, arts. 343 a 348; ADCT art. 125 (EC 132/2023)](../library/lc214_2025_transicao.md); [CGIBS, comunicado de julho/2026; NT NF-e 2025.002](../library/cgibs_comunicado_03_08_2026.md).

## Apuração de teste

Os valores do JSON são **calculados pelas alíquotas corretas sobre o valor de cada operação**, inclusive nas notas sem destaque e na 2309, que traz as alíquotas invertidas. Isso mostra o valor econômico da apuração; não valida os XMLs defeituosos. Assumi, para esta simulação, que os valores das operações são as bases integrais e que não há regime diferenciado ou não incidência, pois os arquivos não trazem dados para outro tratamento.

| Cálculo | CBS | IBS |
|---|---:|---:|
| Débitos: R$ 480.000,00 × 0,90% / 0,10% | R$ 4.320,00 | R$ 480,00 |
| Créditos com destaque por fornecedores regulares: (R$ 62.000,00 + R$ 40.000,00 + R$ 60.000,00) × 0,90% / 0,10% | R$ 1.458,00 | R$ 162,00 |
| Saldo de teste: débitos − créditos | **R$ 2.862,00** | **R$ 318,00** |

Saldo conjunto de teste: **R$ 3.180,00**. As 12 saídas somam R$ 480.000,00, igual à base informada na apuração normal de PIS/COFINS. Esta informa PIS de R$ 3.120,00 e COFINS de R$ 14.400,00 (R$ 17.520,00 no total); **não há compensação de CBS/IBS se nada for recolhido**. Se houver recolhimento efetivo, a biblioteca prevê compensação com PIS/COFINS do mesmo período, mas não há aqui prova de recolhimento nem valor exigível definitivo. [ADCT art. 125, §1º; IN RFB (a editar)](../library/lei_pis_cofins_compensacao.md).

## Checagem das saídas

| NF-e | Valor | CBS / IBS de teste | Constatação |
|---|---:|---:|---|
| 2301 | R$ 18.000,00 | R$ 162,00 / R$ 18,00 | 01/08: sem grupo, admitido antes de 03/08. |
| 2302 | R$ 24.000,00 | R$ 216,00 / R$ 24,00 | 01/08: sem grupo, admitido antes de 03/08. |
| 2303 | R$ 9.500,00 | R$ 85,50 / R$ 9,50 | 02/08: sem grupo, admitido antes de 03/08; cliente Simples não altera o dever da Horizonte. |
| 2304 | R$ 31.000,00 | R$ 279,00 / R$ 31,00 | 02/08: sem grupo, admitido antes de 03/08. |
| 2305 | R$ 4.200,00 | R$ 37,80 / R$ 4,20 | 02/08: sem grupo, admitido antes de 03/08; cliente MEI não altera o dever da Horizonte. |
| 2306 | R$ 42.000,00 | R$ 378,00 / R$ 42,00 | 04/08: destaque por item correto; falta `IBSCBSTot` no XML fornecido. |
| 2307 | R$ 56.000,00 | R$ 504,00 / R$ 56,00 | 06/08: destaque por item correto; falta `IBSCBSTot`. |
| 2308 | R$ 12.500,00 | R$ 112,50 / R$ 12,50 | 10/08: faltam `IBSCBS` e `IBSCBSTot`; cliente Simples não dispensa destaque. |
| 2309 | R$ 38.000,00 | R$ 342,00 / R$ 38,00 | 13/08: XML mostra CBS R$ 38,00 a 0,10% e IBS R$ 342,00 a 0,90%: alíquotas trocadas; falta `IBSCBSTot`. |
| 2310 | R$ 7.800,00 | R$ 70,20 / R$ 7,80 | 18/08: faltam `IBSCBS` e `IBSCBSTot`; cliente MEI não dispensa destaque. |
| 2311 | R$ 61.000,00 | R$ 549,00 / R$ 61,00 | 21/08: destaque por item correto; falta `IBSCBSTot`. |
| 2312 | R$ 176.000,00 | R$ 1.584,00 / R$ 176,00 | 27/08: faltam `IBSCBS` e `IBSCBSTot`. |

Desde **03/08**, os documentos do regime regular precisam do grupo por item com CST, cClassTrib, base, alíquotas e valores. A nota técnica também situa os totalizadores em `IBSCBSTot`; nenhum XML fornecido contém esse grupo. Por isso, classifiquei como irregulares no JSON até os documentos pós-03/08 cujo destaque por item está correto. As notas anteriores a 03/08 permanecem válidas quanto à ausência do grupo. [CGIBS, comunicado de julho/2026; NT NF-e 2025.002](../library/cgibs_comunicado_03_08_2026.md); [NT 2025.002 (resumo técnico)](../library/nt_nfe_grupo_ibscbs.md).

**Autorização pela SEFAZ e conformidade fiscal são verificações diferentes.** O `cStat=100` mostra que o arquivo foi aceito no ambiente indicado, mas não demonstra que a Horizonte destacou CBS/IBS, escriturou e apurou conforme exigido. Uma volta à versão antiga do emissor que omitiu esses dados não sana a obrigação acessória nem comprova o direito à dispensa do recolhimento. A aceitação relatada após 03/08 diverge da rejeição prevista no comunicado; é preciso conferir protocolos, ambiente, datas e XMLs de produção para explicar a divergência. Não há base na biblioteca para declarar, só por essa divergência, que uma NF-e autorizada em produção perdeu sua autorização: a classificação “irregular” no JSON se refere **ao cumprimento de IBS/CBS**, não ao cancelamento da autorização de uso. [LC 214/2025, arts. 343 a 348; ADCT art. 125 (EC 132/2023)](../library/lc214_2025_transicao.md); [CGIBS, comunicado de julho/2026; NT NF-e 2025.002](../library/cgibs_comunicado_03_08_2026.md).

## Checagem das entradas

| NF-e | Valor | Crédito CBS / IBS | Motivo |
|---|---:|---:|---|
| 2313 | R$ 48.000,00 | R$ 0,00 / R$ 0,00 | Fornecedor regular, mas sem destaque; não há crédito documentado nesta apuração. |
| 2314 | R$ 62.000,00 | R$ 558,00 / R$ 62,00 | Fornecedor regular, com destaque por item. |
| 2315 | R$ 15.000,00 | R$ 0,00 / R$ 0,00 | Ponto Fixo, Simples (CRT 1), sem destaque; não creditar. |
| 2316 | R$ 40.000,00 | R$ 360,00 / R$ 40,00 | Fornecedor regular, com destaque por item. |
| 2317 | R$ 60.000,00 | R$ 540,00 / R$ 60,00 | Fornecedor regular, com destaque por item. |

Os três créditos destacados são **informativos e sujeitos à validação dos XMLs**, pois também lhes falta `IBSCBSTot`. O art. 346 da biblioteca vincula crédito a aquisição de contribuinte regular com destaque. Para entrada de optante do Simples, o art. 347 limita o crédito ao valor efetivamente recolhido no Simples e afirma que, em 2026, sem destaque não há crédito. [LC 214/2025, arts. 343 a 348; ADCT art. 125 (EC 132/2023)](../library/lc214_2025_transicao.md); [NT 2025.002 (resumo técnico)](../library/nt_nfe_grupo_ibscbs.md).

## Providências

1. Corrigir o emissor para preencher `IBSCBS` por item, usar CBS 0,90%, IBS UF 0,10% e IBS municipal 0,00%, e gerar `IBSCBSTot`. Aplicar isso a todas as saídas da Horizonte a partir de 03/08, inclusive para compradores do Simples e MEI. A dispensa de destaque do art. 347 pertence ao **emitente** optante do Simples/MEI que não optou pelo regime regular; não ao fornecedor regular desses compradores. [LC 214/2025, arts. 343 a 348; ADCT art. 125 (EC 132/2023)](../library/lc214_2025_transicao.md); [NT 2025.002 (resumo técnico)](../library/nt_nfe_grupo_ibscbs.md).
2. Localizar os protocolos e XMLs de **produção** das duas rejeições e das emissões posteriores; conciliar as operações para identificar falta de nota ou duplicidade. Conferir os XMLs 2308, 2309, 2310 e 2312 e os totalizadores de todas as notas pós-03/08. Definir a forma de correção documental com base nos protocolos reais: a biblioteca não descreve procedimento de substituição ou cancelamento de NF-e já autorizada, portanto não há fundamento aqui para mandar reemitir essas notas automaticamente. O comunicado prevê rejeição de documentos sem os grupos após 03/08. [CGIBS, comunicado de julho/2026; NT NF-e 2025.002](../library/cgibs_comunicado_03_08_2026.md).
3. Escriturar as operações, refazer a apuração-teste após as correções e guardar evidência do cumprimento das obrigações acessórias antes de aplicar a dispensa do recolhimento. Confirmar os créditos das entradas com os XMLs corrigidos dos fornecedores. [LC 214/2025, arts. 343 a 348; ADCT art. 125 (EC 132/2023)](../library/lc214_2025_transicao.md).

**Limite dos arquivos recebidos:** todos os XMLs informam `tpAmb=2` e se declaram fictícios, sem validade fiscal. Os protocolos exibem `cStat=100`; não há arquivos das duas rejeições relatadas. Assim, os números acima são uma **simulação**, não prova de emissão em produção, de rejeição ou de cumprimento das obrigações para a dispensa. O conjunto também não permite determinar um recolhimento efetivamente exigível se a dispensa não for obtida.
