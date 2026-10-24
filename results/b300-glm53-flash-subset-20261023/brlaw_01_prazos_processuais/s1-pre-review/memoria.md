# Memória de cálculo — prazos processuais
**Ferreira & Lima Transportes Ltda.** — processo nº 1044712-38.2026.8.26.0114, 7ª Vara Cível de Campinas (autos **eletrônicos**, e-SAJ).
Cliente pergunta do sócio: *"como somos dois réus com advogados diferentes, temos prazo em dobro para tudo. Confere?"*

Fontes de fato: `documents/intimacao_citacao_dje.pdf`, `documents/intimacao_sentenca_dje.pdf`, `documents/procuracoes_resumo.md`, `documents/email_socio.txt`.
Autoridades citadas (exclusivamente, conforme `library/INDEX.md`): `library/cpc_prazos.md`, `library/cpc_prazos_recursais.md`, `library/lei11419_art4.md`, `library/calendario_forense_campinas.md`.

---

## 1. Resposta curta ao sócio: **prazo em dobro NÃO confere**

Os dois réus têm, de fato, procuradores de escritórios distintos (fls. 61 — Ribeiro & Castanho; fls. 70 — Sampaio Advocacia), o que preencheria o *caput* do **CPC art. 229** [library/cpc_prazos.md]. Porém, o próprio artigo afasta a regra nos autos eletrônicos:

> **Art. 229, §2º** — "Não se aplica o disposto no caput aos processos em autos eletrônicos." [library/cpc_prazos.md]

Este processo é digital/e-SAJ (cabeçalho dos DJe e do próprio processo), logo:
- **`prazo_em_dobro = false`** para contestação, embargos e apelação;
- o art. 229, §1º (cessação da dobra se só um réu de dois defende) fica sem aplicação;
- o recomendado é **não contabilizar** a dobra no calendário: o descuido faria perder o prazo real.

*(Consequência ilustrativa — REJEITADA: com dobra a contestação somaria 30 dias úteis e venceria em **10/02/2027**; com a regra correta vence em **16/12/2026** — diferença de 2 meses. Não use 10/02/2027.)*

---

## 2. Regras aplicadas (mapa)

| # | Regra | Fundamento (biblioteca) |
|---|---|---|
| R1 | Contagem **apenas em dias úteis** | CPC art. 219 [library/cpc_prazos.md] |
| R2 | **Publicação** = 1º dia útil seguinte à disponibilização no DJe | CPC art. 224, §2º [library/cpc_prazos.md]; Lei 11.419/2006, art. 4º, §3º [library/lei11419_art4.md] |
| R3 | **Início da contagem** = 1º dia útil seguinte ao da publicação | CPC art. 224, §3º [library/cpc_prazos.md]; Lei 11.419/2006, art. 4º, §4º [library/lei11419_art4.md]; termo de começo no DJe: art. 231, VII [library/cpc_prazos.md] |
| R4 | **Excluir o dia do começo; incluir o do vencimento** | CPC art. 224, *caput* [library/cpc_prazos.md] |
| R5 | Prazos: contestação 15 dias úteis; apelação 15 dias úteis; embargos de declaração 5 dias úteis | CPC art. 335, III [library/cpc_prazos_recursais.md]; art. 1.003, §5º; art. 1.023 [library/cpc_prazos_recursais.md] |
| R6 | **Suspensão do curso** entre 20/12/2026 e 20/01/2027, inclusive — dias do intervalo não contam | CPC art. 220 [library/cpc_prazos.md]; calendário [library/calendario_forense_campinas.md] |
| R7 | Feriados da tabela forense de Campinas não são dias úteis | [library/calendario_forense_campinas.md] |

Verificação aritmética executada em Python (fins de semana + tabela de feriados R7 + janela R6), reproduzindo todas as séries de dias abaixo.

---

## 3. Citação → contestação

**Fatos:** disponibilização no DJe em **19/11/2026 (5ª-feira)**; intimação de ambos os réus por advogado constituído [documents/intimacao_citacao_dje.pdf].

