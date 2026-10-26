Cliente respondeu. Vou: (1) incorporar as novas informações aos deliverables da Sessão 1 (resposta ao diretor sobre o "sinal" e o risco do Beta), (2) avançar para as Sessões 2 e 3, que não dependem de mais informação do cliente. Primeiro, os cálculos:

Cálculos conferem. Agora o adendo à resposta do diretor com as novas informações (Norte/Beta):

Agora a Sessão 2 — análise cláusula a cláusula do plano e o efeito tributário do deságio:

Agora a Sessão 3 — lançamentos contábeis da novação e a solução do passivo fiscal:

Engajamento concluído (Sessões 1–3), com as respostas do cliente incorporadas. Validação final: JSONs válidos, todos os lançamentos da novação batem (D = C), e as citações conferem com a biblioteca (arts. 64 e 172 constam do próprio texto de `lei11101_excertos.md`; arts. 50 e 83 sinalizados como ausentes, não citados como fundamento).

## O que mudou com as respostas do cliente

**Sessão 1 atualizada** — adendo em `deliverable/sessao1/resposta_diretor.md`:
- **"Sinal" ao Norte: negado, mesmo parcial.** O art. 172 (favorecimento) não tem piso de valor — R$ 310 mil "de sinal" sobre dívida concursal de R$ 1,85 mi é o mesmo ilícito do pagamento total. O "sinal" legal é outro: quitar os R$ 310 mil da entrega pós-pedido (art. 67) e tratar o Norte como **compra à vista**, pois todo fornecimento novo vira crédito pós-pedido pagável integralmente — a melhor posição possível dentro da RJ. A ameaça de parar não vence a suspensão (eles também não podem executar por 180 dias).
- **Beta é o risco existencial, não o Norte**: as máquinas são a linha de separação → protegidas contra retirada durante a suspensão (art. 49 §3º in fine), mas o Beta **não está no plano** (cláusula de deságio 40% é ineficaz) e pode retomar as máquinas após 180 dias (prorrogáveis). Diferença jurídica chave: pagar/renegociar com o Beta **é lícito** (extraconcursal). Proposta: usar o galpão (R$ 4,5 mi) para quitar o Beta (R$ 3,1 mi) — sobram R$ 1,4 mi — dentro da janela de suspensão.

**Sessão 2** (`sessao2/`): `analise_plano.md` — 5 cláusulas: **ilegais** a do fiduciário e a da União (CTN 187, art. 68; "180 parcelas" sequer existe — teto é 120); **condicionalmente ilegal** a trabalhista de 18 meses (art. 54: 1 ano, só 2 com garantia + aprovação da classe); **legais** a de quiro/ME-EPP e a fonte do galpão (com destinação ao Beta). `efeito_tributario_desagio.json` — ganho eficaz **3.882.000** (60% × 6.470.000; ganhos fictícios do fiduciário 1.240.000 e da União 1.350.000 ficaram fora), PIS/COFINS = 0, **trava de 30% não aplicável** (art. 50-A II), IRPJ/CSLL 1.317.880 com alíquotas rotuladas como não verificadas.

**Sessão 3** (`sessao3/`): `lancamentos_novacao.json` — CPC 48: baixa de 6.470.000, novo passivo 2.588.000 (PV aproximado pelo nominal — premissa), ganho 3.882.000 no resultado; Beta e União sem novação. `passivo_fiscal_solucao.md` — adesão imediata à Opção A (120×, R$ 22.500/mês) para obter CPEN e destravar a concessão (art. 57/CTN 191-A), transação em paralelo (até 70% off → R$ 6.750/mês), e o trade-off do prejuízo fiscal entre o parcelamento (Opção B) e o abate do ganho do deságio.

**Desconhecidos sinalizados** (cliente não tem os dados — viraram premissas, não perguntas repetidas): data do protocolo, semanas 5–13 do fluxo, situação dos R$ 310 mil, valor contábil do galpão, estoque de prejuízo fiscal, partes ligadas (risco art. 50-A p.ú.), ICMS/ISS. `STATUS.md`: **COMPLETE WITH OPEN ITEMS** com os 8 itens abertos listados.