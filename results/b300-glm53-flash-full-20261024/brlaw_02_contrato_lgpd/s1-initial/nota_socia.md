# Nota à sócia — parecer sobre a minuta NexaClin (em linguagem simples)

**Clínica Aurora × Nexa Sistemas Ltda. — minuta de licença de uso de software**
*Parecer baseado exclusivamente na biblioteca de referência do escritório (`library/INDEX.md`); sem acesso a fontes externas.*

---

## 1. "Foro em Florianópolis é abusivo pelo CDC e dá pra anular" — **não, neste caso**

Sua colega está aplicando a regra errada para este contrato.

- O Código do Consumidor (CDC, art. 51 — `library/cdc_art51_distrator.md`) só protege **consumidor**: quem contrata como **destinatário final** de um produto ou serviço.
- A Aurora usa o NexaClin como **ferramenta de trabalho da empresa** (prontuário e faturamento), ou seja, como insumo da atividade — não como consumidora final. É a chamada "teoria finalista" do STJ.
- Essa "blindagem" do CDC só cede quando a empresa demonstra vulnerabilidade técnica, jurídica ou econômica — **não se presume**; clínica com R$ 9,2 milhões de faturamento contratando um ERP médico, revisado por advogado, não é o típico caso de vulnerabilidade.
- Entre duas empresas presumidas paritárias, a **cláusula de foro é válida** (CC art. 421-A; CPC art. 63, §1º e §3º; STJ, REsp 1.707.855/SP — `library/cc_contratos_empresariais.md`).

**O que isso significa na prática:** não dá para "anular" o foro pelo CDC. Mas, como o contrato terá muitas mudanças na contraproposta, é legítimo **pedir por acordo comercial** o foro da comarca da sede da Aurora — se a NexaClin recusar, a cláusula segue válida e vale pesar o custo de litigar em Florianópolis antes de assinar.

## 2. Os números do contrato (aritmética aberta)

| Cálculo | Resultado |
|---|---|
| Mensalidade: 3 unidades × R$ 6.900 | **R$ 20.700/mês** |
| Anual: R$ 20.700 × 12 | **R$ 248.400/ano** |
| 36 meses: R$ 20.700 × 36 | **R$ 745.200** |
| Custo total primeira vigência: R$ 48.000 + R$ 745.200 | **R$ 793.200** |
| Multa da cláusula 10 (100% das vincendas, no dia 1) | **R$ 745.200** = 15,5× a implantação (745.200/48.000 = 15,525) e 8,1% do faturamento anual (745.200/9.200.000 = 8,1%) |
| Teto de responsabilidade (cláusula 8): 3 × R$ 20.700 | **R$ 62.100** |
| Crédito máximo do SLA (10% da mensalidade) | **R$ 2.070/mês** (R$ 24.840/ano) |
| Downtime com 99%: 30 d × 24 h × 1% | **7,2 h/mês** (~87,6 h/ano) |
| Multa da não concorrência | **R$ 500.000** = 2,01× o custo anual do contrato (500.000/248.400) |

## 3. Os 4 pontos graves — não assine sem mudar

