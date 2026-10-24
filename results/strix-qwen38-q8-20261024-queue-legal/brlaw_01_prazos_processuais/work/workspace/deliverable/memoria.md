# Memória de contagem de prazos — Processo Digital nº 1044712-38.2026.8.26.0114
**7ª Vara Cível de Campinas (TJSP)** — Procedimento Comum Cível (Cobrança) — **autos eletrônicos (e-SAJ)**
Réis (corréus): Ferreira & Lima Transportes Ltda. (cliente) e Logística Campos Ltda.

## 1. Dados das intimações no DJe (documentos recebidos)

| Intimação | Disponibilização no DJe |
|---|---|
| Citação (despacho de fls. 88) | **19/11/2026** (quinta-feira) |
| Sentença (fls. 212/219) | **10/12/2026** (quinta-feira) |

A citação foi feita por advogado constituído nos autos (procuração fls. 61 — Dr. Otávio Mendes Ribeiro, Ribeiro & Castanho Advogados; fls. 70 — Dra. Marília Sampaio, Sampaio Advocacia). Os dois escritórios são **distintos** (procurações_resumo.md).

## 2. Regras aplicadas e fundamentos

1. **Publicação no DJe** — *publicação* = 1º dia útil seguinte à *disponibilização*.
   Fonte: `library/lei11419_art4.md` (Lei 11.419/2006, art. 4º, §3º); idem CPC art. 224, §2º (`library/cpc_prazos.md`).
2. **Início da contagem** — 1º dia útil **após** a data de publicação; o dia do começo é **excluído** da contagem e o dia do vencimento é **incluído**.
   Fonte: `library/lei11419_art4.md` (art. 4º, §4º); `library/cpc_prazos.md` (arts. 224 *caput*, 224, §3º, 231, VII).
3. **Dias úteis** — computam-se **somente dias úteis** (segunda a sexta, sem feriados/suspensão).
   Fonte: `library/cpc_prazos.md` (art. 219) e `library/calendario_forense_campinas.md`.
4. **Suspensão pelo recesso** — o curso do prazo **suspende-se de 20/12 a 20/01, inclusive**. Dias de suspensão não contam e não corrompem o restante do prazo.
   Fonte: `library/cpc_prazos.md` (art. 220); janela confirmada em `library/calendario_forense_campinas.md`.
5. **Prazo em dobro — NÃO se aplica** — corréus com procuradores de **escritórios distintos** preencheriam o caput do art. 229, **mas** o §2º exclui expressamente o prazo em dobro **nos processos em autos eletrônicos**, e este **é** processo eletrônico (e-SAJ, conforme cabeçalho do DJe e do contrato).
   Fonte: `library/cpc_prazos.md` (art. 229, caput e §2º).
   *Consequência prática:* a afirmação do sócio (e do advogado da Logística Campos) de que “temos prazo em dobro para tudo” **não se confere** nesses autos.
6. **Prazos específicos** — contestação: **15 dias** (CPC art. 335, III, em relação ao art. 231); embargos de declaração: **5 dias** (art. 1.023, que os interrompe para o recurso — art. 1.026); apelação: **15 dias** (art. 1.003, §5º). Fontes: `library/cpc_prazos_recursais.md`.

## 3. Calendário forense usado (trecho relevante de `calendario_forense_campinas.md`)
- 20/11/2026 (sex) — feriado nacional (Zumbi/Consciência Negra, Lei 14.759/2023)
- 08/12/2026 (ter) — feriado **municipal de Campinas** (N. Sra. da Conceição)
- 12/10/2026 — fora das janelas; 28/10 — fora das janelas
- **20/12/2026 a 20/01/2027 (inclusive) — recesso forense (CPC art. 220)**; sem expediente em 24/12, 31/12
- 01/01/2027 (sex) — feriado (dentro do recesso)
- **25/01/2027 (seg) — ANiversário de São Paulo, feriado municipal APENAS na Capital, NÃO em Campinas → conta como dia útil**

