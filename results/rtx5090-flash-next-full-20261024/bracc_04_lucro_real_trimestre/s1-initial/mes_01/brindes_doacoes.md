# Brindes e doações — qualificação fiscal e exposição (Atlas Distribuidora S.A.)

Working paper da sessão 1 (01/2026), aberto em razão do comentário da auditoria interna citado em
`documents/email_diretor.txt` e atualizado com a **resposta do cliente de 26/10/2026**.
Tributos afetados: **IRPJ (lucro real) e CSLL** do 1º trimestre/2026 — apuração em
`deliverable/mes_03/lalur.json` (Parte A). Não afeta PIS/COFINS nem a contabilidade societária.

---

## 1. O que se sabe, e de onde veio

| Item | Informação | Fonte | Natureza |
|---|---|---|---|
| Brinde existe, é material e foi distribuído a clientes | "vinho e canivete gravado pros 400 melhores clientes. Marketing, ora." | resposta do cliente, 26/10/2026 | fala do cliente (não documentada) |
| Empresa considera a despesa "marketing" (dedutível) | mesma frase; e `documents/email_diretor.txt`: "brinde é despesa comercial, sempre foi" | cliente | posição do cliente |
| Houve benefício à Associação Luz, entidade **sem** título de utilidade pública federal e **sem** qualificação de OSCIP | "A Associação Luz é uma ONG do bairro, não tem título nenhum. O presidente conhece o dono." | resposta do cliente, 26/10/2026 | fala do cliente (não documentada) |
| **Valor de ambos: não informado** | "For questions not answered above, the client has no additional information." | cliente | lacuna documental |
| Nenhum documento no arquivo evidencia brindes/doação | busca em `documents/` (razão, balancete, NF-e 8812, aberturas) não localiza brinde, doação, vinho, canivete ou Associação Luz | conferência própria | fato verificado por nós |

Conclusão factual: **as duas despesas indedutíveis existem, mas não são quantificáveis** com o material
disponível. O que existe no razão de janeiro é genérico: 4.2.02 *Despesas comerciais* R$ 85.000,00
(ref `COM`, 20/01/2026) e 4.2.03 *Despesas administrativas* R$ 96.000,00 (ref `ADM`).

## 2. Qualificação fiscal (o que a biblioteca resolve)

