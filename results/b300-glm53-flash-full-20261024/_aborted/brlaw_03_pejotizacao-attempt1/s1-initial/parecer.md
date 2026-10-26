# Parecer — Solaris Tecnologia Ltda. × Rafael Moreira (R.M. Desenvolvimento de Sistemas Ltda.)

**Época:** out/2026 · **Ajuizamento anunciado:** 16/11/2026 · **Encerramento da prestação:** 30/09/2026 · **Contrato (PJ):** 01/10/2019 a 30/09/2026 (84 meses)

**Conclusão executiva.** O Tema 725 **não** dá "risco zero": ele valida a *terceirização lícita entre pessoas jurídicas*, não a contratação de PJ que oculta empregado nos termos do art. 3º da CLT com desvirtuamento (art. 9º). Os indícios no arquivo apontam subordinação, pessoalidade e controle de jornada tolerados pela própria Solaris. Probabilidade de reconhecimento de vínculo: **alta (estimativa 65–80%)**. Exposição quantificada no quinquênio exigível: **R$ 1.738.392,00** (sem horas extras) ou **≈ R$ 1.898.551** com a estimativa de horas extras disponível. Recomendo **provisão CPC 25 "provável" de R$ 1.329.000** e **abertura de acordo** com faixa-alvo de **R$ 900.000 a R$ 1.350.000**. A decisão da diretoria de não provisionar é tecnicamente insustentável neste estado probatório.

Toda citação remete a arquivos de `library/INDEX.md`. Onde um parâmetro usual **não constava** da biblioteca, está assinalado.

---

## 1. Os requisitos do art. 3º da CLT, com as provas do arquivo

Art. 3º (biblioteca `clt_requisitos_vinculo.md`): empregado é quem presta serviços **não eventuais**, sob **dependência** e mediante **salário** — pessoalidade, não eventualidade, onerosidade, subordinação. Também conforme essa página: **art. 9º** (nulidade de pleno direito dos atos que desvirtuem/fraudarem a CLT) e **art. 442-B** (o autônomo contínuo, **com ou sem exclusividade**, afasta o vínculo **desde que ausente a subordinação**); e a nota ao **art. 818**: admitida a prestação de serviços, a prova de que os serviços eram prestados sem subordinação — a autonomia — incumbe à **reclamada**.

| Requisito | Indício no arquivo | Fonte (documents/) |
|---|---|---|
| Pessoalidade | Contratada é unipessoal (sócio único: Rafael) e o contrato exige que "a CONTRATADA **disponibilizará seu sócio**" — só o Rafael pode prestar; substituição não é prevista | `contrato_prestacao_servicos_pj.pdf` (cabeçalho e item 4) |
| Não eventualidade | Prestação contínua de 01/10/2019 a 30/09/2026 (84 notas mensais, 12/ano) | `notas_fiscais_resumo.csv` |
| Onerosidade | R$ 18.000,00/mês **"independentemente de entregas"** — remuneração fixa por tempo, não por obra (própria de emprego, não de autônomo remunerado por resultado) | contrato, item 2 |
| Subordinação | Contrato: horário fixo 9h–18h, seg–sex, nas dependências da Solaris **ou** home office **"autorizado pelo gestor"**; **reporta-se** ao Gerente de Engenharia; **exclusividade** proibindo outros clientes (art. 442-B só afasta vínculo com exclusividade **se ausente subordinação** — aqui ela está presente) | contrato, itens 3, 4 e 5 |

Complementos probatórios — todos em `prints_mensagens.txt`:

- **Controle de jornada pela empresa:** Carla (gerente) registra o desvio de 20 minutos ("vi que você logou 9h20... o combinado é 9h. Marca no planilha de ponto") e determina permanência até **20h** por força de release — ordem direta de sobrejornada a PJ é incompatível com autonomia.
- **Benefícios-clonagem CLT:** pedido de férias aprovado pelo **RH**, com **"saldo de 20 dias"** interno; **avaliação de desempenho "mesmo formulário dos CLTs"**. A cláusula 6 do contrato ("Férias: 20 dias por ano") reforça o aparato empregatício simulado.
- **Planilha de ponto com horas extras registradas** (`escala_e_planilha_ponto.csv`): Jan–Jun/2025, médias de 9,0–9,8 h/dia e 18–34 HE/mês. Que a entidade-cliente *marque ponto de PJ* e registre HE é o indício mais objetivo de subordinação *juridicamente verificável*; a página de jurisprudência (`tst_sumulas_ojs.md`) traz a **Súmula 338** (presunção de jornada pelo controle empregador) e a **Súmula 212** (ônus do término do contrato é do empregador) como vigentes.

