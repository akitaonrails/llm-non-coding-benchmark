# Status do engajamento

**Status geral (Sessões 1–3): COMPLETE WITH OPEN ITEMS**
Todos os 8 entregáveis do contrato estão escritos e validados (schemas JSON conferidos por script; débitos = créditos nos lançamentos; somas fecham). Os "open items" são **desconhecidos que o cliente declarou não possuir** — não inventados nem forçados; cada um está sinalizado no entregável correspondente.

## Entregáveis por sessão

### Sessão 1
1. `sessao1/resposta_diretor.md` — recusa fundamentada do pagamento "por fora" ao Norte (arts. 172/64, conforme excertos da biblioteca); correção da "trava de 30%" (art. 50-A, II: não aplicável ao ganho de deságio; I: fora da base PIS/COFINS); via própria para a União (CTN 187; art. 68; Lei 10.522 arts. 10-A a 10-C).
2. `sessao1/classificacao_creditos.json` — 7 créditos, schema validado: total 13.540.000; concursais 7.430.000 (trabalhistas 960.000; Alfa 4.200.000; Norte 1.850.000; Sul EPP 420.000); extraconcursais: Beta fiduciário 3.100.000 (art. 49 §3º) + Norte pós-pedido 310.000 (art. 67); União 2.700.000 fora do plano.
3. `sessao1/demonstrativo_mensal_aj.md` — caixa reconcilia: 820.000 + 5.770.000 − 5.750.000 = 840.000 (semanas 1–4 de 13).
4. `sessao1/addendum_sinal_norte.md` — resposta ao fato novo: fornecimento à vista novo = pagar (art. 67); **"sinal" sobre saldo pré-pedido = vedado** (concursal fora do plano; novação só na homologação); critical vendor só via plano/assembleia ou autorização judicial (art. 66 — não verificado).
5. `sessao1/addendum_2_adiantamento_simulado.md` — recusa à proposta de pagar o atrasado disfarçado de "adiantamento de fornecimento futuro" (mesma ilicitude do art. 172 + simulação; contas mensais ao AJ são dever legal — art. 52, IV, com destituição na inadimplência); alternativas executáveis: à vista impecável, antecipação genuína sobre pedido real (4 testes), proposta de critical vendor no plano e petição de autorização judicial (art. 66, não verificado).

### Sessão 2
6. `sessao2/analise_plano.md` — 6 cláusulas: trabalhistas 18 meses **ilegal** como redigida (art. 54 e §2º); deságio 60%/120x/24m classes III–IV **legal** (ressalvas: pessoas ligadas, assembleia não verificável); fiduciários "sujeitos ao plano" **ilegal** (art. 49 §3º); União com deságio 50%/180x **ilegal** (CTN 187; art. 68); venda do galpão UPI **legal com ressalvas** (art. 6º-B; regime UPI não verificado); omissões (CND+/art. 57, assembleia, extraconcursais).
7. `sessao2/efeito_tributario_desagio.json` — schema validado: `ganho_desagio = 3.882.000` ((4.200.000+1.850.000+420.000)×0,60 — somente classes III+IV; fiduciário/União ilegais excluídos); `pis_cofins_sobre_ganho = 0` (art. 50-A, I); `trava_30_aplicavel = false` (art. 50-A, II); `prejuizo_fiscal`, `compensacao`, `base_irpj_csll`, `irpj_csll = null` — **saldos que o cliente não possui; não inventados**.
8. `sessao2/efeito_tributario_desagio_notas.md` — aritmética, cenários de compensação (PF≥3.882.000 → base 0; PF=0 → base 3.882.000, imposto ≈ 1.319.880 a ~34%, **alíquotas não verificadas**), efeito CPC 48 a valor presente (taxa do plano desconhecida), alerta não verificado sobre legislação pós-2024 de compensação.

### Sessão 3
9. `sessao3/lancamentos_novacao.json` — 5 lançamentos (ids 1–5), todos com D=C conferidos: baixa Classe III 6.050.000 → novo passivo 2.420.000 + ganho 3.630.000; Classe IV 420.000 → 168.000 + 252.000; trabalhistas 960.000 reclassificados (sem deságio); adesão ao parcelamento federal 2.700.000 (reclassificação, não novação — CTN 187); galpão UPI condicional (valor contábil desconhecido). Fechamento: ganho 3.630.000 + 252.000 = **3.882.000** = JSON da Sessão 2 ✔; passivo pós-plano nominal 9.348.000.
10. `sessao3/passivo_fiscal_solucao.md` — Via A: 120× R$ 22.500; Via B: 30% em PF (810.000) + 1.890.000 em 84× R$ 22.500; Via C (transação, teto 70% desc.): 810.000 em 120× R$ 6.750. Recomendação: **C → A como piso**, preservando PF para o ganho (PF pleno necessário: 4.692.000). Todas geram CND+ (art. 57; CTN 191-A); execuções não suspensas (art. 6º §7º-B) — agir na janela de 180 dias prorrogável.

## Perguntas (estadas em `QUESTIONS.md`)

Respondido: só o item Norte (parcial: à vista novo + pedido de "sinal" — tratado no adendo). Cliente **não tem informação** para os demais ⇒ **desconhecidos permanentes**, sem re-pergunta: data exata do pedido; semanas 5–13 do fluxo; abertura dos R$ 5,75 mi pagos; composição do débito federal e **saldo de prejuízo fiscal**; credores pessoas ligadas (art. 50-A, parágrafo único); trabalhistas individualizados/Simples da Sul; valor contábil e situação do galpão; honorários do AJ. Cada um tem mitigação documental listada em `QUESTIONS.md`.

## Não verificados (não usados como fundamento)

Arts. 66, 60-A (UPI), 58 (quóruns), 41/83 (classificação trabalhista), 7º III; alíquotas de IRPJ/CSLL (~34%, ilustrativo); suposta restrição pós-2024 à compensação de prejuízos; critérios internos da Portaria PGFN 2.382/2021 além do teto 70%/120.

## Premissas declaradas

Deferimento do processamento (12/03/2026) como referência do pedido; semanas 1–4 = pós-pedido; novo passivo do plano a **valor nominal** (taxa de desconto não informada — com taxa, passivo cai e ganho sobe pela diferença, CPC 48).
