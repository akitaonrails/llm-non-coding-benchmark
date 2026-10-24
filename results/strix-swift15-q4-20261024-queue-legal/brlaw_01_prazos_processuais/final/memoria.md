# Memória de contagem de prazos — Pr. 1044712-38.2026.8.26.0114 (7ª Vara Cível de Campinas)

**Cliente:** Ferreira & Lima Transportes Ltda. (corré) — Dr. Otávio Mendes Ribeiro, OAB/SP 212.880, Ribeiro & Castanho Advogados (procuração fls. 61)
**Corré:** Logística Campos Ltda. — Dra. Marília Sampaio, OAB/SP 318.004, Sampaio Advocacia (procuração fls. 70)

Fontes citadas (todas em `library/INDEX.md`):

| Abrev. | Arquivo | Citação |
|---|---|---|
| [CPC-219] | `library/cpc_prazos.md` | Lei 13.105/2015, art. 219 |
| [CPC-220] | `library/cpc_prazos.md` | Lei 13.105/2015, art. 220 |
| [CPC-224] | `library/cpc_prazos.md` | Lei 13.105/2015, art. 224 |
| [CPC-229] | `library/cpc_prazos.md` | Lei 13.105/2015, art. 229 |
| [CPC-231] | `library/cpc_prazos.md` | Lei 13.105/2015, art. 231 |
| [CPC-335] | `library/cpc_prazos_recursais.md` | CPC art. 335 |
| [CPC-ED] | `library/cpc_prazos_recursais.md` | CPC arts. 1.003 §5º e 1.023 |
| [LeiDJe] | `library/lei11419_art4.md` | Lei 11.419/2006, art. 4º, §§3º e 4º |
| [Cal] | `library/calendario_forense_campinas.md` | Calendário forense Campinas/TJSP 2026-2027 |

> **Aviso principal — "prazo em dobro": NÃO se aplica.** A questão é respondida no § 1 abaixo com o
> fundamento [CPC-229].

---

## 1. Prazo em dobro (questão do sócio)

**Fato:** dois réus, advogados de **escritórios de advocacia distintos** (Ribeiro & Castanho × Sampaio
Advocacia — `documents/procuracoes_resumo.md`). O caput do art. 229 do CPC [CPC-229] faria jus a prazo em
dobro "para todas as suas manifestações".

**Porém:** trata-se de **Processo Digital (e-SAJ)** — ambas as intimações do DJe vêm de processo
eletrônico (cabeçalho dos PDFs em `documents/`). O **art. 229, §2º** [CPC-229] dispõe que a contagem em
dobro **não se aplica aos processos em autos eletrônicos**. O §1º (cessa a contagem em dobro se, havendo
apenas 2 réus, é oferecida defesa por apenas um deles) é irrelevante aqui, dado o §2º.

**Conclusão:** `prazo_em_dobro = false`. Todos os prazos contam-se **simples** (15 dias para
contestação/apelação, 5 dias para embargos de declaração).

### 1.1 Análise de risco (pergunta do sócio: "tem certeza? se errarmos pra menos, perdemos o prazo")
O argumento do advogado da corré se baseia no caput do art. 229 [CPC-229], que é real — dá prazo em
dobro a litisconsortes com procuradores de escritórios distintos. A resposta é o **§2º do mesmo
artigo** [CPC-229], que exclui expressamente os processos em autos eletrônicos (este é e-SAJ).

**A assimetria que resolve a preocupação:** entregar **antes** do prazo curto é tempestivo em
*ambas* as hipóteses; entregar no prazo longo só é seguro se o dobro valer. Portanto não há
desvantagem em calendarizar pela data curta — e esperar a data longa é a única estratégia que expõe
a perder o prazo. **Recomendação: agendar para o prazo simples.**

Para transparência, se o dobro *por hipótese* se aplicasse (datas calculadas pelo mesmo script):

| Prazo | Simples (aplicável) | Dobro (hipótese não aplicável) |
|---|---|---|
| Contestação | 15/12/2026 (ter) | 05/02/2027 (sex) |
| Apelação | 03/02/2027 (qua) | 26/02/2027 (sex) |

> **Verificação não confirmada:** a jurisprudência dos tribunais sobre a vigência/alcance do §2º do art.
> 229 **não consta da biblioteca** e o ambiente não tem acesso a internet. A aplicação aqui é a do texto
> vigente tal como constou [CPC-229], sem verificação externa.

---

## 2. Intimação de citação — DJe de 19/11/2026

### 2.1 Fatos
- Disponibilização no DJe: **19/11/2026 (quinta-feira)** — `documents/intimacao_citacao_dje.pdf`.
- Despacho de fls. 88: cita/intima a corré Ferreira & Lima para **contestação no prazo legal**, sob pena
  de revelia.

