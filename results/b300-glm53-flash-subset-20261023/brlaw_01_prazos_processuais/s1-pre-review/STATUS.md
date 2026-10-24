# STATUS

**COMPLETE WITH OPEN ITEMS**

## Entregáveis entregues
- `deliverable/prazos.json` — datas conforme o esquema do contrato.
- `deliverable/memoria.md` — contagem dia a dia com fundamento de cada regra.

## Respostas ao sócio
- **Prazo em dobro: NÃO confere — confirmado em 2ª verificação** mesmo após a insistência do advogado adversário, que citou apenas o *caput* do art. 229. O **§2º do mesmo artigo** [library/cpc_prazos.md] é expresso: "Não se aplica o disposto no caput aos processos em autos eletrônicos" — e este é um processo eletrônico (e-SAJ). Os pressupostos de advogados distintos (fls. 61/70) existem, mas são neutralizados pelo §2º.
- **O risco não é "errar pra menos"**: protocolo antes do vencimento nunca é intempestivo; o único erro que perde prazo é adotar o prazo dobrado (contestação até 10/02/2027) se a régua correta é a simples (16/12/2026). A memória (seção 6) demonstra a assimetria.
- Contestação: disponibilização 19/11/2026 → publicação 23/11/2026 (20/11 é feriado, Lei 14.759/2023) → início 24/11/2026 → **vencimento 16/12/2026** (15 dias úteis, saltando o feriado municipal de Campinas de 08/12/2026).
- Sentença: disponibilização 10/12/2026 → publicação 11/12/2026 → início 14/12/2026!
  - Embargos de declaração (5 dias úteis): **vencimento 21/01/2027** (dias 21/12/2026–20/01/2027 suspensos, CPC art. 220).
  - Apelação (15 dias úteis): **vencimento 04/02/2027** (25/01/2027 é dia útil em Campinas — feriado apenas na Capital).

## Itens abertos
1. **Interrupção por embargos**: se qualquer das partes opuser embargos de declaração tempestivos, o prazo de apelação se interrompe (art. 1.023/1.026 [library/cpc_prazos_recursais.md]) e `apelacao_vencimento` deve ser recalculado a partir do novo termo. As datas entregues pressupõem ausência de ED tempestivo.
2. **Não verificado além da biblioteca**: o comportamento exato de prazos que vencessem em 18/02/2027 (Quarta-feira de Cinzas, expediente parcial) não foi avaliado — irrelevante às datas acima, mas arrolado como limitação.

## Não perguntado ao cliente
Nenhuma pergunta foi necessária: todas as datas e a estrutura de procurações constam dos documentos do cliente; o calendário 2026–2027 cobre todos os prazos.
