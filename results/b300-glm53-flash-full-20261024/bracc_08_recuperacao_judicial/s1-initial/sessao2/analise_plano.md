# Análise do plano — Sessão 2 (cláusula a cláusula)

**Objeto:** minuta do plano (`documents/plano_minuta.md`) — legalidade de cada cláusula contra a única base admitida: `library/INDEX.md` (`lei11101_excertos.md`, `ctn_187_191a.md`, `lei10522_parcelamento_rj.md`, `cpc_contabil_rj.md`).
**Convenção do engajamento:** tudo que não tem texto na biblioteca é rotulado **NÃO VERIFICADO**; nenhuma regra "de memória" é citada.

## Quadro-síntese dos veredictos

| # | Cláusula da minuta | Veredicto | Fundamento |
|---|---|---|---|
| 1 | Classe I — trabaj. integral em até **18 meses** da homologação | **CONDICIONAL** (ilegal no estado atual do texto) | art. 54 caput = 1 ano; §2º até 2 anos com garantias + aprovação da classe |
| 2 | Classes III/IV — deságio 60%, 120×, carência 24m | **Não impugnado pela biblioteca** (regras de votação NÃO VERIFICADAS) | art. 49, caput (sujeição); biblioteca sem teto de deságio para quiro |
| 3 | Fiduciários "sujeitos ao plano, deságio 40%" | **ILEGAL** | art. 49, §3º |
| 4 | União "no plano": deságio 50%, 180× | **ILEGAL (duplicadamente)** | CTN 187; art. 68; teto de 120× na Lei 10.522 |
| 5 | Fonte: UPI galpão R$ 4,5 mi | **Legal com ressalva operacional** | art. 6º-B protege só a alienação **judicial** |

Números-base usados (calculados em Python, conferidos em `sessao1/demonstrativo_mensal_aj.md`): concursais **7.430.000** = 960.000 trab. + 6.470.000 quiro/ME-EPP (Alfa 4.200.000, Norte 1.850.000, Sul 420.000); plano pagável **3.548.000** = 960.000 + 6.470.000×40% (2.588.000); **ganho nominal 3.882.000** = 2.520.000 + 1.110.000 + 252.000.

---

## 1. Classe I — "pagamento integral em até 18 meses a partir da homologação"

- O art. 54, caput (`lei11101_excertos.md`) veta prazo **superior a 1 ano** para créditos trabalhistas **vencidos até a data do pedido**. Os R$ 960.000 são todos da data do pedido (relação de credores) → caput aplicável. **18 meses excedem em 6 meses o teto.**
- O §2º admite **até 2 anos** sob condições específicas: **garantias**, **aprovação da classe** e **integralidade**. A minuta satisfaz a integralidade (pagamento "integral"); **garantias e modo de aprovação não constam** e a diretoria afirmou não ter mais dados (QUESTIONS.md) → pressupostos NÃO VERIFICADOS.
- **Veredicto: CONDICIONAL — ilegal como escrita hoje.** Torna-se regular apenas se (i) o prazo for reduzido a **≤ 12 meses**, ou (ii) a minuta incorporar **garantias** e a aprovação da classe trabalhista for de fato obtida (§2º).
- **Recomendação:** reduzir a 12 meses e não depender do §2º (menor risco de impugnação e de invalidez). Se mantidos 18 meses, registrar expressamente na minuta as garantias que amparam o §2º.
- Ressalva técnica: a biblioteca não esclarece de que marco corre o prazo de 1 ano do caput (a minuta diz "a partir da homologação") — **NÃO VERIFICADO**; o excesso identificado (18 > 12) permanece em qualquer hipótese.

## 2. Classes III (quirografários) e IV (ME/EPP) — deságio 60%, 120 parcelas, carência 24 meses

