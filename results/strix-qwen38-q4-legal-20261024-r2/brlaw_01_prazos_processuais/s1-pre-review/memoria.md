# Memorandum — contagem de prazos
**Processo Digital nº 1044712-38.2026.8.26.0114** — 7ª Vara Cível de Campinas (Comarca de Campinas, TJSP), e-SAJ (autos eletrônicos). Classe: Procedimento Comum Cível — Cobrança. Réus: Ferreira & Lima Transportes Ltda. (Dr. Otávio Mendes Ribeiro, Ribeiro & Castanho Advogados, fls. 61) e Logística Campos Ltda. (Dra. Marília Sampaio, Sampaio Advocacia, fls. 70) — escritórios distintos.

Cliente (e-mail do sócio, `documents/email_socio.txt`): se há **prazo em dobro** (dois réus, escritórios distintos) e quais as datas de **contestação** e de **recurso** da sentença.

---

## 1. Prazo em dobro? — **NÃO**

**Fundamento:** CPC art. 229, caput: litisconsortes com procuradores de escritórios de advocacia distintos têm prazos *contados em dobro* — **§2º: "Não se aplica o disposto no caput aos processos em autos eletrônicos."** (citation: `library/cpc_prazos.md`, Lei 13.105/2015, art. 229).

Os autos são o Processo Digital nº 1044712-38.2026.8.26.0114 em **e-SAJ** (headers de ambos os DJe: `documents/intimacao_citacao_dje.pdf`, `documents/intimacao_sentenca_dje.pdf`). Logo o **§2º exclui o prazo em dobro** e as datas são **idênticas para os dois réus**. A afirmação do advogado da Logística Campos não confere neste processo.

> Nota de transparência: aplico o §2º literalmente, como consta na biblioteca. Não há na biblioteca exceção ou jurisprudência que modifique a conclusão.

---

## 2. Regras aplicadas (fundamento de cada uma)

| Regra | Fundamento (citation: `library/INDEX.md`) |
|---|---|
| Prazos em **dias úteis** | CPC art. 219 (`library/cpc_prazos.md`) |
| **Exclui-se o dia do começo**, inclui-se o dia do vencimento | CPC art. 224, caput (`library/cpc_prazos.md`) |
| **Publicação no DJe = 1º dia útil** seguinte à disponibilização | CPC art. 224, §2º (`library/cpc_prazos.md`); Lei 11.419/2006 art. 4º, §3º (`library/lei11419_art4.md`) |
| **Início do prazo = 1º dia útil** seguinte ao da publicação | CPC art. 224, §3º; art. 231, VII — intimação pelo DJe (`library/cpc_prazos.md`); Lei 11.419/2006 art. 4º, §4º (`library/lei11419_art4.md`) |
| **Suspensão do prazo: 20/12/2026 a 20/01/2027, inclusive** (recesso) | CPC art. 220 (`library/cpc_prazos.md`); `library/calendario_forense_campinas.md` (recesso 20/12/2026–20/01/2027, inclusive; "Não há expediente forense em 24/12 e 31/12") |
| Feriados da comarca de Campinas (excluídos da contagem) | `library/calendario_forense_campinas.md` |
| **Contestação: 15 dias** (termo inicial pelo modo da citação/data de publicação) | CPC art. 335 (`library/cpc_prazos_recursais.md`) |
| **Embargos de declaração: 5 dias** | CPC art. 1.023 (`library/cpc_prazos_recursais.md`) |
| **Apelação: 15 dias** | CPC art. 1.003, §5º (`library/cpc_prazos_recursais.md`) |

**Feriados que realmente caem nas janelas de contagem:** 20/11/2026 (Zumbi e da Consciência Negra, Lei 14.759/2023); 08/12/2026 (N. Sra. da Conceição — feriado **municipal de Campinas**); 24/12/2026 (sem expediente forense); 25/12/2026 (Natal); 31/12/2026 (sem expediente forense); 01/01/2027 (Confraternização Universal).
**Pegadinhas verificadas:** (i) **20/12/2026 é domingo e é o 1º dia do recesso** (CPC art. 220) — nenhum dia útil em 20/12/2026; (ii) **25/01/2027 é dia útil em Campinas** — o feriado de aniversário de SP vale apenas na Capital (citação: `library/calendario_forense_campinas.md`); (iii) o Carnaval de 2027 (08–09/02) é **posterior** ao vencimento da apelação, não interfere.