Leitura da defesa (o que ainda se pode opor): autonomia técnica do desenvolvedor, formalidade PJ e rotina fiscal própria (notas), ausência de sanção disciplinar provada, cláusula de rescisão "contratual". Consideração honesta: esses argumentos perderam força porque os itens 3–6 do contrato e as mensagens desmentem a forma PJ; e, nos termos do art. 818 (como anotado na biblioteca), é a Solaris que terá de provar autonomia. **Síntese: predominância de empregado.**

**Status dos precedentes citáveis.** `tst_sumulas_ojs.md`: Súmulas 331 (terceirização/subsidiária), 212, 338, 363 (não aplicável — administração pública) e OJ 383 (isonomia — depende de terceirização ilícita, fora do caso) estão **vigentes**. A **Súmula 256** e a **OJ SDI-1 nº 191** estão **CANCELADAS** pela própria página e não foram usadas.

## 2. Por que o Tema 725 não resolve

`stf_tema_725_adc48_adpf324.md`: a tese do Tema 725 é a licitude da **terceirização/divisão de trabalho entre pessoas jurídicas distintas**, com responsabilidade subsidiária — ele não fixou tese sobre **pejotização com simulação de empregado**; a própria página registra que os requisitos do art. 3º com fraude (art. 9º) ficam sujeitos a exame **caso a caso** (inclusive em reclamações do STF). A ADC 48 versava transportador autônomo (Lei 11.442) — ainda mais longe do caso. O e-mail da diretoria empurra dois pontos: (i) tema diverso (terceirização ≠ pejotização); (ii) o STF nunca disse "PJ + contrato + nota = sem vínculo". Portanto: o Tema 725 **não afasta o reconhecimento de vínculo** quando presentes os elementos do art. 3º — que aqui estão, apoiados nos documentos e no ônus invertido de prova de autonomia (art. 818, nota da biblioteca).

## 3. Tema 1.389 (pejotização) — efeitos

`stf_tema_1389_pejotizacao.md` (ARE 1.532.603/DF, rel. Min. Gilmar Mendes; RG abril/2025; **suspensão nacional 14/04/2025; biblioteca congelada em out/2026: mérito pendente**):

- **Efeito processual:** a reclamação de 16/11/2026, mesmo instrutória, tenderá a ser **sobrestada** até o julgamento do mérito (prática varia por TRT). Isso **retarda**, não impede.
- **Efeito na exposição:** nada some; juros/correção correm (a página cita **Lei 14.905/2024 — IPCA + SELIC-IPCA**). Uma eventual tese sobre **ônus de prova da fraude** pode restringir ou ampliar o resultado, mas, enquanto pendente o mérito, o provisionamento continua necessário e o mercado precifica o cenário integral.
- Implicação prática: a "anestesia" da suspensão **aumenta o custo final** (tempo + correção). Para provisionamento e acordo, o risco não pode ser tratado como zero.

## 4. Prescrição

Base (`cf_art7_xxix_prescricao.md`): **CF art. 7º, XXIX** / CLT art. 11 — 5 anos + até 2 anos após a extinção; **Súmula 308 TST** — a quinquenal abrange créditos anteriores aos 5 anos **contados do ajuizamento**; mesma regra para FGTS (a página cita STF Tema 608 com modulação). Aviso-prévio proporcional pela Lei 12.506/2011 considera o **tempo total de serviço** mesmo com verbas prescritas.

- **Ajuizamento:** 16/11/2026 → **corte quinquenal: 16/11/2021**.
- **Bienal pós-extinção:** extinção 30/09/2026 + 2 anos = 30/09/2028; ajuizamento em 16/11/2026 ⇒ **dentro do prazo** ✔.
- **Granularidade mensal (adotada):** meses prescritos = Out/2019–Nov/2021 = **26**; meses exigíveis = Dez/2021–Set/2026 = **58**; 26 + 58 = 84 = total do contrato ✔. Nov/2021 é mês cortado pelo dia 16: parte de seu crédito é anterior ao corte; adotei o corte favorável à defesa (Nov/2021 inteiro como prescrito). A visão oposta (58,5 exigíveis / 25,5 prescritos) muda **Δ13º ≈ R$ 1.500** e **ΔFGTS ≈ R$ 120–180** — irrelevante na ordem de grandeza.
- **13º, férias e FGTS:** contados pelos mesmos 26/58 meses (ver §6). Férias: dos 7 períodos aquisitivos (P1 01/10/2019–30/09/2020 … P7 encerrado em 30/09/2026), **P1 e P2 prescritos**; **P3–P7 exigíveis (5)**.
- Nota honesta: se a instrução apurar horas extras em períodos hoje prescritos, o corte muda; sem essa prova, fica como está.

