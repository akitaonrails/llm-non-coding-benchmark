# Memória de cálculo — DAS maio/2026

**Contribuinte:** Lumen Soluções Digitais LTDA ME — Simples Nacional (ME)
**Período de apuração:** 05/2026 · **Faturamento do mês:** R$ 84.000,00 · **DAS apurado: R$ 15.188.84**

**Rodada 2 (respostas do cliente de 22/10/2026 aplicadas).** O resultado **não mudou** (DAS 15.188,84, Anexo V), mas duas hipóteses anteriores foram **eliminadas** (§3.4 e §3.5) e o risco remanescente passou a ser **um único item** (§3.5): a folha paga na janela é 284.600,00 em qualquer leitura, e faltam **R$ 1.000,00** para virar Anexo III.

---

## 1. Fontes

**Biblioteca fechada (única base normativa citável — `library/INDEX.md`):**
- `library/lc123_art18_fator_r.md` — LC 123/2006, art. 18, §§1º, 1º-A, 5º-J, 5º-K, 5º-M, 4º; Res. CGSN 140/2018, arts. 25 e 26 (alíquota efetiva, Fator R, folha **paga**, segregação de receitas, cancelamentos).
- `library/anexos_iii_v_tabelas.md` — tabelas dos Anexos III e V (redação LC 155/2016), com a repartição da 4ª faixa do Anexo III.
- `library/locacao_bens_moveis_iss.md` — LC 123/2006, art. 18, §5º-A; **Súmula Vinculante 31 (STF)**; Res. CGSN 140, art. 25, §1º, V — locação de bens móveis no Anexo III, deduzida a parcela de ISS.

**Documentos do cliente:** `documents/faturamento_12_meses.csv`, `documents/resumo_folha_12_meses.csv`, `documents/notas_emitidas_maio.md`, `documents/nfe_000512_locacao.xml`, `documents/extrato_maio_2026.csv`, `documents/extrato_maio_2026.pdf`, `documents/email_socio.txt`.

Nenhuma fonte externa foi consultada. O que a biblioteca não cobre está declarado no §9 como **NÃO VERIFICADO NA BIBLIOTECA**.

---

## 2. RBT12 e faixa (art. 18, §1º)

`documents/faturamento_12_meses.csv`, competências **2025-05 … 2026-04**:

| mes | 05/25 | 06/25 | 07/25 | 08/25 | 09/25 | 10/25 | 11/25 | 12/25 | 01/26 | 02/26 | 03/26 | 04/26 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| receita | 78.000 | 81.500 | 84.000 | 86.000 | 79.500 | 90.000 | 88.000 | 92.000 | 85.000 | 83.000 | 86.000 | 87.000 |

**RBT12 = 1.020.000,00** (soma conferida).

**Faixa (Anexo V, `library/anexos_iii_v_tabelas.md`):** 1.020.000,00 > 720.000,00 e ≤ 1.800.000,00 → **4ª faixa** → alíquota nominal **20,50%**, parcela a deduzir **R$ 17.100,00**.

**Premissa P1 (o cliente não respondeu):** o CSV é receita **bruta acumulada dos 12 meses anteriores**, já líquida de cancelamentos, e **inclui** a receita de locação de bens móveis (QUESTIONS.md Q5). Se a base for menor (locação fora do RBT12, estornos de outras competências, outras receitas não listadas), a faixa e a alíquota efetiva mudam — ex.: RBT12 ≤ 1.000.000 continua na 4ª faixa, RBT12 ≤ 720.000 cai para a 3ª. **Não ajustado por falta de suporte documental.**

---

## 3. Fator R (art. 18, §§5º-J e 5º-M) — decisão do anexo dos serviços

A regra (biblioteca): atividades de prestação de serviços de TI vão ao **Anexo III** se
`folha de salários (salários + pró-labore + contribuições patronais + FGTS) ÷ receita bruta`, **ambos dos 12 meses anteriores**, for **≥ 28%**; caso contrário, **Anexo V**.
Pela Res. CGSN 140, art. 26, §2º, considera-se o **valor pago** no período, independentemente da competência.

