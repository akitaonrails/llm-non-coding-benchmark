# Memória de cálculo — DAS maio/2026 — Lumen Soluções Digitais ME

Apuração do Simples Nacional de **maio/2026** (fato gerador), conforme `CONTRACT.md`.
Toda citação abaixo aponta para um arquivo listado em `library/INDEX.md`. Nada fora da
biblioteca foi usado como fundamento; o que não está na biblioteca está explicitamente
rotulado como **não verificado** ou **em aberto**.

## 0. Resultado (resumo)

| Item | Valor |
|---|---:|
| RBT12 (mai/2025–abr/2026) | R$ 1.020.000,00 |
| Folha 12m (resumo da folha) | R$ 284.600,00 |
| Fator R | 27,90% (< 28%) → **Anexo V** para os serviços de TI |
| Faixa (RBT12 1.020.000) | 4ª faixa em ambos os anexos |
| Alíquota efetiva serviços (Anexo V, 4ª) | 18,8235% |
| Alíquota efetiva locação (Anexo III, 4ª, sem ISS) | 8,4415% |
| DAS serviços (R$ 78.000,00) | R$ 14.682,35 |
| DAS locação (R$ 6.000,00) | R$ 506,49 |
| **DAS total maio/2026** | **R$ 15.188,84** |

O pedido do sócio ("repetir o Anexo V com a alíquota da faixa") foi **confirmado pelo
cálculo do Fator R, não assumido** — e a alíquota correta é a **efetiva** (§1º-A), não a
nominal da faixa. Além disso, a locação de notebooks **não** vai "junto com os serviços":
é segregada e tributada pelo Anexo III sem ISS (ver §5 e §7).

## 1. Fontes

Documento do cliente usado em cada passo:

- `documents/faturamento_12_meses.csv` — receitas mai/2025–abr/2026 (RBT12).
- `documents/resumo_folha_12_meses.csv` — folha (salários + pró-labore + encargo patronal/FGTS).
- `documents/notas_emitidas_maio.md` — notas fiscais de maio/2026 (inclui estorno e locação).
- `documents/extrato_maio_2026.csv` — movimentação financeira de maio (verificações de consistência).
- `documents/extrato_maio_2026.pdf` — mesmo extrato em PDF; conferido contra o CSV na auditoria
  (mesmas 15 transações e mesmos saldos — §9). Ressalva: rodapé do PDF declara "Banco
  Meridional S.A. is a fictitious institution created for a benchmark; no real account
  exists" — documento de banco fictício, registrado em §12.5.
- `documents/nfe_000512_locacao.xml` — XML da NF-e 000.512 (locação).
- `documents/email_socio.txt` — informações do sócio (pagamento do pró-labore de abril; expectativa de Anexo V).

Fundamentos (todos em `library/`):

- **[L1]** `library/lc123_art18_fator_r.md` — LC 123/2006, art. 18, §§1º, 1º-A, 5º-J, 5º-K, 5º-M;
  Res. CGSN 140/2018, arts. 25, 26 (§§1º–2º); segregar receitas (§4º); devoluções/cancelamentos.
- **[L2]** `library/anexos_iii_v_tabelas.md` — tabelas dos Anexos III e V (LC 155/2016) e
  repartição do Anexo III, 4ª faixa.
- **[L3]** `library/locacao_bens_moveis_iss.md` — locação de bens móveis: Anexo III deduzida a
  parcela de ISS; LC 123/2006, art. 18, §5º-A; Súmula Vinculante 31 (STF); Res. CGSN 140, art. 25, §1º, V.

## 2. RBT12

Base: RBT12 = "receita bruta acumulada nos doze meses anteriores ao do período de apuração"
([L1], §1º). Para maio/2026: mai/2025–abr/2026, exatamente o intervalo do arquivo:

78.000 + 81.500 + 84.000 + 86.000 + 79.500 + 90.000 + 88.000 + 92.000 + 85.000 + 83.000 + 86.000 + 87.000
= **R$ 1.020.000,00**

