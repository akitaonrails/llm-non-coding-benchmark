# STATUS

## COMPLETE WITH OPEN ITEMS — rodada 2 incorporada (respostas da cliente de 24/10/2026)

Entregáveis presentes: `parecer.md` (5 afirmações verdictadas + estrutura recomendada + limites), `numeros.json` (schema do contrato, JSON revalidado após as trocas), `QUESTIONS.md` (18 itens com status + novas Q19–Q21), `PERGUNTAS.md` (top-5), `STATUS.md`.

Vereditos (inalterados pela rodada 2): (1) "integralizar sem ITBI" **FALSA** — locação preponderante, CTN 37 §§1º-2º, empresa nova 3 anos; planejar pagamento, não litígio (Tema 1.348 pendente); (2) "só 11,33%" **verdadeiro como modelo, falso neste caso** — carga real **12,17%–14,27%**; (3) ITCMD **4% correto, base contábil falsa** (base = patrimonial atualizado/mercado); (4) "tir Marcos da sucessão" **FALSA** (herdeiro necessário; só deserdação/indignidade); (5) cláusulas restritivas **DEPENDE** (justa causa, CC 1.848) e "protege dos credores" **sem fonte na library**.

### O que as respostas de 24/10/2026 mudaram (recalculado, script único)

- **Comissão 8%** (81.504/ano): no Presumido **não** reduz tributo federal (presunção de 32% incide sobre a receita — library) → federal segue **124.031,64 (12,17%)**; mas reduz o **distribuível**: 1.018.800 − 124.031,64 − 81.504 = **813.264,36 = 67.772,03/mês**.
- **IRRF 2026**: cenário de planejamento (estrutura final concentra renda na usufrutuária → 1 PF) = 10% × (67.772,03 − 50.000) × 12 = **21.326,44** → carga total **145.358,08 = 14,27%**. Com ≥2 PFs ≤ 50 mil/mês (33.886 cada) o IRRF zera (12,17%) — viável só antes da doação ou se filhos já forem sócios plenos (contador).
- **PF**: comissão é dedutível pela library → `pf.ir_anual` **257.756,40** (teto com a única dedução conhecida; era teto bruto sem ela). IPTU/condomínio mensais não informados (Q21) → pode cair mais.
- **Economia/payback do ITBI**: 133.724,76/ano (sem IRRF) → **~3,2 anos**; 112.398,32/ano (com IRRF) → **~3,9 anos**; por imóvel 2,7–4,8 (Galpão melhor, Jardins pior) / 3,2–5,7 com IRRF.
- `numeros.json`: `pf.ir_anual` 257.756,40; `pj_presumido.irrf_distribuicao_2026` 21.326,44; `total` 145.358,08 — demais campos inalterados.
- Confirmados sem mudança de conta: Casa CDJ/Cotia fora da PJ; netos existem; renda pessoal dela melhora no plano (67.772/mês brutos vs até ~56.628 líquidos atuais), mas o **piso dela é desconhecido** (aluguel de Higienópolis, Q19).

### Inalterados pela rodada 2

ITBI 432.900 (cenário-base de pagamento; teto Tema 796 se base = capital: 126.600, com 306.300 em discussão; sensibilidade Galpão 11% não citável → até 680.900) · GCAP evitado 2.297.250 (integralizar a 4.220.000, Lei 9.249 art. 23) · ITCMD 577.200 (384.800 + 192.400 com usufruto; alternativa 370.600 rejeitada) · sucessão: acervo 18.530.000, legítima 9.265.000, quinhão 3.088.333,33, folga na disponível 1.011.666,67 · aluguel anual 1.018.800, rendimento dos locados 7,06%.

### Itens abertos (não reconciliados / dependem de fatos)

1. **Divergência interna da library, deixada aberta de propósito:** adicional do Presumido sobre o excedente → 124.031,64 (12,17%) vs resumo "≈14,53% acima" (adicional sobre toda a base) → 148.031,64. Banda registrada no parecer §2; nenhuma das duas é validável com a biblioteca.
2. **Premissas mantidas porque a cliente não tem a informação** (Q1, Q4–Q6, Q10, Q12–Q13, Q16–Q17): patrimônio 100% dela (meação ⇒ números sucessórios ~à metade); ITBI 3% em todos os municípios; bases = valores do CSV; tabela IRPF 2026 ausente (`pf.ir_anual` = teto, não estimativa); sem dívidas/avais conhecidos (condição de contorno da doação). Exigem documentos; viraram limites no parecer §7.
3. **Desconhecidos novos (Q19–Q21)**: aluguel que ela paga em Higienópolis; valores mensais de IPTU/condomínio pagos pela locadora; **"vagos" inexistentes no CSV** — se houver imóvel fora da lista, o patrimônio inteiro do parecer muda.
4. **Qualificações jurídicas fora da library**: se ~6 anos de rompimento configuram justa causa (CC 1.848/1.961 ss. não transcritos); cláusulas sobre a disponível e eficácia contra credores — advogado. IRRF na estrutura final com usufruto — contador.
5. **Itens que a própria library marca como não validados:** usufruto ITCMD 2/3+1/3 ("verificar"); percentuais autodeclarados "modelo"; Temas 1.348 / Lei 15.270 / LC 214 citados sem texto (sensibilidade IBS/CBS não quantificável).
6. **Liquidez:** aplicações 2.100.000 cobrem aritmeticamente os ~818 mil à vista (ITBI 433 mil + ITCMD 385 mil); folga real depende de Q19.

Nada foi consultado fora de `library/INDEX.md`; o que não está lá está rotulado como não verificado ou remetido a `QUESTIONS.md`. Números desta rodada: script único de cálculo, contas-aritmética reproduzidas no parecer §2/§4.
