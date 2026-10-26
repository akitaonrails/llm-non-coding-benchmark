# Orientação — CBS/IBS, agosto/2026 — Horizonte Comércio e Serviços Ltda.

**Para:** Paulo (gerente fiscal) · **Assunto:** Resposta ao e-mail "CBS/IBS — precisa fazer algo em agosto?"

**Resposta curta: a premissa está errada — há obrigações a cumprir em 2026.** O recolhimento de fato está
dispensado, mas **só sob condição**: cumprir as obrigações acessórias — destaque nos documentos
fiscais, escrituração e apuração-teste mensal (ADCT art. 125, §4º, in *library/lc214_2025_transicao.md*;
LC 214/2025, arts. 343 e 346, mesmo arquivo). Em agosto há **4 notas de saída irregulares** que,
se não forem sanadas, custam a dispensa (Comunicado CGIBS de julho/2026, in *library/cgibs_comunicado_03_08_2026.md*:
"sem prejuízo da perda da dispensa de recolhimento para quem não cumprir as obrigações acessórias").

## 1. O que é devido, o que é dispensado e sob que condição

- Em 2026 a CBS é cobrada a **0,9%** e o IBS a **0,1%** (IBS estadual 0,1% + municipal 0,0%) e os
  valores são **informativos**, para calibragem das alíquotas de referência (LC 214/2025, art. 343;
  ADCT art. 125, texto consolidado — *library/lc214_2025_transicao.md*; alíquotas no leiaute: NT 2025.002,
  pIBSUF=0,10, pIBSMun=0,00, pCBS=0,90 — *library/nt_nfe_grupo_ibscbs.md*).
- O mesmo contribuinte (regime regular) **deve destacar IBS/CBS nos documentos fiscais eletrônicos e
  apurar mensalmente débitos e créditos**, mesmo na vigência da dispensa (LC 214/2025, art. 346).
- **Dispensa:** o recolhimento do IBS/CBS de 2026 é dispensado ao contribuinte que cumprir as
  obrigações acessórias — destaque, escrituração e apuração-teste (ADCT art. 125, §4º).
  Cumprindo tudo → **recolhimento devido = R$ 0,00** (é o valor registrado em `apuracao_teste.json`).
- **Se não cumprir** (ex.: manter as 4 notas irregulares sem sanar): perde a dispensa e passa a ser
  exigível o saldo apurado do mês — **CBS 2.862,00 + IBS 318,00 = R$ 3.180,00** (aritmética no §2).
  Esse valor seria **compensável com o PIS/COFINS do mesmo período**, que em agosto somam
  3.120,00 + 14.400,00 = **17.520,00** e absorvem os 3.180,00 por completo, sem desembolso de caixa
  (ADCT art. 125, §1º e IN RFB a editar — *library/lei_pis_cofins_compensacao.md*). Para quem cumpre
  as acessórias, nada há a compensar: a apuração é paralela e informativa (mesmo arquivo).
- Penalidades: em 2026 não há multas pelo não preenchimento dos grupos (caráter educativo), **mas** a
  dispensa continua condicionada ao cumprimento das acessórias (Comunicado CGIBS jul/2026).

## 2. A apuração-teste de agosto (os números)

Base legal dos débitos: art. 343 (alíquotas sobre as operações). Créditos: art. 346 (aquisições de
contribuintes do **regime regular com destaque**). Débitos apurados sobre o valor integral das saídas,
**inclusive as notas irregulares** — a irregularidade atinge a dispensa e o crédito do destinatário,
não a existência do débito.

### Saídas (débitos = valor × alíquota; CBS 0,90% e IBS 0,10%)