1. **Dados (cláusula 5).** Do jeito que está, a Nexa poderia guardar os prontuários/exames de ~22.000 pacientes "no exterior, a critério da Nexa" e usar tudo "anonimizado ou agregado" para **pesquisa e desenvolvimento de produtos da própria Nexa**. Dados de saúde são **sensíveis** (LGPD art. 5º, II) e só podem ser tratados nas hipóteses do art. 11; para o operador tratá-los fora das instruções do controlador não há base legal (art. 39), e o excerto da biblioteca adverte que "agregados" de 22 mil pacientes **raramente são anonimizados de verdade** (`library/lgpd_excertos.md`, nota ao art. 12). Proposta: substituir a cláusula inteira pela **cláusula de proteção de dados** entregue em `clausula_dados.md` (papéis, base legal, instruções, subcontratação, transferência internacional, incidentes, auditoria, término).
2. **Não concorrência (cláusula 13).** Por 5 anos, em todo o Brasil, proibida até a **utilização** de software concorrente — isso significaria a clínica parar de trabalhar. O STJ admite não concorrência só limitada no tempo (regra: até 2 anos), no espaço e no objeto, justificada por interesse legítimo; e, em licença de software, vedar o uso de tecnologia concorrente pelo licenciado após o fim **inverte a lógica e é tida por abusiva/sem causa** (STJ, REsp 1.203.109/MG (2015); REsp 680.815/PR — `library/stj_nao_concorrencia.md`). Multa de R$ 500.000 (2× o custo anual do contrato). **Mandem cortar essa cláusula.**
3. **Multa de 100% das vincendas (cláusula 10).** Sair antes do fim custaria, no dia da assinatura, **R$ 745.200** — 15,5× a implantação. A lei permite ao juiz reduzir penalidade manifestamente excessiva (CC art. 413 — `library/cc_contratos_empresariais.md`), mas o caminho mais barato é negociar de partida uma multa proporcional (~10% das vincendas, simétrica para as duas partes).
4. **Exportação por 30 dias (cláusula 7).** O prontuário pertence ao paciente e o estabelecimento deve guardá-lo por no mínimo **20 anos** (Res. CFM 1.821/2007; Res. 2.299/2021; Lei 13.787/2018 — `library/cfm_prontuario.md`). Um CSV apagado 30 dias depois não cobre isso. Pedimos exportação completa e não proprietária, transição com acesso de leitura de no mínimo **180 dias** (prorrogável) e um **ensaio de exportação por ano**: vocês mesmos disseram que migrar os 22 mil prontuários é um projeto de meses — a saída é esse projeto ao contrário, e não cabe em 30 dias nem em 90.

## 4. Pontos que também precisam mudar (gravidade média)

- **Reajuste "a critério da NEXA" (cláusula 2):** índice fixo e objetivo (IGP-M, sem escolha unilateral).
- **Renovação de 3 em 3 anos com aviso só com 180 dias (cláusula 3):** combinada com a multa de 100%, vira armadilha. Proposta: renovação em 12 meses, aviso de 90 dias e dever de a Nexa avisar por escrito antes da data-limite.
- **SLA de 99% com crédito teto de 10% (cláusula 6):** 99% = **7,2 h/mês** fora do ar num prontuário de clínica; a compensação máxima seria R$ 2.070/mês. Proposta: 99,5%, janela de manutenção avisada e direito de rescindir sem multa se descumprir repetidamente. Backup e restauração ficam garantidos na cláusula de dados.
- **Subcontratação sem aviso (cláusula 12):** abre caminho para hospedar seus dados com terceiros (inclusive no exterior) sem autorização e sem repasse das obrigações (LGPD arts. 39 e 42, §1º, I).
- **Teto de R$ 62.100 mesmo para vazamento de dados (cláusula 8):** o teto vale para falhas comuns; para violação de dados/LGPD (art. 42) deve ficar fora do teto, sob pena de esvaziar a responsabilidade legal.

## 5. Pontos aceitáveis

Cláusulas 1 (objeto), 4 (obrigações), 9 (confidencialidade mútua, 5 anos), 11 (multa de mora de 2% + juros), **14 (foro — válido, vide acima)** e 15 (declarações de leitura). Detalhe em `clausulas.json`.

## 6. O que falta verificar / não consta na biblioteca

- **Encarregado (DPO) obrigatório:** a ficha informa que a Aurora **não possui DPO formal**. A LGPD menciona a figura (art. 5º, VIII), mas o excerto da biblioteca **não traz o art. 41**, que regula a obrigatoriedade; recomendamos nomear encarregado e confirmar a exigibilidade fora desta análise (**informação não verificada na biblioteca**). **Atualização (resposta da cliente):** ninguém na Aurora foi designado ainda — nome e contato do encarregado precisam entrar no instrumento antes da assinatura.
- **Proibição de compartilhamento entre controladores** (art. 11, §4º): o faturamento junto às operadoras está expressamente permitido — esse será o gancho para a integração com Unimed/Bradesco indicada no seu e-mail.
- **Art. 18 (direitos dos titulares) também não consta** do excerto; listamos como não verificado em `clausula_dados.md` §3º, v.
- **Mecanismo de transferência internacional (art. 33) aplicável à hospedagem indicada pela Nexa** (AWS, 'provavelmente' nos EUA — resposta da cliente, sem confirmação): o excerto cita as hipóteses gerais do art. 33 (país adequado/cláusulas-padrão), mas **quais mecanismos vigentes se aplicam aos EUA não consta na biblioteca** — verificação externa, com prova a cargo da Nexa (declaração escrita exigida em `clausula_dados.md` §5º).

