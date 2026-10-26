# Orientação — CBS/IBS, apuração-teste de agosto/2026

**Para:** Paulo, gerente fiscal — **Horizonte Comércio e Serviços Ltda.** (CNPJ 27.119.804/0001-30, regime regular, CRT 3)
**Base legal usada:** apenas a biblioteca do engajamento — LC 214/2025 arts. 343, 346 e 347 e ADCT art. 125 §§1º e 4º (`lc214_2025_transicao.md`); Comunicado CGIBS de julho/2026 (`cgibs_comunicado_03_08_2026.md`); NT 2025.002 — grupo IBSCBS (`nt_nfe_grupo_ibscbs.md`); compensação PIS/COFINS (`lei_pis_cofins_compensacao.md`).

## 1. "Em 2026 é só informativo, não precisa fazer nada" — errado

Em 2026 o recolhimento de IBS (0,1%) e CBS (0,9%) é **dispensado**, mas a dispensa é **condicionada**: ela vale "para o contribuinte que cumprir as obrigações acessórias" — destaque nos documentos fiscais, escrituração e **apuração-teste mensal** (ADCT art. 125, §4º, na redação da LC 214; LC 214 arts. 343 e 346). Ou seja: quase nada a *pagar*, mas **muito a fazer**. Quem não cumpre as acessórias fica sujeito à **perda da dispensa** (Comunicado CGIBS). A apuração de agosto está em `apuracao_teste.json`.

## 2. O que é devido em agosto/2026

**Recolhimento devido: R$ 0,00**, sob a dispensa do ADCT art. 125, §4º. A apuração-teste (informativa) fecha assim:

| | CBS (0,90%) | IBS (0,10%) |
|---|---:|---:|
| Débitos s/ saídas de R$ 480.000,00 | 480.000 × 0,9% = **4.320,00** | 480.000 × 0,1% = **480,00** |
| Créditos (entradas c/ destaque — NF-e 2314, 2316, 2317) | **(1.458,00)** | **(162,00)** |
| **Saldo apurado** | **2.862,00** | **318,00** |

Esse saldo **não é pago em 2026** enquanto mantida a dispensa — mas é exatamente a exposição (R$ 3.180,00) se a dispensa for perdida pelo descumprimento apontado no item 3. Como nada foi recolhido, **nada há a compensar com PIS/COFINS** (`lei_pis_cofins_compensacao.md`; ADCT art. 125, §1º — a compensação só existe para valor efetivamente recolhido). A apuração de PIS/COFINS do mês segue normal e independente; a base das saídas (R$ 480.000,00) confere com a sua apuração cumulativa.

## 3. Notas irregulares — 4 documentos, e é aqui que a dispensa está em risco

| NF-e | Data | Problema | Valor |
|---|---|---|---:|
| 2308 | 10/08 | emitida **sem grupo IBSCBS** depois de 03/08 (venda p/ Simples) | 12.500,00 |
| 2309 | 13/08 | alíquotas **invertidas**: destacou IBS 0,90% (R$ 342,00) e CBS 0,10% (R$ 38,00); o correto é **CBS R$ 342,00 e IBS R$ 38,00** (NT 2025.002: pCBS 0,90, pIBSUF 0,10) | 38.000,00 |
| 2310 | 18/08 | sem grupo IBSCBS depois de 03/08 (venda p/ MEI) | 7.800,00 |
| 2312 | 27/08 | sem grupo IBSCBS depois de 03/08 (venda p/ Brisa) | 176.000,00 |

**Causa-raiz confirmada pelo cliente:** a rejeição da SEFAZ dizia "Rejeição: Grupo IBSCBS não informado para emitente do regime regular (NT 2025.002)" — exatamente o bloqueio previsto no Comunicado CGIBS — e o TI a "contornou" **revertendo a versão do emissor** para uma leiaute antigo, sem o grupo. Logo, a emissão de 2308, 2310 e 2312 sem IBSCBS após 03/08 não foi falha do sistema, foi **workaround deliberado** (a 2309 é outro defeito: alíquotas mal configuradas). Isso agrava o risco de perda da dispensa e tem de ser desfeito de imediato.

