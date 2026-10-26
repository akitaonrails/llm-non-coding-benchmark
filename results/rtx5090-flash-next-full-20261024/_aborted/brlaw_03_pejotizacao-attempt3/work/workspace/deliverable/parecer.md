# Parecer — Solaris Tecnologia Ltda. × Rafael Moreira (R.M. Desenvolvimento de Sistemas Ltda.)

**Assunto:** risco de reconhecimento de vínculo empregatício ("pejotização") e exposição financeira estimada.
**Data de referência:** outubro/2026. Fontes: apenas os documentos do acervo (`documents/`) e a biblioteca fechada (`library/`, conforme `library/INDEX.md`). Citações fora da biblioteca estão expressamente marcadas como **não verificadas**.

---

## 1. Resumo executivo

1. O arquivo é **fortíssimo contra a empresa**: os quatro requisitos do art. 3º da CLT estão documentados no próprio contrato e nas comunicações internas. Probabilidade de reconhecimento do vínculo: **alta (75–90%)**.
2. O "risco zero" afirmado pela diretoria com base no **Tema 725 está equivocado**: o Tema 725 (e ADPF 324/ADC 48) declara lícita a **terceirização entre pessoas jurídicas distintas**, e a própria tese mantêm a responsabilidade subsidiária da contratante; ele **não afasta** o reconhecimento de vínculo quando há, no caso concreto, os requisitos do art. 3º da CLT com fraude ao art. 9º (`library/stf_tema_725_adc48_adpf324.md`). A licitude da **pejotização** é exatamente a pergunta pendente no **Tema 1.389** do STF — com **suspensão nacional dos processos desde 14/04/2025 e mérito pendente** (`library/stf_tema_1389_pejotizacao.md`).
3. Exposição estimada (janela não prescrita de **59 meses** até 16/11/2026): **R$ 734.352**, além de horas extras a apurar (≈ R$ 16,6 mil com prova direta; ≈ R$ 163 mil por extrapolação), correção/juros e eventual sucumbência (art. 791-A). Durante a suspensão do Tema 1.389, esse valor **continua crescendo** (IPCA + SELIC−IPCA).
4. Recomenda-se: **provisionar** (classificação da obrigação: **provável**, na escala exigida pelo formato), valor de referência **R$ 734 mil** (piso); e **celebrar acordo** na faixa de **R$ 367 mil a R$ 514 mil**, antes que a correção e o risco de tese futura do STF deteriorem o resultado.
5. A tese da diretoria de que a base real seria **R$ 12 mil** (e não R$ 18 mil) é argumento de defesa reconhecido na biblioteca, mas **depende de prova que a empresa não tem**; ampliaria a banda para **R$ 407 mil a R$ 989 mil** sem alterar o ponto focal (seção 10).

---

## 2. O caso (fatos dos autos administrativos)

| Dado | Fonte |
|---|---|
| Contrato de prestação de serviços PJ com sócio único (Rafael Moreira), início 01/10/2019, prazo indeterminado | `documents/contrato_prestacao_servicos_pj.pdf` |
| Remuneração fixa de R$ 18.000/mês "independentemente de entregas" | cl. 2ª do contrato |
| Exclusividade durante a vigência | cl. 3ª |
| Horário seg–sex 9h–18h, nas dependências da contratante ou home office autorizado pelo gestor | cl. 4ª |
| Reporte ao Gerente de Engenharia | cl. 5ª |
| "Férias: 20 dias por ano, a combinar" | cl. 6ª |
| Notas fiscais: 2019 (3×R$ 54 mil), 2020–2025 (12×R$ 216 mil/ano), 2026 (9×R$ 162 mil) = 84 meses, sempre R$ 18 mil/mês | `documents/notas_fiscais_resumo.csv` |
| Controle de jornada: 21 dias/mês, média 9,0–9,8 h/dia; horas extras registradas em 2025 (18+22+15+26+20+34 = 135 h em jan–jun) | `documents/escala_e_planilha_ponto.csv` |
| Subordinação fática: cobrança de horário ("o combinado é 9h. Marca no planilha de ponto"), ordem de ficar até 20h, folga aprovada por RH com desconto de saldo, avaliação de desempenho com formulário de CLT | `documents/prints_mensagens.txt` |
| Encerramento comunicado em 30/09/2026; ajuizamento anunciado para 16/11/2026, pedindo vínculo desde 01/10/2019 | `documents/notificacao_e_email_diretoria.txt` |

