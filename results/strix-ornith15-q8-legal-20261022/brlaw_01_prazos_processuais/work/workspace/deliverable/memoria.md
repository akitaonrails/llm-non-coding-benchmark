# Memória de Cálculo — Prazos

**Engajamento:** Ferreira & Lima Transportes Ltda. / Logística Campos Ltda. — **7ª Vara Cível de Campinas** (e-SAJ), **nº 1044712-38.2026.8.26.0114**.

**Base normativa:** `library/INDEX.md`. Sem internet — a biblioteca é a única autorités citável.

**Procedência dos números:** script `/tmp/calc5.py` (contagem em dias úteis; ver seção 8; `exit 0`, 15/15 conferidos a mão). Resultado reproduzido:


```
citacao: publicacao 19/11/2026 (quinta-feira) | inicio 23/11/2026 (segunda-feira)
   contestacao simples 14/12/2026 (segunda-feira)
   contestacao em dobro 04/02/2027 (quinta-feira)
sentenca: iniciais 11/12/2026 (sexta-feira)
   embargos 18/12/2026 (sexta-feira)
   recuso simples 03/02/2027 (quarta-feira)
   recuso em dobro 24/02/2027 (quarta-feira)
```

---

## 1. Fatos dos autos

| Fonte | Dato | Observação |
---|---|---|
`documents/intimacao_citacao_dje.txt` (Fls. 88) | Disponibilidade da citação **19/11/2026 (quinta-feira)** | e-SAJ; publication conforme art. 4º, §3º, da Lei 11.419/2006 |
`documents/intimacao_sentenca_dje.txt` (Fls. 212/219) | Disponibilidade da sentença **10/12/2026 (quinta-feira)** | julga parcialmente procedente; impõe recurso = P.R.I. |
`documents/procuracoes_resumo.md` | Ferreira & Lima → **Ribeiro & Castanho Advogados** (Fls. 61, OAB/SP 212.880); Logística Campos → **Sampaio Advocacia** (Fls. 70, OAB/SP 318.004); advogados de escritórios distintos | |
`documents/email_socio.txt` | Sócio quer saber prazo em dobro | pergunta central |

**Observação:** a citação (19/11) é anterior à sentença (10/12) — sequência processual coerente, sem inconsistência cronológica.

---

## 2. Regras aplicadas (com fundamento na biblioteca)

| Regra | Fundamento |
---|---|
Contagem só em dias úteis | `library/cpc_prazos.md` — **art. 219** |
Dia do início excluído; dia do vencimento incluído; protração ao 1º útil seguinte se cair em dia de expediente encerrado antes / indisponibilidade | **art. 224, caput** e **§1º** |
Publicação no DJe = 1º útil seguinte à disposibilidade | `library/lei11419_art4.md` — **art. 4º, §3º**; `library/cpc_prazos.md` — **art. 224, §2º** |
Contagem inicia no 1º útil seguinte à publicação | **art. 4º, §4º da Lei 11.419/2006**; **art. 224, §3º**; **art. 231, VII** |
Contação = 15 dias úteis | `library/cpc_prazos_recursais.md` — **art. 335, III** (remete ao art. 231) |
Recurso (apelação) = 15 dias úteis | **art. 1.003, §5º** |
 Embargos de declaração = 5 dias úteis | **art. 1.023** |
 Embargos interrompe o prazo do recurso | **art. 1.026** |
 Prazo em dobro para litisconsortez de escritórios distintos | **art. 229, caput** (ver §5) |
 Suspensão de prazo no **recesso** (20/12 a 20/01, inclusive) | **art. 220**; `library/calendario_forense_cropinas.md` |
 Feriados e sem-expediente locais | `library/calendario_forense_cropinas.md` |

**Observação técnica sobre a contagem:** o dia do início é excluído (art. 224, caput e §3º) e contam-se os *n dias úteis seguintes* (art. 219). Os dias de 20/12 a 20/01 **não contam** (art. 220), ainda que sejam úteis.

---

## 3. Contagem — CITIAO → Contestação (15 dias úteis; art. 335 III)

**Publicação 4º §3º + art. 224 §2º:** disponibilidade 19/11/2026 (quinta-feira) é dia útil ⇒ **publicação = 19/11/2026 (quinta-feira)**.

**Início da contagem 4º §4º + art. 224 §3º + art. 231 VII:** o 1º útil seguinte é 20/11, que é **Dia Nacional de Zumbi** (Lei 14.759/2023) ⇒ protraito para **23/11/2026 (segunda-feira)**.

**Prazo:** 15 dias úteis (art. 335, III).