## 5. Prescrição aplicada às verbas

Pelos parâmetros de `verbas_e_calculo.md`: 13º **1/12 por mês**; férias+1/3 **simples** (tempo, não dobradas — a página permite essa simplificação); **FGTS 8% sobre salários + 13º + férias com 1/3** (textual da biblioteca); **multa 40% sobre o FGTS**; **aviso-prévio = 30 dias + 3/ano completo, máx. 90** (Lei 12.506/2011, citada na página); **INSS patronal ≈ 28% (20% + RAT + terceiros)** sobre remuneração reconhecida; HE "conforme prova (planilha)".

## 6. Cálculos (aritmética completa)

Remuneração-base presumida: **R$ 18.000,00/mês** — valor efetivamente pago à PJ, conforme `verbas_e_calculo.md` (presunção usual; **defesa**: se o valor embutia tributos/custos da PJ, a base seria menor — nada no arquivo demonstra isso).
Horas normais/mês: 220 (parâmetro usual; **não consta da biblioteca**). Valor-hora: 18.000/220 = **R$ 81,8182**. HE com adicional de 50% (**também usual, não constava da biblioteca** — sinalizado): **R$ 122,7273/h**.

### 6.1 Verbas exigíveis (Dez/2021–Set/2026, 58 meses)

| Rubrica | Conta | Valor (R$) |
|---|---|---|
| Salários | 58 × 18.000 | **1.044.000,00** |
| 13º | 58 × (18.000/12) = 58 × 1.500 | **87.000,00** |
| Férias + 1/3 (P3…P7, simples) | 5 × (18.000 + 6.000) | **120.000,00** |
| Base FGTS | 1.044.000 + 87.000 + 120.000 | 1.251.000,00 |
| FGTS (8%) | 8% × 1.251.000 | **100.080,00** |
| Multa 40% | 40% × 100.080 | **40.032,00** |
| Aviso-prévio indenizado | 30 + 3×7 anos = 51 d × (18.000/30 = 600) | **30.600,00** |
| INSS patronal (28%) | 28% × (1.044.000 + 87.000) | **316.680,00** |
| **Total (sem HE)** | soma das rubricas acima | **1.738.392,00** |

Advertências contábeis: INSS sobre **salários + 13º** (férias indenizadas e aviso-prévio, como indenizações rescisórias, ficaram fora da base); se a base incluir férias (leitura ampla do termo "remuneração reconhecida"), o INSS sobe para **350.280,00** e o total para **1.771.992,00**. FGTS sobre aviso indenizado (**+R$ 2.448**) e integração do aviso ao 13º **não constavam da biblioteca** e foram deixados de fora — essas omissões são conservadoras e por isso a exposição não é forçada a equilibrar. HE não tem reflexos estimados (a biblioteca não define reflexos); se constatados, sobem todas as parcelas em ~30–50%.

### 6.2 Horas extras — estimativa pela amostra e pelo termo "a apurar"

`escala_e_planilha_ponto.csv` cobre **6 meses (Jan–Jun/2025)**: 18+22+15+26+20+34 = **135 h** → **22,5 h/mês**. Consistência com as médias diárias: (9,1−8h)×21 ≈ 23 h; …; (9,8−8)×21 ≈ 38 h — mesma ordem de grandeza (26,6 h/mês → HE alternativa ≈ R$ 189.581,00; adotei a menor, a dos registros).

- HE/mês estimada: 22,5 × 122,7273 = **R$ 2.761,36**
- HE no quinquênio (58 × 2.761,36) = **R$ 160.159,09** (pela média das médias diárias em vez dos registros: **R$ 189.580,91**)
- **Total com HE: 1.738.392,00 + 160.159,09 = R$ 1.898.551,09**

Honesto e destacado: extrapolar 6 meses para 58 é **estimativa**; os demais períodos (Dez/2021–Dez/2024 e Jul/2025–Set/2026) nada produzem além da presunção de jornada (Súmula 338, vigente) — **a apurar**. No `parecer.json`, o campo `horas_extras` fica como texto ("estimativa/a apurar") e o `total` faz a soma **somente** das rubricas monetárias, para não gerar total feito de misturas numéricas/textuais.

### 6.3 Itens fora do cálculo principal (riscos adicionais)

