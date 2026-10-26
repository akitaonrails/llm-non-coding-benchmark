# Parecer — Abertura "Clínica Estética Aurora"

**Confidencial — versão 2, incorpora as respostas do cliente.** Elaborado exclusivamente com base na biblioteca fechada `library/` (vide `library/INDEX.md`) e nos documentos de `documents/`. Afirmações sem correspondente na biblioteca estão marcadas **[NÃO VERIFICADO]**. Premissas proeminentes na §9; desconhecidos remanescentes registrados em `QUESTIONS.md`.

**O que muda da v1:** (i) aluguel real dos 40% conhecido — **R$ 8.000/mês a um dentista**; (ii) confirmado: **casados em 2010, comunhão universal, sem pacto** → vedação do CC art. 977 confirmada; (iii) **Luana não tem dinheiro** para aportar; (iv) **Marina quer ser cotista** e propõe administrar "fora do expediente" — respondido diretamente na §1.1. Configuração societária recomendada atualizada (§1.2 e §7); números recalculados (aritmética na §6 e em `numeros.json`).

## Sumário executivo

| Item | Veredicto |
|---|---|
| Marina (servidora federal) como **cotista** | **Pode** — exceção expressa do art. 117, X da Lei 8.112/90 (`library/lei8112_art117.md`). Mas **não junto com Felipe** no mesmo quadro (CC art. 977): se ela entra, ele sai |
| Marina como **administradora**, "fora do expediente" | **Proibido.** A vedação alcança a **função**, não o horário: "participar de gerência ou administração" (art. 117, X) não tem exceção por turno. A exceção legal é ser **cotista**, não gerir |
| Marina **e** Felipe cotistas juntos | **Impedidos** — CC art. 977; fato **confirmado** pelo cliente: casamento 2010, comunhão universal, sem pacto (`library/cc_sociedade_limitada.md`) |
| **Felipe administrador não sócio** | **Admitido** — CC arts. 1.060/1.061 (`library/cc_sociedade_limitada.md`) |
| **Configuração recomendada** (desejo de Marina atendido) | Quadro: **Marina 80% + Luana 20%**; administração com **Felipe (não sócio)**; Marina jamais pratica ato de gestão |
| Luana 20% "pelo trabalho" | **Proibido** — CC art. 1.055, §2º veda contribuição em serviços. Sem dinheiro dela: quotas **adquiridas por cessão** do casal (onerosa parcelada ou doação — §3); o trabalho dela é pago com **pró-labore**, não com capital |
| Aluguel ao dentista (R$ 8.000/mês) | R$ 96.000/ano ≈ **8% da receita** — não ativa a preponderância imobiliária do ITBI (§4.2); o dentista deve operar com **CNPJ e CRO próprios**, sem usar o CNPJ/estrutura da Aurora (§5) |
| Imóvel integralizado a **R$ 420.000** (valor de declaração), 100% creditado ao capital | **Recomendado** — ganho de capital PF **R$ 0** (Lei 9.249/95, art. 23, `library/lei9249_art23.md`); a valor de mercado R$ 900.000 geraria ganho de R$ 480.000 |
| ITBI na integralização | **Imune** no limite do capital creditado (CF art. 156, §2º, I; CTN arts. 36/37; Tema 796/STF — `library/cf156_ctn37_itbi.md`), sob condição resolutiva de preponderância por 3 anos — margem agora folgada (§4.2) |
| "Pró-labore zero, tudo lucro isento" | **Inviável** — SC COSIT 120/2016: a totalidade pode ser reclassificada como pró-labore para INSS (`library/pro_labore_inss.md`) |
| Retirada pretendida de **R$ 50.000/mês** pelo casal | **Não cabe no lucro**: sustentável ≈ **R$ 25.000/mês** (R$ 20.000 lucros de Marina + R$ 5.000 de Felipe administrador). Fenda de R$ 25.000/mês **deixada aberta**, não reconciliada (§6.3) |
| IRRF sobre distribuição 2026 | **R$ 0/mês** — nenhum beneficiário recebe > R$ 50.000/mês da mesma PJ (Lei 15.270/2025, `library/lei15270_dividendos_2026.md`) |
| Simples Nacional **como desenhado** (PJ dona do imóvel, alugando 40% ao dentista) | **Impossível** — LC 123/2006, art. 17, XV (`library/lc123_vedacoes.md`) |
| Simples Nacional **reestruturado** (Cenário B: imóvel fora da PJ; CNAE único 9602-5/02) | **Viável** — §7; vedações remanescentes não confirmadas (desconhecidos U2/U5, §9) |
| CNAE 8630-5/04 (odontologia) | **Excluir** — sem responsável técnico com CRO; quem administra CRO é o dentista locatário, com CNPJ próprio |
| Não concorrência "para sempre, Brasil inteiro" | **[NÃO VERIFICADO]** — sem fonte na biblioteca; prática: escopo temporal/territorial limitado (~2 anos, Município-sede) |
| Quotas preferenciais de Marina | No desenho novo Marina **é** cotista, logo preferências são admitidas (IN DREI 81/2020, `library/cc_sociedade_limitada.md`) porém **inócuas** (detém 80%); jamais podem conferir gestão (Lei 8.112) |
| Aritmética da minuta | **Quebrada**: 150.000 + 900.000 quotas = 100% do capital; os 20% de Luana (210.000 quotas) não têm lastro — corrigida em `contrato_social_ajustado.md` |

