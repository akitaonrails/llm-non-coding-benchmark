# Orientação fiscal — CBS/IBS período-teste — agosto/2026

**Para:** Paulo (gerente fiscal) — **De:** consultoria — **Ref.:** apuração-teste CBS/IBS de agosto/2026 (Horizonte Comércio e Serviços Ltda., CNPJ 27.119.804/0001-30, regime regular / Lucro Presumido)
**Base da análise:** 12 NF-e de saída (nº 2301–2312) e 5 NF-e de entrada (nº 2313–2317) fornecidas. Citações apenas da biblioteca de referência (`library/INDEX.md`). O que não está na biblioteca está marcado **[não verificado]**.

---

## 1. Resposta direta

**"Em 2026 é só informativo, não se paga nada" — quase, mas não é "não precisa fazer nada".**

- O recolhimento CBS/IBS de 2026 é **dispensado**, mas **condicionado ao cumprimento das obrigações acessórias** (destaque nos documentos fiscais, escrituração e apuração-teste) — ADCT art. 125, §4º (`lc214_2025_transicao.md`).
- **Em agosto a Horizonte descumpriu a condição em 4 das 12 notas de saída** (2308, 2310, 2312 e 2309 — detalhes na seção 4). Se isso não for tratado, **há risco real de perder a dispensa** e ter de recolher **R$ 3.180,00** (seção 2).
- A partir de **03/08/2026**, as notas que vieram erradas nem seriam autorizadas: quem está no regime regular **não pode mais emitir NF-e sem o grupo IBSCBS** — documento sem o grupo deve ser **rejeitado** pela SEFAZ (CGIBS, comunicado de julho/2026; NT 2025.002 — `cgibs_comunicado_03_08_2026.md`). Em 2026 não há penalidade pelo erro, mas a perda da dispensa permanece como consequência.

## 2. O que é devido, o que é dispensado e sob que condição

Apuração-teste do mês (valores informativos, alíquotas do art. 343 da LC 214/2025: CBS 0,9% e IBS 0,1%):

| Débitos (saídas 2301–2312) | R$ |
|---|---:|
| CBS = 480.000,00 × 0,9% | **4.320,00** |
| IBS = 480.000,00 × 0,1% | **480,00** |
| Créditos (entradas com destaque de fornecedores do regime regular: 2314, 2316, 2317) | CBS **−1.458,00**; IBS **−162,00** |
| **Saldo** | **CBS 2.862,00 + IBS 318,00 = R$ 3.180,00** |

- Base de cálculo das saídas: R$ 480.000,00 — **bate exatamente** com a base de PIS/COFINS da apuração normal do mês (`documents/apuracao_normal_agosto.md`: PIS 3.120,00 + COFINS 14.400,00 sobre 480.000,00). População validada.
- **Recolhimento devido hoje: R$ 0,00** — pelo ADCT art. 125, §4º, desde que as obrigações acessórias estejam cumprimas.
- **Condição em risco:** 4 notas irregulares (seção 4). **Se a dispensa for perdida, o devido é o próprio saldo: R$ 3.180,00**, compensável com PIS/COFINS do mesmo período (Há folga: PIS 3.120,00 + COFINS 14.400,00 = 17.520,00 ≥ 3.180,00; art. 125, §1º e `lei_pis_cofins_compensacao.md`).

## 3. Notas de saída — situação documento a documento (resumo)

| Nº | Data | Valor | CBS (0,9%) | IBS (0,1%) | Situação |
|---|---|---:|---:|---:|---|
| 2301 | 01/08 | 18.000,00 | 162,00 | 18,00 | regular (pré-corte, sem grupo) |
| 2302 | 01/08 | 24.000,00 | 216,00 | 24,00 | regular (pré-corte, sem grupo) |
| 2303 | 02/08 | 9.500,00 | 85,50 | 9,50 | regular (pré-corte, sem grupo) |
| 2304 | 02/08 | 31.000,00 | 279,00 | 31,00 | regular (pré-corte, sem grupo) |
| 2305 | 02/08 | 4.200,00 | 37,80 | 4,20 | regular (pré-corte, sem grupo) |
| 2306 | 04/08 | 42.000,00 | 378,00 | 42,00 | regular (grupo OK) |
| 2307 | 06/08 | 56.000,00 | 504,00 | 56,00 | regular (grupo OK) |
| **2308** | 10/08 | 12.500,00 | 112,50 | 12,50 | **irregular** — sem grupo após 03/08 |
| **2309** | 13/08 | 38.000,00 | 342,00 | 38,00 | **irregular** — alíquotas invertidas no destaque |
| **2310** | 18/08 | 7.800,00 | 70,20 | 7,80 | **irregular** — sem grupo após 03/08 |
| 2311 | 21/08 | 61.000,00 | 549,00 | 61,00 | regular (grupo OK) |
| **2312** | 27/08 | 176.000,00 | 1.584,00 | 176,00 | **irregular** — sem grupo após 03/08 |

