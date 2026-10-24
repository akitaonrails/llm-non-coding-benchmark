I’ll audit the figures against the XMLs, check each legal statement against the indexed library, and resolve any wording that treats a simulated exposure as an established amount due. I’ll update the files before reporting the changes.

The arithmetic and cited file links check out. I found one presentation issue: the JSON’s `recolhimento_devido` value could read as a confirmed bill, although the credits are provisional and the supplied XMLs are from homologation. I’m making that conditional reading explicit and adding the unreduced amount as a sensitivity check.

Revisei os 17 XMLs, refiz as somas em Python e conferi todas as citações com `library/INDEX.md`. **Os cálculos fecham:** saídas de R$ 480.000,00, débitos de R$ 4.800,00, créditos de teste de R$ 1.620,00 e saldo de R$ 3.180,00.

Corrigi a apresentação desse saldo em [apuracao_teste.json](/work/workspace/deliverable/apuracao_teste.json) e [orientacao.md](/work/workspace/deliverable/orientacao.md): **R$ 3.180,00 é exposição condicional, não débito exigível confirmado**. Os créditos dependem de regularização documental; sem aproveitá-los, o cálculo seria R$ 4.800,00, sem que isso afirme sua glosa. Também esclareci que a biblioteca não diz que a falta isolada de `IBSCBSTot` causa rejeição.

Mantive em [STATUS.md](/work/workspace/deliverable/STATUS.md) o ponto que não reconcilia: Paulo relata autorização em produção após duas rejeições, mas os arquivos recebidos são fictícios, de homologação, e não incluem os protocolos de produção.