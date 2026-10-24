# Memória de cálculo — DAS maio/2026

**Contribuinte:** Lumen Soluções Digitais LTDA ME — Simples Nacional (ME)
**Período de apuração:** 05/2026 · **Faturamento do mês:** R$ 84.000,00 · **DAS apurado: R$ 15.188,84**

**Rodada 2 (respostas do cliente de 22/10/2026 aplicadas).** O resultado **não mudou** (DAS 15.188,84, Anexo V), mas duas hipóteses anteriores foram **eliminadas** (§3.4 e §3.5) e o risco remanescente passou a ser **um único item** (§3.5): a folha paga na janela é 284.600,00 em qualquer leitura, e faltam **R$ 1.000,00** para virar Anexo III.

**Rodada 3 — revisão da entrega (22/10/2026).** A memória, o JSON e os arquivos de unknowns foram relidos contra as fontes e **corrigidos em 16 pontos**; o valor apurado **não mudou** (**DAS maio/2026 = R$ 15.188,84**). O que mudou, e por quê, está em `REVISAO.md`. As correções são de **rigor**: um parágrafo de conciliação de extrato descrevia lançamentos que **não existem** nos arquivos (§8.1), três números de cenários estavam errados (§3.4, §6.3, §8.2), **a conta indicativa de junho/2026 não fechava e foi refeita (§3.6)**, a dedução de ISS da locação era apresentada como texto de lei quando é **inferência** (§5, P7) e um cálculo de abril/2026 era mostrado como fato quando é **indicativo** (§3.5).

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

**Premissa P1 (o cliente não respondeu):** o CSV é receita **bruta acumulada dos 12 meses anteriores**, já líquida de cancelamentos, e **inclui** a receita de locação de bens móveis (QUESTIONS.md U2). Se a base for menor (locação fora do RBT12, estornos de outras competências, outras receitas não listadas), a faixa e a alíquota efetiva mudam — ex.: RBT12 ≤ 1.000.000 continua na 4ª faixa, RBT12 ≤ 720.000 cai para a 3ª. **Não ajustado por falta de suporte documental.**

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

| cenário | folha 12 m | fator R | anexo serviços | **DAS** | Δ |
|---|---:|---:|---|---:|---:|
| **Adotado** — resumo, com pró-labore de abril pago em 30/04/2026 (dentro da janela) | **284.600,00** | **27,90%** | **V** | **15.188,84** | — |
| 12ª prestação de pró-labore paga na janela (ex.: competência 2026-03, que o resumo traz em branco) | 287.800,00 | 28,22% | III | 10.261,08 | −4.927,76 |
| ~~pró-labore de abril fora da janela (e-mail: pago 06/05)~~ | ~~281.400,00~~ | ~~27,59%~~ | ~~V~~ | ~~15.188,84~~ | **eliminado** pela resposta do cliente (Δ 0,00) |
| sem o estorno da 1188 (serviços = 82.000,00; folha e RBT12 inalterados) | 284.600,00 | 27,90% | V | 15.941,78 | +752,94 |
| treinamento (1186, 4.500,00) classificado no Anexo III | 284.600,00 | 27,90% | V + III | 14.904,54 | −284.30 |
| método do sócio: nominal de 20,50% aplicado sem deduzir a parcela a deduzir | 284.600,00 | — | — | 17.220,00 | +2.031,16 |

Todos os valores usam as alíquotas efetivas da **4ª faixa** apuradas sobre o mesmo RBT12 (1.020.000,00): Anexo V **18,8235%**, Anexo III **12,5059%**, locação (Anexo III sem a parcela de ISS) **8,4415%**. Exemplo de conta da linha do Anexo III: 127.560,00 × 78.000,00 ÷ 1.020.000,00 = **9.754,59** (serviços) + 127.560,00 × 6.000,00 ÷ 1.020.000,00 × 67,50% = **506,49** (locação) = **10.261,08**; Δ = 10.261,08 − 15.188,84 = **−4.927,76**. Na linha "sem o estorno", o fator R **não** muda: maio/2026 não integra a janela de 12 meses anteriores que serve de base ao RBT12 e ao fator R, de modo que só a receita tributável do mês sobe (82.000,00 × 18,8235% = 15.435,29 + 506,49 = 15.941,78).

