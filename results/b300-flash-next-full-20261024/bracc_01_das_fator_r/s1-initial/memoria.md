# Memória de cálculo — DAS maio/2026 · Lumen Soluções Digitais ME

Escopo: apuração do DAS de **maio/2026** (Simples Nacional), a partir de `documents/`, usando
**exclusivamente** a biblioteca fechada `library/` (itens de `library/INDEX.md`). Todo item fora
da biblioteca está marcado como **NÃO VERIFICADO**. Nada foi consultado fora do workspace.

Convenção: valores em R$, 2 casas; percentuais com 4 casas quando relevantes.

---

## 1. Fatos e documentos da pasta do cliente

| Documento | Conteúdo |
|---|---|
| `documents/notas_emitidas_maio.md` | 7 NFS-e de serviços (R$ 82.000 bruto), estorno parcial R$ 4.000 (NFS-e 1188 sobre a 1184) e NF-e 000.512 de locação de notebooks (R$ 6.000) |
| `documents/faturamento_12_meses.csv` | Receita bruta mês a mês — 2025-05 a 2026-04 |
| `documents/resumo_folha_12_meses.csv` | Folha por **competência** 2025-05 a 2026-04 (salários, pró-labore, INSS patronal+FGTS) |
| `documents/extrato_maio_2026.csv` / `.pdf` | Movimentação bancária de maio/2026 |
| `documents/email_socio.txt` | Instrução do sócio: "repetir o Anexo V com a alíquota da faixa"; pró-labore de abril pago atrasado em 06/05; locação "vai junto com os serviços" |

### 1.1 Conciliação das notas com o extrato (maio/2026)

| Nota | Valor | Recebimento no extrato | Data |
|---|---:|---|---|
| NFS-e 1181 — desenv. sprint 11 | 18.000,00 | TED BANCO SAFRA — CLIENTE | 05/05 |
| NFS-e 1182 — sustentação Orla | 12.500,00 | PIX ORLA TECNOLOGIA | 02/05 |
| NFS-e 1183 — consultoria arquitetura | 9.800,00 | PIX RECEBIDO | 05/09 |
| NFS-e 1184 — módulo fiscal | 22.000,00 | TED — MODULO FISCAL | 05/15 |
| NFS-e 1185 — suporte | 6.700,00 | PIX SUPORTE | 05/19 |
| NFS-e 1186 — treinamento | 4.500,00 | PIX TREINAMENTO | 05/22 |
| NFS-e 1187 — integração | 8.500,00 | PIX INTEGRACAO | 05/28 |
| NFS-e 1188 — estorno 1184 | (4.000,00) | PIX ENVIADO ESTORNO GLOSA | 05/29 |
| NF-e 000.512 — locação notebooks | 6.000,00 | TED LOCACAO NOTEBOOKS | 05/26 |

Todas as 7 notas de serviços têm recebimento correspondente; o estorno foi efetivamente pago
em 29/05. Saldos do extrato conferem linha a linha (saldo final 86.100,33 ✓). Não há
cancelamento adicional de 1181/1182 (os recebimentos de 18.000 e 12.500 constam do extrato).
**Ressalva:** o e-mail do sócio afirma que o pró-labore de abril foi pago atrasado "dia 6 de
maio", mas **não há esse débito no extrato de maio** (apenas DARF/GPS/FGTS ABR em 07/05 e
PRO-LABORE MAI em 16/05). Na resposta à rodada anterior, o cliente informou que o pagamento
ocorreu em **30/04/2026** (lance lançado no sistema só em maio) e comprometeu o comprovante —
divergência documental registrada no §4.

---

## 2. Classificação de cada nota (segregação de receitas)

Base: art. 18, §4º da LC 123/2006 (segregação por atividade) — `library/lc123_art18_fator_r.md`;
e `library/locacao_bens_moveis_iss.md` (locação de bens móveis).

| Documento | Classificação | Tratamento |
|---|---|---|
| NFS-e 1181, 1182, 1183, 1184, 1185, 1186, 1187 | Prestação de serviços de TI (desenvolvimento, suporte, consultoria, treinamento) | compõem a receita de **serviços**, sujeita a Anexo III ou V conforme **Fator R** |
| NFS-e 1188 | Estorno/cancelamento parcial de serviço (glosa), pago em 29/05 | **reduz a receita bruta do mês em que ocorre o cancelamento** (maio/2026) — art. 18, §4º e regra de devoluções/cancelamentos, `lc123_art18_fator_r.md` |
| NF-e 000.512 | **Locação de bens móveis** (20 notebooks) | **NÃO** se junta aos serviços, ao contrário do suposto pelo sócio: vai segregada, tributada pelo **Anexo III com a parcela de ISS deduzida** (LC 123, art. 18, §5º-A; SV 31; Res. CGSN 140, art. 25, §1º, V — `locacao_bens_moveis_iss.md`) |

