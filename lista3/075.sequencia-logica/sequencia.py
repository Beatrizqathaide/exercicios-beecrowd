#Escreva um programa que leia um inteiro N. N * 2 linhas devem ser impressas por este programa de acordo com o exemplo abaixo. Para números com mais de 6 dígitos, todos os dígitos devem ser impressos (não é permitida notação científica).

n = int(input())
cont = 1

while cont <= n:
    print(f'{cont} {cont * cont} {cont * cont * cont}')
    print(f'{cont} {cont * cont + 1} {cont * cont * cont + 1}')

    cont += 1