O critério é a **folha de salários paga** na janela, conforme Res. CGSN 140, art. 26, §2º (folha **paga** nos 12 meses anteriores): `library/lc123_art18_fator_r.md`. Como o limite de RBT12 da 4ª faixa do Anexo V vai a 1.800.000,00 (`library/anexos_iii_v_tabelas.md`), **a mudança de anexo é o único caminho para alterar a alíquota nominal neste mês**.

### 3.5 Risco material remanescente (único) — sinalizado, sem nova pergunta

A linha **2026-03** do resumo traz `pro_labore = 0` com a observação *"pró-labore de abril: em aberto na data do resumo"*. Como o cliente esclareceu que o item "em aberto" era o de **abril**, a **lacuna de março/2026 continua sem explicação** no documento. Se houve prestação de março/2026 (3.200,00) paga dentro da janela e fora do resumo, a folha passa a **287.800,00**, o fator R a **28,22%** e os serviços migram para o **Anexo III** (DAS **10.261,08**, −4.927,76).

Indício adicional de que a folha informada pode estar subestimada: o DAS de **abril/2026** pago em 20/05/2026 foi **10.480,22** (`documents/extrato_maio_2026.csv`), ou seja, **12,05%** da receita de abril (87.000,00). **Cálculo indicativo** (as alíquotas efetivas abaixo são as da janela desta apuração, porque o RBT12 de abril/2025–março/2026 não está no pacote): sob o Anexo V, 87.000,00 × 18,8235% = **16.376,47**; sob o Anexo III, 87.000,00 × 12,5059% = **10.880,12** ou, com a locação segregada, 81.000,00 × 12,5059% + 6.000,00 × 8,4415% = **10.636,25**. O valor pago é **incompatível com o Anexo V** e **compatível com o Anexo III**. Ou seja: **janelas anteriores provavelmente tinham folha ≥ 28%**, o que reforça a necessidade de revisar a folha paga de 05/2025–04/2026 (QUESTIONS.md U4). A apuração de abril não pode ser refeita aqui: faltam as receitas de abr/2025–mar/2026 para o RBT12 daquela apuração.

Para encerrar o ponto bastaria um documento ausente do pacote: extratos de mar/2026 e abr/2026, ou a folha de pagamento/DIRF, ou o comprovante de 30/04. **Valor de registro: 284.600,00 → Anexo V.**

### 3.6 Nota indicativa (fora deste entregável) — junho/2026

Duas contas separadas, ambas **INDICATIVAS**: não há extratos de jun/2025–abr/2026 no pacote e a folha de mai/26 aparece só como lançamento do extrato ("FOLHA MAIO — SALARIOS"), sem folha de pagamento anexa.

**RBT12 de junho/2026:** 1.020.000,00 − 78.000,00 (mai/25) + 84.000,00 (mai/26, já com o estorno) = **1.026.000,00** → continua na **4ª faixa** (limite 1.800.000,00), portanto **nenhum efeito de alíquota**. Limiar de folha para o fator R nessa janela: 1.026.000,00 × 28% = **287.280,00**.

**Folha da janela 06/2025–05/2026** (mesma base do resumo, **competência**):

| movimento | valor | acumulado |
|---|---:|---:|
| janela 05/2025–04/2026 (resumo) | 284.600,00 | 284.600,00 |
| − competência 2025-05 | −23.400,00 | 261.200,00 |
| + competência 2026-05 (estimada): salários 16.600,00 + pró-labore 3.200,00 (1.600,00 × 2 pagos em 16/05) + INSS patronal/FGTS 4.700,00 (valor recorrente nas 12 competências) | +24.500,00 | **285.700,00** |