**Estorno (R$ 4.000,00):** deduzido da receita de serviços de **maio/2026** (mês do
cancelamento). Não altera o RBT12, pois a janela de 12 meses anteriores termina em 04/2026.

**Locação (R$ 6.000,00):** segregada; alíquota própria (Anexo III menos a parcela de ISS),
conforme §5.3 abaixo.

---

## 3. RBT12 e faixa

Fonte: `documents/faturamento_12_meses.csv`; conceito de RBT12 = receita bruta acumulada nos
**12 meses anteriores** ao do período de apuração (LC 123/2006, art. 18, §1º —
`lc123_art18_fator_r.md`). Para maio/2026, janela = **05/2025 a 04/2026** (exatamente o CSV).

```
78.000 + 81.500 + 84.000 + 86.000 + 79.500 + 90.000 + 88.000 + 92.000
+ 85.000 + 83.000 + 86.000 + 87.000 = RBT12 = R$ 1.020.000,00
```

Faixa pela tabela (`library/anexos_iii_v_tabelas.md`): 720.000,00 < 1.020.000,00 ≤ 1.800.000,00
→ **4ª faixa**, tanto no Anexo III quanto no V. (Nota: mesmo que se incluísse a receita de maio,
1.020.000 + 84.000 = 1.104.000, a faixa seria a mesma.)

---

## 4. Fator R — folha paga nos 12 meses anteriores

Regras (`lc123_art18_fator_r.md`): TI é tributada pelo **Anexo III se folha/receita ≥ 28%**
(§§5º-J/5º-M), senão **Anexo V**; folha = importâncias **pagas** nos 12 meses anteriores
(salários, retiradas de pró-labore, contribuições patronais e FGTS), **independentemente da
competência** (Res. CGSN 140, art. 26, §§1º–2º).

O `resumo_folha_12_meses.csv` é por **competência**, mas a lei exige **caixa** (regime de
pagamento). Ajustes necessários e evidências:

- **Pró-labore abril** (R$ 3.200, linha 2026-04 do resumo): **respondido pelo cliente na
  rodada anterior — pago em 30/04/2026**, dentro da janela → **incluído** (3.200). O e-mail do
  sócio dizia "pago atrasado, dia 6 de maio" (fora da janela), e o débito de 06/05 **não consta
  do extrato de maio** — prevalece a resposta mais recente do cliente, que atribuiu o "em
  aberto" do resumo a lançamento contábil feito só em maio). O **comprovante de 30/04 foi
  prometido e não veio** — na 2ª rodada o cliente declarou não ter informação adicional. A
  divergência documental fica **registrada e encerrada como documental** (não forçamos).
- **Encargos de abril** (R$ 4.700, linha 2026-04): pagos em **07/05/2026** (extrato) → fora da
  janela → excluídos; em compensação, sob o padrão de defasagem de 1 mês evidenciado pelo
  extrato, os encargos da **competência 04/2025** teriam sido pagos em 05/2025 (dentro da
  janela), recompondo 12 pagamentos de 4.700 (premissa: encargos 04/2025 = 4.700, valor não
  documentado, constante na série).
- **Salários e pró-labore**: o extrato de maio mostra salários e pró-labore pagos **no próprio
  mês de competência** (FOLHA MAIO em 07/05; PRO-LABORE MAI em 16/05). Assumimos o mesmo padrão
  nos meses anteriores da janela (premissa; o cliente declarou não ter informação adicional).
- **Pró-labore março/2026**: linha 2026-03 do resumo traz **zero** de pró-labore; a observação
  "pró-labore de abril: em aberto na data do resumo" refere-se — pela resposta do cliente — ao
  pró-labore da **competência abril** (pago em 30/04), e não a um valor de março. Adotamos,
  portanto, que **não houve pró-labore na competência março** (nem pagamento correspondente).
  Este é o **único ponto remanescente capaz de mudar o Anexo** (§4.2). Na 2ª rodada o cliente
  declarou **não ter informação adicional** sobre ele; a premissa baseada no resumo fica
  adotada em definitivo, com o risco residual **explicitamente sinalizado**.

### 4.1 Cálculo (janela de pagamento: 05/2025–04/2026)

| Componente | Valor | Justificativa |
|---|---:|---|
| Salários (comp. 05/25–04/26, pagos no mês) | 193.000,00 | 15.500×2 + 15.900×3 + 16.200×3 + 16.400×2 + 16.200 + 16.700 |
| Pró-labore pago na janela | 35.200,00 | 10 × 3.200 (comp. 05/25–02/26, pagos no mês) + 3.200 (comp. 04/26, pago em 30/04/2026 conforme cliente); março sem pró-labore (resumo = 0) |
| INSS patronal + FGTS pagos na janela | 56.400,00 | 12 × 4.700 (competências 04/25–03/26, pagas 05/25–04/26, padrão de 1 mês de defasagem evidenciado pelo extrato) |
| **Folha 12m (cenário principal)** | **284.600,00** | |

