# Leia dois valores inteiros X e Y. Imprima a soma de todos os valores ímpares entre eles.

x = int(input())
y = int(input())

soma = 0

for c in range(y + 1, x):
    if c % 2 != 0:
        soma += c

print(soma)