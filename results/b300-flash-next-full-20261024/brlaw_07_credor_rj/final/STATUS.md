# STATUS DO ENGAGEMENT — Fornecedor Sul S.A. × Atlas Distribuidora S.A.
**20/04/2026 — atualizado após a rodada 3 de mensagens do cliente**

## STATUS: COMPLETE WITH OPEN ITEMS

> **⚠ ALERTA OPERACIONAL IMEDIATO (rodada 3):** o Sr. Edson anuncia envio de caminhão para retirar as empilhadeiras e o sistema de separação do galpão da Atlas. Retirada é **vedada durante o stay** (art. 49, §3º; art. 6º, §§4º e 7º-A; STJ Tema 1.051) e seria revertida pelo juízo da RJ. Carta URGENTE emitida (`resposta_cliente_3.md`); risco registrado em `estrategia.json → acoes_imediatas`. Nenhum item do cronograma de protocolo (27/04) muda — mas este risco é a prioridade zero das próximas 48h.

Entregáveis em `deliverable/`:

| # | Arquivo | Conteúdo | Situação |
|---|---|---|---|
| 1 | `estrategia.json` | Estratégia estruturada (schema do contrato + chaves extras: atualizações das rodadas 2 e 3 e `desconhecidos_restantes`) | OK — JSON validado; todos os campos exigidos presentes |
| 2 | `habilitacao_divergencia.md` | Divergência c/c habilitação ao AJ (art. 7º §1º; conteúdo do art. 9º) | OK — essencialidade confirmada incorporada ao §V; §VIII reescrito: lacunas correm por autos/registros públicos, sem nova pergunta ao cliente; placeholders factuais permanecem marcados |
| 3 | `resposta_cliente.md` + `resposta_cliente_2.md` + `resposta_cliente_3.md` | Resposta em linguagem simples às 3 perguntas do e-mail (v1) + follow-up às respostas do cliente, com condutas diante da notificação do Banco Horizonte (v2) + **carta URGENTE** contra a retirada iminente dos bens (v3, rodada 3) | OK |
| 4 | `QUESTIONS.md` | Rodada 2: registro do que foi respondido + desconhecidos remanescentes com via de obtenção **sem o cliente** (o cliente declarou não ter mais informação; nenhuma pergunta foi repetida) | OK |

## Conclusões centrais (inalteradas; premissas agora confirmadas)
- **Prazo: 27/04/2026 (segunda)** — 15 dias corridos do edital de 10/04/2026 (arts. 7º §1º; 189, §1º, I); 15º dia em sábado 25/04 → 1º dia útil seguinte (CPC 224 §1º via art. 189 caput, conforme a própria biblioteca).
- **Crédito correto: R$ 2.100.000,00** = R$ 900.000,00 fiduciários, NÃO sujeitos ao plano (art. 49 §3º), com retomada dos bens **vedada durante o stay** (art. 6º §§4º/7º-A; Tema 1.051) — **essencialidade agora confirmada pelo cliente** ("sem isso a Atlas para") + R$ 1.200.000,00 quirografários em **classe IV** (EPP confirmada — art. 41, IV), não classe III.
- **Divergência: R$ 1,6 mi listado × R$ 2,1 mi correto** (−R$ 500 mil); a composição dos R$ 1,6 mi segue **expressamente não reconciliada** (peça, item "d" do pedido).
- **Fiança do sócio NÃO extinta pela homologação** — CONFIRMADO que o Banco Horizonte não anuiu e **já notificou o fiador**: fiança viva e em exigência (Súmula 581; arts. 49 §1º e 59; Tema 885: só vincula quem aprovou). Advertência nova: se o **banco** aprovar expressamente o plano com a cláusula, aí sim cairia — condutas de blindagem emitidas em `resposta_cliente_2.md` (não assinar, não anuir, responder à notificação, negociar direto com o banco).
- **Voto: classe IV, maioria simples por cabeça (art. 45)**, só com a parcela sujeita ao plano; tempestividade preserva o voto (art. 10 §1º).
- **Objeção ao plano: 30 dias da publicação da relação do AJ (art. 55)** — termo inicial ainda não ocorrido.

## Itens abertos (open items) — nenhum bloqueia o protocolo até 27/04
1. **[PRIORIDADE ZERO] Tentativa iminente de retirada dos bens (caminhão anunciado pelo cliente, rodada 3)** → carta URGENTE emitida (`resposta_cliente_3.md`); bloquear a retirada, monitorar o galpão e, se a Atlas alienar/deteriorar os bens, comunicar o juízo da RJ no ato (art. 6º, §7º-A).
2. **Data do pedido da RJ / do deferimento do processamento** (atualização art. 9º, II; cômputo do stay). Cliente não sabe → obter do inteiro teor do edital/autos; peça já preparada para sair com valores nominais + ressalva (peça, §VIII).
3. **Número dos autos, qualificação registral, docs do art. 9º III** (contrato, duplicatas/NFs, certidão do registro da fiduciária, nº de série dos bens) → autos/cartórios; complementação no mesmo expediente administrativo.
4. **Composição dos R$ 1,6 mi listados** — não reconcilia com os títulos (1,2 mi / 900 mil / 2,1 mi); deixada aberta de forma visível na peça e no JSON; esclarecer pela relação do art. 51 nos autos.
5. **Conteúdo/prazo da notificação do Banco Horizonte** e estado da CCB/execuções contra o fiador → cliente orientado a apenas **enviar a notificação** (peça de trabalho, não pergunta).
6. **Publicação da relação do AJ** → monitoramento; dela correm impugnação (10 dias, art. 8º) e objeção (30 dias, art. 55).
7. **Preferência estratégica final** do cliente (classe IV vs. dação vs. execução pós-stay) → colhida na resposta v2; decisão pode aguardar a relação do AJ.
8. **Premissas declaradas** (QUESTIONS, §C): stay em curso em 20/04 (conservador); EPP × Lucro Presumido — regra da LC 123/2006 **não verificada** na biblioteca (não invocada como fundamento); regresso do fiador que pagar sujeita-se à RJ — **não verificado** na biblioteca, tratado como premissa.

## Nota de conformidade
Citações exclusivamente em arquivos de `library/INDEX.md`. As duas proposições fora da biblioteca usadas apenas como premissas de trabalho estão rotuladas como não verificadas (acima, item 8, e nos textos). Nenhum fato foi inventado: os novos fatos das rodadas 2 e 3 vêm das mensagens do cliente (essencialidade, EPP/Lucro Presumido, não anuência + notificação do banco; anúncio da retirada dos bens) e foram incorporados com a fonte indicada. **Auditoria pré-entrega concluída em 20/04:** releitura integral dos 5 arquivos da biblioteca e dos 7 entregáveis; datas/dias-da-semana e todas as somas reconfirmadas; seis defeitos corrigidos (citação do art. 189 §1º, I em 4 arquivos; texto integral da Súmula 581; remoção de vínculo indevido com art. 10 §1º em `estrategia.json`; início do stay e subordinação de retardatários rebaixados a premissa/predição nas cartas; tese LC 123 reformulada como premissa na carta v2; previsões de efeito hedgadas na carta v3).
