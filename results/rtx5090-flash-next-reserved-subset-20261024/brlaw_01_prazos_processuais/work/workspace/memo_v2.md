# Memória de cálculo de prazos — autos nº 1044712-38.2026.8.26.0114

**Réus:** Ferreira & Lima Transportes Ltda. (fls. 61 — Dr. Otávio Mendes Ribeiro, OAB/SP 212.880, Ribeiro & Castanho Advogados) e Logística Campos Ltda. (fls. 70 — Dra. Marília Sampaio, OAB/SP 318.004, Sampaio Advocacia)
**Autora:** Distribuidora Vale Verde Ltda.
**Juízo:** 7ª Vara Cível da Comarca de Campinas/SP (TJSP) — o próprio cabeçalho das intimações diz "PROCESSO ELETRÔNICO (e-SAJ)" e "Processo Digital nº 1044712-38.2026.8.26.0114"
**Documentos usados:** `documents/intimacao_citacao_dje.pdf`, `documents/intimacao_sentenca_dje.pdf`, `documents/procuracoes_resumo.md`, `documents/email_socio.txt`
**Fontes citadas (só o que está em `library/INDEX.md`):** `library/cpc_prazos.md`, `library/cpc_prazos_recursais.md`, `library/lei11419_art4.md`, `library/calendario_forense_campinas.md`

> ### Resposta à pergunta do sócio (e‑mail de Jorge Ferreira): **não, não há prazo em dobro.**
>
> O art. 229, **caput**, do CPC de fato dá prazo em dobro aos litisconsortes com procuradores de
> escritórios distintos — e é o caso daqui (fls. 61 × fls. 70, escritórios diferentes). Mas o
> **§ 2º do mesmo artigo**, no texto de `library/cpc_prazos.md`, diz:
> **"§2º Não se aplica o disposto no caput aos processos em autos eletrônicos."**
> Os autos são eletrônicos (e‑SAJ). **Logo, prazo simples para os dois réus, para todas as
> manifestações.** O que o advogado da corré disse está errado quanto à conclusão.
>
> Datas (prazo simples, contagem em dias úteis, calendário de Campinas da biblioteca):
>
> | Manifestação | Vencimento |
> |---|---|
> | Contestação (15 dias — art. 335) | **{{v_contest}}** |
> | Embargos de declaração da sentença (5 dias — art. 1.023) | **{{v_emb}}** |
> | Apelação, se não houver embargos (15 dias — art. 1.003, §5º) | **{{v_apel}}** |
>
> Se embargos de declaração forem opostos até {{v_emb}}, **a data de apelação acima deixa de
> valer** (os embargos interrompem o prazo recursal — item "Interrupção" de
> `library/cpc_prazos_recursais.md`). Ver Seção 7.

---

## 1. O que os documentos dizem — e o que não dizem

| Dado | Intimação da citação (despacho de fls. 88) | Intimação da sentença (fls. 212/219) |
|---|---|---|
| Disponibilização no DJe | **{{d_cit}}** ({{dw_cit}}) | **{{d_sent}}** ({{dw_sent}}) |
| Caderno | "Diário da Justiça Eletrônico — Caderno Judicial — 1ª Instância — Interior" | idem |
| Modalidade | "Processo Digital" / "PROCESSO ELETRÔNICO (e‑SAJ)" | idem |
| Data de publicação indicada no documento | "Data de publicação: **conforme art. 4º, §3º, da Lei 11.419/2006**" (data não impressa) | não impressa; mesmo mecanismo de DJE |
| Ato intimado | "Cite‑se e intime‑se a corré FERREIRA & LIMA TRANSPORTES LTDA., **na pessoa de seu advogado constituído nos autos** (procuração de fls. 61 …), para, querendo, apresentar contestação **no prazo legal**, sob pena de revelia. Intime‑se igualmente a corré LOGÍSTICA CAMPOS LTDA., por seu advogado (fls. 70 …)" | sentença que "JULGO PARCIALMENTE PROCEDENTES os pedidos para condenar as rés, solidariamente, ao pagamento de R$ 184.300,00 … Honorários de 10% … P.R.I." |
| Prazo em dias impresso no documento | **não há** (só "prazo legal") | **não há** (nenhum "último dia" impresso) |