## 7. Recomendação final sobre o prazo de 10 dias

Os prazos de 10 dias são viáveis **para assinar uma minuta revisada**, não para assinar esta. Basta a Aurora devolver hoje a contraproposta com: (a) a cláusula de dados substituinte (cláusula 5), (b) 7 correções de redação já prontas em `clausulas.json` (cláusulas 2, 3, 6, 7, 8, 10 e 12), (c) exclusão total da cláusula 13 e (d) a questão do foro apresentada como pedido comercial — e exija junto a confirmação **por escrito** da hospedagem (região/país e serviços AWS, §5º da cláusula de dados). Se a Nexa concordar com tudo, assine; se fizer resistência apenas nos itens comerciais bilaterais (foro e SLA), ainda assim assinável; **não** assine mantendo os 4 pontos graves da seção 3.

---

## 8. Atualização com as respostas de vocês (AWS "provavelmente" nos EUA + migração de meses)

**O que ouvimos:** a Nexa disse usar AWS, **"provavelmente" nos EUA** (sem confirmação), e que migrar os 22 mil prontuários é **um projeto de meses** — sair no meio seria caótico. Duas consequências, já refletidas na contraproposta:

1. **Hospedagem fora do Brasil = transferência internacional (LGPD art. 33).** Se os dados saem do Brasil, o art. 33 exige base específica (país com grau de proteção adequado ou cláusulas-padrão, entre outros — `library/lgpd_excertos.md`). "Provavelmente" não basta: a cláusula de dados (§5º) agora exige (i) declaração **por escrito**, na assinatura, da região/país e dos serviços da Nexa; (ii) **prova** do mecanismo de salvaguardas antes do fluxo começar; (iii) nada espelhado em região não autorizada. A confirmação é pendência **da Nexa**, não de vocês — e qual mecanismo vale para os EUA **não consta do excerto da biblioteca** (verificação externa). E como a decisão é comercial: se a Nexa oferecer hospedagem 100% no Brasil sem custo adicional, basta pedir — a redação funciona nos dois cenários.
2. **A migração lenta muda a estratégia, não a lei.** Se a saída é caótica na prática, o momento real de proteger a Aurora é **hoje, na assinatura** — depois, a clínica fica cativa de fato. Por isso: (a) os 4 pontos graves da seção 3 precisam entrar resolvidos no contrato; (b) a multa de 100% das vincendas (cláusula 10) e a não concorrência de R$ 500 mil (cláusula 13) reforçam o **efeito de tranca** — quem não consegue sair dá ao fornecedor pouco incentivo a se esforçar; (c) a transição de saída foi recalibrada para a realidade: **mínimo de 180 dias** de acesso de leitura (antes 90) e **ensaio de exportação 1×/ano** (`clausula_dados.md` §9º); (d) na implantação, peçam por escrito o **plano de migração dos 22 mil prontuários com cronograma e responsáveis**, e mantenham o sistema atual disponível até a migração ser confirmada — é o mesmo risco, espelhado. Juntas, as multas de 10 e 13 somam R$ 1.245.200 (745.200 + 500.000) contra um contrato de R$ 793.200 na primeira vigência (1,57× o custo total).

Nenhum item acima bloqueia a contraproposta: tudo tem redação pronta. As perguntas de `QUESTIONS.md` não respondidas (cidade-sede, índice, janela de manutenção, encarregado) viraram pendências registradas com premissa de trabalho em `STATUS.md` — não voltamos a perguntá-las.

*Assunções declaradas: consideramos que todo o prontuário, exames e cadastro dos ~22.000 pacientes ativos migrarão para o NexaClin; que a Nexa atuará como operadora desses dados; e que o contrato é B2B entre empresas com assessoria jurídica (presunção de paridade, CC art. 421-A). Com as respostas recebidas, assumimos ainda: hospedagem da Nexa em AWS "provavelmente" nos EUA (**não confirmada** — tratada como transferência internacional, art. 33, até a declaração escrita); migração dos prontuários como projeto de meses (base da transição de 180 dias). Nenhuma dessas premissas altera as conclusões jurídicas; pendências em `STATUS.md`.*
