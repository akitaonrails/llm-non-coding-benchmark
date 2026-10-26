# Orientação — CBS/IBS, agosto/2026 — Horizonte Comércio e Serviços Ltda. (regime regular)

Para: Paulo, gerente fiscal
Referência: documentos de agosto/2026 em `documents/`; legislação em `library/`

## Resposta curta

Você está **meio certo**: em 2026 **não há recolhimento a pagar**, mas **há obrigações a cumprir** — e o descumprimento faz **perder a dispensa**. A dispensa de recolhimento do IBS/CBS de 2026 é **condicionada** ao cumprimento das obrigações acessórias: **destaque nos documentos fiscais, escrituração e apuração-teste** (ADCT art. 125, §4º, redação da LC 214/2025 — `library/lc214_2025_transicao.md`). Você tem **4 notas irregulares** em agosto (2308, 2309, 2310 e 2312). Se isso não for regularizado, a dispensa fica em risco e o saldo apurado abaixo passa a ser devido (ainda que compensável com PIS/COFINS — ADCT art. 125, §1º).

## 1. Apuração-teste de agosto (os números, com a conta)

Alíquotas de 2026: **CBS 0,9%** e **IBS 0,1%** (IBS sempre no campo UF: pIBSUF 0,10, pIBSMun 0,00 — LC 214, art. 343; NT 2025.002 — `library/nt_nfe_grupo_ibscbs.md`).

**Débitos (saídas)** — 12 NF-e, somatório das notas = **R$ 480.000,00** (confere exatamente com a base de PIS/COFINS da sua apuração normal de agosto — reconciliação ok):

- CBS: 480.000,00 × 0,9% = **R$ 4.320,00**
- IBS: 480.000,00 × 0,1% = **R$ 480,00**

(Nota a nota em `apuracao_teste.json`. Ex.: NF-e 2306: 42.000 × 0,9% = 378,00 CBS; 42.000 × 0,1% = 42,00 IBS — confere com o destaque da própria nota.)

**Créditos (entradas)** — só geram crédito aquisições de fornecedor do regime regular **com destaque** (LC 214, art. 346):

| NF-e | Fornecedor | Valor | CBS cred. | IBS cred. | Por quê |
|---|---|---:|---:|---:|---|
| 2313 | Distribuidora Norte (regular) | 48.000,00 | 0,00 | 0,00 | emitida 02/08 **sem destaque** → sem crédito |
| 2314 | Distribuidora Norte (regular) | 62.000,00 | 558,00 | 62,00 | destaque correto |
| 2315 | **Ponto Fixo (Simples)** | 15.000,00 | 0,00 | 0,00 | ver §4 — sem crédito em 2026 |
| 2316 | Logística Atlas (regular) | 40.000,00 | 360,00 | 40,00 | destaque correto |
| 2317 | Distribuidora Norte (regular) | 60.000,00 | 540,00 | 60,00 | destaque correto |
| **Total** | | 225.000,00 | **1.458,00** | **162,00** | 558+360+540; 62+40+60 |

**Saldo-teste de agosto:**

- CBS: 4.320,00 − 1.458,00 = **R$ 2.862,00**
- IBS: 480,00 − 162,00 = **R$ 318,00**
- **Total apurado: R$ 3.180,00**

**Recolhimento devido: R$ 0,00**, porque o recolhimento de 2026 é **dispensado** ao contribuinte que cumprir as obrigações acessórias (ADCT art. 125, §4º). Os valores são **informativos, para calibragem de alíquotas** (LC 214, art. 343). **Condição da dispensa:** se as 4 notas irregulares (§3) não forem sanadas e você não escriturar/apurar, a dispensa pode ser perdida e aí os R$ 3.180,00 seriam devidos — nesse caso compensáveis com PIS/COFINS do mesmo período (PIS 3.120,00 + COFINS 14.400,00 = 17.520,00 > 3.180,00 → compensação integral, sem desembolso líquido; ADCT art. 125, §1º e `library/lei_pis_cofins_compensacao.md`).

## 2. O que muda a partir de 03/08/2026

Comunicado do Comitê Gestor do IBS (jul/2026 — `library/cgibs_comunicado_03_08_2026.md`):

- A partir de **03/08/2026**, contribuinte do **regime regular não pode emitir NF-e/NFC-e/NFS-e/CT-e sem o grupo IBSCBS** (CST, cClassTrib, bases e alíquotas) — o documento é **rejeitado**.
- Notas emitidas **antes** de 03/08 sem o grupo **permanecem válidas** (por isso suas notas 2301–2305 e a entrada 2313 estão regulares nesse ponto).
- Em 2026 **não há multa** pelo não preenchimento (caráter educativo), **mas** quem não cumpre as obrigações acessórias **perde a dispensa de recolhimento** (ADCT art. 125, §4º — citado expressamente pelo comunicado).

