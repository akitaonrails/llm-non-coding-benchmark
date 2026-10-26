# STATUS — Execução Fiscal 5001234-56.2026.4.03.6182

**Sessão 3: COMPLETE** (análise do redirecionamento) — **Sessão 2: COMPLETE WITH OPEN ITEMS** (R3 do cliente processada; Q6 encerrada sem resposta → convertida em desconhecido **U6**)

## Entregues (sessão 3)
- `deliverable/sessao3/analise_redirecionamento.json` — 7 chaves do contrato + evidências/contagens/premissas; JSON validado. Síntese:
  - **Pedido**: União quer redirecionar contra a ex-sócia **Ana Paula Vieira** (Súmula 435 + CTN 135 III), usando só a certidão negativa do oficial (28/09/2026).
  - **Súmula 435 não se forma**: exige "deixar de funcionar no domicílio **sem comunicação aos órgãos competentes**"; a mudança foi registrada na JUCESP em 12/03/2026 e na RFB em 20/03/2026 — **200/192 dias antes** da diligência. A biblioteca tem nota expressa de afastamento da presunção. (Fato desfavorável antecipado: saída fática "desde o começo do ano", ~70 dias antes da comunicação.)
  - **Tema 962** barra Ana Paula em qualquer cenário: retirada regular em 15/06/2023 (JUCESP 22/06/2023; 957 dias antes da AIF), sem causa da dissolução de 2026.
  - **Tema 981** desautoriza o critério da Fazenda ("administradora à época dos FGs"): o marco é a data da dissolução → único nome possível seria **Bruno Tavares** (administrador único desde 15/06/2023).
  - **dissolucao_irregular_configurada = false**; sócio que responderia se configurada = Bruno, jamais Ana Paula.
  - Decadência preservada: o redirecionamento só alcançaria o remanescente **R$ 591.000**; os **R$ 509.000** decaídos não se estendem a sócio algum (Súmula 393).

## Entregues (sessão 2)
- `deliverable/sessao2/manifestacao.md` — réplica à manifestação da Fazenda:
  - **Emenda/substituição da CDA**: aceita como correção apenas formal do fundamento da multa (LEF art. 2º §8º; Súmula 392), com três limites — não reaviva crédito extinto por decadência, **vedada modificação do sujeito passivo** (Súmula 392 in fine), devolução do prazo de embargos.
  - **Rejeição da tese "173 I para todos"**: o critério é declaração/pagamento (Súmula 555: "quando não houver declaração do débito"; Tema 163: pagamento parcial → art. 150 §4º). 4T/2020 e 1T/2021 tiveram DARFs (61 mil / 84 mil) → §4º; 3T/2020 e 2T/2021 sem pagamento → 173 I.
  - **Armadilha demonstrada**: pela régua da própria Fazenda (vencimento → exercício seguinte), o **3T/2020 fica decaído** (lim. 31/12/2025) — a Fazenda nem indicou limite para esse período. E o **4T/2020 está decaído sob TODAS as leituras** (FG trimestral = FG anual = 31/12/2020 no 4T) → mínimo decaído **R$ 241.000**; tese correta **R$ 509.000** (3T + 4T/2020), remanescente R$ 591.000.
  - **Fraude não comprovada**: CDA substitutiva reafirma multa de 75% (art. 44 I), não 150% (§1º) → exceção final do §4º indisponível à Fazenda.
  - Pedidos: juntada da **íntegra da CDA substitutiva** (anunciada mas ausente dos autos) + memória de cálculo do AIF; consignação de que o sujeito passivo não mudou; reserva de embargos.

## Aberto (sessão 2)
- **U6 — CDA substitutiva não está nos autos**: cliente respondeu que **não tem informação adicional** (R3); Q6 encerrada, não será repetida. Único teor conhecido: a linha da multa ("75% — Lei 9.430/96, art. 44, I"). Única via: **juntada requerida nos autos** (manifestação, item V "d"); ao chegar, conferir sujeito passivo (Súmula 392 veda modificação), valores, períodos e datas de inscrição.
- Desconhecidos U1–U5 (sessão 1) permanecem como premissas sinalizadas; U2 ganha reforço probatório: a própria CDA substitutiva, ao reafirmar 44 I (75%), documenta que o Fisco **não** caracterizou fraude.

## Instrução do cliente recebida e processada (26/10)
- Bruno: "a CDA estava errada, tem que anular tudo, a Fazenda não pode consertar depois" → **não acatada literalmente** (contraria LEF art. 2º §8º e Súmula 392 — correção é expressamente permitida até a sentença de embargos); orientado e registrado em `deliverable/NOTA_AO_CLIENTE_CDA.md` (o argumento do erro continua nos autos e será aprofundado nos embargos; risco antecipado: "anular tudo" poderia reabrir lançamento do 2T/2021 até 31/12/2026 com multa 150%).

## Preparação (não entregável)
- `deliverable/PREPARATORIO_SESSOES3_4.md` — linha do tempo com contagens conferidas (retirada→AIF: 957 dias; comunicação JUCESP/RFB→diligência: 200/192 dias antes), enquadramento Súmulas 435/430 + Temas 962/981, fato desfavorável antecipado (saída fática "desde o começo do ano" ~70 dias antes da comunicação) e rascunho do gabarito JSON. Será convertido nos entregáveis S3–4 quando a petição de redirecionamento existir nos autos.

## Entregues (sessão 1 — mantidos)
- `sessao1/analise.json` (decaído R$ 509.000 / remanescente R$ 591.000; premissas + desconhecidos U1–**U6**, atualizado nesta rodada) e `sessao1/peca.md` (exceção de pré-executividade + pedido de junta do PAF).
- `QUESTIONS.md` — registro encerrado: Q1–Q6 todas respondidas ou encerradas "sem informação" (R1–R3); **nenhuma será repetida**.

## Pendentes do roteiro (dependem dos atos processuais scriptados)
- **Sessão 4** (`defesa_redirecionamento.md` + `carta_aos_socios.md`): material pronto no preparatório + análise da S3; redigir quando a sessão for aberta (peça enfrenta o pedido de 26/10; carta precisa tratar o alerta Tema 981 — se a dissolução se configurasse, o alvo seria Bruno, mas a mesma prova das comunicações JUCESP/RFB protege os dois).
- **Sessão 5** (`garantia.json`): aguarda a fase de garantia.
