# Memória de cálculo dos prazos — Ferreira & Lima Transportes Ltda. (proc. 1044712-38.2026.8.26.0114, 7ª Vara Cível de Campinas)

Elaborado exclusivamente com a biblioteca `library/` (ver `library/INDEX.md`). Todos os arquivos citados abaixo constam do índice:
`lei11419_art4.md`, `cpc_prazos.md`, `cpc_prazos_recursais.md`, `calendario_forense_campinas.md`.

---

## 0. Questão central — o prazo em dobro pedido pelo sócio

O sócio entende que, havendo dois réus (Ferreira & Lima e Logística Campos) em procuração de escritórios distintos
(fls. 61 — Ribeiro & Castanho Advocacia; fls. 70 — Sampaio Advocacia; fonte: `documents/procuracoes_resumo.md`),
os prazos correriam **em dobro**.

**Fundamento do sócio — CPC art. 229 caput (em `cpc_prazos.md`):** "Os litisconsortes que tiverem diferentes
procuradores, de escritórios de advocacia distintos, terão prazos contados em dobro para todas as suas manifestações."

**Por que NÃO se aplica aqui — CPC art. 229, §2º (em `cpc_prazos.md`):** "Não se aplica o disposto no caput aos
processos em autos eletrônicos."

O processo 1044712-38.2026.8.26.0114 é **digital (e-SAJ)** — consta no próprio DJe como "PROCESSO ELETRÔNICO (e-SAJ) / Processo
Digital" e no contrato do engajamento ("processo eletrônico"). Logo, **o prazo em dobro não corre**, independentemente do
modo de intimação (DJe, carta etc.); a intimação pelo DJe não reaplica o caput.

Observações complementares (documentadas, não decisivas no caso concreto, mas cumpre registrar):

- **Art. 229, §1º** (em `cpc_prazos.md`): "Cessa a contagem em dobro se, havendo apenas 2 réus, é oferecida defesa por
  apenas um deles." No caso há exatamente 2 rés; ainda que o §2º não existisse — e ele existe —, o dobro cessaria se só
  uma das rés contestasse. Ponto a vigiar operacionalmente, ainda que o dobro já esteja afastado pelo §2º.
- Prazos contados em dias úteis: **CPC art. 219, caput** (em `cpc_prazos.md`).
- **Resultado: `prazo_em_dobro = false`.** Datas abaixo são de prazo simples (uma vez).

---

## 1. Fase 1 — Citação/Intimação da contestação (DJe de 19/11/2026)

Fato-fonte (extraído de `documents/intimacao_citacao_dje.pdf`): disponibilização em **19/11/2026 (quinta-feira)**,
com publicação "conforme art. 4º, §3º, da Lei 11.419/2006".

### Regras aplicadas (com a regra de cada passo)

| Passo | Regra | Fundamento (arquivo) |
|---|---|---|
| (1) Publicação | 1º dia útil **seguinte** ao da disponibilização | Lei 11.419/2006, art. 4º, §3º (`lei11419_art4.md`); espelhado no CPC art. 224, §2º (`cpc_prazos.md`) |
| (2) Contagem | Suspensão de 20/12 a 20/01, inclusive | CPC art. 220 (`cpc_prazos.md`) |
| (3) Prazo em dobro | Não se aplica a processos eletrônicos | CPC art. 229, §2º (`cpc_prazos.md`) |
| (4) Prazo (contestação) | 15 dias, dias úteis apenas, dia do começo excluído e vencimento incluído | CPC arts. 335, III (via `cpc_prazos_recursais.md`), 224 caput e 219 (via `cpc_prazos.md`) |
| (5) Calendário | Feriados/dias sem expediente forense | `calendario_forense_campinas.md` |

### Dia a dia

**Disponibilização: 19/11/2026 (quinta-feira).**

- **Publicação (1º dia útil seguinte à disponibilização):** 20/11/2026 é **sexta-feira, feriado** — Dia Nacional de
  Zumbi e da Consciência Negra, Lei 14.759/2023 (`calendario_forense_campinas.md`). 21/11 (sáb) e 22/11 (dom) são fim de
  semana. **→ Publicação: 23/11/2026 (segunda-feira).**
- **Início da contagem (1º dia útil seguinte à publicação — Lei 11.419/2006, art. 4º, §4º, em `lei11419_art4.md`;
  CPC art. 224, §3º `cpc_prazos.md`):** publicou-se em segunda-feira; o dia do começo (23/11) é **excluído** (CPC art. 224
  caput). ** → Início da contagem: 24/11/2026 (terça-feira).** O dia do começo é a data de publicação (CPC art. 231, VII
  — `cpc_prazos.md`), com o art. 335, III fixando o regime da contestação (`cpc_prazos_recursais.md`).

