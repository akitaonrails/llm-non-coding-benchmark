# QUESTIONS.md — perguntas ao cliente (Atlas Distribuidora S.A.)

**Da:** Controller
**Para:** Diretor Financeiro/Administradores
**Contexto:** Sessão 1 (mês do pedido) encerrada com `COMPLETE WITH OPEN ITEMS`; os itens abaixo desbloqueiam a Sessão 2 (análise do plano/efeito tributário) e a Sessão 3 (novação/União) e aperfeiçoam o demonstrativo do mês 1.

1. **Data exata do pedido** da RJ (protocolo)? Preciso do marco de corte concursal × pós-pedido e do período formal do demonstrativo do art. 52, IV. Os dados sugerem algo entre 03/02/2026 e 12/03/2026.
2. **Fluxo de caixa:** o arquivo se chama `fluxo_caixa_13_semanas.csv`, mas contém apenas as semanas 1–4. Favor enviar as semanas 5–13 (mesmas colunas) e a data de início da semana 1.
3. **Prejuízo fiscal:** saldo disponível acumulado (IRPJ e CSLL separado) e lucro real do período; regime atual de tributação (real? presumido?). Necessário p/ compensação do ganho do deságio na Sessão 2.
4. **Fornecedor Norte — entrega de 20/03/2026 (R$ 310.000):** já foi paga? Se não, há prazo/acordo?
5. **Composição dos pagamentos semanais pós-pedido** (R$ 1,38–1,55 mi/semana): lista por credor. Preciso confirmar que nenhum deles é credor concursal sendo pago por fora.
6. **Pessoas ligadas (art. 50-A, parágrafo único):** há, entre os créditos a renegociar, dívida de sócio/diretor/empresa ligada? Se sim, o benefício tributário do art. 50-A não alcança a parte correspondente.
7. **Encargos:** a minuta não menciona juros/correção — as 120 parcelas dos quirografários/ME-EPP e o pagamento trabalhista em até 18 meses têm índice/taxa? E o parcelamento da União (Selic etc.)? Necessário p/ PV no teste de novação de 10% (CPC 48) e valores da Sessão 3.
8. **UPI (galpão):** valor contábil, eventual garantia sobre o imóvel e data-alvo da venda; e se a alienação se fará por via judicial (afeta o tratamento do art. 6º-B).
9. ~~**Banco Beta:** as máquinas dadas em alienação fiduciária são **bens de capital essenciais**?~~ **RESOLVIDO** — resposta da diretoria: *"As máquinas do Beta são a linha de separação de pedidos; sem elas, não opera."* → bens de capital essenciais; art. 49, §3º aplicado por inteiro (propriedade prevalece + vedação de venda/retirada durante a suspensão do art. 6º, §4º). Registrado no adendo da `sessao1/resposta_diretor.md`.
10. **Minuta/plano:** além do que a minuta diz, há proposta de garantias reforçadas ou tratamento igualitário aos trabalhistas p/ amparar 18 meses no art. 54, §2º? E há adesões informalmente combinadas com o Fornecedor Norte?

---

## Fechamento da coleta da Sessão 1 (resposta do cliente)

- **Item 9 — respondido** (v. acima): máquinas do Beta = bens de capital essenciais.
- **Fato novo do Norte** (não houve pergunta, informado pela diretoria): o Norte aceita seguir fornecendo **à vista**, mas exige um **"sinal"** sobre o atrasado, sob ameaça de cortar o suprimento. Posição do Controller: **recusado** (adendo da `sessao1/resposta_diretor.md`) — pagamento a concursal fora do plano é vedado em qualquer valor.
- **Demais itens (1–8, 10):** o cliente declarou **não ter informações adicionais**. Eles permanecem listados acima a título de registro; nos entregáveis, cada lacuna está tratada como **assunção destacada** ("ASSUNÇÃO"/"NÃO VERIFICADO") ou mantida em aberto nos `STATUS.md`. **Não serão repetidos como pergunta.**

## Novas perguntas para a Sessão 3 (decisões e dados, não repetição)

11. **(Decisão) Via para a União (R$ 2.700.000)**, após as opções apresentadas na Sessão 3: parcelamento simples (120×), parcelamento com prejuízo fiscal (30% + 84×) ou transação PGFN (até 70% de desconto). Preciso da escolha para qualificar a `passivo_fiscal_solucao.md`.
12. **(Decisão) Alienação do galpão (UPI R$ 4.500.000):** será por **via judicial**? Só a alienação judicial afasta a trava de 30% do ganho de capital conforme o texto da biblioteca (art. 6º-B).
13. **Taxa de desconto** para o valor presente das 120 parcelas (novação/CPC 48). Sem resposta, assumirei taxa nula (valores nominais) com rótulo de assunção — o ganho então fica no piso nominal de R$ 3.882.000.
14. **Data da homologação do plano** (quando ocorrer) e confirmação das cláusulas ajustadas após a Sessão 2 — base para os `lancamentos_novacao.json` da Sessão 3.
