#Leia um inteiro N e calcule todos os seus divisores.

n = int(input())

for c in range(1, n + 1):
    if n % c == 0:
        print(c)