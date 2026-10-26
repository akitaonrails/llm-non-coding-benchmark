O cliente confirmou a **existência** de brindes e de uma doação não qualificada — mas não deu valores. Vou registrar isso, refutar a justificativa do crédito e preparar o impacto fiscal.

Li as respostas do cliente e processei. Três delas mudam o quadro — e uma não muda nada.

## O que a resposta do cliente fez

**1. "É papel e toner da sede. O fornecedor destacou PIS/COFINS, então creditamos."**
Isso **não** salva o crédito — confirma o erro. O destaque do fornecedor só mostra o tributo que *ele* pagou na venda (e é justamente o que faz o PIS/COFINS entrar no nosso custo: 120.000,00 + 11.100,00 = 131.100,00). Crédito não cumulativo depende de o bem ser **insumo**, não de haver destaque na nota — e "papel e toner da sede" (uso administrativo, CFOP 1556) é a descrição exata do que não é insumo. Estorno **AJ-01 mantido**: PIS/COFINS a recolher em janeiro = **R$ 79.883,00** (a Atlas apurou 68.783,00).

**2. "Vinho e canivete gravado pros 400 melhores clientes. Marketing, ora."**
O cliente confirmou o brinde e, sem perceber, confirmou a indedutibilidade. O art. 13, VII da Lei 9.249/95 veda a despesa com brindes **"independentemente do disposto no art. 47 da Lei 4.506/64"** — o artigo não pergunta em que conta a despesa caiu. "É marketing" é argumento contábil; para IRPJ/CSLL não produz efeito.

**3. "Associação Luz é ONG do bairro, não tem título nenhum."**
Fechou a única porta que existia: a exceção do art. 13, § 2º, II exige entidade **reconhecida como de utilidade pública federal ou qualificada como OSCIP**. Sem título → doação **integralmente indedutível**. E mesmo no melhor cenário o teto seria 2% do lucro operacional: janeiro dá 156.483,00 × 2% = **R$ 3.129,66** — a exceção se mede em milhares, não em dezenas de milhares.

**4. Valor: o cliente não tem.** Então não lancei número nenhum. A vedação do art. 13 só atua no e-LALUR (Parte A), sem tocar a contabilidade societária — janeiro fecha normal; o que fica travado é a quantificação do IRPJ/CSLL. Registrei o teto material (4.2.02 = 85.000,00 e/ou 4.2.03 = 96.000,00 → 181.000,00) como **limiar, não fato**, e a exposição: cada R$ 1.000 omitidos custa R$ 168,00 com a trava de 30% (a adição aumenta o próprio teto, então o lucro real sobe só 0,70×) — cenário completo de **R$ 14.280,00 a R$ 43.078,00**.

## Onde o engajamento está

**BLOCKED.** O `documents/` só tem janeiro (`mes_01/razao.csv`, `balancete.csv`, a NF-e 8812), as aberturas e o e-mail do diretor. **Não há razão nem balancete de fevereiro e de março** — sem eles, `mes_02/*`, `mes_03/*`, `lalur.json` e `memoria.md` não podem ser feitos com números reais, e eu não fabrico saldo de mês sem documento.

Arquivos atualizados/criados:
- `deliverable/STATUS.md` — engajamento **BLOCKED**; sessão 1 **COMPLETE WITH OPEN ITEMS**
- `deliverable/QUESTIONS.md` — rodada 2: só o pedido dos dados de fev/mar + **2 perguntas novas** (competência dos brindes/doação — se forem de 4T2025, o ajuste é de e-LALUR/ECF 2025; e se existe algum comprovante). O que ficou sem resposta virou assunção declarada, não pergunta repetida.
- `deliverable/mes_01/brindes_doacoes.md` — novo: qualificação, limite de 2%, tabela de exposição por cenário e as opções (a) enviar valor / (b) autorizar o teto / (c) instruir por escrito para não adicionar
- `deliverable/mes_01/ajustes.json` — refutação do "destaque" na observação do AJ-01, os dois itens não ajustados (brinde e doação) e o bloco `correspondencia_cliente` com as duas instruções **não atendidas** ("não mexer" e "compensar todo o prejuízo" — para compensar 900.000,00 seria preciso lucro ajustado trimestral de 3.000.000,00, pela trava de 30%)
- `deliverable/mes_01/pendencias.md` — item 1 com a refutação, item 3 reescrito, novos 3.1 (competência) e 3.2 (fev/mar ausentes)