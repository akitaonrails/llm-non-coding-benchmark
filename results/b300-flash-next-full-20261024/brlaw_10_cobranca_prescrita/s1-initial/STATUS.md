# STATUS — **COMPLETE WITH OPEN ITEMS**

**Análise concluída em 12/10/2026 e atualizada no mesmo dia com as respostas do cliente (12/10/2026).** Conclusões centrais fechadas com as fontes da biblioteca fechada (`library/INDEX.md`); os itens abertos **não alteram** essas conclusões — afetam apenas o valor final do pedido (correção monetária) e a gestão de risco/prática de duas frentes.

## Entregáveis
| Arquivo | Conteúdo | Situação |
|---|---|---|
| `analise.json` | via processual, prescrição parcela a parcela, valores, negativação, protesto, recomendação + registro da diligência de 12/10/2026 | completo |
| `memorando.md` | raciocínio parcela a parcela, via processual, negativação/protesto, estratégia ação × acordo com números + §9 (respostas do cliente) | completo |
| `calculo_encargos.csv` | memória de cálculo por parcela (multa, juros 1% a.m. por dias/30, saldo com abatimento do PIX) | completo — linha "correção IPCA = PENDENTE" |
| `QUESTIONS.md` / `PERGUNTAS.md` | registro das 10 perguntas: 5 fechadas, 5 abertas, 1 pendência de direito | atualizado |

## Conclusões firmes (não dependem dos itens abertos)
1. **Via:** ação **monitória** (CPC art. 700), não execução — contrato sem 2 testemunhas não é título executivo e boleto não é título (`library/cpc_titulo_executivo_monitoria.md`). **Fato confirmado pelo cliente em 12/10/2026** (Q4): só os 2 representantes assinaram, sem certificação digital → via **definitivamente** monitória; execução direta só por novo instrumento de confissão com 2 testemunhas.
2. **Prescrição:** parcelas 1–4 interrompidas em 15/09/2022 (CC art. 202 VI) com novo termo **15/09/2027**; parcelas 5 e 6 **prescritas** em 10/02/2026 e 10/03/2026. PIX de 02/08/2023 não interrompe de novo (art. 202 caput).
3. **Valores:** principal exigível **R$ 110.000,00** (PIX foi o único pagamento — confirmado pelo cliente, Q2); prescrito **R$ 60.000,00**; total estimável hoje **R$ 194.390,00** (principal + multa R$ 2.400,00 + juros R$ 81.990,00), **sem IPCA**.
4. **Negativação de 12/08/2026 (R$ 180.000,00):** regular quanto a **R$ 110.000,00**, indevida quanto a **R$ 70.000,00** (R$ 60.000,00 prescritos + R$ 10.000,00 pagos) → **retificar já**. Dano moral: risco **baixo, condicionado** à Súmula 385/STJ (3 inscrições anteriores, legitimidade não confirmada), com risco real de exclusão/rebaixa do registro.
5. **Protesto:** recomendado **somente** sobre o exigível; protestar as parcelas 5 e 6 é indevido e gera responsabilidade.
6. **Urgência:** ~11 meses até 15/09/2027; a interrupção do art. 202 já foi consumida, então ajuizar não reabre prazo.
7. **Mesa de acordo (novo):** os 6 relatórios de serviço estão assinados pelo encarregado da devedora (Q7) — neutralizam a alegação "serviço não concluído" na negociação; a admissão do cliente de serviço apenas parcial ("fizemos o que deu") reforça **não** litigar as parcelas 5 e 6.

## Itens abertos (por que não é COMPLETE)
1. **Correção IPCA não calculada** — série inexistente em `workspace/`/`library/` **e o cliente não dispõe dela** (Q1). Totais seguem nominais e **subestimados**; recálculo mecânico se a série aparecer (memória pronta em `calculo_encargos.csv`).
2. **Imputação do PIX de R$ 10.000,00** (principal × encargos) — regra legal **não está na biblioteca (não verificado)**; cliente sem dado novo. Cenário adotado R$ 194.390,00; alternativo quantificado R$ 198.280,00 (+R$ 3.890,00 e indevida só R$ 60.000,00) — os dois permanecem vivos (§4.3).
3. **Legitimidade das 3 negativações anteriores da ré** (Q3) — cliente não dispõe; é condição da Súmula 385; risco de dano moral segue "baixo, condicionado".
4. **Instrução do protesto no cartório** (Q5) — lacuna da biblioteca; confirmar originais/carteiras **antes** de protocolar.
5. **Solvência da devedora** (Q9) e **ações em curso/endereço para citação** (Q10) — cliente não dispõe; sem efeito nas conclusões, relevantes para garantia do acordo e roteiro de ajuizamento.
6. **Pontos de direito fora da biblioteca** — contagem de prazo (CC art. 132), revisão de encargos, desdobramentos da monitória e do protesto: marcados **não verificados**, sem efeito prático nas conclusões.

## Fechadas nesta diligência (12/10/2026)
Q2 (único pagamento = PIX), Q4 (assinatura sem testemunhas → monitória definitiva), Q6 (sem documento posterior sobre as parcelas 5/6 → upside de R$ 102.320,00 permanece fraco e fora do pedido), Q7 (relatórios assinados existem; greve confirmada), Q8 (contrato não pactua capitalização/limite de encargos).

Nada foi "fechado para equilibrar": a linha de correção IPCA segue PENDENTE na planilha e as duas leituras de imputação permanecem vivas.
