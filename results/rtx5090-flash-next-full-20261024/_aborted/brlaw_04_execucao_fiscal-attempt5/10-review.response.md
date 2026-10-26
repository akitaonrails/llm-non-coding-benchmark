Vou reler as fontes e as peças antes de concluir qualquer coisa.

Há pastas `documents/sessao2`, `sessao3` e **`sessao5`** que preciso conferir — podem trazer insumos da própria sessão 5 que ainda não usei:

Achado importante: **`documents/sessao5/proposta_garantia.md`** — insumo da própria Sessão 5 que eu **não usei**: traz SELIC acumulada (10/07→30/11/2026 = 3,9%), cotações reais (seguro 1,2% a.a.; fiança 2,5% a.a.; penhora de faturamento 5%) e a intimação do juízo. Meu `garantia.json` tratou a SELIC como inexistente e usou ponto médio da faixa da biblioteca em vez das cotações. Vou verificar o impacto e o resto do conjunto antes de corrigir:

Validação final do JSON reescrito + varredura de consistência em todo o deliverable:

Revisão concluída e correções aplicadas. O achado central: eu havia **ignorado o insumo da própria Sessão 5** (`documents/sessao5/proposta_garantia.md` — intimação do juízo, SELIC oficial e cotações reais) e, por consequência, cometido um **erro de decomposição aritmética** no cálculo da transação. Tudo foi corrigido e revalidado por máquina.

## O que mudou

**1. `sessao5/garantia.json` — reescrito com os dados corretos**
- **Débito remanescente atualizado: 591.000 → 614.049.** O rascunho tratava a SELIC como "não verificável" (base sem atualização). A intimação traz a SELIC oficial de 10/07→30/11/2026 = **3,9%**: 591.000 × 1,039 = 614.049.
- **Cobertura de garantia: 768.300 → 798.263,70** (130% × 614.049; Portaria PGFN 164/2014 + "+30%" confirmado nas próprias cotações).
- **Custos anuais: ponto médio das faixas da biblioteca → cotações reais da intimação.** Seguro-garantia 1,2% a.a. = **9.579,16**; fiança bancária 2,5% a.a. = **19.956,59** (economia do seguro: 10.377,43/ano). As taxas reais caem dentro das faixas típicas da fonte (0,8–1,5% / 2–3%) — conferido como consistência.
- **Erro de aritmética corrigido (transação):** o rascunho decompunha os 591.000 por ÷1,75 (principal 337.714 / multa 253.286), o que **pressupunha que o total continha só principal + multa**. O PDF da CDA (extraído por `pdftotext`) itemiza exatamente: principal **307.320** + multa 75% **230.490** + SELIC até a inscrição **53.190** = 591.000 (multa confere: 75% do principal).
- **Desconto estimado de transação: 164.636 → 199.373,85** = 65% × encargos transacionáveis (230.490 + 53.190 + 23.049 = 306.729), dentro do teto legal (≤ principal 307.320 ✔).
- **Recomendação reescrita** para o cenário real da intimação: (i) extrair dos autos o **prazo da intimação** (não consta da cotação); (ii) seguro-garantia como modalidade recomendada, com nomeação de bens e penhora de faturamento de 5% avaliadas (fonte: penhora de faturamento é excepcional); (iii) embargos em 30 dias da garantia; (iv) transação só após a decisão da decadência; (v) premissa explicitada de que "remanescente" = exequendo líquido dos 509.000 decaídos — se a intimação alcançar o integral, reescalar a cobertura antes de contratar; (vi) **parcelamento marcado como não analisado** (regras não constam da biblioteca).

**2. `STATUS.md`** — bloco da Sessão 5 reescrito com os novos números + registro "Revisão" documentando as duas falhas corrigidas (insumo não usado e ÷1,75); pendência 8 reescrita (deixou de ser "planilha SELIC em falta" — problema resolvido pelo insumo — e passou a ser verificação nos autos: prazo da intimação, decisão da exceção, reconfirmar SELIC/prêmio na contratação); "próximo passo" atualizado.

**3. `QUESTIONS.md`** — item 8 reescrito: não é pergunta ao cliente, e sim item de autos (prazo, decisão, reconfirmação de taxas na data).

## O que foi verificado e não precisou mudar
- **Sessões 1–4**: tabela de períodos da peça confere campo a campo com o PDF da CDA; números nominais (1.100.000 / 509.000 / 591.000) fecham em todas as peças; `analise_redirecionamento.json` continua válido.
- **Autoridade não suportada**: varredura em todo o deliverable achou só duas ocorrências — CPC (`sessao4/defesa_redirecionamento.md:72`) e Decreto 9.580/2018 (`sessao2/manifestacao.md:86`) — ambas em notas internas que **expressamente mandam não citá-las** por não estarem na biblioteca. Corretas como estão.
- **Números antigos residuais**: nenhum em circulação; a única menção a "164.636/÷1,75" é o registro deliberado da correção no STATUS.
- **Validação final do JSON**: schema do contrato conferido chave a chave e toda a aritmética refeita a partir dos dados-fonte — todas as conferências `True`.

## Ressalvas que permanecem (rotuladas, não resolúveis aqui)
- Prazo da intimação e eventual decisão da exceção: só os autos respondem (pendência 8).
- SELIC de 3,9% projeta até 30/11/2026 e os prêmios são cotações — reconfirmar na data da contratação.
- Regras de parcelamento não estão na biblioteca: sinalizado como não verificado, não analisado.

Status geral segue **COMPLETE WITH OPEN ITEMS** — agora com os números da Sessão 5 ancorados nos documentos do caso, não em estimativas.