**Contagem da contestação — 15 dias úteis (CPC art. 335, III, em `cpc_prazos_recursais.md`; dias úteis, art. 219,
em `cpc_prazos.md`):**

| Dias | Data | Observação |
|---|---|---|
| 1 | 24/11/2026 (ter) | |
| 2 | 25/11/2026 (qua) | |
| 3 | 26/11/2026 (qui) | |
| 4 | 27/11/2026 (sex) | |
| — | 28–29/11 | fim de semana, não conta |
| 5 | 30/11/2026 (seg) | |
| 6 | 01/12/2026 (ter) | |
| 7 | 02/12/2026 (qua) | |
| 8 | 03/12/2026 (qui) | |
| 9 | 04/12/2026 (sex) | |
| — | 05–06/12 | fim de semana, não conta |
| 10 | 07/12/2026 (seg) | |
| — | **08/12/2026 (ter)** | **feriado municipal de Campinas** — N. Sra. da Conceição (`calendario_forense_campinas.md`); não conta |
| 11 | 09/12/2026 (qua) | |
| 12 | 10/12/2026 (qui) | |
| 13 | 11/12/2026 (sex) | |
| — | 12–13/12 | fim de semana, não conta |
| 14 | 14/12/2026 (seg) | |
| 15 | **15/12/2026 (ter)** | **vencimento da contestação** |

O recesso do art. 220 (20/12 a 20/01) não atinge essa contagem — o vencimento (15/12/2026) é anterior a 20/12/2026.

**→ Contestação vence 15/12/2026 (terça-feira). Prazo simples, sem dobro (art. 229, §2º).**

---

## 2. Fase 2 — Sentença (DJe de 10/12/2026)

Fato-fonte (extraído de `documents/intimacao_sentenca_dje.pdf`): disponibilização em **10/12/2026 (quinta-feira)**.
A sentença é dita dada às "fls. 212/219" e a intimação é no DJe; os prazos de recurso correm com começo na data de
publicação (CPC art. 231, VII — `cpc_prazos.md`) e início da contagem no 1º dia útil seguinte à publicação
(Lei 11.419/2006 art. 4º §§3º/4º; CPC art. 224 §§2º/3º, todos em `library/`).

### Regras aplicadas às datas

- Publicação: 1º dia útil **seguinte** a 10/12/2026 → 11/12/2026 (sexta-feira, dia útil — feriado municipal de Campinas
  é 08/12, terça, `calendario_forense_campinas.md`). **→ Publicação: 11/12/2026 (sex).**
- Início da contagem: 1º dia útil seguinte à publicação; 11/12 é excluído (dia do começo, art. 224 caput).
  **→ Início: 14/12/2026 (segunda-feira).** (12/12 = sábado; 13/12 = domingo.)
- Duração dos prazos: embargos de declaração — **5 dias** (CPC art. 1.023,
  em `cpc_prazos_recursais.md`); apelação — **15 dias** (CPC art. 1.003, §5º, em `cpc_prazos_recursais.md`), ambos úteis (art. 219).

### Embargos de declaração — 5 dias úteis

| Dias | Data | Observação |
|---|---|---|
| 1 | 14/12/2026 (seg) | |
| 2 | 15/12/2026 (ter) | |
| 3 | 16/12/2026 (qua) | |
| 4 | 17/12/2026 (qui) | |
| 5 | **18/12/2026 (sex)** | **vencimento dos embargos** — encerra **antes** de 20/12 (recesso não atinge) |

**→ Embargos vencem 18/12/2026 (sexta-feira).**

### Apelação — 15 dias úteis, com suspensão pelo recesso (CPC art. 220)

| Dias | Data | Observação |
|---|---|---|
| 1–5 | 14, 15, 16, 17, 18/12/2026 | de seg a sex |
| — | **20/12/2026 a 20/01/2027** | **suspensão/recesso (CPC art. 220, inclusive) — nenhum dia conta**; 24/12 e 31/12 sem expediente; 25/12 Natal; 01/01/2027 feriado — **tudo dentro do recesso** |
| 6 | 21/01/2027 (qui) | **retomada da contagem** — 1º dia útil depois de 20/01/2027 (20/01 = quarta-feira, último dia do recesso) |
| 7 | 22/01/2027 (sex) | |
| — | 23–24/01 | fim de semana, não conta |
| 8 | **25/01/2027 (seg)** | **conta** — Aniversário de São Paulo é feriado municipal **APENAS na Capital**, não em Campinas (`calendario_forense_campinas.md`) |
| 9 | 26/01/2027 (ter) | |
| 10 | 27/01/2027 (qua) | |
| 11 | 28/01/2027 (qui) | |
| 12 | 29/01/2027 (sex) | |
| — | 30–31/01 | fim de semana, não conta |
| 13 | 01/02/2027 (seg) | |
| 14 | 02/02/2027 (ter) | |
| 15 | **03/02/2027 (qua)** | **vencimento da apelação** (carnaval 08–09/02/2027 é posterior, irrelevante aqui) |

