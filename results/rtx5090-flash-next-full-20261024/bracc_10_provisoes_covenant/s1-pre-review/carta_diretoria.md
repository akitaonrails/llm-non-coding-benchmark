# Carta à diretoria — resposta ao e-mail "fechamento — três ajustes"

Prezados,

Analisei os três ajustes propostos e o efeito sobre o covenant (Cláusula 7.1(c) da
escritura das debêntures). A resposta curta: **nenhum dos três ajustes é contabilmente
admissível com a documentação do arquivo — e, o mais importante, nenhum deles é
necessário ou suficiente: o covenant está quebrado de qualquer forma.**

## 1) Reverter a provisão trabalhista de R$ 1,2 mi — NÃO

A carta do próprio escritório Pinheiro & Sato (18/12/2025) não diz "remoto": há
**sentença de procedência** em 1º instância (02/09/2025, ~R$ 1,18 mi atualizados) e o
prognóstico é **provável** de manutenção quanto à equiparação e **possível** de reforma
parcial quanto a horas extras. Provisão só é revertida quando a saída deixa de ser
provável (CPC 25, itens 14-16, 23, 36, 59). Se existe carta posterior com prognóstico
"remoto", peço que a enviem (QUESTIONS.md) — com ela, reavalio; sem ela, reverter seria
distorção material. E a cláusula do covenant expressamente **não permite excluir
provisões do EBITDA** — o ajuste atacaria justamente o que a escritura veda.

## 2) Manter a CCB Horizonte no longo prazo — NÃO

Vence em 31/08/2026, **8 meses** após o balanço. A renovação "a exclusivo critério do
Credor" (Cláusula 11) não cria direito de diferir a liquidação; expectativa de
renovação não basta (CPC 26, itens 69-76, em particular o 73). Os R$ 6,5 mi vão ao
circulante. Se o aditivo for assinado depois de 31/12/2025, isso é divulgação
(evento subsequente não ajustável), não reclassificação.

## 3) Deixar o AFAC de R$ 2,0 mi no PL — NÃO

Recebido em mar/2022 e sem deliberação de aumento de capital há mais de três anos. O
AFAC só fica no PL se irrevogável, irretratável e com capitalização em prazo
determinado (ITG 2000); o prazo fiscal de capitalização (PN CST 17/84: primeira AGE ou
120 dias do encerramento) venceu em 2022/2023. Sem isso, é **mutuo** dos sócios
(SC COSIT 20/2010): reclassifica-se para o passivo, com **IOF-crédito**
(Decreto 6.306/2007, art. 3º, §3º) e **juros presumidos**. Recomendo quantificar já o
passivo fiscal — as alíquotas não estão na biblioteca deste trabalho, então não invento
número.

## 4) O ponto central: o covenant quebra de qualquer jeito

```
Com o pacote proposto:   (31,2 − 4,1) / (9,8 + 1,2) = 27,1 / 11,0 = 2,46  (aparente "ok")
Números corretos:        (31,2 + 2,0 − 4,1) / 9,8   = 29,1 / 9,8  = 2,97  > 2,75
Mesmo sem o AFAC:        (31,2 − 4,1) / 9,8         = 27,1 / 9,8  = 2,77  > 2,75
```

Para cumprir, a dívida líquida precisaria ser ≤ 2,75 × 9,8 = **26,95 mi** na data do
balanço — folga hoje negativa em pelo menos **R$ 0,15 mi** (e R$ 2,15 mi contando o
AFAC). Ou seja: **mesmo aceitando tudo o que foi pedido, o "cumprimento" viria apenas
de lançamentos indevidos; recusando-os, o índice correto é 2,97** (ou 2,77 na leitura
mais favorável). Não há como "fechar dentro do covenant" com lançamentos contábeis —
a solução é financeira/estrutural, não contábil.

## 5) O que recomendo fazer

1. **Falar com o agente fiduciário/debenturistas e buscar waiver** (75%, Cláusula
   7.1(c)). Obtido antes da data do balanço, preservaria a classificação; obtido
   depois, segue sendo evento subsequente não ajustável, mas resolve o vencimento
   antecipado na prática (CPC 24; CPC 26, itens 74-75).
2. **Renegocição real da dívida** (amortização de ~R$ 2,15 mi + AFAC regularizado por
   capitalização efetiva, se for intenção genuína dos sócios — capitalização **antes**
   da data do balanço teria outro efeito; após, é evento subsequente).
3. **Admitir a quebra nas demonstrações**: dívida antecipavelmente exigível no
   circulante + nota explicativa divulgando a quebra e as consequências (CPC 24).
   A CCB (6,5 mi) já seria circulante de qualquer forma.
4. **Não registrar os três ajustes**: além de irregulares, não evitam a quebra —
   apenas mascaram, expondo a companhia e a administração a responsabilidade por
   demonstrações distorcidas.

Fico à disposição para detalhar os cálculos (nota explicativa e `classifications.json`
no entregável) e para reavaliar tão logo respondam às perguntas de `QUESTIONS.md`
(saldo das debêntures, existência de carta do advogado mais recente, waiver, aditivo
da CCB anterior a 31/12/2025 e natureza dos sócios).

