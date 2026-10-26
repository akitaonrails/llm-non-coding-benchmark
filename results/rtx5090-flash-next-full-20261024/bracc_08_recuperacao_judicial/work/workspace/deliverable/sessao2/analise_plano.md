# Análise do Plano de Recuperação Judicial (minuta) — cláusula a cláusula

**Atlas Distribuidora S.A.** — Processo TJSP 1012xxx-xx.2026.8.26.0100
Fonte analisada: `documents/plano_minuta.md`. Autoridade: apenas `library/INDEX.md`. Onde a biblioteca é silenciosa, digo que o ponto **não é verificável** aqui.

**Visão geral:** das 5 cláusulas, **3 são ilegais/ineficazes** (fiduciário, União, e — condicionalmente — o prazo trabalhista), **1 é legal** (quirografários/ME-EPP) e **1 é legal mas condicionada** (fonte de recursos). O plano, como redigido, **não seria aprovado** e, pior, esconderia o principal risco operacional da empresa: a retomada das máquinas do Beta após a suspensão.

---

## Cláusula 1 — Classe I (trabalhistas): integral em até 18 meses

**Veredito: CONDITIONALMENTE ILEGAL — só se sustenta se preenchidas as condições do art. 54, §2º.**

- Regra geral: **art. 54** — o plano **não pode prever prazo superior a 1 ano** para créditos trabalhistas vencidos até o pedido. 18 meses viola a regra.
- Exceção: **§2º admite até 2 anos** em condições específicas: **garantias, aprovação da classe, integralidade**.
  - Integralidade: ✓ (a minuta prevê pagamento integral — R$ 960.000, art. 49).
  - Aprovação da classe: ✗ incerto — depende de assembleia da classe I.
  - Garantias: ✗ não previstas na minuta.
- **Recomendação:** reduzir para **12 meses**, salvo se a empresa estiver disposta a dar garantia e a buscar aprovação da classe I. Custo mensal na regra de 12 meses: 960.000 ÷ 12 = **R$ 80.000/mês**; nos 18 meses da minuta: 960.000 ÷ 18 = **R$ 53.333/mês** (diferença de R$ 26.667/mês — marginal, não vale o risco de impugnação).
- Não verificável na biblioteca: critérios de convocação/votação das classes em assembleia (arts. 39–45 não constam).

## Cláusula 2 — Classe III (quirografários) e IV (ME/EPP): deságio 60%, 120 parcelas, carência de 24 meses

**Veredito: LEGAL (dentro do que a biblioteca permite verificar).**

- Deságio e alongamento de quirografários/ME/EPP são mecanismos típicos de plano; **nenhum excerto da biblioteca os veda** (limite: o art. 50 — conteúdo mínimo/facultativo do plano — não consta da biblioteca, então a estrutura completa não é verificável; classifico como legal *à luz do material disponível*).
- Efeito tributário favorável expresso: **art. 50-A** — sem PIS/COFINS sobre a renegociação (I), sem trava de 30% para compensar o ganho (II), despesas do plano dedutíveis (III). Ver `efeito_tributario_desagio.json`.
- Ponto de atenção financeira (aritmética, não legal): o fluxo de caixa das semanas 1–4 é quase neutro (+R$ 20.000 no período). Parcelas de classe III/IV começam em 2028 (carência 24): saldo nominal 6.470.000 × 40% = 2.588.000 ÷ 120 = **R$ 21.567/mês** — administrável, mas o plano **não pode contar com o caixa atual para pagar o Norte "por fora"** (ver `sessao1/resposta_diretor.md`).
- ME/EPP (Fornecedor Sul, R$ 420 mil): a aplicação do mesmo deságio à classe IV não tem vedação na biblioteca; tratamento específico de ME/EPP fora dela — **não verificável**.

## Cláusula 3 — Credores com garantia fiduciária: "sujeitos ao plano, com deságio de 40%"

**Veredito: ILEGAL/INEFICAZ contra o Banco Beta.**

- **Art. 49, §3º**: o titular de **propriedade fiduciária não se submete aos efeitos da RJ**; prevalece o direito de propriedade. O plano **não pode** puxar o Beta para dentro com deságio de 40% (pretensão de ganho de R$ 1.240.000 = 40% × 3.100.000 que **não se materializa** — não incluí no cálculo tributário).
- O que a lei dá é a proteção da **empresa**: durante a suspensão do art. 6º, §4º (180 dias, prorrogável uma vez — decisão de 12/03/2026), é **vedada a venda ou retirada de bens de capital essenciais**. O cliente **confirmou que as máquinas são a linha de separação de pedidos** → sem elas não há operação.
- Consequência prática: após a janela de suspensão, o Beta pode fazer valer a fidúcia. **Saneamento do plano:**
  1. Excluir o Beta do plano; negociar **acordo bilateral** (o pagamento de credor extraconcursal não é favorecimento — art. 172 protege a igualdade entre concursais).
  2. Fontes: galpão R$ 4.500.000 − quitação Beta R$ 3.100.000 = **R$ 1.400.000 de sobra** para operar/juniorizar.
  3. Agir **dentro da janela**: acordar com o Beta extensão/quietação condicionada à venda do galpão, submetida ao juízo/AJ.
