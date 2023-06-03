#Leia um número e faça um programa que coloque esse número na primeira posição de um array N[10]. Em cada posição subsequente, coloque o dobro da posição anterior. Por exemplo, se o número de entrada for 1, os números da matriz devem ser 1,2,4,8 e assim por diante.

n = int(input())

for c in range(0, 10):
    if c == 0:
        print(f'N[{c}] = {n}')
    else:
        n = n * 2
        print(f'N[{c}] = {n}')