**(a) Brindes — vedação legal, não classificação contábil.**
Lei 9.249/95, art. 13, VII: são vedadas, para o lucro real **e** para a base de cálculo da CSLL, as
deduções "das despesas com brindes", *independentemente do disposto no art. 47 da Lei 4.506/64*
(`library/lei9249_art13.md`). Ou seja: o art. 13 não pergunta onde a despesa foi contabilizada. O
argumento do cliente ("é marketing, sempre foi") é contábil e **não produz efeito fiscal** — vinho e
canivete gravado entregues a 400 clientes, sem Revenda e sem contrapartida de preço, são brinde.
Tratamento devido: **adição na Parte A do e-LALUR** do trimestre, pelo valor total da despesa
(`library/irpj_csll_trimestral.md`: "despesas indedutíveis são adições na Parte A; não se altera a
contabilidade societária (CPC), apenas a apuração fiscal").

**(b) Doação à Associação Luz — fora da exceção, logo indedutível.**
Lei 9.249/95, art. 13, VI: vedadas "as doações, exceto as referidas no § 2º". As exceções são
taxativas: I — projetos culturais (Lei 8.313/91); II — entidades civis sem fins lucrativos que prestem
serviços gratuitos a empregados/dependentes da doadora ou à comunidade, **reconhecidas como de
utilidade pública federal ou qualificadas como OSCIP**, até 2% do lucro operacional; III — instituições
de ensino e pesquisa sem fins lucrativos, até 1,5% (`library/lei9249_art13.md`).
O cliente afirma que a entidade "não tem título nenhum" → **não** satisfaz o requisito de
credenciamento do § 2º, II, e não se enquadra em I nem III → **doação integralmente indedutível**.
O vínculo pessoal ("o presidente conhece o dono") é irrelevante para essa conclusão; se houver
relação/partes relacionadas envolvida, a biblioteca **não** contém norma aplicável → ponto não
verificável, apenas registrado.

**(c) Mesmo no melhor cenário a dedução seria mínima.** Se a Associação Luz fosse qualificada no
§ 2º, II, a dedução seria limitada a 2% do lucro operacional. Lucro operacional de janeiro:
2.127.250,00 (receita líquida = 2.540.000,00 − 234.950,00 PIS/COFINS − 177.800,00 ICMS)
− 1.397.000,00 CMV − 210.000,00 pessoal − 85.000,00 comerciais − 96.000,00 administrativas
− 131.100,00 material (já bruto do estorno AJ-01) − 51.667,00 depreciação = **156.483,00**
(despesas financeiras de 28.000,00 são não operacionais nessa montagem).
Limite: 156.483,00 × 2% = **R$ 3.129,66** (e 1,5% = R$ 2.347,24 para ensino/pesquisa). Portanto, uma
doação de qualquer monta relevante jamais seria dedutível em sua totalidade — o teto da exceção está
em milhares de reais, não em dezenas de milhares.

## 3. Por que nenhum valor foi lançado

- Não medimos o que não existe em documento: lançar R$ 85.000,00 (ou qualquer número) de adição seria
  **inventar fato**, e o valor errado produz tributo errado para mais ou para menos.
- A vedação do art. 13 não altera a contabilidade societária, só a apuração fiscal
  (`library/irpj_csll_trimestral.md`); portanto a ausência do valor **não impede fechar janeiro** —
  impede **quantificar o IRPJ/CSLL do trimestre**.
- Consequência assumida e declarada: se o valor não aparecer até março, o `lalur.json` de março traz a
  linha de adição **aberta/não quantificada** e o e-LALUR será entregue com ressalva expressa na
  `memoria.md`, com o risco de tributo pago a menor medido pela tabela abaixo. Não assinaremos um
  e-LALUR como correto nesse cenário.

## 4. Exposição (limiares — NÃO são fatos apurados)

Teto materialmente possível em janeiro: 4.2.02 R$ 85.000,00 (conta onde a própria empresa diz que o
brinde fica) e/ou 4.2.03 R$ 96.000,00 → teto conjunto R$ 181.000,00.

Efeito de **R$ 1.000,00** de adição de brinde/doação, no trimestre, com a trava de 30% em vigor
(saldo de prejuízo fiscal disponível: R$ 900.000,00 — `documents/saldos_fiscais_abertura.md`):
a adição aumenta o lucro líquido ajustado; a compensação é limitada a 30% dele
(Lei 9.065/95, arts. 15-16 — `library/lei9065_art15_trava.md`), então **o lucro real sobe só 70%** do
valor adicionado: 1.000,00 × 0,70 = 700,00 → IRPJ 15% = 105,00 + CSLL 9% = 63,00 = **168,00**;
se o lucro real trimestral passar de R$ 60.000,00, soma-se adicional de 10% sobre 700,00 = 70,00 →
**238,00 por 1.000,00 adicionados** (23,8%).

| Hipótese (teto, não apurada) | Adição X | Lucro real +0,70X | IRPJ 15% | CSLL 9% | Adicional 10% | Total | % de X |
|---|---:|---:|---:|---:|---:|---:|---:|
| só 4.2.02 | 85.000,00 | 59.500,00 | 8.925,00 | 5.355,00 | 5.950,00 | **20.230,00** | 23,8% |
| 4.2.02 + 4.2.03 | 181.000,00 | 126.700,00 | 19.005,00 | 11.403,00 | 12.670,00 | **43.078,00** | 23,8% |
| idem, sem adicional (lucro real trimestral ≤ 60.000,00) | 85.000,00 | 59.500,00 | 8.925,00 | 5.355,00 | — | 14.280,00 | 16,8% |
| idem, sem trava **e sem** saldo a compensar (hipótese contra legem, só para medir) | 181.000,00 | 181.000,00 | 27.150,00 | 16.290,00 | 18.100,00 | 61.540,00 | 34,0% |
| idem, sem trava **com** saldo suficiente (contra legem) | 181.000,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 no trimestre | 0% agora — consome saldo; o tributo sai dos trimestres futuros |

Leitura: cada real de brinde/doação não identificado custa entre **R$ 0,168 e R$ 0,34** de tributo (no caso
da Atlas, com a trava e o adicional de 10% incidindo, **R$ 0,238**). A interação com a trava é o ponto
contraintuitivo: a adição aumenta o próprio teto de 30%
(cap = 30% × lucro ajustado), por isso o impacto líquido é 0,70×, e não 1,00×. A linha contra legem não
gera economia: ela só **move** o tributo para os trimestres seguintes (e depende de haver lucro lá —
prazo do crédito não está na biblioteca, U-17).

## 5. O que resolveria (documento, não opinião)

1. Notas fiscais de remessa de brinde / pedidos / lista dos 400 clientes / custo unitário de vinho e
   canivete gravado, segregadas por competência.
2. Comprovante da transferência ou do benefício à Associação Luz (extrato, recibo, contrato de patrocínio).
3. Relatório da auditoria interna que originou o comentário — ele presume valor conhecido por eles.
4. **Competência**: se os brindes/doação são de 4T2025, a correção é do e-LALUR/ECF do exercício de
   2025 (retificação de exercício anterior), fora do escopo deste trimestre; se são de 1T2026, entram
   no e-LALUR de março. Sem essa informação, a adição fica alocada no 1º trimestre/2026 por
   assunção — assunção declarada, não fato.

## 6. Alternativas de tratamento (só com instrução escrita do cliente)

- **Travar o teto** (adicionar 85.000,00 ou 181.000,00): superestima a adição → tributo a maior. É a
  alternativa de menor risco de autuação, mas paga tributo indevido e distorce a demonstração fiscal.
- **Não adicionar nada**: subestima o IRPJ/CSLL; posição que **não podemos** apresentar como correta
  diante do art. 13, VI e VII.
- Nenhuma das duas foi adotada por decisão nossa. Aguardamos quantificação ou instrução formal.

Não há, na biblioteca (`library/INDEX.md`), norma sobre PIS/COFINS/ICMS/IPI na remessa de brindes nem
sobre doação de bens; esses possíveis desdobramentos **não foram analisados** e não devem ser lidos
como conformidade.