| NF-e | Data | Destinatário | Valor | CBS 0,90% | IBS 0,10% | Situação |
|---:|---|---|---:|---:|---:|---|
| 2301 | 01/08 | Brisa (regular) | 18.000,00 | 162,00 | 18,00 | regular (sem grupo, antes de 03/08 → válida) |
| 2302 | 01/08 | Serra Verde (regular) | 24.000,00 | 216,00 | 24,00 | regular (sem grupo, antes de 03/08 → válida) |
| 2303 | 02/08 | Ponto Fixo (Simples) | 9.500,00 | 85,50 | 9,50 | regular (antes de 03/08 → válida) |
| 2304 | 02/08 | Brisa (regular) | 31.000,00 | 279,00 | 31,00 | regular (sem grupo, antes de 03/08 → válida) |
| 2305 | 02/08 | J. Silva (MEI) | 4.200,00 | 37,80 | 4,20 | regular (antes de 03/08 → válida) |
| 2306 | 04/08 | Brisa (regular) | 42.000,00 | 378,00 | 42,00 | regular (destaque confere) |
| 2307 | 06/08 | Serra Verde (regular) | 56.000,00 | 504,00 | 56,00 | regular (destaque confere) |
| 2308 | 10/08 | Ponto Fixo (Simples) | 12.500,00 | 112,50 | 12,50 | **irregular** — sem grupo após 03/08 |
| 2309 | 13/08 | Brisa (regular) | 38.000,00 | 342,00 | 38,00 | **irregular** — alíquotas invertidas no destaque |
| 2310 | 18/08 | J. Silva (MEI) | 7.800,00 | 70,20 | 7,80 | **irregular** — sem grupo após 03/08 |
| 2311 | 21/08 | Serra Verde (regular) | 61.000,00 | 549,00 | 61,00 | regular (destaque confere) |
| 2312 | 27/08 | Brisa (regular) | 176.000,00 | 1.584,00 | 176,00 | **irregular** — sem grupo após 03/08 |
| **Total** | | | **480.000,00** | **4.320,00** | **480,00** | |

Aritmética dos totais: CBS = 0,90% × 480.000,00 = **4.320,00**; IBS = 0,10% × 480.000,00 = **480,00**
(soma item a item confere: 162+216+85,50+279+37,80+378+504+112,50+342+70,20+549+1.584 = 4.320,00;
18+24+9,50+31+4,20+42+56+12,50+38+7,80+61+176 = 480,00).

**Conciliação com a apuração normal:** o somatório das 12 notas (480.000,00) é exatamente a base de
PIS/COFINS de agosto da apuração normal (PIS 0,65% × 480.000,00 = 3.120,00; COFINS 3,00% × 480.000,00
= 14.400,00), e os vPIS/vCOFINS destacados nas notas somam 3.120,00 e 14.400,00 — i.e., o arquivo de
saídas está completo e amarra com o livro. Nada a reconciliar em aberto.

### Entradas (créditos)

| NF-e | Data | Fornecedor | Valor | Crédito CBS | Crédito IBS | Motivo |
|---:|---|---|---:|---:|---:|---|
| 2313 | 02/08 | Distribuidora Norte (regular, CRT 3) | 48.000,00 | 0,00 | 0,00 | documento válido (pré-03/08), **mas sem destaque → sem crédito** (art. 346) |
| 2314 | 05/08 | Distribuidora Norte (regular) | 62.000,00 | 558,00 | 62,00 | destaque correto (IBSUF 62,00 + IBSMun 0,00; CBS 558,00) → crédito integral |
| 2315 | 09/08 | Ponto Fixo (**Simples**, CRT 1) | 15.000,00 | 0,00 | 0,00 | art. 347: crédito limitado ao efetivamente recolhido pelo optante; em 2026, sem destaque, não há crédito |
| 2316 | 16/08 | Logística Atlas (CRT 3) * | 40.000,00 | 360,00 | 40,00 | destaque correto → crédito (premissa: emitente do regime regular — ver QUESTIONS.md) |
| 2317 | 22/08 | Distribuidora Norte (regular) | 60.000,00 | 540,00 | 60,00 | destaque correto → crédito |
| **Total** | | | **225.000,00** | **1.458,00** | **162,00** | |

### Saldo do mês (informativo)

- CBS: 4.320,00 − 1.458,00 = **2.862,00**
- IBS: 480,00 − 162,00 = **318,00**
- Teórico do mês: 2.862,00 + 318,00 = **3.180,00** → **não recolhido**, pela dispensa do ADCT art. 125,
  §4º (condicionada ao cumprimento das acessórias).

## 3. O que fazer com as notas irregulares