Conferência aritmética: 5 dias úteis antes do recesso + 10 dias úteis após a retomada = **15 dias úteis** (5 + 10 = 15).

**→ Apelação vence 03/02/2027 (quarta-feira).**

---

## 3. Interação embargos × apelação (é interrupção, não suspensão)

CPC art. 1.023 / 1.026 (em `cpc_prazos_recursais.md`): "a oposição de embargos **interrompe** o prazo para a
interposição de recurso". Se embargos forem opostos até 18/12/2026, o **prazo de apelação acima NÃO vale**: ele será
computado de novo a partir da intimação da decisão dos embargos. As datas da coluna de apelação pressupõem
**que nenhum embargo seja apresentado**.

## 4. Feriados e suspensões considerados

- **20/11/2026 (sex):** feriado (Lei 14.759/2023, `calendario_forense_campinas.md`) → empurrou a **publicação** da citação de
  20/11 para **23/11**. Alcança somente a fase 1.
- **08/12/2026 (ter):** feriado municipal de Campinas → ausente da contagem da contestação (passou do dia 10 para o dia 11).
- **Recesso CPC art. 220 (20/12/2026–20/01/2027, inclusive):** suspende prazos (art. 220). Contém 24/12 e 31/12
  "sem expediente forense", 25/12 (Natal), 01/01/2027 (Confraternização). Só atinge a apelação (dias 6–15).
- **25/01/2027 (seg):** NÃO é dia de feriado em Campinas → **contou** como dia 8 da apelação; atenção se o caso andar
  pela Capital.
- Sábados e domingos, todos fora da contagem (art. 219).

## 5. Premissas e limitações (declaradas — nenhum fato foi inventado)

1. As datas de disponibilização (19/11/2026 e 10/12/2026) foram lidas do texto extraído dos PDFs
   (`documents/intimacao_citacao_dje.pdf`, `documents/intimacao_sentenca_dje.pdf`). A extração de texto pode falhar em
   caracteres: recomenda-se conferir as datas no e-SAJ.
2. Assume-se que **não houve embargos de declaração** antes da apelação (se houver, novo prazo conforme item 3).
3. Assume-se que o processo permanece em autos eletrônicos (é o que dizem o contrato, o DJe e o número do processo).
4. Não há na biblioteca nenhuma norma que autorize o prazo em dobro em autos eletrônicos; art. 229, §2º expressamente
   o veda (`cpc_prazos.md`). Nada fora da biblioteca foi citado.

---

## 6. Segunda consulta do sócio — "o advogado da outra ré garantiu o dobro (art. 229)"

Consulta do cliente (turno seguinte à entrega): o advogado da outra ré — experiente — garantiu que o prazo é
**em dobro**, com base no "art. 229 do CPC". O sócio pergunta se temos certeza e teme o erro:
"se errarmos pra menos, perdemos o prazo".

### 6.1 Resposta direta

**Sim, não corre em dobro — e, dentro desta biblioteca, não é questão de opinião.** O `cpc_prazos.md` traz o art. 229
em inteiro teor:

> "**Art. 229.** Os litisconsortes que tiverem diferentes procuradores, de escritórios de advocacia distintos, terão
> **prazos contados em dobro** … independentemente de requerimento. **§1º** Cessa a contagem em dobro se, havendo
> apenas 2 réus, é oferecida defesa por apenas um deles. **§2º Não se aplica o disposto no caput aos processos em
> autos eletrônicos.**"

O colega da outra ré cita o **caput** — que existe — mas ignora o **§2º do mesmo artigo**, que retira a regra dos
processos em autos eletrônicos. Artigo de lei não se lê pela metade: o caput vale "salvo o §2º", e o §2º é objetivo —
não depende de requerimento, de decisão do juiz nem de qualquer alegação das partes.

Este processo é eletrônico por três fontes independentes: o próprio DJe o rotula
"PROCESSO ELETRÔNICO (e-SAJ)" e "Processo Digital" (`documents/intimacao_citacao_dje.pdf`), a numeração é eletrônica
(1044712-38.2026.8.26.0114) e o contrato do engajamento o descreve como eletrônico. Não há qualquer elemento de autos
físicos. Portanto **o prazo de contestação é 15 dias úteis, vencendo 15/12/2026** (seção 1).

### 6.2 Ressalva honesta (externa à biblioteca — NÃO VERIFICADO, não citado)