### 3.1 Composição da folha (janela 05/2025–04/2026)

`documents/resumo_folha_12_meses.csv` (12 competências), coluna `total_folha`:

| componente | valor | origem |
|---|---:|---|
| salários | 193.000,00 | soma da coluna `salarios` (12 linhas) |
| pró-labore | 35.200,00 | 11 competências × 3.200,00 (2 sócios × 1.600,00); linha 2026-03 = 0 |
| INSS patronal + FGTS | 56.400,00 | 12 × 4.700,00 (coluna `inss_patronal_fgts`) |
| **folha 12 m** | **284.600,00** | soma da coluna `total_folha` (conferida linha a linha) |

### 3.2 Resposta do cliente sobre o pró-labore de abril/2026

> "O pró-labore de abril (R$ 1.600 cada sócio, R$ 3.200) foi pago em 30 de abril, mas a contabilidade tirou o resumo com ele 'em aberto' porque eu lancei o PIX no sistema só em maio. Te mando o comprovante de 30/04."

Consequências:
1. O pagamento em **30/04/2026 está dentro da janela 05/2025–04/2026**. Portanto a prestação de abril/2026 **conta** no Fator R desta apuração pelo critério de **pagamento** — e o resumo já a contém (linha 2026-04 = 3.200,00).
2. O critério de **competência** (resumo) e o critério de **pagamento** (informado pelo cliente) **convergem para 284.600,00**. Fica **eliminada** a hipótese anterior de folha paga de **281.400,00**, que se baseava no e-mail do sócio ("pró-labore de abril eu paguei atrasado, dia 6 de maio" — `documents/email_socio.txt`).
3. **Corroboração documental parcial:** o extrato de maio/2026 não traz nenhum PIX de pró-labore em 06/05/2026 — só os dois PIX de 16/05/2026, rotulados "PRO-LABORE MAI" (3.200,00). A ausência em maio é **compatível** com pagamento em 30/04/2026 (mês não coberto por extrato no pacote).
4. **Ressalva:** o **comprovante de 30/04 não chegou** a `documents/`; a data de 30/04/2026 é **alegação do cliente**, registrada como premissa, não como evidência arquivada.

### 3.3 Fator R apurado

```
fator R = 284.600,00 / 1.020.000,00 = 0,2790196… = 27,90%
limite 28%  -> folha necessária = 0,28 × 1.020.000,00 = 285.600,00
margem      = 285.600,00 − 284.600,00 = R$ 1.000,00
```

**27,90% < 28% → serviços no ANEXO V, 4ª faixa.**

### 3.4 Cenários de folha (atualizado)

| cenário | folha 12 m | fator R | anexo serviços | DAS |
|---|---:|---:|---|---:|
| **Adotado** — resumo, com pró-labore de abril pago em 30/04/2026 (dentro da janela) | **284.600,00** | **27,90%** | **V** | **15.188,84** |
| 12ª prestação de pró-labore paga na janela (ex.: competência 2026-03, que o resumo traz em branco) | 287.800,00 | 28,22% | III | 10.261,08 |
| ~~pró-labore de abril fora da janela (e-mail: pago 06/05)~~ | ~~281.400,00~~ | ~~27,59%~~ | ~~V~~ | **eliminado pela resposta do cliente** |

### 3.5 Risco material remanescente (único) — sinalizado, sem nova pergunta

A linha **2026-03** do resumo traz `pro_labore = 0` com a observação *"pró-labore de abril: em aberto na data do resumo"*. Como o cliente esclareceu que o item "em aberto" era o de **abril**, a **lacuna de março/2026 continua sem explicação** no documento. Se houve prestação de março/2026 (3.200,00) paga dentro da janela e fora do resumo, a folha passa a **287.800,00**, o fator R a **28,22%** e os serviços migram para o **Anexo III** (DAS **10.261,08**, −4.927,76).

