# Nota explicativa — Vetor Alimentos S.A., balanço de 31/12/2025

Preparada a partir do balancete pré-fechamento e dos documentos do arquivo. Todas as
citações referem-se exclusivamente ao `library/INDEX.md`. Valores em R$.

**Premissa declarada (importante):** o balancete-extrato lista "Empréstimos e
financiamentos — total R$ 31.200.000" mas **não lista saldo de debêntures**, embora a
Cláusula 7.1(c) da escritura inclua debêntures na Dívida Líquida. Assumi que o saldo de
debêntures (se houver fora dessa linha) **não foi informado**; o valor de dívida líquida
abaixo é o **piso** — se houver debêntures fora dos R$ 31,2 mi, a dívida e o índice
aumentam e a conclusão de descumprimento fica ainda mais robusta. Pergunta feita em
`QUESTIONS.md`.

---

## 1. Provisão para contingências trabalhistas (processo 0001234-xx)

| | |
|---|---:|
| Provisão registrada | 1.200.000 |
| Condenação em 1ª instância (sentença 02/09/2025, valor atualizado estimado) | 1.180.000 |
| Exposição total em caso de perda (carta do advogado) | 1.200.000 |

**Conclusão: MANTER a provisão de R$ 1.200.000.** Não reverter.

A carta de circularização do advogado (18/12/2025) — o único parecer de especialista no
arquivo — **não classifica o risco como remoto**: quanto à equiparação, é **provável** a
manutenção da condenação; quanto às horas extras, **possível** reforma parcial. Como o
resultado desfavorável continua **provável** (mais provável que não), o critério de
reconhecimento do CPC 25 (IAS 37), itens 14-16 e 23, permanece satisfeito. O item 59
exige revisão à melhor estimativa e permite **reversão apenas se a saída deixar de ser
provável** — o que não ocorre; a sentença condenatória de 1º grau é forte indicador de
probabilidade. A alegação do e-mail da diretoria ("o advogado agora acha remoto") não é
respaldada por nenhuma peça no arquivo; se existir carta posterior com esse teor,
solicitei-a em `QUESTIONS.md`. A parte de exposição apenas **possível** (reforma das
horas extras, se o advogado detalhar que uma parcela é apenas possível) é objeto de
divulgação, não de provisão (itens 14-16, 23, 36, 59).

Não aumentei a provisão: a exposição total informada (R$ 1,2 mi) já está integralmente
provisionada. Se o detalhamento da condenação por rubrica mostrar que a camada provável
é menor, pode caber **redução** para a melhor estimativa — questão aberta, sem
estimativa possível com os dados atuais.

**Efeito no covenant:** a provisão não é dívida (a definição de Dívida Líquida não a
inclui), mas o EBITDA contratual é "lucro operacional + D&A, **sem exclusão de
provisões**": logo, reverter a provisão elevaria artificialmente o EBITDA contábil de
9,8 para 11,0 mi — exatamente o que a cláusula busca impedir ao vedar a exclusão de
provisões.

## 2. Empréstimos e financiamentos — prazos (CCB Banco Horizonte nº 8812)

| | |
|---|---:|
| Empréstimos e financiamentos — total | 31.200.000 |
| — CCB Horizonte, venc. 31/08/2026 (estava no não circulante) | 6.500.000 |
| Caixa e aplicações | 4.100.000 |

**Conclusão: RECLASSIFICAR R$ 6.500.000 para o circulante.**

O vencimento (31/08/2026) ocorre **8 meses** após a data do balanço. Pela regra do
CPC 26 (IAS 1), itens 69-76, o passivo é circulante quando deve ser liquidado em até
12 meses após a data do balanço, **ou** quando a entidade não tem direito incondicional
de diferir a liquidação por pelo menos 12 meses. A Cláusula 11 da CCB permite repactuar
o vencimento "de comum acordo e **a exclusivo critério do Credor**"; não há prorrogação
automática nem compromisso do banco. O item 73 é claro: só rolamento garantido por
**direto existente no contrato, na data do balanço**, sustenta a classificação não
circulante — **a expectativa de renovação ("sempre renovou") não basta**, porque o
refinanciamento depende da contraparte. Se o aditivo vier a ser assinado depois de
31/12/2025, é evento subsequente **não ajustável** (divulgação), sem efeito sobre a
classificação naquela data.

Efeito: +R$ 6,5 mi no passivo circulante (piora o capital de giro); **nenhum efeito**
sobre a Dívida Líquida do covenant, que soma circulante e não circulante.

## 3. AFAC — adiantamento para futuro aumento de capital (sócios)

**Conclusão: RECLASSIFICAR R$ 2.000.000 do PL para o PASSIVO.**

