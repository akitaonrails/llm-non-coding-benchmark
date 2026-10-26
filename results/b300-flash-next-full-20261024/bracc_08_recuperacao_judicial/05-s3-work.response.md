

Sessão 3 já está entregue e validada — `deliverable/sessao3/lancamentos_novacao.json` (5 lançamentos, todos com débitos = créditos conferidos por script) e `deliverable/sessao3/passivo_fiscal_solucao.md`. Segue o resultado:

## Contabilização da novação (evento: homologação do plano — CPC 48/IFRS 9, novação do art. 59)

| # | Evento | Débito | Crédito |
|---|---|---|---|
| 1 | **Classe III** (Alfa 4.200.000 + Norte pré-pedido 1.850.000) | Passivo concursal original **6.050.000** | Novo passivo plano (PV) **2.420.000** + **Receita de renegociação 3.630.000** |
| 2 | **Classe IV** (Sul EPP) | Passivo concursal **420.000** | Novo passivo **168.000** + **Receita 252.000** |
| 3 | **Classe I** (trabalhistas, integral) | Passivo trabalhista **960.000** | Novo passivo plano **960.000** (reclassificação, sem ganho nominal) |
| 4 | **União — adesão ao parcelamento** (não é novação de plano!) | Tributos federais a recolher **2.700.000** | Passivo de parcelamento especial (curto/longo prazo) **2.700.000** |
| 5 | **Galpão UPI** (condicional) | Banco 4.500.000 + ajuste | Imobilizado pelo **valor contábil — desconhecido**, lançamento sem valores até o número chegar |

**Ganho do deságio: 3.630.000 + 252.000 = 3.882.000** — bate com `efeito_tributario_desagio.json` da Sessão 2 ✔ (divulgação separada no resultado, receita fora de PIS/COFINS e sem trava de 30% — art. 50-A, I e II).

**Passivo pós-homologação (nominal): 9.348.000** = plano 3.548.000 + parcelamento federal 2.700.000 + Beta fiduciário fora do plano 3.100.000 (contra 13.540.000 pré-plano; diferença de 4.192.000 = deságio 3.882.000 + Norte pós-pedido 310.000 que sai ao ser pago).

Premissas declaradas no JSON: valores **nominais** porque a taxa de desconto do plano não foi informada — quando vier, o novo passivo cai a PV e o ganho sobe na diferença; Beta não novae sem acordo bilateral; IRPJ/CSLL diferidos sobre o ganho ficam com a auditoria (CPC 32 fora da biblioteca); e, se algum credor for **pessoa ligada**, o ganho dele perde o art. 50-A (parágrafo único) — relação desconhecida, item aberto.

## Passivo fiscal (União, R$ 2.700.000) — via, prazos e valores

CTN 187 + art. 68 tiram o tributo do plano, mas art. 57 + CTN 191-A exigem **certidão para a concessão** — e a adesão ao parcelamento/transação gera **CND+**. Paga-se a União **por fora do plano para poder homologar o plano**:

| Via | Estrutura | Parcela/mês (sobre principal) |
|---|---|---|
| **A** — parcelamento especial (Lei 10.522, art. 10-A) | 2.700.000 em 120x | **22.500** |
| **B** — art. 10-A §1º-B: 30% liquidados em prejuízo fiscal (810.000) | 1.890.000 em 84x | **22.500** (consome 810.000 de PF) |
| **C** — transação PGFN (Lei 13.988/2020; Portaria 2.382/2021), teto 70% de desconto | 810.000 em 120x | **6.750** |

**Recomendação: C → A como piso.** Cada real de desconto da transação economiza R$ 1,00 de caixa; cada real de PF economiza só a alíquota (~34%, não verificada) — logo, se o PF for escasso (preciso ≥ **4.692.000** para cobrir ganho 3.882.000 + Via B 810.000), vale preservar PF para o ganho e brigar pela transação; a Via B só fecha se a transação falhar **e** o PF for abundante. Via A é o piso porque **a homologação não espera**: sem CND+ não há concessão.

**Cronograma:** tudo dentro da suspensão de **180 dias (prorrogável)** — simulação oficial no e-CAC e minuta de transação na PGFN desde já; CND+ antes da concessão; execuções fiscais seguem correndo (art. 6º §7º-B), com a defesa das **máquinas essenciais** (competência do juízo da RJ) como alerta de constrição.

**Não quantificado (desconhecidos declarados):** composição do débito por tributo/inscrição, saldo de PF/base negativa (decide B vs. C), percentual efetivo de desconto da transação, e encargos Selic do parcelamento (parcela real > 22.500 — usar simulação do e-CAC). Os `null` do JSON da Sessão 2 se preenchem com o item PF.