# STATUS.md — status do engajamento

**Data:** 26/10/2026 (atualizado com as respostas do cliente recebidas hoje)
**Status: `COMPLETE WITH OPEN ITEMS`**

Todos os entregáveis obrigatórios estão escritos e no lugar. As posições de fundo (o que atacar na
minuta e por quê) estão completas, cada uma ancorada em arquivo da `library/INDEX.md` ou em fato do
data room. O cliente respondeu duas matérias (IRPJ e Horizonte Azul) e informou que **não há
informação adicional** para as demais — por isso os valores continuam nos documentos como símbolos
com fórmulas expostas, e não como números.

## Respostas recebidas (26/10/2026) — já incorporadas aos entregáveis

1. **IRPJ 2023 — pergunta 7 respondida.** Débito em cobrança, ~R$ 310.000 (data room §3.1), **sem
   parcelamento**, porque os sócios discordam do lançamento. Consequência adotada: sem
   regularização por recolhimento/parcelamento antes do fechamento, a certidão federal segue
   **positiva no Fechamento**; tratamento por anexo de exceções + escrow dedicado de R$ 310.000 +
   encargos, com prazo próprio (redline 5.9, 8.4(b), 10.2). Dois desfechos possíveis e ambos
   cobertos: discussão ganha → reserva liberada; discussão perdida → reserva consome o saldo.
2. **Horizonte Azul — pergunta 2 sem número, mas com fato novo material.** Maior cliente (31% da
   receita); o diretor é amigo de Hélio, o jurídico é "duro"; **a venda ainda não foi comunicada e
   nenhum pedido de anuência foi feito**. Consequência adotada: pedido **formal e por escrito**
   enviado já na assinatura do SPA, com narrativa controlada; o apoio informal do diretor **não
   equivale** à "anuência prévia e expressa" da cláusula 19 (data room §1.1); a multa
   0,20 × S_HA segue no Anexo 3.2 e no escrow itemizado (redline 3.2(i), 10.2).

## Entregáveis

| Arquivo | Status | Observação |
|---|---|---|
| `achados.json` | ✅ pronto (atualizado 26/10) | 14 achados; soluções dos achados de Horizonte Azul, CND e 5.9 revisadas com as respostas; JSON validado com `python3 -m json.tool` |
| `redline.md` | ✅ pronto (atualizado 26/10) | Cláusulas 2.3, 3.2 (Anexo 3.2 + CADE), 5.7, 5.9, 8.4(a)–(d), 9.1 e 10.2; os comentários de Anexo 3.2 e 5.9 agora registram os fatos confirmados pelo cliente |
| `resposta_advogado_comprador.md` | ✅ pronto (atualizado 26/10) | Replicações sobre Anexo 3.2, condição de CADE e 8.4(c) + seção 4 respondendo à segunda carta ("padrão de mercado"; "se está tudo certo, qual o problema?"); nada do quadro interno dos sócios é exposto ao comprador |
| `nota_socios.md` | ✅ pronto (atualizado 26/10) | Itens de IRPJ e Horizonte Azul reescritos com o quadro informado; seção "Podemos só assinar?" responde ao Hélio com a conta do que assinar como está deixa na mesa; decisões requeridas renumeradas |
| `QUESTIONS.md` | ✅ pronto (atualizado 26/10) | Respostas registradas; perguntas respondidas não repetidas; itens abertos listados explicitamente |
| `PERGUNTAS.md` | ✅ pronto | Aponta para `QUESTIONS.md` (autoritativo) e resume os temas; evita duas versões divergentes |
| `STATUS.md` | ✅ presente | Este arquivo |

## Open items (sem informação adicional do cliente; valores como símbolos)

1. **P** — preço total da operação. Destrava: escrow 20% × P, teto 15% × P e a exposição
   "teto = Preço Total" das cláusulas 5.7/5.9. *Afeta:* redline.md, nota_socios.md.
2. **S_HA** — saldo contratual Horizonte Azul. Destrava: multa 0,20 × S_HA (Anexo 3.2 e escrow
   itemizado) e a escolha entre abatimento no preço e reserva dedicada. *Afeta:* achados.json,
   redline.md, nota_socios.md.
3. **CAP_PJ** — salários e tempos de casa dos 11 engenheiros PJ. Destrava: o teto da indenização
   específica. *Afeta:* achados.json, redline.md (8.4(b)/(c)), nota_socios.md.
4. **EBITDA histórico 2023–2025.** Destrava: probabilidade real do gatilho do earn-out
   (EBITDA > R$ 1.100.000) e quanto do teto de R$ 1.500.000 (= 35% × excesso; excesso máximo
   1.500.000 ÷ 0,35 = R$ 4.285.714) está em jogo. *Afeta:* nota_socios.md, redline.md.
5. **Venda da totalidade vs. parcial das quotas.** Destrava: renúncia recíproca à preferência do
   contrato social (data room §4.1) e viabilidade do calendário de 45 dias. *Afeta:* redline.md,
   nota_socios.md.
6. **Território da não concorrência** — municípios/estados além de Sorocaba. Destrava:
   preenchimento do Anexo de Território da cláusula 9.1. *Afeta:* redline.md.
7. **Confirmação de que não há outras cláusulas de mudança de controle** (pergunta 8 sem
   resposta). O data room §1.3 segue como única fonte; o Anexo 3.2 parte da lista atual até
   confirmação contrária. *Afeta:* redline.md, resposta_advogado_comprador.md.

## Observações de conformidade

- Citações: todo apontamento remete a arquivo listado em `library/INDEX.md` ou a fato do data
  room. O que não está na library está explicitamente rotulado **"não verificado"** nos
  entregáveis (ex.: estrutura de cálculo das verbas dos PJs; alternativa de exclusão por
  conhecimento documentado em 8.4(c)).
- Números: aritmética exposta nos entregáveis; nada foi forçado a fechar. Os valores falados
  pelo cliente ("uns 310 mil") coincidem com o número registrado no data room (R$ 310.000),
  que foi o adotado.
- Fatos ausentes: nenhum fato foi inventado; o que não existe nos documentos aparece como
  símbolo com fórmula, não como valor.

## Próximos passos

1. **Decisão dos sócios (nota_socios.md, item final):** autorizar o pedido formal de anuência à
   Horizonte Azul (envio na assinatura do SPA) e a comunicação prévia ao Município de Sorocaba,
   com a substituição do responsável técnico no CREA.
2. **Quando P e S_HA existirem:** dimensionar, com aritmética exposta, a escolha entre abatimento
   no preço (≈ 0,20 × S_HA) e reserva dedicada no escrow itemizado.
3. **Quando houver dados dos PJs:** apurar CAP_PJ (equivalência salarial + verbas + encargos por
   tempo de casa — estrutura não verificada na biblioteca, rotulada como tal).
4. **Quando houver EBITDA histórico:** avaliar a probabilidade do gatilho de R$ 1.100.000 e o
   quanto do teto de R$ 1.500.000 está materialmente em disputa.