Indício adicional de que a folha informada pode estar subestimada: o DAS de **abril/2026** pago em 20/05/2026 foi **10.480,22** (`documents/extrato_maio_2026.csv`), ou seja, **12,05%** da receita de abril (87.000,00) — valor **incompatível com o Anexo V** (87.000 × 18,8235% = 16.376,45) e compatível com o **Anexo III** (87.000 × 12,5059% = 10.880,13; com locação segregada, 81.000 × 12,5059% + 6.000 × 8,4415% = 10.636,27). Ou seja: **janelas anteriores provavelmente tinham folha ≥ 28%**, o que reforça a necessidade de revisar a folha paga de 05/2025–04/2026 (QUESTIONS.md Q7). A apuração de abril não pode ser refeita aqui: faltam as receitas de abr/2025–mar/2026 para o RBT12 daquela apuração.

Para encerrar o ponto bastaria um documento ausente do pacote: extratos de mar/2026 e abr/2026, ou a folha de pagamento/DIRF, ou o comprovante de 30/04. **Valor de registro: 284.600,00 → Anexo V.**

### 3.6 Nota indicativa (fora deste entregável) — junho/2026

Janela de pagamentos 06/2025–05/2026: folha ≈ 284.600,00 − 23.400,00 (mai/25) + 16.600,00 (salários mai/26 pagos em 07/05) + 3.200,00 (pró-labore mai/26, 16/05) + 4.700,00 (GPS/FGTS abr/26, 07/05) = **285.700,00**; RBT12 ≈ 1.020.000,00 − 78.000,00 (mai/25) + 84.000,00 (mai/26) = **1.026.000,00** → fator R ≈ **27,85%** (limite de folha: 287.280,00). O pró-labore de abril (30/04/2026) fica **fora** dessa janela. Cálculo **indicativo**: a folha de mai/26 no extrato está rotulada "FOLHA MAIO — SALARIOS" **parcial**, e não há extratos de jun/2025–abr/2026 no pacote. A margem estrutural do contribuinte em torno de 28% é estreita em ambos os meses.

---

## 4. Receitas de maio/2026 e o estorno da NFS-e 1188

`documents/notas_emitidas_maio.md`:

| documento | descrição | valor |
|---|---|---:|
| NFS-e 1181 | desenvolvimento de software — sprint 11 | 18.000,00 |
| NFS-e 1182 | sustentação mensal — Cliente Orla | 12.500,00 |
| NFS-e 1183 | consultoria de arquitetura | 9.800,00 |
| NFS-e 1184 | desenvolvimento — módulo fiscal | 22.000,00 |
| NFS-e 1185 | suporte técnico | 6.700,00 |
| NFS-e 1186 | treinamento equipe | 4.500,00 |
| NFS-e 1187 | desenvolvimento — integração | 8.500,00 |
| **bruto serviços** | | **82.000,00** |
| NFS-e 1188 | estorno parcial — glosa de escopo (sobre 1184) | (4.000,00) |
| **serviços líquidos** | | **78.000,00** |
| NF-e 000.512 | locação de 20 notebooks — maio | 6.000,00 |
| **total do mês** | | **84.000,00** |

### 4.1 Estorno confirmado como cancelamento/glosa definitivo (resposta do cliente)

> "O cliente contestou parte do escopo da 1184; a gente emitiu a 1188 estornando R$ 4.000 e devolveu via PIX."

- Base legal na biblioteca (`library/lc123_art18_fator_r.md`, "Devoluções/cancelamentos"): não integra a receita bruta o serviço cancelado; **o estorno reduz a receita do mês em que ocorrer**.
- O estorno é de **maio/2026** (nota emitida em maio) → reduz a receita de **maio/2026**: 82.000,00 → **78.000,00**.
- **Conferência bancária:** `documents/extrato_maio_2026.csv` de 29/05/2026, "PIX ENVIADO ESTORNO GLOSA — CLIENTE 1184 −4.000,00" → a devolução citada pelo cliente **está** no extrato. Nenhum recebimento correspondente a nota substitutiva aparece no extrato (créditos de maio = 88.000,00 = 82.000,00 + 6.000,00 das notas emitidas).
- **Cenário eliminado:** "nota cancelada com serviço reemitido em junho" (**+752,94**, = 4.000,00 × 18,8235%) **não se aplica**.
- Efeito sobre o RBT12 das apurações futuras: na janela contratual de maio/2026 a troca de 82.000,00 por 78.000,00 levaria o RBT12 a 1.016.000,00 — **mesma 4ª faixa**, sem efeito de alíquota.