---

## 3. Requisitos do art. 3º da CLT × provas (library/clt_requisitos_vinculo.md)

| Requisito | Prova no arquivo |
|---|---|
| **Pessoa física** | O "contratado" é PJ de **sócio único**; a cláusula 4ª obriga o sócio, em pessoa, a disponibilizar-se. Todo o arquivo (Slack, RH, ponto) trata Rafael individualmente. |
| **Não eventualidade** | 84 meses contínuos (01/10/2019–30/09/2026), contrato por prazo indeterminado, 12 NFs idênticas por ano, objeto permanente ("desenvolvimento e manutenção de sistemas conforme demandas"). |
| **Onerosidade (salário)** | R$ 18.000 fixos por mês **"independentemente de entregas"** — paga-se a disposição da força de trabalho, não o resultado: preço do contrato do ponto de vista trabalhista é salário. |
| **Subordinação** | (i) horário fixo e local de trabalho definidos pela tomadora (cl. 4ª); (ii) hierarquia: "reportar-se-á ao Gerente de Engenharia" (cl. 5ª); (iii) poder diretivo concreto: cobrança de login às 9h e exigência de registro em ponto (12/03/2024); (iv) jornada extraordinária por ordem do gestor (02/06/2025); (v) férias/ausências com autorização do RH e "saldo de 20 dias" — gestão de ausência como empregado; (vi) avaliação de desempenho com **o mesmo formulário dos CLTs** (05/01/2026); (vii) exclusividade (cl. 3ª), incompatível com autonomia empresarial. |

**Qualificação jurídica:** presentes os requisitos, o contrato de PJ é **nulo de pleno direito** por fraude à aplicação da CLT (art. 9º). O art. 442-B não salva a contratação: no entendimento registrado na biblioteca, ele afasta a qualidade de empregado do autônomo contínuo/com exclusividade **"desde que ausente a subordinação"** — e aqui a subordinação é documental. **Ônus da prova:** admitida a prestação pessoal do serviço, cabe à Solaris provar a autonomia (CLT art. 818; e Súmula 212 quanto ao término). A empresa não tem como prová-la — suas próprias mensagens provam o contrário.

Contra-argumentos disponíveis (fraquezas do reclamante): o contrato formal existe e foi assinado; a empresa pode tentar provar que os R$ 18.000 embutiam tributos/custos para reduzir a base (argumento de defesa registrado em `library/verbas_e_calculo.md`) — o diretor afirmou que sim, mas **sem prova documental** (análise na seção 10); ausência de provas de exclusividade fática fora da cláusula. Nada disso rompe o quadro acima. **Atenção:** a própria fala do diretor ("um CLT equivalente ganharia uns 12 mil") é admissão de que a função era equivalente a um posto CLT — útil apenas para a discussão de *base*, e contra a empresa na discussão de *vínculo*.

---

## 4. Por que o Tema 725 **não** resolve (resposta direta ao e-mail da diretoria)

O e-mail do Diretor de Operações confunde duas coisas:

1. **O que o Tema 725 decidiu** (RE 958.252, 2018; ADPF 324; ADC 48, 2020): "é lícita a terceirização ou qualquer outra forma de divisão do trabalho **entre pessoas jurídicas distintas**... **mantida a responsabilidade subsidiária da empresa contratante**" (`library/stf_tema_725_adc48_adpf324.md`). É licitude do **intermediário empresarial** — não validade de **simular autonomia** onde há subordinação real. A própria biblioteca registra que a tese "não afasta o reconhecimento de vínculo quando presentes, no caso concreto, os requisitos do art. 3º da CLT com fraude (art. 9º)".
2. **O caso concreto**: Rafael é PJ sócio único que cumpre horário, bate ponto, obedece ao gerente, tem exclusividade, folga aprovada por RH e avaliação de CLT. Isso é **pejotização** — e sua licitude é justamente a questão submetida no **Tema 1.389**, ainda **não julgada**. Ou seja: não existe hoje decisão do STF que absolva este formato; existe decisão que **suspende** os processos até que o STF responda.
3. Mesmo dentro da lógica da terceirização, a tese mantêm a **responsabilidade subsidiária** (cf. também Súmula 331, `library/tst_sumulas_ojs.md`) — não é "risco zero" nem nesse plano.

**Conclusão:** a premissa diretoria ("STF já liberou a pejotização") é **falsa**. O que o STF liberou foi a terceirização; a pejotização está sob judice, com suspensão nacional.

---

## 5. Tema 1.389 (STF, ARE 1.532.603/DF, rel. Gilmar Mendes)

(`library/stf_tema_1389_pejotizacao.md` — status da biblioteca: **congelada em out/2026: mérito pendente; suspensão mantida**)

- Repercussão geral reconhecida (abril/2025) sobre: licitude da contratação de PJ/autônomo, competência da Justiça do Trabalho e **ônus da prova da fraude**.
- **Suspensão nacional** de todos os processos sobre licitude de contratação de PJ/autônomo desde **14/04/2025**.
- **Efeito processual aqui:** a reclamação anunciada para 16/11/2026 tende a ser **sobrestada** (em geral após a instrução, antes da sentença, conforme a prática de cada TRT). O processo não morre — congela.
- **Efeito sobre a exposição:** nenhum alívio. O passivo fica em aberto **com juros e correção correndo** (Lei 14.905/2024: IPCA + SELIC−IPCA, conforme a própria decisão de suspensão descrita na biblioteca). O mérito do STF poderá fixar teses sobre fraude e ônus da prova — **incerto nos dois sentidos**: pode endurecer (validade da tese com efeitos retroativos desfavoráveis) ou ajudar a defesa; apostar nesse resultado é especulação, não gestão de risco.

---

## 6. Prescrição (CF art. 7º, XXIX; CLT art. 11; Súmula 308 — `library/cf_art7_xxix_prescricao.md`)

- **Bienal:** termino em 30/09/2026; ajuizamento anunciado em 16/11/2026 → dentro de 2 anos. **Não há prescrição total.** (Prazo correria até 30/09/2028; a defesa tem interesse em que qualquer acordo/ajustamento preserve a data de término.)
- **Quinquenal:** corte em **16/11/2021** (5 anos contados **do ajuizamento** — Súmula 308).
  - Vínculo: 01/10/2019 a 30/09/2026 = **84 meses** (confere com as NFs: 3 + 6×12 + 9 = 84).
  - **Meses exigíveis (não prescritos): 59** → nov/2021–dez/2021 (2) + 2022–2025 (48) + jan–set/2026 (9).
  - **Meses prescritos: 25** → out/2019–out/2021 (3 + 12 + 10).
  - *Premissa*: crédito de novembro/2021 considerado exigível após 16/11/2021 (salário pago ao fim do mês/início do seguinte). Se o ajuizamento atrasar até 16/12/2026, a janela cai para 58 meses (≈ R$ 12 mil a menos). O pedido do reclamante (vínculo "desde 01/10/2019 com todas as verbas") **não vale** contra a Súmula 308: os 25 primeiros meses estão fulminados.