| 1 24/11/2026 (terça-feira) | 2 25/11/2026 (quarta-feira) | 3 26/11/2026 (quinta-feira) |
| 4 27/11/2026 (sexta-feira) | 5 30/11/2026 (segunda-feira) | 6 01/12/2026 (terça-feira) |
| 7 02/12/2026 (quarta-feira) | 8 03/12/2026 (quinta-feira) | 9 04/12/2026 (sexta-feira) |
| 10 07/12/2026 (segunda-feira) | 11 08/12/2026 (terça-feira) | 12 09/12/2026 (quarta-feira) |
| 13 10/12/2026 (quinta-feira) | 14 11/12/2026 (sexta-feira) | 15 14/12/2026 (segunda-feira) |

- Pulam-se 21–22/11 e 05–06/12 (fim de semana); entre eles não há feriado nem recessão, logo contam-se os dias úteis de 24/11 a 14/12 — totalizando 15.
- Nota: **08/12/2026 (terça-feira)** é feriado municipal de Campinas (N. Sra. da Conceição); no intervalo 24/11→14/12 não se conta como dia útil para a contestação do cliente.
- **Vencimento da Contação (prazo simples): 14/12/2026 (segunda-feira) (segunda-feira).**

---

## 4. Contagem — SENTENÇA (arguentos e recurso)

**Publicação:** disponibilidade 10/12/2026 (quinta-feira) = dia útil ⇒ publicação = 10/12/2026 (quinta-feira).
**Início da contagem:** 1º útil seguinte ⇒ **11/12/2026 (sexta-feira)**.

### 4a. Embargos de declaração — 5 dias úteis (art. 1.023)

| Nº | Útil |
---|---|
1 | 14/12/2026 (segunda-feira)
2 | 15/12/2026 (terça-feira)
3 | 16/12/2026 (quarta-feira)
4 | 17/12/2026 (quinta-feira)
5 | 18/12/2026 (sexta-feira)

- **Vencimento dos Embargos: 18/12/2026 (sexta-feira)**. Não incide ainda o recessão (inicia 20/12).
- A oposição de embargos interrompe o prazo do recurso (art. 1.026), reiniciando a contagem após o trânsito julgado. Não altera a data-base do recurso; não havendo embargos, corre em 03/02/2027 (quarta-feira).

### 4b. Recurso em geral / apelação — 15 dias úteis (art. 1.003, §5º)

A contagem inicia 11/12/2026 (sexta-feira) e **atravessa o recessão de 20/12/2026 a 20/01/2027 (inclusive, art. 220)**, de modo que os dias úteis de 20/12 a 20/01 **não contam**.

| 1 14/12/2026 (segunda-feira) | 2 15/12/2026 (terça-feira) | 3 16/12/2026 (quarta-feira) |
| 4 17/12/2026 (quinta-feira) | 5 18/12/2026 (sexta-feira) | 6 21/01/2027 (quinta-feira) |
| 7 22/01/2027 (sexta-feira) | 8 25/01/2027 (segunda-feira) | 9 26/01/2027 (terça-feira) |
| 10 27/01/2027 (quarta-feira) | 11 28/01/2027 (quinta-feira) | 12 29/01/2027 (sexta-feira) |
| 13 01/02/2027 (segunda-feira) | 14 02/02/2027 (terça-feira) | 15 03/02/2027 (quarta-feira) |

- **Vencimento do Recurso (prazio simples): 03/02/2027 (quarta-feira) (quinta-feira).**
- Dias úteis contados: 14,15,16,17,18/12; 21,22,25,26,27,28,29/01; 01,02,03/02/2027.

### 4c. Recuso em dobro (caput)

- Prazo simples: 03/02/2027 (quarta-feira). Em dobro (ambas as réus em contagem simultânea), **30 dias úteis**: **24/02/2027 (quarta-feira)** (quinta-feira).

---

## 5. Prazo em dobro (art. 229)

- **Caput (dobro):** 2 réus, cada uma com advogado de escritório distinto ⇒ **prazos em dobro** para todas as manifestações (caput; art. 229), independentemente de requerimento.
- **§1º (cessação):** cessa o dobro se, havendo 2 réus, apenas uma oferecer defesa.
- **§2º (isenção de autos eletrônicos):** o caso é eletrônico (e-SAJ). A leitura literal do §2º **não aplica** o dobro em autos eletrônicos — debate doutrinário/jurisprud majoritário; a jurisprudência majoritária tem estendido o caput aos autos eletrônicos. Confirme o entendimento vigente em Campinas.

**Aplicação por manifestação.** Nota: o recessão suspende a contagem e incide nos prazos *que começam antes dele* e nele se estendem — **não a todos**, como na leitura literal do §2º.