---

## 1. Quadro societário — fatos confirmados e desenho recomendado

### 1.1 Marina: cotista sim; administradora não — nem "fora do expediente"
Pergunta da cliente: *"Posso ser sócia, né? Administrar eu faria fora do expediente."*

- **Cotista: sim.** A Lei 8.112/90, art. 117, X proíbe ao servidor "participar de **gerência ou administração** de sociedade privada, personificada ou não personificada, exercer o comércio, **exceto na qualidade de acionista, cotista ou comanditário**" (`library/lei8112_art117.md`). Participação puramente patrimonial — subscrever quotas, votar em atos de sociedade, receber lucros — está dentro da exceção expressa. Receber lucros não é retribuição por trabalho.
- **Administradora: não — e o horário é irrelevante.** A vedação incide sobre a **função** ("participar de gerência ou administração"), sem restrição de turno; "fora do expediente", em férias ou recessão **não convalida** nada — a exceção legal é a qualidade de cotista, não a gestão em horário alternativo. O mesmo valeria para "administradora de fato": praticar atos de gestão sem nomeação formal cai na mesma proibição **[sanções disciplinares e consequências dos atos: NÃO VERIFICADO — a biblioteca traz apenas a literalidade do art. 117, X]**.
- A vedação de "exercer o comércio" também não a alcança como cotista (mesma exceção). A atividade da Aurora é estética (serviço) e, no Cenário A, locação — não comércio **[classificação: NÃO VERIFICADO]**.
- **Consequência prática:** cláusula expressa de vedação no contrato (Cl. 5ª do texto ajustado) e governança que a mantenha fora de qualquer ato de gestão (contas, contratos, folha, alvarás).

### 1.2 Comunhão universal confirmada — CC art. 977
O cliente confirmou: casamento em 2010, **comunhão universal de bens, sem pacto**. O CC art. 977 faculta aos cônjuges contratar sociedade "desde que **não tenham casado no regime da comunhão universal de bens**" (`library/cc_sociedade_limitada.md`). Tradução prática: **o casal não pode compor o mesmo quadro societário** **[leitura assentada; a biblioteca traz a literalidade — NÃO VERIFICADO quanto à hipótese de um só cônjuge com terceiro, embora seja a interpretação corrente]**. Conclusão: **exatamente um** dos dois no quadro.

**Configuração recomendada (v2 — desejo de Marina atendido):**

| Posição | Quem | Base |
|---|---|---|
| Cotista — 80% | **Marina** | Exceção "cotista", art. 117, X (`library/lei8112_art117.md`) |
| Cotista — 20% | **Luana** | Cessão de quotas do casal (§3; CC 1.055 §2º impede "sócia de trabalho") |
| Administrador — **não sócio** | **Felipe** | CC arts. 1.060/1.061 (`library/cc_sociedade_limitada.md`) |