**"Mas a SEFAZ autorizou essas notas (o TI voltou a versão e passou) — se autorizou, está regular?"** Não — e veja primeiro o que a biblioteca diz. O Comunicado CGIBS estabelece que **não é permitida a emissão** sem os grupos de IBS/CBS a partir de 03/08/2026 e que documentos sem os grupos serão **rejeitados**: a rejeição é só o controle automático de uma regra que **já proíbe** a emissão. E **nada na biblioteca convalida a omissão por ter havido autorização**: o comunicado comina a **perda da dispensa** a quem "não cumprir as obrigações acessórias" — o critério é o cumprimento (destaque no documento fiscal), não a concessão do protocolo. A posição do fisco sobre esse conteúdo está na própria mensagem de rejeição citada acima: o mesmo conteúdo, emitido pelo emissor conforme, é **bloqueado**; ele não se torna regular porque o emissor desatualizado desviou do bloqueio. Nossa leitura — que registramos como **premissa fora da biblioteca**, argumento, não citação de autoridade — é que o protocolo cStat 100 desses arquivos valida **o leiaute transmitido**, não o cumprimento das obrigações do emitente; mas mesmo sem essa premissa a conclusão não muda, porque nenhuma regra da biblioteca cura a omissão via autorização. O rollback do TI não consertou o documento — fez o arquivo chegar por um caminho em que a checagem nem existe, como passar por uma cancela que não estava aferindo. Por isso as notas seguem marcadas como irregulares na apuração-teste, com o débito lançado pelos valores corretos.

O que fazer: **(a)** desfazer o rollback do TI e colocar o emissor no leiaute da NT 2025.002, gravando sempre o grupo `IBSCBS` (CST, cClassTrib, base, pIBSUF 0,10 / pIBSMun 0,00 / pCBS 0,90 e totais `IBSCBSTot`) — não existe "contorno" legítimo para a rejeição, ela é a regra em vigor; **(b)** manter as 4 notas na apuração-teste com os valores **corretos** (foi o que fizemos no JSON; a 2309 foi corrigida para CBS 342,00 / IBS 38,00) e escriturá-las; **(c)** o Comunicado CGIBS diz que durante 2026 "não haverá aplicação de penalidades **pelo não preenchimento**" (caráter educativo) — a ressalva de penalidades da biblioteca cobre o **não** preenchimento dos grupos (2308/2310/2312); para nota **preenchida errada** (inversão de alíquotas da 2309) a biblioteca **não** afirma a mesma ressalva — ponto de atenção; em qualquer caso, o risco concreto é a perda da dispensa de recolhimento. **Não está na biblioteca** qual o procedimento de regularização/correção dessas notas em 2026 nem se a perda da dispensa atingiria o mês inteiro ou só as operações irregulares — segue como ignorado declarado em `PERGUNTAS.md`; não invente correção "de memória".

## 4. Cliente do Simples e do MEI — "não destaco nada, certo?" — errado

O destaque é **obrigação sua, emitente do regime regular**, independentemente do regime do cliente (LC 214 art. 346, que não condiciona o destaque ao regime do destinatário). O cliente Simples/MEI **não está sujeito, em 2026, ao destaque nem à apuração** (LC 214 art. 347) — essa é a regra **dele**, e não o dispensa a você. Desde **03/08/2026** o documento sem o grupo é **rejeitado** para regime regular (Comunicado CGIBS) — as rejeições que você viu eram o fisco **funcionando corretamente** (mensagem citada pelo cliente: "Grupo IBSCBS não informado para emitente do regime regular"); o "contorno" do TI — voltar a versão do emissor — não foi conserto, foi a origem das notas irregulares 2308 e 2310 (justamente as vendas para Simples/MEI) e de 2312. Vendas antes de 03/08 sem destaque (2301–2305, incl. 2303/2305 p/ Simples e MEI) **permanecem válidas** (Comunicado CGIBS).