Atenção a uma armadilha de dupla contagem: o DARF/GPS/FGTS de 4.700,00 pago em 07/05/2026 é da **competência abr/2026**, que **já está** nos 284.600,00; por isso os 4.700,00 somados acima são os da competência mai/26 (estimados pela recorrência), e não o lançamento do extrato.

- **Leitura-base:** folha ≈ **285.700,00** → fator R 285.700,00 ÷ 1.026.000,00 = **27,85%** (< 28%) → junho/2026 ainda no **Anexo V**, margem de 1.580,00.
- **Variante ligada a U1:** se houver pró-labore devido na competência **2026-03** (linha com 0,00 no resumo, sem explicação), a folha passa a 285.700,00 + 3.200,00 = **288.900,00** → fator R **28,16%** (> 28%) → junho/2026 no **Anexo III** (limiar excedido em 1.620,00). É a mesma incógnita de U1, uma janela adiante.

**Correção desta rodada:** a versão anterior escrevia "284.600,00 − 23.400,00 + 16.600,00 + 4.700,00 = 285.700,00" e concluía que junho/2026 tenderia ao Anexo III. A soma desses quatro termos dá **282.500,00** (faltava o pró-labore de mai/26 na conta) e, refeita, a conclusão muda: na leitura-base junho/2026 **fica no Anexo V**; o Anexo III só aparece na variante com a lacuna de U1.

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
- Efeito sobre as apurações futuras: maio/2026 **não** integra a janela deste mês (05/2025–04/2026), mas entra nas janelas seguintes. Com receita de maio/2026 = **84.000,00** (78.000,00 + 6.000,00) em vez de 88.000,00, o RBT12 de **junho/2026** fica ≈ **1.026.000,00** (§3.6) — ainda dentro da **4ª faixa** (limite 1.800.000,00), portanto **sem efeito de alíquota**. Não confundir com o RBT12 desta apuração, que permanece 1.020.000,00.

### 4.2 Premissa P2 (o cliente não respondeu): classificação das atividades

Todas as 7 NFS-e de serviço (1181–1187) foram tratadas como **atividades de TI do mesmo bloco sujeito a Fator R** (Anexo V/III), incluindo "consultoria de arquitetura" (1183) e "treinamento equipe" (1186).
**As listas de atividades dos anexos NÃO estão na biblioteca** (`library/INDEX.md` traz só as tabelas) → a classificação é **NÃO VERIFICÁVEL NA BIBLIOTECA** (QUESTIONS.md U3). Impacto quantificado: se o treinamento (1186, 4.500,00) pertencesse ao Anexo III, o DAS cairia **284,30** (§3.4 e §8.2).

---

## 5. Anexo aplicável a cada receita (art. 18, §4º — segregação)

| receita | anexo | fundamento na biblioteca |
|---|---|---|
| serviços de TI — 78.000,00 | **Anexo V** (4ª faixa) | fator R 27,90% < 28% (`lc123_art18_fator_r.md`, §§5º-J/5º-M) |
| locação de notebooks — 6.000,00 | **Anexo III, deduzida a parcela de ISS** | `locacao_bens_moveis_iss.md`: locação de bens móveis é tributada "na forma do **Anexo III, deduzida a parcela correspondente ao ISS**", porque não é serviço para ISS (**Sv. Vinculante 31**) |

**Como a parcela de ISS foi deduzida (inferência documentada, não texto literal da lei):** `library/locacao_bens_moveis_iss.md` manda tributar a locação "na forma do **Anexo III, deduzida a parcela correspondente ao ISS**", mas **não indica o percentual** a deduzir. O percentual foi retirado da **repartição da 4ª faixa do Anexo III** (`anexos_iii_v_tabelas.md`), que embute **ISS 32,50%** do DAS → fator remanescente **100% − 32,50% = 67,50%**. Como a locação de bens móveis não é fato gerador de ISS (Sv. Vinculante 31), a parcela de ISS é excluída. **Sensibilidade (§7.1):** a tabela de repartição soma **99,85%**; se a lacuna de 0,15% pertencer ao ISS (ISS = 32,65%, redutor 67,35%), a locação custa **505,36** — que é exatamente a soma dos componentes da repartição — e o DAS total cai para **15.187,71** (−1,13).