### 4.2 Premissa P2 (o cliente não respondeu): classificação das atividades

Todas as 7 NFS-e de serviço (1181–1187) foram tratadas como **atividades de TI do mesmo bloco sujeito a Fator R** (Anexo V/III), incluindo "consultoria de arquitetura" (1183) e "treinamento equipe" (1186).
**As listas de atividades dos anexos NÃO estão na biblioteca** (`library/INDEX.md` traz só as tabelas) → a classificação é **NÃO VERIFICÁVEL NA BIBLIOTECA**. Impacto quantificado: se o treinamento (1186, 4.500,00) pertencesse ao Anexo III, o DAS cairia **284,29** (§8.2).

---

## 5. Anexo aplicável a cada receita (art. 18, §4º — segregação)

| receita | anexo | fundamento na biblioteca |
|---|---|---|
| serviços de TI — 78.000,00 | **Anexo V** (4ª faixa) | fator R 27,90% < 28% (`lc123_art18_fator_r.md`, §§5º-J/5º-M) |
| locação de notebooks — 6.000,00 | **Anexo III, deduzida a parcela de ISS** | `locacao_bens_moveis_iss.md`: locação de bens móveis é tributada "na forma do **Anexo III, deduzida a parcela correspondente ao ISS**", porque não é serviço para ISS (**Sv. Vinculante 31**) |

**Por que a locação tem a parcela de ISS deduzida (não é escolha, decorre da tabela):** a repartição do Anexo III, 4ª faixa (`anexos_iii_v_tabelas.md`) embute **ISS 32,50%** do DAS. Como a locação de bens móveis não é fato gerador de ISS (Sv. Vinculante 31), essa parcela é excluída → fator remanescente **100% − 32,50% = 67,50%**.
**Coerência com os documentos:** `documents/nfe_000512_locacao.xml` é uma **NF-e** (modelo 55) de locação, sem destaque de ISS — §7.2.

**Correção técnica ao pedido do sócio** (`documents/email_socio.txt`: "é só repetir o cálculo da tabela com a alíquota da faixa", "acho que vai junto com os serviços"): a **alíquota nominal da faixa (20,50%) não é o valor a recolher**. A lei define a **alíquota efetiva** = (RBT12 × alíquota − PD) ÷ RBT12 (§1º-A). Aplicar 20,50% sobre as receitas do mês daria 17.220,00 — **2.031,16 a maior** — e, aplicada à locação isolada, produziria alíquota efetiva negativa, o que evidencia o erro do método. Ver §6.

---

## 6. Cálculo do DAS (aritmética completa)

### 6.1 Alíquotas efetivas sobre o RBT12 = 1.020.000,00

**Anexo V, 4ª faixa** (nominal 20,50%, PD 17.100,00):
```
1.020.000,00 × 0,2050 = 209.100,00
209.100,00 − 17.100,00 = 192.000,00
192.000,00 / 1.020.000,00 = 0,18823529… -> 18,8235%
```

**Anexo III, 4ª faixa** (nominal 16,00%, PD 35.640,00) — usada só para a locação:
```
1.020.000,00 × 0,1600 = 163.200,00
163.200,00 − 35.640,00 = 127.560,00
127.560,00 / 1.020.000,00 = 0,12505882… -> 12,5059%
efetiva da locação (sem parcela de ISS) = 0,12505882… × 0,675 = 0,08441470… -> 8,4415%
```

### 6.2 Valor a recolher por bloco (alíquota efetiva × receita do mês)

| bloco | cálculo | valor |
|---|---|---:|
| serviços (Anexo V) | 78.000,00 × 18,8235% | **14.682,35** |
| locação (Anexo III − ISS) | 6.000,00 × 8,4415% | **506,49** |
| **DAS maio/2026** | | **15.188,84** |

