# Análise das cláusulas da minuta do plano — Sessão 2

**Atlas Distribuidora S.A. — recuperação judicial** | Minuta em `documents/plano_minuta.md`
Método: cada cláusula recebe **LEGAL / ILEGAL / LEGAL COM RESSALVAS / NÃO VERIFICÁVEL** com o fundamento restrito à biblioteca (`library/INDEX.md`). O que a biblioteca não cobre está marcado como **não verificado**, sem citação.

---

## Cláusula 1 — Classe I (trabalhistas): "integral em até 18 meses a partir da homologação"

**ILEGAL como redigida.**
Fundamento: **art. 54** — o plano "**não poderá prever prazo superior a 1 ano**" para pagamento dos créditos trabalhistas vencidos até a data do pedido; o **§2º admite até 2 anos "em condições específicas: garantias, aprovação da classe, integralidade"** (`library/lei11101_excertos.md`).

- 18 meses > 1 ano ⇒ depende de satisfazer as condições do §2º.
- A cláusula cumpre a **integralidade**, mas **não prevê garantias nem exige aprovação da classe** como condição — como está, não passa.
- **Correção (uma das opções):** (a) pagar em **até 12 meses**; ou (b) estruturar para 24 meses cumprindo as condições do §2º: integralidade **+** garantias **+** submissão à classe I para aprovação.
- Risco se mantida: objeção de credores/MP e não homologação (art. 57 — a concessão depende de quitação fiscal; requisitos de assembleia — art. 58 **não verificado** na biblioteca, sem excerto: vide Cláusula 6).

## Cláusula 2 — Classes III e IV: "deságio de 60%, saldo em 120 parcelas, carência de 24 meses"

**LEGAL (para os concursais das classes III e IV).**
Fundamento: todos os créditos existentes na data do pedido sujeitam-se à recuperação (art. 49) e a biblioteca não contém limite para deságio/prazo/carência entre concursais — é matéria de negociação e de deliberação da assembleia. Base de cálculo: Alfa 4.200.000 + Norte 1.850.000 = 6.050.000 (III) e Sul 420.000 (IV); **total 6.470.000** → deságio 60% = **3.882.000**, saldo nominal **2.588.000** (aritmética em `efeito_tributario_desagio.json`).
**Ressalvas:** (i) efeitos tributários favorecidos pelo art. 50-A (ver `efeito_tributario_desagio.json`), **exceto** para dívidas com **pessoas ligadas** (art. 50-A, parágrafo único) — não confirmadas; relação entre credores e controladores é **desconhecida** (cliente não tem a informação); (ii) a vigência depende de aprovação em assembleia — quóruns do art. 58 **não verificáveis** na biblioteca; (iii) ME/EPP (Sul, R$ 420 mil) vota em classe própria — a Classe IV vem da relação de credores do cliente; a mecânica de votação por classe **não consta da biblioteca (não verificado)**.

## Cláusula 3 — "Credores com garantia fiduciária: sujeitos ao plano, com deságio de 40%"

**ILEGAL / INEFICAZ.**
Fundamento: **art. 49, §3º** — o credor titular da posição de **proprietário fiduciário** de bens móveis "**não se submete aos efeitos da recuperação judicial**, prevalecendo os direitos de propriedade" (`library/lei11101_excertos.md`). O Banco Beta (CCB com alienação fiduciária de máquinas, **R$ 3.100.000**) está **fora do plano**; deságio imposto por cláusula é inexequível — não haveria novação (o credor não é parte nem fica vinculado sem adesão).
**Correção:** suprimir a cláusula; tratar o Beta por **acordo bilateral** (que pode, este sim, prever deságio negociado — aí como renúncia voluntária, com efeito de novação por transação, e consequência tributária própria). **Contrapartida a nosso favor:** durante a suspensão do art. 6º, §4º (180 dias, prorrogável), é **vedada a venda ou retirada do estabelecimento das máquinas essenciais** (mesmo §3º) — as máquinas ficam conosco no período crítico.

## Cláusula 4 — "União incluída no plano com deságio de 50% e 180 parcelas"