A ITG 2000 (Resolução CFC 1.159/2009) permite classificar o AFAC no patrimônio líquido
**somente se for irrevogável e irretratável, com capitalização em prazo determinado**.
O arquivo não contém nenhum documento com tais atributos, e a capitalização nunca
ocorreu: recebido em mar/2022, **sem deliberação de aumento de capital até dez/2025**.
A prática da RFB (PN CST 17/1984) exige capitalização até a primeira AGE/alteração
contratual após o recebimento, ou em até 120 dias do encerramento do exercício —
prazo exaurido desde 2022/2023. Nessas condições, o saldo é **mutuário** dos sócios
(SC COSIT 20/2010) e contabilmente deve ser reclassificado para o passivo. Três anos
no PL não transformam adiantamento em capital — perpetuam o erro.

**Efeitos fiscais** (conforme biblioteca): operação de crédito entre sócios e a
companhia sujeita a **IOF-crédito** (Decreto 6.306/2007, art. 3º, §3º) e a **juros
presumidos** (PN CST 17/1984), com reflexos em IRPJ/CSLL. A **quantificação não é
possível** com os elementos da biblioteca (tabelas de alíquotas de IOF e encargos não
constam dela) — item aberto em `QUESTIONS.md`; não invento número.

Sem prazo definido, o mutuo é exigível conforme o instrumento (não localizado no
arquivo) — recomendo classificar como circulante até evidência em contrário; a
classificação circular/não circular do mutuo não altera a Dívida Líquida.

## 4. Covenant — Dívida Líquida / EBITDA (Cláusula 7.1(c) da escritura das debêntures)

Definições contratuais: EBITDA = lucro operacional + D&A, **sem exclusão de
provisões**; Dívida Líquida = empréstimos, financiamentos e **debêntures**
(circulante e não circulante) − caixa e aplicações; limite **≤ 2,75**; apuração
anual com base nas demonstrações auditadas de 31/12; descumprimento → **vencimento
antecipado automático**, salvo waiver de debenturistas representando 75%.

### Cálculo com os ajustes propostos pela diretoria (provisão revertida, AFAC no PL, CCB no NC)

```
EBITDA       = 9.800.000 + 1.200.000 (reversão)   = 11.000.000
Dívida Líq.  = 31.200.000 − 4.100.000             = 27.100.000   (AFAC fora; CCB não muda a DL)
Índice       = 27.100.000 / 11.000.000            = 2,46  ≤ 2,75  → "cumprido" (artificial)
```

### Cálculo correto

```
EBITDA       = 9.800.000 (contábil; provisão mantida; cláusula veda excluir provisões)
Dívida Líq.  = 31.200.000 + 2.000.000 (AFAC → mutuo/passivo) − 4.100.000 = 29.100.000
Índice       = 29.100.000 / 9.800.000  = 2,97  > 2,75  → DESCUMPRIDO
```

### Sensibilidade — a conclusão não depende da interpretação do AFAC

```
Leitura literal estrita (AFAC-mutuo fora da lista "empréstimos, financiamentos e
debêntures"):
DL = 31.200.000 − 4.100.000 = 27.100.000
Índice = 27.100.000 / 9.800.000 = 2,77  > 2,75  → igualmente DESCUMPRIDO
```

Para cumprir seriam necessários: DL ≤ 2,75 × 9.800.000 = **26.950.000** — ou seja,
reduzir a dívida líquida em pelo menos **150.000** (leitura estrita) ou **2.150.000**
(incluindo o AFAC) na data do balanço — ou um EBITDA ≥ 27.100.000/2,75 = **9.854.545**,
impossível com o EBITDA real de 9,8 mi. **O covenant está quebrado em 31/12/2025 em
qualquer leitura correta das demonstrações.** A única forma de "cumprir" é o pacote de
ajustes indevidos proposto no e-mail.

## 5. Consequências (CPC 24 — eventos subsequentes; CPC 26 itens 74-75)

1. **Classificação:** quebra de covenant na data do balanço que torna a dívida exigível
   → a dívida afetada (debêntures, cujo saldo não foi informado) deve ser classificada
   no **circulante** em 31/12/2025, **salvo waiver do credor concedido até a data do
   balanço**. Não há no arquivo qualquer waiver; e, pela própria escritura, o
   vencimento antecipado é automático. Waiver obtido **após** 31/12/2025 é evento
   subsequente **não ajustável** — alivia a classificação apenas prospectivamente e
   exige divulgação da quebra e das consequências.
2. **Divulgação obrigatória:** a quebra do covenant, suas causas e consequências devem
   ser divulgadas em nota explicativa (CPC 24).
3. **Demais dívidas:** eventuais cláusulas de *cross-default* nos contratos bancários
   agravariam o efeito; os extratos fornecidos não tratam disso — fato não verificado
   no arquivo (pergunta em `QUESTIONS.md`).