> **"Mas a SEFAZ autorizou essas notas (o TI voltou a versão antiga do emissor e passou). Se
> autorizou, está regular, não?" — Não.** Autorização é o **crivo técnico do validador disponível
> naquele momento**; não convalida conteúdo nem substitui a obrigação legal. Quem impõe o destaque
> é a **lei** — o art. 346 da LC 214/2025 exige que o regime regular destaque IBS/CBS nos documentos
> eletrônicos e apure mensalmente, **mesmo durante a dispensa**. O validador da SEFAZ é só a barreira
> que captura o descumprimento (por isso o Comunicado CGIBS diz que NF-e de regime regular sem o grupo
> é **rejeitada**). Voltar a versão antiga do emissor não torna a nota regular: **remove o detector do
> erro**. O raciocínio "passou no validador antigo → está correta" tem estrutura idêntica a "o
> detector de velocidade foi desligado, então eu não estava acima do limite". E há um efeito colateral
> prático: com a versão antiga o grupo simplesmente **não é preenchido** — é o que produz documentos
> sem destaque, como as três autorizadas sem grupo (2308/2310/2312; e a Brisa, destinatária regular,
> ficou sem crédito). A dispensa do recolhimento, lembre-se, é **condicionada ao cumprimento das
> obrigações acessórias** (destaque,
> escrituração, apuração — ADCT art. 125, §4º); manter notas autorizadas-but-sem-destaque é manter a
> condição descumprida. E o "contorno" não é o caminho oficial: a regra em vigor manda **rejeitar**
> esses documentos (Comunicado CGIBS; leiaute na NT 2025.002) — e foi exatamente essa rejeição que
> apareceu para vocês ("Grupo IBSCBS não informado", NT 2025.002). Corretivo: restaurar a versão que
> preenche o grupo (a que gerou 2306/2307/2311) e cancelar/reemitir as três.

1. **NF-e 2309 (13/08, R$ 38.000,00)** — o grupo IBSCBS foi preenchido com **alíquotas invertidas**:
   destacou pIBSUF=0,90 (IBS 342,00) e pCBS=0,10 (CBS 38,00). Pela NT 2025.002, em 2026 é
   pIBSUF=0,10, pIBSMun=0,00, pCBS=0,90 → correto seria **IBS 38,00 e CBS 342,00**. A apuração-teste
   usa os valores corretos, mas o destaque na NF-e está errado: **cancele e reemita** com as alíquotas
   certas e revise a configuração do emissor. (Enquanto o destaque estiver errado, a Brisa não consegue
   se creditar do valor correto.)
2. **NF-e 2308 (10/08), 2310 (18/08) e 2312 (27/08)** — emitidas **depois de 03/08/2026 sem o grupo
   IBSCBS**. A obrigatoriedade é do **emissor do regime regular** e independe do regime do
   destinatário: pelo Comunicado CGIBS esses documentos **são rejeitados** — e foi exatamente essa
   rejeição que vocês viram: *"Rejeição: Grupo IBSCBS não informado para emitente do regime regular
   (NT 2025.002)"*. O "contorno" do TI (voltar a versão do emissor) é a **causa raiz**: ao voltar a
   versão anterior, o sistema "voltou a emitir" sem o grupo sem encontrar a barreira da validação
   nova. Autorização obtida por contorno, porém, **não sana o documento**: ele continua sem o
   destaque exigido do regime regular (art. 346; leiaute na NT 2025.002). Conduta: **desfazer o
   rollback** (restaurar emissor que preenche o IBSCBS sempre — cobrar a correção do fornecedor do
   software) e **cancelar/reemitir** as três com destaque. Manter documentos irregulares em 2026 põe
   em risco a dispensa do recolhimento (ADCT art. 125, §4º).

   **As duas notas rejeitadas**: rejeição não gera documento fiscal — elas, por si, **não entram na
   apuração**. As operações subjacentes parecem estar cobertas pelas 12 autorizadas: a soma
   480.000,00 amarra exatamente com a base de PIS/COFINS da apuração normal (§2). Os números/chaves
   exatos das tentativas rejeitadas permanecem **desconhecidos** (não há XML delas em `documents/` e o
   cliente não dispunha da informação) — detalhe operacional que não altera esta apuração; se aparecer
   algum documento **autorizado** que não nos foi enviado, a apuração deve ser refeita.
3. As notas **sem grupo emitidas antes de 03/08** (2301–2305) **permanecem válidas** — não refaçam
   (Comunicado CGIBS). Entradas sem destaque de fornecedor regular emitidas antes de 03/08 (NF-e
   2313) também são válidas, apenas não geram crédito (art. 346).

## 4. Clientes do Simples Nacional e MEI (as suas perguntas)

- **"Para cliente do Simples e MEI eu não destaco nada, certo?" — Errado.** Quem está dispensado do
  destaque e da apuração em 2026 é **o próprio optante do Simples/MEI** nos documentos que **ele**
  emite (LC 214/2025, art. 347). A sua obrigação é de **emissor do regime regular** (art. 346 +
  Comunicado CGIBS): do dia 03/08 em diante, **toda** NF-e sua precisa do grupo IBSCBS preenchido,
  venda para Brisa, Ponto Fixo (Simples) ou J. Silva (MEI). É exatamente o que torna as NF-e 2308 e
  2310 irregulares.