Conforme `multa_477_e_honorarios.md` (todas vigentes):
- **Multa do art. 477 §8º:** 1 salário = **R$ 18.000** — "discutível" na reversão de pejotização (não houve rescisão formal de empregado com verbas incontroversas rescindidas); risco moderado.
- **Art. 467:** 50% sobre incontroversas — improvável em pejotização (não há verba rescisória incontroversa); risco baixo.
- **Honorários sucumbenciais (art. 791-A): 5–15%** sobre condenação: sobre R$ 1.581.871 (condenação sem INSS) = **R$ 79.094 a 237.281**.
- **INSS patronal 316.680** é exigível da empresa pela **RFB**, não é pago ao autor, mas é devido se o vínculo for reconhecido (o fisco pode lançá-lo de ofício).

### 6.4 Cenários

| Cenário | Probabilidade (est.) | Valor (R$) |
|---|---|---|
| Vínculo reconhecido; quinquênio integral + HE amostra | ~65–75% | 1.898.551,09 + multa 477 + honorários + INSS à RFB (pior caso ≈ **2.074.738**) |
| Vínculo reconhecido; verbas parciais (HE impugnadas) | ~10–15% | ~1.500.000–1.750.000 |
| Vínculo não reconhecido | ~10–15% | custas + honorários da defesa, estimados ≲ R$ 100.000 |

## 7. Provisionamento (CPC 25)

Há obrigação presente decorrente de fato passado (a prestação sob subordinação descrita acima) de cujo desfecho pode decorrer resposta financeira: pelo CPC 25, saída **provável** (>50% de chance de desembolso) obriga a **provisão**; saída **possível** obriga nota, não provisão. A estimativa central: saída esperada = 70% × exposição total estimada = 0,70 × 1.898.551,09 = **1.328.985,76** → **provisão recomendada: R$ 1.329.000 (classificação "provável")**. Cenário integral (pior caso com multa 477, honorários médios e INSS) ≈ **R$ 2,07 mi**, para fins de nota explicativa; revisão semestral ou ao decidir o Tema 1.389.

**Resposta à tese "risco zero":** a diretoria está expondo-se à condenação integral sem margem. O provisionamento não é mera obrigação contábil: ele distancia a empresa da condenação em cascata (multas, honorários, INSS à RFB) e disciplina a negociação quando o sobrestamento do Tema 1.389 terminar.

## 8. Acordo — recomendação

Economia do acordo: condenação esperada ≈ 0,7 × (1.581.871 + honorários médios ≈ 158.187 (10%) + multa 477 18.000 + INSS à RFB 316.680) ≈ **R$ 1,45 mi**, ainda sem contar tempo, correção e incerteza do Tema 1.389. **Recomendo acordo, faixa-alvo R$ 900.000–1.350.000** — piso ≈ 47% da exposição bruta; teto ≈ valor da provisão (71% da exposição). A solução em acordo deve tratar o INSS à parte (o acordo entre as partes não vincula a RFB); cláusulas de quitação ampla e emenda na CTPS se reconhecido vínculo; forma de pagamento definida. Ganhos do acordo: **evitar condenação-cascata, honorários e publicidade do processo**.

## 9. Assunções e aberturas (resumo)

1. **Encerramento da prestação em 30/09/2026** (coincide com a 9ª nota de 2026 e com a notificação extrajudicial da mesma data) — confirmar com o cliente.
2. O valor pago à PJ (R$ 18.000,00/mês) é presumido salário integral — inclusive para 13º, férias, FGTS e INSS — sem dedução de tributos/custos da PJ (defesa possível, não demonstrada no arquivo). **Na resposta de 25/10/2026 o Diretor confirmou a narrativa ("18 mil cheios", "CLT equivalente ~12 mil"), sem apresentar comprovante de destino tributário — presunção mantida; cenário defensivo quantificado em §10.**
3. HE: **extrapolação da amostra Jan–Jun/2025** para o quinquênio; períodos restantes **a apurar**; **divisor 220 e adicional de 50% aplicados por prática usual, não pela biblioteca**.
4. Reflexos de HE em 13º/férias/FGTS **não computados** (biblioteca não define).
5. Férias: **zero dias gozados** presumido; se o saldo "de 20 dias" revelar gozo, deduzir ≈ **R$ 800 por dia gozado** (600 de salário integral + 1/3). **Rev. 25/10/2026: Carla confirmou que aprovava férias "igual aos CLTs" — o gozo ocorreu, sem quantificação; cenário de dedução em §10.**
6. Aviso: 51 dias sobre base sem HE.
7. **INSS patronal sobre salários + 13º** (leitura mais ampla, com férias na base: 350.280).
8. Multa art. 477 §8º, art. 467 e honorários **fora do total** (contingências, §6.3).
9. **Rev. 25/10/2026 — sem informação adicional do cliente** (permanecem desconhecidos): registros de ponto fora da amostra; efetivo >20 empregados (Súm. 338); confirmação formal da extinção 30/09/2026; qualquer recolhimento histórico de FGTS/INSS.

