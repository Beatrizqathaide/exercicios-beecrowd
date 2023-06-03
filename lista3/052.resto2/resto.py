#Leia um inteiro N. Imprima todos os números entre 1 e 10.000, que dividido por N dará o resto = 2.

n = int(input())

for c in range(1, 10000 + 1):
    if c % n == 2:
        print(c)