Método equivalente, sem arredondar a alíquota (usado para conferência):
- serviços: 192.000,00 × 78.000,00 ÷ 1.020.000,00 = 14.682,3529… → **14.682,35**
- locação: 127.560,00 × 6.000,00 ÷ 1.020.000,00 × 0,675 = 750,3529… × 0,675 = 506,4882… → **506,49**

Carga efetiva sobre o mês: 15.188,84 ÷ 84.000,00 = **18,08%**.

### 6.3 Comparação com o método proposto pelo sócio

| método | serviços | locação | total |
|---|---:|---:|---:|
| **Apurado (correto)** | 14.682,35 | 506,49 | **15.188,84** |
| "20,50% cheio sobre tudo" | 16.000,00 | 1.230,00 | 17.220,00 |
| diferença | +1.317,65 | +723,51 | **+2.031,16 a maior** |

---

## 7. Repartição por tributo e documentos fiscais

### 7.1 Locação — repartição apurada (única tabela disponível na biblioteca)

Base: parcela do DAS anterior à dedução de ISS = 6.000,00 × 12,5059% = **750,35**. Percentuais da 4ª faixa do Anexo III (`anexos_iii_v_tabelas.md`):

| tributo | % | valor |
|---|---:|---:|
| IRPJ | 4,00% | 30,01 |
| CSLL | 3,50% | 26,26 |
| COFINS | 14,05% | 105,42 |
| PIS | 3,05% | 22,89 |
| CPP (INSS) | 42,75% | 320,78 |
| ISS | 32,50% | **0,00** — parcela **excluída** (Sv. Vinculante 31; NF-e 512 sem ISS) |
| **soma dos componentes** | (tabela soma **99,85%**) | **505,36** |

**Divergência registrada, não compensada:** a tabela da biblioteca **não fecha em 100%** (soma = 99,85%). A diferença de **1,13** entre a soma dos componentes (505,36) e o DAS de locação apurado (506,49) corresponde exatamente a essa lacuna de 0,15% sobre 750,35. Não foi criado valor de "arredondamento" para forçar o fechamento.

### 7.2 Serviços — repartição **NÃO APURADA**

A biblioteca **não contém a tabela de repartição do Anexo V**. Inventar percentuais de IRPJ/CSLL/COFINS/PIS/CPP/ISS para os 14.682,35 de serviços seria fato não suportado → **repartição dos serviços não apurada**. No `apuracao.json`, o bloco `reparticao` refere-se **exclusivamente à locação**. (QUESTIONS.md Q8 — pedimos a tabela, o cliente não forneceu.)

### 7.3 NF-e 000.512 (locação)

`documents/nfe_000512_locacao.xml`: modelo 55, **sem destaque de ISS** — coerente com a Sv. Vinculante 31 e com o enquadramento da locação no Anexo III sem a parcela de ISS. O documento **destaca PIS 39,00 (0,65%) e COFINS 180,00 (3,00%)** em regime não cumulativo, o que é inconsistente com o Simples Nacional (PIS/COFINS vêm no DAS). A vedação aplicável (art. 13/§ da LC 123) **não está na biblioteca** → observação registrada como **NÃO VERIFICADO NA BIBLIOTECA**, sem efeito sobre o valor do DAS (QUESTIONS.md Q9).

---

## 8. Conciliação com o extrato de maio/2026 e histórico

### 8.1 Extrato — 100% conciliado com as notas

`documents/extrato_maio_2026.csv`:
- **créditos** = 12.500 + 18.000 + 9.800 + 22.000 + 6.700 + 4.500 + 6.000 + 8.500 = **88.000,00** = soma das notas emitidas (82.000,00 serviços + 6.000,00 locação). Cada recebimento casa com uma nota (Orla 12.500 → 1182; Safra 18.000 → 1181; 9.800 → 1183; módulo fiscal 22.000 → 1184; suporte 6.700 → 1185; treinamento 4.500 → 1186; locação 6.000 → NF-e 512; integração 8.500 → 1187).
- **débitos** = 16.600,00 (folha mai/26) + 4.700,00 (DARF/GPS/FGTS abr/26) + 4.200,00 (aluguel) + 1.600,00 + 1.600,00 (pró-labore mai/26) + 10.480,22 (DAS abr/26) + 4.000,00 (estorno 1184) = **43.180,22**.
- **saldo:** 41.280,55 + 88.000,00 − 43.180,22 = **86.100,33** = saldo final do CSV.

