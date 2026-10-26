A Sessão 3 sairá com os itens 11–14 sem resposta (cliente disse não haver mais dados) — lacunas rotuladas como assunção, nunca re-perguntadas. Antes de escrever os dois entregáveis, vou reconferir os textos citáveis que sustentam essa sessão:

Textos conferidos. Falta só a base contábil (CPC) para alinhar os rótulos dos lançamentos:

Base contábil conferida. Agora a aritmética completa da Sessão 3 (plano, novação e as três rotas da União), com asserções:

Aritmética fecha com asserções — e traz um ponto novo: na rota B os 30% são liquidados **com prejuízo fiscal** (sem desembolso), o que muda a matriz de caixa. Escrevendo os dois entregáveis:

Três toxinas de rascunho que notei ao reler — corrigindo e validando o JSON na sequência:

O JSON validou (`JSON VÁLIDO ✓`), e o único "hit" do sweep é texto legítimo da Sessão 2 no STATUS.md ("propriedade prevalece; comercial" — ponto-e-vírgula prosódico), não toxina: os arquivo novos saíram limpos. Agora os dois fechamentos — lendo os arquivos atuais para editar com precisão:

Ambos os arquivos na mão. Quatro edições em paralelo (três no STATUS.md, uma no QUESTIONS.md):

Quatro edições aplicadas. Validação final — releitura do STATUS.md e sweep anti-rascunho na pasta de entregáveis:

Engajamento encerrado — sweep clean (os "hits" restantes são falsos positivos: "todo mundo" em português e o "xxx" de processo anonimizado da Sessão 1). STATUS.md e QUESTIONS.md atualizados e coerentes. Segue o relatório da Sessão 3:

---

# Sessão 3 — Homologação: novação + passivo fiscal ✅

**STATUS: COMPLETE WITH OPEN ITEMS** (engajamento completo — 3 de 3 sessões)

## Entregável 1 — `sessao3/lancamentos_novacao.json`

**O lançamento da novação (na data da homologação — placeholder `D_HOM`, valores independem da data):**

| Partida | Valor (R$) |
|---|---|
| Dr — Passivo trabalhista em RJ (baixa) | 960.000 |
| Dr — Passivo quirografários/ME-EPP em RJ (baixa) | 6.470.000 |
| Cr — Novo passivo do plano | 3.548.000 |
| Cr — **Receita de renegociação de dívidas em RJ** (ganho) | **3.882.000** |

Dr 7.430.000 = Cr 7.430.000 ✓ (verificado em Python com asserções). Teste dos 10% do CPC 48 superado com folga — deságio de 60% nas classes III/IV é termo substancialmente diferente ⇒ baixa do passivo original e reconhecimento do ganho em rubrica própria.

- **Base nominal (assunção rotulada, item 13):** sem taxa de desconto informada, adotei taxa nula — **3.882.000 é o piso do ganho**. Com taxa positiva, o PV das parcelas cai e o ganho só aumenta (fórmula condicional documentada).
- **Novo passivo:** trabalhistas íntegros em **12× 80.000**; quiro/ME-EPP **120 parcelas** (média 21.566,67) após carência de 24 meses.
- **Lançamentos não efetuados (com justificativa legal):** União 2.700.000 (CTN 187; art. 68), Beta 3.100.000 (art. 49, §3º), pós-pedido 310.000 (art. 67).
- **Galpão (UPI):** partida condicional — Dr caixa 4.500.000; imobilizado e ganho de capital com `null` + rótulos, porque o valor contábil do imóvel **não foi informado** (item 8). Recomendo **alienação por via judicial** (art. 6º-B) — é o que afasta a trava de 30% do ganho de capital.
- **Tributário ligado:** PIS/COFINS sobre o ganho = 0 (art. 50-A, I); IRPJ/CSLL NAO_CALCULAVEL (alíquotas fora da biblioteca); despesas do plano dedutíveis (art. 50-A, III).

## Entregável 2 — `sessao3/passivo_fiscal_solucao.md`

**Proposta para os R$ 2.700.000 da União** (fora do plano — CTN 187/art. 68; execuções seguem correndo, art. 6º §7º-B; sem solução, a certidão trava a concessão — art. 57 + CTN 191-A):

| Rota (Lei 10.522) | Caixa | Folga da fonte (UPI 4.5 mi) |
|---|---|---|
| **C — Transação PGFN ≤ 70%** ⭐ proposta | 810.000 | **+142.000** (única positiva) |
| B — 30% com prejuízo fiscal + 84× | 1.890.000 | −938.000 (condicional ao item 3: prejuízo ≥ 810.000) |
| A — Parcelamento 120× | 2.700.000 | −1.748.000 (último recurso) |

**Recomendação: Rota C.** É a única que fecha o caixa com a fonte declarada (oimento do plano) e destrava a concessão já na adesão, via certidão positiva com efeito de negativa. Resalvas honestas: o teto de 70% é o limite da biblioteca, não o resultado garantido; o tratamento tributário do desconto da transação é NAO_VERIFICADO — **nenhum ganho foi lançado antecipadamente**; encargos/Selic e cronograma das parcelas ficam para o termo pós-adesão.

## O que ficou como aberto (sem re-pergunta)
- **Decisões executivas com a diretoria:** aprovar a Rota C e autorizar a venda judicial do galpão (recomendações emitidas;caixa não bloqueia os entregáveis).
- **Lacunas mantidas como assunção rotulada:** prejuízo fiscal (item 3), encargos (item 7), valor contábil do galpão (item 8), data da homologação (`D_HOM`).

Todos os arquivos estão em `workspace/deliverable/sessao3/`; `STATUS.md` (COMPLETE WITH OPEN ITEMS) e `QUESTIONS.md` (bloco de fechamento dos itens 11–14) estão atualizados.