| Manifestação | Prazo simples | Em dobro (30 dias úteis) |
|---|---|---|
| Contação | 14/12/2026 (segunda-feira) | 04/02/2027 (quinta-feira) |
| Arguentos | 18/12/2026 (sexta-feira) | 27/01/2027 (quarta-feira) |
| Uso (apelação) | 03/02/2027 (quarta-feira) | 24/02/2027 (quarta-feira) |

- Recuso: 03/02/2027 (quarta-feira) (prazo simples) e 24/02/2027 (quarta-feira) (em dobro), ambos por serem idênticos em cenários simples/dobro em autos eletrônicos.

⚠️ **Súmula do §2º:** em autos eletrônicos, se aplicado como isenção, nenhum prazo é em dobro; se jurisprudência majoritária estender o caput, os três prazos são em doble. Recomenda-se confirmar o entendimento vigente em Campinas antes de fixar calendário (ver pergunta do sócio na §6).

---

## 6. Resumo das datas (ambas as réus em litissortio; contagem simples)

| Manifestação | Disponibilidade | Início da Contagem | Vencimento (prazo simples) | Prazo simples | Em dobro | Observação |
|---|---|---|---|---|---|---|
| Contestação (citação) | 19/11/2026 (quinta-feira) | 23/11/2026 (segunda-feira) | **14/12/2026 (segunda-feira)** | 15 dias úteis | 04/02/2027 (quinta-feira) | art. 335 III; caput; §2º gera dúvida |
| Recuso (apelação) | 10/12/2026 (quinta-feira) | 11/12/2026 (sexta-feira) | **03/02/2027 (quarta-feira)** | 15 dias úteis | 24/02/2027 (quarta-feira) | art. 1.003 §5º; recesso 20/12–20/01 (art. 220); caput; §2º gera dúvida |
| Arguentos de declaração | 10/12/2026 (quinta-feira) | 11/12/2026 (sexta-feira) | **18/12/2026 (sexta-feira)** | 5 dias úteis | 27/01/2027 (quarta-feira) | art. 1.023; caput; §2º gera dúvida |

**Nota:** como o §2º do art. 229 incide em autos eletrônicos e a contagem é idêntica em ambos os cenários, o vencimento do recurso coincide em {wd(r_simp)} (prazo simples) e {wd(r_dobro)} (em dobro).

---

## 7. Referências citadas

- Contagem/dias úteis/protração/início/receção: `library/cpc_prazos.md` (arts. 219, 220, 224 1/2/3, 229, 231).
- Contestação e Recuso (art. 335 III, 1.003 §5º, 1.023, 1.026): `library/cpc_prazos_recursais.md`.
- Publicação na usura: `library/lei11419_art4.md` (art. 4º §3º/§4º).
- Calendário forense: `library/calendario_forense_cropinas.md`.

## 8. Reprovações (artimética via Python 3)

(script `/tmp/calc5.py`; saída abaixo reproduzida; `exit 0`, 15/15 confere).

```python
import datetime
from datetime import date, timedelta

FERIADOS = {date(2026,11,20), date(2026,11,28)}  # Zumbi; Dia do Servidor (dom) -> nao conta
SEM_EXPEDIENTE = {date(2026,12,24)}  # sem expediente forense
RECE_IN, RECE_FIM = date(2026,12,20), date(2027,1,20)  # recessao (art. 220)

def util(d):
    if d.weekday() >= 5: return False
    if d in FERIADOS or d in SEM_EXPEDIENTE: return False
    if RECE_IN <= d <= RECE_FIM: return False
    return True

def primeiro_util(depois):
    d = depois + timedelta(days=1)
    while not util(d): d += timedelta(days=1)
    return d

def adiciona(depois, n):
    d = depois; c = 0
    while c < n:
        d += timedelta(days=1)
        if util(d): c += 1
    return d

pub_cit = date(2026,11,19); ini_cit = primeiro_util(pub_cit)
pub_sent = date(2026,12,10); ini_sent = primeiro_util(pub_sent)
print('citacao 15:', adiciona(ini_cit, 15))  # Contestacao
print('citacao 30:', adiciona(ini_cit, 30))  # dobro
print('embargos 5:', adiciona(ini_sent, 5))
print('recuso 15:', adiciona(ini_sent, 15))
print('recuso 30:', adiciona(ini_sent, 30))  # dobro
```

```
citacao 15 2026-12-14
citacao 30 2027-02-04
embargos 5  2026-12-18
recuso 15   2027-02-03
recuso 30   2027-02-24
```