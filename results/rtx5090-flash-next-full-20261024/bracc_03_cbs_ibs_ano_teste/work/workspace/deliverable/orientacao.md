# Orientação — CBS/IBS, período de teste de 2026 (agosto/2026)

**Para:** Paulo, gerente fiscal — **Horizonte Comércio e Serviços Ltda** (CNPJ 27.119.804/0001-30, CRT 3, regime regular)
**Base:** somente a biblioteca de referência (`library/INDEX.md`): LC 214/2025 arts. 343–348 e ADCT art. 125 (EC 132/2023) [`lc214_2025_transicao.md`]; comunicado do CGIBS de julho/2026 [`cgibs_comunicado_03_08_2026.md`]; NT NF-e 2025.002 [`nt_nfe_grupo_ibscbs.md`]; ADCT art. 125 §1º [`lei_pis_cofins_compensacao.md`].

## Resposta curta à sua pergunta ("não precisa fazer nada em 2026"?)

**Não é isso.** Em 2026 a CBS é calculada a **0,9%** e o IBS a **0,1%**, e os valores apurados são **informativos** (LC 214/2025, art. 343) — mas a **dispensa de recolhimento é condicional**: vale apenas para quem **cumprir as obrigações acessórias** — destacar IBS/CBS nos documentos fiscais, escriturar e fazer a apuração-teste mensal (ADCT art. 125, §4º; LC 214/2025, art. 346). Ou seja: **não se paga, desde que se calcule, destaque e escriture.** Sem isso, a dispensa pode ser perdida (o comunicado do CGIBS diz expressamente que a ausência de penalidades em 2026 é "sem prejuízo da perda da dispensa de recolhimento").

## O que é devido e o que é dispensado (agosto/2026)

Apuração-teste completa em `apuracao_teste.json`. Aritmética:

**Débitos (12 saídas, base total R$ 480.000,00):**
- CBS: 480.000,00 × 0,9% = **R$ 4.320,00**
- IBS: 480.000,00 × 0,1% = **R$ 480,00**

**Créditos (só entradas de regime regular COM destaque — LC 214/2025, art. 346):**
- NF-e 2314: 62.000 × 0,9% = 558,00 | × 0,1% = 62,00
- NF-e 2316: 40.000 × 0,9% = 360,00 | × 0,1% = 40,00
- NF-e 2317: 60.000 × 0,9% = 540,00 | × 0,1% = 60,00
- NF-e 2313 (regime regular, **sem destaque**): **crédito zero**
- NF-e 2315 (Ponto Fixo, Simples): **crédito zero** (ver §entradas do Simples)
- Créditos: CBS **R$ 1.458,00** | IBS **R$ 162,00**

**Saldos da apuração-teste:**
- CBS: 4.320,00 − 1.458,00 = **R$ 2.862,00**
- IBS: 480,00 − 162,00 = **R$ 318,00**

**Recolhimento devido: R$ 0,00** — dispensado pelo ADCT art. 125, §4º, **desde que** as obrigações acessórias sejam cumpridas. Como as NF-e 2308, 2309, 2310 e 2312 estão irregulares (abaixo), a dispensa está **ameaçada enquanto não regularizadas**; se perdida, a exposição seria o saldo apurado (CBS 2.862,00 + IBS 318,00). A biblioteca **não diz** se a perda da dispensa atinge o mês inteiro ou apenas as operações irregulares — marquei isso como questão aberta (`QUESTIONS.md`).

**Compensação com PIS/COFINS:** o valor efetivamente recolhido de CBS/IBS em 2026 seria compensável com PIS/COFINS do período (ADCT art. 125, §1º). Mas, cumprindo as obrigações acessórias, o recolhimento é dispensado e **"nada há a compensar"** — a apuração é paralela e informativa [`lei_pis_cofins_compensacao.md`]. Não misture com a apuração normal de PIS/COFINS (que segue: base R$ 480.000, PIS 3.120,00, COFINS 14.400,00 — conferem com a soma das 12 notas de saída, R$ 480.000,00 ✓).

## Checagem documento a documento

Critério: a partir de **03/08/2026** é vedada ao regime regular a emissão de DFe **sem** o grupo `IBSCBS` (CST, cClassTrib, bases e alíquotas; em 2026 pIBSUF = 0,10, pIBSMun = 0,00, pCBS = 0,90 — NT 2025.002); documentos sem os grupos emitidos **antes** de 03/08 permanecem válidos (comunicado CGIBS).

