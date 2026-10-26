# Perguntas ao cliente — regime tributário 2026

Rodada 1 enviada em 24/10/2026. **Rodada 2 (24/10/2026): o cliente respondeu Q1 e o mix de Q2.**
**Rodada 3 (24/10/2026 — encerramento): o cliente informou que "não tem informações adicionais" sobre
todas as perguntas não respondidas** (remanescente de Q2, Q3, Q4, Q5, Q6, Q7, Q8) e mandou não repetir as
já respondidas. **Nenhuma pergunta será reenviada.** As não respondidas ficam **encerradas** e registradas
como **desconhecidos explicitamente sinalizados**, com todo efeito **limitado por sensibilidade calculada**.
Nenhum número foi ajustado nem completado por suposição no lugar do dado faltante.

---

## Respondidas (não serão repetidas)

### Q1 — Composição da folha de pagamento — **RESPONDIDA** ✅
Resposta do cliente: **folha de pagamento (salários + pró-labore) = R$ 1.050.000**;
**encargos sobre folha (INSS patronal + RAT + FGTS etc.) = R$ 250.000**.
Fecha exatamente com a linha agregada do balancete (1.050.000 + 250.000 = 1.300.000).

**Efeito na conta:** a base do INSS patronal fora do Simples é a **folha** (R$ 1.050.000), não a linha
agregada. CPP = 28% × 1.050.000 = **R$ 294.000** (antes: 364.000). Presumido caiu de 1.079.620 para
**1.009.620**; Real de 1.080.790 para **1.010.790**; a vantagem do Simples caiu de 163.120 para
**93.120**. A conclusão (Simples mais barato) **não mudou**. Ver §4, §5 e §6-A do memorando.

### Q2 — Natureza e mix das receitas de obras — **PARCIALMENTE RESPONDIDA** ✅/⏳
Resposta do cliente: **"uns 15% do faturamento é obra pequena com material; o resto é consultoria"**
— igual ao balancete (630.000 / 4.200.000 = 15,0%). **Mix confirmado**, presunções 8%/32% mantidas, e o
vetor de sensibilidade do mix está encerrado (seriam precisos ≈32% de obras para o Presumido empatar).
⏳ Ainda não informado: se a obra é **empreitada com material fornecido pela Vértice** ou se o material
é do dono da obra (define Anexo IV vs. Anexo III e o tratamento de ICMS) — continua em aberto, apertado
por Q7/R1.

---

## Encerradas sem resposta — desconhecidos permanentes sinalizados (remanescente de Q2 · Q3 · Q4 · Q5)

### Q3 — Créditos de energia, aluguel, equipamentos, depreciação
Sem valor informado. Limitamos o efeito: para o Lucro Real empatar com o Simples (cenário-base) seria
preciso **R$ 1.019.351** de créditos adicionais de insumo (94.290 / 9,25%) — improvável, mas não verificado.

### Q4 — Demonstrativo de resultado (reconciliar o lucro de R$ 756.000)
Sem resposta. A subtração dos custos informados dá 4,2 mi − 1,05 mi − 0,25 mi − 1,4 mi = **R$ 1,5 mi**,
contra 756 mil informados → **≈ R$ 744 mil** de despesas não detalhadas. Não forçamos a reconciliação;
o lucro de 756 mil é usado como informado (P4) e o erro tem efeito limitado (cada 100 mil de lucro a mais
= +34 mil no Real). Ver R6.

### Q5 — Plano 2027 (crescimento de receita e mudança de folha)
Sem resposta. Usamos 2026 ≈ 12m (4,2 mi) e a folha informada de 1.050.000. Sensibilidade de receita: o
ponto em que o Presumido alcançaria o Simples é **≈ R$ 4.674.134** (folha fixa em 1,05 mi) — **abaixo** do
teto de 4,8 mi, ou seja, se a receita crescer ~11% o Simples deixa de ser o regime mais barato **antes** de
a empresa sair do Simples por teto. Precisamos da previsão de receita **e** de folha para 2027.

---

## Novas perguntas (rodada 2 — surgiram da resposta do cliente, não são repetição) — **encerradas na rodada 3 pelo mesmo motivo: o cliente não tem o dado; permanecem como desconhecidos limitados**

