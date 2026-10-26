# PENDÊNCIAS — 02/2026 (Atlas Distribuidora S.A.)

> **Versão atual — fevereiro FECHADO.** Esta versão substitui o marcador "BLOQUEADO" anterior: os registros de fevereiro foram fornecidos em `documents/mes_02/` (razão, balancete acumulado, NF-e 4410, recibo de doação, relatório de auditoria interna) e o mês foi efetivamente apurado. Entregáveis: `ajustes.json`, `pis_cofins.json` (neste diretório) e e-LALUR preliminar do trimestre em `../mes_03/`.

## 1. Conciliação dos livros (tie-out) — OK
Verificado por script (Python) sobre `documents/`: **abertura** (`balancete_abertura.csv`) + **razão de jan/2026** (excluídas as linhas `ABERT`, que repetem a abertura) + **razão de fev/2026** reproduzem o **balancete acumulado de fev/2026** em **22/22 contas, sem divergência**. Balancete acumulado fecha em equilíbrio: débitos = créditos = **23.299.010,00**.
Exemplo de amarração do resultado de fevereiro: receita 2.580.000,00 − PIS/COFINS s/ vendas 238.650,00 − ICMS s/ vendas 180.600,00 − CMV 1.419.000,00 − pessoal 210.000,00 − comerciais 163.000,00 − administrativas 96.000,00 − depreciação 51.667,00 − financeiras 28.000,00 = **193.083,00** (lucro contábil de fevereiro). Acumulado jan+fev (pós-AJ-2601-01): 128.483,00 + 193.083,00 = **321.566,00**.

## 2. PIS/COFINS de fevereiro (não cumulativo, 9,25%)
- Débito: 9,25% x receita 2.580.000,00 = **238.650,00**.
- Créditos válidos: 9,25% x compras p/ revenda 1.702.800,00 = **157.509,00** (único crédito lançado).
- Estornos: **0,00** — nenhum crédito indevido tomado em fevereiro (ver item 3).
- **A recolher fevereiro = 81.141,00.**
- Amarração com o ativo: 1.1.04 no balancete fev = 323.676,00 = 166.167,00 (jan) + 157.509,00 (fev) — confere, e comprova que o estorno de janeiro segue pendente (item 5).

## 3. NF-e 4410 — brindes a clientes (R$ 48.000,00) — sem estorno, com adição no e-LALUR
- Fato: 400 kits-presente (vinho + canivete gravado) para clientes, campanha "Parceiros Atlas", Brindes Prime LTDA, 12/02/2026, CFOP 1949; lançado D 4.2.02 / C 1.1.01 (razão ref. NF4410).
- **PIS/COFINS:** a empresa **não tomou crédito** sobre a aquisição (o razão de fev só credita 1.1.04 na ref. COMPRA) → nada a estornar. Registro defensivo: mesmo que houvesse crédito destacado, brinde destinado a distribuição gratuita não é insumo de produção/revenda e não geraria crédito (library/pis_cofins_uso_consumo.md).
- **IRPJ/CSLL:** despesa com brindes é **dedução vedada** — Lei 9.249/95, art. 13, **VII** (library/lei9249_art13.md) → **adição de 48.000,00** na Parte A do e-LALUR do 1º trimestre (já refletida em `../mes_03/lalur.json`).
- Instrução do diretor ("brinde é despesa comercial, sempre foi"): **contabilmente correta** (a classificação societária em 4.2.02 está adequada e não será alterada — library/irpj_csll_trimestral.md: adições não alteram a contabilidade CPC), **mas não afasta a adição fiscal**, que decorre da vedação legal expressa, independentemente da classificação contábil ("independentemente do disposto no art. 47 da Lei 4.506/64" — art. 13, caput).

## 4. Doação à Associação Beneficente Luz (R$ 30.000,00) — indedutível
- Fato: doação paga em 18/02/2026 (razão ref. DOACAO, D 4.2.02 / C 1.1.01); recibo da entidade informa que **não possui título de OSCIP nem certificação de utilidade pública federal** (associação civil registrada em cartório).
- Enquadramento: doações são dedutíveis **exceto** as do § 2º do art. 13 (Lei 9.249/95 — library/lei9249_art13.md). As hipóteses do § 2º exigem qualificação específica: I projetos culturais (Lei 8.313/91); II entidades c/ **utilidade pública federal ou OSCIP** (limite de 2% do lucro operacional); III instituições de ensino/pesquisa (limite 1,5%). **Nenhuma se aplica** à Associação Luz → despesa **indedutível** → **adição de 30.000,00** no e-LALUR do 1º trimestre.
- Auditoria interna (relatório de revisão analítica de fev, item 3) sinalizou brindes acima do padrão e a doação, pedindo verificação de classificação e reflexos: **procedente quanto aos reflexos fiscais** (adições acima). A classificação contábil em 4.2.02 é aceitável para fins societários e foi mantida; o "reflexo" devido é na apuração, não no razão. A dispensa da observação pela diretoria não foi aceita: a vedação é legal.

## 5. AJ-2601-01 (estorno de 11.100,00 de janeiro) — AINDA NÃO ESCRITURADA
Reiterada em `ajustes.json` (retificacoes_meses_anteriores). Evidência no balancete acumulado de fev: 1.1.04 = 323.676,00 (deveria ser 312.576,00). Escriturar D 4.2.04 / C 1.1.04 com data de 31/01/2026. O lucro de janeiro nos livros do cliente ainda está 139.583,00 em vez de 128.483,00; a apuração em `../mes_03/` já considera o valor pós-ajuste.

## 6. Recolhimentos e EFD — pendências operacionais
- Nada foi recolhido: 2.1.03 acumulado em fev = 1.572.000,00 = abertura 740.000,00 + PIS/COFINS jan 234.950,00 + ICMS jan 177.800,00 + PIS/COFINS fev 238.650,00 + ICMS fev 180.600,00 (amarração verificada no tie-out). Consequência prática: **DARFs de PIS/COFINS em aberto** — jan 79.883,00 (com o estorno) e fev 81.141,00; cálculo de acréscimos (mora) não é possível com a biblioteca disponível e depende da data de pagamento.
- **Status de transmissão das EFD-Contribuições de jan e fev: desconhecido** (pergunta em `../QUESTIONS.md`). Se a EFD de jan já transmitida com o crédito da NF 8812: EFD retificadora + DARF complementar de 11.100,00 + acréscimos (library/pis_cofins_uso_consumo.md).

## 7. Premissas e desconhecidos remanescentes
- Premissa mantida de janeiro: adição de brindes de jan = 100% da conta 4.2.02 de jan (85.000,00), por confirmação prévia do cliente em janeiro; em fevereiro a composição de 4.2.02 está **documentada** (48.000 brindes + 30.000 doação + 85.000 ordinárias), de modo que apenas a parcela de janeiro depende dessa premissa.
- ICMS (jan 177.800,00; fev 180,600,00) está fora do escopo dos entregáveis do contrato (ajustes + PIS/COFINS + LALUR), mas foi usado na amarração de 2.1.03.
- **Março/2026 continua sem registros** em `documents/` → fechamento de `mes_03` e apuração **definitiva** do 1º trimestre seguem impossíveis; o e-LALUR em `../mes_03/` é **preliminar (jan+fev)** e não deve ser usado para recolhimento ou escrituração definitiva.
