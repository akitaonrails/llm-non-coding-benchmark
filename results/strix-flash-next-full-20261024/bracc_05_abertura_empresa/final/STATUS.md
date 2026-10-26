# STATUS — Clínica Estética Aurora Ltda. (rodada 2)

## COMPLETE WITH OPEN ITEMS

Todos os entregáveis exigidos pelo `CONTRACT.md` estão em `workspace/deliverable/` e atualizados com as respostas do cliente:

- `parecer.md` (v2) — análise ponto a ponto com a nova estrutura recomendada (**Variante B**).
- `numeros.json` — JSON válido, schema exato do contrato, validado por script (aritmética do ITBI: 96.000/1.296.000 = 7,4% < 50% → imunidade; IRRF 0; simples_possivel `false` **para o plano como apresentado** — ver §3 do parecer).
- `contrato_social_ajustado.md` (v2) — Variante B como texto principal; cláusulas da Variante A (imóvel no capital, avaliação CC 997 V/1.055 §1º, imunidade ITBI) no ANEXO 1.
- `checklist_registro.md` (v2).
- `QUESTIONS.md` e `PERGUNTAS.md` (espelho, pois o contrato cita os dois nomes) — apenas lacunas restantes; perguntas já respondidas não se repetem.

## Conclusões centrais (com os fatos confirmados)

1. **ITBI: não devido** — imunidade confirmada com números (CTN art. 37: locação do dentista = 7,4% da receita projetada < 50%); na Variante B nem há transmissão.
2. **Simples Nacional: vedado no plano atual** — CNPJ alugando imóvel próprio (ainda que R$ 8 mil/mês) é impeditivo (LC 123/2006, art. 17, XV). **Volta a ser possível na Variante B** (locação na PF do casal).
3. **Luana**: "trabalho vale 20%" é vedado (CC 1.055 §2º). Na Variante B ela paga **R$ 4.800 (12× R$ 400)**; na Variante A precisaria de R$ 142.500 — ela declarou não ter.
4. **Marina**: pode ser **cotista**; **não pode administrar** a sociedade em horário algum (Lei 8.112/90, art. 117, X — sem exceção "fora do expediente"). Comunhão universal confirmada → CC 977: só um dos cônjuges no quadro; Felipe = **administrador não sócio** (CC 1.060/1.061).
5. **Pró-labore**: Marina R$ 0; Felipe R$ 5.000; Luana R$ 8.000; INSS retido R$ 1.430/mês (11%).
6. **Distribuições**: IRRF R$ 0 em 2026 (cada sócia < R$ 50.000/mês — Lei 15.270/2025 art. 6º-A); **a pretensão de R$ 600 mil/ano não casa com o lucro projetado (R$ 420 mil, e menos após aluguel/pró-labore na B)** — deixado aberto por determinação do contrato, com cenários 35 mil/23 mil/10 mil por mês.

## Revisão pré-entrega (v3) — correções aplicadas nesta rodada

Auditoria de fundamentação (só `library/INDEX.md`), fatos (só `documents/`) e aritmética. Correções:

1. **Fatos inventados removidos**: órgão de Marina corrigido de "IBGE" para **Ministério da Saúde** (questionário); nomes completos inventados ("Marina Alves da Costa", "Luana Barros de Moraes", "Felipe Gomes da Costa") substituídos pelos nomes dos documentos (**Marina Costa, Luana Prado, Felipe Costa**) + `[A DEFINIR: qualificação]`; endereço de rua inventado ("Rua Maria Jaiba Siqueira, 32, Região Central") substituído pela descrição da matrícula (**"Sala comercial nº 1204, Ed. Aurora Office, 180 m²"**, rua não informada).
2. **Fundamentos sem suporte corrigidos**: CC **1.057** NÃO está na biblioteca → 8ª/clause 1 do checklist reescritos como prática contratual com `[NÃO VERIFICADO]`; "IN DREI 81/2020, art. 34" (non-compete) → IN DREI só aparece no arquivo quanto a quotas preferenciais; "Res. CGSN 140/2018, Anexo VI" para 9602-5/02 → literalidade do arquivo ("permitidas — **Anexo III**"); "Decreto 731/1993 e IN DREI citados na biblioteca" → **não constam** da biblioteca; "ato separável do contrato" (administrador) → biblioteca só trata de "designados no contrato"; paráfrase do CTN art. 36 ("não desmembra") marcada `[NÃO VERIFICADO: texto não reproduzido]`; numeração "art. 37, parágrafo único" trocada pela redação literal da biblioteca.
3. **Omissão suprida**: regra de transição da Lei 15.270/2025 (lucros até 31/12/2025 aprovados até lá ficam isentos se pagos até 2028) anotada no parecer §4.3 — inaplicável ao caso, mas registrada.
4. **Erros de texto**: "discriminación" → "discriminação" (5ª); "balanho" → "balanço" (checklist 12); frase do CTN 37 embaralhada no §2.2 reescrita com a literalidade da biblioteca.
5. **Interpretações marcadas**: "vedação independe de registrar CNAE sem exercer" agora etiquetada como interpretação (§2.3).

Nada na aritmética mudou (96.000/1.296.000 = 7,4%; 13.000×11% = 1.430; cenários 35/23/10 mil seguem abertos). `numeros.json` mantém o schema; ajuste apenas de redação no campo `itbi.fundamento` ("par. único" → regra literal da empresa nova).

## Itens em aberto (não bloqueiam; premissas aplicadas)

1. **Escolha Variante A x B** — parecer recomenda B; contrato já redigido em B. Decisão dos sócios pendente.
2. **Se as projeções (R$ 1,2 mi / R$ 420 mil) já descontam aluguel/pró-labore** — cliente não tem mais informação; premissa: não descontam (daí o cenário pessimista).
3. **Preço de mercado do aluguel dos 60%** (premissa: R$ 12.000/mês por rateio; partes relacionadas — exige comprovação).
4. **Capacidade de Luana pagar 12× R$ 400** e sua formação/registro profissional (requisitos sanitários: NÃO VERIFICADO — fora da biblioteca).
5. **Diligências externas à biblioteca**: alíquota/procedimento de ITBI no Município de SP (só na Variante A), rotinas JUCESP, regime substituto (Lucro Presumido) se A escolhida, **regime legal de cessão de quotas (CC 1.057 — ausente da biblioteca; cláusula 8ª redigida como prática contratual)**, outorga conjugal em cessão de quotas, quóruns de deliberação (CC 1.073-1.080), tabela IRPF do aluguel na PF — todos marcados **[NÃO VERIFICADO]** nos textos.
6. **Dados cadastrais** (qualificação completa, endereço, denominação "Aurora" livre) para o registro.
