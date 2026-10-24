# QUESTIONS.md — Incógnitas sinalizadas (não são perguntas a reenviar)

**Resposta do cliente (24/10/2026):** *"For questions not answered above, the client has no
additional information. Flag remaining unknowns explicitly."* As cinco perguntas abaixo foram
devolvidas **sem resposta factual**. Elas **não serão repetidas**; convertem‑se em **incógnitas
sinalizadas explicitamente (U1–U5)**, com a direção do impacto sobre os prazos calculados.
Espelho detalhado em `memoria.md` § 9.1.

---

## U1 — Data efetiva da citação (certidão / AR)
- **Pergunta original:** haveria certidão ou AR de citação nos autos com data diversa da intimação de fls. 88?
- **Resposta do cliente:** não dispõe da informação.
- **O que foi usado:** intimação da citação na pessoa do advogado (despacho de fls. 88, DJE com
  disponibilização em 19/11/2026) como marco do art. 231, VII — único inciso de art. 231 na biblioteca.
- **Impacto se mudar:** certidão com data **posterior** empurra o vencimento da contestação
  (15/12/2026) para mais tarde; data **anterior** o antecipa. **15/12/2026 mantém‑se como data de
  trabalho segura** para planejamento (o risco de revelia está do lado mais cedo).
- **Ação possível futura:** ao juntar certidão de citação aos autos, recalcular a trilha da citação.

## U2 — Datas de publicação nas telas do e‑SAJ
- **Pergunta original:** exportar as telas de publicação do e‑SAJ das duas intimações.
- **Resposta do cliente:** não dispõe da informação.
- **O que foi usado:** cadeia legal — publicação = primeiro dia útil seguinte à disponibilização
  (art. 4º, §§ 3º–4º, Lei 11.419/2006 + art. 224, §§ 2º–3º, CPC): **23/11/2026** e **11/12/2026**.
- **Impacto se mudar:** publicação em dia útil diverso da cadeia desloca **todos** os vencimentos em
  ± 1 dia útil. Mitigante: o próprio PDF invoca o art. 4º, § 3º, da Lei 11.419/2006, ou seja, a cadeia
  adotada é a declarada na própria intimação.

## U3 — Oposição de embargos de declaração até 18/12/2026
- **Pergunta original:** a estratégia inclui opor embargos?
- **Resposta do cliente:** não dispõe da informação (decisão de estratégia pendente).
- **O que foi usado:** apelação em **03/02/2027**, válida **apenas se nenhum embargo tempestivo for oposto**.
- **Impacto se mudar:** embargos tempestivos ⇒ os 15 dias da apelação **recomeçam do zero** após a
  intimação do julgamento (arts. 1.023/1.026, conforme a biblioteca). **Fronteira inferior teórica:**
  intimação do julgamento disponibilizada em 19/12/2026 → publicação 21/01/2027 → dia 1 em 22/01/2027 →
  apelação vence **15/02/2027 (seg)**; julgamento posterior ⇒ prazo posterior. Na fronteira, 4 dias
  úteis da contagem (10, 11, 12 e 15/02/2027) estariam **fora da vigência da tabela de calendário**
  da biblioteca, e o marco inicial do art. 231 para essa intimação **não está na biblioteca**
  (só o inc. VII) — premissas rotuladas em `memoria.md` §§ 6.3 e 9.1.

## U4 — Calendário forense após 09/02/2027
- **Pergunta original:** haveria novo extrato de calendário após 09/02/2027?
- **Resposta do cliente:** não dispõe da informação.
- **O que foi usado:** tabela da biblioteca (vigência até 09/02/2027). **Todos os vencimentos adotados
  caem dentro da vigência**: contestação 15/12/2026, embargos 18/12/2026, apelação 03/02/2027
  (hipótese rejeitada do prazo em dobro: 05/02/2027).
- **Impacto se mudar:** só é relevante se U3 se materializar (fronteira 15/02/2027 exige calendário
  além da tabela). Sem novos dados, nenhuma data adotada fica descoberta.

## U5 — Feriados locais fora da tabela
- **Pergunta original:** haveria feriados municipais/estaduais não listados (ex.: 18/07, 11/08, 07/12/2026)?
- **Resposta do cliente:** não dispõe da informação.
- **O que foi usado:** apenas os feriados listados na tabela da biblioteca.
- **Impacto se mudar:** **possível impacto apenas em 07/12/2026**, que é **segunda‑feira** e está dentro da
  contagem da contestação (10º dia computado). Se fosse feriado local não listado, o vencimento seria
  empurrado para **16/12/2026 (quarta‑feira)** — sentido favorável: a data de trabalho adotada
  (15/12/2026) continuaria tempestiva. 18/07 e 11/08/2026 são anteriores a todas as contagens — sem impacto.

---

Nenhuma data adotada em `prazos.json` depende de resposta pendente: U1–U5 alteram apenas cenários e
controles, e estão todas sinalizadas acima, em `memoria.md` § 9.1 e no fundamento do `citacao` em `prazos.json`.
