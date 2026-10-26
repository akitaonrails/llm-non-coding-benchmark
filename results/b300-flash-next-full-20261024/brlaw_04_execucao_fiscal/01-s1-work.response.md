

Now let me read the CDA PDF and the contract (contrato social):





All source documents and the closed library are read. Let me verify the arithmetic with Python before drafting:





Now the main brief:





Sessão 1 concluída. Resumo do trabalho:

## Análise da decadência (auto de infração lavrado em 03/02/2026)

| Período | Situação no PAF | Regra | Limite p/ lançar | Resultado | Valor |
|---|---|---|---|---|---|
| 3T/2020 | sem pagamento, DCTF zerada | CTN 173 I (termo 01/01/2021) | 31/12/2025 | **DECAÍDO** (AI 34 dias após) | R$ 268.000 |
| 4T/2020 | pagamento parcial R$ 61 mil (Tema 163 → CTN 150 §4º, FG 31/12/2020) | CTN 150 §4º | 31/12/2025 | **DECAÍDO** | R$ 241.000 |
| 1T/2021 | pagamento parcial R$ 84 mil | CTN 150 §4º (FG 31/03/2021) | 31/03/2026 | tempestivo (56 dias de folga) | R$ 302.000 |
| 2T/2021 | sem pagamento | CTN 173 I (termo 01/01/2022) | 31/12/2026 | tempestivo | R$ 289.000 |

- **Decaído: R$ 509.000 · Remanescente: R$ 591.000** (soma confere com os R$ 1.100.000 da CDA). Verifiquei os 2020 sob **as duas regras** — decaídos em qualquer leitura, e mesmo prorrogando o termo a 01/01/2026.
- Ponto forte contra a exceção "fraude" do 150 §4º: a multa é 75% exato sobre 572.000 (art. 44 **I**, não o §1º de 150%) — a própria Fazenda não tipificou fraude.

## Nulidades/vícios identificados
1. **Multa sem fundamento legal** na CDA (campo em branco; TVF genérico) — LEF 2º §5º III; emenda possível (2º §8º, Súmula 392), mas sem reabrir períodos decaídos;
2. Citação negativa vs. **mudança de endereço comunicada antes da diligência** (JUCESP 12/03, RFB 20/03/2026) — pedido de citação no endereço novo + afastamento antecipado da Súmula 435;
3. CDA sem corresponsáveis — item de atenção para o redirecionamento futuro (Súmulas 392/430/435, Temas 962/981).

## Veículo escolhido: **exceção de pré-executividade**
Decadência é matéria de ofício e puramente documental (Súmula 393), não exige garantia do juízo nem o custo de 130% do seguro/fiança, e reduz já a execução em R$ 509 mil. Embargos (30 dias da garantia) ficam preservados para o mérito probatório de 1T/2021 e 2T/2021.

## Arquivos
- `deliverable/sessao1/analise.json` — mapa de decadência, vícios, veículo (JSON validado; somas conferem)
- `deliverable/sessao1/peca.md` — exceção de pré-executividade completa, com aritmética demonstrada e citações restritas à `library/INDEX.md`
- `deliverable/QUESTIONS.md` — 6 perguntas para as próximas sessões (TVF integral/fraude, memória de cálculo e dedução dos DARFs, prova dos depósitos, situação da empresa em Cotia, sócios, garantia/CAPAG) + premissas adotadas
- `deliverable/STATUS.md` — **COMPLETE WITH OPEN ITEMS** (Sessão 1), com os itens em aberto

Risco sinalizado: há chance de a Fazenda ter cobrado o principal **sem deduzir** os DARFs parciais (R$ 61 mil + R$ 84 mil) — se confirmado, o remanescente de R$ 591 mil está sobrefaturado; isso vira impugnação de valor nos embargos.