A mensagem que a empresa recebeu na semana passada — *"Rejeição: Grupo IBSCBS não informado para emitente do regime regular (NT 2025.002)"* (informação da empresa) — é exatamente essa vedação em ação. E o TI confirmou a causa raiz: para "contornar" a rejeição, **a versão do emissor foi rebaixada** para uma versão que não valida o grupo. É a mesma causa das notas 2308, 2310 e 2312 terem voltado a ser emitidas sem o grupo depois de 03/08 (ver §3).

Ou seja: a rejeição não é a sanção; a sanção de verdade é **ter que recolher** os R$ 3.180,00 apurados.

## 3. As notas irregulares — o que fazer

| NF-e | Data | Valor | Problema |
|---|---|---:|---|
| 2308 | 10/08 | 12.500,00 | emitida **depois de 03/08 sem o grupo IBSCBS** (destinatário Ponto Fixo, Simples) |
| 2309 | 13/08 | 38.000,00 | grupo presente com **alíquotas invertidas**: pIBSUF 0,90 (v 342,00) e pCBS 0,10 (v 38,00); o correto é **pIBSUF 0,10 → 38,00** e **pCBS 0,90 → 342,00** (NT 2025.002). O total destacado (380,00) coincide com o correto (342+38), mas a divisão CBS/IBS está errada |
| 2310 | 18/08 | 7.800,00 | emitida depois de 03/08 **sem o grupo IBSCBS** (destinatário MEI) |
| 2312 | 27/08 | 176.000,00 | emitida depois de 03/08 **sem o grupo IBSCBS** — a maior nota do mês |

Ações:

1. **Desfazer o contorno do TI e corrigir o emissor agora**: a volta de versão do emissor removeu a validação do grupo IBSCBS — é isso que permitiu "o sistema voltar a emitir" notas sem o grupo. O emissor deve voltar a preencher o grupo `IBSCBS` em todo documento de regime regular (CST 000, cClassTrib 000001 para tributação plena, vBC = valor da operação, pIBSUF 0,10, pIBSMun 0,00, pCBS 0,90 — `library/nt_nfe_grupo_ibscbs.md`). O contorno não resolve o problema: as notas 2308/2310/2312 seguem irregulares (sem o grupo, depois de 03/08) tenha a SEFAZ as autorize ou rejeite.
2. **Sanear as 4 notas**: o mecanismo de correção dos documentos já autorizados (cancelamento, NF-e de ajuste etc.) **não está previsto na biblioteca deste trabalho** — não posso indicar o procedimento correto com base apenas nela; item aberto (ver `PERGUNTAS.md`).
3. **Escriturar e apurar mensalmente** débitos e créditos mesmo com o recolhimento dispensado (LC 214, art. 346) — a `apuracao_teste.json` atende à apuração-teste de agosto.

## 4. Clientes do Simples Nacional e MEI — sua pergunta

**Errado não destacar para eles.** A dispensa do art. 347 é do **optante** do Simples/MEI: ele próprio não destaca nem apura IBS/CBS em 2026. Mas você (regime regular) **destaca CBS/IBS nas suas notas de saída independentemente do regime do destinatário** — a obrigação e o destaque são do **emissor** (LC 214, arts. 346 e 347). Foi exatamente o que tornou irregulares as notas 2308 (Ponto Fixo) e 2310 (MEI). Para destinatários do Simples/MEI você deve tributar normalmente e informar no grupo IBSCBS; quem não aproveita o crédito é o destinatário optante.

## 5. Crédito na entrada do Ponto Fixo (Simples) — sua pergunta

**Não pode creditar.** Aquisição de optante do Simples gera crédito ao adquirente do regime regular **limitado ao valor efetivamente recolhido** pelo optante a título de IBS/CBS no Simples; em 2026, **sem destaque, não há crédito** (LC 214, art. 347). NF-e 2315: crédito **zero**.
Mesma lógica na NF-e 2313: fornecedor do regime regular, mas nota de 02/08 **sem destaque** → sem crédito (art. 346: créditos vêm de aquisições **com destaque** de contribuintes do regime regular). O documento dela é válido (anterior a 03/08), só não gera crédito.

## 6. As duas rejeições — causa confirmada, desdobramentos em aberto

