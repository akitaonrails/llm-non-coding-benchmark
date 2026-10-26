# STATUS

## Engajamento: Fornecedor Sul S.A. (EPP) × Atlas Distribuidora S.A. (RJ)

**Situação: `COMPLETE WITH OPEN ITEMS`**

Todos os entregáveis obrigatórios foram produzidos:

| Entregável | Arquivo | Estado |
|---|---|---|
| 1. Estratégia (JSON no schema do contrato) | `deliverable/estrategia.json` | ✅ completo (JSON válido; chaves exatas do schema) |
| 2. Peça ao AJ (art. 9º) | `deliverable/habilitacao_divergencia.md` | ✅ completa (placeholders de qualificação assinalados) |
| 3. Resposta simples às 3 perguntas do e-mail | `deliverable/resposta_cliente.md` | ✅ completa |
| 4a. Perguntas (opcional) | `deliverable/QUESTIONS.md` | ✅ 8 perguntas (item 7 parcialmente respondido pela cliente — 20/04/2026) |
| 4b. STATUS | `deliverable/STATUS.md` | este arquivo |

## Conclusões centrais

1. **Habilitar/ divergir SIM, até 27/04/2026** (15 dias corridos do edital de 10/04; 15º dia = 25/04, sábado → prorrogação para 27/04). Retardatário = sem voto (art. 10, §1º), e o valor/classe errados da relação prevaleceriam.
2. **Crédito fiduciário R$ 900.000:** fora do plano (art. 49 §3º), *mas* sem retirada dos bens essenciais durante o stay (arts. 49 §3º e 6º §§4º/7º-A; Tema 1.051). Retomada da execução apenas ao fim do stay. **Atualização 20/04/2026: a essencialidade dos bens foi confirmada pela cliente** (comunicação de 20/04/2026: os bens são "o coração do galpão" da Atlas; "sem isso a Atlas para") — afirmação da credora, que não constava dos documentos e foi integrada nos entregáveis.
3. **Crédito quirografário R$ 1.200.000:** classe IV (EPP, art. 41, IV), não III; voto por cabeça (art. 45).
4. **Divergência de valor:** listado R$ 1.600.000 × correto R$ 2.100.000 (900k + 1.200k).
5. **Fiança do sócio:** NÃO extinta pela homologação (Súmula 581/STJ; art. 49 §1º; art. 59/Tema 885 — cláusula do plano não vincula o Banco Horizonte, que não anuiu). Não dar anuência.
6. **Objeção ao plano (art. 55):** apresentar em juízo até 11/05/2026 (premissa: relação publicada em 10/04/2026) contra cláusulas que (i) submetem fiduciários ao plano e (ii) " extinguem" garantias pessoais.

## Aritmética (mostrada)

- **Prazo da divergência:** edital 10/04/2026 (sexta) → 1º dia corrido = 11/04 → 15º dia corrido = 25/04 (sábado: 25 − 11 = 14 dias depois do 1º) → termo final **27/04/2026** (prorrogação para o 1º dia útil seguinte, regra da biblioteca: CPC 224 §1º via art. 189 caput, `library/lrf_habilitacao_prazos.md`). Verificação computacional (Python): 2026-04-10 = sexta; day15 = 2026-04-25 (sábado); next business day = 2026-04-27 (segunda).
- **Prazo da objeção:** 10/04/2026 + 30 dias corridos → day30 = **10/05/2026 (domingo)** → prorrogado: **11/05/2026 (segunda)**. (Mesma verificação computacional.)
- **Crédito:** 900.000 + 1.200.000 = **2.100.000**; divergência 2.100.000 − 1.600.000 = **500.000** (não "forcei" nenhuma recomposição dos 1.6 milhões da Atlas; a origem desses 1,6 mi não constou dos documentos e ficou aberta — QUESTIONS.md, item 3).
- **Valores nominais:** sem atualização (art. 9º, II) por falta de data do pedido e encargos — assunção em destaque na peça e na resposta; não há margem para "fazer bater" nada.

## OPEN ITEMS (o que falta/melhoria)

1. **Dados de qualificação e documentos** (CNPJ, endereço, procuração, contratos, registro fiduciário, duplicatas, demonstrativo de parcelas) — pedidos em `deliverable/QUESTIONS.md` itens 1 e 4; a peça deixa placeholders.
2. **Data do pedido de RJ e encargos** → atualização do crédito até a data do pedido (art. 9º, II); peça reserva retificação (QUESTIONS.md, item 2).
3. **Data de publicação autônoma da relação do AJ (art. 7º §2º)**, se existir — fixa com precisão o prazo da objeção; atualmente assumido 10/04/2026, destacado como premissa (QUESTIONS.md, item 5).
4. **Data de deferimento do processamento** → cálculo do fim do stay (180 dias, prorrogável 1×) e janela de retomada da execução fiduciária (QUESTIONS.md, item 6).
5. **Composição dos R$ 1.600.000** listados — conferência junto ao AJ após resposta/explicações (QUESTIONS.md, item 3).
6. **Assunções em destaque nos entregáveis:** (i) valores nominais; (ii) data da relação = 10/04/2026; (iii) bens permanecem em poder da Atlas — **confirmado pela cliente** em 20/04/2026 (em uso, "o coração do galpão" da Atlas), embora sem nº de série/laudo (item 7 abaixo). Nenhuma delas inventa fato: todas estão marcadas onde aparecem.
7. **Estado e identificação dos bens** (sinais de retirada/dano, nº de série, laudo): **sem informação e permanece desconhecido** — na resposta de 20/04/2026 a cliente disse não ter informações adicionais além da essencialidade; monitoramento fica a cargo da credora (QUESTIONS.md, item 7 — parte restante; peça, art. 9º, III e V).

*Nota de fonte: toda citação legal dos entregáveis aponta para os arquivos listados em `library/INDEX.md`; nada fora da biblioteca foi consultado ou citado.*