**Premissa P6 (como a faixa é apurada para cada bloco):** `library/lc123_art18_fator_r.md` (art. 18, §4º) manda segregar as receitas "e aplicar a cada uma o anexo e a alíquota correspondentes", e o §1º-A define a alíquota efetiva com o **RBT12 do contribuinte** — a biblioteca **não disciplina** se a faixa/parcela a deduzir de cada bloco vêm do RBT12 global ou do RBT12 daquela atividade. Adotamos o **RBT12 global (1.020.000,00) para os dois blocos** (4ª faixa em ambos), que é a leitura literal do §1º-A. Leitura **alternativa, não adotada:** apurar a faixa com o RBT12 próprio da locação; como o pacote não traz a locação mês a mês, isso só pode ser ilustrado — se a locação fosse 6.000,00/mês nas 12 competências (72.000,00 → **1ª faixa** do Anexo III, nominal 6,00%, PD 0), a locação custaria 6.000,00 × 6,00% × 67,50% = **243,00** e o DAS cairia **263,49** (14.925,35). Não adotado: pressupõe dado inexistente no pacote e contraria a literalidade do §1º-A (QUESTIONS.md U9).

**Premissa P7 (redutor de ISS da locação):** o fator **67,50%** usado no §6.1 vem da **inferência documentada** descrita acima (ISS 32,50% da repartição do Anexo III, 4ª faixa). A biblioteca não fixa o percentual, e a própria tabela soma 99,85% → sensibilidade de **−1,13** no redutor 67,35% (§7.1, QUESTIONS.md U6).

**Coerência com os documentos:** `documents/nfe_000512_locacao.xml` é uma **NF-e** (modelo 55) de locação, sem destaque de ISS — §7.3.

**Correção técnica ao pedido do sócio** (`documents/email_socio.txt`: "é só repetir o cálculo da tabela com a alíquota da faixa", "acho que vai junto com os serviços"): a **alíquota nominal da faixa (20,50%) não é o valor a recolher**. A lei define a **alíquota efetiva** = (RBT12 × alíquota − PD) ÷ RBT12 (§1º-A). Aplicar 20,50% sobre as receitas do mês daria 17.220,00 — **2.031,16 a maior** (§6.3). Além disso, a fórmula do §1º-A trabalha com o **RBT12**: se a parcela a deduzir de 17.100,00 fosse aplicada sobre uma base mensal isolada — como a receita de locação de 6.000,00 —, o numerador (6.000,00 × 20,50% − 17.100,00 = −15.870,00) seria **negativo**, o que mostra que faixa e parcela a deduzir se referem à receita acumulada de 12 meses, não ao mês. Ver §6.

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

Carga efetiva sobre o mês: 15.188,84 ÷ 84.000,00 = **0,180820 → 18,08%** (arredondada a 4 casas no JSON: 0,180820).

### 6.3 Comparação com o método proposto pelo sócio

| método | serviços | locação | total |
|---|---:|---:|---:|
| **Apurado (correto)** | 14.682,35 | 506,49 | **15.188,84** |
| "20,50% cheio sobre tudo" | 15.990,00 | 1.230,00 | 17.220,00 |
| diferença | +1.307,65 | +723,51 | **+2.031,16 a maior** |

Conta da linha do sócio: 78.000,00 × 20,50% = 15.990,00 e 6.000,00 × 20,50% = 1.230,00 → 17.220,00. Conferência das diferenças: 15.990,00 − 14.682,35 = 1.307,65; 1.230,00 − 506,49 = 723,51; 1.307,65 + 723,51 = 2.031,16 = 17.220,00 − 15.188,84.

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

