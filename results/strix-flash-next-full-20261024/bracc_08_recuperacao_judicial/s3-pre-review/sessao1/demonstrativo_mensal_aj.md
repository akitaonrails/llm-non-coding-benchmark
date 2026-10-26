# Contas Demonstrativas Mensais — 1ª competência da Recuperação Judicial

**Atlas Distribuidora S.A.** — Recuperação Judicial
TJSP — 2ª Vara de Falências e Recuperações Judiciais — Proc. 1012xxx-xx.2026.8.26.0100
**Administrador Judicial:** AJ Reorganiza Ltda.
**Competência:** 1º mês do processo (março/2026) — período de referência: **semanas 1 a 4** do fluxo de
caixa informado, encerrando com o processamento deferido em **12/03/2026** (art. 52).
**Base legal:** apresentação de contas demonstrativas mensais enquanto perdurar a recuperação judicial,
**sob pena de destituição dos administradores** — Lei 11.101/2005, art. 52, IV (`library/lei11101_excertos.md`).

Todas as citações remetem a `library/INDEX.md`. O que não tem suporte na biblioteca está marcado
**NÃO VERIFICADO**. Valores em R$, sem correção monetária (não há índice nos arquivos).

---

## 1. Caixa e equivalentes

| Semana | Saldo inicial | Recebimentos | Pagamentos pós-pedido | Saldo final (cálculo) | Saldo final (arquivo) |
|---|---|---|---|---|---|
| 1 | 820.000 | 1.450.000 | 1.380.000 | 890.000 | 890.000 ✔ |
| 2 | 890.000 | 1.390.000 | 1.420.000 | 860.000 | 860.000 ✔ |
| 3 | 860.000 | 1.510.000 | 1.400.000 | 970.000 | 970.000 ✔ |
| 4 | 970.000 | 1.420.000 | 1.550.000 | 840.000 | 840.000 ✔ |
| **Mês** | **820.000** | **5.770.000** | **5.750.000** | **840.000** | **840.000 ✔** |

Aritmética do mês (reconciliada, sem ajustes):

```
Recebimentos:  1.450.000 + 1.390.000 + 1.510.000 + 1.420.000 = 5.770.000
Pagamentos:    1.380.000 + 1.420.000 + 1.400.000 + 1.550.000 = 5.750.000
820.000 + 5.770.000 − 5.750.000 = 840.000                     → confere com o arquivo
Geração líquida de caixa do mês: 5.770.000 − 5.750.000 = +20.000
```

Leitura para o AJ: a geração de caixa do mês é **quase nula** (+20.000 em 4 semanas, 0,35% dos recebimentos)
e a disponibilidade de 840.000 equivale a **14,6% dos recebimentos mensais** (840.000 ÷ 5.770.000), menos do
que a média semanal de pagamentos (5.750.000 ÷ 4 = 1.437.500). Não há folga para pagamentos extraordinários a
credores concursais (ver §3 e `resposta_diretor.md`).

**Ressalva material:** o arquivo `documents/fluxo_caixa_13_semanas.csv` tem o título de 13 semanas, mas só
**4 semanas** foram preenchidas (semanas 5 a 13 ausentes). Este demonstrativo cobre apenas as semanas 1–4.
Pedidos de complemento em `deliverable/QUESTIONS.md` (nº 1 e 2).

---

## 2. Obrigações pós-pedido (extraconcursais — art. 67)

Obrigações contraídas **durante** a recuperação, notadamente fornecimentos pós-pedido, são
**extraconcursais**: não entram no plano, não sofrem deságio nem carência e devem ser pagas no vencimento
(Lei 11.101/2005, art. 67 — `library/lei11101_excertos.md`).

| Obrigação | Fato gerador | Valor | Situação |
|---|---|---|---|
| Fornecedor Norte Ltda — entrega pós-pedido | 20/03/2026 | 310.000 | **A confirmar** (não identificada nos pagamentos das semanas 1–4) |
| Demais fornecimentos/obrigações do período | semanas 1–4 | embutidos em **5.750.000** de "pagamentos_pos_pedido" | Detalhe não informado |
| **Total identificado e exigível** | | **310.000** | |

```
Cobertura do crédito extraconcursal pelo caixa do fim do mês: 840.000 ÷ 310.000 = 2,71×
Caixa teórico se os 310.000 ainda não foram pagos: 840.000 − 310.000 = 530.000
```

