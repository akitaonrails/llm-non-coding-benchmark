# Resposta ao Diretor Financeiro

**Para:** Diretor Financeiro — Atlas Distribuidora S.A.
**De:** Controller
**Ref.:** (i) pagamento "por fora" ao Fornecedor Norte; (ii) tributação do ganho de deságio e a trava de 30%; (iii) inclusão da União no plano.
**Base:** apenas o arquivo do cliente e a biblioteca de referência (`library/INDEX.md`). Tudo que não está lá está sinalizado como **não verificado**.

---

## 1. Norte: não podemos pagar os R$ 1,85 mi "por fora do plano" — e não é questão de opinião

O saldo vencido do Norte (R$ 1.850.000, origem 15/01/2026) é **crédito existente na data do pedido** e, portanto, **concursal** (Lei 11.101/2005, art. 49 — `library/lei11101_excertos.md`). Pagar credor concursal fora do plano:

- viola a **par condicio creditorum** e configura **favorecimento de credor — crime** (art. 172 da LRF);
- **enseja o afastamento dos administradores** (art. 64);
- **pode levar à convolação em falência**.

(Excerto expresso nesses termos na biblioteca: `lei11101_excertos.md`, item "Pagamento de credor concursal fora do plano".) Pagar "pelo menos metade essa semana" colocaria você pessoalmente em risco criminal e a empresa em risco de falência. Não faremos isso.

**O que podemos (e devemos) fazer de forma legítima:**

1. **Pagar em dia tudo que é pós-pedido.** O fornecimento de 20/03/2026 (R$ 310.000) é obrigação contraída durante a recuperação, logo **extraconcursal** (art. 67) — paga-se no curso normal, sem autorização judicial. O caixa das 4 semanas informadas fecha em R$ 840 mil e cobre esse valor (demonstrativo anexo). Manter o Norte **em dia no que é novo** é o argumento prático para ele não parar: quem ele recebe garantido é o fornecimento novo, não o saldo velho.
2. **Se o saldo pré-pedido for mesmo essencial à atividade**, existe no sistema um caminho de **pagamento de crédito concursal pré-pedido com autorização judicial** quando essencial à atividade empresarial (creio ser o art. 66 da Lei 11.101/2005 — **essa norma NÃO está na nossa biblioteca de referência; trate como não verificado**). O caminho correto é **peticionar ao juízo da recuperação**, com justificativa de essencialidade, nunca pagar por fora. Posso preparar a minuta do pedido ao juízo.
3. **Alavanca de negociação com o Norte:** durante a suspensão do art. 6º, §4º (180 dias, prorrogável — decisão de processamento), o plano tratará esse crédito na classe quirografária; e a alternativa de todos (convolação) não interessa a nenhum credor.

## 2. Deságio de 60%: haverá ganho contábil, mas a "trava de 30%" **não se aplica** — a contabilidade está desatualizada

- **Ganho contábil:** com a homologação opera-se **novação** (LRF art. 59); sendo os termos substancialmente diferentes (teste dos 10%), baixa-se o passivo original e a diferença é **ganho** no resultado ("receita de renegociação de dívidas em RJ"), a valor justo (CPC 48/IFRS 9 — `library/cpc_contabil_rj.md`). A contabilidade está certa nisso.
- **PIS/COFINS:** a receita obtida pelo devedor na renegociação **não entra na base do PIS/COFINS** (Lei 11.101/2005, art. 50-A, I).
- **Trava de 30%: não se aplica.** O art. 50-A, II (redação da Lei 14.112/2020) afirma expressamente que o ganho com redução da dívida **não se sujeita ao limite percentual dos arts. 42 e 58 da Lei 8.981/95 e 15 e 16 da Lei 9.065/95** na apuração de IRPJ/CSLL. Ou seja, o prejuízo fiscal compensa o ganho do deságio **sem** o limite de 30%. As despesas do plano são dedutíveis (art. 50-A, III). **Ressalva:** o art. 50-A não se aplica a dívidas com **pessoas ligadas** — precisamos confirmar que nenhum credor (ex.: sócio/coligado) se enquadra.
- Alienação do galpão: se houver ganho de capital em alienação judicial de bens em RJ, a trava de 30% também não se aplica (art. 6º-B).
- A quantificação (ganho, compensação, IRPJ/CSLL) sai na **Sessão 2** — `efeito_tributario_desagio.json`.

## 3. União: não entra no plano — o caminho é parcelamento/transação (e é melhor para nós)

- **Impossível incluir no plano:** a cobrança de crédito tributário **não se sujeita a concurso de credores nem a habilitação** na recuperação (CTN, art. 187) e a LRF é explícita: **o crédito tributário não se sujeita ao plano** (art. 68 — `library/ctn_187_191a.md` e `lei11101_excertos.md`). A cláusula da minuta ("União incluída no plano com deságio de 50% e 180 parcelas") é **inaplicável** e será rejeitada; insistir nela só atrasa a homologação.
- **Execuções fiscais não se suspendem** com o deferimento da RJ (art. 6º, §7º-B), ressalvada a competência do juízo da RJ sobre atos constritivos de **bens de capital essenciais** — cuidado com penhora das máquinas (que também protegemos via art. 49, §3º frente ao fiduciário).
- **Via correta (Lei 10.522/2002, arts. 10-A a 10-C; Lei 13.988/2020; Portaria PGFN 2.382/2021 — `library/lei10522_parcelamento_rj.md`):**
  - parcelamento federal em até **120 parcelas** (art. 10-A); ou
  - liquidar até **30% com prejuízo fiscal/base negativa de CSLL** e o restante em **84 parcelas** (art. 10-A, §1º-B); ou
  - **transação com a PGFN** (desconto de até 70%, em até 120 meses).
- A adesão gera **certidão positiva com efeitos de negativa (CND+)**, que é **requisito para a concessão da recuperação** (LRF art. 57; CTN art. 191-A). Ou seja: não é opcional — precisamos de CND+ para homologar. Detalhamento com prazos e valores na **Sessão 3**.

## 4. Alertas sobre a minuta do plano (tratamos na Sessão 2)

- **Trabalhistas em 18 meses:** o art. 54 limita a prazo **não superior a 1 ano** para créditos trabalhistas vencidos até o pedido (§2º admite até 2 anos somente em condições específicas — garantias, aprovação da classe, integralidade). Precisa renegociar ou enquadrar nas condições do §2º.
- **Fiduciários "sujeitos ao plano com deságio de 40%":** o proprietário fiduciário **não se submete** aos efeitos da RJ (art. 49, §3º). Cláusula ilegal — Banco Beta (R$ 3,1 mi, CCB com alienação fiduciária) está fora do plano. Contrapartida útil: no prazo de suspensão, o fiduciário **não pode retirar/vender as máquinas essenciais** do estabelecimento (§3º).

**Resumo executivo:** (1) Norte pré-pedido: nada por fora — negociar e/ou pedir autorização judicial; Norte pós-pedido (R$ 310 mil): pagar normalmente, isso sim. (2) Ganho do deságio: compensável com prejuízo fiscal **sem trava de 30%** e fora da base de PIS/COFINS. (3) União: fora do plano; parcelamento/transação art. 10-A a 10-C para obter CND+ e viabilizar a homologação.