A economia familiar não muda: sob comunhão universal, quotas e lucros integram o patrimônio comum do casal em qualquer caso **[regra do regime de bens: NÃO VERIFICADO — fora da biblioteca]**; a escolha é formal. Alternativa equivalente (v1): **Felipe** cotista+administrador e Marina fora do quadro — minimize qualquer discussão sobre servidor no quadro, mas contraria o desejo declarado dela. Ambas cumprem 977 e 117, X.

Alertas da configuração "Marina no quadro": (i) **Simples Nacional**: o trecho da biblioteca (LC 123, art. 17) não arrola vedação a servidor cotista **[NÃO VERIFICADO — confirmar no texto integral/local, desconhecido U5]**; (ii) **conflito de interesses**: Marina é analista federal da área de saúde — regras internas do órgão, declaração de conflito e eventual compatização com a participação em clínica do setor regulado **[NÃO VERIFICADO — fora da biblioteca; desconhecido U6]**; (iii) transferência de bem comum do casal para sociedade de que só a esposa participa — a biblioteca não trata de regras de disposição entre cônjuges **[NÃO VERIFICADO]**.

### 1.3 O imóvel é do casal
A matrícula 118.442 registra Felipe "casado em comunhão universal com Marina" (`documents/matricula_imovel_excerto.md`): bem comum. Qualquer disposição — integralização (Cenário A) ou locação pelo casal (Cenário B) — exige a intervenção/anuência de **ambos** **[outorga conjugal/regras de administração: NÃO VERIFICADO — fora da biblioteca]**. No desenho recomendado, Felipe atua como locador/administrador meeiro, nunca como sócio junto com a esposa.

## 2. Quem administra
**Felipe Costa, administrador não sócio** (CC arts. 1.060/1.061, `library/cc_sociedade_limitada.md`), com remuneração própria (Cl. 8ª do texto ajustado; §6.2). Marina **não** administra, **não** trabalha na sociedade e **não** recebe pró-labore: pró-labore pressupõe trabalho (`library/pro_labore_inss.md`), e trabalhar na sociedade é precisamente o que a Lei 8.112 veda — qualquer valor pago a ela "por trabalho" seria, em si, o ato proibido **[consequências: NÃO VERIFICADO]**. Se preferirem o desenho v1 (Felipe cotista+administrador), nada muda nestes termos.

## 3. Dra. Luana — sem dinheiro: o trabalho não vira capital; quotas viram por **cessão**
- CC art. 1.055, §2º: **"É vedada contribuição que consista em prestação de serviços"** (`library/cc_sociedade_limitada.md`). A pretensão de Luana ("meu trabalho vale 20%") **não se converte em integralização** — a Cláusula 3ª da minuta, nesse ponto, faz a Junta rejeitar o registro **[prática de exame: NÃO VERIFICADO]**.
- Confirmado pela cliente que ela **não tem dinheiro** para aportar. O caminho lícito inverte a origem: o capital é 100% subscrito e integralizado **pelo casal** (dinheiro comum; no Cenário A, também o imóvel), e Luana **adquire 20% das quotas por cessão** do quinhão de Marina:
  - **(a) Cessão onerosa com pagamento diferido** — preço em R$ com nota particular de pagamento parcelado entre Marina e Luana (ela quita com o próprio pró-labore/lucros). Capital da sociedade fica 100% integralizado desde logo; a dívida é **pessoal**, entre sócios, sem efeito no caixa social. Preço a valor contábil (R$/quota = 1) → sem ganho aparente **[regras de ganho de capital na cessão de quotas PF: NÃO VERIFICADO — fora da biblioteca]**. **Recomendada.**
  - **(b) Doação de quotas** — custo zero para Luana; atrai **ITCMD** e reflexos de IR do doador **[regras: NÃO VERIFICADO — fora da biblioteca; desconhecido U5]**.
  - **(c) Inviáveis:** integralização em serviços (vedada) ouLuana subscrever sem integralizar (quotas não integralizadas geram responsabilidade solidária **[alcance: NÃO VERIFICADO]** — CC art. 1.055 exige integralização; a biblioteca não detalha sanção).