| Etapa | Cálculo | Data |
|---|---|---|
| Disponibilização | intimação publicada no DJe | 19/11/2026 (qui) |
| Publicação (R2) | 20/11/2026 = **feriado** (Zumbi, Lei 14.759/2023); 21/11 sáb; 22/11 dom → 1º dia útil seguinte | **23/11/2026 (seg)** |
| Início (R3) | 1º dia útil após a publicação | **24/11/2026 (ter)** |
| Contagem (R1, R4) | 15 dias úteis, excluindo 24/11 e incluindo o dia 15 | **16/12/2026 (qua)** |

Dia a dia (dias úteis; o dia do começo 24/11 não conta — R4):

1. 25/11 (qua) · 2. 26/11 (qui) · 3. 27/11 (sex) · 4. 30/11 (seg) · 5. 01/12 (ter) · 6. 02/12 (qua) · 7. 03/12 (qui) · 8. 04/12 (sex) · 9. 07/12 (seg) · **[08/12 (ter) = feriado municipal de Campinas, salto — R7]** · 10. 09/12 (qua) · 11. 10/12 (qui) · 12. 11/12 (sex) · 13. 14/12 (seg) · 14. 15/12 (ter) · 15. **16/12/2026 (qua)** ✅ *(série confirmada por Python)*

- Sem interação com o recesso (R6): o vencimento, 16/12/2026, antecede 20/12/2026 e é dia útil ordinário.
- **Vencimento da contestação de Ferreira & Lima: 16/12/2026 (quarta-feira).**

---

## 4. Sentença → embargos de declaração e apelação

**Fatos:** disponibilização no DJe em **10/12/2026 (5ª-feira)**; sentença parcialmente procedente, condenações solidárias, sucumbência recíproca [documents/intimacao_sentenca_dje.pdf].

| Etapa | Cálculo | Data |
|---|---|---|
| Disponibilização | DJe | 10/12/2026 (qui) |
| Publicação (R2) | 11/12/2026 é dia útil ordinário | **11/12/2026 (sex)** |
| Início (R3) | 1º dia útil após a publicação (13/12 dom, 12/12 sáb) | **14/12/2026 (seg)** |

### 4.1 Embargos de declaração — 5 dias úteis (R5)

1. 15/12 · 2. 16/12 · 3. 17/12 · 4. 18/12 · **[20/12/2026 a 20/01/2027 = suspensão (R6)]** · 5. **21/01/2027 (qui)** ✅

O dia 5 cairia em 21/12/2026, dentro da janela suspensiva (R6): o último dia suspenso é 20/01/2027 (qua); a contagem retoma no 1º dia útil seguinte, 21/01/2027 (qui), que se torna o dia 5. **Vencimento 21/01/2027.**

**Vencimento dos embargos de declaração: 21/01/2027 (quinta-feira).**

### 4.2 Apelação — 15 dias úteis (R5)

1. 15/12 · 2. 16/12 · 3. 17/12 · 4. 18/12 · *[suspensão 20/12/2026–20/01/2027]* · 5. 21/01/2027 · 6. 22/01 · **7. 25/01/2027 (seg) — dia útil em Campinas** (feriado municipal *apenas* na Capital; calendário: *"não em Campinas"*) · 8. 26/01 · 9. 27/01 · 10. 28/01 · 11. 29/01 · 12. 01/02 · 13. 02/02 · 14. 03/02 · 15. **04/02/2027 (qui)** ✅

**Vencimento da apelação: 04/02/2027 (quinta-feira).**

---

## 5. Quadro-resumo (datas para o calendário)

