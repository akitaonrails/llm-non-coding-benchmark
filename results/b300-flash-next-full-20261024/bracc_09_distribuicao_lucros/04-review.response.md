

Let me systematically re-audit: (1) verify every citation maps to the library INDEX or client documents, (2) re-verify all arithmetic, (3) check internal consistency across the three deliverables.





Now the premissas list, JSON notes, and STATUS:









All corrections are applied. Now the post-edit validation — JSON parse check and cross-file consistency scan:






Revisão concluída e validada. Todos os entregáveis em `workspace/deliverable/` permanecem íntegros (JSON parseia, chaves exigidas presentes, nenhuma menção desatualizada restante).

## O que a revisão encontrou e foi corrigido

**1. Ambiguidade não sinalizada no teto da multa do art. 32 (achado material).** A redação da biblioteca (`library/lei4357_art32.md`) diz "multa de 50% das quantias distribuídas (PJ) **e** 50% (beneficiários), **limitada a 50% do valor total do débito não garantido**" — não esclarece se o teto de R$ 740.000 vale **por lado ou global**. Meu texto anterior resolvia isso implicitamente "por lado" (multas de 400k + 400k). Corrigido: o item 4 e a tabela do item 8 do parecer, o `numeros.json` e o `STATUS.md` agora apresentam o **intervalo de exposição R$ 1.620.000 a R$ 1.680.000 (2,0–2,1× o caixa)**, com a ambiguidade explicitamente marcada como não resolvida. O campo `multa_art32_risco = 400.000` foi mantido e rerotulado como o lado da PJ (valor idêntico nas duas leituras).

**2. Resumo executivo e STATUS subestimavam a multa.** Diziam "risco de R$ 400.000" quando o corpo do parecer aplica a multa nos dois lados. Harmonizado: "R$ 400.000 sobre a PJ **e mais** R$ 400.000 sobre os beneficiários (R$ 200.000 por sócio), com teto controvertido".

**3. "Solidariamente" removido da descrição da multa.** A biblioteca aplica 50% a cada lado separadamente; a solidariedade que ela prevê é só a do CC art. 1.009 (restituição). A descrição do item 4(a) foi reescrita citando a redação original.

**4. Base do presumido sem ressalva.** O limite teórico de 1.300.800 usa receita bruta × 32% como base; exclusões/deduções da base do IRPJ presumido não constam nem dos documentos nem da biblioteca. Adicionada ressalva (iii) no item 2, na premissa 2 e na nota do JSON ("se existirem, o limite cai").

**5. Pró-labore descrito como "título lícito / porto seguro" sem suporte.** A biblioteca só trata pró-labore como categoria de rendimento tributável (destino de recaracterização) — não disciplina o pró-labore voluntário. Item 7.3 e item 8(i) suavizados para "alternativa relativamente mais segura, não verificada na biblioteca", mantendo a inferência defensável de que pode existir sem lucro apurado.

**6. Retórica e erros menores.** "Ordem pública anual" (afirmação minha, não da fonte) substituída pela citação literal "enquanto estiverem em débito, não garantido… não poderão"; erro de digitação "não constamos aqui hipótese" → "não vislumbramos na biblioteca hipótese"; espaços perdidos na nota do JSON.

## O que foi verificado e estava correto

- **Citações:** varredura completa — toda referência normativa nos entregáveis aponta para um dos 5 arquivos da biblioteca ou para documento do cliente; nada citado como autoridade sem lastro.
- **Aritmética:** tudo confere — base 6.4M×32% = 2.048.000; IRPJ 440.000 (307.200 + 132.800); CSLL 307.200; limite 1.300.800; variante PIS/COFINS ≈ 1.067.200; IRRF 80.000; multa 400.000×2; teto 740.000.
- **Não amarração do balanço (gap de R$ 760.000):** deliberadamente **não** forçada — segue sinalizada no item 5 e em `PERGUNTAS.md`; a conclusão (lucro distribuível = 0) não muda em nenhuma das duas leituras.
- **Controvérsia da exigibilidade suspensa** (COSIT 30/2016 vs. CARF 1402-00.xxx): exposta, não resolvida — correto, dado o escopo da biblioteca.

Status final: **COMPLETE WITH OPEN ITEMS** — os itens em aberto (amarração, residência dos sócios, valores efetivos de 2025, pontualidade dos 610 mil) são terminalmente sem resposta do cliente e estão listados em `PERGUNTAS.md` sem afetar a conclusão central: **distribuição isenta recomendada = R$ 0,00; mútuo não recomendado; "antecipação de lucros futuros" recusada.**