Consequência metodológica: **nenhuma data de vencimento vem do papel** — todas resultam da contagem
feita abaixo a partir da disponibilização. Não existe, nos documentos, linha "DJe disponibilizado em /
publicado em" nem certidão de citação (AR/mandado) com data; isso é premissa declarada na Seção 10.

---

## 2. Regras aplicadas (todas com texto no acervo)

| Regra | Texto (de `library/`) | Arquivo |
|---|---|---|
| Só dias úteis | "Art. 219. Na contagem de prazo em dias, estabelecido por lei ou pelo juiz, computar‑se‑ão **somente os dias úteis**." | `cpc_prazos.md` |
| Suspensão de 20/12 a 20/01 | "Art. 220. **Suspende‑se o curso do prazo processual nos dias compreendidos entre 20 de dezembro e 20 de janeiro, inclusive.**" | `cpc_prazos.md` |
| Excluir o dia do começo | "Art. 224. Salvo disposição em contrário, os prazos serão contados **excluindo o dia do começo e incluindo o dia do vencimento**." | `cpc_prazos.md` |
| Publicação no DJE | "Art. 224, §2º **Considera‑se como data de publicação o primeiro dia útil seguinte ao da disponibilização da informação no Diário da Justiça eletrônico.** §3º **A contagem do prazo terá início no primeiro dia útil que seguir ao da publicação.**" | `cpc_prazos.md` |
| Publicação no DJE (mesma regra, lei especial) | "§3º Considera‑se como data da publicação o primeiro dia útil seguinte ao da disponibilização da informação no Diário da Justiça eletrônico. §4º Os prazos processuais terão início no primeiro dia útil que seguir ao considerado como data da publicação." | `lei11419_art4.md` |
| Dia do começo no processo eletrônico | "Art. 231. … VII – **a data de publicação**, quando a intimação se der pelo Diário da Justiça impresso ou eletrônico." | `cpc_prazos.md` |
| Termo inicial da contestação | "Art. 335. O réu poderá oferecer contestação, por petição, no prazo de **15 (quinze) dias**, cujo termo inicial será a data: … III – **prevista no art. 231**, de acordo com o modo como foi feita a citação." | `cpc_prazos_recursais.md` |
| Embargos de declaração | "Art. 1.023. Os embargos de declaração serão opostos, no prazo de **5 (cinco) dias** …" + "a oposição de embargos **interrompe** o prazo para a interposição de recurso (art. 1.026)" | `cpc_prazos_recursais.md` |
| Apelação | "Art. 1.003, §5º. Excetuados os embargos de declaração, o prazo para interpor os recursos e para responder‑lhes é de **15 (quinze) dias**." | `cpc_prazos_recursais.md` |
| Prazo em dobro (e sua exclusão) | "Art. 229. Os litisconsortes que tiverem diferentes procuradores, de escritórios de advocacia distintos, terão **prazos contados em dobro** … §1º Cessa a contagem em dobro se, havendo apenas 2 réus, é oferecida defesa por apenas um deles. **§2º Não se aplica o disposto no caput aos processos em autos eletrônicos.**" | `cpc_prazos.md` |
| Feriados / sem expediente / recesso do foro | tabela de 23 datas + comunicado "Recesso/suspensão de prazos (CPC art. 220): **20/12/2026 a 20/01/2027, inclusive**. Não há expediente forense em 24/12 e 31/12." | `calendario_forense_campinas.md` |

## 3. Cadeia de publicação e critério de contagem (por que o "dia 1" é o dia seguinte ao da publicação)

1. **Disponibilização** (dado do documento) →
2. **Data de publicação = primeiro dia útil seguinte** (Lei 11.419/2006, art. 4º, §3º; CPC art. 224, §2º) — a intimação da citação manda expressamente aplicar esse §3º;
3. Essa data de publicação é o **dia do começo** do prazo (CPC art. 231, VII), que é **excluído** da contagem (CPC art. 224, caput);
4. **A contagem começa no primeiro dia útil seguinte ao da publicação**, que é o **dia 1** (CPC art. 224, §3º: "A contagem do prazo terá início no primeiro dia útil que seguir ao da publicação"; Lei 11.419, art. 4º, §4º, idêntico);
5. Correm só os dias úteis (art. 219), com suspensão de 20/12 a 20/01 (art. 220); o vencimento é incluído (art. 224, caput).