- A sujeição destes créditos ao plano é a regra do art. 49, caput — base da cláusula, correta.
- **Não há texto na biblioteca** que limite deságio, prazo total ou carência de quirografários/ME-EPP; o art. 54 restringe apenas trabalhistas. A cláusula **não pode ser invalidada por nada que conste da biblioteca** — status: **não impugnado pela biblioteca**.
- As regras de **aprovação por classes e de votação não constam da biblioteca** (NÃO VERIFICADO): a cláusula depende de aprovação regular das classes presentes na relação — não há credores de classe II (garantia real): classe I trabalhistas, classe III quirografários, classe IV ME/EPP. E aqui está a **cláusula mais sensível**: o Fornecedor Norte.
- **Ponto de atenção Norte:** com a nova informação da diretoria (aceita fornecer à vista, mas exige um **"sinal"** sobre o atrasado, sob ameaça de cortar o suprimento), o tratamento registrado (740.000 em 120× após 24m de carência) pode não satisfazê-lo. Todo ajuste a favor do Norte **não pode gerar pagamento avulso**; se a diretoria quiser diferenciar o tratamento dele, isso se decide **dentro do plano** (tratamento da classe III, votado abertamente) — mecanismos de diferenciação não constam da biblioteca (NÃO VERIFICADO). A política de **fornecimento novo à vista** (art. 67) é a proteção operacional já acordada.
- Matemática: 6.470.000 → 2.588.000 (40%); ganho nominal **3.882.000** — sem juros/índice informados, fluxos tratados como nominais (assunção; ver QUESTIONS.md item 13).
- Efeito tributário do deságio: objeto do `efeito_tributario_desagio.json`, na mesma pasta.

## 3. Credores fiduciários — "sujeitos ao plano, com deságio de 40%"

- **ILEGAL.** O art. 49, §3º (`lei11101_excertos.md`) é o texto mais forte em contrário: o **proprietário fiduciário** de bens móveis/imóveis **não se submete aos efeitos da recuperação judicial**, prevalecendo **os direitos de propriedade**. Uma cláusula que impõe deságio (redução da dívida) ao fiduciário é **invalidável**.
- Fato novo que deve ir à impugnação: a diretoria confirmou que as máquinas do Banco Beta são **bens de capital essenciais** ("linha de separação de pedidos; sem elas, não opera"). Durante a suspensão do art. 6º, §4º (de 12/03/2026 até **08/09/2026**, prorrogável uma vez), é **vedada a venda ou retirada** do estabelecimento desses bens — o mesmo §3º. Ou seja:
  - o direito do Beta prevalece (fora do plano); e
  - por segurança operacional, os bens **ficam** no estabelecimento no período (produção protegida), sem nenhuma cominação monetária prevista na biblioteca.
- **Recomendação:** remover integralmente a cláusula; tratar o Beta fora do plano (extraconcursal, propriedade fiduciária preservada). Qualquer renegociação com o Beta é **comercial**, fora do plano — o plano não pode prevê-la.

## 4. União — "incluída no plano com deságio de 50% e 180 parcelas"

- **ILEGAL em dois planos independentes:**
  1. **Matéria de sujeição:** crédito tributário **não se sujeita** a concurso de credores ou habilitação (CTN art. 187 — `ctn_187_191a.md`) e **não se submete ao plano** da RJ (art. 68 — `lei11101_excertos.md`). Cláusula com deságio sobre crédito tributário é nula — a União nem sequer participa do voto das classes (a biblioteca não regulamenta votação — NÃO VERIFICADO — mas a ilegalidade da inclusão independe disso).
  2. **Matéria de regime fiscal:** o único regime de parcelamento/transação na biblioteca é o da Lei 10.522, arts. 10-A a 10-C (`lei10522_parcelamento_rj.md`), que conhece **até 120 parcelas** (10-A), **30% + 84 parcelas** (10-A §1º-B) ou **transação** (até 70% de desconto, até 120 meses). **180 parcelas não existem em nenhum desses regimes** — a cláusula descreve um programa inexistente.
- **Recomendação:** deletar a cláusula do plano inteira. A solução da União é **extraplanar**, pelas vias da Lei 10.522 — será qualificada na Sessão 3 (`passivo_fiscal_solucao.md`), com a escolha da diretoria entre as rotas (QUESTIONS.md, item 11). A adesão **não depende do plano** e destrava o art. 57 (certidão positiva com efeito de negativa) e reduz o risco das execuções fiscais, que **não se suspendem** pelo deferimento (art. 6º, §7º-B — ressalvados atos constritivos sobre bens de capital essenciais, no juízo da RJ).
- Coerência com o demonstrativo do mês 1: a União (2.700.000) já foi **excluída do quadro concursal** de ofício (`sessao1/demonstrativo_mensal_aj.md`, seção 3.2).