| Data | Evento |
|---|---|
| 19/11/2026 | disponibilização DJe — citação |
| 23/11/2026 | publicação (art. 224, §2º; Lei 11.419/2006 art. 4º, §3º) |
| 24/11/2026 | início da contagem |
| **16/12/2026** | **vencimento da contestação (15 dias úteis, SEM dobra)** |
| 10/12/2026 | disponibilização DJe — sentença |
| 11/12/2026 | publicação |
| 14/12/2026 | início da contagem recursal |
| **21/01/2027** | **vencimento dos embargos de declaração (5 dias úteis)** |
| **04/02/2027** | **vencimento da apelação (15 dias úteis)** |

---

## 6. Adenda — dúvida do sócio: "art. 229 do CPC" (2ª passagem)

O advogado da outra ré citou "art. 229 do CPC". Confirmado, **sim: não confere** — e a fonte dele é a nossa:

1. **O art. 229 tem três dispositivos, e o advogado leu só o primeiro.** Íntegra na biblioteca [library/cpc_prazos.md]: *caput* (dobra para litisconsortes de escritórios distintos) + §1º (cessa se só um dos dois réus defende) + **§2º "Não se aplica o disposto no caput aos processos em autos eletrônicos."** Citar "art. 229" invoca o artigo **inteiro**, inclusive o §2º — que elimina a dobra neste processo, 1044712-38.2026.8.26.0114, autos eletrônicos (e-SAJ).

2. **O risco não é "errar pra menos" — é o contrário.** Prazo não se perde por antecipação; perde-se por atraso. Adotando os prazos simples abaixo, qualquer cenário jurídico está coberto:
   | Prazo | Simples (ADOTAR) | Hipótese c/ dobra (rejeitada) |
   |---|---|---|
   | Contestação | **16/12/2026** | 10/02/2027 (30 dias úteis; margem de 56 dias corridos) |
   | Embargos de declaração (5 → 10 dias úteis) | **21/01/2027** | 28/01/2027 |
   | Apelação (15 → 30 dias úteis) | **04/02/2027** | data além da verificada (não calculada — rejeitada) |
   Se o art. 229, §2º prevalece (prevalece: é o texto), quem expectar o prazo dobrado **perde o prazo real de 16/12/2026** — exatamente a catástrofe que o sócio quer evitar. O erro "pra menos" é juridicamente inofensivo: protocolo antes do vencimento nunca é intempestivo.

3. **Nenhum motivo para discordância com o colega**: a afirmativa dele é comum porque a dobra era a regra nos autos físicos; a exceção do §2º — autos eletrônicos —, porém, é expressa e taxativa. Ela dialoga com a Lei 11.419/2006, art. 4º [library/lei11419_art4.md], que disciplina a publicação e o início da contagem no DJe aplicados aqui (seções 3 e 4 desta memória).

**Conclusão reafirmada: `prazo_em_dobro = false`. Datas para o calendário: 16/12/2026, 21/01/2027 e 04/02/2027.**

---

## 7. Ressalvas e condições

1. **Dobra rejeitada por lei, não por fato**: se o processo não fosse eletrônico, a dobra incidiria (art. 229, caput). Nos autos eletrônicos, o §2º afasta a regra. A expectativa do sócio J. Ferreira (e-mail do advogado da co-ré) não prospera; a expressão "prazo em dobro" não teve amparo na biblioteca para este processo.
2. **Embargos interrompem o prazo recursal**: a oposição tempestiva de embargos de declaração **interrompe** o prazo de apelação (nota dos arts. 1.023/1.026 em [library/cpc_prazos_recursais.md]). As datas de apelação acima pressupõem que **ninguém ingressa com ED tempestivo** antes do vencimento; se ingressar, o termo reinicia conforme a regra de interrupção e **as datas devem ser recalculadas** (ver item aberto em STATUS.md).
3. Sem expediente em 24/12, 25/12, 31/12/2026 e 01/01/2027 fica absorvido pela suspensão (R6) — não cria efeito adicional.
4. **Nada além do indexado foi citado**: regras não presentes em `library/INDEX.md` não foram aplicadas nem mencionadas como certeza (p. ex., qualquer detalhe da contagem na Quarta-feira de Cinzas de 18/02/2027 é posterior à apelação e ficou sem efeito).
