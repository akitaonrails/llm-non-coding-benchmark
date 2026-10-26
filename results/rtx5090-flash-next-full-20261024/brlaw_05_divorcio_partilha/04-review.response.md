Good discipline to demand a QA pass. Let me re-read the source documents and the remaining library pieces, then audit every citation and every number across the five deliverables.

Fontes conferidas. Agora a auditoria: origens dos fatos, citações e aritmética em todos os entregáveis.

Agora os dois entregáveis restantes e a peça do STJ (para conferir "3ª T." e as citações literais do §9):

Citações da biblioteca confirmadas (inclusive as literais do §9 e "3ª Turma/2020"). Faltam dois documentos-fonte para checar fatos que usei ("João Andrade", "resolver rápido"):

Fontes confirmadas: "João Andrade" e "resolver rápido e sem briga" e "guarda compartilhada" e "dívida do carro é dela" — tudo real nos documentos. Agora vou reler os trechos exatos que preciso editar:

Tenho todo o texto exato. Uma última checagem da literalidade do FGTS no resumo antes de editar o Q7:

Confirmado: "saldo integral depositado durante o casamento". Aplicando todas as correções agora:

Correção 1 aplicada. Agora as correções 2 e 3 (origem dos 400k e "unificado"):

Agora correções 4, 5 e 6:

Mais duas menções à "estimativa verbal" dos 400k para consistência (partilha.json linha 45 e STATUS linha 16):

Code Mode é JavaScript — vou rodar a validação em Python via shell:

Tudo validado. Uma leitura final do parágrafo reescrito do §7 para garantir que ficou legível:

Revisão de QA concluída e tudo revalidado por script. Segue a lista do que mudou:

## Erros encontrados e corrigidos

**1. Balanço da proposta de Fernanda estava errado (proposta §7 + STATUS).** O número anterior ("ela receberia ≈ 1.720.000 → excesso de +515.000") não se reconstruía a partir das palavras literais dela e tinha sinais trocados nos itens de carro e PGBL (ela fica com ambos nos **dois** esquemas → delta 0, não −45.000/±100.000). Reescrevi com aritmética exposta: como a proposta dela ("metade de tudo que está no nome do Marcelo") é muda sobre o apartamento — que está no nome de **ambos** — e sobre os financiamentos, o valor a ela é uma **faixa de 1.300.000 a 1.900.000** (excesso de **+95.000 a +695.000** vs. meação de 1.205.000), e mostrei que em todas as leituras a soma dos dois lados fecha em 3.490.000 ✔. O núcleo juridicamente indefensável é idêntico em qualquer leitura: Atibaia +400.000 + quotas +200.000 = 600.000, compensado só pelo FGTS de que ela abre mão (−70.000).

**2. Aritmética interna quebrada no `partilha.json` (linha TOTAL).** Dizia "Marcelo fica com 1.200.000 (apto líq.)", mas a soma dessa própria frase daria 2.585.000 ≠ 2.285.000. Corrigido para "900.000 (apto líq. = 1.200.000 − 300.000 do financiamento que ele assume)" — o total 2.285.000 sempre esteve certo; a parcela escrita, não.

**3. Risco de dupla contagem do PGBL (§3 e partilha.json).** "Ela compensa Marcelo com 45.000 — já absorvido no caixa" podia ser lido como pagamento adicional. Reescrito: a compensação de 45.000 **já está líquida dentro do caixa de 985.000; não há pagamento adicional, sob pena de dupla contagem**.

**4. Fundamentação exagerada ("autoridade não suportada").** "Precedente **unificado** de Seção" (2×) não tem apoio na biblioteca — ela só diz "2ª Seção, 2017". Suavizado para "precedente da 2ª Seção (2017)".

**5. Fato mal atribuído: os 400.000 da empresa em 2014.** Eu tratava como "só estimativa verbal do cliente", mas o **próprio resumo de documentos registra** "valor em 2014: R$ 400.000,00; lucros reinvestidos" — que inclusive reforça a tese dos lucros reinvestidos no §9. Corrigido em §8, §8.2, §9, partilha.json e STATUS: registro documental + confirmação verbal, mas **sem laudo/balanço de 2014** (o risco de perícia adversa permanece como estava).

**6. Ajustes menores.** Delta de pensão "≈32.000–75.000" → "≈31.000–75.000/ano" com o cálculo explícito (31.000 a 75.200); QUESTIONS Q7 agora cita o literal do resumo ("saldo integral depositado durante o casamento"); títulos de QUESTIONS/STATUS diziam "2 rodadas" → "3 rodadas (a 3ª é objeção, não pergunta)"; erro de concordância "casamento iniciados" → "iniciado"; no balanço do §7 acrescentei que "metade das quotas em espécie" é **inexequável** (sem ingresso na sociedade — REsp 1.595.775) e somei o delta alimentar ao contraste econômico.

## O que foi checado e não precisou mudar
- **Fontes factuais**: formal de partilha (inventário "João Andrade", 620.000, matrícula 11/2019), e-mail do cliente ("resolver rápido e sem briga", guarda compartilhada, dívida do carro) — tudo real, nada fabricado.
- **Citações da biblioteca**: frases literais do §9 ("integram o patrimônio comum e devem ser partilhados"; "o art. 1.659, VI, não afasta..."), "3ª Turma (REsp 1.698.774)", ITCMD 4%/ITBI 3% SP, CC 1.584 §2º — todas conferidas palavra por palavra.
- **Números centrais** (massa 2.770.000, líquido 2.410.000, meação 1.205.000, caixa 985.000, prova 3.490.000) e o `alimentos.json` — validados, intactos.

Revalidação final por script: JSONs parseiam, todas as somas fecham (inclusive os 3 cenários do novo balanço, cada um somando 3.490.000), e nenhuma string antiga (1.720.000, 515.000, "unificado", etc.) permanece em nenhum entregável. Nada foi forçado para fechar — a única coisa que virou faixa expressa (o balanço da proposta adversa) reflete ambiguidade real da própria proposta dela.