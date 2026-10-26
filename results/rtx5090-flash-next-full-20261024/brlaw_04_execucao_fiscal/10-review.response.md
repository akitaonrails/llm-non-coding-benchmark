Vou revisar tudo: (1) datas dos autos que sustentam a base SELIC; (2) cadeia de citações vs. biblioteca fechada; (3) toda a aritmética, incluindo os cenários de DARF.

A inscrição em 10/07/2026 está ancorada na extração S1 (`analise.json:48`, `peca.md:34`) — a base SELIC está correta. As citações no LEF art. 16 (30 dias contados da garantia), Súmula 393 e Tema 163 estão todas presentes na biblioteca. Agora, a verificação crítica da aritmética dos DARF que sinalizei:

Erros confirmados: `0.75 × 84,000 = 63,000`, e não 54,780. O valor 54,780 é a *penalidade corrigida* para 1º trimestre/2021, ou seja, o excesso real de penalidade é de 63,000, e o cenário intermediário de "507,000" (credita apenas o principal e mantém inalterada a penalidade) não corresponde a nenhuma leitura coerente da própria CDA (penalidade = 0.75 × principal). Com o DARF não creditado, o excesso é de até **147,000** → o limite inferior de execução é de 444,000. Se o lançamento já o tiver creditado, o excesso é **zero**. Aplicando as correções agora:

Agora aplicando as correções — primeiro `garantia.json`:

Currently editing three segments of `recomendacao` (DARF conflict range, coverage reduction scenarios, and root comparison range):

Revalidating `garantia.json` (parses + exact schema keys + arithmetic):

`garantia.json` está limpo. Agora as edições de `garantia_memoria.md` — obtendo o texto exato de §4–§9:

Aplicando as seis edições de correção na memória:

Memória concluída. Agora `STATUS.md` — verificando o texto exato em torno das linhas 12 e 18:

Final sweep — varredura em todo o entregável da S5 para verificar se há valores obsoletos restantes e reler o §7 corrigido:

Todas as correções foram aplicadas e verificadas. As únicas ocorrências restantes dos números antigos são as menções autorreferentes intencionais ("a versão preliminar dizia X — corrigido para Y"), que documentam a correção. Revisão concluída.

## O que a revisão encontrou e o que mudou

### Erros corrigidos

**1. Erro aritmético na memória de cálculo (§7)** — o maior problema.
Eu escrevera "multa sobre o valor pago ≈ 54.780 = 0,75 × 84.000". Ora, **0,75 × 84.000 = 63.000**. O número 54.780 é, na verdade, a *multa corrigida* do 1T/2021 (0,75 × 73.040, o principal líquido se o DARF for creditado). Corrigido em `garantia_memoria.md` e `STATUS.md`.

**2. Cenário "507.000 → 526.773" retratado (inconsistência interna).**
A versão preliminar deduzia o DARF de 84.000 do principal mas mantinha a multa em 117.780. Isso contraria a régua da própria CDA — multa = exatamente 0,75 × principal, verificado nos dois períodos que trazem ambos os campos. Se o lançamento ignorou o DARF, **principal e multa** estão ambos excessivos; se já o deduziu, o excesso é zero. Não existe meio-termo coerente. O tratamento correto agora é uma faixa, dependendo da **U1** (prova ainda pendente):
- **Leitura (a)** — DARF não creditado: excesso de até **147.000** (84.000 principal + 63.000 multa proporcional) → piso vivo **444.000** → atualizado **461.316** → cobertura mínima possível **599.710,80** (seguro ~7.196,53/ano);
- **Leitura (b)** — DARF já deduzido: excesso **zero**, base fica 614.049.

**3. Comparação de rotas refeita** (JSON + memória §6).
"Defesa vencedora paga ~526.773" → **entre 461.316 e 614.049** conforme a leitura da U1. "A diferença (~100 mil)" → economia real da transação **~12 mil a ~165 mil** (estimado) ou **~47 mil a ~199 mil** (desconto máximo) — sempre condicionada às premissas não confirmadas do edital (classificação/CAPAG, percentual real). Também removi o "|ganho ≈ >10x o prêmio" que só valia no cenário antigo.

**4. Typo**: "períodos nulos forem formalmente excluído" → "excluídos" (`garantia.json`).

### Verificado como correto — não alterado

- **Datas**: inscrição 10/07/2026 está fundamentada na extração da Sessão 1 (`sessao1/analise.json:48`); a janela SELIC 10/07→30/11/2026 é a cotação dos próprios autos. ✓
- **Citações**: todas dentro da biblioteca fechada — LEF art. 16 (embargos em 30 dias da garantia), Súmulas 392/393, Tema 163 (REsp 973.733), +30% da Portaria PGFN 164/2014 art. 3º, regras de transação da Lei 13.988/2020. ✓
- **Núcleo da garantia**: 614.049,00 / cobertura 798.263,70 / seguro 9.579,16 / fiança 19.956,59 — aritmética revalidada. ✓
- **Decomposição da CDA**: somas fecham (multas 429.000 + principais 572.000 + encargos embutidos 99.000 = 1.100.000). ✓
- **Recomendação**: inalterada — seguro-garantia + embargos em 30 dias; transação só como plano B. A almofada dos +30% (184.214,70) cobre até o cenário novo de 147.000 sem risco de insuficiência. ✓

### Escolhas documentadas

- A **carta da Sessão 4 ("~446.000") não foi reescrita** — já foi entregue ao cliente. Curiosamente ficou perto do piso correto (444.000), mas pela decomposição errada (contava os dois DARFs e ignorava a multa). A correção vive na memória §7; se quiser, redijo um adendo curto de uma página para os sócios.
- `STATUS.md` ganhou um item de registro de revisão; a U1 ficou **mais valiosa** — os DARFs comprovantes que pedimos na carta S4 agora valem até 147.000, não 84.000.

O entregável avaliado (`sessao5/garantia.json`) revalida no schema exato do contrato e está limpo de números antigos.