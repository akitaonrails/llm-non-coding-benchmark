# Nota à sócia — contrato NexaClin × Clínica Aurora (linguagem simples)

**Para:** Dra. Beatriz Lemos · **Assunto:** o que precisa mudar na minuta antes de assinar · **Prazo:** assinar em 10 dias é viável se enviarmos a contraproposta nesta semana.

## 1. Sobre o foro: a colega está errada, e é bom que a senhora saiba antes de "brigar" por isso

A cláusula de foro em **Florianópolis** (casa da NEXA) **não é abusiva e não pode ser anulada pelo CDC** neste contrato:

- O Código do Consumidor só vale para **relação de consumo**. A clínica contrata o software como **insumo da sua atividade** (prontuário e faturamento), não como destinatária final. É a "teoria finalista" do STJ, e sua exceção ("finalista mitigada") exige **vulnerabilidade demonstrada** — não se presume numa sociedade com R$ 9,2 milhões de faturamento assessorada por advogado (Lei 8.078/90, arts. 2º, 3º e 51).
- Entre empresas, a eleição de foro é **válida** quando consta de instrumento escrito e cita o negócio — o contrato faz isso (CPC, art. 63, caput e §1º; STJ, REsp 1.707.855/SP, citado na biblioteca). A regra do art. 63, §3º (juiz anular foro abusivo de ofício) mira contrato de adesão com parte vulnerável, não o nosso caso.

Consequência prática honesta: se um dia litigarmos com a NEXA, será em Florianópolis. Isso é **inconveniente, não ilegalidade**. Se a senhora quiser, negociamos "foro do domicílio do réu" — mas como preferência comercial, não como cláusula nula. Não recomendo gastar capital de negociação aqui; há pontos muito mais graves abaixo.

## 2. O que de fato precisa mudar (resumo)

| Cl. | Problema em uma frase | Gravidade |
|---|---|---|
| 5 | Entrega dados de saúde (prontuário/exames) para a NEXA usar em "pesquisa e produtos", em servidores onde ela quiser, sem papéis LGPD. **Substituir pela cláusula nova (clausula_dados.md).** | Alta |
| 12 | Permite subcontratar hospedagem/suporte **sem nos avisar** — fere o controle que a LGPD exige do nosso papel de controladora. | Alta |
| 7 | No fim, devolve dados só em CSV e por 30 dias — incompatível com a guarda de 20 anos do prontuário (Res. CFM 1.821/2007; Lei 13.787/2018). | Alta |
| 13 | Proíbe a clínica de **usar qualquer software concorrente por 5 anos em todo o Brasil**, multa de R$ 500 mil — o STJ considera esse tipo de restrição sem limite territorial/tempo desproporcional inválida, e aqui ela nem protege know-how (é o licenciante quem detém o software). **Excluir.** | Alta |
| 10 | Sair antes do prazo = pagar **100% das mensalidades que faltam** (ex.: no mês 12, R$ 496.800). Reduzível pelo juiz (CC art. 413), mas negociemos um teto. | Média |
| 3 | Renovação automática de 36 em 36 meses com aviso de 180 dias — tranca junto com a multa acima. Pedir renovação de 12 meses e aviso de 90 dias. | Média |
| 2 | Reajuste "IGP-M **ou outro índice a critério da NEXA**" — índice tem que ser certo; nada de troca unilateral. | Média |
| 8 | Teto de indenização = 3 mensalidades (R$ 62.100) mesmo se vazar prontuário de 22 mil pacientes. Pedir carve-out para dados/confidencialidade e teto de 12 mensalidades. | Média |

Estão bem como estão: objeto (1), obrigações (4), SLA com créditos (6), confidencialidade (9), multa por atraso (11), foro (14), gerais (15).

## 3. Os números, com a conta feita

- Mensalidade: R$ 6.900 × 3 unidades = **R$ 20.700/mês** → ano: 20.700 × 12 = **R$ 248.400** → 36 meses: 20.700 × 36 = R$ 745.200 + implantação R$ 48.000 = **R$ 793.200** (sem reajuste).
- Multa de saída no fim do 12º mês: 24 vincendas × 20.700 = **R$ 496.800** ≈ 2 anos de mensalidade.
- Teto de responsabilidade: 3 × 20.700 = **R$ 62.100** ≈ **R$ 2,82 por paciente** (22.000) — irrisório diante de um vazamento de dados de saúde, cuja reparação é dever legal nosso e da NEXA (LGPD, art. 42).
- Multa da não concorrência: R$ 500.000 ≈ 500.000 ÷ 20.700 ≈ **24 mensalidades** (2,01 × o valor anual do contrato).
- SLA: 99% numa conta de 30 dias = até 7,2 h de indisponibilidade/mês; crédito de 2% por ponto = 0,02 × 20.700 = R$ 414/pt, teto 10% = R$ 2.070/mês. Remédio fraco, mas lícito.

## 4. Dados: o que a senhora perguntou ("vamos colocar prontuário, exames, tudo lá")