*Premissa A1:* o `faturamento_12_meses.csv` é a receita bruta total (todas as atividades) e
já está líquido de eventuais estornos dos próprios meses. Se houver locação de bens móveis
em meses anteriores a mai/2026, ela já estaria incluída; o uso do RBT12 **total** para
determinar faixa e alíquota efetiva de cada anexo é a leitura literal do §1º-A ([L1]) —
ver Premissa A5.

## 3. Classificação nota a nota (maio/2026)

Fonte: `documents/notas_emitidas_maio.md`; valores conferidos contra o extrato (§9).

| Documento | Descrição | Valor | Classificação |
|---|---|---:|---|
| NFS-e 1181 | Desenvolvimento de software — sprint 11 | 18.000,00 | serviço de TI (desenvolvimento) — [L1] §5º-J |
| NFS-e 1182 | Sustentação mensal — Cliente Orla | 12.500,00 | serviço de TI (sustentação/suporte) — [L1] §5º-J |
| NFS-e 1183 | Consultoria de arquitetura | 9.800,00 | serviço de TI (consultoria em TI) — *Premissa A2* |
| NFS-e 1184 | Desenvolvimento — módulo fiscal | 22.000,00 | serviço de TI (desenvolvimento) — [L1] §5º-J |
| NFS-e 1185 | Suporte técnico | 6.700,00 | serviço de TI (suporte) — [L1] §5º-J |
| NFS-e 1186 | Treinamento equipe | 4.500,00 | serviço de TI — *Premissa A2* |
| NFS-e 1187 | Desenvolvimento — integração | 8.500,00 | serviço de TI (desenvolvimento) — [L1] §5º-J |
| NFS-e 1188 | Estorno parcial da 1184 (glosa de escopo acordada) | (4.000,00) | cancelamento/estorno — reduz a receita do mês (§4) |
| NF-e 000.512 | Locação de 20 notebooks — maio | 6.000,00 | **locação de bens móveis** — [L3]; Anexo III sem ISS (§5 e §7) |

*Premissa A2:* a biblioteca descreve "atividades de prestação de serviços de TI
(desenvolvimento, licenciamento, suporte etc.)" ([L1], §5º-J) mas **não** traz a lista
exaustiva de atividades de cada anexo. Não é verificável na biblioteca se "consultoria de
arquitetura" e "treinamento" são equiparadas a serviços de TI para fins de Fator R. Elas
foram tratadas como serviços de TI (atividade-fim da empresa, corroborada pelo e-mail do
sócio "a gente pagava pelo Anexo V (TI)"). Se alguma delas não for atividade de TI, muda
a tributação daquela nota e o Fator R pode ser recalculado. Perguntado (1ª rodada), o
cliente não trouxe informação adicional; a premissa **permanece** e o ponto fica
sinalizado como em aberto.

*Observação (não verificado na biblioteca):* o CRT=1 do XML indicaria Simples Nacional —
Optante pelo Simples. A biblioteca não traz tabela de CRT; não é possível verificar se a
empresa é optante pelo Simples a partir da biblioteca. Assumido a partir do contexto do
contrato (cálculo de DAS).

Soma dos serviços brutos: 18.000 + 12.500 + 9.800 + 22.000 + 6.700 + 4.500 + 8.500 =
**R$ 82.000,00** (confere com a linha de totais do arquivo de notas).

## 4. O estorno (NFS-e 1188 / glosa da 1184)

Regra: "o cancelamento/estorno de serviço reduz a receita do mês em que ocorrer"
([L1], Devoluções/cancelamentos). A glosa de R$ 4.000,00 foi estornada em maio/2026
(nota 1188 emitida em maio; PIX de devolução em 2026-05-29 no extrato), portanto reduz a
receita de **maio/2026**:

Receita de serviços maio/2026 = 82.000,00 − 4.000,00 = **R$ 78.000,00**

Não se estorna a nota 1184 no mês original: o arquivo de notas e o extrato tratam a glosa
como evento de maio. O RBT12 (§2) é histórico e não foi ajustado — não há informação na
biblioteca nem nos documentos de que faturamentos anteriores tenham sofrido estornos.
Perguntado, o cliente informou não ter informação adicional; fica **em aberto**, sem
impacto sobre o uso do RBT12 do arquivo (Premissa A1).

## 5. Locação de bens móveis (NF-e 000.512)