## 10. Revisão pós-respostas do cliente (25/10/2026)

**Respostas recebidas.** (i) **Carla**: "Aprovava férias, cobrava horário, dava feedback. Igual aos CLTs." (ii) **Diretor**: "Os 18 mil eram 'cheios' justamente porque ele era PJ. Um CLT equivalente ganharia uns 12 mil." Para as demais perguntas, cliente não tem informação adicional.

**Efeito probatório — reforço do vínculo.** A declaração de Carla é **admissão** de que horário, aprovação de férias e avaliação de desempenho eram iguais aos dos empregados CLT — corrobora exatamente o que os documentos já indicavam (contrato itens 3–5; prints; RH). O parágrafo do Diretor confirma que a sobrevalorização da "notas" é derivada do enquadramento PJ — reconhecimento implícito de que a verba compõe contraprestação equivalente à de emprego. **A probabilidade de vínculo (65–80%) permanece "alta"; as admissões empurram a estimativa para o topo da faixa (~80%); a provisão central mantém 70% por prudência** (cenários de 65/70/80% na tabela abaixo). A tese "risco zero" da diretoria fica insustentável também pela fala da própria diretoria.

**Efeito no cálculo — nenhum no caso base.** A biblioteca (`verbas_e_calculo.md`) prescreve base = valor pago à PJ, e o pagamento mensal em 84 notas continuadas não foi discutido pelo Diretor, apenas caracterizado como "cheio". Mantém-se R$ 18.000 como base. Dois cenários de sensibilidade (ambos favoráveis à Solaris, para limitar a exposição no pior cenário defensivo):

| Cenário | Premissa | Total sem HE | Com HE estimada | Prov. @70% |
|---|---|---|---|---|
| **Base (uso no parecer)** | 18k integral; férias não gozadas | **1.738.392** | 1.898.551,09 | 1.328.986 (≈1.329.000) |
| **A — salário base 12k** (fala do Diretor) | tudo escala ×⅔; única mudança de rubrica: aviso 51×400=20.400; HE 1.305h×81,8182 | **1.158.928** (=⅔×1.738.392) | 1.265.700,73 | 885.991 |
| **B — férias gozadas 20 d/ano** (cláusula do próprio contrato + declaração de Carla) | dedução de valor de verbas absorvidas no mês de férias: 5×(20×600+⅓)=80.000; FGTS −6.400 (para 93.680); multa → 37.472 | **1.649.432** | 1.809.591,09 | 1.266.713 |

*Sensibilidade da provisão pelo nível de probabilidade (caso base):* 65% → **1.234.058** · 70% → **1.328.986 ≈ 1.329.000** (central adotada) · 80% → **1.518.841**.

*Flags de método:* os cenários A e B são **estimativas de defesa, não parâmetros da biblioteca** — em A, fixar salário base na fala do Diretor não é o que a `verbas_e_calculo.md` prescreve (base = valor pago à PJ); em B, a lógica de dedução de verbas "absorvidas" via nota continuada não consta da biblioteca (posição mais prudente: expor como defesa possível). O resultado real tende a entre ambos limites; o caso base segue sendo o fundamento do provisionamento.

**Efeito na estratégia de acordo.** A faixa de abertura **R$ 900.000–1.350.000 permanece**; com as admissões recentes, recomendo negociar mirando a **metade superior (≈R$ 1.100.000–1.350.000)**: cada mês de espera sob o sobrestamento do Tema 1.389 encarece (IPCA + SELIC-IPCA) e o risco de reviravolta do mérito (provável fixação de tese) é assimétrico.

## 11. Referências (todas em INDEX)

`clt_requisitos_vinculo.md` (art. 3º, 9º, 442-B, 818) · `cf_art7_xxix_prescricao.md` (CF 7º XXIX, CLT 11, Súm. 308, Tema 608, Lei 12.506) · `stf_tema_725_adc48_adpf324.md` · `stf_tema_1389_pejotizacao.md` (inclusive Lei 14.905/2024) · `tst_sumulas_ojs.md` (212, 331, 338, 363, 383; 256/OJ 191 canceladas — não citadas como vigentes) · `verbas_e_calculo.md` (457, 477, 487, Lei 8.036 arts. 15/18, Lei 8.212 art. 22, Lei 12.506/2011, Súm. 450/81) · `multa_477_e_honorarios.md` (467, 477 §8º, 791-A).
