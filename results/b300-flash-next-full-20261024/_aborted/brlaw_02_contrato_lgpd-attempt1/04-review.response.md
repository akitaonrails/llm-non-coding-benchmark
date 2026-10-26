

Boa verificação de pré-entrega. Vou cruzar **cada citação** dos entregáveis com o texto literal da biblioteca e refazer toda a aritmética:







Encontrei um artefato em inglês ("inconvenient" no JSON). Vou esgotar a lista de citações e re-extrair a minuta para conferir os fatos das cláusulas 1–6:





A minuta confirma os fatos (crédito de 2%/p.p., teto 10%; R$ 6.900/unidade; IGP-M "a critério"). Agora a revisão integral do JSON e do Anexo contra a biblioteca:





Ficha confirma: **3 unidades, ~22.000 pacientes, R$ 9,2 mi/ano** — todo bate com os números das peças. Falta o espaço extra em "Amazon/ AWS" e a varredura final do anexo/nota:






Anexo A revisado por completo — seções A.1–A.11, itens 1–22 + 13-A, remissões internas batem (13-A→item 11; 19(iv)→19(i); A.11→item 21) e todas as citações constam da biblioteca. Agora a varredura final: nota da sócia, revalidação do JSON e checagens mecânicas:






A nota está sólida, mas a leitura final encontrou três defeitos de redação — incluindo um erro de ortografia real: **"excessões"** (linha 52; o certo é "exceções") e **"um litigar"** (linha 10). Vou checar se "excessões" aparece em mais arquivos e corrigir:





Só na nota. Corrigindo as três:







Correções aplicadas. Última verificação de consistência e leitura do STATUS:






A linha 97 que o grep apontou é só o "inconven**iente**" já corrigido (o padrão casou como substring) — está limpo. Revisão concluída.

## O que mudei (5 correções)

| Arquivo | Antes | Depois | Natureza |
|---|---|---|---|
| `clausulas.json` (fundamento cl. 14) | "É **inconvenient** e negociável" | "É **inconveniente** e negociável" | palavra cortada/estrangeira |
| `clausula_dados.md` (item 13-A) | "A Amazon/ AWS" | "A Amazon/AWS" | espaço indevido |
| `nota_socia.md` (§5) | "com **excessões** para dados/sigilo/PI" | "com **exceções** para" | palavra inexistente |
| `nota_socia.md` (§1) | "o risco consciente de **um litigar** em SC" | "de **litigar** em SC" | gramática |
| `nota_socia.md` (§2) | "dever de vocês, **controladoras**" | "de vocês, **como controladora**" | concordância — a Aurora é controladora única, como o resto das peças |

Nada de substância (avaliações, riscos, fundamentos ou números) mudou — eram defeitos de texto, não de análise.

## O que foi conferido e **não** precisou mudar

**Autoridade — cada citação cruzada com o texto literal da biblioteca:** LGPD arts. 5º (II/VI/VII/VIII), 11 II "f" e §4º, 12, 33, 37, 39, 42 e §1º I, 46–48; Res. CD/ANPD 15/2024 (3 dias úteis); CC arts. 422, 413, 421-A, 473 p.ú.; CPC art. 63 §§1º/3º; REsp 1.707.855/SP, 1.203.109/MG, 680.815/PR; CDC arts. 2º/3º/51 e teoria finalista; CFM 1.821/2007, 2.299/2021 e Lei 13.787/2018 (20 anos; incompatibilidade dos 30 dias) — **todas conferem**. Os arts. 7º/11 aparecem no Anexo apenas como referência genérica a bases legais, coberta pelo escopo de citação da biblioteca. O que não está na biblioteca segue rotulado "não verificado" (adequação dos EUA; CC art. 122 — fundei no 422; dispensa de DPO; prazos/percentuais de redação = propostas).

**Fatos da minuta (re-extraí o PDF):** IGP-M "ou outro índice a critério da NEXA"; servidores "Brasil ou exterior" + P&D; crédito SLA de 2%/p.p. com teto 10%; 36 meses com renovação automática e denúncia de 180 dias; CSV por 30 dias; teto "3 mensalidades, exceto dolo" (ambiguidade mantida como flagged); multa de 100% das vincendas; não concorrência 5 anos/Brasil/R$ 500 mil.

**Aritmética (contra a ficha: 9,2 mi, 22.000 pacientes, 3 unidades):** 3×6.900=20.700/mês; 248.400/ano=2,7%; ano 1 = 296.400; 36m = 793.200; multas 496.800/745.200 (8,1%); teto 0,23–0,68% e R$ 0,94–2,82/paciente; 500 mil = 5,4%; SLA 87,6 h ≈ 3,6 dias; crédito máx. 2.070 — **tudo fecha**.

**Mecânica:** JSON válido, 17 entradas (6/9/2 = contagens do STATUS); `QUESTIONS.md` ≡ `PERGUNTAS.md`; remissões internas do Anexo batem (13-A→11; 19(iv)→19(i); cl. 9→A.11); varredura de inglês limpa (só o cabeçalho do STATUS, que é do protocolo).

As peças estão prontas para entrega em `workspace/deliverable/`, com o STATUS honesto: **COMPLETE WITH OPEN ITEMS** — os em aberto são os pedidos de confirmação escrita à NEXA (região AWS, subcontrato, art. 33), não lacunas do parecer.