

The library's `verbas_reversao.md` actually backs the 45-day aviso, the verbas menu, **and** the CLT 223-G reference — good. Now the full audit of both deliverables:





The grep confirms the exact defect locations. Before patching, let me see §2 (premises) and §5.1 to place the férias assumption correctly:





All defects located. Quick fact-check before the férias-assumption note — is the prontuário actually silent on accrued vacation?





Confirmed — the prontuário never mentions férias, so that must be disclosed as an assumption. Applying all fixes:













Auditoria completa — tudo revalidado. O único "residual" nos greps é o próprio log de correções no `STATUS.md` (cita as palavras corrigidas de propósito). Conclusão e todos os totais permanecem intactos.

## O que encontrei e corrigi (9 itens)

**Erros aritméticos/de datas**
1. **`parecer.md` §7.1 e §7.2 — "50 dias" → 47 dias.** De 21/08/2026 (e-mail da Renata) a 07/10/2026 há 47 dias, não 50. O §3.2 e o JSON já diziam 47 — os números internos agora batem em todos os pontos.

**Autoridade não suportada (regra do contrato: só `library/` é citável)**
2. **`parecer.json` alternativa 3 — "acordo firmado sob pressão durante estabilidades **é anulável**"**: disciplina de invalidade de negócio jurídico (coação) **não está na biblioteca**. Rebaixado a "premissa NÃO verificada — não a invoco como fundamento", mantendo a recomendação prática (advogado + contrapartida real).
3. **Rodapé do `parecer.md` citava "art. 484-B CLT"** como exemplo fora-da-biblioteca — artigo que nunca foi invocado e cujo próprio número não posso verificar sem a biblioteca. Substituído por formulação descritiva ("regras de acordo de rescisão por mútuo consentimento").

**Incoerências internas / redação**
4. **§7.3, "Comparação final": "R$ 228,5–351,3 mil"** conflitava com o parágrafo anterior, que diz que o dano moral de 15 mil **some** na dispensa sem justa causa. Corrigido para **R$ 228,5–336,3 mil** (teto sem o item "k"), com ressalva de que outras pretensões podem reconfigurá-lo.
5. **§4.3 dizia "indenização de todo o período até a dispensa"** — direção invertida. Corrigido: **da dispensa até o fim da estabilidade**.
6. **Recomendação final: "R$ 243,5 mil + reintegração"** sugeria soma; reintegração é **alternativa** à indenização (com os salários do período). Redação corrigida.
7. **§5.1 — presunção de férias explicitada**: conferi os documentos — o prontuário **não registra férias vencidas**; a premissa "nenhuma pendente" estava implícita e agora está escrita como **item aberto**.
8. **Typo "alcanceado" → "alcançado"** (§7.3).
9. **`STATUS.md`** passou a registrar a rodada de revisão com as 9 correções.

## O que foi auditado e **não** precisou de correção
- **Todos os números re-recalculados**: aviso 45×260 = 11.700 (bibliosa `verbas_reversao.md` dá "30 + 3/ano"); 13º 7.150 e férias 6.933,33 com projeção do aviso documentada; multa FGTS 624×67×0,40 = 16.723,20; verbas 42.506,53; gestante 347d → 107.762,78; CIPA 599d → 186.022,78; totais **243.529,31 / 351.292,09 / 228.529,31 / 336.292,09** batem.
- **Cada citação rastreada até `library/INDEX.md`** — inclusive a referência ao **CLT 223-G** (§5.3), que verifiquei estar no texto de `verbas_reversao.md` ("até 3 salários leve, 5 média, 20 grave") — suportada; Lei 9.029/95 só aparece com aviso "detalhe fora da biblioteca".
- **JSON**: parseia, chaves exatas do schema do `CONTRACT.md`, `total` confere com os componentes, `justa_causa_cabivel: false`, datas das estabilidades como "AAAA-MM-DD + descrição" como o schema permite.

Nada abriu pergunta nova ao cliente; os itens abertos continuam U1–U6 em `PERGUNTAS.md`. **STATUS: COMPLETE WITH OPEN ITEMS — entregue.**