O XML (mod 55, CFOP 5949, natOp "Locação de bens móveis", vProd 6.000,00) e a tabela de
notas confirmam: R$ 6.000,00 de **locação de bens móveis**.

Tratamento: locação de bens móveis **não é serviço para fins de ISS** (Súmula Vinculante 31)
e é tributada "na forma do Anexo III, deduzida a parcela correspondente ao ISS" ([L3]).
Logo, a locação **não** acompanha os serviços do Anexo V (ao contrário do palpite do e-mail
"acho que vai junto com os serviços") e também não sofre a alíquota efetiva do Anexo V:

- Segregação obrigatória por atividade ([L1], art. 18, §4º).
- Alíquota = efetiva do Anexo III, 4ª faixa, **menos a parcela de ISS** da repartição.

*Premissa A3:* a parcela de ISS a deduzir é a percentagem de repartição do anexo/faixa
(ISS 32,50% na 4ª faixa do Anexo III, [L2]) aplicada sobre a alíquota efetiva. A biblioteca
diz "deduzida a parcela correspondente ao ISS" ([L3]) e fornece o percentual de repartição
([L2]), mas não descreve a mecânica exata; essa é a leitura mais direta. Em aberto para
confirmação.

*Confirmação do cliente (2ª rodada):* "Alugamos 20 notebooks pra Orla por uns meses. Emiti
NF-e porque me disseram que locação não é NFS-e." — ou seja, atividade de locação
**recorrente** (vários meses) e emissão por NF-e mod 55. [L3] sustenta que a locação está
fora do campo do ISS; **a regra sobre qual documento emitir (NFS-e × NF-e) não consta da
biblioteca** — a prática relatada é compatível com [L3] nesse aspecto, mas a emissão por
NF-e fica como leitura não verificada (entendimento do cliente). "Por uns meses" sugere que locações em meses anteriores
podem estar incluídas no `faturamento_12_meses.csv` (já dentro do RBT12 total — Premissa
A1); sem resposta sobre o detalhamento mensal, o ponto fica em aberto, sem impacto no uso
do total.

*Observação:* o próprio XML traz `infCpl` "Documento fictício gerado para benchmark; sem
validade fiscal" — e, em contradição interna, um protocolo de autorização (`protNFe`:
nProt 135000000000512, cStat 100 "Autorizado o uso da NF-e"). O campo `tpAmb` tem valor 2;
seu significado não consta da biblioteca (não verificado). Ainda assim, a receita de R$ 6.000,00 está corroborada pela tabela de
notas (`notas_emitidas_maio.md`) e pelo crédito de 2026-05-26 no extrato, de modo que a
operação existe nos documentos do cliente; apenas o XML é auto-descrito como sem validade
fiscal — sinalizado, mas a receita foi considerada.

## 6. Fator R — escolha do anexo (III ou V)

Regra ([L1], §5º-J/§5º-M): serviços de TI → **Anexo III se folha/receita (12m) ≥ 28%**,
senão **Anexo V**. Folha = valores pagos no período ([L1], Res. 140 art. 26 §§1º–2º:
independe do mês de competência).

Folha pelo resumo (12 competências mai/2025–abr/2026):

23.400 + 23.400 + 23.800 + 23.800 + 23.800 + 24.100 + 24.100 + 24.100 + 24.300 + 24.300 + 20.900 + 24.600
= **R$ 284.600,00** (confere com a soma da coluna `total_folha`)

Fator R = 284.600 / 1.020.000 = **27,90%** < 28% → **Anexo V**.

Sensibilidade (regra do "pago", Res. 140 art. 26 §2º) — **atualizada com a resposta do
cliente (2ª rodada)**:

- **Pró-labore de abril (R$ 3.200,00): pago em 30/04/2026 — dentro da janela
  mai/2025–abr/2026.** O e-mail inicial ("paguei atrasado, dia 6 de maio") estava impreciso:
  o PIX foi *lançado no sistema* em maio, mas o pagamento ocorreu em 30/04 (comprovante
  prometido pelo sócio, ainda não anexado aos autos). A linha 2026-04 do resumo (pró-labore
  3.200, total 24.600) reflete esse pagamento; a obs. "em aberto na data do resumo" explica o
  lançamento tardio na contabilidade, não o pagamento. Portanto o pró-labore **não** sai da
  folha da janela — o cenário "281.400 / 27,59%" fica sem efeito. (Por que a linha 2026-03
  tem pró-labore zero continua sem explicação; não havendo pagamento de março, o total do
  resumo já reflete a realidade de caixa.)