Divergências menores registradas (sem efeito no DAS): o PDF do extrato (`documents/extrato_maio_2026.pdf`) traz um débito "OUTBACK STEAK R$ 120,00" ausente do CSV e saldo final 100,00 menor — reconciliação bancária a cargo do cliente.

### 8.2 Sensibilidades (valores recalculados)

| cenário | efeito no DAS |
|---|---:|
| folha paga ≥ 285.600,00 (ex.: 12ª prestação de pró-labore → 287.800,00) → serviços ao Anexo III | **−4.927,76** (DAS 10.261,08) |
| treinamento (1186, 4.500,00) classificado no Anexo III | **−284,29** |
| estorno substituído por nota reemitida em maio | **+752,94** — **eliminado** pela resposta do cliente |
| método do sócio (20,50% nominal sobre tudo) | **+2.031,16** — **recusado**, sem amparo legal |
| RBT12 menor (ex.: ≤ 720.000 → 3ª faixa) | rebaixa a alíquota; não quantificado por falta de base (P1) |

### 8.3 Anomalia de período anterior (fora do escopo, requer atenção)

DAS **abr/2026 = 10.480,22** pago em 20/05/2026 ≈ **12,05%** da receita de abril → compatível com **Anexo III**, não com o "ano passado a gente pagava pelo Anexo V" do e-mail. Consequências possíveis: (i) as janelas de folha anteriores tinham fator R ≥ 28% — o que tornaria a folha da janela de maio/2026 suspeita de subestimação (§3.5); ou (ii) apurações anteriores em anexo equivocado → **retificação**, fora do escopo de maio/2026 (QUESTIONS.md Q7).

---

## 9. NÃO VERIFICADO NA BIBLIOTECA (declarado, não suprido)

A biblioteca autorizada contém **3 arquivos** (`library/INDEX.md`). Não há base para concluir sobre:
1. **listas de atividades/atividades típicas dos Anexos III e V** (classificação de "consultoria de arquitetura" e "treinamento");
2. **tabela de repartição do Anexo V** (por isso §7.2);
3. **limite de receita do Simples Nacional, sublimites, enquadramento/ME, CNAE** e demais regras do art. 3º/§;
4. **vedação de destaque de PIS/COFINS por optante do Simples** (art. 13 e correlatos);
5. **obrigações acessórias**: PGDAS-D, comunicação de atividade ao fisco municipal, retenção/substituição de ISS, emissão de NF-e x NFS-e para locação;
6. **prazo de vencimento do DAS** (usamos 20 do mês seguinte apenas como referência operacional do cliente — o extrato mostra "DAS ABR/2026" pago em 20/05/2026);
7. **folha de pagamentos da janela 05/2025–04/2026** (não documentada; só o resumo por competência).

---

## 10. Respostas do cliente aplicadas nesta rodada

| item | resposta | efeito |
|---|---|---|
| pró-labore de abr/2026 | pago em **30/04/2026**; o "em aberto" no resumo veio do lançamento tardio do PIX (maio) | entra na janela; **cenário 281.400,00 eliminado**; folha 284.600,00 confirmada em ambas as leituras; comprovante **não recebido** no pacote (alegação) |
| estorno NFS-e 1188 | glosa de escopo com **devolução via PIX**, sem nota substitutiva | cancelamento definitivo confirmado; receita de serviços **78.000,00**; cenário **+752,94 eliminado** |
| demais perguntas | "o cliente não tem informação adicional" | convertidas em **unknowns sinalizados** (QUESTIONS.md, §9) — não reapresentadas como perguntas novas |

**Resultado mantido: DAS maio/2026 = R$ 15.188,84** (serviços Anexo V 14.682,35 + locação Anexo III sem ISS 506,49). Item que ainda pode alterar o resultado: **folha paga ≥ 285.600,00 → Anexo III → DAS 10.261,08** (§3.4/§3.5).