- Cautela: se o galpão também for bem essencial à distribuição, a alienação durante a suspensão exige autorização judicial (ratio do art. 49, §3º, in fine) — submeter ao AJ.

## Cláusula 4 — União: "incluída no plano com deságio de 50% e 180 parcelas"

**Veredito: ILEGAL em três frentes.**

1. **CTN art. 187**: crédito tributário **não se sujeita a concurso de credores nem habilitação** em RJ.
2. **Art. 68 da LRF**: o crédito tributário **não se sujeita ao plano** (Fazendas podem deferir parcelamento especial — via própria, não o plano).
3. **Art. 6º, §7º-B**: execuções fiscais **não se suspendem** pela RJ — a União pode penhorar enquanto o plano "parcela".
4. Detalhe adicional: mesmo a via correta tem teto — **Lei 10.522, art. 10-A: até 120 parcelas** (ou transação da PGFN até 120 meses). "180 parcelas" não existe em nenhuma modalidade da biblioteca.
- Deságio de 50% sobre tributos via plano: inexistente; desconto só existe via **transação** (até 70%, Lei 13.988/2020/Portaria PGFN 2.382/2021 — citadas no índice), sujeita às regras da PGFN.
- **Bloqueio adicional**: a **concessão da recuperação exige certidão negativa/positiva com efeito de negativa** (art. 57 da LRF; CTN art. 191-A). Sem adesão ao parcelamento/transação, o processo **não concede a recuperação** independentemente do plano. Solução completa com prazos e valores: `deliverable/sessao3/passivo_fiscal_solucao.md`.

## Cláusula 5 — Fonte de recursos: operação + venda de galpão (UPI) por R$ 4,5 mi

**Veredito: LEGAL, com duas condições práticas.**

- Nada na biblioteca veda a fonte. Se a alienação for **judicial**, o ganho de capital fica fora da trava de 30% (**art. 6º-B**).
- Condição 1: o galpão ainda não tem valor contábil informado (cliente não tem a informação) — ganho contábil **não calculável**; deixo em aberto, não estimo.
- Condição 2 (novo, com a resposta do cliente): o destino natural do produto é **quitar o Beta e salvar a linha de separação de pedidos** (R$ 4,5 mi − R$ 3,1 mi = R$ 1,4 mi). A minuta não diz isso — e é o ponto que decide se a empresa opera depois da suspensão. Recomendo reescrever a cláusula com essa destinação expressa.

---

## Quadro-resumo

| # | Cláusula | Veredito | Fundamento | Correção |
|---|---|---|---|---|
| 1 | Trabalhistas 18 meses | Condicionalmente ilegal | Art. 54 (1 ano; §2º até 2 anos cond.) | 12 meses, ou garantia + aprovação da classe |
| 2 | Quiro/ME-EPP: 60%, 120x, carência 24 | Legal | Art. 49; art. 50-A (tributação) | Manter; fluxo sustenta R$ 21.567/mês pós-carência |
| 3 | Fiduciário no plano, deságio 40% | Ilegal/ineficaz | Art. 49, §3º | Tirar do plano; acordo bilateral + quitação com o galpão |
| 4 | União no plano, 50% e 180x | Ilegal | CTN 187; art. 68; art. 6º, §7º-B; Lei 10.522 art. 10-A (120x) | Parcelamento/transação (Sessão 3) |
| 5 | Galpão R$ 4,5 mi | Legal, condicionada | Art. 6º-B; art. 49 §3º (bens essenciais) | Destinar à quitação do Beta; valor contábil pendente |

## Deságio eficaz (base do cálculo tributário)

- Classe III: 4.200.000 + 1.850.000 = 6.050.000; Classe IV: 420.000 → **base 6.470.000**
- Deságio 60% → **ganho 3.882.000**; nominal renegociado **2.588.000**
- Trabalhistas integral (sem ganho); fiduciário fora (cláusula ineficaz); União fora (não sujeita).
- Detalhamento PIS/COFINS/IRPJ/CSLL/prejuízo fiscal: `efeito_tributario_desagio.json`.