A leitura das três normas é encaixada, não concorrente: a **publicação** é o dia do começo excluído
pelo caput do art. 224; o **§3º** diz que a contagem *começa* no dia útil seguinte. Não se exclui
nenhum segundo dia. Existe no foro a leitura de que também o primeiro dia útil seguinte à publicação
seria "dia do começo" e, por isso, igualmente excluído (**"critério B"**, que desloca tudo um dia
útil para frente); **nenhuma norma do acervo a sustenta** — ao contrário, o §3º do art. 224 e o §4º
do art. 4º da Lei 11.419 fixam expressamente o início no primeiro dia útil seguinte — e ela
equivaleria a excluir duas vezes o mesmo dia. Ainda assim a contagem B foi **calculada**
(`calculo_prazos.py`, dicionário `B`) para controle, e a diferença está na Seção 10.1: a divergência
é de **um dia útil em cada prazo**, o que na apelação significa mudar o vencimento de
{{v_apel}} para {{v_apel_B}}.

## 4. Janela de publicação das duas intimações

{{tab_publicacao}}

- **Citação:** disponibilização {{d_cit}} ({{dw_cit}}); o dia seguinte, 20/11/2026 (sexta‑feira), é
  feriado nacional na tabela ("Dia Nacional de Zumbi e da Consciência Negra — Lei 14.759/2023"),
  então o primeiro dia útil seguinte é {{p_cit}} ({{pw_cit}}) — a data de publicação (dia do começo,
  excluído). Dia 1: {{i_cit}} ({{iw_cit}}).
- **Sentença:** disponibilização {{d_sent}} ({{dw_sent}}), que já é dia útil; primeira sexta‑feira
  seguinte... na verdade o primeiro dia útil seguinte é {{p_sent}} ({{pw_sent}}) — sexta‑feira, dia
  útil na tabela —, que é a publicação (dia do começo, excluído). Dia 1: {{i_sent}} ({{iw_sent}}),
  segunda‑feira seguinte.

## 5. Citação → contestação ({{c_prazo_cit}} dias úteis, art. 335 c/c art. 231, VII)

{{tab_citacao}}

**Vencimento: {{v_contest}} ({{vw_contest}}).** Conferência: {{c_uteis_cit}} dias úteis contados de
{{i_cit}} a {{v_contest}}, inclusive {{i_cit}}.

Dentro desse prazo entrou **um feriado municipal de Campinas**: 08/12/2026 (terça‑feira),
"N. Sra. da Conceição — feriado municipal de Campinas". Sem ele o vencimento seria {{sem_fer_0812}}.

## 6. Sentença → embargos de declaração (5 dias, art. 1.023)

{{tab_emb}}

**Vencimento: {{v_emb}} ({{vw_emb}}).** Nenhum feriado dentro da janela; {{c_fds_emb}} fins de semana.

## 7. Sentença → apelação (15 dias, art. 1.003, §5º) — e o efeito dos embargos

{{tab_apel}}

**Vencimento: {{v_apel}} ({{vw_apel}})**, assim distribuídos: {{apel_pre_recesso}} dias úteis antes
da janela suspensa ({{i_sent}} a 18/12/2026), depois {{c_susp_apel}} dias de semana suspensos pelo
art. 220, e os {{apel_restam}} dias restantes retomam em {{retoma}} ({{retoma_w}}).

**Atenção — a data da apelação só vale se não houver embargos.** O acervo diz que "a oposição de
embargos **interrompe** o prazo para a interposição de recurso (art. 1.026)". Interromper não é
suspender: o prazo recomeça do zero, do primeiro dia útil seguinte à intimação da decisão dos
embargos. Como o prazo de embargos vence em {{v_emb}} — já colado na janela suspensa de 20/12 —,
na prática a decisão dos embargos dificilmente seria intimada antes de {{retoma}}, e uma apelação
protelatória com embargos opostos na última hora empurraria o vencimento da apelação para
aproximadamente **{{apel_com_emb_arg}}** (estimativa, ver Seção 10.2). Se a intenção é recorrer,
convém **não** contar com {{v_apel}} sem antes decidir sobre os embargos.

