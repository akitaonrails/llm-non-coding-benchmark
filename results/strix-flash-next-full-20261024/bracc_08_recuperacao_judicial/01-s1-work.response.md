Vou analisar os dados e fazer os cálculos com Python antes de redigir.

Cálculos conferidos. Agora vou escrever os entregáveis da Sessão 1.

Sessão 1 concluída. Arquivos gravados:

**`deliverable/sessao1/resposta_diretor.md`** — resposta aos três pedidos do diretor:
- **Pagar o Norte "por fora do plano": não.** R$ 1,85 mi têm origem em 15/01/2026, antes do pedido → crédito concursal (art. 49). Pagar fora do plano viola a *par condicio* e o art. 172 (favorecimento de credor — crime), com afastamento dos administradores (art. 64) e risco de convolação em falência. E o caixa não sustenta: `840.000 − 925.000 = −85.000`. O caminho lícito é pagar a **entrega pós-pedido de 20/03/2026 (R$ 310.000)**, extraconcursal (art. 67) — o caixa cobre 2,71× — e contratar os fornecimentos novos como pós-pedido.
- **União no plano com deságio de 50%: inexequível.** CTN art. 187 (não sujeita a concurso/habilitação), LRF art. 68 (crédito tributário não se sujeita ao plano), art. 6º §7º-B (execuções fiscais não suspensas). O "ganho" de R$ 1.350.000 não existe e as 180 parcelas extrapolam o teto de 120 da Lei 10.522, art. 10-A. Via correta: parcelamento/transação para obter CND-E exigida pelo art. 57 da LRF e CTN 191-A.
- **Trava de 30%: não se aplica.** Art. 50-A, II afasta o limite das Leis 8.981/95 e 9.065/95; I afasta PIS/COFINS sobre a receita da renegociação; III permite deduzir despesas do plano. E o ganho contábil será **menor** que o deságio nominal (CPC 48, teste dos 10%, passivo novo a valor presente): teto nominal `6.470.000 × 60% = 3.882.000`. Alertas extras: cláusula fiduciária (art. 49 §3º) e trabalhistas em 18 meses (art. 54).

**`deliverable/sessao1/classificacao_creditos.json`** — 7 créditos, JSON validado no esquema do contrato: concursais sujeitos ao plano **7.430.000** (trabalhista 960.000 / quirografários 6.050.000 / ME-EPP 420.000); extraconcursais **3.410.000** (fiduciário 3.100.000 + pós-pedido 310.000); União **2.700.000** não sujeita; total **13.540.000**, conferindo com o arquivo.

**`deliverable/sessao1/demonstrativo_mensal_aj.md`** (art. 52, IV) — caixa reconciliado (`820.000 + 5.770.000 − 5.750.000 = 840.000`, geração de apenas +20.000), obrigações pós-pedido, quadro de concursais/extraconcursais, UPI (R$ 4,5 mi = 60,6% dos concursais, sem ingresso de caixa), suspensão de 180 dias contada de 12/03/2026 → **08/09/2026** (prorrogável até 07/03/2027).

**`deliverable/QUESTIONS.md`** (14 perguntas) e **`deliverable/STATUS.md`**: **COMPLETE WITH OPEN ITEMS**. Principais aberturas declaradas: data exata do pedido (premissa: entre 03/02 e 12/03/2026), semanas 5–13 do fluxo ausentes, situação dos R$ 310.000 pós-pedido e composição dos 5.750.000 pagos, ônus/essencialidade do galpão e das máquinas, e taxa de desconto + prejuízo fiscal para o cálculo da Sessão 2. Classificações cuja base legal não está na biblioteca (classe trabalhista nos arts. 41/83, classe IV ME/EPP, regime da UPI) estão marcadas como **NÃO VERIFICADO** em vez de citadas.