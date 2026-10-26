# Revisão de estilo e redação da minuta do Comprador

**Escopo e limitação (ler antes de tudo).** Revisamos apenas o texto que temos — o extrato
de uma página ("cláusulas relevantes": 2.3, 3.2, 5.7, 5.9, 8.1, 8.4(a)–(d), 9.1, 10.2) e a
carta do advogado do Comprador. Preâmbulo, qualificação das partes, definições, demais
declarações e a maioria dos anexos **não foram fornecidos**: nada aqui se afirma sobre o
resto, e os itens marcados "conferir no texto completo" podem já estar resolvidos lá.
Este arquivo trata de **redação, coerência interna e termos indefinidos**. O conteúdo
substancial de cada ponto está em `redline.md` e `achados.json`; aqui só se aponta onde o
texto, como está, cria ambiguidade ou contradição por si só.

**Método.** Citações abaixo reproduzem literalmente o extrato (conversão de texto do PDF;
em caso de divergência, prevalece a versão assinada).

---

## Questões gerais (transversais)

**G1 — "preço" × "Preço Total".** Em 8.4(b) coexistem "15% do **preço**" e "cujo limite
será o **Preço Total**"; em 10.2, "20% do **preço**". São o mesmo termo definido? Não
há como confirmar (definições não fornecidas). Se "Preço Total" incluir o earn-out (2.3),
o teto sem limite para 5.7/5.9 fica atrelado a um valor que só se conhecerá 12 meses depois
do fechamento, e a base da conta-garantia (20% "do preço") fica indeterminada.
**Sugestão:** definir o termo uma vez ("Preço Total" = sinal + parcelas + earn-out máximo?)
e usar sempre o definido. *Afeta interpretação: sim.*

**G2 — Marcos temporais sem definição.** O texto alterna "fechamento" (2.3, 3.2),
"assinatura" (8.4(c)) e um prazo "de sobrevivência" sem termo inicial (8.4(d)) — três
marcos que não coincidem e nenhum definido no extrato. *Afeta interpretação: sim.*

**G3 — "Notificação" × "Aprovação" do CADE.** A minuta condiciona o fechamento à
"**Aprovação** do CADE, nos termos da Lei 12.529/2011"; a carta do Comprador pede que se
"confirmem a **notificação** ao CADE". Os dois textos usam institutos diferentes — e, no
caso concreto, nenhum dos dois se aplica, porque a operação não preenche os limiares do
art. 88 (ver redline §3.3 e achado "CADE"). A confusão terminológica entre notificação e
"aprovação" revela o erro de base. *Afeta interpretação: sim.*

---

## Cláusula por cláusula

### 2.3 — Earn-out

- **a) "limitado a R$ 1.500.000,00" — a maior ambiguidade do texto.** O limitador pode se
  referir ao **pagamento** ("pagará 35% do excedente, sendo o earn-out limitado a R$ 1,5 mi") ou ao
  **excedente** ("o valor em que o EBITDA exceder R$ 1,1 mi, limitado esse excedente a
  R$ 1,5 mi")? As duas leituras dão valores finais diferentes: pagamento limitado a
  **R$ 1,5 mi**; excedente limitado a R$ 1,5 mi ⇒ pagamento máximo de
  35% × R$ 1,5 mi = **R$ 525 mil**. A escolha entre as leituras vale R$ 975 mil — e, na
  primeira leitura, o teto só seria alcançado com EBITDA de 1,1 + 1,5 ÷ 0,35 =
  **R$ 5.385.714**, acima da receita total de R$ 4,2 mi (data room §4.2), o que torna a
  promessa inatingível (ver achado "earn-out", com a conta completa).
  **Sugestão:** reescrever sem o particípio solto — ex.: "sendo o pagamento total a título
  de earn-out limitado a R$ 1.500.000,00" (ou "o excedente considerado para esse cálculo
  será limitado a…", conforme a intenção real dos Vendedores — confirmar antes).
  *Afeta interpretação: sim — item nº 1 desta revisão.*
- **b) Cálculo nas mãos do devedor.** "apurado pelo Comprador segundo suas práticas
  contábeis, podendo incluir rateio de despesas corporativas do grupo": quem paga define o
  quanto deve, sem padrão contábil objetivo (BR GAAP/IFRS?), sem direito de fiscalização ou
  impugnação do Vendedor e sem critério para o "rateio". *Afeta interpretação: sim.*
  (Ponto de conteúdo tratado em `QUESTIONS.md`.)
- **c) Mecânica ausente no extrato.** "EBITDA dos 12 meses seguintes ao fechamento" — 12
  meses corridos da data do fechamento ou período contábil? Prazo para pagar após a
  apuração, mora, acesso dos Vendedores aos números: nada consta no extrato. Pode estar no
  texto completo — conferir. *Afeta interpretação: sim (se não estiver no completo).*
