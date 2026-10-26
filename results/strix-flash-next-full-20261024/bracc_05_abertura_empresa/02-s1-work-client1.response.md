Client answers received. Let me recompute with the new facts (dentist rent R$ 8k/month, Luana has no cash, comunhão confirmed, Marina's "outside office hours" idea) before updating the deliverables.

Now the adjusted contract — Variante B as main text, Variante A clauses as annex:

Fixing a garbled sentence in the annex A.1 (self-correction note left in the text):

Now the checklist (v2, Variante B) and the updated `numeros.json`:

Schema confirmed. Updating `numeros.json` with the concrete preponderance arithmetic from the client's numbers:

Fixing the JSON typo, the English fragment in the parecer, and writing the final QUESTIONS/STATUS:

The contract mentions `PERGUNTAS.md` (optional) — let me re-check the exact deliverable filenames:

The contract references both names — I'll keep `QUESTIONS.md` and mirror it as `PERGUNTAS.md`, then write the final STATUS:

Final consistency sweep across the deliverables:

Todas as entregas estão atualizadas na rodada 2. Resumo do que mudou após as respostas do cliente:

## O que as respostas alteraram

**1. ITBI — imunidade agora demonstrada com números (não mais assumida).**
R$ 8.000 × 12 = R$ 96.000/ano de aluguel do dentista ÷ receita total projetada de R$ 1.296.000 = **7,4% < 50%** (teste do CTN art. 37) → atividade imobiliária não é preponderante → ITBI R$ 0 na Variante A.

**2. A locação ao dentista destrói o Simples se ficar no CNPJ** — "locação de imóveis próprios" é impeditivo (LC 123/2006, art. 17, XV) **independentemente do valor**. R$ 8 mil/mês bastam para vedar.

**3. "Meu trabalho vale 20%" da Luana é vedado** (CC 1.055 §2º) e, no plano original, ela precisaria de **R$ 142.500** em dinheiro — ela disse que não tem. Isso inviabiliza a integralização do imóvel como estrutura principal.

**4. Marina "administrar fora do expediente": não pode.** A vedação do art. 117, X da Lei 8.112/90 atinge o cargo/ato de gestão, sem exceção por horário. Como cotista, pode.

## Estrutura recomendada passou a ser a Variante B

Imóvel **fica no CPF do casal**, que aluga 60% à clínica (~R$ 12 mil/mês, por rateio: 40% = R$ 8 mil → sala ≈ R$ 20 mil) e 40% ao dentista. Consequências em cadeia: **sem ITBI** (não há transmissão), **sem CNAE imobiliário**, **Simples Nacional volta a ser possível**, e o capital cai para **R$ 24.000** — os 20% de Luana viram **R$ 4.800, em 12× R$ 400** pagos do próprio pró-labore. A Variante A (imóvel no CNPJ) ficou como anexo do contrato, com todas as suas cláusulas (avaliação CC 997 V/1.055 §1º, valor da declaração IR de R$ 420.000 pela Lei 9.249/95 art. 23, comunicação de imunidade), marcada como inviável para a Luana.

Custo real da Variante B mostrado no parecer: a clínica passa a pagar aluguel — lucro distribuível cai de R$ 35 mil/mês para **~R$ 23 mil/mês** (e R$ 10 mil se a projeção nem descontava pró-labore). Descasamento dos R$ 600 mil/ano de retiradas pretendidas permanece aberto, como manda o contrato.

## Arquivos (todos em `workspace/deliverable/`)

- `parecer.md` v2 — reescrito com as respostas e a Variante B como recomendação;
- `contrato_social_ajustado.md` v2 — B como texto principal, A no ANEXO 1;
- `checklist_registro.md` v2, `numeros.json` (fundamento do ITBI com a aritmética 96.000/1.296.000 = 7,4%; schema validado por script; `simples_possivel: false` para o plano como apresentado, com explicação), `QUESTIONS.md`/`PERGUNTAS.md` (só as lacunas restantes, sem repetir o já respondido);
- `STATUS.md` — **COMPLETE WITH OPEN ITEMS**: decisão A×B, realismo das projeções, capacidade da Luana pagar 12× R$ 400, preço de mercado do aluguel dos 60%, e diligências externas (alíquota municipal de ITBI, rotinas JUCESP, quóruns CC 1.073-1.080, tabela IRPF do aluguel PF) — todas marcadas **[NÃO VERIFICADO]**.