### 2.2 Regras
1. **Publicação:** primeiro dia útil seguinte à disponibilização — [LeiDJe §3º]; idêntico [CPC-224 §2º].
2. **Início da contagem:** primeiro dia útil que seguir ao da publicação — [LeiDJe §4º]; idêntico
   [CPC-224 §3º]. (A data de publicação é o ponto de referência do "começo do prazo" para intimação
   por DJe — [CPC-231 VII] —; a contagem propriamente dita só inicia no dia útil seguinte.)
3. **Contagem:** somente dias úteis — [CPC-219]; exclui o dia do começo e inclui o do vencimento
   [CPC-224 caput].
4. **Feriados/sem expediente:** 20/11/2026 (Zumbi/Consciência Negra — [Cal]); 21–22/11 (fim de semana);
   08/12/2026 (N. Sra. da Conceição, feriado municipal de Campinas — [Cal]).

### 2.3 Cálculo da publicação
```
19/11/2026 (qui) disponibilização
+1 → 20/11 (sex)  feriado [Cal]   → excluído
+2 → 21/11 (sáb)  fim de semana   → excluído
+3 → 22/11 (dom)  fim de semana   → excluído
+4 → 23/11 (seg)  dia útil        ✔ PUBLICAÇÃO = 23/11/2026
```

### 2.4 Cálculo do início
```
23/11 (seg) publicação
+1 → 24/11 (ter)  dia útil        ✔ INÍCIO DA CONTAGEM = 24/11/2026
```

### 2.5 Contagem de 15 dias úteis — contestação [CPC-335] + [CPC-219]
```
nº  data      dia     observação
 1  24/11/26  ter
 2  25/11/26  qua
 3  26/11/26  qui
 4  27/11/26  sex
    28–29/11  s/f   → excluídos (fim de semana)
 5  30/11/26  seg
 6  01/12/26  ter
 7  02/12/26  qua
 8  03/12/26  qui
 9  04/12/26  sex
    05–06/12  s/f   → excluídos (fim de semana)
10  07/12/26  seg
    08/12/26  ter   → excluído (feriado municipal [Cal])
11  09/12/26  qua
12  10/12/26  qui
13  11/12/26  sex
    12–13/12  s/f   → excluídos (fim de semana)
14  14/12/26  seg
15  15/12/26  ter   ✔ VENCIMENTO = 15/12/2026
```

**→ Contestação: 15/12/2026 (terça-feira)** — prazo simples (sem dobro, §1).

---

## 3. Intimação de sentença — DJe de 10/12/2026

### 3.1 Fatos
- Disponibilização no DJe: **10/12/2026 (quinta-feira)** — `documents/intimacao_sentenca_dje.pdf`.
- Sentença de fls. 212/219: parcialmente procedente; condenação solidária; "P.R.I.".
- Prazos cabíveis de ofício: **embargos de declaração — 5 dias** [CPC-ED: art. 1.023];
  **apelação — 15 dias** [CPC-ED: art. 1.003 §5º].

### 3.2 Cálculo da publicação [LeiDJe §3º]
```
10/12/26 (qui) disponibilização
+1 → 11/12 (sex)  dia útil [Cal]  ✔ PUBLICAÇÃO = 11/12/2026
```
(o primeiro dia útil seguinte já é 11/12, antes do recesso — 24/12, 25/12, 31/12 e o recesso não interferem)

### 3.3 Cálculo do início [CPC-224 §3º; Lei 11.419/2006 §4º]
```
11/12 (sex) publicação
+1 → 12/12 (sáb)  fim de semana → excluído
+2 → 13/12 (dom)  fim de semana → excluído
+3 → 14/12 (seg)  dia útil       ✔ INÍCIO DA CONTAGEM = 14/12/2026
```

### 3.4 Embargos de declaração — 5 dias úteis [CPC-ED: art. 1.023]
```
nº  data      dia
 1  14/12/26  seg
 2  15/12/26  ter
 3  16/12/26  qua
 4  17/12/26  qui
 5  18/12/26  sex  ✔ VENCIMENTO = 18/12/2026
```
(Último dia útil antes do recesso: 19/12 é sábado, 20/12 é domingo e já abre a suspensão — [Cal].)

**→ Embargos de declaração: 18/12/2026 (sexta-feira).**

### 3.5 Apelação — 15 dias úteis, com suspensão pelo recesso [CPC-ED: art. 1.003 §5º; CPC-220]

O **recesso forense de 20/12/2026 a 20/01/2027 (inclusive)** suspende o curso do prazo — [CPC-220];
[Cal] confirma o período. Nenhum dia do intervalo conta — [CPC-219].

