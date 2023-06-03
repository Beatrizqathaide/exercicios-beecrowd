#Escreva um programa que leia dois números inteiros X e Y. Imprima todos os números entre X e Y que dividindo por 5 o resto é igual a 2 ou igual a 3.

x = int(input())
y = int(input())

if y < x:
    temp = x
    x = y
    y = temp

for n in range(x + 1, y):
    if n % 5 == 2 or n % 5 == 3:
        print(n)