- **Valores por cenário** (aritmética §7): Cenário A — capital **R$ 570.000** (R$ 150.000 dinheiro + R$ 420.000 imóvel), 20% = **R$ 114.000** em quotas (114.000 quotas de R$ 1,00); Cenário B — capital **R$ 150.000**, 20% = **R$ 30.000**. O trabalho de Luana (biomédica esteta) é remunerado por **pró-labore/contrato de serviços** (§6.2) — esse é o lugar lícito do "trabalho" na LTDA.
- O momento/mecanismo da cessão no registro (instrumento próprio na constituição × alteração logo após; exigências da Junta) **[NÃO VERIFICADO — prática de registro fora da biblioteca; desconhecido U8]**.
- Subsiste o vício aritmético da minuta (210.000 quotas órfãs): 150.000 + 900.000 quotas já = 100% do capital de R$ 1.050.000, sem lastro para os "20%" de Luana. Corrigido em `contrato_social_ajustado.md`.

## 4. Integralização do imóvel — valor, ganho de capital e ITBI (Cenário A)
**Aritmética** (`documents/questionario_abertura.md`; `documents/matricula_imovel_excerto.md`): valor de mercado R$ 900.000; valor na declaração de IR / aquisição 2016: R$ 420.000.

### 4.1 Valor a atribuir (Lei 9.249/95, art. 23 — `library/lei9249_art23.md`)
| Opção | Base | Ganho de capital da PF |
|---|---|---|
| **(Recomendada)** Valor da declaração | R$ 420.000 | **R$ 0** |
| Valor de mercado | R$ 900.000 | **R$ 480.000** (900.000 − 420.000), tributável como ganho de capital **[alíquotas 15–22,5%: NÃO VERIFICADO — fora da biblioteca; ≈ R$ 72.000–108.000, estimativa NÃO VERIFICADA]** |

Pelo CC art. 1.055, §1º, todos os sócios respondem **solidariamente pela exata estimação** dos bens conferidos ao capital, **até 5 anos do registro** (`library/cc_sociedade_limitada.md`): documentar a valoração (declaração de IR; laudo). Creditar acima do valor integralizado não é solução: cria excesso tributável de ITBI (Tema 796, abaixo).

### 4.2 ITBI (CF art. 156, §2º, I; CTN arts. 36–37; Tema 796 — `library/cf156_ctn37_itbi.md`)
- **Regra:** não incide ITBI na transmissão de bens ao patrimônio de PJ **em realização de capital**.
- **Tema 796/STF (RE 796.376):** a imunidade **não alcança o valor que exceder o limite do capital social a ser integralizado**. No desenho recomendado, o imóvel entra por **R$ 420.000 integralmente creditados ao capital** → base imune R$ 420.000; **base tributável R$ 0**. Se entrasse por R$ 900.000 com parte creditada a reservas, o excesso de R$ 480.000 seria tributável; se creditasse tudo ao capital, o ITBI seria imune, mas a PF pagaria o ganho de R$ 480.000 — as duas opções não são compatíveis, e a barata é a primeira.
- **Preponderância (CF §2º, I; CTN art. 37 — PJ nova, 3 anos seguintes):** com o aluguel **real** informado — **R$ 8.000/mês ao dentista = R$ 96.000/ano** — a renda locatícia representa **8,0%** dos R$ 1.200.000 projetados (ou **7,4%** se somada à receita: 96.000 ÷ 1.296.000). A exceção só se ativaria se a receita de estética caísse abaixo de ~R$ 96.000/ano **[~92% de queda]** — margem folgadíssima sobre a projeção. Veredito: **ITBI devido = não (base 0)**, sob monitoramento de 3 anos.
- **Alerta:** repercussão geral pendente sobre o alcance da exceção na integralização (RE 1.495.108); a biblioteca adota a redação literal de CF/CTN **[desfecho: NÃO VERIFICADO]**.
- **No Cenário B** não há transmissão onerosa nem ITBI; os R$ 96.000/ano de aluguel do dentista ficariam com o **casal (PF)** — tributação do locador pessoa física e retenções **[NÃO VERIFICADO — fora da biblioteca]**.