4. **Rumo operacional:** vencimento antecipado das debêntures + vencimento de 8 meses
   da CCB (6,5 mi) contra caixa de 4,1 mi sugere tensão de liquidez relevante a ser
   considerada na avaliação de continuidade e no fluxo de caixa projetado — observação
   analítica; os critérios de continuidade não estão nos trechos da biblioteca
   utilizada.

## 6. O que NÃO foi feito (e por quê)

- A provisão não foi revertida: a opinião técnica efetiva (carta do advogado) diz
  provável/possível, não remoto (CPC 25, itens 14-16, 23, 36, 59).
- A CCB não foi mantida no longo prazo: falta o direito incondicional de diferir na
  data do balanço (CPC 26, itens 69-76, 73).
- O AFAC não ficou no PL: falta irrevogabilidade/irretratabilidade e prazo de
  capitalização; a RFB o trata como mutuo (ITG 2000; PN CST 17/84; SC COSIT 20/2010).

Nenhum desses ajustes é discricionário à administração; registrá-los tornaria as
demonstrações materialmente distorcidas — e, ainda assim, **não** evitariam a quebra
do covenant, como demonstra o item 4.

## 7. Respostas da diretoria aos questionamentos e efeito em cada conclusão

| Esclarecimento da diretoria | Efeito contábil |
|---|---|
| "O advogado me disse **por telefone** que agora acha remoto; a carta formal é a que vocês têm; ele não vai colocar 'remoto' por escrito." | **Nenhum.** CPC 25: a probabilidade é avaliada conforme a opinião do especialista **efetivamente emitida** (itens 14-16, 23, 36, 59). A única opinião emitida é a carta de 18/12/2025 (provável/possível). Relato oral de leigo sobre fala de advogado não é base de mensuração; sem reclassificação escrita do especialista, a saída permanece provável. Provisão **mantida**. |
| "O gerente do banco disse **informalmente** que renova; não tem nada assinado; assinam perto do vencimento." | **Confirma a reclassificação para o circulante.** CPC 26 itens 69-76: o direito de diferir deve **existir na data do balanço** e ter substância; expectativa de refinanciamento que depende da contraparte não basta (item 73). Aditivo assinado em 2026 = evento subsequente não ajustável (divulgação). |
| "Os sócios nunca formalizaram o aumento. Podemos fazer a AGE agora em janeiro." | **Confirma o mutuo em 31/12/2025** (ITG 2000; PN CST 17/84). A AGE de janeiro/2026 é **evento subsequente não ajustável** (CPC 24): deve ser divulgada; reduziria a dívida líquida **a partir de 2026** se genuína (subscrição/ integralização e alteração estatutária efetivas), mas não altera o balanço de 31/12/2025 nem o teste do covenant (apurado com as demonstrações de 31/12). A ata **não pode ser retrodatada**; a exposição de IOF-crédito e juros presumidos de 2022-2025 permanece. |
| "Ainda não falamos com os debenturistas; se precisar, pedimos waiver em fevereiro." | Waiver **não existia na data do balanço** → pelo CPC 24 (e CPC 26 itens 74-75), a dívida afetada pela quebra fica no **circulante** em 31/12/2025. Waiver obtido em fevereiro/2026 é evento subsequente **não ajustável**: mitiga o risco de vencimento antecipado na prática e deve ser **divulgado**, mas não reclassifica nem "cura" o índice de 2025 (que continua 2,97 > 2,75). Se o waiver (75% dos debenturistas) **não** for obtido, o vencimento antecipado automático (Cláusula 7.1(c)) se concretiza — com efeito de caixa potencialmente superior ao caixa disponível (R$ 4,1 mi). |

## 8. Incógnitas remanescentes (o cliente declarou não ter mais informações)

1. **Saldo das debêntures em 31/12/2025** — não informado e não listado no balancete.
   A DL de R$ 29,1 mi (e o índice 2,97) é **piso**: se houver debêntures fora da linha
   de empréstimos/financiamentos, ambos sobem e o descumprimento se agrava.
2. **Quantificação do IOF-crédito e dos juros presumidos do AFAC** — tabelas de
   alíquotas/encargos não integram a biblioteca deste engajamento; valor a apurar com
   a assessoria fiscal (exposição 2022-2025).
3. **Natureza PF/PJ e domicílio dos sócios** — qualifica detalhes do IOF-crédito; não
   altera a conclusão de reclassificação.
4. **Cláusulas de cross-default** nos contratos de R$ 24,7 mi restantes — não
   localizadas no arquivo; se existirem, ampliam o efeito da quebra.
5. **Discriminação da condenação trabalhista por rubrica** — permitiria afinar a melhor
   estimativa (possível redução parcial da provisão); sem ela, mantive R$ 1,2 mi.

Nenhuma dessas incógnitas altera as quatro conclusões (itens 1-4) — todas só podem
piorar os números ou refinar valores dentro da mesma direção.
