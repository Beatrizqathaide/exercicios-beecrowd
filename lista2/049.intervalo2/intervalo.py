'''
Leia um inteiro N. Este N será o número de números inteiros X que serão lidos.

Imprima quantos desses números X estão no intervalo [10,20] e quantos valores estão fora desse intervalo.
'''

n = int(input())
dentro = 0
fora = 0

for c in range(0, n):
    x = int(input())
    if x >= 10 and x <= 20:
        dentro += 1
    else:
        fora += 1

print(f'{dentro} in')
print(f'{fora} out')