| NF-e | Data | Valor (R$) | Grupo IBSCBS no XML | Situação | CBS/IBS apurados (R$) |
|---|---|---:|---|---|---|
| 2301 | 01/08 | 18.000,00 | não | **regular** (antes de 03/08 — válida) | 162,00 / 18,00 |
| 2302 | 01/08 | 24.000,00 | não | **regular** (antes de 03/08) | 216,00 / 24,00 |
| 2303 | 02/08 | 9.500,00 | não | **regular** (antes de 03/08) | 85,50 / 9,50 |
| 2304 | 02/08 | 31.000,00 | não | **regular** (antes de 03/08) | 279,00 / 31,00 |
| 2305 | 02/08 | 4.200,00 | não | **regular** (antes de 03/08) | 37,80 / 4,20 |
| 2306 | 04/08 | 42.000,00 | sim, alíquotas corretas | regular | 378,00 / 42,00 (conferido) |
| 2307 | 06/08 | 56.000,00 | sim, corretas | regular | 504,00 / 56,00 (conferido) |
| 2308 | 10/08 | 12.500,00 | **não** | **irregular** — após 03/08 sem o grupo | 112,50 / 12,50 |
| 2309 | 13/08 | 38.000,00 | sim, **alíquotas invertidas** (pIBSUF 0,90 / pCBS 0,10) | **irregular** | 342,00 / 38,00 corrigidos (o XML destaca 38,00 de CBS e 342,00 de IBS, trocados) |
| 2310 | 18/08 | 7.800,00 | **não** | **irregular** — após 03/08 sem o grupo | 70,20 / 7,80 |
| 2311 | 21/08 | 61.000,00 | sim, corretas | regular | 549,00 / 61,00 (conferido) |
| 2312 | 27/08 | 176.000,00 | **não** | **irregular** — após 03/08 sem o grupo | 1.584,00 / 176,00 |

Entradas (crédito só com destaque de fornecedor do regime regular):

| NF-e | Fornecedor | Valor (R$) | Crédito CBS/IBS (R$) | Motivo |
|---|---|---:|---|---|
| 2313 | Distribuidora Norte (CRT 3) | 48.000,00 | 0,00 / 0,00 | sem destaque: documento válido (emitida 02/08), mas art. 346 dá crédito só a aquisições **com destaque** |
| 2314 | Distribuidora Norte (CRT 3) | 62.000,00 | 558,00 / 62,00 | destaque correto (conferido) |
| 2315 | Ponto Fixo (CRT 1, Simples) | 15.000,00 | 0,00 / 0,00 | ver §entradas do Simples |
| 2316 | Logística Atlas (CRT 3) | 40.000,00 | 360,00 / 40,00 | destaque correto (conferido) |
| 2317 | Distribuidora Norte (CRT 3) | 60.000,00 | 540,00 / 60,00 | destaque correto (conferido) |

Observação de conciliação (atualizada após a resposta do cliente): as NF-e 2308, 2310 e 2312 aparecem nos arquivos **autorizadas** (cStat 100), mas com `tpAmb=2` (ambiente de **homologação**). A biblioteca **não descreve** o comportamento da validação em ambiente de teste; a **inferência** compatível com os arquivos — notas sem o grupo "autorizadas" em homologação — é que ali essa checagem não bloqueia. O cStat 100 dos arquivos, portanto, **não prova** autorização em produção. O cliente relatou que a mensagem de rejeição na produção era **"Rejeição: Grupo IBSCBS não informado para emitente do regime regular (NT 2025.002)"** — texto vindo do relato do cliente (o comunicado não cita a mensagem literal; promete apenas "rejeição específica (cStat 999/…)") e **compatível com a rejeição anunciada** no comunicado do CGIBS de julho/2026, o que indica que a produção está aplicando a regra. As duas notas rejeitadas **são candidatas** a esse mesmo perfil (sem o grupo, pós-03/08), mas **quais números exatos foram rejeitados o cliente não sabe** — e as notas rejeitadas não estão entre os arquivos que recebi. Não forcei conciliação: isso fica marcado como desconhecido (`QUESTIONS.md`).

## O que fazer com as notas irregulares

### Cuidado: o "contorno" do TI (rollback do emissor) NÃO é solução

O cliente relatou que, após as duas rejeições, o TI **"contornou" o problema rebaixando a versão do emissor** ("o sistema voltou a emitir"). Isso é o oposto da regularização:

- A rejeição tem mensagem confirmada pelo cliente — "Grupo IBSCBS não informado para emitente do regime regular (NT 2025.002)" — e é **compatível com** o que o comunicado do CGIBS de julho/2026 anuncia: a partir de 03/08/2026 documentos do regime regular **sem o grupo IBSCBS serão rejeitados** pelo fisco. A rejeição não é bug: é a regra sendo aplicada.
- Rebaixar o emissor fez o sistema "voltar a emitir" — ou seja, a versão anterior voltou a gerar XML **sem o grupo IBSCBS** (**inferência**: a versão rebaixada não implementa o grupo exigido pela NT 2025.002 — é a explicação compatível com a própria mensagem de rejeição). É o mesmo defeito que causou a rejeição. Se essas notas "voltaram a emitir" e foram **autorizadas em produção**, isso **contradiz o comunicado do CGIBS** e precisa ser verificado com urgência (pode ser confusão com homologação, ambiente errado, ou validação ainda não implantada por algum autorizador — a biblioteca não explica como contornar isso; não afiro de memória). Se continuam rejeitadas, aquelas vendas podem estar **sem DFe autorizado** — consequência e forma de regularização não estão descritas na biblioteca (marcado como aberto).
- De qualquer modo, o "contorno" **não cumpre a condição da dispensa de recolhimento** (destaque nos documentos fiscais — ADCT art. 125, §4º), e as emissões seguintes a 03/08 sem o grupo **ampliam** o universo de operações irregulares.
- **A solução é o caminho inverso: atualizar o emissor** para versão compatível com a **NT 2025.002**, que preenche o grupo `IBSCBS` (CST, cClassTrib, vBC, pIBSUF = 0,10, pIBSMun = 0,00, pCBS = 0,90 em 2026), e emitir com ele.

### "Se a SEFAZ autorizou, está regular, não?" — NÃO

Objeção levantada pelo gerente: "a SEFAZ autorizou essas notas (o TI voltou a versão antiga e passou); se autorizou, está regular". Não é o que as regras da biblioteca dizem:

1. **Autorização (cStat 100) não é atestado de conformidade.** O comunicado do CGIBS define a conduta devida: a partir de 03/08/2026 "**não será permitida a emissão** de DFe por contribuintes do regime regular **sem o preenchimento** dos grupos de IBS e CBS", e documentos sem os grupos "serão **rejeitados**". A vedação é da **emissão** — não depende de o autorizador conseguir fiscalizá-la. Se um autorizador deixou passar XML sem o grupo, a leitura compatível com o texto é **falha/atraso de implantação da validação** naquele ambiente, não permissão. A biblioteca **não** diz em nenhum lugar que nota autorizada sem o grupo passa a ser regular; o único salvo-conduto de validade que ela dá a documentos sem o grupo é para os emitidos **antes** de 03/08/2026.
2. **O ponto financeiro é a dispensa, e ela independe da autorização.** A dispensa de recolher em 2026 exige cumprir as obrigações acessórias, entre elas **destacar** IBS/CBS nos documentos fiscais (ADCT art. 125, §4º; LC 214/2025, art. 346). Nota sem o grupo `IBSCBS` **não tem destaque** — autorizada ou não, a condição segue descumprida. O comunicado é explícito: 2026 não tem penalidade (caráter educativo), "**sem prejuízo da perda da dispensa de recolhimento**" para quem não cumpre as acessórias. É aqui que o "passou na SEFAZ" não protege: a exposição (teto: CBS 2.862,00 + IBS 318,00 de agosto) continua.
3. **A "autorização" alegada também não está provada nos arquivos.** Os cStat 100 que existem nos arquivos são de `tpAmb=2` (**homologação**) — ambiente de teste, e neles essas notas sem o grupo aparecem "autorizadas"; a **inferência** compatível (a biblioteca não descreve a validação nesse ambiente) é que a checagem do grupo ali não bloqueia — é por isso que 2308/2310/2312 aparecem "autorizadas" lá. Na **produção**, o relato do próprio cliente aponta o contrário: o ambiente rejeitou notas com esse perfil. Não recebemos **nenhum XML de produção** das notas "que passaram" com o emissor rebaixado — nem chaves, nem números. **Verificar no portal do autorizador a lista de NF-e em produção** de 03/08 em diante antes de concluir qualquer coisa.
4. **E se de fato houver autorização em produção de notas sem o grupo?** A biblioteca não descreve esse cenário nem o que acontece com esses documentos (não afiro de memória) — tratar como **anomalia a esclarecer com SEFAZ/CGIBS**. O que não muda em nenhuma hipótese: a apuração-teste (os débitos são calculados de qualquer forma — art. 343/346) e o risco à dispensa enquanto não houver destaque.

**Resumo para o Paulo:** o critério de 2026 não é "a SEFAZ carimbou?"; é "calculei, destaquei, escriturei e fiz a apuração-teste?". O emissor rebaixado é justamente o que elimina o **destaque** — a condição mais importante para continuar sem pagar nada em 2026. Manter o rollback é trocar um incômodo (rejeição) pela perda potencial da dispensa.