**Ponto em aberto (não fechamos de propósito):** a coluna do CSV chama "pagamentos_pos_pedido" o total de
5.750.000, mas **não informa se os 310.000 da entrega de 20/03/2026 já estão pagos** nem qual a parcela
desse total que corresponde a fornecimentos essenciais, tributos e folha. As duas hipóteses acima ficam
abertas até a resposta do cliente.

Também ficam **fora do plano, mas não são extraconcursais**, os créditos com garantia fiduciária e os
tributários — §3 e §4 abaixo.

---

## 3. Créditos concursais (art. 49) e demais passivos identificados

Marco: estão sujeitos à RJ **todos os créditos existentes na data do pedido, ainda que não vencidos**
(art. 49 — `library/lei11101_excertos.md`). A data exata do pedido **não consta dos arquivos**; premissa:
pedido ajuizado entre **03/02/2026** e **12/03/2026** (pergunta nº 1).

| Classe | Credor | Valor | Sujeito ao plano | Fundamento |
|---|---|---|---|---|
| Trabalhista (I) | Trabalhistas — 112 empregados | 960.000 | Sim | art. 49; prazo do art. 54 |
| Quirografário | Banco Alfa (capital de giro) | 4.200.000 | Sim | art. 49 |
| Quirografário | Fornecedor Norte Ltda (pré-pedido) | 1.850.000 | Sim | art. 49 |
| ME/EPP (IV) | Fornecedor Sul S.A. | 420.000 | Sim | art. 49 (classe IV não verificada) |
| **Subtotal concursais** | | **7.430.000** | | |
| Extraconcursal fiduciário | Banco Beta (CCB, alienação fiduciária de máquinas) | 3.100.000 | **Não** | art. 49, §3º |
| Extraconcursal pós-pedido | Fornecedor Norte — entrega 20/03/2026 | 310.000 | **Não** | art. 67 |
| **Subtotal extraconcursal** | | **3.410.000** | | |
| Não sujeito (tributário) | União — IRPJ/CSLL/PIS/COFINS | 2.700.000 | **Não** | CTN art. 187; LRF art. 68 |
| **Total do passivo identificado** | | **13.540.000** | | |

Conferência: `7.430.000 + 3.410.000 + 2.700.000 = 13.540.000` ✔ (origem: `documents/relacao_credores.csv`).

Notas para o AJ:

1. **União (2.700.000):** fora do quadro de concursais — a cobrança judicial do crédito tributário não se
   sujeita a concurso nem habilitação (CTN art. 187 — `library/ctn_187_191a.md`) e o crédito tributário não
   se sujeita ao plano (art. 68 — `library/lei11101_excertos.md`). As **execuções fiscais não ficam
   suspensas** (art. 6º, §7º-B). A regularização se dá por parcelamento/transação (Lei 10.522/2002,
   arts. 10-A a 10-C — `library/lei10522_parcelamento_rj.md`), exigível também para a certidão necessária à
   concessão (CTN art. 191-A; LRF art. 57).
2. **Banco Beta (3.100.000):** proprietário fiduciário **não se submete** aos efeitos da RJ (art. 49, §3º);
   em contrapartida, durante a suspensão é **vedada venda ou retirada dos bens de capital essenciais**
   (art. 49, §3º, in fine). **Essencialidade confirmada pela administração na 2ª rodada:** as máquinas
   alienadas fiduciariamente são a **linha de separação de pedidos** e sem elas a operação não funciona.
   Logo, estão protegidas contra retirada/venda até **08/09/2026** (prorrogável até **07/03/2027**), e
   eventual ato constritivo sobre elas — inclusive penhora em execução fiscal — atrai a competência do juízo
   da recuperação (ressalva do art. 6º, §7º-B). O contrato do Beta segue fora do plano e **não temos a
   prestação mensal do CCB** (pergunta nº 16), o que impede fechar o serviço de dívida da empresa.
3. **Suspensão das execuções (§4º do art. 6º):** deferida em **12/03/2026** por **180 dias, prorrogável uma
   vez** (`documents/decisao_processamento.md`; art. 6º, §4º — `library/lei11101_excertos.md`). Cômputo:
   12/03/2026 + 180 dias = **08/09/2026**; com prorrogação, até **07/03/2027**.
