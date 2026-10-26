Excelente objeção — provavelmente é **a** discussão que decide o acordo. Vou responder com números, mas antes recalculo as três cenários possíveis em Python para não me apoiar em intuição:

Os números confirmam a tese. Resposta ao ponto em questão:

Seu primo acerta a **regra-mãe** (CC 1.659 — bens particulares) e ignora as **duas regras-parte** que a disciplinam (CC 1.660, V — frutos do trabalho comunicam — e a jurisprudência que a biblioteca registra). Nenhuma das duas perguntas é "ponto final"; e o custo de tratá-las como tal é assimétrico: o ganho teórico é de R$ 70.000, a exposição é de R$ 200.000. Por partes:

## 1. FGTS — "é meu salário"

*"É meu salário" é a **origem** do dinheiro, não o **regime** dele.* Sob comunhão parcial, os frutos do trabalho percebidos na constância comunicam (CC art. 1.660, V — `cc_comunhao_parcial.md`); o que o art. 1.659, VI ("proventos do trabalho pessoal") protege não é o FGTS **já depositado** — a biblioteca registra no STJ (REsp 1.399.199/RS, 2ª Seção, 2017 — `stj_fgts_quotas_previdencia.md`) que depósitos feitos na constância **integram o comum e partilham, ainda que o saque fique diferido**. Salário recebido durante o casamento não fica particular — vira FGTS, carro ou PGBL, e todos entram na partilha pelo mesmo critério. O saldo de 140.000 está depositado desde o casamento: por isso a meação da Fernanda é 140.000 ÷ 2 = **70.000**.

**O que o conselho do primo realmente compra, em números (Python):** se o FGTS sair da conta como "particular", o comum cai de 2.290.000 para 2.150.000, a meação de cada um cai de 1.145.000 para 1.075.000, e o pagamento total iria de 995.000 para **925.000** (550.000 haveres + 375.000 de equalização) — economia teórica de **R$ 70.000**. Mas se em juízo prevalecer o REsp (que é a posição registrada na biblioteca), os mesmos 70.000 voltam à conta — *pagos com honorários, custas e anos de processo incluídos*. Na melhor das hipóteses para o primo, você termina com a mesma conta e mais gasto. Pior: ao contestar um ponto onde a peça da própria advogada da Fernanda já errou, você destrói o crédito recém-formado que sustenta as concessões (reforma de 60.000, FGTS revisado) e convida a prima a reabrir todo o resto.

E há um espelho que corta contra você: se "FGTS é de quem depositou", então *o FGTS em nome dela* (se houver saldo — não constava no registro) seria dela e não seu — a mesma regra corre para os dois lados.

## 2. Empresa — "é de antes do casamento"

**Meia verdade — metade funcional.** Sociedade constituída em 2011: as quotas são particulares **no valor de 2014: R$ 400.000** (CC art. 1.659, I — e aqui seu primo está certo). O que ele ignora é o segundo passo: você mesmo confirmou no turno passado que **nunca distribuiu lucro — reinvestiu tudo** — e o valor subiu de 400.000 para 1.500.000. Esses **1.100.000** são fruto do período comum: lucros não distribuídos/reinvestidos comunicam (CC art. 1.660, V; STJ REsp 1.595.775/AP — `stj_fgts_quotas_previdencia.md`).

Três consequências práticas:
- **A empresa continua 100% sua.** Fernanda não entra na sociedade: recebe **apuração de haveres em dinheiro (550.000)** — só a metade da valorização do período. Você mantém o controle integral e a administração intacta.
- **"Ponto final" custaria 200.000.** Se você levar a tese "tudo particular" à frente — ou simplesmente não fechar —, a prima persiste no que **já escreveu**: "metade das quotas" = 750.000 sobre 1.500.000. Nesse cenário a conta salta de 995.000 para **1.195.000** (200.000 a mais; 140.000 acima do plano completo de 1.055.000, com a compensação da reforma virando briga em vez de concessão).
- **O plano atual já é a concessão.** 550.000 < 750.000: você está pagando a metade da *valorização do casamento* — não "metade da empresa". Seu primo está propondo, sem números, um jogo cujo pior desenho é perder mais 200.000.

## Síntese

| Tese do primo | Ganho se prevalecer | Custo se prevalecer (e ela prevalecerá na biblioteca) |
|---|---:|---:|
| FGTS particular | 70.000 (economia teórica) | 70.000 devolvidos + honorários + anos de processo |
| Empresa toda particular | 0 (não é a pretensão dela) | +200.000 (750.000 em vez de 550.000) |

Nenhum dos dois conselhos adiciona valor; o segundo só abre a porta que o acordo fecha. Recomendo manter o plano: FGTS revisado (70.000 concedidos), haveres de 550.000 sem sócia, pagamento total de **1.055.000** — e registrar a objeção nos entregáveis para que a resposta fique documentada:

Registrando a resposta nos entregáveis:

The STATUS edit introduced an unintended bold wrapper on the PGBL line — reverting it and adding the turno-3 record properly:

One garbled sentence in STATUS.md to fix:

Objecção respondida e registrada nos entregáveis.

## Resumo da resposta ao cliente

1. **FGTS** — "ser meu salário" define a origem, não o regime: depósitos feitos na constância estão incorporados e comunicam (CC 1.660, V; REsp 1.399.199/RS — `stj_fgts_quotas_previdencia.md`), ainda que o saque fique diferido. Seguir o conselho do primo economiza 70.000 teoricamente (conta iria de 995.000 → 925.000) e devolve os mesmos 70.000 em juízo — com honorários e anos de processo incluídos. Ganho líquido esperado: **zero ou negativo**. E a tese corre simétrica: o FGTS em nome dela (se houver — nova pendência registrada) também partilharia.

2. **Empresa** — particular é só a parte de 2014 (**400.000**, CC 1.659, I — aí o primo acerta). Os **1.100.000** do crescimento — que o próprio cliente confirmou vir do reinvestimento de lucros sem distribuição — comunicam (CC 1.660, V; REsp 1.595.775/AP). E insistir no "ponto final" é o cenário de **maior custo**: a prima já escreveu "metade das quotas" = 750.000; nessa escalada a conta salta de 995.000 para **1.195.000** (+200.000). O plano em pé paga 550.000 em dinheiro, sem ela ingressar na sociedade — a empresa continua 100% do Marcelo.

**Síntese quantificada:** o conselho informal compra zero na melhor hipótese e até **+200.000** na realista. Recomendação mantida: FGTS revisado (70.000), haveres 550.000, pagamento total 1.055.000.

## Entregáveis atualizados

- **`proposta_acordo.md`** — nova subseção §5-A "Objeção do cliente (turno 3)" com os três cenários (A 995.000 / B 925.000 / C 1.195.000) calculados e conferidos em Python.
- **`QUESTIONS.md` + `PERGUNTAS.md`** (sincronizados) — nova pendência: saldo de FGTS de Fernanda (meação cruzada simétrica pela mesma regra).
- **`STATUS.md`** — seção "Turno 3" com a objeção, a resposta e a recomendação mantida; JSONs validados intactos.

Pronto para a conversa de fechamento: **plano de 1.055.000 permanece a recomendação**, e a objeção do primo está hoje no papel, com números, se ele quiser discutir.