**Divergência registrada, não compensada:** a tabela da biblioteca **não fecha em 100%** (soma = 99,85%). A diferença de **1,13** entre a soma dos componentes (505,36) e o DAS de locação apurado (506,49) corresponde exatamente a essa lacuna de **0,15%** sobre 750,35 (750,3529… × 0,0015 = 1,1255). Não foi criado valor de "arredondamento" para forçar o fechamento.

Duas leituras, ambas registradas:
- **Adotada — usar a tabela literal (ISS 32,50%):** redutor de 67,50% sobre a efetiva do Anexo III → DAS de locação **506,49**; a soma dos componentes (505,36) fica 1,13 menor que o valor a recolher, e os percentuais não somam 100%.
- **Alternativa — imputar a lacuna de 0,15% ao ISS (32,65%, para a tabela somar 100%):** redutor 67,35% → 750,3529… × 0,6735 = **505,36**, que ** casa exatamente** com a soma dos componentes; DAS total **15.187,71** (Δ −1,13).

A primeira é a que está na biblioteca; a segunda é a que torna a repartição aritmeticamente fechada. Diferença entre elas: **1,13** no DAS do mês (QUESTIONS.md U6).

### 7.2 Serviços — repartição **NÃO APURADA**

A biblioteca **não contém a tabela de repartição do Anexo V**. Inventar percentuais de IRPJ/CSLL/COFINS/PIS/CPP/ISS para os 14.682,35 de serviços seria fato não suportado → **repartição dos serviços não apurada**. No `apuracao.json`, o bloco `reparticao` refere-se **exclusivamente à locação**. (QUESTIONS.md U5 — pedimos a tabela, o cliente não forneceu.)

### 7.3 NF-e 000.512 (locação)

`documents/nfe_000512_locacao.xml`: modelo 55, **sem destaque de ISS** — coerente com a Sv. Vinculante 31 e com o enquadramento da locação no Anexo III sem a parcela de ISS. O documento **destaca PIS 39,00 (0,65%) e COFINS 180,00 (3,00%)** em regime não cumulativo, o que é inconsistente com o Simples Nacional (PIS/COFINS vêm no DAS). A vedação aplicável (art. 13/§ da LC 123) **não está na biblioteca** → observação registrada como **NÃO VERIFICADO NA BIBLIOTECA**, sem efeito sobre o valor do DAS (QUESTIONS.md U7).

Registro adicional, para não deixar o destaque como número solto: 39,00 + 180,00 = **219,00** de PIS/COFINS destacados na nota. Como optante do Simples, essas contribuições **já estão dentro do DAS** (a repartição do Anexo III da biblioteca traz COFINS 14,05% e PIS 3,05% da parcela da locação = 105,42 + 22,89 = **128,31**), de modo que o destaque da nota **não é valor adicional a recolher** — é apenas inconsistência documental a corrigir pelo emissor. **Não há na biblioteca norma que disciplina o destaque**, portanto a conclusão se limita ao aritmético: o valor não foi somado ao DAS e não deve ser pago em separado (QUESTIONS.md U7).

---

## 8. Conciliação com o extrato de maio/2026 e histórico

### 8.1 Extrato — 100% conciliado com as notas

`documents/extrato_maio_2026.csv`:
- **créditos** = 12.500 + 18.000 + 9.800 + 22.000 + 6.700 + 4.500 + 6.000 + 8.500 = **88.000,00** = soma das notas emitidas (82.000,00 serviços + 6.000,00 locação). Cada recebimento casa com uma nota (Orla 12.500 → 1182; Safra 18.000 → 1181; 9.800 → 1183; módulo fiscal 22.000 → 1184; suporte 6.700 → 1185; treinamento 4.500 → 1186; locação 6.000 → NF-e 512; integração 8.500 → 1187).
- **débitos** = 16.600,00 (folha mai/26) + 4.700,00 (DARF/GPS/FGTS abr/26) + 4.200,00 (aluguel) + 1.600,00 + 1.600,00 (pró-labore mai/26) + 10.480,22 (DAS abr/26) + 4.000,00 (estorno 1184) = **43.180,22**.
- **saldo:** 41.280,55 + 88.000,00 − 43.180,22 = **86.100,33** = saldo final do CSV.