- **"O IBS/CBS na nota de entrada do Ponto Fixo (Simples) — posso creditar?" — Não.** A NF-e 2315
  (15.000,00) não tem destaque e, para aquisições de optantes do Simples, o crédito em 2026 é
  **limitado ao valor efetivamente recolhido pelo optante a título de IBS/CBS no Simples**; como o
  Simples não destaca em 2026, **sem destaque não há crédito** (art. 347). Crédito existe só em
  aquisição de contribuinte **do regime regular com destaque** (art. 346) — por isso 2314, 2316 e 2317
  geram crédito, e a NF-e 2313 (regular, porém pré-03/08 e sem destaque) **não** gera. (Confirmado
  pelo cliente: Ponto Fixo é do Simples e a nota dele veio sem qualquer referência a IBS/CBS — como
  no XML da 2315; nada muda.)

## 5. O que muda a partir de 03/08/2026

- **Antes de 03/08:** NF-e sem o grupo IBSCBS podia ser emitida e **permanece válida** (documentos
  2301–2305 e a entrada 2313 se explicam por isso).
- **A partir de 03/08:** contribuinte do regime regular **não pode emitir** NF-e/NFC-e/NFS-e/CT-e sem
  os grupos IBS/CBS (CST, cClassTrib, bases e alíquotas) — o documento **é rejeitado** (Comunicado
  CGIBS; leiaute do grupo na NT 2025.002: `IBSCBS` com CST, cClassTrib, vBC, pIBSUF 0,10, pIBSMun 0,00,
  pCBS 0,90 e totalizador `IBSCBSTot`). E foi isso que aconteceu em agosto: as duas emissões rejeitadas
  receberam exatamente "Grupo IBSCBS não informado para emitente do regime regular (NT 2025.002)" —
  a regra **está valendo**. O retorno de versão do emissor feito pelo TI ("contorno") não resolve:
  só desliga a validação local e faz o documento sair sem destaque, que é a irregularidade. Em agosto,
  2306, 2307 e 2311 já saíram com o grupo — a versão correta existia; **restaurem-na**.
- **Durante 2026:** sem penalidades pelo não preenchimento (caráter educativo), **mas** a dispensa do
  recolhimento se perde para quem não cumprir as obrigações acessórias. Ou seja: o "não se paga nada"
  do Paulo só vale enquanto se **destaca, escritura e apura** todo mês.

## 6. Plano de ação (objetivo)

1. Corrigir o software emissor: grupo IBSCBS sempre preenchido (CST, cClassTrib, bases e alíquotas
   pIBSUF 0,10 / pIBSMun 0,00 / pCBS 0,90, conforme NT 2025.002), inclusive para destinatários
   Simples/MEI. Os valores de CST/cClassTrib aplicáveis a cada venda devem ser confirmados no Manual
   de Orientamento (não verificados na biblioteca).
2. Cancelar e reemitir as NF-e 2308, 2309, 2310 e 2312 com destaque correto; **desfazer o rollback do
   emissor** (a versão que emitia certo já existiu — 2306/2307/2311 saíram com o grupo) e conferir no
   log do emissor as tentativas rejeitadas e qual nota autorizada cobre cada operação.
3. Manter a apuração-teste mensal (esta) e a escrituração — é a condição da dispensa (ADCT art. 125, §4º).
4. Conferir o regime dos fornecedores antes de creditar: só há crédito com emitente do regime regular
   **e** destaque (2313 não gera; 2315, do Simples, não gera em 2026).
5. Nada lanç/compensar no PIS/COFINS deste mês: cumprindo as acessórias, o recolhimento é dispensado e
   não há valor pago a compensar (*library/lei_pis_cofins_compensacao.md*).

---
*Todas as citações acima restringem-se à biblioteca de referência (`library/INDEX.md`): LC 214/2025
arts. 343–348 e ADCT art. 125 (EC 132/2023); Comunicado CGIBS jul/2026; NT NF-e 2025.002; ADCT art. 125
§1º e IN RFB a editar. O que não está na biblioteca (ex.: procedimentos de cancelamento/reemissão de
NF-e) é dito como orientação operacional de senso comum e está sinalizado como não verificado na
biblioteca; a IN RFB que disciplina a compensação ainda não foi editada.*
