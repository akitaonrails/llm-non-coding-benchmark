Vou primeiro verificar novamente toda a aritmética da segunda rodada com Python antes de editar os arquivos.

Um erro de indentação na linha 36 — corrigindo e executando novamente:

Os números foram todos verificados — incluindo duas galhardetes que my plano anterior deixou passar (transmissão total = 741.200 = 4% × 18,53M sob qualquer estrutura; inventário sobre 10.315.000 = 412.600). Agora deixe-me ver os outros dois arquivos de entrega antes de editar:

All verified. Now applying the second-round updates to `parecer.md` — starting with item 2 (PF and PJ blocks):

Now the section 3 numbers block (ITCMD), to reflect the revised donation design and the total-transmission identity:

Now section 4 — appending the concrete "mínimo possível" plan responding to the client's stated wish:

Now the síntese table:

Now the "Estrutura recomendada" items 3 and 4:

Now the premissas section:

Now the roteiro de cálculo section:

Dois pequenos apontamentos para as premissas já que o cliente disse que não haverá mais informações:

Adicionando ao cabeçalho os fatos de segunda rodada para que o parecer documente a resposta do cliente em si:

Now let me re-check the contract's JSON schema before rewriting `numeros.json`:

O schema confirma as chaves existentes. Reescrevendo `numeros.json` com os números da segunda rodada:

JSON done. Now `QUESTIONS.md` — annotating what was answered without re-asking:

Duas deslizes de digitação no QUESTIONS.md que preciso corrigir:

Agora o `STATUS.md` final:

Retomando do checkpoint. Agora a verificação final: procurar números obsoletos, validar o JSON e ler o parecer completo.

Verificações residuais: nenhuma, e o JSON é analisável com todos os inteiros. Agora, uma leitura completa de coerência do parecer:

A leitura completa confirma que todos os números da segunda rodada foram incorporados (PF 257.756,40 / PJ 145.358,08 / economia 112.398,32 / pagamentos 4,39 e 9,41 anos / ITCMD 328.600 + 412.600 = 741.200 / piso de Marcos 3.088.333). Encontrei uma dúzia de escorregões de linguagem a corrigir:

Todas as edições foram aplicadas. Verificação final em todo o pacote de entregas:

Todas as verificações passaram — os "OUT OF RANGE" são apenas repetições legítimas de figuras-chave entre seções (todos os valores aparecem no mínimo nas quantidades esperadas; nenhum obsoleto). Antes do relatório final, vou confirmar as linhas da síntese para resumi-las com precisão:

Tudo verificado e fechado. O pacote está completo e coerente.

---

# Relatório final — parecer patrimonial/sucessório (Dona Helena Furtado)

## O que mudou na 2ª rodada (respostas da cliente incorporadas — nada re-perguntado)

**1. Item 2 (PF × PJ) recalculado com a comissão de 8%:**
- Comissão dedutível nos dois lados: 84.900 × 8% = 6.792/mês → base PF 78.108.
- **PF carnê-leão:** 78.108 × 27,5% = 21.479,70/mês → **257.756,40/ano (25,3% da receita)**
- **PJ Presumido:** IRPJ+CSLL+PIS+COFINS 124.031,64 (base presumida imune à comissão) + IRRF sobre distribuição 21.326,44 (10% × 67.772,03 que excede 50k) = **145.358,08 (14,27%)**
- **Economia: R$ 112.398,32/ano** → payback do ITBI (492.900) ≈ **4,39 anos**
- Leitura alternativa do IRRF 2026 quantificada: economia cai para 52.398,32, payback 9,41 anos — o ganho persiste nas duas leituras.

**2. Item 4 (sucessão) responded:** doação de nua-propriedade de 50% das quotas (4.107.500 cada a Ricardo/Paula; 8.215.000 ≤ teto 9.265.000, folga 1.050.000), usufruto vitalício reservado. **Piso de Marcos: R$ 3.088.333,33 — invariante pela colação**, independentemente do que for doado dentro do teto. Único caminho abaixo disso: deserdação (justa causa — não confirmada na biblioteca; encaminhado a advogado formal).

## Veredito das 5 afirmações da palestra (síntese do parecer)

| # | Afirmação | Veredicto | Número-chave |
|---|---|---|---|
| 1 | Integralizar sem ITBI | **Falsa** no plano descrito | ITBI ≈ 492.900 (3% × 16,43 mi; Tema 796: 141.600 + 351.300) |
| 2 | PJ paga só 11,33% vs 27,5% | **Depende** — números errados | PJ 14,27% vs PF 25,3%; economia 112.398,32/ano |
| 3 | ITCMD 4% sobre valor contábil | **Falsa** na base (story 188.800 refutada); alíquota certa | Doação 328.600; **total invariante 741.200 = 4% × 18.530.000** |
| 4 | Excluir quem quiser | **Falsa** | 50% indisponível; piso de Marcos 3.088.333 |
| 5 | Cláusulas protegem de todos | **Depende** | CC 1.848: na legítima, só com justa causa |

Identidade-chave do item 3: doação (328.600) + inventário sobre 10.315.000 (412.600) = **741.200 = o mesmo ITCMD de um único inventário** — a estrutura ganha em controle/timing, não em ITCMD.

## Incógnitas → premissas (não re-perguntadas)

Valor venal, faixas IRPF/GCAP, base do IRRF, montantes de IPTU/condomínio, regimes de bens, passivos e causas de deserdação viraram **Premissas A–E** no parecer e 8 itens abertos no STATUS. Nenhum número foi deduzido dessas lacunas sem aritmética explícita e rótulo de premissa.

## Entregáveis (todos validados)

- **`/work/workspace/deliverable/parecer.md`** — 5 vereditos, aritmética completa, estrutura recomendada, limites/premissas; zero texto obsoleto (suite final: sem ocorrências de figuras da 1ª rodada, sem anglicismos/erros restantes).
- **`/work/workspace/deliverable/numeros.json`** — parseia OK, só inteiros, chaves exatas do CONTRACT (257756 / 124032 / 21326 / 145358 / 492900 / 4720000 / 1756500 / 328600).
- **`/work/workspace/deliverable/QUESTIONS.md`** — itens 2 e 8 marcados respondidos; os demais anotados como premissa adotada, sem nova cobrança.
- **`/work/workspace/deliverable/STATUS.md`** — COMPLETE WITH OPEN ITEMS, com os 8 itens abertos numerados e nota de consistência (payback 4,39 anos; ITCMD invariante 741.200; piso de Marcos 3.088.333).

Não há pendências de cálculo nem de texto. Os únicos abertos são os itens documentados que dependem de terceiros (registros, tabeliões, advogado formal) ou de dados que a cliente disse não ter.