## 5. Regime tributário e CNAEs (`library/lc123_vedacoes.md`)
1. **Cenário A: sem Simples.** A PJ locadora de imóvel próprio atrai a vedação do art. 17, XV da LC 123/2006 — **independe do inquilino ser dentista** (a exceção do dispositivo é para serviços tributáveis pelo ISS; locação de sala própria não é **[qualificação: NÃO VERIFICADO]**). Por isso `numeros.json` responde `simples_possivel=false` **no desenho pretendido** (imóvel na PJ + aluguel de 40%).
2. **O dentista locatário:** deve contratar a sala com **CNPJ próprio e licença/CRO próprios**, em nome dele — a Aurora **não** pode prestar, subcontratar ou "emprestar estrutura" (recepcionista, maca, CNPJ) a serviço da atividade odontológica sem responsável técnico inscrito no CRO; o trecho da biblioteca sobre CNAE 8630-5/04 indica que atividade odontológica exige habilitação própria ("não é o caso" de Luana, biomédica) **[consequências de operar sem RT/CRO: NÃO VERIFICADO]**. Recomendação: contrato de locação autônomo (casal→dentista no Cenário B; PJ→dentista no A), sem compartilhamento de pessoal/estrututra além da sala, e verificação de alvará do dentista **[NÃO VERIFICADO — licenças fora da biblioteca]**.
3. **8630-5/04 (odontologia) no CNPJ da Aurora: excluir.** Sem RT com CRO no quadro/equipe.
4. **9602-5/02 (estética): mantido** — Anexo III. **[Habilitação do biomédico esteta/conselho: NÃO VERIFICADO — desconhecido U3.]**
5. **Cenário B (imóvel fora da PJ, CNAE único 9602-5/02): Simples Anexo III viável**, ressalvadas as demais vedações do art. 17 (ex.: participação em outra optante — cliente **não pôde confirmar**, U2; teto ME/EPP para R$ 1,2 mi/ano **[NÃO VERIFICADO]**; servidor federal como cotista — não arrolado no trecho da biblioteca **[NÃO VERIFICADO]**).
6. No Simples Anexo III a **patronal está no DAS**; permanece a **retenção de 11%** do pró-labore do segurado (`library/pro_labore_inss.md`). No Lucro Presumido (Cenário A), soma-se **patronal de 20%** sobre o pró-labore. **[Alíquotas efetivas: NÃO VERIFICADO — fora da biblioteca; não calculadas.]**

## 6. Pró-labore e distribuição em 2026
### 6.1 Por que "pró-labore zero" não funciona
`library/pro_labore_inss.md`: quem presta serviço à sociedade (administra **ou trabalha**) é contribuinte individual obrigatório; pela **SC COSIT 120/2016**, trabalhando e distribuindo-se valores **sem pró-labore**, a totalidade pode ser reclassificada como pró-labore para fins previdenciários. Aqui, dois trabalham (Felipe administra; Luana atende) — retirar tudo "de lucro" expõe a sociedade a INSS patronal 20% + retenção 11% + adicionais **[base/multas: NÃO VERIFICADO]** sobre R$ 600.000/ano, e IRRF sobre o reclassificado.

### 6.2 Pró-labore recomendado (mensal) — **premissa, sem fonte na biblioteca**
| Pessoa | Papel | Pró-labore | Fundamento |
|---|---|---|---|
| Marina | Cotista — **não pode trabalhar** | **R$ 0** | Trabalhar seria o ato vedado (Lei 8.112, art. 117, X); não há serviço a remunerar |
| Felipe | Administrador **não sócio** | **R$ 5.000** **[premissa]** | Remuneração de administrador; CI obrigatório **[a literalidade da biblioteca trata do sócio que administra/trabalha; administrador não sócio como CI: NÃO VERIFICADO — regra geral da Lei 8.212 fora do acervo]** |
| Luana | Biomédica esteta | **R$ 5.000** **[premissa]** | Sócia que trabalha = CI (`library/pro_labore_inss.md`); compatível com Fator R **[NÃO VERIFICADO]** |

Benchmarks de mercado são **desconhecido U4** (cliente não forneceu). INSS com pró-labore de R$ 5.000: retenção 11% = **R$ 550/mês/pessoa**; patronal 20% = **R$ 1.000/mês/pessoa** fora do Simples (dois remunerados → R$ 2.000/mês no Lucro Presumido; no Anexo III, no DAS).

