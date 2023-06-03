#Escreva um programa que leia um inteiro N (1 < N < 1000). Este N é o número de linhas de saída impressas por este programa.

n = int(input())
cont = 1

while cont <= n:
    print(f'{cont} {cont * cont} {cont * cont * cont}')

    cont += 1