### Q8 — O plano "outra empresa no Lucro Real faturando dezembro" será realmente executado, e com o quê?
Pergunta feita pelo sócio em 24/10/2026 ("e se eu abrir outra empresa no Lucro Real e faturar dezembro
por ela?"). **Respondemos em `memorando.md` §8.2**: se migrar **só a receita**, o imposto **sobe**
(164.250 vs marginal de 130.375 — pior em 33.875); só haveria "ganho" (≈46.142) se **contratos, folha
(87.500/mês) e insumos (75.000/mês) migrem juntos** — desenho que concentra exatamente os fatos que a
**biblioteca não nos permite avaliar** (desvirtuamento/pluralidade simulada, cessão de contratos, regime
de empresa recém-constituída, estouro do teto — todos **não verificados**). Recomendação registrada:
**não executar**; o caminho legal para Lucro Real é a exclusão até 29/01/2027. Se o sócio insistir,
precisamos saber: **(a)** dezembro é mês de pico ou de vale (usamos média 350.000)? **(b)** a receita de
2026 vai fechar acima de 4,8 mi sem o plano? **(c)** que contratos/empregados/materiais efetivamente
passariam para a nova empresa em dezembro? **Encerrada na rodada 3:** o sócio não forneceu esses fatos; a
recomendação **não executar** permanece e a pergunta só reabre se o plano avançar com fatos concretos.

### Q6 — O que exatamente está nos R$ 250.000 de "encargos", e o Lucro Real deduziria a CPP?
É hoje **a pergunta mais importante do trabalho**. A biblioteca diz que, no Simples dos Anexos I, II, III
e V, a CPP **está dentro do DAS** e a empresa "não recolhe INSS patronal à parte" (`inss_patronal.md`).
Logo uma empresa no Anexo III **não pagaria** INSS patronal + RAT à parte em 2026 — e 28% × 1.050.000 =
**294.000 > 250.000**, ou seja, a linha contábil não pode conter a CPP integral devida fora do Simples.
Precisamos saber: **(a)** os R$ 250 mil são FGTS, 13º, férias e provisões (sem CPP)? **(b)** no plano de
2027 em Lucro Real, os R$ 294 mil de INSS patronal entrariam como **despesa dedutível**, reduzindo o lucro
de 756 mil? Por que importa: o escudo possível é 34% × 294.000 = **R$ 99.960**, maior que a folga de
93.120. Se a CPP inteira for incremental e dedutível, o Lucro Real fica em **910.830** — **5.670 abaixo**
do Simples, invertendo a recomendação (memorando §6-C). **Encerrada na rodada 3 (cliente não tem o
dado):** a inversão permanece **cenário-limite calculado, não adotado como caso-base**; o caso-base segue
Simples 916.500 vs Real 1.010.790, com esta dúvida explicitamente sinalizada como o único item capaz de
inverter o ranking (tolerância de apenas 5.670).

### Q7 — Qual parcela da folha (R$ 1.050.000) é paga nas atividades de obra, e qual é a folha dos serviços?
Para segregar a receita de obras ao **Anexo IV** (LC 123, art. 18, §4º, IV), é preciso saber quantos
funcionários/profissionais atuam nas obras (engenharia residente, medição, campo) versus na consultoria.
Por que importa: no Anexo IV a CPP **não** está no DAS, então a folha alocada às obras passa a pagar INSS
patronal à parte. Com a folha informada, o **ponto de empate com o Presumido é 31,7% da folha alocada às
obras** (R$ 332.600); a hipótese proporcional (15% = 157.500 → +44.100) mantém o Simples mais barato por
49.020. Ver memorando §6-B e R1. **Encerrada na rodada 3 (cliente não tem o dado):** o caso-base mantém a
classificação integral no Anexo III (a do balancete), com o ponto de empate (31,7% da folha) sinalizado.

---

## Pergunta que não foi feita (e não será)
**Não** pedimos confirmação de nenhum texto legal nem de alíquotas — isso é trabalho nosso. Tudo o que
depende de norma **não disponível na biblioteca** (alíquotas do Anexo IV e do Anexo V, regra dos 28% do
Fator R, critério de alocação de folha entre anexos, dedutibilidade da CPP no Lucro Real, recuperação de
ICMS-ST, redução de base de ISS da construção, exclusão de ofício por estouro de teto, **desvirtuamento /
pluralidade simulada de entidades, cessão de contratos e de pessoal, regime tributário de empresa
recém-constituída**, vencimentos de DARF,
feriados) está **marcado como não verificado** nos arquivos de entrega e não foi delegado ao cliente.
