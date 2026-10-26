# STATUS: COMPLETE WITH OPEN ITEMS

Entregáveis em `workspace/deliverable/` (atualizados na 2ª rodada, após respostas do cliente):

- `clausulas.json` — avaliação das 15 cláusulas da minuta (8 "alterar", 7 "aceitavel"; nenhuma marcada como abusiva sem base na biblioteca). Fundamentos exclusivamente citados de `library/INDEX.md`.
- `clausula_dados.md` — Cláusula 5 substitutiva completa (papéis LGPD; bases legais para dados de saúde — art. 11, II, "f" e §4º para faturamento TISS; instruções; subcontratação; transferência internacional; incidentes; término/portabilidade; auditoria; responsabilidade).
- `nota_socia.md` — resposta em linguagem simples, incluindo a correção da tese do foro (CDC não se aplica; foro interempresarial válido — CPC art. 63; teoria finalista) e aritmética das exposições.
- `PERGUNTAS.md` — perguntas opcionais/não bloqueantes (nenhuma era necessária para concluir; por isso não há `QUESTIONS.md`).
- `documents/minuta_contrato_nexa_texto.txt` — texto extraído do PDF (trabalho de apoio).

## Premissas declaradas

- Clínica Aurora é pessoa jurídica contratando software como insumo empresarial (ficha do cliente) → CDC não aplicável; contrato regido por CC/CPC conforme a biblioteca.
- Confirmado pelo cliente nesta rodada: NEXA usa AWS "provavelmente" nos EUA → endereçado no item 5.7 da cláusula de dados (revelação da região + mecanismo do art. 33 LGPD em 30 dias, ou migração para região no Brasil em ≤90 dias, sob pena de rescisão sem multa) e na AWS como subcontratada listada (item 5.6).
- Confirmado pelo cliente: migração de ~22.000 prontuários leva meses → fundamentos das Cláusulas 3, 7 e 10 reforçados (CC art. 473, parágrafo único: saída em prazo compatível com investimentos; transição de 180 dias na Cláusula 7).

## Itens em aberto (não bloqueiam os entregáveis; cobrados da NEXA na contraproposta)

1. Região exata de hospedagem/tratamento na AWS e de backups/suporte (a resposta "provavelmente" não basta).
2. Mecanismo do art. 33 LGPD hoje utilizado para a AWS, ou plano de migração para o Brasil (≤90 dias).
3. Lista completa de subcontratados da NEXA e certificações de segurança.
4. Interno Aurora: nomeação do encarregado (DPO), política de privacidade do site e histórico de incidentes — sem resposta do cliente até aqui; nada no parecer depende dessas informações.

Nada foi afirmado além da biblioteca fechada; pontos não cobertos por ela (ex.: sanções administrativas da ANPD em valores) foram omitidos ou marcados como não verificados.