A empresa confirmou: a rejeição da semana passada foi *"Grupo IBSCBS não informado para emitente do regime regular (NT 2025.002)"*, e o TI a "contornou" rebaixando a versão do emissor. A cadeia causal está fechada — as 2 notas rejeitadas e as notas 2308/2310/2312 (emitidas após o rebaixamento, sem o grupo) decorrem do mesmo defeito.

O que **não foi apurado** (a empresa não tem mais informação):

- **Numeração e valor das 2 NF-e rejeitadas** — não estão em `documents/saidas/` (as 12 que estão são todas autorizadas, cStat 100). Documento rejeitado pela SEFAZ não chega a ser um documento fiscal autorizado: se as operações correspondentes ocorreram, estão até hoje sem documentação fiscal válida.
- **Impacto na receita**: a soma das 12 NF-e de saída (R$ 480.000,00) confere *exatamente* com a base de PIS/COFINS da apuração normal de agosto. Se as 2 rejeitadas forem operações realizadas, essa receita falta **nas duas apurações** (normal e-teste). A conciliação deve ser feita pelo log de rejeições do TI ou consulta à SEFAZ (ver `PERGUNTAS.md`).

## 7. "Se a SEFAZ autorizou, está regular?" — sua pergunta

**Não.** Autorização (cStat 100) não é o critério de regularidade das obrigações de 2026:

1. **A regra exige o grupo, não o "passar".** O comunicado do CGIBS determina que, a partir de 03/08, documentos do regime regular **sem o grupo IBSCBS são rejeitados**. As 3 notas (2308/2310/2312) só "passaram" porque o TI rebaixou a versão do emissor, removendo a validação — fluxo anormal, não conformidade. Em nenhum lugar o comunicado diz que autorizado = permitido; ele **exige** o grupo.
2. **O risco relevante não é a rejeição, é a dispensa condicionada.** O ADCT art. 125, §4º condiciona a dispensa de recolhimento de 2026 ao **cumprimento das obrigações acessórias** (destaque no documento fiscal, escrituração, apuração-teste) — e o comunicado repete: "**sem prejuízo da perda da dispensa de recolhimento** para quem não cumprir as obrigações acessórias". Documento emitido sem o grupo/destaque depois de 03/08 é obrigação acessória descumprida, **tenha a SEFAZ autorizado ou não**.
3. **Exemplo que derruba o argumento: a NF-e 2309.** Ela foi autorizada **com** o grupo — e mesmo assim o destaque está errado (alíquotas invertidas contra a NT 2025.002: pIBSUF 0,90/pCBS 0,10; o correto é 0,10/0,90). A autorização não tornou o destaque correto. Se "autorizou = regular" valesse, a 2309 estaria perfeita, e não está.
4. **Ponto não verificado na biblioteca** (assinalo como conclusão desta análise, não como regra citada): a biblioteca não contém norma que **convalide** documento emitido em desconformidade com o requisito vigente pelo só fato da autorização — nem o contrário. Como o critério do §4º é o cumprimento **efetivo** das obrigações acessórias, tratamos 2308/2309/2310/2312 como irregulares independentemente do cStat. O mecanismo de saneamento dessas notas continua aberto (`PERGUNTAS.md`).

Consequência prática: a autorização não elimina a exposição. Se a dispensa for perdida por descumprimento acessório, os R$ 3.180,00 apurados (§1) são devidos — ainda que compensáveis com PIS/COFINS (ADCT art. 125, §1º).

## Citações utilizadas (somente a biblioteca)

- ADCT art. 125 (caput: CBS 0,9% / IBS 0,1%; §1º compensação com PIS/COFINS; §4º dispensa condicionada a obrigações acessórias) e LC 214/2025, arts. 343, 346 e 347 — `library/lc214_2025_transicao.md`
- CGIBS, comunicado de julho/2026 (obrigatoriedade dos grupos IBSCBS a partir de 03/08/2026; notas anteriores válidas; sem multa em 2026, mas perda da dispensa) — `library/cgibs_comunicado_03_08_2026.md`
- NT NF-e 2025.002 (leiaute do grupo IBSCBS; pIBSUF 0,10, pIBSMun 0,00, pCBS 0,90) — `library/nt_nfe_grupo_ibscbs.md`
- Compensação do IBS/CBS de 2026 com PIS/COFINS (ADCT art. 125, §1º; IN RFB **a editar**) — `library/lei_pis_cofins_compensacao.md`

Não há qualquer outro fundamento na legislação da biblioteca; onde a biblioteca é omissa (p. ex. procedimento de correção de NF-e já autorizada; conteúdo da IN RFB sobre compensação), isso está sinalizado como aberto, não como regra verificada.