## 5. Entradas — o que pode creditar

- **Ponto Fixo (Simples), NF-e 2315 (R$ 15.000,00): não pode creditar.** Aquisição de optante do Simples gera crédito ao adquirente **limitado ao valor efetivamente recolhido** pelo optante a título de IBS/CBS no Simples — e **em 2026, sem destaque, não há crédito** (LC 214 art. 347). A NF-e 2315 foi emitida **sem destaque** (o Simples não está sujeito a destacar em 2026), logo crédito R$ 0,00.
- **NF-e 2313 (Distribuidora Norte, R$ 48.000,00): também não.** Crédito exige aquisição de contribuinte do regime regular **com destaque** (LC 214 art. 346); a nota foi emitida em 02/08, antes da obrigatoriedade do grupo (documento válido — Comunicado CGIBS), porém **sem destaque** de IBS/CBS, o que já basta para zerar o crédito.
- **Creditáveis: 2314 (CBS 558,00 / IBS 62,00), 2316 (CBS 360,00 / IBS 40,00) e 2317 (CBS 540,00 / IBS 60,00)** — total CBS 1.458,00 e IBS 162,00. Se fornecedor do regime regular deixar de destacar depois de 03/08, a nota será rejeitada; não aceite "recibo" sem destaque.

## 6. O que muda a partir de 03/08/2026

Para contribuinte do regime regular, a emissão de NF-e/NFC-e/NFS-e nacional/CT-e **sem os grupos de IBS e CBS passa a ser rejeitada** (Comunicado CGIBS; layout na NT 2025.002). Documentos anteriores a 03/08 sem os grupos continuam válidos. O Comunicado diz que durante 2026 não haverá penalidades **pelo não preenchimento** dos grupos (caráter educativo) — a biblioteca não afirma ressalva para preenchimento **errado** (o caso da 2309) — sempre **sem prejuízo da perda da dispensa de recolhimento** para quem descumprir as acessórias, por isso o item 3 é prioridade.

## 7. Premissas assumidas (importante)

1. As 17 NF-e da pasta `documents/` representam as operações reais de agosto/2026 — embora estejam marcadas com ambiente de homologação (`tpAmb` 2) e aviso "documento fictício" no texto livre, tratamos os arquivos como o arquivo fiscal do mês, conforme recebido.
2. Regime dos **fornecedores** (Distribuidora Norte, Logística Atlas) inferido do `CRT` 3 das próprias notas (regime regular), já que a carteira fornecida só lista clientes.
3. Débitos da apuração-teste calculados sobre **todas** as saídas do mês às alíquotas de 2026 (CBS 0,90% / IBS 0,10%), com os documentos sem/erroneamente destacado marcados como irregulares — a exigência de destaque não altera a incidência aferida na apuração-teste (LC 214 arts. 343 e 346). Subtotais: grupo IBSCBS preenchido no documento R$ 197.000,00 (CBS 1.773,00 / IBS 197,00 — inclui a 2309, com alíquotas invertidas no documento, débitos lançados pelos valores corretos); sem o grupo R$ 283.000,00 (CBS 2.547,00 / IBS 283,00); 197.000,00 + 283.000,00 = 480.000,00.

**Resumo executivo:** nada a pagar em agosto (R$ 0,00 sob a dispensa), mas entregue a apuração-teste mensal, destaque IBS/CBS em **todas** as notas (inclusive p/ Simples e MEI) a partir de agora, e nada de crédito sobre entradas do Simples ou sem destaque. Risco em aberto: R$ 3.180,00 se a dispensa for perdida pelas 4 notas irregulares.
