# Perguntas ao cliente — DAS maio/2026 (Lumen Soluções Digitais ME)

Contexto: o DAS de maio/2026 foi apurado com o que constava em `documents/`. O valor do imposto
não dependia das perguntas (todas as leituras dos dados resultam no mesmo anexo e faixa — ver
`memoria.md`). As perguntas da 1ª rodada foram enviadas ao cliente; ele respondeu e informou
que, para o que não foi respondido, **não tem mais nada a acrescentar** — nenhuma pergunta nova
foi enviada. Este arquivo ficou como registro: respostas recebidas, sem resposta e incertos
que permanecem explícitos em `STATUS.md`.

## Respostas recebidas

1. ✔ **Respondida — pró-labore de abril.** Pago em **30/04/2026** (2 × R$ 1.600 = R$ 3.200). O
   resumo o exibia "em aberto" porque o PIX só foi **lançado** no contábil em maio (não foi um
   pagamento em 06/05). O cliente disse enviar o comprovante de 30/04, mas o arquivo
   **não consta em `documents/`** (incerto 3 em `STATUS.md`). *Efeito:* pago dentro da janela
   mai/2025–abr/2026 (Res. CGSN 140, art. 26, §2º) ⇒ o valor **permanece** na base do Fator R de
   maio/2026: folha 12m = R$ 284.600,00, **Fator R 27,90%** (< 28%) ⇒ Anexo V, faixa 4 — ver
   `memoria.md` §2. O DAS de maio não muda; para junho/2026 não há mais nada a ajustar por esta
   resposta.

2. ◐ **Parcial — locação de notebooks à Orla.** "Alugamos 20 notebooks pra Orla **por uns
   meses**" e a NF-e foi emitida porque "locação não é NFS-e". Confirma que a locação é corrente
   (não pontual) e valida a escolha do documento (coerente com `memoria.md` §4 e **[LOCACAO]**).
   **Não confirmou** se os valores dos meses anteriores à NF-e 000.512 estão somados em
   `faturamento_12_meses.csv` ("receita_bruta"). *Efeito:* segue incerto — incerto 1 em
   `STATUS.md`, com sensibilidade: se 2–6 meses × R$ 6.000 estiverem fora do CSV, o DAS de
   maio/2026 passa de R$ 15.188,84 para até ~R$ 15.238,24 (+0,3%); anexo e faixa não mudam.

## Sem resposta (o cliente informou não ter mais nada a acrescentar)

3. **Base do resumo de folha.** Não recebemos extratos de 2025-05 a 2026-03; sem eles não é
   possível remapear cada pagamento pelo mês em que ocorreu (o extrato de maio/2026 mostra,
   p.ex., "DARF/GPS/FGTS ABR" −4.700 só em 07/05). Incerto documentado em `memoria.md` §9 (A3).
   *Efeito:* nenhum no resultado — o Fator R fica entre 25,49% e 27,90% em qualquer leitura,
   sempre < 28%.

4. **Linha "obs" do resumo.** A observação do pró-labore de abril citada na linha da competência
   2026-03 não teve confirmação de deslocamento de linha. *Efeito:* nenhum — a observação
   referia-se ao pró-labore de abril, já tratado (pago 30/04, item 1 acima).

## Incertos remanescentes (índice)

- 1) composição do `faturamento_12_meses.csv` quanto a locações anteriores (RBT12);
- 2) repartição do Anexo V ausente de `library/` (campo `reparticao` zerado, não validado);
- 3) comprovante de 30/04 do pró-labore de abril não anexado ao acervo;
- 4) pagamentos de folha anteriores a maio/2026 — remapeamento impossível sem extratos;
- 5) extrato `.pdf` ilegível ⇒ adotado o `.csv` espelho.

Detalhes e quantificação em `STATUS.md` ("Itens abertos").