## 4. Citação → contestação (15 dias úteis)

Arquitetura: disponibilização → publicação → início → 15 dias úteis.

| Passo | Data | Cálculo / justificativa |
|---|---|---|
| Disponibilização | **19/11/2026** (quinta) | dado do DJe |
| Publicação | **23/11/2026** (seg) | 1º dia útil após 19/11. 20/11 é **feriado nacional**, 21/11-22/11 são **sábado/domingo** → 23/11 (Lei 11.419/2006 art. 4º §3º; CPC 224 §2º) |
| Início da contagem | **24/11/2026** (ter) | 1º dia útil após a publicação (Lei 11.419/2006 art. 4º §4º; CPC 224 §3º). Excluído da contagem em razão do CPC art. 224 *caput* |

Contagem dos 15 dias úteis (iniciando em 25/11/2026):

| Dia útil | Data | Observação |
|---|---|---|
| 1 | 25/11 (qua) | |
| 2 | 26/11 (qui) | |
| 3 | 27/11 (sex) | |
| — | 28-29/11 (sáb/dom) | fim de semana — não computa |
| 4 | 30/11 (seg) | |
| 5 | 01/12 (ter) | |
| 6 | 02/12 (qua) | |
| 7 | 03/12 (qui) | |
| 8 | 04/12 (sex) | |
| — | 05-06/12 (sáb/dom) | fim de semana — não computa |
| 9 | 07/12 (seg) | |
| — | **08/12 (ter)** | **feriado municipal de Campinas — não computa** |
| 10 | 09/12 (qua) | (08/12 é feriado e fica entre 7/12 e 9/12) |
| 11 | 10/12 (qui) | |
| 12 | 11/12 (sex) | |
| — | 12-13/12 (sáb/dom) | fim de semana — não computa |
| 13 | 14/12 (seg) | |
| 14 | 15/12 (ter) | |
| **15** | **16/12/2026 (qua)** | **VENCIMENTO DA CONTESTAÇÃO** |

> **Contestação vence em 16/12/2026 (quarta-feira).** Prazo de 15 dias, **não em dobro**.

**Reconhecimento da contagem (aritmética exibida, via Python):**
`dias_uteis = [25,26,27,30,1,2,3,4,7,9,10,11,14,15,16]` (nov→dez) → o 15º é `16/12`. Feriados/sem dentro do intervalo: 28-29/11, 05-06/12, 08/12 (feriado), 12-13/12 → nenhum deles entraria na lista.

## 5. Sentença → embargos de declaração (5 dias úteis)

| Passo | Data | Justificativa |
|---|---|---|
| Disponibilização | **10/12/2026** (quinta) | dado do DJe |
| Publicação | **11/12/2026** (sex) | 1º dia útil após 10/12 (seguinte dia é sexta, útil) — Lei 11.419/2006 art. 4º §3º |
| Início | **12/12/2026** (sex)? → não: 1º dia útil após 11/12 é **14/12/2026** (seg) | 12/12-13/12 = sáb/dom → 14/12 — CPC art. 224 §3º. Excluído da contagem (CPC 224 caput) |

> **Correção de raciocínio:** o início é o 1º dia útil **após** a publicação. Publicou em sexta 11/12/2026; sábado 12 e domingo 13 não são dias úteis → **início em 14/12/2026 (segunda)**, excluído da contagem. A contagem efetiva começa na **15/12/2026 (terça)**.

Contagem dos 5 dias úteis de embargos (começando em 15/12/2026):

| Dia útil | Data | Observação |
|---|---|---|
| 1 | 15/12 (ter) | |
| 2 | 16/12 (qua) | |
| 3 | 17/12 (qui) | |
| 4 | 18/12 (sex) | |
| — | **20/12/2026 → 20/01/2027 (inclusive)** | **SUSPENDIDO — recesso forense (CPC art. 220)**: 24/12, 31/12 sem expediente; 01/01 feriado |
| — | 19/12 (sáb) | já não-contado antes do recesso (fim de semana) |
| **5** | **21/01/2027 (qui)** | **VENCIMENTO DOS EMBARGOS DE DECLARAÇÃO** |