**Conferência do PDF contra o CSV (`documents/extrato_maio_2026.pdf`, lido com `pdftotext -layout`):** os dois arquivos descrevem **exatamente o mesmo extrato**. Cabeçalho idêntico — saldo inicial **41.280,55** · débitos **43.180,22** · créditos **88.000,00** · saldo final **86.100,33** — e as **15 transações** são as mesmas, na mesma ordem, com os mesmos valores e os mesmos saldos intermediários (53.780,55 → 71.780,55 → 55.180,55 → 50.480,55 → 60.280,55 → 56.080,55 → 78.080,55 → 76.480,55 → 74.880,55 → 81.580,55 → 71.100,33 → 75.600,33 → 81.600,33 → 90.100,33 → 86.100,33). A coluna "saldo" é **internamente consistente linha a linha** (cada saldo = saldo anterior + montante da linha) e fecha com os totais do cabeçalho. **Não há divergência entre PDF e CSV.** Diferenças apenas de forma: o PDF qualifica o emissor ("Banco Meridional S.A.", período 01/05/2026–31/05/2026, conta final 3302-7) e quebra em duas linhas a descrição do estorno ("PIX ENVIADO ESTORNO GLOSA — CLIENTE 1184"); o CSV usa a forma compacta ("ALUGUEL ESCRITORIO").

Dois registros de transparência: (1) a versão anterior desta memória afirmava que o PDF trazia um débito "OUTBACK STEAK R$ 120,00" e saldo final 100,00 menor — **essa alegação não se sustenta**, nenhum dos dois arquivos contém tal lançamento; ela foi retirada e a conferência acima foi refeita sobre o texto integral do PDF. (2) O rodapé do PDF declara que a instituição bancária é fictícia, criada para um benchmark — registrado apenas como qualificação do documento; a conciliação acima é feita com os valores dos dois arquivos e não depende dessa informação.

### 8.2 Sensibilidades (valores recalculados)

| cenário | efeito no DAS |
|---|---:|
| folha paga ≥ 285.600,00 (ex.: 12ª prestação de pró-labore → 287.800,00) → serviços ao Anexo III | **−4.927,76** (DAS 10.261,08) |
| treinamento (1186, 4.500,00) classificado no Anexo III | **−284,30** (DAS 14.904,54) |
| estorno substituído por nota reemitida em maio (serviços 82.000,00) | **+752,94** (DAS 15.941,78) — **eliminado** pela resposta do cliente |
| lacuna de 0,15% da tabela de repartição imputada ao ISS (redutor 67,35%) | **−1,13** (DAS 15.187,71) — §7.1, U6 |
| método do sócio (20,50% nominal sobre tudo) | **+2.031,16** — **recusado**, sem amparo legal |
| RBT12 menor (ex.: ≤ 720.000 → 3ª faixa) | rebaixa a alíquota; não quantificado por falta de base (P1) |

### 8.3 Anomalia de período anterior (fora do escopo, requer atenção)

DAS **abr/2026 = 10.480,22** pago em 20/05/2026 ≈ **12,05%** da receita de abril → compatível com **Anexo III**, não com o "ano passado a gente pagava pelo Anexo V" do e-mail. Consequências possíveis: (i) as janelas de folha anteriores tinham fator R ≥ 28% — o que tornaria a folha da janela de maio/2026 suspeita de subestimação (§3.5); ou (ii) apurações anteriores em anexo equivocado → **retificação**, fora do escopo de maio/2026 (QUESTIONS.md U4).

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
