# Solução do passivo fiscal (União — R$ 2.700.000) — Sessão 3

**Objeto:** propor a solução para o passivo fiscal extraconcursal, com base exclusiva na biblioteca (`library/INDEX.md`). Itens 11–14 de `QUESTIONS.md` sem resposta (cliente declarou não haver mais dados): a matriz abaixo qualifica as rotas e **propõe** a via primária; a decisão executiva segue registrada como pendente de diretoria no `STATUS.md` (nada é re-perguntado).

## 1. Enquadramento legal (por que a União ficou fora do plano)

- O crédito tributário **não se sujeita a concurso de credores** (CTN art. 187 — `ctn_187_191a.md`) e **não se submete ao plano** da RJ (art. 68 — `lei11101_excertos.md`). A cláusula original da minuta (deságio 50%, 180×) é nula — veredicto #4 da Sessão 2; **deleção recomendada** e pendente de ajuste da minuta.
- **Risco sem solução:** as execuções fiscais **não se suspendem** pelo deferimento da RJ (art. 6º, §7º-B — ressalvados atos constritivos sobre bens de capital essenciais, no juízo da RJ). Patrimônio exposto fora da vara.
- **Trava de concessão:** a RJ exige certidão negativa de débitos tributários ou **positiva com efeito de negativa** (art. 57 + CTN 191-A — `lei11101_excertos.md`, `ctn_187_191a.md`); a adesão a parcelamento/transação **gera** essa certidão (`lei10522_parcelamento_rj.md`). Sem via fiscal, a concessão fica bloqueada.
- Coerência: a União já consta **excluída de ofício** do quadro concursal do demonstrativo do mês 1 (`sessao1/demonstrativo_mensal_aj.md` §3.2).

## 2. As três rotas da biblioteca (Lei 10.522, arts. 10-A a 10-C)

Débito tratado: **R$ 2.700.000**. Cálculo em Python com asserções (verificado neste engajamento).

| Rota | Regime | Caixa necessário | Outra "moeda" | Custo econômico nominal |
|---|---|---|---|---|
| **A — Parcelamento 120×** (art. 10-A) | até **120 parcelas**; parcela média **22.500** | **2.700.000** (100%) em 120× | — | 2.700.000 |
| **B — 30% + 84×** (art. 10-A §1º-B) | **liquidar até 30% com prejuízo fiscal/base negativa** e restante em 84 parcelas | **1.890.000** (84 × 22.500) | prejuízo fiscal **810.000** (30% — **sem caixa**) | 2.700.000 |
| **C — Transação PGFN** (art. 10-C) | desconto **até 70%**, até **120 meses** | **a partir de 810.000** | — (desconto real depende dos termos da PGFN) | 2.700.000 × 30% = **810.000** no teto do desconto |

Encargo de parcelamento/juros/correção (Selic etc.): **não informados e não previstos nos excertos** — todos os totais acima são **nominais, sem encargos (assunção rotulada; QUESTIONS.md item 7 sem resposta)**.

## 3. Matriz de caixa contra a fonte declarada (UPI — galpão R$ 4.500.000)

Fonte do plano: 4.500.000; plano pagável: 3.548.000 (960.000 + 2.588.000 — Sessão 1/2).

| Cenário | Saídas nominais | Folga sobre a fonte | Leitura |
|---|---|---|---|
| Só o plano | 3.548.000 | **952.000** | folga nominal base |
| Plano + **Rota C** (teto do desconto) | 4.358.000 | **142.000** | única rota que fecha o caixa com a fonte declarada |
| Plano + **Rota B** (se prejuízo operativo) | 5.438.000 | **−938.000** | folga negativa — dependeria de caixa de operação (não informado) |
| Plano + **Rota A** | 6.248.000 | **−1.748.000** | folga negativa maior |

**Cronogramas não reconciliados com os dados disponíveis:** a carência de 24 meses do plano colide com o início das parcelas da União — o momento de início das parcelas desses regimes **não consta da biblioteca** (NAO_VERIFICADO); nada de calendário foi assumido além do nominal. Sem prejuízo fiscal confirmado (item 3 sem resposta), a Rota B **não é qualificável hoje**.

## 4. Proposta (recomendação do Controller)

1. **Via primária — Rota C (transação PGFN):** é a única rota cujo caixa de teto (810.000) mantém **folga positiva** (142.000) com a fonte declarada, preserva resolução de curto prazo e destrava o art. 57/CTN 191-A (certidão positiva com efeito de negativa) já na adesão. **Resalvas:**
   - o desconto efetivo ≤ 70% depende da proposta aceita pela PGFN — a biblioteca dá o **teto**, não o resultado (razoável planejar com margem acima de 810.000);
   - o **tratamento tributário/contábil do desconto** obtido (IRPJ/CSLL sobre ganho?) **não consta da biblioteca** — NAO_VERIFICADO: nenhum ganho é reconhecido antecipadamente nos lançamentos (`lancamentos_novacao.json`);
   - cronograma pós-adesão a extrair do termo/edital da transação (NAO_VERIFICADO).
2. **Alternativa condicional — Rota B:** reabrir se o item 3 confirmar **saldo de prejuízo fiscal/base negativa de ao menos 810.000** (IRPJ/CSLL, conforme regra do regime): reduz o caixa para 1.890.000, mas permanece folga negativa (−938.000) — exigiria fonte adicional de caixa ou re-negociação de prazo da fonte. Sem o dado, fica **condicionada**, não descartada.
3. **Último recurso — Rota A:** 120× fecha o débito sem desconto, mas com folga de **−1.748.000** nominais pela fonte atual; adotável apenas com nova fonte de caixa declarada.
4. **Ordem operacional:** (i) protocolar proposta de transação (Rota C); (ii) protocolada a adesão/termo, obter a **certidão positiva com efeito de negativa** (`lei10522_parcelamento_rj.md`) e anexá-la aos autos da RJ (art. 57 + CTN 191-A); (iii) atualizar o parcelamento mensal ao AJ no demonstrativo (art. 52, IV); (iv) o plano deve **apenas referenciar** o regime legal — nunca regulá-lo (Sessão 2, §6.4).

## 5. O que permanece aberto (nunca re-perguntado)

- Decisão executiva da rota (item 11) — proposta acima; pendência registrada no `STATUS.md`.
- Escolha da alienação **judicial** do galpão (item 12) — recomendação constante: é o que afasta a trava de 30% do ganho de capital (art. 6º-B); a UPI segue com montantes condicionais no `lancamentos_novacao.json`.
- Encargos (Selic/juros), saldo de prejuízos, e datas efetivas — lacunas mantidas como assunção rotulada em cada entregável.

*Fontes citadas:* `lei10522_parcelamento_rj.md` (arts. 10-A, 10-A §1º-B, 10-C; certidão), `lei11101_excertos.md` (arts. 57, 68, 6º §7º-B), `ctn_187_191a.md` (art. 187; 191-A), `cpc_contabil_rj.md` (rubricas) — todas em `library/INDEX.md`.
