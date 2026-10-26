Sessão 5. Antes de calcular, vou reler o contrato (schema exato), os arquivos da biblioteca de garantia/transação e conferir o estado dos arquivos:

Contrato e bibliotecas confirmados. Antes de fechar a matemática, vou ancorar a data-base do cálculo SELIC-documentado (S2) e os valores por período:

Agora a nota ao cliente da Sessão 5, com toda a memória de cálculo:

Agora as perguntas novas da Sessão 5 (P13–P15):

Auditoria final de todos os arquivos (verificando reversões do ambiente):

Sessão 5 concluída — status **COMPLETE WITH OPEN ITEMS**. Tudo auditado por script (JSON válido, chaves exatas do schema, 15 âncoras aritméticas conferidas).

## Entregues (`deliverable/sessao5/`)

**`garantia.json`** — schema exato do contrato:
- `valor_remanescente_atualizado`: **591.000** (documentado até a inscrição 10/07/2026: principal 307.320 + multa 230.490 + SELIC 53.190; conferência: 1.100.000 − 509.000 decaídos)
- `seguro_garantia`: 768.300 garantidos (591.000 × 1,30 — Portaria PGFN 164/2014, art. 3º); custo anual até **11.524,50** (1,5%)
- `fianca`: mesmos 768.300; custo anual até **23.049,00** (3%)
- `transacao`: base 591.000 (os 509.000 decaídos ficam fora — a biblioteca veda transacionar débito decaído); desconto estimado **184.392** (65% × 283.680 de multa+SELIC, abaixo do limite do principal); saldo ~406.608 em até 120 parcelas
- `recomendacao`: seguro + litigar; transação só como plano B

**`nota_ao_cliente.md`** — memória completa: sensibilidade da garantia por cenário (768.300 → 659.100 com DARF → 359.463 ganhando tudo); carrego de 3 anos (seguro 18,4–34,6 mil vs fiança 46–69 mil); transação a 65% e 70% (se ME/EPP — não verificado); a tabela que decide: **ganhar só a nulidade da multa (360.510) já bate qualquer transação (406.608/392.424) e sem confissão**.

## Recomendação (resumo)

Seguro-garantia → embargos (mérito dos depósitos + excesso dos DARF + nulidade da multa) → transação apenas depois de planilha PGFN + CAPAG + confirmação ME/EPP, **nunca sem ordem escrita** — a adesão é confissão irrevogável e mataria exatamente as defesas que ainda valem até 314.490.

##ressalvas registradas
- **SELIC superveniente** (após 10/07/2026) não é calculável pela biblioteca (sem série histórica) — os números são o piso documentado; planilha atualizada pedida ao cliente (P14).
- Prêmio aplicado sobre o valor garantido (premissa de mercado; sensibilidade sobre o débito também mostrada na nota).

Controle atualizado: `STATUS.md` (cabeçalho S5, seção de entregues, item 5 operacionalizado, item 13 = aguardando ordem do cliente) e `QUESTIONS.md` (**P13** ME/EPP + CAPAG + imóveis próprios; **P14** planilha atualizada da PGFN — que também fecha a dúvida da dedução dos DARF; **P15** ordem sobre garantia+litígio × sondagem de transação).

O engajamento de cinco sessões está inteiro em `deliverable/` — aguardando as respostas P10–P15 para as providências práticas (juntada de documentos, apólice, embargos).