## 8. Fechamento das contas em dias corridos (nenhuma data "ajustada na força")

| Janela (publicação → vencimento) | Corridos | Dia do começo | Computados | Feriados fora da janela do art. 220 | Dias de semana suspensos (art. 220) | Fins de semana |
|---|---|---|---|---|---|---|
| Citação → contestação ({{p_cit}} → {{v_contest}}) | {{c_corr_cit}} | 1 | {{c_uteis_cit}} | {{c_fer_cit}} | {{c_susp_cit}} | {{c_fds_cit}} |
| Sentença → embargos ({{p_sent}} → {{v_emb}}) | {{c_corr_emb}} | 1 | {{c_uteis_emb}} | {{c_fer_emb}} | {{c_susp_emb}} | {{c_fds_emb}} |
| Sentença → apelação ({{p_sent}} → {{v_apel}}) | {{c_corr_apel}} | 1 | {{c_uteis_apel}} | {{c_fer_apel}} | {{c_susp_apel}} | {{c_fds_apel}} |
| Citação → contestação em dobro — **hipótese rejeitada** ({{p_cit}} → {{v_dobro}}) | {{c_corr_dobro}} | 1 | 30 | {{c_fer_dobro}} | {{c_susp_dobro}} | {{c_fds_dobro}} |