Conferência da tabela: somatório de valores 480.000,00; CBS 4.320,00; IBS 480,00 — igual à seção 2. Documento a documento com os motivos completos está em `apuracao_teste.json`. As notas sem grupo **antes** de 03/08 (2301–2305) **permanecem válidas** (comunicado CGIBS); nelas não houve destaque, então **o cliente não gera crédito** (art. 346) — mas o **débito da Horizonte subsiste** (art. 343).

## 4. O que fazer com as 4 notas irregulares

**Por que são irregulares:**
- **2308, 2310, 2312** — emitidas **após 03/08 sem o grupo IBSCBS**. O comunicado CGIBS é claro: desde 03/08 isso **não é permitido** e o documento **deve ser rejeitado** pela SEFAZ.
- **2309** — tem o grupo, mas com **alíquotas invertidas**: pIBSUF 0,90 e pCBS 0,10; destaque saiu IBS 342,00 / CBS 38,00 — exatamente o oposto do leiaute (NT 2025.002 prescreve pIBSUF = 0,10; pIBSMun = 0,00; pCBS = 0,90). Valores corretos: IBS 38,00 / CBS 342,00 (é o que está registrado na apuração).

**Causa raiz — CONFIRMADA pelo cliente (resposta de out/2026):**
- Confirmação: *"A rejeição dizia: 'Rejeição: Grupo IBSCBS não informado para emitente do regime regular (NT 2025.002)'. O TI 'contornou' voltando a versão do emissor."*

Ou seja: o emissor primeiro **rejeitou corretamente** duas notas (a regra pós-03/08 funcionou), e a **solução do TI foi rebaixar (rollback) a versão do emissor** para voltar a emitir — por isso as notas 2308/2310/2312 constam **autorizadas (cStat 100) sem o grupo**. Foi uma **derrubada deliberada da validação**, não uma falha aleatória:

1. **Reverter URGENTE o rollback**: restaurar a versão atual do emissor (a que valida o grupo IBSCBS). Enquanto a versão antiga estiver em produção, **cada nova emissão repete o erro** — o risco à dispensa (ADCT art. 125, §4º) cresce a cada dia/competência. Quem liberou o rollback: TI da empresa (informação do cliente); versão/data do rollback: **[não informado pelo cliente]**.
2. **Corrigir a parametrização por upgrade, não por rollback** (manter o grupo IBSCBS com alíquotas pIBSUF 0,10 / pIBSMun 0,00 / pCBS 0,90 por item) e **revalidar com NF-e de teste** antes do próximo faturamento.
3. **Nota 2309:** o rollback **não** corrigiu a troca CBS↔IBS — é outro defeito de parametrização, a corrigir à parte (e conferir se a versão rebaixada foi a causa da inversão).
4. **Tratamento dos 4 documentos:** a biblioteca **não traz o procedimento** de cancelamento/regularização de NF-e autorizada sem o grupo ou com destaque trocado **[não verificado]**. Pergunta enviada ao cliente em `QUESTIONS.md` (Q4). Não assumir procedimento sem confirmar (prazo/carta de correção/cancelamento).

**Impacto nos clientes — comunicar:**
- **BRISA (2304 pré-corte e 2312):** em 2312 ela **não poderá tomar crédito** de CBS 1.584,00 / IBS 176,00 por falta de destaque (art. 346: crédito exige destaque). Maior impacto do mês.
- **SERRA VERDE (2307 e 2309):** em 2309 recebeu destaque **sem lastro** (créditos trocados: IBS 342,00 / CBS 38,00 em vez de IBS 38,00 / CBS 342,00). Verificar se ela já usou os valores e avisar da correção.
- **PONTO FIXO (2303 pré-corte e 2308) / J. SILVA (2305 e 2310):** sem destaque, sem crédito para eles (art. 346) — mas isso não altera o débito da Horizonte (art. 343).