- **Aviso-prévio proporcional** considera o **tempo total de serviço** (84 meses), ainda que parte das verbas esteja prescrita (`library/cf_art7_xxix_prescricao.md`) — por isso ele é calculado sobre os 7 anos completos, não sobre a janela.

---

## 7. Exposição — cálculo (parâmetros de `library/verbas_e_calculo.md`)

**Base:** remuneração mensal = R$ 18.000,00 (valor pago à PJ — presunção usual da Justiça do Trabalho registrada na biblioteca; defesa pode tentar reduzi-la provando tributos/custos embutidos).

Janela de cálculo = **59 meses** (salvo aviso-prévio, que usa o tempo total).

| Verba | Aritmética | Valor (R$) |
|---|---|---:|
| Remuneração-base (base de cálculo da janela) | 18.000 × 59 | **1.062.000** |
| 13º salários (1/12 por mês) | 18.000 × 59/12 = 18.000 × 4,9167 (= 4 inteiros + 2/12 de 2021 + 9/12 de 2026) | **88.500** |
| Férias + 1/3 (simples, por determinação da biblioteca) | 18.000 × 59/12 = 88.500; terço = 88.500/3 = 29.500 | **118.000** |
| FGTS 8% sobre salários + 13º + férias com 1/3 | 0,08 × (1.062.000 + 88.500 + 118.000) = 0,08 × 1.268.500 | **101.480** |
| Multa 40% sobre FGTS (Lei 8.036/90 art. 18) | 0,40 × 101.480 | **40.592** |
| Aviso-prévio proporcional (30 + 3×anos completos; Lei 12.506) | 7 anos completos → 30+21 = 51 dias (≤90 ✓); 18.000 × 51/30 | **30.600** |
| INSS patronal ≈ 28% (20% + RAT + terceiros, Lei 8.212/91 art. 22) sobre remuneração reconhecida | 0,28 × (1.062.000 + 88.500 + 118.000) = 0,28 × 1.268.500 | **355.180** |
| **Total dos créditos** | 88.500 + 118.000 + 101.480 + 40.592 + 30.600 + 355.180 | **734.352** |

**Como ler o campo "remuneracao_base" (R$ 1.062.000): é a base de cálculo, não um acréscimo de caixa.** Os R$ 18 mil/mês já foram pagos a Rafael via NFs; na reversão, os salários são compensados com o já pago (não há pagamento em duplicidade) — o que pesa no caixa são os **reflexos/créditos adicionais** acima, que compõem o total de R$ 734.352. Se, num cenário extremado, um juízo não compensasse os valores pagos, a exposição subiria para 1.062.000 + 734.352 = **R$ 1.796.352**; é cenário improvável e não o que recomendamos provisionar, mas convém que a diretoria o conheça.

**Itens fora do total (abertos de propósito, conforme a biblioteca):**

- **Horas extras** ("conforme prova (planilha)"): a planilha só cobre jan–jun/2025 (dentro da janela): 135 h. Com hora a 18.000/220 = R$ 81,82 e adicional de 50% (divisor e adicional **não constam da biblioteca — premissas não verificadas**): 135 × R$ 122,73 ≈ **R$ 16.568** com prova direta. Extrapolar a média de 22,5 h/mês aos 59 meses (≈1.328 h) dá ≈ **R$ 162.920**. A planilha ser da própria tomadora reforça a materialidade das HE; a extensão aos demais anos depende de prova pericial/testemunhal (cf. Súmula 338 sobre controle de jornada).
- **Multas dos arts. 467 e 477 §8º** (R$ 18.000 a multa do 477; 467 = 50% sobre incontroversas): "discutíveis na reversão de pejotização" (`library/multa_477_e_honorarios.md`) — não somadas, mas potencialmente devidas (~R$ 18–50 mil).
- **Honorários sucumbenciais** 5–15% (CLT art. 791-A): sobre R$ 734 mil ≈ **R$ 37–110 mil** se sucumbente.
- **Correção/juros** durante o sobrestamento do Tema 1.389 (IPCA + SELIC−IPCA) — materializam o custo do tempo.
- **FGTS:** a biblioteca simplifica (incide sobre salários + 13º + férias com 1/3, sem distinção de férias indenizadas) — adotado tal qual; divergência possível para menos, não apurada.