**Fator R = 284.600 / 1.020.000 = 0,279020 → 27,90% < 28%** → **Anexo V** para os serviços.

### 4.2 Sensibilidade (todas as combinações possíveis dos fatos remanescentes)

| Cenário | Folha | Fator R | Anexo |
|---|---:|---:|---|
| Pessimista: encargos só comp. 05/25–03/26 pagas na janela (51.700) | 279.900 | 27,44% | V |
| Data do e-mail: pró-labore abril pago em 06/05 (fora da janela) | 281.400 | 27,59% | V |
| **Principal** (cliente: pró-labore abril pago em 30/04, na janela) | **284.600** | **27,90%** | **V** |
| Competência puro (resumo sem ajuste de caixa — não conforme a regra) | 284.600 | 27,90% | V |
| **Único cenário de virada (hipotético)**: existiu pró-labore de março/2026, efetivamente pago até 30/04/2026 — **contraria o resumo (linha 2026-03 = 0)** | 287.800 | 28,22% | III |

Limite: 28% × 1.020.000 = **285.600** (folha ficaria a apenas 1.000,00 do limite no cenário
principal). Com o fato informado pelo cliente (pró-labore de abril pago em 30/04), **todas as
leituras documentadas** — inclusive a data do e-mail (06/05) — mantêm o Fator R abaixo de 28%:
o enquadramento em **Anexo V é robusto**. O único arranjo que levaria ao Anexo III (28,22%)
exigiria um pró-labore de março/2026 pago na janela que o resumo não registra; perguntado nas
duas rodadas, o cliente **não tem informação adicional**. A incerteza residual fica
explicitamente sinalizada em `STATUS.md`/`QUESTIONS.md`.

---

## 5. Cálculo do DAS de maio/2026

### 5.1 Alíquota efetiva (não a nominal!) — Anexo V, 4ª faixa

O sócio pediu para "repetir o Anexo V **com a alíquota da faixa**" (nominal 20,50%). **Isso
contraria a norma da biblioteca**: pelo art. 18, §1º-A (LC 123/2006, `lc123_art18_fator_r.md`),
a **alíquota efetiva** é **(RBT12 × Aliq − PD) / RBT12**. A alíquota nominal da faixa serve só
para compor a efetiva. Refazeremos, portanto, com a efetiva — não com 20,50%.

```
Efetiva Anexo V = (1.020.000 × 0,2050 − 17.100) / 1.020.000
                = (209.100 − 17.100) / 1.020.000
                = 192.000 / 1.020.000
                = 18,8235% (0,18823529...)
```

(Para contraste: com a instrução literal do sócio, os serviços pagariam 78.000 × 20,50% =
15.990,00 — um erro de +1.307,65 vs. 14.682,35. No Anexo III a efetiva seria
(1.020.000 × 0,16 − 35.640)/1.020.000 = 127.560/1.020.000 = 12,5059%.)

### 5.2 Serviços

```
Receita de serviços (maio) = 82.000,00 (bruto) − 4.000,00 (estorno do mês) = 78.000,00
DAS serviços = 78.000,00 × 0,18823529 = 14.682,3529 → R$ 14.682,35
```

### 5.3 Locação de bens móveis (NF-e 000.512)

Pela biblioteca (`locacao_bens_moveis_iss.md`): tributada **pelo Anexo III, deduzida a parcela
correspondente ao ISS** (art. 18, §5º-A; SV 31 — locação de bens móveis não é fato gerador de
ISS). A repartição da 4ª faixa do Anexo III (`anexos_iii_v_tabelas.md`) atribui **32,50%** à
parcela ISS.

**Interpretação aplicada (premissa declarada):** como os percentuais de repartição incidem sobre
o valor devido, a alíquota da locação = efetiva do Anexo III × (1 − 32,50%):

```
Alíquota locação = 0,12505882 × 0,675 = 0,08441471 → 8,4415%
DAS locação = 6.000,00 × 0,08441471 = 506,4882 → R$ 506,49
```

Alternativa interpretativa (dedução da parcela de ISS sobre a **nominal**: 0,12505882 −
0,325×0,16 = 7,3059%): DAS locação = R$ 438,35 (−68,14). A biblioteca não desambigua;
assumimos a 1ª (proporcional à alíquota efetiva paga) — o cliente foi consultado e **não tem
informação adicional**, então a premissa fica adotada em definitivo. A locação **não integra a
base de serviços do Anexo V** (segregação, §4º).

### 5.4 Total

