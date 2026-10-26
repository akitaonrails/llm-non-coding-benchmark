# STATUS — COMPLETE WITH OPEN ITEMS (itens finalizados como incógnitas sinalizadas)

Turno de revisão pré-entrega: todos os números foram recalculados por script (battin = todos conferem), todas as citações foram conferidas contra `library/INDEX.md` e os trechos dos arquivos, e a reconciliação (cronograma = gcap_total; líquidos) foi verificada. Correções aplicadas ao memorando: (i) teto real do escalonamento da distribuição corrigido (economia de IRRF de até R$ 705.600, não ~R$ 10 mil — conclusão inalterada: A vence por R$ 774.000 mesmo com IRRF zero); (ii) preço de empate de B duplamente delimitado (≈ R$ 10,77 mi no melhor caso extremo; ≈ R$ 12,09 mi na hipótese conservadora); (iii) nota de que a biblioteca não especifica se os 10% da Lei 15.270/2025 incidem sobre o excedente ou o total; (iv) flags de escopo para CTN art. 149, base dos 4% da Lei 14.973/2024 e alíquota de presunção 32% (fato do cliente, não citável); (v) rótulo de citação e referências cruzadas internas corrigidos. Nenhum número do `comparativo.json` mudou.

Turno 2: o cliente respondeu que **não possui informações adicionais**. As perguntas foram encerradas (não serão re-perguntadas) e convertidas em **assunções explicitamente sinalizadas**, com o impacto de cada uma dimensionado e limitado (bounds) na seção 7 do `memorando.md`. Nenhum número do `comparativo.json` mudou — as assunções originais foram mantidas.

Entregáveis presentes em `deliverable/`:
- `comparativo.json` — válido; chaves conforme especificação; cronograma soma = gcap_total
- `memorando.md` — memória de cálculo com aritmética explícita; resposta à Beatriz; análise da alegação de ágio do comprador; riscos e pontos de negociação; **seção 7: tabela de incertezas residuais e robustez**; só citações de `library/INDEX.md`
- `QUESTIONS.md` — encerradas (turno 2); `PERGUNTAS.md` — ponteiro
- `STATUS.md` — este arquivo

Conclusões (inalteradas e robustas a todas as incógnitas):
- Recomendação: **PF — venda de quotas (Proposta A)**. Líquido A = R$ 7.830.000 × B = R$ 6.350.400 (vantagem A = R$ 1.479.600). Mesmo no melhor caso de B (IRRF efetivo zero na distribuição inteira, por escalonamento dentro da faixa ou lucros pré-2025), A vence por R$ 774.000; para empatar, B exigiria preço entre ≈ R$ 10,77 mi (melhor caso extremo) e ≈ R$ 12,09 mi (hipótese conservadora), ou ~R$ 14,8 mi de dividendos isentos na distribuição lump-sum.
- DIRPF: **não retificar** o custo para R$ 2 mi/sócio — crime (Lei 8.137/90, art. 1º, I e II) e revisão de ofício (CTN, art. 149); custo correto é o declarado (R$ 600 mil/sócio).
- Follow-up da Beatriz (turno 3 — "lei de atualização de bens, ao menos parcial?"): respondido na **seção 4.1 do memorando**. Regra: custo é o declarado na DIRPF, atualização só por hipótese legal expressa; a única listada na biblioteca (Lei 14.973/2024, opção com pagamento de 4%) tem **prazo encerrado**; "atualização parcial" sem fato que a funde é a mesma vedação e o mesmo risco criminal. Resposta permanece **nao** (JSON inalterado).
- Alegação de ágio do comprador não se sustenta na compra de estabelecimento (Lei 12.973/2014 exige incorporação/fusão/cisão + laudo); usar como alavanca de preço na estrutura A.

Incógnitas sinalizadas (abertas por falta de informação do cliente; bounds na seção 7):
1. Data do fechamento — sem impacto nos valores (rótulos do cronograma).
2. Correção monetária das parcelas (A) — se houver, só melhora A.
3. Lucros pré-2025 com distribuição aprovada até 31/12/2025 (B) — se existirem, só melhoram B, insuficiente para empatar.
4. Ajuste do IRPFM sobre o IRRF da distribuição (B) — tabela do IRPFM ausente da biblioteca: **não verificável**; bound superior tratado.
5. Residência fiscal dos sócios — assunção: residentes no Brasil; se falso, a ponta PF exige reavaliação (fora da biblioteca).
6. Garantias das parcelas da Proposta A — risco negocial não resolvido; action item pré-fechamento (caução/penhor/aval).
