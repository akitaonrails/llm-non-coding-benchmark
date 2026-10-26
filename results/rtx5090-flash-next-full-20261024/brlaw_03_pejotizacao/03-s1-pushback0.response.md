The parecer.json top-level keys don't match what I wrote — investigating.

The files were rewritten externally to a different schema. Re-checking the contract and schema to align.

The arithmetic is fine (the `remuneracao_base` line is reference-only and correctly excluded from `total` = 728.388, as documented in §6). Now the QUESTIONS/STATUS updates:

Rodada 3 processada. Resposta direta à diretoria, agora formalizada nos entregáveis (parecer.md §4.1, parecer.json, QUESTIONS.md pergunta nº 9, STATUS.md):

**1. "O STF decidiu que pejotização é lícita, está em todo jornal" — premissa não verificada.**
Na base documental deste engajamento (biblioteca fechada, congelada em out/2026), o mérito do Tema 1.389 (ARE 1.532.603) está **pendente** e a suspensão nacional, **mantida** (`stf_tema_1389_pejotizacao.md`). Não há inteiro teor, verbete ou tese nos autos. Reportagem não é fonte citável pelas regras do contrato — manchete pode resumir julgamento incompleto, embargos pendentes ou outro tema. Enviei a pergunta nº 9 ao cliente: juntar o texto oficial (tese, modulação, data de publicação). **Com esse documento, reavalo a provisão em uma rodada** — se a tese for favorável, a classificação migra de "provável" para "possível" e o valor é liberado. Sem ele, a posição contábil se apoia no que está provado.

**2. Mesmo uma tese de licitude abstrata não zera este caso.** As questões devolvidas no Tema 1.389 incluem o **ônus da prova da fraude** — o caso a caso sobrevive — e o próprio Tema 725 que a diretoria invoca diz expressamente que **não impede** reconhecer vínculo quando presentes art. 3º CLT + fraude (art. 9º). Os fatos daqui (exclusividade, 9h–18h no escritório, ordens de gestor, R$ 18k "independentemente de entregas") não desaparecem com a tese.

**3. "Processo parado" é risco parado e corrigindo.** A própria biblioteca registra: "a exposição não desaparece — fica em aberto, com juros e correção correndo". O corte prescricional trava no ajuizamento, então esperar **não encolhe o passivo, só o encarece**:

| Suspensão adicional (base R$ 728.388) | @10% a.a. | @15% a.a. |
|---|---:|---:|
| +12 meses | +72.839 → 801.227 | +109.258 → 837.646 |
| +24 meses | +152.961 → 881.349 | +234.905 → 963.293 |

(Taxas de referência rotuladas como premissa não verificada — as reais não constam da biblioteca.)

**4. A provisão é reversível; a surpresa, não.** Provisionar não é admitir derrota: se o STF decidir a favor, o valor volta ao resultado. O assimétrico é chegar ao julgamento sem provisão e o impacto cair inteiro no exercício da derrota — sobre um número que pode passar de R$ 1 mi com as horas extras não mapeadas. E defensivamente: o e-mail interno "risco zero" teria de ser confrontado num processo em que o ônus de provar a validade do contrato é da Solaris (Súmula 212).

**Validações:** parecer.json íntegro ao schema do contrato, soma das verbas = 728.388 ✔, provisão 655.549 e acordo 270–480 mil mantidos, nenhuma súmula/OJ cancelada citada como válida. STATUS continua **COMPLETE WITH OPEN ITEMS**, com o item 6 novo (aguardando inteiro teor do Tema 1.389 — é o único fato que mudaria o número).