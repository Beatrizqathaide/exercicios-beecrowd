#Leia um inteiro N. Imprima o quadrado de cada um dos valores pares de 1 a N incluindo N se for o caso.

n = int(input())

for c in range(1, n + 1):
    if c % 2 == 0:
        print(f'{c}^2 = {c * c}')