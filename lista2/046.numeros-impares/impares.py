#Leia um valor inteiro X (1 <= X <= 1000). Em seguida, imprima os números ímpares de 1 a X, cada um em uma linha, incluindo X se for o caso.

num = int(input())

for n in range(1, num + 1):
    if n % 2 != 0:
        print(n)