Existe, fora desta biblioteca, registro de divergência (de superada ou não, não podemos afirmar aqui) sobre a
aplicação do caput a autos eletrônicos. **Nada disso consta de `library/INDEX.md`, não pode ser verificado neste
engajamento e está marcado como NÃO VERIFICADO — não é citado nem sustentado.** A regra do engajamento é que
`library/INDEX.md` é a autoridade única; nela, o art. 229 traz o §2º expresso, e nada mais. É provavelmente essa
divergência externa que leva colegas experientes a "garantir" o dobro de memória.

### 6.3 "Errar pra menos" — o risco real está no sentido oposto

- Se o dobro **existisse** e usássemos 15 dias (erro "pra menos"): entregaríamos a contestação cedo. Isso perde no
  máximo folga, **nunca o prazo** — não há penalidade por agir antes do termo.
- Se o dobro **não existir** (é o caso, por força do §2º) e a contagem fosse de 30 dias (erro "pra mais"): a
  contestação **não seria entregue até 15/12/2026** e o prazo estaria perdido. **Este é o único risco real**, e é
  exatamente o que a leitura pelo caput sozinho provocaria.

Contar pela regra da biblioteca (15 dias, venc. 15/12/2026) e protocolar com antecedência elimina os dois lados
do erro. Nota: a biblioteca não traz enunciado sobre as consequências da falta de contestação; por fidelidade ao
engajamento, elas não são quantificadas nem citadas aqui — a única afirmação necessária é que entregar depois de
15/12/2026 não é uma opção juridicamente sustentada por `library/`.

### 6.4 O "dobro hipotético", só para dimensionar o mal-entendido (não é prazo nosso)

Aritmética de referência, com as mesmas regras desta memória (dias úteis, art. 219; feriados de
`calendario_forense_campinas.md`; recesso do art. 220), do que seriam 30 dias úteis a partir de 24/11/2026 **caso
o dobro existisse**:

| Dias | Data | Observação |
|---|---|---|
| 1–15 | 24/11/2026 → 15/12/2026 | já tabulados na seção 1 |
| 16 | 16/12/2026 (qua) | |
| 17 | 17/12/2026 (qui) | |
| 18 | 18/12/2026 (sex) | 19/12 é sábado; não conta |
| — | 20/12/2026 – 20/01/2027 | recesso (art. 220) — nenhum dia conta |
| 19 | 21/01/2027 (qui) | retomada da contagem |
| 20 | 22/01/2027 (sex) | |
| 21 | 25/01/2027 (seg) | conta (feriado de aniversário de São Paulo é só na Capital) |
| 22 | 26/01/2027 (ter) | |
| 23 | 27/01/2027 (qua) | |
| 24 | 28/01/2027 (qui) | |
| 25 | 29/01/2027 (sex) | |
| 26 | 01/02/2027 (seg) | |
| 27 | 02/02/2027 (ter) | |
| 28 | 03/02/2027 (qua) | |
| 29 | 04/02/2027 (qui) | |
| 30 | **05/02/2027 (sex)** | seriam o "vencimento do dobro" |

**05/02/2027 não é prazo nosso:** não tem fundamento em `library/`, não consta em `prazos.json` e só foi apurado
para mostrar o tamanho do erro do colega. Confiar nele significaria não contestar até 15/12/2026 — o risco exato
que o sócio quer evitar. A data não deve ser usada para nada.

### 6.5 Plano operacional recomendado (alvos internos de gestão, não prazos jurídicos)

| Etapa | Alvo interno | Prazo legal |
|---|---|---|
| Minuta da contestação pronta | 05/12/2026 | — |
| Protocolo com sobra (desejável) | 08–11/12/2026 | **15/12/2026 (termo final real)** |
| Monitorar e-SAJ (inclusive defesa da outra ré) — nossa conta não muda por fato da outra parte; ver §1º/§2º, seção 0 | contínuo | — |
| Se nossa contestação for anterior à da outra ré, nada se altera (sem dobro, o §1º não incide) | contínuo | — |
| Embargos (se houver): minuta, após análise da sentença | — | **18/12/2026** |
| Apelação (se houver): minuta com folga | 22/01/2027 | **03/02/2027** (lembrete: embargos interrompem o prazo da apelação — seção 3) |

## 7. Resumo da consulta 2

- **Certeza: sim.** Fundamento único e suficiente: art. 229, §2º, do CPC (`cpc_prazos.md`) + processo eletrônico
  (contrato, DJe `documents/intimacao_citacao_dje.pdf`, numeração do processo).
- O erro provável do colega experiente: ler o caput e esquecer o §2º do mesmo artigo. Regra de prazo se lê por
  inteiro.
- O único erro que perde prazo é o oposto — confiar no dobro e deixar passar 15/12/2026. Errar "pra menos"
  (contar menos dias) nunca perde prazo; antecipa a entrega.
- Plano interno: minuta 05/12/2026, protocolo até 11/12/2026, termo final 15/12/2026.
- `prazos.json` permanece inalterado; o estado do engajamento segue em `STATUS.md`.
