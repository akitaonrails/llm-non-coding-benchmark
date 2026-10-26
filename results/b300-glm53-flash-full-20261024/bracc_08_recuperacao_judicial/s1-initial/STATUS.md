# STATUS.md — engajamento Atlas Distribuidora S.A. (RJ)

**Status geral: COMPLETE WITH OPEN ITEMS**
Sessão 1: **COMPLETE** (atualizada com os fatos novos da diretoria) · Sessão 2: **COMPLETE WITH OPEN ITEMS** · Sessão 3: **BLOQUEADA** — aguardando as respostas aos itens 11–14 de `QUESTIONS.md`.

---

## Sessão 1 — mês do pedido (entregável: `deliverable/sessao1/`)

- [x] `resposta_diretor.md` — (i) pagamento "por fora" do Norte **vetado** (art. 49; par condicio; arts. 172 e 64; risco de convolação) + alternativa: fornecimentos novos à vista (art. 67), política **confirmada pela diretoria**; (ii) trava de 30% **não atinge o ganho** (art. 50-A, I e II); (iii) União **fora do plano** (CTN 187; art. 68) — vias da Lei 10.522. **Adendo (§5):** veto ao "sinal" do Norte **para qualquer valor**; essencialidade das máquinas do Beta confirmada → art. 49, §3º por inteiro.
- [x] `classificacao_creditos.json` — 7 créditos, R$ 13.540.000. Totais: concursais 7.430.000 (trab 960.000; quiro/ME-EPP 6.470.000); não sujeitos/extraconcursais 6.110.000 (Beta 3.100.000; União 2.700.000; pós-pedido 310.000).
- [x] `demonstrativo_mensal_aj.md` — mês 1 ao AJ: caixa conferido (4 semanas, saldo final 840.000 ✓); obrigações pós-pedido; concursais (União excluída de ofício); UPI; notas atualizadas com as respostas da diretoria (essencialidade confirmada; "à vista" confirmado; cláusula fiduciária condenada na Sessão 2).

## Sessão 2 — cláusulas do plano + efeito tributário do deságio (`deliverable/sessao2/`)

- [x] `analise_plano.md` — veredicto por cláusula: **#1 trabalhistas 18m = CONDICIONAL** (art. 54 caput = 1 ano; §2º exige garantias + aprovação da classe — NÃO VERIFICADO; recomendação: ≤ 12m); **#2 deságio 60% classes III/IV = não impugnado pela biblioteca** (sujeição via art. 49; sem teto de deságio no texto; votação NÃO VERIFICADA); **#3 fiduciários sujeitos ao plano = ILEGAL** (art. 49, §3º — propriedade prevalece; comercial, fora do plano); **#4 União no plano = ILEGAL em dobro** (CTN 187 + art. 68; 180× não existe na Lei 10.522 — regimes: 120×; 30%+84×; transação ≤ 70%/120m); **#5 UPI galpão = legal com ressalva** (art. 6º-B protege só alienação **judicial** — recomendação de venda judicial). Omissões da minuta listadas; ponte para a novação (Sessão 3) traçada.
- [x] `efeito_tributario_desagio.json` — **ganho nominal 3.882.000** (2.520.000 Alfa + 1.110.000 Norte + 252.000 Sul; verificado em Python); **PIS/COFINS = 0** (art. 50-A, I); **trava de 30% não aplica ao ganho** (art. 50-A, II); **IRPJ/CSLL = NAO_CALCULAVEL** (alíquotas não constam da biblioteca — NÃO VERIFICADO; base mínima nominal 3.882.000); **compensação = null** (prejuízo fiscal não informado) com fórmula condicional documentada (limite = 30% × lucro excluído do ganho — interpretação rotulada do art. 50-A, II); dedutibilidade das despesas do plano (art. 50-A, III); ressalva de pessoas ligadas (p.ú.).

## Itens em aberto

**Dados sem resposta (cliente declarou não haver mais informações — tratados como assunção/não verificado, nunca re-perguntados):** 1 data do pedido (adotado mês do pedido = março/2026) · 2 semanas 5–13 + início da semana 1 · 3 prejuízo fiscal/lucro real/regime · 4 entrega Norte 20/03 (R$ 310.000) · 5 composição dos pagamentos semanais · 6 encargos/juros/taxas · 7 pessoas ligadas · 8 galpão (valor contábil/garantias) · 10 garantias reforçadas/adesões informais.

**Decisões pendentes para a Sessão 3 (QUESTIONS.md 11–14):** 11 via fiscal da União (120× / 30%+84× / transação ≤ 70%) · 12 alienação do galpão judicial? (art. 6º-B) · 13 taxa de desconto (sem resposta → nominal) · 14 data/termos da homologação (base dos lançamentos).

## Próximos passos (Sessão 3 — liberada após as respostas 11–14)

1. `lancamentos_novacao.json` — baixa do passivo sujeito (7.430.000, exceto União/Beta), novo passivo a valor justo (PV das parcelas), ganho na rubrica própria ("receita de renegociação de dívidas em RJ"); nominal se item 13 sem resposta.
2. `passivo_fiscal_solucao.md` — qualificação da via escolhida (item 11): cronograma, certidão positiva com efeito de negativa (art. 57), custo × folga da UPI (952.000 → 142.000 na transação de 70%).

*Autoridade citável: somente `library/INDEX.md`. Nada fora dela é citado; lacunas marcadas NÃO VERIFICADO/assunção.*
