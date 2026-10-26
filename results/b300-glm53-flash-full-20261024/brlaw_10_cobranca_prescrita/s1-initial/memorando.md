# Memorando — Técnica Forte Ltda. × Metalúrgica Boa Vista Ltda. — cobrança de R$ 180 mil (2020/2021)

Data-base: **12/10/2026**. Só se cita a biblioteca (`library/INDEX.md`); fatos vêm de `documents/`.

## 1. Resposta direta ao cliente

- **"Quero EXECUTAR o contrato"**: não dá. O contrato particular foi assinado **sem testemunhas** → não é título executivo (CPC 784 III exige devedor + 2 testemunhas; boleto não é título) — `library/cpc_titulo_executivo_monitoria.md`.
- **"não prescreveu nada, certo?"**: errado. Parcelas 5 e 6 **prescreveram** (10/02/2026 e 10/03/2026). O e-mail de 15/09/2022 interrompeu a prescrição **apenas quanto às parcelas 1–4** (reconhecidas) e a interrupção ocorre **uma única vez** (CC 202 caput, VI e parágrafo único — `library/cc_prescricao_202_206.md`). O pagamento parcial de 02/08/2023 é novo reconhecimento, mas **não interrompe novamente** (`library/cc_prescricao_202_206.md`, nota final).
- **"já negativei no Serasa"**: foi por **R$ 180.000** — R$ 70.000 indevidos (R$ 60.000 prescritos + R$ 10.000 já pagos). Corrigir para R$ 110.000 (`library/negativacao_prescrita_sumula385.md`).
- **"protestar"** só quanto à dívida **exigível**; recomendo **não** protestar agora (detalhe na seção 6).

## 2. Roteiro parcela a parcela (datas)

Prazo: **5 anos** (CC 206 §5º I — dívida líquida de instrumento particular — `library/cc_prescricao_202_206.md`).

| Parc. | Vencimento | Ato interruptivo? | Recomeço / termo final | Hoje 12/10/2026 |
|---|---|---|---|---|
| 1 | 10/10/2020 | e-mail 15/09/2022 (reconhecimento) | **15/09/2027** | viva |
| 2 | 10/11/2020 | idem | 15/09/2027 | viva |
| 3 | 10/12/2020 | idem | 15/09/2027 | viva |
| 4 | 10/01/2021 | idem | 15/09/2027 | viva |
| 5 | 10/02/2021 | **não** — contestada no e-mail de 15/09/2022 | 10/02/2026 | **prescrita** |
| 6 | 10/03/2021 | não | 10/03/2026 | **prescrita** |

- O e-mail de 15/09/2022 (`documents/emails_reconhecimento.txt`) reconheceu "parcelas 1 a 4, total R$ 120.000" e **contestou as 5 e 6**: reconhecimento parcial interrompe apenas quanto às parcelas reconhecidas (`library/cc_prescricao_202_206.md`).
- Interrupção foi tempestiva em todas (15/09/2022 < termos originais de 10/10/2025 a 10/01/2026).
- PIX de R$ 10.000 em 02/08/2023 "por conta da parcela 1": novo reconhecimento, mas **não interrompe novamente** — o prazo corre de 15/09/2022 a 15/09/2027.
- Risco de calendário: como a interrupção já ocorreu **uma única vez**, não conte com uma nova interrupção; **cite a Boa Vista antes de 15/09/2027** (ajustar já a inicial e pedir despacho citatório rápido).

## 3. Números — principal exigível

- Parcelas 1–4: 4 × R$ 30.000 = R$ 120.000.
- (−) PIX 02/08/2023 imputado à parcela 1, conforme declaração do próprio devedor (`documents/emails_reconhecimento.txt`): −R$ 10.000.
- **Principal exigível = R$ 110.000** (P1: R$ 20.000; P2–P4: R$ 30.000 cada).
- **Excluído (prescrito): P5 + P6 = R$ 60.000.**
- Checagem: R$ 110.000 + R$ 60.000 = R$ 170.000 + R$ 10.000 pago = R$ 180.000 (fecha com o e-mail do cliente).

## 4. Encargos estimados (juros + multa; IPCA fica aberto)

Convenções (aritmética pelo Python; variante de convenção muda pouco):
- juros de mora simples 1% a.m. **pro rata die** (mês = 30 dias) desde o vencimento (contrato; CC 389/406 — `library/juros_correcao.md`);
- multa 2% sobre o **saldo** de cada parcela, pois o acervo manda calcular "abatido o pagamento parcial" (`library/juros_correcao.md`);
- correção IPCA: **não computada** — não há série do índice no acervo. Estimativa é conservadora; na inicial, atualizar pelo IPCA (parcela a parcela, só das exigíveis). Veja `QUESTIONS.md`.

| Cálculo | Dias | Capital | Juros (0,01 × dias/30 × capital) |
|---|---|---|---|
| P1: 10/10/2020 → 02/08/2023 (até o PIX) | 1.026 | 30.000 | 10.260,00 |
| P1: 02/08/2023 → 12/10/2026 | 1.167 | 20.000 | 7.780,00 |
| P2: 10/11/2020 → 12/10/2026 | 2.162 | 30.000 | 21.620,00 |
| P3: 10/12/2020 → 12/10/2026 | 2.132 | 30.000 | 21.320,00 |
| P4: 10/01/2021 → 12/10/2026 | 2.101 | 30.000 | 21.010,00 |
| **Juros totais** | | | **81.990,00** |

- Multa: 2% × 20.000 (P1) + 2% × 30.000 × 3 = 400 + 1.800 = **2.200,00** (se a multa da P1 incidir sobre o valor da mora original, R$ 600, sobra +R$ 200,00 — abandone a leitura mais favorável ao cliente somente se convencido; verso registrado aqui).
- **Total sem IPCA, na data-base: 110.000 + 81.990 + 2.200 = R$ 194.190,00.**
- Não fechamos com IPCA por falta da série — aberto, deliberadamente.