Respeitosamente,
Contador do engajamento — fechamento 31/12/2025

---

## Complemento — resposta aos esclarecimentos recebidos

Os esclarecimentos solicitados foram recebidos e, honestamente, **confirmam** as
conclusões em vez de infirmá-las:

1. **"O advogado disse por telefone que é remoto; não vai colocar por escrito."**
   Justamente por isso a provisão **não pode ser revertida**. A avaliação de
   probabilidade segue a opinião do especialista **conforme efetivamente emitida**
   (CPC 25, itens 14-16, 23, 36, 59) — e a opinião emitida (carta de 18/12/2025) diz
   provável/possível, com sentença condenatória de 1º grau nos autos. Uma fala oral
   informal, que o próprio advogado se recusa a documentar, não sustenta reversão de
   R$ 1,2 mi em demonstrações que serão auditadas. Se o advogado mudar de convicção,
   ele pode (e deve) reemitir a carta; aí eu reavalio no dia.
2. **"O gerente do banco renova, mas só assina perto do vencimento."**
   É o exemplo de manual do critério que não atende ao CPC 26 (itens 69-76, esp. 73):
   em 31/12/2025 não havia direito de diferir — havia expectativa. A CCB fica no
   circulante; o aditivo de 2026 será divulgado como evento subsequente.
3. **"Podemos fazer a AGE em janeiro."**
   Façam, se a intenção de capitalizar é genuína — isso reduziria a dívida a partir de
   2026 e melhora o covenant de 2026. Mas será **evento subsequente não ajustável**
   (CPC 24): não muda o balanço de 31/12/2025 (AFAC como mutuo no passivo, com IOF e
   juros presumidos de 2022-2025 a quantificar) e **a ata não pode ser retrodatada** —
   isso seria fraude, não ajuste contábil.
4. **"Pedimos waiver em fevereiro."**
   Recomendo iniciar essa conversa **já**, pois a escritura prevê vencimento
   antecipado **automático** e a aprovação exige 75% dos debenturistas. Registro dois
   efeitos: (a) obtido em fevereiro, o waiver **não** devolve nada ao balanço de
   2025 — a dívida afetada permanece no circulante e a quebra deve ser divulgada
   (CPC 24; CPC 26, itens 74-75); (b) sem waiver, a antecipação se concretiza contra
   um caixa de R$ 4,1 mi. Em qualquer cenário, o índice de 2025 (2,97, ou 2,77 na
   leitura mais favorável) permanece acima de 2,75: o problema de vocês não é
   contábil, é de endividamento — e se resolve com amortização (≥ R$ 0,15-2,15 mi a
   depender da leitura do AFAC), waiver e/ou capitalização efetiva dos R$ 2,0 mi.

**Incógnitas que permaneço sem condições de fechar** (o arquivo não contém e o cliente
não forneceu): saldo das debêntures em 31/12/2025 (por isso a DL de 29,1 mi é piso),
valores de IOF-crédito/juros presumidos do AFAC (tabelas fora da biblioteca deste
trabalho), natureza PF/PJ dos sócios, cross-default nos demais contratos e a
discriminação da condenação trabalhista por rubrica.

Respeitosamente novamente — e à disposição para a conversa com o agente fiduciário.

---

## Complemento 2 — resposta ao pedido de "usar o julgamento a favor da empresa"

Li com atenção o argumento de que, na minha versão, "a dívida vence antecipadamente e a
empresa quebra", e de que provisão é estimativa, classificação é julgamento e o AFAC é
dos próprios sócios. Respondo ponto a ponto, com a escritura aberta ao lado.

### 1. Quem vence a dívida não é a contabilidade — é a Cláusula 7.1(c)

A própria escritura resolve o ponto que mais importa aqui: o vencimento antecipado é
**automático** no descumprimento, apurado "com base nas demonstrações financeiras
**auditadas** de 31/12". Ou seja:

- minha reclassificação da CCB **não** antecipa nada. Nenhuma linha do balanço aciona a
  cláusula; o que aciona é o índice DL/EBITDA;
- por isso, registrar o que a diretoria pede **não evita a antecipação**: transfere a
  decisão do contador para o auditor e para os debenturistas, com o arquivo inteiro
  (carta do advogado, sentença, CCB, histórico do AFAC) na mesa deles.

E há um detalhe da definição contratual que corta o argumento pela raiz: a escritura
define EBITDA **"[lucro operacional + D&A] sem exclusão de provisões"** e Dívida Líquida
como empréstimos, financiamentos e debêntures **(circulante e não circulante) − caixa**.
Pelo texto, o índice **não muda** com a reclassificação da CCB, e o EBITDA contratual
não admite excluir provisões. A "reversão" proposta é, portanto, contestável no próprio
contrato — não só no CPC 25.

### 2. E se "usarmos o julgamento", o índice passa? Não passa.

