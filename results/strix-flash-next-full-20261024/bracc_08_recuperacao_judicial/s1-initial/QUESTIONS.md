# Perguntas ao cliente — as três sessões

Numeração **fixa**: o mesmo número é usado em `sessao1/`, `sessao2/` e `sessao3/`. Itens respondidos **mantêm o
número** e vão para o arquivo do fim do arquivo — nenhuma referência muda de número no meio do trabalho.

O cliente informou que **não tem informação adicional** sobre os itens ainda abertos. Por isso cada pergunta aberta
tem uma **premissa assumida** (numerada P1–P11, tabela em `deliverable/sessao2/analise_plano.md`, repetida em
`deliverable/sessao3/lancamentos_novacao.json` → `premissas`), e os efeitos da premissa errada ficam registrados em
`reconciliacoes_abertas` e em `deliverable/STATUS.md`. Nada foi reconciliado à força.

---

## Marcos do processo

1. **Data exata do ajuizamento do pedido** da recuperação (os arquivos só trazem o deferimento do processamento em
   12/03/2026). É o marco do art. 49: define quem é concursal e, no art. 54, quais trabalhistas entram no teto de
   prazo.
   *Premissa assumida (P1):* pedido entre **03/02/2026** e **12/03/2026**. Se o pedido for posterior a 12/03, a nota
   de 12/03/2026 (210.000,00) deixa de ser pós-pedido e a base de L1 sobe para 6.260.000,00.
2. **Relação de credores e edital do art. 52, §1º:** já publicados? Houve **habilitação ou impugnação** de créditos?
   A administradora judicial já apresentou relação própria?
   *Efeito:* o quadro de concursais (13.540.000,00) pode mudar. O procedimento de habilitação **não consta da
   biblioteca** → NÃO VERIFICADO, não citamos artigo.
3. **Galpão oferecido como UPI (R$ 4.500.000,00):** de quem é o imóvel (matrícula/propriedade) e se os R$ 4,5 mi são
   **proposta firme, appraisal ou estimativa**.
   *Parcialmente respondida (Rodada 3):* a operação roda em **imóvel alugado** → o galpão não é a sede operacional.
   Propriedade, titular e natureza dos 4,5 mi seguem desconhecidos.
   *Premissa assumida (P8):* venda **não** realizada até a homologação; não há recebimento no fluxo.
4. **Máquinas dadas em alienação fiduciária ao Banco Beta:** são bens de capital essenciais (art. 49, §3º, in fine)?
   *Respondida (Rodada 3):* **sim** — são a **linha de separação de pedidos**, essenciais à atividade. Já constou a
   existência de **ação de reintegração / busca e apreensão** em curso? Isso segue aberto.
5. **Trabalhistas (960.000,00 / 112 empregados):** discriminado com (a) vencido **antes** e **depois** do pedido,
   (b) parcelas vincendas (aviso prévio, FGTS, multas), (c) valores até 5 salários mínimos por credor, (d) acidentes
   de trabalho. Decide se os 18 meses da minuta cabem no art. 54 (1 ano; até 2 anos só com garantia real ou
   fidejussória expressa, aprovação da classe I e pagamento integral — §2º).
   *Trava:* sem o corte pré × pós pedido não há como dimensionar o teto. Custos das duas rotas estão em
   `sessao2/analise_plano.md` (a opção §2º custa 26.666,67/mês a mais de caixa).
6. **Composição dos 5.750.000,00 de "pagamentos_pos_pedido"** e situação da **entrega do Norte de 20/03/2026
   (310.000,00)**: já foi paga, em qual semana do fluxo? Quanto desses pagamentos foi feito a credores **pré-pedido**?
   *Parcialmente respondida (Rodada 3):* a Norte fornece **à vista** e o "sinal" de 925.000,00 **não foi pago** (e não
   pode ser — ver `sessao1/resposta_diretor.md`). Composição dos 5,75 mi segue desconhecida.

## Créditos e garantias

7. **Sul S.A. (420.000,00):** enquadramento como **ME/EPP** em 2026 e se o crédito decorre de fornecimento contínuo
   (classe IV). Também: qual a data do pedido usada pela empresa nas relações de credores.
   *Premissa:* mantida na classe IV da relação de credores. A base legal da classe IV **não está na biblioteca** →
   NÃO VERIFICADO.
8. **Prejuízo fiscal e base negativa de CSLL** acumulados e disponíveis, por exercício, e limitações eventuais.
   *Premissa assumida (P6):* **zero** — é ausência de dado, não afirmação. Com prejuízo ≥ 3.882.000,00 o IRPJ/CSLL
   sobre o ganho tende a zero (a trava de 30% do art. 50-A, II não se aplica à RJ).
9. **Taxa de desconto** (e periodicidade de pagamento) para o valor presente das 120 parcelas com carência de 24
   meses.
   *Premissa assumida (P9):* **1,5% ao mês**. Toda a mensuração é sensível a isso — grade de sensibilidade em
   `sessao2/efeito_tributario_desagio_sensibilidade.md` e `sessao3/lancamentos_novacao.json` →
   `sensibilidade_por_taxa`.
10. **União (2.700.000,00):** quanto em **débito declaratório** e quanto em **dívida ativa**; há parcelamento ou
    transação em curso? Existem **execuções fiscais/bloqueios** ativos? Há CND ou CPD-EN hoje?
    *Trava:* define a ordem de aderência às rotas da Lei 10.522/2002, arts. 10-A a 10-C (Lei 13.988/2020) e a emissão
    da CND-E (art. 57 da LRF; art. 191-A do CTN) — `sessao3/passivo_fiscal_solucao.md`.