```
DAS maio/2026 = 14.682,35 (serviços, Anexo V) + 506.49 (locação, Anexo III sem ISS)
              = R$ 15.188,84
```

Se o cenário de virada do §4.2 (pró-labore de março/2026 pago na janela, não registrado no
resumo) se confirmasse e o Anexo mudasse para III: serviços = 78.000 × 12,5059% = 9.754,59;
total passaria a 9.754,59 + 506,49 = **R$ 10.261,08**.

---

## 6. Repartição dos tributos no DAS

**Locação (R$ 506,49)** — verificável pela biblioteca (repartição 4ª faixa Anexo III,
`anexos_iii_v_tabelas.md`), aplicada sobre a importância integral de Anexo III
(6.000 × 12,5059% = 750,35) e afastada a cota de ISS (243,86):

| Tributo | % | Valor |
|---|---:|---:|
| IRPJ | 4,00% | 30,01 |
| CSLL | 3,50% | 26,26 |
| COFINS | 14,05% | 105,42 |
| PIS | 3,05% | 22,89 |
| CPP | 42,75% | 320,78 |
| ISS | 32,50% | 0,00 (deduzida — SV 31) |

*Non-reconciliation (não forçamos):* a soma dos percentuais da tabela da biblioteca é
**99,85%**, não 100%; as cotas não-ISS somam 505,36 contra 506,49 pagos (diferença de 1,13).
Deixamos aberto e sinalizado.

**Serviços (R$ 14.682,35, Anexo V)** — **NÃO CALCULÁVEL com a biblioteca fornecida**: o
`INDEX.md` só traz a tabela de repartição do **Anexo III (4ª faixa)**. Não existe na biblioteca a
tabela de repartição do Anexo V. Recusamo-nos a inventar números: em `apuracao.json` os campos
de `reparticao` refletem **apenas a parcela da locação** (valores verificáveis), não o DAS
total. A tabela oficial de repartição do Anexo V foi solicitada ao cliente para inclusão na
biblioteca; ele **não tem informação adicional** (2ª rodada), de modo que a lacuna permanece
e o JSON reflete apenas o verificável.

---

## 7. O que não está na biblioteca (NÃO VERIFICADO)

Qualquer entendimento meu sobre regra não listada em `library/INDEX.md` é **não verificado** e
não foi usado como fundamento. Pontos que dependeriam de norma fora da biblioteca:

1. Tabela de repartição do Anexo V (ausente — ver §6).
2. Desambiguação do modo de deduzir o ISS na locação (§5.3) — a biblioteca dá o princípio, não
   a mecânica exata entre nominal/efetiva.
3. Se a receita de locação entraria no denominador do Fator R dos serviços. Usamos a receita
   bruta total do CSV (conceito literal de "receita bruta" dos 12 meses anteriores em
   `lc123_art18_fator_r.md`); não há evidência de locação nos 12 meses anteriores (só a de
   maio/2026, que está fora da janela).
4. PGDAS-D/portal (prática operacional) — fora da biblioteca, não invocamos.

---

## 8. Fontes da biblioteca utilizadas (todas citáveis por `library/INDEX.md`)

1. `lc123_art18_fator_r.md` — RBT12 (§1º), alíquota efetiva (§1º-A), segregação (§4º),
   devoluções/cancelamentos, Fator R (§§5º-J/5º-M), folha em caixa (Res. CGSN 140, art. 26).
2. `anexos_iii_v_tabelas.md` — faixas/alíquotas/parcelas dos Anexos III e V; repartição 4ª
   faixa do Anexo III.
3. `locacao_bens_moveis_iss.md` — locação de bens móveis: Anexo III com parcela ISS deduzida
   (art. 18, §5º-A; SV 31; Res. CGSN 140, art. 25, §1º, V).

---

## 9. Encerramento da fase de perguntas ao cliente

- **1ª rodada:** respondido o pró-labore de abril (pago em 30/04/2026, na janela), a natureza
  do estorno da NFS-e 1188 (glosa parcial devolvida via PIX em 29/05) e a regularidade da
  NF-e de locação; para as demais, "sem informação adicional".
- **2ª rodada (perguntas 1–4 + premissas da seção D):** o cliente declarou **não ter
  informação adicional** sobre nenhum ponto, inclusive o único capaz de mudar o Anexo
  (pró-labore de março/2026 não registrado no resumo) e o comprovante de 30/04 prometido.
- **Consequência:** não há mais o que perguntar (não repetimos perguntas já respondidas);
  as premissas declaradas ao longo desta memória ficam **adotadas em definitivo** e os
  desconhecimentos residuais estão **explicitamente sinalizados** em `STATUS.md` (U1–U6 em
  `QUESTIONS.md`). Resultado final inalterado: **Anexo V, DAS R$ 15.188,84**.
