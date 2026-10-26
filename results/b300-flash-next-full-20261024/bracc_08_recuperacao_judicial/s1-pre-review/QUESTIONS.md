# Perguntas ao cliente — estado final

**Rodada 1 enviada (Sessão 1). Respostas recebidas:** apenas o item 9 (parcial) — ver abaixo. O cliente declarou **não ter informação adicional** para as demais. As perguntas não respondidas **não serão reenviadas**; passam a **desconhecidos permanentes**, sinalizados nos entregáveis que dependem delas. Elas só podem ser sanadas por documentos de terceiros (contabilidade/ex-CAC/extratos/relação do AJ), não por nova pergunta ao cliente.

## Respondido (parcial)

- **9. Fornecedor Norte.** Resposta do cliente: *"o Norte aceita continuar fornecendo à vista a partir de agora, mas quer 'um sinal' sobre o atrasado; se eu não pagar, eles param."*
  - Tratado em `sessao1/addendum_sinal_norte.md`: fornecimento à vista novo = pagar normalmente (art. 67, extraconcursal); **"sinal" sobre o saldo pré-pedido = pagamento de concursal fora do plano, vedado** (art. 172; novação só na homologação). Vias legítimas para o saldo velho: tratamento diferenciado no plano aprovado em assembleia ou autorização judicial (art. 66 — não verificado).
  - **Sub-item não respondido:** se há outros créditos pré-pedido do Norte além dos R$ 1.850.000 da relação, e o prazo factual de paralisação das entregas. Tratado como: relação do AJ é a fonte oficial (art. 7º, III — não verificado no detalhe) e o risco de ruptura está precificado no demonstrativo como alerta ao AJ.

## Desconhecidos permanentes (cliente não tem a informação — não re-perguntar)

| # | Item | Impacto / onde está sinalizado | Mitigação (fonte externa, não o cliente) |
|---|---|---|---|
| 1 | **Data exata do protocolo do pedido** (só se tem o deferimento do processamento, 12/03/2026) | Corte do art. 49; classificação Norte (310.000 pós-pedido) | Cópia da petição inicial/autuação no processo (juízo da RJ) |
| 2 | **Semanas 5–13 do fluxo de caixa** (arquivo traz só 1–4) | Demonstrativo mensal cobre 4 de 13 semanas | ERP/Tesouraria; demonstrativos mensais sucessivos ao AJ |
| 3 | **Abertura dos R$ 5.750.000 pagos (semanas 1–4)** | Atestado de que nada foi pago a concursal pré-pedido | Razão auxiliar / extratos bancários do período |
| 4 | **Composição do débito União (tributo/inscrição) e saldo de prejuízo fiscal e base negativa** | Sessões 2–3: campos `null` em `efeito_tributario_desagio.json`; Via B vs. preservação de PF em `passivo_fiscal_solucao.md` (PF ≥ 4.692.000 p/ cenário pleno) | Laudo de IRPF da contabilidade; extrato e-CAC/PGFN (posicionamento por inscrição) |
| 5 | **Credores pessoas ligadas** (Alfa/Beta/Norte/Sul vs. controladores) | Condição do art. 50-A (parágrafo único) — ganho pode perder o benefício PIS/COFINS | Quadro societário + Partes Relacionadas (e-CAC/LEI); declaração de controladores |
| 6 | **Sul EPP optante do Simples; créditos trabalhistas individualizados (teto 40 SM)** | Enquadramento Classe IV; eventual excedente quirografário | Certidão Simplificada da Junta; folha/homologações trabalhistas |
| 7 | **Galpão/UPI:** proposta/contrato, ônus, valor contábil | Lançamento id 5 em `lancamentos_novacao.json` fica sem valores; ganho de capital não calculável | Matrícula do imóvel; razão do imobilizado; carta de intenção do comprador |
| 8 | **Honorários do AJ e da assessoria** | Coluna extraconcursais dos demonstrativos mensais | Petição de fixação de honorários nos autos |

## Pergunta única que ainda faríamos (e por quê)

Nenhuma em aberto para o cliente. O que falta é **documento, não depoimento**. Se o cliente quiser fechar os `null` das Sessões 2–3, a lista de compras documental está na coluna "Mitigação" acima — a mais crítica é a **4** (prejuízo fiscal), que decide a estratégia entre Via B e Via C da União e o IRPJ/CSLL sobre o ganho de 3.882.000.