Pode — mas só com a nova Cláusula 5 (arquivo `clausula_dados.md`). Pontos que a senhora precisa aprovar:

- **Papéis:** a clínica é a controladora (quem decide), a NEXA é operadora (executa). Isso manda o risco regulatório para a NEXA quando ela desobedecer (LGPD, arts. 5º, 39 e 42).
- **Base legal dos dados de saúde:** não é "consentimento de todo paciente" — é a **tutela da saúde** prestada por serviço de saúde (LGPD, art. 11, II, "f"). Menos burocracia e base mais firme.
- **Integração com Unimed/Bradesco (TISS):** permitida expressamente como "transação financeira/administrativa" de faturamento (LGPD, art. 11, §4º) — desde que limitada ao necessário por faturamento. A NEXA **não** poderá minerar esses dados para vender produtos.
- **A promessa de dados "anonimizados/agregados" para pesquisa da NEXA:** na prática, com 22 mil pacientes quase nunca é anonimização irreversível (LGPD, art. 12) — cortamos.
- **Incidentes:** aviso em 24 h para conseguirmos comunicar ANPD/titulares em 3 dias úteis (Res. CD/ANPD 15/2024, citada na biblioteca).
- **Deveres da clínica que o contrato não resolve:** a Aurora **não tem encarregado (DPO) formal** e tem política de privacidade genérica. Nomear o encarregado e atualizar a política são passos nossos, independentes do contrato (LGPD, art. 5º, VIII). Recomendo concluir antes ou junto com a assinatura.

## 5. Plano para os 10 dias

1. Enviar contraproposta com as redações de `clausulas.json` + nova Cláusula 5 (dias 1-2).
2. Pedir à NEXA: lista de subcontratados e local dos servidores; certificações de segurança; onde os dados já estão hospedados hoje (dias 1-2).
3. Nomear encarregado e revisar a política de privacidade do site (dias 3-7).
4. Linha vermelha: **Cláusula 13 (não concorrência) e o uso de dados para "P&D" da NEXA — sem cortar, não assinar.** Cláusulas de preço/SLA são negociáveis; dados e prontuário, não.

## 6. Premissas e lacunas

- Clínica Aurora: sociedade empresária, 3 unidades, ~22.000 pacientes, R$ 9,2 mi/ano, sem DPO (ficha do cliente); contrato B2B, não de consumo.
- Confirmado pela NEXA (via cliente): hospedagem em AWS, "provavelmente" nos EUA → tratamos no item 7 e na nova Cláusula 5 (item 5.7).
- Lacunas ainda abertas (cobradas da NEXA na negociação, não da senhora): **região exata da AWS e base legal da transferência; lista completa de subcontratados; certificações de segurança**. Do lado interno, sem resposta até hoje: cidades das 3 unidades (só para preferir negociar o foro) e histórico de incidentes. O parecer não depende de nenhuma delas; as redações cobrem ambos os cenários.
- Nada neste parecer usa lei fora da biblioteca de referência do arquivo; o que a biblioteca não cobre (ex.: valores de multas administrativas da ANPD) não foi afirmado.

## 7. Atualização — respostas recebidas da NEXA

**(a) "AWS, provavelmente nos EUA".** Hospedar no exterior **não é ilegal por si só** — mas a LGPD só permite transferência internacional nos mecanismos do art. 33 (país adequado, cláusulas-padrão etc.). "Provavelmente" não serve: é informação vaga justamente sobre o dado mais sensível que existe (prontuário). Exigimos, antes de assinar (nova Cláusula 5, item 5.7): **revelação por escrito da região exata em 30 dias + comprovação do mecanismo do art. 33 (ex.: cláusulas-padrão com a AWS), ou plano de migração para região no Brasil em até 90 dias**; sem isso, rescisão sem multa. A AWS passa a figurar como subcontratada notificada (item 5.6). Não há nada aqui que justifique trocar de fornecedor agora — há uma exigência de papel e de região.

**(b) "Migrar 22 mil prontuários é projeto de meses; sair no meio seria caótico."** É exatamente o argumento que usamos a nosso favor:
- valida a nova Cláusula 7 (exportação estruturada + **180 dias de transição** com sistema funcionando) — sem isso a senhora ficaria com 20 anos de dever de guarda (CFM) e sistema desligado;
- enfraquece a multa da Cláusula 10 e as renovações de 36 em 36 meses da Cláusula 3: a clínica fará investimentos consideráveis para executar o contrato, e o CC (art. 473, parágrafo único) exige que a saída ocorra em **prazo compatível** com eles — a multa de 100% das vincendas fecha a porta de saída em nome de quem justamente não pode sair às pressas;
- na prática: a decisão de não renovar precisa ser tomada **~6 meses antes** de cada aniversário da vigência (aviso de 180 dias). Com renovação de 12 meses que propomos, errar o timing custa 1 ano, não 3.

Plano de 10 dias inalterado; a exigência da cláusula 5.7 entra na carta de contraproposta como condição de assinatura.