**Cenários** (sem horas extras; sem juros):

| Cenário | Total |
|---|---:|
| Férias já gozadas compensam (deve-se só o terço): 13º 88.500 + terço 29.500 + FGTS 0,08×1.180.000 = 94.400 + 40% 37.760 + aviso 30.600 + INSS 0,28×1.180.000 = 330.400 | **611.160** |
| **Base recomendada (tabela acima)** | **734.352** |
| Base + HE extrapoladas (162.920) + multa 477 (18.000) + honorários médios 10% (73.435) | **≈ 988.707** |
| Sem compensação dos valores pagos às NFs (extremo) | 1.796.352 + acessórios |

A banda relevante de planejamento era **R$ 610 mil a R$ 990 mil**; com a resposta do cliente sobre a base (seção 10), ela passa a **R$ 407 mil a R$ 989 mil**, permanecendo o **ponto focal provisionado em R$ 734 mil** (presunção da biblioteca, não elidida por prova).

---

## 8. Estratégia recomendada

1. **Corrigir a premissa da diretoria por escrito** (este parecer): Tema 725 ≠ pejotização; hoje há **suspensão nacional** e mérito incerto. "Não provisionar" é decisão tomada sobre fato jurídico inexistente.
2. **Provisionar**: obrigação de saída mais provável do que não — classificação **"provável"** na escala pedida pelo formato (nota: a norma de contingências — CPC/NBC TG 25 — não integra a biblioteca; a classificação usa a probabilidade jurídica apurada acima). Valor de referência: **R$ 734.352** (piso), revisando mensalmente pela correção.
3. **Acordar: SIM.** Faixa recomendada: **R$ 367 mil a R$ 514 mil** (50–70% da exposição focal). Racional: (i) probabilidade de perda alta; (ii) a suspensão do Tema 1.389 **aumenta** o valor final pela correção e impede "virar a página"; (iii) o resultado do mérito do STF é incerto nos dois sentidos; (iv) um acordo bem estruturado (extensão da quitação e formalização a definir — normas processuais aplicáveis não constam da biblioteca) deve ser feito **antes** do julgamento do Tema 1.389, enquanto a incerteza ainda valoriza a transação para os dois lados.
4. **Preservar prova e limites**: sustentar a data de término 30/09/2026 (evita risco de prorrogação fática); sustentar prescrição quinquenal (corte 16/11/2021, 25 meses fulminados); explorar o argumento de que os R$ 18.000 embutiam tributos/custos para atacar a base; contestar HE além de 2025 (falta de prova) e as multas de 467/477.
5. **Revisar o modelo para os demais PJs**: os prints revelam política generalizada de subordinação sobre contratados PJ ("avaliação de desempenho dos PJs... mesmo formulário dos CLTs"). Se há outros casos, o risco não é um — é uma carteira. (Fora do escopo deste cálculo.)

**Súmulas/OJs não invocadas:** não se citam, como vigentes, a **Súmula 256** e a **OJ SDI-1 nº 191**, ambas **canceladas** (`library/tst_sumulas_ojs.md`); qualquer defesa ou petição que as utilize conteria erro grosseiro.

---

## 9. Premissas e pontos abertos (repetido aqui para destaque)

