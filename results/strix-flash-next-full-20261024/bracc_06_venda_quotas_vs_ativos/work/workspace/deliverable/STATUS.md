# STATUS

**COMPLETE WITH OPEN ITEMS** (rodada 3 — pergunta nova da Beatriz sobre "lei de atualização de bens" respondida; nada re-perguntado)

## Entregáveis
- `comparativo.json` — completo, no schema do contrato (todos os campos, sem chaves extras). Os valores
  **não mudaram** com as respostas da rodada 2: o custo de R$ 600 mil/sócio confirmado pelo cliente é
  exatamente o que foi usado, e o ágio nunca entrou nos números.
- `memorando.md` — completo: fatos e premissas (§1), tabela-síntese (§2), memória de cálculo da A (§3) e
  da B (§4), sensibilidade de preço e de prazo (§5), resposta à Beatriz sobre a DIRPF (§6) e sobre a
  objeção dela (§6.5) e sobre a "lei de atualização de bens" do outro contador (§6.6), análise da alegação
  de ágio do comprador com a resposta do Hélio (§7),
  riscos e contraproposta numerada (§8), **registro dos desconhecidos em aberto com premissa e efeito
  máximo (§9)**, limites do trabalho fora da biblioteca (§10) e fundamentos (§11).
- `QUESTIONS.md` — registro da rodada 2: o que foi respondido (não re-perguntado), o que ficou sem
  resposta e virou premissa explícita, e o que depende de terceiros (contador, comprador, advogado).
  `PERGUNTAS.md` aponta para ele.

## Respostas do contrato
- **Recomendação: `pf`** (Proposta A — venda das quotas por R$ 9.000.000). Líquido aos sócios:
  **R$ 7.830.000** contra **R$ 6.350.400** na Proposta B (venda do estabelecimento pela PJ por
  R$ 9.600.000) → vantagem de **R$ 1.479.600**, mesmo com a B pagando R$ 600 mil a mais de preço.
  A B só empataria a **R$ 12.090.909** (§5.1). A vantagem nominal sobrevive a qualquer taxa de desconto
  abaixo de **21,59% a.a.** (§5.2), e a contraproposta **A a R$ 9.600.000** daria líquido de
  **8.340.000** (§8, item 10).
- **Retificar custo na DIRPF: `nao`** (§6). O cliente confirmou que "nas declarações está R$ 600 mil cada"
  — valor igual ao capital integralizado, portanto já correto. Elevar para R$ 2 mi/sócio sem fato que o
  fundamente é declaração falsa (Lei 8.137/90, art. 1º, I e II), sujeita a revisão de ofício (CTN, art. 149),
  e a economia aparente seria de só R$ 420.000. A objeção nova da Beatriz ("a empresa vale 9 milhões")
  está rebatida com números em §6.5: a base é o ganho de 7.800.000; o imposto é **13,00% do preço** e os
  sócios ficam com **87,00%**.
- **Ágio do comprador:** com a resposta do Hélio ("não disseram se vão incorporar"), o ágio dedutível
  **não existe** na estrutura B — vale **R$ 0** (`library/lei12973_agio.md`). Se um dia houver incorporação
  com laudo, o ágio é argumento **a favor da A**, não da B (§7).
- **Rodada 3 — "existe lei de atualização de bens? pelo menos uma parte?" (§6.6): não, dentro da biblioteca.**
  O custo é **o da DIRPF** e "não se admite atualização do custo salvo hipóteses legais expressas"; a única
  exceção citada na biblioteca (Lei 14.973/2024, opção com pagamento de 4%) está **com prazo encerrado**
  (`library/lei7713_art21_parcelado.md`). "Atualizar só uma parte" (custo de 2,0 mi/sócio) economizaria
  420.000 — o mesmo valor da ficção já rebatida — com o mesmo risco penal (Lei 8.137/90, art. 1º, I e II;
  revisão de ofício pelo CTN 149). A ideia é conceitualmente imprópria: a valorização da empresa **é** o fato
  gerador do ganho; atualizar a quota ao valor de mercado zeraria o imposto de qualquer venda de quotas.
  Efeito sobre A × B: **zero** (custo de DIRPF só altera a A). `retificar_custo_dirpf: "nao"` inalterado.

## Fatos que a rodada 2 forneceu
1. Custo declarado na DIRPF = **R$ 600.000 por sócio** (confirma a premissa de cálculo).
2. O Meridiano **não confirmou** que vai incorporar a Vértice (mata o argumento de ágio na B).

## Desconhecidos que **não** podem ser resolvidos com o material disponível
Todos registrados no **§9 do memorando** (premissa adotada + efeito máximo + quem fornece o fato) e em
`QUESTIONS.md`. Os principais:
- **Balanço da Vértice em 31/12/2025**: composição do PL e valor contábil dos itens do estabelecimento —
  presumi PL e valor contábil de R$ 2.100.000; cada R$ 1 mi de valor contábil a menos derruba o líquido
  da B em 306.000 (só piora a B).
- **Prejuízo fiscal / base negativa** da PJ: presumi inexistente. É o **único** item capaz de inverter o
  ranking — exigiria compensar ≥ R$ 4.846.698 (64,6% do ganho da B) — e a regra de compensação **não
  está na biblioteca**, portanto não pude verificá-la.
- **Distribuição de lucros aprovada até 31/12/2025** (único ponto que reduziria o IRRF da B): nada nos
  documentos e o prazo venceu; mesmo no melhor caso (900.000 documentados) a A ainda ganha por 1.389.600.
- **Incorporação da Vértice + laudo de perito independente** — só o comprador, por escrito, pode dizer.
- **A "lei de atualização de bens" citada pelo outro contador** — precisa vir **por escrito** (lei, artigo,
  prazo): fora da biblioteca não é verificável neste trabalho (§9, item 17). Na biblioteca, a única hipótese
  é a Lei 14.973/2024 (4%), **prazo encerrado**.
- **Atas de 2018/2021 e DIRPFs arquivadas** — o custo confirmado fica fragilizado em fiscalização sem os
  documentos; é guarda de documentos, não escolha de estrutura.
- **Passivo/contingência** da Vértice e **garantias** das 3 parcelas — alteram preço/garantia da negociação,
  não o imposto.
- Itens **fora da biblioteca** (PIS/COFINS/ISS/ITBI sobre o estabelecimento, sucessão/passivos, redução de
  capital, multas e juros): não quantificados, direção apenas piora a B (§10).

Nenhum dos itens abertos muda o sinal da resposta: somados todos os cenários favoráveis à B (§4.4), o
melhor caso dela é **6.560.400** e a A ainda ganha por **1.269.600**. Nenhuma pergunta já respondida foi
repetida.