11. **Semanas 5 a 13** do `fluxo_caixa_13_semanas.csv` (o arquivo só tem 4 semanas). Se não existem, confirmar que o
    demonstrativo mensal cobre as semanas 1–4.
    *Premissa assumida (P4):* geração de caixa de **+5.000,00/mês** extrapolada das 4 semanas preenchidas. É o
    único dado de geração de caixa do engajamento.
12. **Outros fornecedores essenciais** com risco de corte e exposição pré-pedido, além da Norte Suprimentos: valor e
    data de origem, para levar ao juízo/AJ de forma fundamentada (e não pagar por conta própria).
    *Parcialmente respondida (Rodada 3):* a Norte é o caso conhecido (fornece à vista; pede 925.000,00 de sinal).
13. **Formalização do pedido de pagamento "por fora do plano" à Norte (925.000,00):** foi formalizado por alguém
    (e-mail, aprovação de pagamento, painel de pagamentos)? Houve **algum** pagamento a credor concursal desde
    12/03/2026? Precisamos para as contas mensais ao AJ (art. 52, IV).
14. **Pessoas ligadas:** algum credor do plano é controlador, administrador, sócio, coligada, controlada ou pessoa
    interposta da Atlas? O art. 50-A, parágrafo único, **exclui** dívidas com pessoas ligadas de todos os benefícios
    fiscais do deságio.
    *Premissa assumida (P3):* nenhum credor do plano é pessoa ligada.

## Bens, garantias e calendário

15. **Galpão da UPI × imóvel onde a linha de separação está instalada:** é o mesmo imóvel? Se a linha estiver no
    galpão oferecido à venda, a venda descontinua a operação e colide com a proteção do art. 49, §3º, in fine.
    *Trava:* é a principal fonte de recursos do plano (4.500.000,00) e não pode ser validada sem essa resposta.
16. **Prestação mensal do CCB do Banco Beta** (3.100.000,00, vencido desde 03/2025): valor, prazo e taxa do contrato
    original / renegociação em curso.
    *Trava:* sem isso o serviço de dívida da empresa não fecha — os cenários de caixa de
    `sessao2/analise_plano.md` usam o payoff integral de 3.100.000,00 como piso.
17. **Ônus sobre o galpão** oferecido como UPI: hipoteca, penhora, alienação fiduciária, outras garantias.
    *Trava:* decide se os 4.500.000,00 são realmente disponíveis para o plano e se a classe III seria paga com
    produto de bem gravado.
18. **Despacho de homologação / status da assembleia-geral de credores:** data prevista ou realizada do pedido de
    homologação, e calendário de parcelas a partir daí.
    *Premissa assumida (P5):* as 120 parcelas são contadas da **homologação** (t=0), como diz a minuta; a suspensão
    do art. 6º, §4º corre de 12/03/2026 a 08/09/2026, prorrogável até 07/03/2027 (P2).
19. **Composição dos 1.480.000,00 de fornecedores extraconcursais** no extrato de 31/03/2026 (saldo que não bate com
    os 310.000,00 pós-pedido da relação de credores): quais notas, de que período, pré ou pós pedido.
    *Trava:* deixa 1.170.000,00 sem classificação — registrado em `reconciliacoes_abertas`, não lançamos.
20. **Débitos tributários estaduais e municipais:** existem? Estão em dívida ativa, parcelados, garantidos por
    seguro/penhora? Não estão na relação de credores nem no extrato.
21. **Valor contábil do galpão** (custo amortizado e depreciação acumulada) e sua rubrica no imobilizado.
    *Trava:* sem esse valor o lançamento L9 (reclassificação da UPI) não tem importe e a ganho/perda da venda não pode
    ser medida.
22. **Despesas da recuperação judicial:** honorários do administrador judicial, dos administradores substitutos,
    advogados da empresa e demais custos do processo, com base de cálculo e periodicidade.
    *Trava:* são extraconcursais (art. 67) e dedutíveis (art. 50-A, III), mas sem valor não entram no caixa nem na
    base fiscal.

---

## Arquivo — respostas recebidas (mantêm o número da pergunta que fecharam)

**Rodada 2**
- CCB do Banco Beta **vencido desde 03/2025** (informação que sustenta o tratamento do item 16 e o payoff de
  3.100.000,00 nos cenários de caixa).
- O crédito do Beta é garantido por **alienação fiduciária de máquinas** — por isso não entra no plano
  (art. 49, §3º) e o deságio de 40% da cláusula 3 da minuta é **inafastável** (1.240.000,00 não lançáveis).

**Rodada 3**
- Nº 4: as máquinas fiduciárias são **bens de capital essenciais** — são a linha de separação de pedidos.
- Nº 4 (reforço): além da fiduciária, há **garantias reais adicionais e aval dos controladores**; o avalista não pode
  ser pago pelo plano.
- Nº 3: o imóvel da operação é **alugado** → o galpão oferecido como UPI não é a sede; a identidade do imóvel segue
  em aberto (nº 15).
- Nº 6: a Norte Suprimentos fornece **à vista**; o "sinal" de 925.000,00 **não foi pago** e, se pago, seria pagamento
  de crédito pré-pedido fora do plano (ilegal — art. 49; risco de destituição e de convolação).
- Nº 12: nenhum outro fornecedor essencial com exposição pré-pedido foi indicado além da Norte.

**Rodada 4 (instrução permanente)**
- "Para as perguntas não respondidas acima, o cliente não tem informação adicional. Marque explicitamente as
  incógnitas restantes." → todas as perguntas 1–22 ainda abertas foram convertidas em **premissas declaradas**
  (P1–P11) com o efeito de cada uma quantificado; nenhuma será repetida.