**Sobre as duas notas rejeitadas pelo sistema:** a mensagem de rejeição foi identificada pelo cliente ("Grupo IBSCBS não informado para emitente do regime regular — NT 2025.002"), o que **confirma que a validação pós-03/08 estava funcionando**. **Permanece sem resposta** (o cliente não tem informação adicional): **quais documentos** foram rejeitados e se foram reemitidos dentro da série 2301–2312 (ou com novos números fora dela). A população adotada segue sendo as 12 saídas fornecidas — a base delas (480.000,00) reconcilia exatamente com a base de PIS/COFINS da apuração normal, o que **reforça** que não falta documento de mercadoria na série; documento adicional, se existir, alteraria a apuração (explicitado como desconhecido em `STATUS.md`).

**"Mas a SEFAZ autorizou — autorizada não é regular?"** (Paulo, out/2026) — **Não. A autorização não regulariza o documento:**

1. **A norma manda; o cStat só constata.** Desde 03/08, o comunicado CGIBS/NT 2025.002 diz que emitir NF-e do regime regular **sem o grupo "não é permitida"** — a rejeição é apenas o mecanismo de defesa do ambiente. O que o TI derrubou foi o controle (rollback do emissor); **o dever de destaque não foi derrubado com ele**. A régua do conceito "regular/irregular" na apuração é a norma (LC 214/2025 + NT 2025.002 + CGIBS), não o resultado do envio.
2. **Prova dentro do próprio mês:** a NF **2309 foi autorizada (cStat 100) com destaque invertido** (IBS 342,00 / CBS 38,00 em vez de IBS 38,00 / CBS 342,00 — a NT prescreve pIBSUF 0,10 / pCBS 0,90). Se "autorizada = regular" valesse, nenhum erro de conteúdo importaria — mas o próprio regulamento existe justamente para dizer o que a nota precisa conter. Autorizada **e** errada é possível — agosto dela é o exemplo em dobro.
3. **O próprio comunicado separa autorização de conformidade:** em 2026 não há penalidade ("caráter educativo"), **"sem prejuízo da perda da dispensa"**. Ou seja: autorizar não gera multa, mas **não cumpre as obrigações acessórias** — e a dispensa (ADCT art. 125, §4º) está condicionada ao **cumprimento** (destaque no documento, escrituração, apuração-teste), não ao cStat do documento.
4. **Efeito prático:** as 4 notas seguem marcadas **"irregular"** e a condição da dispensa **está em risco**; se perdida, vira recolhimento devido de **R$ 3.180,00** (compensável com PIS/COFINS — 17.520,00 disponíveis, art. 125 §1º). A correção que resolve é reverter o rollback e parametrizar por upgrade — quanto antes, menos documentos irregulares e menor o argumento contra a dispensa.

*Resumo para o gerente:* "autorizada" responde à pergunta técnica "o ambiente aceitou o arquivo?"; "regular" responde à jurídica "a nota contém o que a norma exige?". Em agosto, a Horizonte tem 4 documentos com a primeira resposta sim e a segunda não — por isso a apuração as marca como irregulares, e o plano de ação (§8, item 1) é urgente.

## 5. Clientes do Simples e do MEI — destaque sim

Sua frase "para cliente do Simples e MEI eu não destaco nada, certo?" — **errado a partir de 03/08**:

- Quem define o destaque é **o regime do emissor (a Horizonte, regime regular)**, não o do cliente (art. 343). A venda a optante do Simples ou a MEI **não isenta nem reduz o débito** da Horizonte: 2303 (9.500,00 → CBS 85,50; IBS 9,50) e 2305 (4.200,00 → 37,80/4,20) têm débito integral na apuração-teste.
- O cliente optante do Simples/MEI **não apura crédito nem é obrigado a destaque do lado dele em 2026** (art. 347). Mas, como você está no regime regular, **tem de destacar o grupo nas notas que emite, inclusive para Simples/MEI**, quando emissão após 03/08 (comunicado CGIBS).
- Casos do mês: 2303/2308 (para PONTO FIXO, Simples), 2305/2310 (para J. SILVA, MEI). Pre-03/08 tudo válido; **a partir de 03/08** (2308, 2310) a ausência do grupo é irregular por isso mesmo.

## 6. Entrada do Ponto Fixo (Simples) — pode creditar? **NÃO**

Sua pergunta: "o IBS/CBS na nota de entrada do Ponto Fixo (Simples) — posso creditar?" —

- **Art. 347:** aquisições de optante do Simples geram crédito **limitado ao valor efetivamente recolhido** pelo optante a título de IBS/CBS — e, em 2026, **sem destaque, não há crédito**.
- NF 2315 (PONTO FIXO COMERCIO ME — CRT 1, Simples, 15.000,00, sem grupo IBSCBS): **crédito = 0,00**. Não creditar.
- As outras entradas, de fornecedores do regime regular **com** destaque, são creditáveis integralmente:

| Nº | Fornecedor | Valor | Crédito CBS (0,9%) | Crédito IBS (0,1%) |
|---|---|---:|---:|---:|
| 2313 | Distribuidora Norte (regular, **sem grupo**, 02/08) | 48.000,00 | **0,00** | **0,00** |
| 2314 | (regular, grupo OK) | 62.000,00 | 558,00 | 62,00 |
| 2315 | Ponto Fixo (**Simples**) | 15.000,00 | **0,00** | **0,00** |
| 2316 | Logística Atlas (grupo OK) | 40.000,00 | 360,00 | 40,00 |
| 2317 | (regular, grupo OK) | 60.000,00 | 540,00 | 60,00 |

- A nota 2313 (48.000,00 × 1% = **480,00** de crédito potencial) **não gerou crédito por falta de destaque** (art. 346); a biblioteca não prevê crédito retroativo sem destaque **[não verificado]. Operação antes do corte de 03/08 é válida, mas o crédito não nasce**. Fica como custo do mês — representa o ponto de atenção para futuras entradas imediatamente após o início de qualquer janela de obrigatoriedade.

## 7. O que muda a partir de 03/08/2026 (em uma linha)

**Antes:** NF-e do regime regular sem grupo = válida (educativo). **Depois (≥ 03/08):** emissão sem o grupo IBSCBS **não é permitida** e documento **rejeitado**; grupo com alíquotas erradas (como a 2309) gera destaque sem lastro. Sem penalidade em 2026 (caráter educativo), **mas a perda da dispensa** de recolhimento (ADCT 125 §4º) segue como consequência para quem não cumprir as obrigações acessórias (`cgibs_comunicado_03_08_2026.md`).

## 8. Plano de ação (prioridade)

1. **Reverter o rollback do emissor** (restaurar a versão com NT 2025.002) e **parametrizar por upgrade** (grupo IBSCBS + alíquotas 0,90 CBS / 0,10 pIBSUF / 0,00 pIBSMun por item); **NF-e de teste** antes do próximo faturamento — urgente.
2. **Decidir o tratamento dos 4 documentos irregulares** (2308, 2309, 2310, 2312) com instrução da contabilidade/FISCO — pendência de decisão interna: a biblioteca não traz o mecanismo de cancelamento/regularização **[não verificado]** e o cliente não tem informação adicional (Q4).
3. **Comunicar BRISA e SERRA VERDE** dos impactos de crédito (2312: sem crédito; 2309: destaque trocado).
4. **Não creditar** a nota de entrada do Ponto Fixo (2315).
5. **Manter escrituração e apuração-teste** mensal (art. 346) — é a condição da dispensa.
6. Se a dispensa vier a ser perdida: recolher **R$ 3.180,00** e **compensar com PIS/COFINS** (17.520,00 disponíveis; §1º).

## 9. Desconhecidos explícitos (sem resposta do cliente)

- Procedimento de cancelamento/substituição de NF-e autorizada sem o grupo ou com destaque trocado — **não verificado** (decisão interna Q4; cliente sem informação adicional).
- **Quais documentos** sofreram as 2 rejeições e se foram reemitidos na série 2301–2312 — cliente **sem informação** (a mensagem de rejeição confirmada foi "Grupo IBSCBS não informado para emitente do regime regular, NT 2025.002").
- NFS-e (serviços) ou outros documentos de saída/entrada em agosto além dos 17 fornecidos — cliente **sem informação**; adotada a premissa de população completa (base 480.000,00 reconcilia com a apuração normal).
- Versão/data do rollback do emissor e desde quando emissões saem sem grupo — cliente **sem informação** (risco às competências seguintes até a reversão).
- Se BRISA e SERRA VERDE já lançaram/usaram os créditos de 2312 e 2309 — cliente **sem informação**.
- Existência de IN RFB disciplinadora da compensação PIS/COFINS: a biblioteca a lista como "(a editar)" — método operacional pendente de regulação **[não verificado]**.

---
*Fontes citáveis utilizadas: `library/lc214_2025_transicao.md`, `library/cgibs_comunicado_03_08_2026.md`, `library/nt_nfe_grupo_ibscbs.md`, `library/lei_pis_cofins_compensacao.md` (conforme `library/INDEX.md`). Dados do cliente: `documents/saidas/`, `documents/entradas/`, `documents/apuracao_normal_agosto.md`, `documents/email_gerente_fiscal.txt` (fatos do cliente, não norma).*