Dias não computados, um a um: {{det_cit}} (contestação); {{det_emb}} (embargos); na apelação, os
{{c_susp_apel}} dias de semana suspensos estão todos dentro de {{rec_inicio}}–{{rec_fim}} — nos dias
{{rec_motivos}} a razão é dupla (a tabela da biblioteca já os marca como feriado/"sem expediente
forense" **e** eles estão dentro do art. 220), mas cada dia é contado uma só vez.

## 9. Calendário usado (transcrito de `library/calendario_forense_campinas.md`) e a janela do art. 220

{{tab_calendario}}

{{tab_recesso}}

Armadilhas de calendário que apareceram (ou puderiam aparecer) neste caso:

- **20/11/2026** (feriado nacional) — empurrou a publicação da citação de 20/11 para {{p_cit}};
- **08/12/2026** — feriado municipal **de Campinas** dentro do prazo de contestação (adiou
  {{v_contest}} em um dia);
- **24/12/2026 e 31/12/2026** — "sem expediente forense" na tabela e, além disso, dentro do
  art. 220: dupla razão para não computar;
- **25/01/2027** — a tabela registra "Aniversário de São Paulo — feriado municipal **APENAS na
  Capital** (não em Campinas)": em Campinas seria dia útil, mas cai dentro da janela suspensa do
  art. 220 e não é computado por isso;
- **08/02 e 09/02/2027 (Carnaval)** — caem **depois** de {{v_apel}}, o vencimento mais tarde
  adotado: não afetam nada. Só entrariam na conta se o prazo fosse em dobro ({{v_dobro}}), hipótese
  rejeitada; e a tabela da biblioteca termina em 09/02/2027, de modo que prazos posteriores exigiriam
  calendário novo;
- **18/07/2026, 11/08/2026 e 07/12/2026** — **não** estão na tabela (feriado estadual de 9 de Julho
  em 09/07 está; os outros dois, não). Não foram computados como feriados porque o acervo não os
  registra; se o foro de Campinas tiver feriados locais fora da tabela, é dado que falta (Seção 10.3).

## 10. Premissas, leituras divergentes e o que o acervo não permite verificar

### 10.1 Duas leituras do "primeiro dia útil seguinte" — a que adotamos

| Prazo | **Adotada** (dia 1 = 1º dia útil após a publicação — art. 224, §3º, e Lei 11.419, art. 4º, §4º, lidos literalmente) | Controle: também se exclui esse 1º dia útil |
|---|---|---|
| Contestação | **{{v_contest}}** | {{v_contest_B}} |
| Contestação em dobro (hipótese) | {{v_dobro}} | {{v_dobro_B}} |
| Embargos | **{{v_emb}}** | {{v_emb_B}} |
| Apelação | **{{v_apel}}** | {{v_apel_B}} |

A coluna da direita desloca cada prazo de um dia útil e, no caso dos embargos, faz o próprio prazo
de 5 dias correr quase inteiro dentro da janela suspensa ({{p_sent}} → {{v_emb_B}}). Adotamos a
coluna da esquerda porque (i) é a leitura direta do §3º do art. 224 e do §4º do art. 4º da
Lei 11.419 — a contagem "terá início no primeiro dia útil que seguir ao da publicação"; (ii) evita
excluir duas vezes o mesmo dia; e (iii) é a mais antiga para a parte (prazos vencem antes). Se o
escritório preferir a margem da segunda leitura, o vencimento alternativo está na tabela — mas
**agendar pela data mais antiga** é o que protege contra preclusão.

### 10.2 Premissas (fatos que não estão nos documentos)

1. **Data de publicação não impressa.** Adotou‑se a regra legal (Lei 11.419, art. 4º, §3º) sobre a
   disponibilização informada: {{p_cit}} e {{p_sent}}. Se a consulta ao e‑SAJ mostrar data de
   publicação diferente, é só religar o cálculo a ela (a rotina está parametrizada em
   `calculo_prazos.py`).
2. **Não há, nos documentos, certidão de citação (AR/mandado) com data.** O despacho determina a
   citação "na pessoa de seu advogado constituído", e o acervo transcreve do art. 231 **apenas o
   inciso VII** (intimação pelo DJE), que é o que usamos via art. 335, III. Se nos autos houver AR
   ou certidão com data própria, o inciso aplicável pode ser outro — e o acervo não permite
   verificar. Não se tentou "reconciliar" nada: a premissa está declarada.
3. **A data de intimação da decisão dos embargos (se opostos) ainda não existe**, por isso não há
   como calcular o vencimento da apelação nesse cenário — {{apel_com_emb_arg}} é apenas uma
   ordem de grandeza (15 dias úteis a partir de {{retoma}}), não um cálculo de fato.
4. **Nada nos autos indica gratuidade de justiça, prazo em horas, ou procedimento da Lei 9.099/1995**
   (que o art. 220, no texto do acervo, não menciona; a suspensão do art. 220 foi aplicada como
   escrita). O texto do acervo para o art. 220 não tem parágrafos, e nada aqui depende de parágrafo.

### 10.3 Limites do acervo

- Só há calendário de Campinas de **01/01/2026 a 09/02/2027**. Todos os vencimentos adotados estão
  dentro dessa faixa; qualquer prazo depois de 09/02/2027 (por exemplo, apelação após embargos, ou
  contrarrazões) exige calendário novo.
- O acervo **não** traz os arts. 231 (demais incisos), 240 e 1.026; por isso não se verificaram aqui
  termos de citação por correio/mandado nem os efeitos细 da extemporaneidade dos embargos.
- Não há jurisprudência no acervo; as questões de leitura acima foram resolvidas com o texto legal.

## 11. Resumo para colocar no calendário

{{tab_resumo}}

Em uma frase: **contestação {{v_contest}}**, **embargos {{v_emb}}**, **apelação {{v_apel}}** (esta só
se não houver embargos), tudo em **prazo simples**, porque os autos são eletrônicos e o art. 229,
§2º, exclui o dobro nesse caso. Se os autos fossem físicos, a contestação iria até {{v_dobro}} —
{{ganho_dias_corr}} dias corridos a mais —, o que mostra por que a pergunta do sócio precisava ser
respondida antes de fechar a agenda.

---

*Contagem reproduzível: `workspace/calculo_prazos.py` lê a tabela de feriados e a janela de recesso
direto de `library/calendario_forense_campinas.md` (nenhuma data de calendário é digitada à mão) e
`conferir()` falha se alguma soma não fechar. As datas e tabelas desta memória são geradas por
`workspace/gera_entrega.py` a partir do mesmo módulo, de modo que o texto, o `prazos.json` e o script
não podem divergir.*