- O extrato de maio mostra "DARF/GPS/FGTS **ABR**" pago em 07/05/2026: o encargo
  patronal/FGTS de abr/2026 (R$ 4.700, incluído no resumo) foi pago fora da janela; em
  contrapartida, entraria na janela o encargo pago em mai/2025 (referente a abr/2025 —
  valor não informado, presumivelmente 4.700). Se iguais, o efeito líquido é **nulo**:
  folha caixa = 284.600 → **27,90%**; sem o ingresso de abr/2025: 279.900 → **27,44%**.

Em todos os cenários (27,4%–27,9%) o Fator R **fica abaixo de 28%** → Anexo V. A conclusão
é robusta a essas incertezas; ela foi *demonstrada*, não repetida do histórico. Notar que o
Anexo V é o **mais caro** entre os dois; a escolha não é discricionária: com Fator R < 28%,
o Anexo V é o devido ([L1]).

*Alerta (limiar):* para o Fator R atingir 28% seria preciso folha ≥ 0,28 × 1.020.000 =
R$ 285.600. No cenário do encargo defasado, o pagamento de abr/2025 (não documentado) teria
de ser ≥ R$ 5.700, ou haver outros pagamentos de folha não documentados na janela, para
mudar o anexo (o DAS cairia de ~15,2 mil para ~12,5 mil). O cliente informou não ter mais
informação/extratos dos 12 meses; o ponto fica registrado como em aberto, sem impacto
conhecido sobre o resultado.

## 7. Faixa e alíquota efetiva (4ª faixa)

RBT12 = 1.020.000,00 → 4ª faixa (> 720.000 e ≤ 1.800.000) em ambos os anexos ([L2]).

**Anexo V (serviços):** alíquota nominal 20,50%, parcela a deduzir 17.100,00.
Alíquota efetiva (§1º-A [L1]) = (RBT12 × Aliq − PD) / RBT12
= (1.020.000 × 0,205 − 17.100) / 1.020.000
= (209.100 − 17.100) / 1.020.000 = 192.000 / 1.020.000 = **18,8235%**

**Anexo III (locação):** nominal 16,00%, PD 35.640,00.
Efetiva = (1.020.000 × 0,16 − 35.640) / 1.020.000 = (163.200 − 35.640)/1.020.000
= 127.560 / 1.020.000 = **12,5059%**
Parcela de ISS na 4ª faixa = 32,50% ([L2]) → deduzir: 12,5059% × 0,325 = 4,0644%
Alíquota locação = 12,5059% × (1 − 0,325) = 12,5059% × 0,675 = **8,4415%**

## 8. DAS de maio/2026

- Serviços: 78.000,00 × 18,8235% = **14.682,35**
  (aritmética exata: 78.000 × 192.000/1.020.000 = 14.682,3529…)
- Locação: 6.000,00 × 8,4415% = **506,49**
  (exato: 6.000 × 0,125058823… × 0,675 = 506,4882…)
- **Total: 14.682,35 + 506,49 = 15.188,84**

*Premissa A4:* o custo do estorno não é deduzido da receita da locação e vice-versa; cada
atividade recebe sua alíquota sobre sua própria receita segregada ([L1], §4º).

## 9. Verificações de consistência

Extrato mai/2026 — recebimentos: 12.500 + 18.000 + 9.800 + 22.000 + 6.700 + 4.500 + 6.000 +
8.500 = 88.000; menos PIX de estorno 4.000 (29/05) = **84.000 líquido** = serviços 78.000 +
locação 6.000. **Confere** com as notas.

Extrato **PDF** × **CSV** (auditoria pré-entrega): conferem — mesmas 15 transações e mesmos
totais/saldos (inicial 41.280,55; débitos 43.180,22; créditos 88.000,00; final 86.100,33,
compatível com o saldo corrente da primeira linha do CSV). O PDF traz rodapé de banco
fictício (§1, §12.5).