- **d) Valores só em algarismos.** "R$ 1.100.000,00" e "R$ 1.500.000,00" sem forma por
  extenso, praxe em contratos. *Não.*

### 3.2 — Condições precedentes

- **a) Condição de objeto vazio (contradição interna).** "Obtenção das anuências listadas
  no Anexo 3.2 (Anexo 3.2: 'não aplicável')" — a condição remete a um anexo que se declara
  vazio: ou a condição não tem objeto, ou está incompleta e indeterminada. Além do erro de
  conteúdo (o Anexo deveria listar a anuência da Horizonte Azul — ver redline §3.2 e
  achado "Horizonte"), é má técnica incluir o texto do anexo entre parênteses no corpo da
  cláusula. **Sugestão:** condição com anexo preenchido e referência limpa ("conforme Anexo
  3.2"). *Afeta interpretação: sim.*
- **b) "Aprovação do CADE"** — ver G3: terminologia errada para o regime da Lei
  12.529/2011 (notificação para análise; desfecho é a alçada, não uma "aprovação"
  discricionária). *Afeta interpretação: sim.*

### 5.7 — Declarações — Trabalhista

- **a) "Todos os prestadores de serviços" — termo nunca definido.** Abrange profissionais
  PJ de prestação continuada (são 11, com "exclusivos, horário, subordinação — mesmo
  perfil do caso Solaris", data room §2.2)? Se sim, a declaração nasce falsa contra o
  próprio data room; se não, declara apenas o trivial e não cobre o risco real. O termo
  indefinido é armadilha nos dois sentidos. **Sugestão:** definir "Prestadores de
  Serviço" e amarrar à lista dos contratos do anexo de declarações.
  *Afeta interpretação: sim.* (Conteúdo: redline §5.7, achado "PJs".)
- **b) "inexistindo risco de reconhecimento de vínculo" — asserção absoluta.** Prometer
  "inexistência de risco" não é atestar um estado verificável de coisas: qualquer risco,
  por remoto, torna a declaração "falsa", sobretudo combinada com 8.4(c) (sandbagging) e
  sobrevivência de 5 anos (8.4(d)). **Sugestão:** fórmula epistêmica e concreta — "não
  há ações ou procedimentos administrativos ou judiciais em curso ou, ao conhecimento dos
  Vendedores, ameaçados, versando sobre reconhecimento de vínculo empregatício".
  *Afeta interpretação: sim.*

### 5.9 — Declarações — Tributária

- **a) "com certidões negativas vigentes" — contradiz o data room.** O dossiê §3.1 traz
  **certidão federal positiva** (débito de R$ 310 mil de IRPJ 2023 em cobrança, sem
  parcelamento) junta aos regulares CRF/FGTS e estaduais/municipais. Certidão positiva
  não é "negativa vigente": a declaração é literalmente falsa na data da assinatura —
  "situação fiscal regular" idem. Além da correção de conteúdo (redline §5.9, achado
  "CND"), a redação precisa de **carve-out expresso** para a situação revelada, não de
  adjetivo padrão. *Afeta interpretação: sim.*
- **b) Sem marco temporal.** "encontra-se em situação fiscal regular": certidões vencem
  em meses; sem "na data desta Contrato" (ou fórmula equivalente no texto completo), a
  declaração vira garantia de perpetuidade. Conferir se há qualificador geral de data nas
  demais declarações. *Afeta interpretação: sim (se não houver qualificador geral).*

### 8.1 — Indenização pelos Vendedores

- **Linha única, carga máxima.** "Perdas decorrentes de violação de declarações." Em uma
  linha se define o gatilho de tudo — sem materialidade, sem nexo ("diretamente
  decorrentes"?), sem tratar de lucros cessantes, sem gross-up (dívida tributária paga a
  prazo tem custo financeiro: quem paga juros do parcelamento?), sem procedimento. Pode o
  texto completo resolver isso — não temos como ver. Se o completo for tão seco quanto o
  extrato, esta é a linha mais cara do contrato, porque é ela que ativa os limites de
  8.4 e a amplitude de 8.4(c). *Afeta interpretação: sim (limitação de escopo: não
  verificável no material fornecido).*

### 8.4 — Limites

- **(a) Três rótulos, um sentido não escrito.** "franquia (basket) de R$ 150.000,00, não
  dedutível (tipping)" empilha vocabulário de dois regimes opostos: *deductible/franquia*
  (só o excedente é indenizável) e *tipping basket* (ultrapassado o limiar, indeniza-se do
  primeiro real). "não dedutível (tipping)" indica a segunda leitura, mas a redação convida
  à disputa porque não diz a conta. **Sugestão:** escrever a fórmula, não o rótulo —
  "nenhuma indenização será devida até que as Perdas agreguem R$ 150.000,00; ultrapassado
  esse valor, indenizar-se-á a totalidade das Perdas [ou: apenas o excedente]".
  *Afeta interpretação: sim.*
