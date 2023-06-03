#Escreva um programa que leia um inteiro N. Este N é o número de linhas de saída impressas por este programa.

n = int(input())
linha = 1
cont = 0

while cont < n:
    for l in range(0, 3):
        print(linha, end=' ')
        linha += 1

    print('PUM')
    linha += 1

    cont+= 1