## 5. Fonte de recursos — "operação + venda de um galpão (UPI) por R$ 4,5 mi"

- **Legal em princípio:** venda de ativo próprio como fonte de pagamento do plano não é impugnada por nenhum texto da biblioteca.
- **Ressalva decisiva (texto literal):** o art. 6º-B (`lei11101_excertos.md`) afasta a trava de 30% **"ao ganho de capital na alienação judicial de bens em RJ"**. Nosso conhecimento da biblioteca **só cobre a alienação judicial**. Se a venda do galpão for privada (extra-judicial), o afastamento da trava **não está garantido pelo texto da biblioteca** (NÃO VERIFICADO).
- **Recomendação:** conduzir a venda por **via judicial** para capturar o art. 6º-B; se a diretoria preferir venda privada, o risco tributário do ganho de capital fica assinalado. Hoje, o ganho de capital do galpão **não está quantificado** (valor contábil não informado — QUESTIONS.md item 8; cliente sem mais dados) — deixado aberto de propósito.
- Cobertura (do demonstrativo do mês 1): 4.500.000 ≥ 3.548.000 → folga nominal 952.000; se a União for transacionada com desconto de 70%, até 810.000 de custo; folga cairia para **142.000**. Calibragem de prazos (carência de 24 meses × datas da UPI × parcelamento da União) permanece **não reconciliada com os dados disponíveis** — aberto.

## 6. Omissões da minuta (não são cláusulas, mas afetam execução e novação)

1. **Sem juros/correção** — as 120 parcelas e o trabalhista não têm índice/taxa informados; todos os números do plano são nominais (assunção com rótulo em todo entregável).
2. **Sem data-base de homologação** e cronograma ancorado — a carência de 24 meses fica sem termo inicial operável.
3. **Sem integração com a UPI** — a minuta menciona o galpão como fonte, mas não reserva cronograma de venda × pagamento das parcelas.
4. **Sem disposição sobre o parcelamento da União** — se a diretoria aderir à Lei 10.522, o plano deveria apenas **referenciar** o regime legal (não regulá-lo).

## 7. Novação e efeito contábil (ponte para a Sessão 3)

- Na **homologação**, a renegociação opera novação (`cpc_contabil_rj.md`). Com deságio de 60% (e 40% para fiduciários, que será removido), os termos são **substancialmente diferentes** — o teste do **10%** do CPC 48 (IFRS 9) é superado com folga → baixa-se o passivo original e reconhece-se o novo a **valor justo (PV das parcelas)**; a diferença é o **ganho** no resultado, divulgado separadamente como "receita de renegociação de dívidas em RJ".
- **PV pendente:** sem taxa de desconto (não informada; QUESTIONS.md item 13), os lançamentos da Sessão 3 ficarão em base **nominal** com assunção destacada, ou aguardarão a taxa. Com taxa positiva, o PV das 120 parcelas é menor que o nominal e o ganho contábil tende a ser **maior** que 3.882.000 (piso nominal).
- Trabalhistas: sem redução (integral), não geram ganho de renegociação — apenas efeito de prazo/alocação. União já fora do plano — qualquer efeito virá do parcelamento/transação, tratado na Sessão 3; o tratamento tributário de eventual desconto em transação **não consta da biblioteca** (NÃO VERIFICADO).

---

**Síntese para a diretoria:** a minuta, como está, **não deve ser protocolada sem ajustes**: (i) 18 meses trabalhistas precisam de §2º ou volta aos 12 meses; (ii) a cláusula fiduciária é nula e deve sair; (iii) a cláusula da União é nula e deve sair; (iv) a UPI deve ser alienação **judicial** para garantir o art. 6º-B. O núcleo do deságio (III/IV) é conforme com a biblioteca, desde que votado regularmente em classes (mecanismo NÃO VERIFICADO por falta de texto na biblioteca).

*Fontes citadas:* `lei11101_excertos.md`, `ctn_187_191a.md`, `lei10522_parcelamento_rj.md`, `cpc_contabil_rj.md` — todos em `library/INDEX.md`.