Cálculos executados em Python 3 (`datetime`): dia útil = segunda a sexta, **descontados** os feriados do calendário forense de Campinas (`library/calendario_forense_campinas.md`) e o recesso 20/12/2026–20/01/2027 (art. 220). O dia a dia abaixo é a saída da execução, sem arredondamento; os vencimentos foram conferidos contra os dias úteis enumerados.

---

## 3. CITAÇÃO — contestação (15 dias úteis — art. 335)

DJ (despacho de fls. 88): **disponibilização 19/11/2026 (qui)**.
**Publicação:** 23/11/2026 (seg) — 20/11/2026 é feriado (Zumbi e da Consciência Negra), 21–22/11 fim de semana; 1º dia útil seguinte = 23/11.
**Início da contagem:** 24/11/2026 (ter) — 1º dia útil após a publicação (art. 224, §3º; art. 231, VII).

Contagem dia a dia (exclui 24/11; conta 15 dias úteis):

| Dia útil | Data | Dia útil | Data |
|---:|---|---:|---|
| 1 | 25/11/2026 (qua) | 9 | 07/12/2026 (seg) |
| 2 | 26/11/2026 (qui) | 10 | 09/12/2026 (qua) |
| 3 | 27/11/2026 (sex) | 11 | 10/12/2026 (qui) |
| 4 | 30/11/2026 (seg) | 12 | 11/12/2026 (sex) |
| 5 | 01/12/2026 (ter) | 13 | 14/12/2026 (seg) |
| 6 | 02/12/2026 (qua) | 14 | 15/12/2026 (ter) |
| 7 | 03/12/2026 (qui) | **15** | **16/12/2026 (qua) ← VENCIMENTO** |
| 8 | 04/12/2026 (sex) | | |

Dias não úteis consumidos no meio (verificação): sáb/doms de 21–22, 28–29/11 e 05–06, 12–13/12. **Feriado não interferiu** (o 08/12 cai fora desta janela).
Nenhum dia de recesso (recesso começa em 20/12/2026, após o vencimento).

> **✅ Contestação: 16/12/2026 (quarta-feira).**

---

## 4. SENTENÇA (publicada no DJ de disponiv. 10/12/2026)

DJ: **disponibilização 10/12/2026 (qui)**.
**Publicação:** 11/12/2026 (sex) — dia útil imediato.
**Início da contagem:** 14/12/2026 (seg) — 1º dia útil após a publicação (art. 224, §3º). Os dois prazos recursais (embargos 5 dias; apelação 15 dias) **partem do mesmo início**.

### 4.1 Embargos de declaração — 5 dias úteis (art. 1.023)

| Dia útil | Data |
|---:|---|
| 1 | 15/12/2026 (ter) |
| 2 | 16/12/2026 (qua) |
| 3 | 17/12/2026 (qui) |
| 4 | 18/12/2026 (sex) |
| *(19/12 dom; 20/12 dom — e a partir de 20/12 começa o recesso: art. 220; 21–23/12, 25/12 (Natal), 28–30/12, 01/01/2027 (Confraternização), 04–08/01, 11–15/01, 18–20/01 — recesso/feriados; 24/12 e 31/12 sem expediente forense)* | |
| 5 | 21/01/2027 (qui) — 1º dia útil após o recesso (20/01/2027 inclusive é dia de suspensão) |

> **✅ Embargos de declaração: 21/01/2027 (quinta-feira).**

### 4.2 Apelação — 15 dias úteis (art. 1.003, §5º)

