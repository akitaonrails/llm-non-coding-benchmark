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