Saída do script de verificação (Python 3), dia a dia:

```
 1  14/12/2026 (seg)
 2  15/12/2026 (ter)
 3  16/12/2026 (qua)
 4  17/12/2026 (qui)
 5  18/12/2026 (sex)
 ── 20/12/2026 a 20/01/2027: RECESSO [CPC-220] — 32 dias suspensos
 │   (inclui 24/12, 25/12 e 31/12 sem expediente forense [Cal], 01/01 [Cal], fins de semana) ──
 6  21/01/2027 (qui)
 7  22/01/2027 (sex)
    23–24/01 (sáb/dom) → excluídos (fim de semana)
 8  25/01/2027 (seg)  CONTA: feriado municipal APENAS em São Paulo/SP, não em Campinas [Cal]
 9  26/01/2027 (ter)
10  27/01/2027 (qua)
11  28/01/2027 (qui)
12  29/01/2027 (sex)
    30/01–01/02 (sáb/dom) → excluídos (fim de semana)
13  01/02/2027 (seg)
14  02/02/2027 (ter)
15  03/02/2027 (qua)  ✔ VENCIMENTO = 03/02/2027
```
Os feriados de Carnaval (08–09/02/2027 [Cal]) não são alcançados pela contagem
(o 15.º dia cai em 03/02), mas figurariam nas contagens mais longas (ex.: apelação condicionada,
abaixo).

**→ Apelação: 03/02/2027 (quarta-feira)** — prazo simples.

#### Cenário condicionado (informação ao cliente)
Se forem opostos **embargos de declaração** (vencem em 18/12/2026), o prazo de apelação é
**interrompido** e recomeça do primeiro dia útil seguinte à publicação da sentença que os julgar —
[CPC-ED: art. 1.023, cujo texto menciona o art. 1.026]. O termo inicial exato depende da data de
publicação dessa sentença no
DJe, que **ainda não se conhece**. Por referência apenas: se o prazo de 15 dias úteis começasse no
primeiro dia útil após o vencimento dos embargos, o script daria **12/02/2027**
(1: 21/01, 2: 22/01, 3: 25/01 … 10: 03/02, 11: 04/02, 12: 05/02, 13: 10/02, 14: 11/02, 15: 12/02,
pulando o Carnaval de 08–09/02 e o fim de semana 06/02) — **não é o critério legal**, apenas
referência para escalação de agenda.

---

## 4. Resumo de datas

| Evento | Data |
|---|---|
| Publicação da citação | 23/11/2026 (seg) |
| Início da contagem (citação) | 24/11/2026 (ter) |
| **Vencimento da contestação** | **15/12/2026 (ter)** |
| Publicação da sentença | 11/12/2026 (sex) |
| Início da contagem (sentença) | 14/12/2026 (seg) |
| **Vencimento dos embargos de declaração** | **18/12/2026 (sex)** |
| **Vencimento da apelação (sem embargos)** | **03/02/2027 (qua)** |
| Prazo em dobro | **Não se aplica** (CPC art. 229, §2º — autos eletrônicos) |

## 5. Notas e ressalvas
- **Cálculos** executados em Python 3; todas as contagens (citação, sentença, cenário condicionado e
  hipótese de dobro) foram conferidas por script; os resultados do script são os que constam em
  `prazos.json`.
- **25/01/2027** foi deliberadamente **contado como dia útil**: a biblioteca [Cal] registra-o como
  feriado municipal **apenas na Capital (São Paulo)**, não em Campinas.
- Os dias de **recesso suspensos** na apelação: 20/12/2026 a 20/01/2027 (inclusive) — 32 dias — [CPC-220],
  [Cal].
- **Divergência de datas nos documentos (deixada aberta):** a sentença foi publicada
  11/12/2026, **antes** do vencimento da contestação (15/12/2026) — ordem incomum num Procedimento
  Comum (normalmente a sentença vem depois de esgotada a fase de resposta). Os cálculos seguem
  fielmente as datas das duas intimações fornecidas [`documents/`], mas recomendo confirmar nos
  autos se há outra intimação ou fato processual (ex.: sentença sobre questão prévia/cerceamento,
  desistência parcial, reconvenção) que explique a ordem. **Não forçado a reconciliar.**
- **Não verificado (sem internet):** alcance/jurisprudência do art. 229, §2º CPC; eventual regra local
  de prorrogação de expediente em 18/12/2026 (último dia útil antes do recesso) — ambas ausentes da
  biblioteca. Se o TJSP/Campinas tivesse comunicado de expediente antecipado em 18/12/2026, o vencimento
  dos embargos seria protraído (CPC art. 224, §1º) — **não consta na biblioteca**; tratado como
  hipótese aberta, não como fato.