| Dia útil | Data | Dia útil | Data |
|---:|---|---:|---|
| 1 | 15/12/2026 (ter) | 9 | 29/01/2027 (sex) |
| 2 | 16/12/2026 (qua) | 10 | 01/02/2027 (seg) |
| 3 | 17/12/2026 (qui) | 11 | 02/02/2027 (ter) |
| 4 | 18/12/2026 (sex) | 12 | 03/02/2027 (qua) |
| *(recesso 20/12/2026–20/01/2027, inclusive, art. 220; 24/12 sem exp., 25/12 Natal, 31/12 sem exp., 01/01/2027 Confraternização Universal — e fins de semana ao longo do intervalo — suspensos)* | | **15** | **04/02/2027 (qui) ← VENCIMENTO** |
| 5 | 21/01/2027 (qui) | 13 | 05/02/2027 (sex) |
| 6 | 22/01/2027 (sex) | 14 | 10/02/2027 (qua) |
| 7 | 25/01/2027 (seg) — **não é feriado em Campinas** (aniv. de SP só na Capital) | | |
| 8 | 26/01/2027 (ter) | | |

**Verificações de saída do recesso:** 20/01/2027 (qua) é o **último dia de suspensão** (art. 220, "inclusive"); o 1º dia útil retoma em **21/01/2027 (qui)** → dia útil nº 5. Carnaval 2027 (08–09/02) é posterior ao vencimento (04/02) — não conta.

> **✅ Apelação: 04/02/2027 (quinta-feira).**

### 4.3 Embargos interrompem o prazo de apelação? (item não-verificável na biblioteca)

A biblioteca traz (CPC art. 1.023, `library/cpc_prazos_recursais.md`): "a oposição de embargos **interrompe** o prazo para a interposição de recurso (art. 1.026)". O **art. 1.026 em si não está na biblioteca** — sem texto, não calculo a apelação *caso seja oposto um ED*.

**Cenário hipotético, rotulado como não-verificado** (apenas para o sócio dimensionar; base: interrupção, retomada contagem de 15 dias a partir do 1º dia útil após o vencimento do prazo de ED — suposição de mecânica, sem amparo na biblioteca): se ED for oposto no último dia do prazo (21/01/2027), a apelação hipotética venceria em ~**15/02/2027**. Não usar como data processual; vale a data do §4.2 (04/02/2027) para recurso direto.

---

## 4A. Resposta à dúvida do sócio: "e se o prazo for em dobro? erramos pra menos?"

**Pergunta:** a outra parte garante "art. 229 do CPC — em dobro". Se errarmos pra menos, perdemos o prazo?

**1. Sobre a lei — certeza fundamentada.** O caput do art. 229 concede prazos *contados em dobro* a litisconsortes com procuradores de escritórios distintos (o que é o nosso caso). **Mas o §2º é expresso e literal:** "Não se aplica o disposto no caput aos processos em autos eletrônicos." (citation: `library/cpc_prazos.md`, art. 229, §2º). Os autos são o **Processo Digital nº 1044712-38.2026.8.26.0114 em e-SAJ** — autos eletrônicos — logo o caput **não se aplica**. A garantia do advogado da co-ré ("é em dobro") está **equivocada** para este processo. Não estou adivinhando: está no texto da biblioteca.

> Ressalva honesta: a biblioteca traz só o texto da lei (status "in force"), **sem jurisprudência** dos tribunais sobre o §2º em autos eletrônicos. Não encontro na biblioteca qualquer exceção ou tese que reaplique o caput a autos eletrônicos; por isso sigo o texto literal (não se aplica). Isso é o máximo de segurança que a biblioteca oferece — não há precedente contra o §2º documentado aqui.

**2. Sobre o risco real — a estratégia é "agir na data simples".** A chave é esta: o prazo **em dobro é SEMPRE ≥ o prazo simples**. Então, se eu me comporto como se o prazo fosse **simples** (o mais curto), eu **atendo o prazo em qualquer um dos dois cenários**:

- Se o prazo **for simples** (a leitura correta, §2º): atendo na data simples → ok.
- Se o prazo **fosse em dobro** (cenário que NÃO creio, mas hipoteticamente): a data simples ainda cai **dentro** do prazo em dobro → ok.

