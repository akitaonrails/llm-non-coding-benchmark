

Sessão 2 já está entregue e validada — `deliverable/sessao2/analise_plano.md`, `efeito_tributario_desagio.json` (chaves exatamente conforme o schema do contrato) e `efeito_tributario_desagio_notas.md`. Segue o resultado:

## Minuta do plano, cláusula a cláusula

| Cláusula | Veredito | Por quê (biblioteca) |
|---|---|---|
| **Trabalhistas: integral em 18 meses** | **Ilegal como redigida** | Art. 54: plano **não pode prever prazo > 1 ano** para trabalhistas vencidos até o pedido; §2º admite até 2 anos só com as condições específicas (**garantias, aprovação da classe, integralidade**). A cláusula só cumpre a integralidade — falta garantia e aprovação da classe I. Corrigir: 12 meses, ou estruturar 24 meses com as condições do §2º |
| **Classes III+IV: deságio 60%, 120x, carência 24m** | **Legal** (com ressalvas) | Créditos concursais sujeitam-se ao plano (art. 49) e a biblioteca não traz limite de deságio/prazo entre concursais. Ressalvas: art. 50-A não vale para **pessoas ligadas** (parágrafo único — relação dos credores com controladores é desconhecida); vigência depende de assembleia (quóruns do art. 58 **não verificáveis** na biblioteca) |
| **Fiduciários "sujeitos ao plano, deságio 40%"** | **Ilegal/ineficaz** | Art. 49, §3º: proprietário fiduciário **não se submete** aos efeitos da RJ. O Banco Beta (R$ 3.100.000, CCB de máquinas) está **fora** — deságio imposto é inexequível sem adesão voluntária. Contrapartida boa para nós: na suspensão do art. 6º §4º é **vedada a retirada das máquinas essenciais**. Corrigir: suprimir e negociar acordo bilateral |
| **União: "no plano", deságio 50%, 180x** | **Ilegal — duas vezes** | CTN 187 + art. 68: crédito tributário **não se sujeita ao plano**; e 180x até excederia o parcelamento (120). Execução fiscal **não se suspende** (art. 6º §7º-B) — a cláusula "no papel" não protege contra penhora. Via correta: parcelamento/transação (Lei 10.522, 10-A a 10-C) → CND+ p/ art. 57/CTN 191-A (modelado na Sessão 3) |
| **Fonte: galpão (UPI) por R$ 4,5 mi** | **Legal com ressalvas** | Vender ativo para pagar o plano é lícito; trava de 30% não alcança ganho em alienação judicial (art. 6º-B). Mas regime da UPI (60-A) e valor contábil do galpão: **não verificado/desconhecido** — ganho da venda não calculável ainda |
| **Omissões** | **Pendências** | Falta prever **CND+** (sem ela não há concessão — art. 57; CTN 191-A), quóruns de assembleia, tratamento de extraconcursais (art. 67) e honorários do AJ |

## Efeito tributário do deságio (`efeito_tributario_desagio.json`)

```
ganho_desagio        = 3.882.000   = (4.200.000 Alfa + 1.850.000 Norte + 420.000 Sul) × 0,60
pis_cofins_sobre_ganho = 0          (art. 50-A, I — fora da base)
trava_30_aplicavel   = false        (art. 50-A, II — o ganho da redução não esbarra na trava)
prejuizo_fiscal / compensacao / base_irpj_csll / irpj_csll = null
```

- A base inclui **somente** classes III+IV: o deságio do fiduciário (40%) e o da União (50%) são cláusulas ilegais — não geram ganho registrável (hipotéticos: +1.240.000 e +1.350.000, excluídos); trabalhistas são integrais (ganho zero sobre o principal) e os 310.000 do Norte são pós-pedido.
- Os quatro campos `null` são o saldo de **prejuízo fiscal e seus desdobramentos** — o cliente declarou não ter a informação; não inventei número. Cenários com fórmula nas notas: **PF ≥ 3.882.000 → base 0, imposto 0**; PF = 0 → base 3.882.000 e ~R$ 1,32 mi de IRPJ/CSLL a ~34% (alíquotas **não verificadas** na biblioteca). Atenção registrada: suposta restrição legislativa pós-2024 à compensação **não consta da biblioteca** — validar antes de contar com o offset pleno.
- Divergência contábil: pelo CPC 48 o ganho é a valor **presente** (120x com carência de 24m ⇒ ganho contábil > 3.882.000); taxa do plano não informada — o número acima é o ganho nominal, base defensável para o fiscal.

Nada a re-perguntar ao cliente: os únicos insumos faltantes (PF, taxa, pessoas ligadas, valor contábil do galpão) já estão marcados como desconhecidos permanentes em `QUESTIONS.md`, com a fonte documental de cada um.