- **2308, 2310, 2312 (sem grupo IBSCBS após 03/08):** a emissão não era permitida; o risco apontado pela norma é a **perda da dispensa de recolhimento** (ADCT art. 125, §4º; comunicado CGIBS). São as candidatas naturais às duas rejeições relatadas (mesmo perfil: pós-03/08, sem o grupo), mas os números exatos rejeitados permanecem **desconhecidos**. A biblioteca **não descreve o instrumento de regularização** (carta de correção, complementação, novo documento) — isso precisa ser confirmado com a SEFAZ/CGIBS; não posso afirmar de memória (não verificado na biblioteca).
- **2309 (alíquotas invertidas):** o emissor preencheu pIBSUF 0,90 e pCBS 0,10; a NT 2025.002 fixa **pIBSUF 0,10 e pCBS 0,90** em 2026. Corrija a **configuração do sistema** (o erro é sistemático de cadastro de alíquotas) e regularize o documento (mesma ressalva acima). Na apuração-teste lancei os valores legais corrigidos (CBS 342,00; IBS 38,00) e não os destacados no XML.
- **Não reemita "no susto":** as notas de 01–02/08 sem o grupo (2301–2305) **permanecem válidas** — não precisam de ajuste (comunicado CGIBS).
- Enquanto não regularizadas, a dispensa destas operações está em risco — é a prioridade da semana.

## Clientes do Simples Nacional e MEI (saídas)

**Errado não destacar nada.** A obrigação de destacar é **do emissor do regime regular** (art. 346), e o comunicado do CGIBS fala dos documentos emitidos "por contribuintes do regime regular", sem exceção por regime do destinatário. O art. 347 dispensa o **Simples/MEI enquanto emissores** da sua própria obrigação de destaque/apuração — não você. Logo: vendas 2308 (Ponto Fixo) e 2310 (MEI) **deveriam ter o grupo IBSCBS** de 03/08 em diante; configure o sistema para destacar em **todas** as saídas, inclusive Simples/MEI (o cliente é que não aproveitará o crédito). Atenção: o trecho da lei na biblioteca não lista exceção para consumidor final não contribuinte — se houver, não está verificável aqui.

## Entradas do Simples (NF-e 2315, Ponto Fixo)

**Não pode creditar.** Aquisição de optante do Simples gera crédito ao adquirente do regime regular **limitado ao valor efetivamente recolhido** pelo optante a título de IBS/CBS no Simples; em 2026, **sem destaque, não há crédito** (LC 214/2025, art. 347). Crédito zero também para a NF-e 2313 (fornecedor do regime regular sem destaque): o art. 346 só dá crédito a "aquisições de contribuintes do regime regular **com destaque**".

## O que muda a partir de 03/08/2026

1. **Obrigatório** o grupo `IBSCBS` (CST, cClassTrib, vBC, pIBSUF/pIBSMun/pCBS e valores) em NF-e/NFC-e/NFS-e/CT-e do regime regular — leiaute e alíquotas na **NT 2025.002**; sem ele, **rejeição** anunciada no **comunicado do CGIBS** (jul/2026). Documentos de antes de 03/08 sem o grupo continuam válidos.
2. Alíquotas de 2026 no leiaute: **pCBS 0,90, pIBSUF 0,10, pIBSMun 0,00** (NT 2025.002; ADCT art. 125; LC 214 art. 343).
3. Em 2026 não há **penalidade** pelo não preenchimento (caráter educativo), **mas** o descumprimento das obrigações acessórias **pode custar a dispensa de recolhimento** (comunicado CGIBS; ADCT art. 125, §4º).

## Ação recomendada (objetiva)

1. **Desfazer o rollback do TI imediatamente**: atualizar o emissor para versão compatível com a NT 2025.002 (grupo `IBSCBS`, alíquotas de 2026: pCBS 0,90, pIBSUF 0,10, pIBSMun 0,00). "Voltar a versão" só reproduz o defeito que causou a rejeição.
2. Auditar a **lista de NF-e emitidas em produção** de 03/08 em diante: confirmar quais notas existem/foram autorizadas, quais foram rejeitadas (inclusive identificar os números das duas rejeitadas, que o cliente não tem) e se as "reemissões" do emissor rebaixado chegaram a ser autorizadas — se sim, anomalia a esclarecer com o autorizador.
3. Corrigir o ERP para sempre emitir o grupo IBSCBS com as alíquotas de 2026 (resolve 2309 no futuro) e destacar também nas saídas para Simples/MEI e consumidor final.
4. Regularizar 2308/2309/2310/2312 com a SEFAZ/CGIBS (instrumento de regularização **não está na biblioteca** — confirmar lá; não afiro de memória).
5. Escriturar a apuração-teste de agosto (débitos 4.320,00/480,00; créditos 1.458,00/162,00) e guardá-la como prova do cumprimento do art. 346.
6. Não recolher nada em agosto e não gerar compensação com PIS/COFINS enquanto a dispensa estiver de pé (ADCT §4º; `lei_pis_cofins_compensacao.md`).