Portanto **"agir na data mais curta" nunca nos faz perder prazo**. O único cenário em que se perde prazo é agir *apenas* na data em dobro (mais longa) quando, na verdade, o prazo é simples — o que não é o nosso conselho.

**3. Tabela de ambos os cenários** (contagem idêntica no `prazos.json`/§3–4; coluna "dobro" = período × 2, mesma base):

| Prazo | **Simples (base)** | Início | **Em dobro (hipotético)** | Observação |
|---|---|---|---|---|
| Contestação (art. 335) | **16/12/2026 (qua)** | 24/11/2026 | 10/02/2027 (qua) — 30 d.u. | *ver nota abaixo* |
| Embargos de declaração (art. 1.023) | **21/01/2027 (qui)** | 14/12/2026 | 28/01/2027 (qui) — 10 d.u. | |
| Apelação (art. 1.003, §5º) | **04/02/2027 (qui)** | 14/12/2026 | 01/03/2027 (seg) — 30 d.u. | |

*Nota sobre a contestação em dobro: o vencimento simples já é **16/12/2026**, anterior ao início do recesso; o "dobro" apenas alongaria a janela útil (vencimento 10/02/2027), **não** empurraria para depois do recesso um prazo que já se encerra antes dele. Ou seja, agir em 16/12/2026 cobre tanto o simples quanto o hipotético dobro.*

**4. Recomendação prática:**
- **Calendário do sócio:** 16/12/2026 (contestação), 21/01/2027 (embargos) e 04/02/2027 (apelação) — datas **curtas/seguras**; cobrem ambos os cenários.
- **Margem:** apresente a contestação e os recursos **com antecedência** (não no próprio vencimento), para eliminar risco de indisponibilidade do e-SAJ (art. 224, §1º, item aberto 6.3).
- **Se o litígio sobre o prazo vingar,** o fato de ter-se presentado nas datas simples **inocenta** o risco: não houve intempestividade em nenhum cenário.

**Conclusão:** estou certo de que o §2º do art. 229 exclui o prazo em dobro em autos eletrônicos — há texto expresso na biblioteca, e é a leitura literal. **E, de todo modo, agir nas datas simples é a única estratégia que jamais nos faz perder prazo.** O erro perigoso seria o oposto (contar em dobro).

---

## 5. Resumo

| Prazo | Base | Publicação | Início contagem | **Vencimento** |
|---|---|---|---|---|
| Contestação | art. 335 (15 d.u.) | 23/11/2026 | 24/11/2026 | **16/12/2026 (qua)** |
| Embargos de declaração | art. 1.023 (5 d.u.) | 11/12/2026 | 14/12/2026 | **21/01/2027 (qui)** |
| Apelação | art. 1.003, §5º (15 d.u.) | 11/12/2026 | 14/12/2026 | **04/02/2027 (qui)** |
| Prazo em dobro (CPC art. 229) | autos eletrônicos → **não se aplica (§2º)** | — | — | **não se aplica** |

Estrutura JSON idêntica: `deliverable/prazos.json`.

## 6. Premissas e itens abertos

1. **Premissa** (evidente nos autos): processo é eletrônico (e-SAJ) → §2º do art. 229 aplica-se. Fonte: headers dos dois PDFs do DJe.
2. **Premissa** (calendário): feriado municipal de Campinas (08/12/2026) e a suspensão do recesso (20/12–20/01) seguem `library/calendario_forense_campinas.md`.
3. **Item aberto — art. 224, §1º**: prazos se prorrogam para o 1º dia útil seguinte se houver **indisponibilidade da comunicação eletrônica** (e-SAJ). Nada nos autos informa indisponibilidade; se for constatada indisponibilidade no dia do vencimento (16/12/2026, 21/01/2027, 04/02/2027), o vencimento se desloca para o 1º dia útil seguinte. Recomenda-se checar o DJe/e-SAJ em cada data-limite.
4. **Item aberto — art. 1.026**: fora da biblioteca. Caso o cliente opte por opor ED, a data da apelação tem de ser recalculada a partir da decisão do ED — **não-verificado aqui**.
5. Nenhuma fonte fora de `library/INDEX.md` foi usada.