### 6.3 Distribuição — a fenda de R$ 50.000 continua aberta
Lucro projetado R$ 420.000/ano = R$ 35.000/mês; menos pró-labore (5.000 + 5.000) × 12 = R$ 120.000 → **remanescente ≈ R$ 300.000/ano = R$ 25.000/mês** **[efeitos de IRPJ/CSLL/DAS: NÃO VERIFICADO — alíquotas fora da biblioteca]**. Pro rata do quadro novo (Marina 80% / Luana 20%):

| Beneficiário | Pró-labore | Lucros/mês | Total/mês |
|---|---|---|---|
| Marina (80%) | 0 | 25.000 × 0,80 = **20.000** | 20.000 |
| Luana (20%) | 5.000 | 25.000 × 0,20 = **5.000** | 10.000 |
| Felipe (adm. não sócio) | **5.000** | 0 | 5.000 |

**Casal (patrimônio comum):** 20.000 + 5.000 = **R$ 25.000/mês** contra os **R$ 50.000/mês pretendidos** → **fenda de R$ 25.000/mês (~R$ 300.000/ano), deixada em aberto** — não forcei reconciliação: cobriria com aporte, crescimento de receita além do projetado, ou corte da retirada. Luana, se optar pela cessão parcelada (§3a), serve-se dos R$ 10.000/mês para quitar a nota particular. **[Distribuir além do lucro realizado: consequências NÃO VERIFICADAS — fora da biblioteca.]**

### 6.4 IRRF — Lei 15.270/2025 (`library/lei15270_dividendos_2026.md`)
Retenção de **10% sobre o total pago no mês** por **uma mesma PJ** a **cada PF**, na parcela **acima de R$ 50.000/mês** (antecipação do IRPFM para rendas anuais > R$ 600 mil; progressivo a partir de R$ 1,2 mi).
- Plano: Marina 20.000; Luana 5.000 (pró-labore de Felipe/Luana tribut-se na fonte próprio) → **ninguém > 50.000 → IRRF dividendos = R$ 0/mês**.
- Mesmo na pretensão (25.000/cabeça), o limiar é **por beneficiário-PJ pagadora**, sem agregação de cônjuges **[agregação: NÃO VERIFICADO — a literalidade fala em "pessoa física"]**.
- **Transitório** (lucros apurados até 2025): inaplicável — constituição em 2026.
- Renda anual por cônjuge ≈ R$ 300.000 < 600.000 → sem IRPFM projetado **[cálculo detalhado: NÃO VERIFICADO]**.

## 7. Estruturas possíveis (valores recalculados — Luana sem dinheiro)
**Cenário B — RECOMENDADO:**
- Imóvel **fora** da PJ: casal loca ~60% da sala à clínica e os **40% diretamente ao dentista (R$ 8.000/mês)** — tributação PF do casal locador **[NÃO VERIFICADO]**.
- Quadro: Marina 80% + Luana 20%; Felipe administrador não sócio.
- Capital **R$ 150.000** em dinheiro (recursos do casal), 100% integralizado; **cessão de R$ 30.000 (20%)** em quotas a Luana (§3).
- CNAE único 9602-5/02 → **Simples Anexo III** possível (ressalvas §5.5). Sem ITBI, sem ganho de capital, sem CNAE 6810-2/02.

**Cenário A — plano original ajustado:**
- Imóvel integralizado por **R$ 420.000** (valor de declaração; casal intervm; anuência formal **[NÃO VERIFICADO]**), 100% creditado ao capital.
- Capital **R$ 570.000** = R$ 150.000 (dinheiro do casal) + R$ 420.000 (imóvel) — tudo do casal; **cessão de R$ 114.000 (20%)** a Luana.
- ITBI imune (§4.2; preponderância 7,4–8,0%, monitorar 3 anos); ganho PF R$ 0.
- **Lucro Presumido** (locação de 40% ao dentista veda Simples); a PJ celebra o contrato com o dentista (CNPJ/CRO próprios).

`numeros.json` responde o **desenho pretendido pelo cliente** (A): `itbi.devido=false`, `base=0`, `simples_possivel=false`. A decisão A×B não foi respondida pelo cliente (U10) — a recomendação profissional permanece **B**.