Itens do extrato **não** usados no cálculo (corretamente): folha mai/2026 (07/05), DARF/GPS/FGTS
ABR (07/05), aluguel de escritório, pró-labore MAI (16/05), DAS ABR — esses afetam o Fator R de
*períodos futuros*, não a receita de maio. O pró-labore da competência **abril** foi pago em
30/04/2026 (§6), portanto fora do extrato de maio; o extrato de maio traz apenas o pró-labore
de maio (16/05), consistente com isso.

**Divergências sinalizadas (atualizadas com a resposta do cliente — 2ª rodada):**
1. ~~E-mail × extrato sobre o pró-labore de abril~~ — **resolvido**: o sócio confirmou
   pagamento em **30/04/2026**; o "dia 6 de maio" do e-mail era a data de lançamento do PIX
   no sistema. Isso explica a ausência de débito de R$ 3.200 no extrato de maio e mantém o
   pagamento **dentro** da janela do Fator R (§6). Comprovante prometido, ainda não anexado.
2. DAS ABR pago em 20/05 = R$ 10.480,22 = **12,0462%** da receita de abr (87.000).
   *Correção desta linha na auditoria pré-entrega:* a versão anterior afirmava que "nenhuma
   combinação Anexo III/V × RBT12 reproduz 10.480,22" — impreciso. Resolvendo exatamente
   para as 12 combinações (2 anexos × 6 faixas, exigindo RBT12 dentro da faixa):
   - a **única** reprodução exata é **Anexo III, 4ª faixa**, com RBT12 da janela de abril
     (abr/2025–mar/2026, não documentada) de **R$ 901.418,11**: 16,00% − 35.640/901.418,11
     = 12,0462% → 87.000 × 12,0462% = 10.480,22 ✓;
   - as outras 11 combinações exigiriam RBT12 fora da própria faixa de aplicabilidade
     (impossíveis por definição);
   - mas até essa leitura Anexo III/4ª é **refutada pelos autos**: os 11 meses conhecidos
     dessa janela (mai/2025–mar/2026, `faturamento_12_meses.csv`) já somam R$ 933.000
     (> 901.418,11), o que implicaria receita de abr/2025 **negativa** (−31.581,89); e,
     para qualquer RBT12 ≥ 933.000, a efetiva do Anexo III/4ª é ≥ 12,18% (≠ 12,0462%) e a
     do Anexo V ≈ 18,7%.
   
   Logo, o DAS de abril **não é reproduzível** pelas tabelas da biblioteca ([L2]) com as
   receitas documentadas. Hipóteses alternativas (receita de abril diferente do CSV, DAS
   pago com encargos/multa, pagamento incluindo competências anteriores) não são
   verificáveis nos autos. A memória do sócio ("pagávamos pelo Anexo V") também não bate
   com o valor pago. **Não forcamos ajuste** — fica em aberto.
3. Linha 2026-03 do resumo: pró-labore zero com obs. "pró-labore de abril: em aberto na data
   do resumo". A explicação do cliente ("a contabilidade tirou o resumo com o pró-labore de
   abril em aberto porque lancei o PIX só em maio") esclarece a obs., mas não por que a
   pró-labore da competência **março** consta zero. Como não houve pagamento lançado em
   março, o total do resumo (caixa) permanece o melhor valor; micro-ponto em aberto.

## 10. Repartição por tributo

O campo `reparticao` do `apuracao.json` contém **apenas** a repartição verificável na
biblioteca: a proporção da **parcela de locação** (R$ 506,49) pelas percentagens do Anexo
III, 4ª faixa ([L2]): IRPJ 4,00% · CSLL 3,50% · COFINS 14,05% · PIS 3,05% · CPP 42,75% ·
ISS 32,50% → IRPJ 20,26 · CSLL 17,73 · COFINS 71,16 · PIS 15,45 · CPP 216,52 · ISS 164,61.