1. Ajuizamento em **16/11/2026** (data anunciada na notificação) — prescrição recalculada se atrasar; cada mês de atraso acrescenta ≈ R$ 12 mil à janela.
2. Término do vínculo em **30/09/2026** (data da notificação; cláusula 7ª previa aviso de 30 dias — se houver projeção do aviso, meses exigíveis e aviso mudam marginalmente).
3. Férias **simples** (sem dobra), incidência de FGTS sobre salários+13º+férias com 1/3, INSS ≈ 28% (RAT/terceiros não individualizados) — tudo conforme simplificação da própria biblioteca.
4. Horas extras: divisor 220 h e adicional 50% **não verificados na biblioteca**; extrapolação da média de 2025 é premissa.
5. Extensão da janela dos créditos proporcionais (13º e férias) tratada por 59/12 avos — simplificação; férias efetivamente gozadas (cl. 6ª / e-mail RH) podem reduzir a rubrica de férias ao terço (cenário R$ 611.160).
6. Perguntas específicas em `PERGUNTAS.md`: houve **uma única resposta** do cliente (a da base de cálculo — analisada na seção 10); para as demais, o cliente informou não ter mais informações. Os desconhecidos remanescentes estão sinalizados na seção 10.5 e em `PERGUNTAS.md` (não serão repetidos).

---

## 10. Resposta do cliente — a tese da base de R$ 12.000 (atualização)

**Resposta recebida (Diretor de Operações):** *"Os R$ 18 mil eram 'cheios' justamente porque ele era PJ. Um CLT equivalente ganharia uns 12 mil."* Para as demais perguntas, o cliente informou **não ter mais informações**.

### 10.1 Enquadramento jurídico da tese

A biblioteca admite o argumento: base = **valor pago à PJ** (presunção usual da Justiça do Trabalho), *"salvo prova de que embutia tributos/custos — argumento de defesa"* (`library/verbas_e_calculo.md`). Ou seja: a alegação **desloca para a Solaris o encargo de provar** (guias de DAS, extratos bancários da PJ, notas de custos, contabilidade) que os R$ 18.000 embutiam tributos/custos. **Nada disso existe no acervo.** E o acervo aponta em sentido contrário à tese:

- cl. 2ª: preço fixo **"independentemente de entregas"** — não há repasse de risco de resultado ao PJ;
- férias eram **gozadas com pagamento integral**: as 12 NFs de R$ 216 mil/ano se repetem em todos os anos do contrato, e o RH geria "saldo de 20 dias" — o PJ não arcou com custo de inatividade;
- nenhuma estrutura da PJ aparece no arquivo (sem empregados, equipamentos ou escritório; o sócio executa pessoalmente tudo, cl. 4ª).

Sem prova documental, a presunção (R$ 18.000) prevalece. **Decisão: o valor focal do parecer — e o `parecer.json` — permanece R$ 734.352**; a tese de R$ 12.000 entra como **cenário baixo**, não como premissa.

### 10.2 A conta com base R$ 12.000 (mesma janela de 59 meses, mesmos parâmetros da seção 7)

| Verba | Aritmética | Valor (R$) |
|---|---|---:|
| Remuneração-base (base de cálculo) | 12.000 × 59 | 708.000 |
| 13º salários | 12.000 × 59/12 | 59.000 |
| Férias + 1/3 | 59.000 + 59.000/3 (= 19.666,67) | 78.666,67 |
| FGTS 8% | 0,08 × (708.000 + 59.000 + 78.666,67) = 0,08 × 845.666,67 | 67.653,33 |
| Multa 40% FGTS | 0,40 × 67.653,33 | 27.061,33 |
| Aviso-prévio (51 dias) | 12.000 × 51/30 | 20.400 |
| INSS patronal 28% | 0,28 × 845.666,67 | 236.786,67 |
| **Total dos créditos** | 59.000 + 78.666,67 + 67.653,33 + 27.061,33 + 20.400 + 236.786,67 | **489.568,00** |

Variante **12k + férias gozadas compensam (deve-se só o terço)**: 13º 59.000 + terço 19.666,67 + FGTS 0,08 × 786.666,67 = 62.933,33 + 40% 25.173,33 + aviso 20.400 + INSS 0,28 × 786.666,67 = 220.266,67 → **R$ 407.440,00** (piso do caso).