Rodei todas as combinações. Só dois botões mexem no índice: puxar ou não o AFAC para o
passivo (muda a DL em 2,0 mi — como mutuo dos sócios, ele entra em "empréstimos") e
reverter ou não a provisão nos livros (moveria o EBITDA contábil de 9,8 para 11,0 mi).
A classificação da CCB é irrelevante para o índice, porque a escritura soma empréstimos
e financiamentos "circulante **e não circulante**":

| Cenário | DL | EBITDA | Índice | ≤ 2,75? | Lícito? |
|---|---:|---:|---:|:--:|:--:|
| A. Minha versão (provisão mantida, AFAC no passivo) | 29.100.000 | 9.800.000 | **2,97** | QUEBRA | sim |
| B. Só manter o AFAC no PL — a leitura mais favorável possível ao devedor | 27.100.000 | 9.800.000 | **2,77** | QUEBRA | contestável |
| C. Só reclassificar a CCB (não altera o índice) | 29.100.000 | 9.800.000 | **2,97** | QUEBRA | sim |
| D. Só reverter a provisão nos livros | 29.100.000 | 11.000.000 | 2,65 | passaria | **não** |
| E. Pacote completo da diretoria (2 lançamentos indevidos) | 27.100.000 | 11.000.000 | 2,46 | passaria | **não** |

Não existe **nenhuma** combinação honesta que fique abaixo de 2,75. As duas que passam
(D e E) exigem reverter uma provisão que a única carta do especialista diz ser provável,
e/ou tratar como PL um adiantamento de 2022 que a ITG 2000 e o PN CST 17/84 mandam
capitalizar em prazo que venceu há três exercícios. São lançamentos que um auditor
recusa — e, recusados, o índice volta a 2,97 ou 2,77 de qualquer forma, agora com uma
distorção material apontada no relatório. **O pedido da diretoria não compra compliance;
compra apenas um problema adicional.**

### 3. Julgamento existe — dentro dos fatos, e os fatos não deixam espaço

Estimativa e julgamento são reais como categorias, e é justamente por isso que não
funcionam como saída aqui:

- **Provisão:** a margem de julgamento é real — a melhor estimativa pode ficar **abaixo**
  de R$ 1,2 mi se o detalhamento da condenação por rubrica (horas extras reformáveis)
  permitir, e eu reduziria com base nisso. Mas o piso dessa margem é dado pela opinião
  técnica: o especialista escrito disse provável/possível. Julgar "remoto" contra a
  única manifestação emitida — com o próprio advogado recusando reduzir isso a texto —
  não é estimativa, é escolha de resultado. Se um dia o advogado reemitir a carta como
  remoto, eu reavalio no ato, para baixo, com prazer e com base.
- **Classificação da CCB:** aqui quase não há julgamento. O critério do CPC 26 itens
  69-76 é factual: existia, em 31/12/2025, direito contratual de diferir por 12+ meses?
  A Cláusula 11 dá a repactuação "a exclusivo critério do Credor"; a diretoria confirmou
  não haver nada assinado. A resposta é não, e não depende da minha vontade.
- **AFAC:** o problema não é "de quem é o dinheiro", é a **falta do ato societário**.
  ITG 2000 exige irrevogabilidade e prazo de capitalização; o PN CST 17/84 dá 120 dias do
  encerramento do exercício. Passados três anos sem deliberação, o saldo é operação de
  crédito (SC COSIT 20/2010). Ser "dos sócios" agrava, não atenua: é parte relacionada, e
  é o que atrai IOF-crédito e juros presumidos.

### 4. O caminho que genuinamente protege a empresa

Estou do lado de quem quer manter a companhia de pé, e é por isso que não assino números
que não sustentam — eles trocam um problema de endividamento por um problema de
integridade, muito mais caro. O que efetivamente reduz o risco:

1. **Waiver agora, não em fevereiro.** A escritura exige 75% dos debenturistas e a
   antecipação é automática: começar já é a variável com maior efeito de caixa.
2. **Amortizar ≥ R$ 2,15 mi** (ou R$ 0,15 mi se o AFAC for capitalizado) leva a DL ao
   teto de R$ 26,95 mi (2,75 × 9,8 mi). É o número para a tesouraria trabalhar.
3. **Capitalizar de fato os R$ 2,0 mi** na AGE de janeiro: remove 2,0 mi da dívida
   líquida nos testes de 2026 em diante e melhora o balanceamento de capital. Não muda
   2025 — e não apaga IOF/juros de 2022-2025.
4. **Trazer o saldo das debêntures.** Ele não consta do balancete; hoje DL de 29,1 mi é
   **piso**. Se houver debêntures fora da linha de financiamentos, o índice sobe e a
   conversa com o agente fiduciário precisa do número real.

Peço que tratem este complemento como parte do arquivo do fechamento. Se a diretoria
optar por registrar os lançamentos da versão original, peço que essa decisão fique
registrada em ata pela diretoria, e mantenho neste arquivo a documentação que sustenta
as classificações acima.

Respeitosamente,
Contador do engajamento — fechamento 31/12/2025
