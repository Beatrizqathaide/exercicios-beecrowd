#Escreva um programa que leia dois números X e Y (X < Y). Depois disso, mostre uma sequência de 1 a y, passando para a próxima linha a cada X números.

x, y = input().split()

x = int(x)
y = int(y)

cont = 1

for num in range(1, y + 1):
    if cont == x:
        print(num)
        cont = 1
    else:
        print(num, end=' ')
        cont += 1