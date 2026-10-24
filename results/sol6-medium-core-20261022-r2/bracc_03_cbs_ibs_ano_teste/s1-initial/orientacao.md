# Horizonte — apuração-teste de CBS/IBS, agosto de 2026

**Resposta ao gerente.** Há trabalho em 2026: a Horizonte, como emitente do regime regular (CRT 3), deve destacar CBS/IBS, escriturar e apurar mensalmente. A dispensa é **do recolhimento**, condicionada ao cumprimento dessas obrigações. A apuração-teste indica saldo de **CBS R$ 2.862,00** e **IBS R$ 318,00**. Se as obrigações forem cumpridas, o recolhimento dos dois é **R$ 0,00**. Se não forem, a exposição calculada sobre estes dados é **R$ 3.180,00**, sujeita à validação dos créditos e dos documentos. [LC 214/2025, arts. 343 a 348; ADCT art. 125](../library/lc214_2025_transicao.md)

## Cálculo e alcance

| Etapa | CBS | IBS |
|---|---:|---:|
| Débitos: R$ 480.000,00 de saídas × 0,9% / 0,1% | R$ 4.320,00 | R$ 480,00 |
| Créditos com destaque em entradas regulares: R$ 62.000,00 + R$ 40.000,00 + R$ 60.000,00 = R$ 162.000,00 × 0,9% / 0,1% | R$ 1.458,00 | R$ 162,00 |
| Saldo informativo: débitos menos créditos | **R$ 2.862,00** | **R$ 318,00** |

A soma das 12 saídas, R$ 480.000,00, concilia com a base da apuração normal recebida. Os valores de cada nota, inclusive as irregulares, foram **recalculados** com 0,9% de CBS e 0,1% de IBS; não se adotou o destaque invertido da NF-e 2309. Os créditos de 2314, 2316 e 2317 usam os valores corretos destacados por item, mas dependem de regularização do totalizador. A 2313, sem destaque, e a 2315, do Simples, entram com crédito zero. [LC 214/2025, arts. 343 a 348; ADCT art. 125](../library/lc214_2025_transicao.md) · [NT 2025.002](../library/nt_nfe_grupo_ibscbs.md)

**Limite da evidência:** todos os XMLs recebidos têm `tpAmb=2` e se declaram fictícios; são arquivos de homologação. Portanto, o saldo e os R$ 3.180,00 são uma **simulação**, não confirmação de débito exigível em produção. Todos têm `cStat=100`, inclusive os que omitem o grupo obrigatório, e não há XML rejeitado entre os arquivos. A informação do e-mail sobre duas rejeições não se reconcilia com o conjunto entregue. Conferir os XMLs, protocolos e escrituração de produção antes de fechar a situação real.

## Checagem documental e providências

- **Saídas 2301–2305 (01–02/08):** ausência de `IBSCBS` aceita pela regra de transição anterior a 03/08. Permanecem na apuração-teste pelos valores recalculados. [CGIBS, comunicado de julho/2026](../library/cgibs_comunicado_03_08_2026.md)
- **Saídas 2306, 2307 e 2311:** `IBSCBS` por item tem base, CST, cClassTrib e alíquotas/valores corretos, mas não há `IBSCBSTot`; sanar o totalizador no fluxo documental e conferir a escrituração. **2309:** além do totalizador ausente, troca as alíquotas e os valores de CBS e IBS; o correto sobre R$ 38.000,00 é CBS R$ 342,00 e IBS R$ 38,00. [NT 2025.002](../library/nt_nfe_grupo_ibscbs.md)
- **Saídas 2308, 2310 e 2312 (a partir de 03/08):** falta `IBSCBS` e `IBSCBSTot`. O comunicado prevê rejeição de emissões do regime regular sem o grupo desde **03/08/2026**. Investigar por que estes arquivos exibem `cStat=100`, recuperar os retornos efetivos de produção e providenciar a regularização documental cabível. Não presumir que o status no arquivo de homologação prova emissão válida em produção. [CGIBS, comunicado de julho/2026](../library/cgibs_comunicado_03_08_2026.md) · [NT 2025.002](../library/nt_nfe_grupo_ibscbs.md)
- **Entradas 2314, 2316 e 2317:** pedir aos fornecedores a correção do totalizador ausente e confirmar o documento final antes de consolidar os créditos. **2313:** pré-03/08 e sem destaque, crédito zero. **2315 (Ponto Fixo, Simples):** sem destaque, crédito de CBS/IBS zero; os valores de PIS/COFINS impressos nela não viram crédito de CBS/IBS. [LC 214/2025, arts. 343 a 348; ADCT art. 125](../library/lc214_2025_transicao.md) · [NT 2025.002](../library/nt_nfe_grupo_ibscbs.md)

A partir de 03/08, parametrizar o emissor para informar por item `IBSCBS` com CST, cClassTrib, base, IBS UF **0,10%**, IBS municipal **0,00%**, CBS **0,90%** e totalizadores `IBSCBSTot`; validar os retornos de autorização e fazer a apuração mensal. A biblioteca informa ausência de penalidade pelo não preenchimento em 2026, mas ressalva a **perda da dispensa de recolhimento** se as obrigações acessórias não forem cumpridas. [CGIBS, comunicado de julho/2026](../library/cgibs_comunicado_03_08_2026.md) · [NT 2025.002](../library/nt_nfe_grupo_ibscbs.md)

O regime do **cliente** não muda a obrigação da Horizonte: as vendas a Ponto Fixo (Simples) e J. Silva (MEI) entram em seu destaque e em sua apuração. A exceção de 2026 para Simples/MEI diz respeito a eles **quando emitentes** não optantes pelo regime regular. Aquisição de fornecedor do Simples sem destaque, como a 2315, não gera crédito de CBS/IBS em 2026. [LC 214/2025, arts. 343 a 348; ADCT art. 125](../library/lc214_2025_transicao.md)

PIS e COFINS da apuração normal recebida continuam em trilha própria: R$ 480.000,00 × 0,65% = **R$ 3.120,00** de PIS; × 3% = **R$ 14.400,00** de COFINS. Com a dispensa e sem recolhimento de CBS/IBS, **não há valor destes tributos a compensar**. Se houver recolhimento, a biblioteca prevê compensação com PIS/COFINS do período; ela não traz o procedimento da IN RFB ainda indicada como “a editar”. Não se abateu automaticamente o saldo-teste dos R$ 17.520,00 de PIS/COFINS. [Compensação do IBS/CBS de 2026 com PIS/COFINS](../library/lei_pis_cofins_compensacao.md)