HE na base 12k (mesmas premissas **não verificadas** — divisor 220 h e adicional 50%): 1.327,5 h × (12.000/220) × 1,5 ≈ **R$ 108.614** (extrapolada).

### 10.3 Por que a comparação "PJ 18 mil × CLT 12 mil" não ajuda a empresa

- **A comparação é desequilibrada.** Pelos parâmetros da própria biblioteca, um CLT de R$ 12.000 custaria ≈ R$ 19.500/mês à tomadora (salário + 13º + férias c/ 1/3 + FGTS 8% + INSS 28%) — **acima** dos 18 mil pagos à PJ. A "economia" do formato veio de suprimir acessórios trabalhistas, exatamente o traço de fraude (art. 9º) que o reclamante explora.
- **Para o cálculo trabalhista, base é o que remunerava o trabalho**: R$ 18.000 recebidos todo mês como única contraprestação (ele não tinha 13º, férias, FGTS ou INSS próprios). Os tributos/custos da PJ **não estão quantificados no acervo** — e alíquotas de Simples/DAS **não constam da biblioteca** (não verificáveis aqui).
- **Admissão perigosa**: afirmar que "um CLT equivalente ganharia uns 12 mil" admite que a função **corresponde a um posto CLT interno** — argumento útil ao reclamante no mérito do vínculo. Recomendação: **não sustentar a tese da base em contestação ou depoimento sem lastro documental**; se a direção quiser levá-la adiante, que antes instrua o processo com extratos/DAS/custos da PJ.

### 10.4 Cenários consolidados (sem HE; sem correção monetária)

| Cenário | Total (R$) |
|---|---:|
| Base 12k + férias gozadas compensam (melhor caso da empresa — exige prova hoje inexistente) | **407.440** |
| Base 12k aceita integralmente (redução provada) | 489.568 |
| Base 18k + férias gozadas compensam | 611.160 |
| **Focal: base 18k (presunção da biblioteca, não elidida)** | **734.352** |
| Focal + HE extrapoladas (162.920) + multa 477 (18.000) + honorários médios 10% (73.435) | ≈ **988.707** |

**Banda de planejamento: R$ 407 mil – R$ 989 mil; focal inalterado em R$ 734.352.** Provisão (**provável**, R$ 734.352) e faixa de acordo (**R$ 367–514 mil**) permanecem: o reclamante tem a presunção a seu favor e ancorará a negociação em ~R$ 734 mil; a tese da base, **se um dia provada**, é teto de defesa, não chão de acordo.

### 10.5 Desconhecidos que permanecem (cliente sem mais informações — sinalizados, sem repetir perguntas)

1. **Data real do término** (opera-se com 30/09/2026) **e do ajuizamento** (16/11/2026); ajuizamento mais tarde encurta a janela (≈ −R$ 12 mil/mês na base 18k).
2. **Férias efetivamente gozadas (2019–2025)**: pode cortar até ≈ **R$ 123 mil** (base 18k) ou ≈ **R$ 82 mil** (base 12k) do total.
3. **Pontos/planilhas fora de jan–jun/2025**: HE entre ≈ R$ 16,6 mil (prova direta) e ≈ R$ 163 mil (extrapolação), na base 18k.
4. **Estrutura/custos da PJ** (DAS, contabilidade, extratos): **única peça capaz de dar efeito prático à tese da base**; sem ela, a alegação dos 12 mil não chega ao processo com valor probatório.
5. **Nº de empregados e RAT/terceiros reais** da Solaris (INSS adotado ≈ 28%, conforme a biblioteca).
6. **Eventuais outros contratos PJ idênticos** (os prints sugerem política generalizada): risco de carteira, fora deste cálculo.

*Todas as citações deste parecer apontam para arquivos indexados em `library/INDEX.md`. Itens marcados "não verificados" não constam da biblioteca e estão sinalizados como premissas.*