4. **Concursais não listados:** o edital do art. 52, §1º foi determinado na decisão; habilitações e
   impugnações podem alterar o quadro acima. O procedimento e o prazo de habilitação **não constam da
   biblioteca** — **NÃO VERIFICADO**; o quadro deve ser reaberto após a relação do administrador judicial.

---

## 4. UPI — Unidade Produtiva Isolada (galpão, R$ 4.500.000)

Fonte de recursos prevista na minuta do plano (`documents/plano_minuta.md`): "venda de um galpão (UPI) por
R$ 4,5 mi".

| Item | Situação nesta competência |
|---|---|
| Valor de alienação previsto | 4.500.000 (valor de minuta/estimativa, não de proposta) |
| Ingresso no caixa das semanas 1–4 | **Não** — não há recebimento dessa ordem no fluxo |
| Efeito no passivo | Nenhum ainda: nenhuma novação/baixa de passivo antes da homologação |
| Régua de aprovação da venda | A disciplina de alienação da UPI **não consta da biblioteca** — **NÃO VERIFICADO** (não citamos art. 66-A) |
| Reflexo tributário, se houver alienação judicial | **Não se aplica a trava de 30%** ao ganho de capital na alienação judicial de bens em RJ (art. 6º-B — `library/lei11101_excertos.md`) |

Riscos a endereçar antes de contar com esse recurso: (i) não sabemos se o galpão está **livre de ônus**, se é
**essencial** à atividade ou se serve de garantia (pergunta nº 3); (ii) se o imóvel for essencial à operação,
a alienação em bloco como UPI tem de preservar a atividade — e o texto aplicável não está na biblioteca, de
modo que **não** damos parecer sobre a forma de venda; (iii) R$ 4,5 mi equivalem a **60,6%** dos concursais
(4.500.000 ÷ 7.430.000), de modo que a viabilidade do plano depende dessa venda — sensibilidade na Sessão 2.

**(iv) Risco novo e crítico, aberto na 2ª rodada:** a administração confirmou que a **linha de separação de
pedidos** (máquinas alienadas fiduciariamente ao Banco Beta) é essencial — mas **não disse em que imóvel ela
está instalada**. Se a linha estiver dentro do galpão oferecido como UPI por R$ 4,5 mi, a venda desmonta a
operação de que o próprio plano depende para gerar caixa; e, ainda que o imóvel seja vendido, as máquinas
são de terceiro (propriedade fiduciária do Beta) e **não podem ser entregues com o imóvel** nem retiradas
durante a suspensão (art. 49, §3º, in fine). É a **pergunta nº 15**, e trava a validação da fonte de recursos
do plano até resposta.

---

## 5. Conformidade e pendências do mês

- **Obrigação em dia:** esta é a 1ª conta demonstrativa mensal (art. 52, IV). A omissão sujeita os
  administradores à destituição (`library/lei11101_excertos.md`).
- **Alerta de conduta:** foi solicitada internamente a **quitação parcial (925.000) de crédito concursal
  fora do plano**. Registro expresso: pagamento de credor concursal fora do plano viola a par condicio
  creditorum e o art. 172 (favorecimento de credor — crime), com afastamento dos administradores (art. 64)
  e risco de convolação em falência (`library/lei11101_excertos.md`). Ver `resposta_diretor.md`.
- **Contabilização durante a RJ:** créditos concursais em rubrica própria e obrigações pós-pedido separadas
  (`library/cpc_contabil_rj.md`) — foi assim que este demonstrativo foi montado (§2 vs. §3).
- **Itens não reconciliados:** semanas 5–13 do fluxo; situação dos 310.000 pós-pedido; composição dos
  5.750.000 pagos; data exata do pedido; débitos trabalhistas vencidos antes/depois do pedido; ônus sobre o
  galpão/UPI **e localização da linha de separação de pedidos**; **prestação mensal do CCB do Banco Beta**;
  saldo de prejuízo fiscal e base negativa; taxa de desconto para o valor presente do novo passivo. Lista
  numerada em `deliverable/QUESTIONS.md` (o cliente informou não ter mais informações: os itens permanecem
  abertos e são tratados como **premissas explicitamente rotuladas** nas Sessões 2 e 3).

*Elaborado pela controladoria da Atlas Distribuidora S.A. para o administrador judicial. Não foi usada
qualquer fonte fora de `library/`.*