**ILEGAL — duas vezes.**
Fundamento: **CTN, art. 187** (cobrança do crédito tributário "**não é sujeita a concurso de credores ou habilitação** em recuperação judicial") e **art. 68** da LRF ("**o crédito tributário não se sujeita ao plano**") (`library/ctn_187_191a.md`, `library/lei11101_excertos.md`). O deságio de 50% é inadmissível sem transação legal; as 180 parcelas excederiam até o limite do parcelamento especial (120).
**Correção:** suprimir; a via é o **parcelamento/transação** da Lei 10.522/2002, arts. 10-A a 10-C, que gera **CND+**, exigência para a concessão da recuperação (**art. 57; CTN art. 191-A**). Modelos com prazos e valores: `../sessao3/passivo_fiscal_solucao.md`. Alerta: **execuções fiscais não se suspendem** pela RJ (art. 6º, §7º-B) — deixar a União no plano "no papel" não protege contra penhora; só a adesão ao parcelamento/transação.

## Cláusula 5 — Fonte de recursos: "operação + venda de um galpão (UPI) por R$ 4,5 mi"

**LEGAL EM PRINCÍPIO, COM RESSALVAS.**
- Vender ativo para pagar o plano é lícito. Porém o **regime da UPI** (creio ser o art. 60-A da LRF: alienação de unidade isolada fora da RJ, com efeitos trabalhistas/societários próprios) **NÃO consta da biblioteca — NÃO VERIFICÁVEL**; a estrutura da venda (judicial x extrajudicial, sucessão de contratos/empregados) precisa de validação do contencioso antes de virar promessa no plano.
- Se houver ganho de capital em **alienação judicial** de bem em RJ, **não incide a trava de 30%** (**art. 6º-B**, verificado). Valor contábil do galpão **desconhecido** (cliente não informou) ⇒ ganho e IRPJ/CSLL da venda **não calculáveis** neste momento — item aberto.
- Os R$ 4,5 mi são **pretensão**: nada de venda de ativo aparece nos recebimentos das 4 semanas do fluxo (ver demonstrativo Sessão 1). No plano, fonte de recurso sem contrato gera objeção — buscar carta de intenção.

## Cláusula 6 — Omissões relevantes (o plano não diz)

1. **Regularidade fiscal para a concessão:** o plano não prevê a obtenção de **CND+** (art. 57; CTN 191-A via 10-A a 10-C). Sem isso a recuperação não é concedida — incluir cronograma de adesão dentro da janela de suspensão (180 dias, prorrogável).
2. **Critérios de aprovação:** quóruns/assembleia (art. 58) e critérios de homologação — o art. 58 está listado no INDEX mas **sem excerto na biblioteca ⇒ NÃO VERIFICÁVEL**; marcar com o contencioso.
3. **Tratamento de extraconcursais pós-pedido** (art. 67) e dos **honorários** do AJ/assessoria: ausência de previsão de caixa; valores de honorários **desconhecidos**.
4. **Norte:** eventual "critical vendor" só dentro do plano/assembleia ou por autorização judicial (art. 66 — **não verificado**); ver `../sessao1/addendum_sinal_norte.md`.

---

## Quadro-resumo

| # | Cláusula | Veredito | Fundamento (biblioteca) |
|---|---|---|---|
| 1 | Trabalhistas 18 meses | **Ilegal** como redigida | Art. 54 e §2º |
| 2 | Deságio 60% / 120x / 24m (III–IV) | **Legal** (ressalvas) | Art. 49; 50-A (tributação favorável); assembleia não verificável |
| 3 | Fiduciários no plano com 40% | **Ilegal/ineficaz** | Art. 49, §3º |
| 4 | União com deságio 50%/180x | **Ilegal** | CTN 187; art. 68; 6º §7º-B; 57/191-A |
| 5 | Venda do galpão (UPI) 4,5 mi | **Legal c/ ressalvas** | Art. 6º-B (trava não aplicável); regime UPI não verificado |
| 6 | Omissões (CND+, assembleia, extraconcursais) | **Pendências** | Art. 57; CTN 191-A; 10-A a 10-C; art. 67 |
