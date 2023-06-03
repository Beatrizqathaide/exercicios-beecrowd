#Escreva um programa que leia dois números inteiros X e Y e calcule a soma de todos os números não divisíveis por 13 entre eles, incluindo ambos.

x = int(input())
y = int(input())

if y < x:
    temp = x
    x = y
    y = temp


soma = 0
for n in range(x, y + 1):
    if n % 13 != 0:
        soma += n

print(soma)