- **(b) Base do teto.** "15% do preço" — ver G1 (preço × Preço Total). Além disso, a
  exceção ("cujo limite será o Preço Total" para 5.7/5.9 = teto de 100% do preço) convive
  com 10.2 (escrow de 20% "do preço" por 5 anos): a retenção supera o teto geral de 15%
  para tudo o que não for 5.7/5.9 — inconsistência numérica interna (achado "escrow").
  *Afeta interpretação: sim.*
- **(c) "O conhecimento do Comprador…" — quem é o Comprador que "conhece"?** A cláusula
  não define titular nem padrão do "conhecimento" (órgãos? gestores? a equipe de due
  diligence? qualquer documento entregue no data room conta como conhecimento?). Em leitura
  larga, tudo que os próprios Vendedores entregaram no data room vira "conhecimento" que,
  por 8.4(c), não afasta indenização — é exatamente a combinação declarada no extrato
  (5.7/5.9 absolutas + 8.4(c) + 8.4(d)) que torna o sandbagging caro (redline §8.4(c),
  achado "sandbagging"). *Afeta interpretação: sim.*
- **(d) "prazo: 5 anos para 5.7 e 5.9; 2 anos demais" — telegráfica e omissa.** Três
  vícios de redação: (i) "2 anos demais" sem verbo nem substantivo (padrão: "2 (dois)
  anos para as demais declarações"); (ii) **termo inicial indefinido** — assinatura,
  fechamento ou data da violação? Com condição pendente de anuência e comunicação a
  Sorocaba, o hiato assinatura→fechamento não é desprezível e muda a contagem; (iii) não
  distingue sobrevivência da declaração do prazo para apresentar **reclamação escrita**
  (praxe: a notificação protocolada preserva a claim mesmo após a sobrevivência).
  *Afeta interpretação: sim.* (Conteúdo: achado "sobrevivência".)

### 9.1 — Não concorrência

- **Cláusula-esqueleto: "Vendedores: 10 anos, território nacional."** Falta verbo e
  estrutura dispositiva, e faltam definições elementares: (i) o que é vedado (concorrer com
  a Sociedade? com o grupo do Comprador? em "atividades concorrentes" — definidas onde?);
  (ii) quem obriga (só os sócios pessoas físicas? entidades que controlem ou integrem?
  herdeiros?); (iii) referência territorial — "nacional" em relação a quê, se a atuação
  registrada no dossiê não descreve presença nacional (data room §§1.1–1.2 e §4.2); (iv) se há
  ou não contrapartida (relevante para o controle de razoabilidade do art. 1.147 do CC,
  `library/cc_1147_nao_concorrencia.md`). Uma cláusula que restringe atividade profissional
  em uma linha é tecnicamente frágil antes mesmo de se discutir seu excesso.
  *Afeta interpretação: sim.* (Conteúdo: redline §9.1, achado "não concorrência".)

### 10.2 — Conta-garantia (escrow)

- **Uma linha para cinco funções.** "20% do preço por 5 anos" não diz: quem é o agente
  depositário e onde; quando e como se libera (liberação única em 5 anos? escalonada pelas
  sobrevivências de 8.4(d), que são de 2 e 5 anos — incompatíveis com liberação única?);
  que reclamação trava a liberação e de quem; custos bancários e rendimento. E a
  inconsistência numérica com 8.4(b) (20% retidos > teto geral de 15%) já está apontada
  no achado "escrow". *Afeta interpretação: sim.*

### Carta do advogado do Comprador

- "Confirmem a notificação ao CADE para não atrasar" — a fórmula imperativa **pressupõe** a
  obrigação de notificar ("confirmem"), quando a obrigação é precisamente o que se discute
  (e não existe: G3 e redline §3.3). Não é erro de estilo do contrato, mas a correspondência
  do Comprador merece resposta no mesmo tom factual com que foi escrita — ver
  `resposta_advogado_comprador.md`.

---

## O que não foi possível revisar (limitação de escopo)

Qualificação das partes; seção de definições ("Sociedade", "Preço Total", "Fechamento",
"Prestadores"); existência de anexo de disclosure schedules (que resolveria 5.7/5.9 na
origem — ver redline §8.5–8.7); declarações 5.1–5.6 e 5.8; procedimento de reclamação da
Cláusula 8 (8.2, 8.3); os demais anexos além do "Anexo 3.2"; a numeração completa da
Cláusula 10 (o extrato só traz 10.2). Recomenda-se obter o texto integral antes da
assinatura; esta revisão vale somente sobre o material fornecido.