Avisos:
- A **repartição do Anexo V, 4ª faixa (serviços) não consta da biblioteca** — não é
  possível apurar a partição dos R$ 14.682,35 em IRPJ/CSLL/COFINS/PIS/CPP/ISS sem citar
  fonte fora do INDEX. Perguntado ao cliente (conferência no programa da Receita), ele
  informou não ter informação adicional. Deixamos **em aberto** (não inventamos). O ISS
  embutido nos serviços (se houver, pois TI paga ISS) não foi quantificado por falta de
  base na biblioteca.
- A tabela do Anexo III/4ª faixa da biblioteca soma **99,85%**, não 100% — divergência
  interna da própria fonte ([L2]); por isso as parcelas acima somam 505,73 ≠ 506,49
  (diferença de R$ 0,76). Não ajustamos à força; registrado.
- A linha "ISS" da locação é mostrada por simetria à tabela; na materialidade **não há ISS
  sobre locação de bens móveis** (Súmula Vinculante 31, [L3]) — a parcela de ISS já foi
  deduzida da alíquota (§7).

## 11. Premissas (resumo)

- A1: RBT12 total do arquivo de faturamento (12 competências), líquido de ajustes históricos.
- A2: consultoria de arquitetura e treinamento são serviços de TI (Fator R); não verificável na biblioteca.
- A3: dedução do ISS da locação = percentual de repartição do anexo/faixa × alíquota efetiva.
- A4: alíquota efetiva de cada anexo calculada com o RBT12 total e aplicada à receita mensal segregada.
- A5: folha de 12m = soma do resumo (284.600); pró-labore de abril confirmado pago em
  30/04/2026 (dentro da janela); encargo INSS/FGTS defasado 1 mês com ingresso presumido de
  abr/2025 — sensibilidade 27,4%–27,9% em §6 (não altera o anexo).

## 12. Itens em aberto (pós-resposta do cliente — 2ª rodada)

O cliente respondeu à 1ª rodada e informou **não ter informação adicional** para o demais.
Nada foi forçado nem inventado; o que segue fica explicitamente em aberto:

1. Repartição do Anexo V/4ª faixa (serviços, R$ 14.682,35) — não existe na biblioteca e o
   cliente não tem o dado; o `apuracao.json` traz apenas a parcela verificável (locação,
   Anexo III — §10).
2. Caixa dos 12 meses para o Fator R em sentido estrito — extratos comprovantes não
   existem mais; defasagem do INSS/FGTS produz faixa 27,4%–27,9%, toda < 28% (Anexo V não
   muda). Para mudar de anexo, o encargo de abr/2025 (não documentado) teria de ser
   ≥ R$ 5.700 (§6).
3. DAS de abril (R$ 10.480,22 = efetiva de 12,0462%): a única combinação aritmeticamente
   consistente é Anexo III/4ª com RBT12 (abr/2025–mar/2026) de R$ 901.418,11 — refutada
   pela receita documentada (os 11 meses conhecidos da janela já somam 933.000; abr/2025
   implicado seria negativo). Sem explicação do cliente; hipóteses alternativas não
   verificáveis; não ajustado (§9.2).
4. Natureza fiscal de "consultoria de arquitetura" e "treinamento" (A2) — sem resposta;
   premissa mantida.
5. Documentos autodeclarados fictícios — o XML da NF-e 000.512 ("documento fictício… sem
   validade fiscal", convivendo com protocolo de autorização cStat 100 — §5) e o rodapé do
   extrato em PDF (banco e conta fictícios) — não endereçados pelo cliente; as receitas são
   corroboradas pela tabela de notas e pelos dois extratos (CSV e PDF conferem entre si);
   ponto registrado.
6. Tabela de repartição Anexo III/4ª soma 99,85% na própria biblioteca ([L2]) — divergência
   de fonte, insolúvel pelo cliente.
7. Por que a linha 2026-03 do resumo tem pró-labore zero — sem explicação; sem efeito sobre
   o total (não houve pagamento em março).
8. Comprovante do pró-labore de 30/04/2026 — prometido pelo sócio, ainda não anexado aos
   autos.

**Resolvidos nesta rodada:** data de pagamento do pró-labore de abril (30/04/2026, dentro
da janela — §6 e §9.1) e a natureza da operação da NF-e 000.512 (locação recorrente de
bens móveis, NF-e mod 55 — §5).