## 5. Via processual

- **Execução: descartada** — contrato sem duas testemunhas não é título (CPC 784 III; REsp 1.438.263 allí citado; Tema 1.247/STJ não se aplica, contrato é papel assinado sem testemunhas) — `library/cpc_titulo_executivo_monitoria.md`.
- **Monitória (CPC 700): recomendada** — prova escrita sem eficácia de título (contrato + relatórios assinados pelo encarregado por parcela + e-mails de reconhecimento + comprovante PIX). Rapidinha: possível execução provisória. O prazo é o da pretensão (5 anos, CC 206 §5º I); as parcelas 1–4 cabem até 15/09/2027 — monitória é meio de exercício, como nas Súmulas 299/503 (`library/cpc_titulo_executivo_monitoria.md`).
- **Cobrança (comum): fallback** se o juízo apertar os requisitos da prova escrita; mais lenta.

## 6. Negativação e protesto

- **Serasa (12/08/2026, R$ 180.000)**: parte regular R$ 110.000; **indevida R$ 70.000** (60.000 prescritos + 10.000 já pagos). Inscrição de dívida prescrita é indevida e obriga cancelamento; pretensão extinta não pode constar — CC 206 §5º I, por analogia CDC 43 §5º, Tema 1.264; **Súmula 385**: não há dano moral quando há **inscrição legítima preexistente** — `library/negativacao_prescrita_sumula385.md`.
- A Boa Vista tem **3 inscrições anteriores legítimas (2024–2025, não contestadas)** → risco de dano moral contra a Técnica Forte é baixo, mas a obrigação de **excluir/corrigir** permanece ("ressalvado o direito ao cancelamento"). Corrigir já para R$ 110.000 e guardar a prova.
- **Protesto: "não"** (Lei 9.492 — protestar exige dívida **exigível**; documento de dívida sem força executiva até pode, mas só quanto ao exigível — `library/negativacao_prescrita_sumula385.md`). Não recomendo agora: (i) seria só sobre R$ 110.000, que já é alvo da monitória; (ii) pressão pública já existe via Serasa; (iii) custo + risco de imprecisão e de indevido (se sair acima de 110 mil). Se o cliente insistir depois, protesto de **documento de dívida** limitado a R$ 110.000, jamais do contrato como título e jamais dos R$ 180.000.

## 7. Estratégia: ação × acordo (com números)

- **Ajuizar (monitória por R$ 110.000 + encargos ≈ 84.190, sem IPCA ≈ R$ 194.190 na data-base)**: força execução provisória e juros correm. Contras: prazo até citação (15/09/2027), IPCA a complementar, eventual embargos.
- **Acordo (recomendado tentar em paralelo, já que a Boa Vista sinalizou pagar o que reconhece `documents/emails_reconhecimento.txt`)**: proposta de referência = **principal R$ 110.000** + encargos negociados; novo calendário curto (ex.: 10×10.000 nov/2026–ago/2027) com juros/multa condicionados ao fiel cumprimento; salvar por escrito que o **novo cronograma vale como novo reconhecimento**, sem prejuízo do que já foi reconhecido em 15/09/2022. Com acordo honesto, evita-se litigar o IPCA e discutir multa.
- Em qualquer cenário: **não cobrar** R$ 60.000 (prescritos) nem os R$ 10.000 recebidos.

## 8. Presupostos declarados (suposições em destaque)

1. Juros são **moratórios** simples 1% a.m. desde o vencimento (contrato; `library/juros_correcao.md`); mês=30 dias pro rata.
2. PIX imputado ao **principal** da parcela 1 (declaração do devedor). Se imputado primeiro a juros da P1, o total exigível muda pouco (~±R$ 300 nos encargos); deixo assim por fidelidade ao documento.
3. Multa sobre saldo (leitura "abatido o pagamento parcial"); variante +R$ 200 anotada.
4. **IPCA não aplicado** — série indisponível no acervo; pedido em `QUESTIONS.md`.
5. Nenhum pagamento/reconhecimento posterior ao PIX de 02/08/2023 nos autos **(confirmado pela cliente)**; roteiro mantido.

## 9. Atualização pós-resposta da cliente

1. **"Pagaram R$ 10 mil em agosto de 2023 por conta da primeira parcela. Depois sumiram."** — confirma o roteiro prescricional: última intervenção do devedor em 02/08/2023; parcelas 1–4 exigíveis até **15/09/2027**; parcelas 5–6 prescritas. Nada muda nos números da seção 4.
2. **Greve (fev/2021) e relatórios das parcelas 5–6**: irrelevante para a ação — não vamos cobrar essas parcelas (prescritas). Pela mesma razão, **não cabe** discutir se a prestação foi integral.
3. **Prova reforçada** para a monitória: relatórios assinados pelo encarregado da Boa Vista **para todas as parcelas** — bom para as exigíveis 1–4; e um reconhecimento tácito de que o serviço existiu (aza para a defesa, caso a Boa Vista "esqueça" isso).
4. **Desconhecidos explícitos** (sem resposta da cliente e sem dados no acervo):
   - **IPCA out/2020–out/2026**: não computável — a estimativa de **R$ 194.190,00 (sem IPCA)** permanece como número final deste acervo; claim real será maior (diferença não quantificada, pois a série não existe aqui). Não cito índice nenhum de memória; está aberto.
   - **CNPJ e endereço da Boa Vista**: não informados; necessários só na hora de protocolar a monitória (levantar via consulta que a cliente fizer no ato; fora deste acervo).
