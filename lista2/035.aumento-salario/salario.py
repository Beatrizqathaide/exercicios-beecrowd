'''
A empresa ABC decidiu dar um aumento salarial aos seus funcionários, conforme tabela a seguir:

Salário                      Taxa de reajuste salarial
0 - 400,00                           15%
400,01 - 800,00                      12%
800,01 - 1200,00                     10%
1200,01 - 2000,00                    7% 
Acima de 2.000,00                    4%

Leia o salário do funcionário, calcule e imprima o salário do novo funcionário, bem como o dinheiro ganho e o percentual de aumento obtido pelo funcionário, com mensagens correspondentes em português, conforme exemplo abaixo.
'''

salario = float(input())

if salario > 0 and salario <= 400:
    percentual = 15
    novoSalario = salario + (salario / 100 * percentual)
    reajuste = salario / 100 * percentual

elif salario >= 400.01 and salario <= 800:
    percentual = 12
    novoSalario = salario + (salario / 100 * percentual)
    reajuste = salario / 100 * percentual

elif salario >= 800.01 and salario <= 1200:
    percentual = 10
    novoSalario = salario + (salario / 100 * percentual)
    reajuste = salario / 100 * percentual

elif salario >= 1200.01 and salario <= 2000:
    percentual = 7
    novoSalario = salario + (salario / 100 * percentual)
    reajuste = salario / 100 * percentual

else:
    percentual = 4
    novoSalario = salario + (salario / 100 * percentual)
    reajuste = salario / 100 * percentual

print(f'Novo salario: {novoSalario:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {percentual} %')