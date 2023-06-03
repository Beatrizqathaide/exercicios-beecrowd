'''
Em um país imaginário chamado Lisarb, todas as pessoas ficam muito felizes em pagar seus impostos porque sabem que não existem políticos corruptos e os impostos são usados ​​para beneficiar a população, sem nenhum desvio. A moeda deste país é o Rombus, cujo símbolo é R$.

Leia um valor com 2 dígitos após a vírgula, equivalente ao salário de um habitante do Lisarb. Em seguida, imprima o valor devido que essa pessoa deve pagar de impostos, conforme tabela abaixo.

Lembre-se, se o salário for R$ 3.002,00 por exemplo, a alíquota de 8% é apenas acima de R$ 1.000,00, pois o salário de R$ 0,00 a R$ 2.000,00 é isento de impostos. No exemplo a seguir, a taxa total é de 8% acima de R$ 1.000,00 + 18% acima de R$ 2,00, resultando em R$ 80,36 ao todo. A resposta deve ser impressa com 2 dígitos após o ponto decimal.
'''

salario = float(input())
imposto = 0.00

if salario > 4500.00:
    imposto += (salario - 4500.00) * 0.28 # vai calcular o q passar de 4500
    salario -= (salario - 4500) #retira o valor q foi calculado o imposto

if salario > 3000.00:
    imposto += (salario - 3000.00) * 0.18 # vai calcular o valor q está entre 3000 e 4500
    salario -= (salario - 3000.00)

if salario > 2000.00:
    imposto += (salario - 2000.00) * 0.08 # vai calcular o valor q está entre 2000 e 3000

if imposto == 0.00:
    print('Isento')
else:
    print(f'R$ {imposto:.2f}')