## 8. Cláusulas da minuta → correção
| Minuta | Vício | Correção (em `contrato_social_ajustado.md`) |
|---|---|---|
| Cl. 3ª (capital/quotas) | Contribuição de Luana em **serviços** (CC 1.055, §2º); quotas sem lastro (150k+900k = 100%); imóvel a R$ 900.000 (ganho de R$ 480.000; excesso sobre capital furta imunidade — Tema 796) | Capital A **R$ 570.000** (B: R$ 150.000), 100% integralizado pelo casal; imóvel **por R$ 420.000** creditado integralmente ao capital; Luana entra por **cessão de quotas** (R$ 114.000/R$ 30.000), não por trabalho |
| Cl. 5ª (administração Marina) | Lei 8.112, art. 117, X — a gestão é vedada **a qualquer horário** | **Felipe, administrador não sócio** (CC 1.060/1.061); cláusula de salvaguarda: servidor não administra nem trabalha, "ainda que fora do expediente" |
| Cl. 9ª (não concorrência Luana: sempre, Brasil) | Sem amparo na biblioteca; escopo abusivo **[NÃO VERIFICADO]** | ≤ 2 anos pós-saída; Município-sede + limítrofes; contraprestação **[NÃO VERIFICADO]** |
| Cl. 10ª (quotas preferenciais Marina) | Na v1 Marina não podia ser sócia; agora **pode** | Preferências admitidas (IN DREI 81/2020) porém **inócuas** (80% já a controla); jamais podem importar poder de gestão (117, X) **[alcance da preferência: NÃO VERIFICADO]** |
| Silêncios | — | Incluir: CNAEs (9602-5/02; sem 8630-5/04; sem 6810-2/02 no B); regime por cenário; política de pró-labore/distribuição (ata mensal, suporte L. 15.270); locação da sala (casal→clínica 60%, casal→dentista 40% no B); cessão de quotas a Luana; capital com forma de integralização (CC 997, V) |

## 9. Premissas e desconhecidos
**Fatos agora conhecidos (respostas do cliente):** aluguel dos 40% = R$ 8.000/mês (dentista); comunhão universal desde 2010, sem pacto; Luana sem disponibilidade financeira; Marina deseja ser cotista.

**Premissas nossas (proeminentes):** (P1) pró-labore de R$ 5.000 (Felipe/Luana) = piso defensivo, sem benchmark; (P2) receita R$ 1.200.000/ano e lucro R$ 420.000/ano do questionário, líquidas de tributos diretos e antes do pró-labore; (P3) distribuição pro rata do lucro realizado; (P4) cessão de quotas a Luana a valor contábil, sem ágio; (P5) receita de estética permanece ≫ R$ 96.000/ano nos 3 anos (teste do CTN art. 37); (P6) constituição em 2026 (transitório da L. 15.270 inaplicável).

**Desconhecidos remanescentes (cliente sem mais informações — sinalizados, não re-perguntados):**
- **U1** — Município/UF da sede (ITBI local, alvarás, ISS, Junta).
- **U2** — Se Marina/Felipe/Luana participam de **outra optante do Simples** (vedações do art. 17/LC 123 não verificáveis → condição do Simples no Cenário B em aberto).
- **U3** — Habilitação/conselho da biomédica esteta e licenças de funcionamento.
- **U4** — Benchmarks de mercado p/ administrador e biomédica (pró-labore é premissa).
- **U5** — Tributos da cessão/doação de quotas a Luana (ITCMD, ganho de capital) — podem inverter a escolha entre cessão onerosa e doação.
- **U6** — Regras do órgão de Marina (conflito de interesses como analista federal de saúde; deveres declaratórios).
- **U7** — Tributação do casal como locador PF (Cenário B: 60% clínica + 40% dentista = R$ 96.000/ano só do dentista).
- **U8** — Tratamento registral da cessão na constituição (IN DREI/local).
- **U9** — Teto ME/EPP e alíquotas efetivas (Simples/LP) — fora da biblioteca.
- **U10** — Decisão **A × B**: o cliente não manifestou preferência; recomendo **B** e o `numeros.json` reflete **A** (desenho pretendido).