> **Embargos de declaração vencem em 21/01/2027 (quinta-feira).**

## 6. Sentença → apelação (15 dias úteis)

Mesmo início (14/12/2026 excluído; contagem a partir de 15/12/2026). Se **não** houver embargos de declaração (ou considerando o prazo próprio), contagem de 15 dias úteis:

| Dia útil | Data | Observação |
|---|---|---|
| 1 | 15/12 (ter) | |
| 2 | 16/12 (qua) | |
| 3 | 17/12 (qui) | |
| 4 | 18/12 (sex) | |
| — | **20/12/2026 a 20/01/2027 (inclusive)** | **SUSPENSO — recesso (CPC art. 220)** |
| **5** | **21/01/2027 (qui)** | 1º dia útil após o recesso |
| 6 | 22/01 (sex) | |
| 7 | 25/01 (seg) | **NÃO é feriado em Campinas** (aniversário de SP é só capital) → útil |
| 8 | 26/01 (ter) | |
| 9 | 27/01 (qua) | |
| 10 | 28/01 (qui) | |
| 11 | 29/01 (sex) | |
| — | 30-31/01 (sáb/dom) | fim de semana — não computa |
| 12 | 01/02 (seg) | |
| 13 | 02/02 (ter) | |
| 14 | 03/02 (qua) | |
| **15** | **04/02/2027 (qui)** | **VENCIMENTO DA APELAÇÃO (sem embargos)** |

> **Apelação, sem embargos de declaração, vence em 04/02/2027 (quinta-feira).**
> **Se opostos embargos de declaração:** o prazo da apelação é **interrompido** (CPC art. 1.026) e **recomeça de 15 dias úteis** após a intimação da **decisão** (acórdão/sentença) dos embargos — nova contagem a ser feita naquela data, com o mesmo recesso/feriados de fevereiro/2027 (Carnaval 08-09/02 e Cinzas 10/02, se a intimação posterior coincidir, conforme calendário).

## 7. Tabela-resumo para o calendário do sócio

| Prazo | Inicio (excluído) | Vencimento | Prazo efetivo |
|---|---|---|---|
| Contestação | 25/11/2026 (início 24/11) | **16/12/2026** | 15 dias úteis (não em dobro) |
| Embargos de declaração | 15/12/2026 (início 14/12) | **21/01/2027** | 5 dias úteis + suspensão de recesso |
| Apelação (sem ED) | 15/12/2026 (início 14/12) | **04/02/2027** | 15 dias úteis + suspensão de recesso |
| Apelação (se houver ED) | após decisão dos ED | a recalcular | 15 dias úteis a contar da intimação |

**Prazo em dobro: NÃO** (CPC art. 229, §2º — autos eletrônicos). A tese de “prazo em dobro para tudo” do corréu **não se aplica** a este processo.

## 8. Pontos de atenção / itens abertos

- A **contestação** vence **antes** do recesso (16/12/2026), então o recesso **não** afeta esse prazo — mas é um prazo curto. Confirmar que a contagem a partir de 24/11 foi validada e preparar a contestação.
- Se houver necessidade de **embargos de declaração** para sanar omissão/contradição, o prazo (21/01/2027) é **mais curto e vence logo após o recesso** — prioridade alta.
- O vencimento da **apelação** (04/02/2027) só é seguro **na hipótese de não opor embargos**; se opostos, **recontar** a partir da intimação da decisão dos ED.
- Nenhum dos prazos foi calculado considerando **fórum eletrônico indisponível** (CPC art. 224, §1º) nem **encerramento antecipado de expediente**; se houver, os dias do começo/vencimento seriam **protraídos** para o 1º dia útil seguinte.
