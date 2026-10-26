# STATUS

**COMPLETE WITH OPEN ITEMS**

Atualização pós-2ª rodada: respostas da cliente incorporadas (comissão de administração 8%; IPTU/condomínio dos imóveis vagos pagos por ela, sem montantes; desejo de mínimo legal para Marcos com cláusulas de proteção). Conforme informado, **não há informação adicional** para os demais itens — cada um virou premissa destacada no parecer, sem re-encaminhamento de perguntas.

Atualização pós-3ª rodada: pergunta da cliente — "se doar tudo em vida, o Marcos herda nada?" — respondida no parecer (item 4): **não**; piso invariante de **3.088.333,33** preservado por colação (arts. 544 e 2.002) e pela nulidade do excesso (art. 549), com o excedente de 9.265.000 redutível. Sem novos unknowns.

Auditoria pré-entrega: todos os números do parecer e do `numeros.json` recomputados (aritmética decimal) e todas as citações conferidas palavra por palavra contra os 6 arquivos da biblioteca. Ajustes desta rodada: (i) item 4 do parecer — legítima citada pelos arts. 1.845-1.846 (o art. 1.789 aparece só na linha de citação da biblioteca, sem texto reproduzido); (ii) retirada a afirmação "base legal do ITBI = valor venal municipal" (parecer item 1, Premissa C, `numeros.json`, QUESTIONS item 1, STATUS item 3) — a biblioteca não traz a base; a estimativa de mercado permanece como premissa rotulada "não verificável"; (iii) removido o gloss "(fato gerador consumado)" no item 3 do parecer (não é texto da biblioteca); (iv) registrada a opção de ITCMD integral no ato, que a biblioteca menciona junto ao 2/3-1/3; (v) rotuladas como inferência (arts. 1.848 + 544) as cláusulas restritivas em doação — sem regra textual na biblioteca; (vi) nota do RE 1.495.108 (Tema 1.348) acrescentada ao item 1 do parecer (consta da biblioteca); (vii) QUESTIONS item 6 reescrito — o efeito de outras despesas sobre a vantagem da PJ depende do tipo (dedutível no carnê-leão: reduz; fora da lista: aumenta); (viii) "demais regras da colação (arts. 2.002-2.012)" e "base legal do ITBI-SP" incluídas na lista de não verificáveis do parecer. Nenhum cálculo alterado.

## Entregáveis
- `parecer.md` — aferição das 5 afirmações com números, estrutura recomendada (incluindo plano de "mínimo possível" para Marcos), limites e premissas A–E. ✔
- `numeros.json` — no schema do contrato; valores da 2ª rodada: PF 257.756; PJ total 145.358 (IRRF 21.326); ITCMD da doação recomendada 328.600. ✔
- `QUESTIONS.md` — respostas da cliente registradas inline (itens 2 e 8); itens sem resposta transformados em premissas, sem re-encaminhamento. ✔

## Itens em aberto (unknowns explícitos)
1. **Tabela progressiva do IRPF (faixas) não consta da biblioteca** → IR da PF pela alíquota de teto 27,5% sobre a base deduzida da comissão (78.108/mês) — sobrestima o IR; conclusão se mantém.
2. **Base do IRRF da Lei 15.270/2025** (excedente × total acima de R$ 50 mil/mês) não explicitada na biblioteca → JSON assume "sobre o excedente" (21.326/ano); cenário alternativo no parecer (81.326/ano; carga PJ 20,16%).
3. **Base do ITBI**: base legal não reproduzida na biblioteca (não verificável); valor venal municipal não informado → estimativa usa valor de mercado; se a base real for menor, cai na proporção da diferença.
4. **Faixas de alíquota do GCAP** não reproduzidas (só o intervalo 15%-22,5%) → `gcap_evitado` usa a faixa mínima (15% × 11.710.000 = 1.756.500; até 2.634.750 na superior).
5. **Dispositivo "2/3-1/3" do ITCMD** (Lei 10.705/2000, art. 9º) vem com a ressalva "verificar" da própria biblioteca → o total não muda; muda só o timing do caixa.
6. **Causas legais de deserdação (arts. 1.961-1.965)**: dispositivos listados, causas não reproduzidas na biblioteca → o rompimento de 6 anos **não foi confirmado como causa legal**; exclusão de Marcos exige orientação formal com fatos e prova. **Cláusulas restritivas em doação inter vivos fora da legítima**: não verificável na biblioteca.
7. **IPTU/condomínio dos vagos** (pagos pela cliente) sem montantes; **dos locados**, pagador desconhecido → não deduzidos em nenhum cenário (se comprovados, a carga da PF cai e a vantagem da PJ diminui).
8. **Passivos, regimes de bens dos filhos, colação de nua-propriedade/usufruto, ISS, custas de inventário, LC 214/2025** → sem fonte na biblioteca ou sem informação; premissas destacadas no parecer (A–E).

## Observação de consistência
Nada foi forçado a fechar. Economia anual IR (PF 257.756,40 − PJ 145.358,08 = **112.398,32**) paga o ITBI (492.900) em ≈ **4,39 anos**. O **ITCMD total do plano é invariante**: doação (328.600) + inventário (412.600) = **741.200 = 4% × 18.530.000** — o mesmo de um único inventário; a estrutura muda timing e pagador, não o total. O piso de Marcos (1/3 × 9.265.000 = **3.088.333**) é invariante pela colação dentro do teto disponível; abaixo disso só deserdação com causa legal provada (fora do escopo aritmético deste parecer).
