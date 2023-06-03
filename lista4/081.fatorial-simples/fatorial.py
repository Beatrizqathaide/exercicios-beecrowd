#Leia um valor N. Calcule e escreva seu fatorial correspondente. Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.

n = int(input())
aux = n
cont = 1
diferenca = aux

while diferenca != 1:
    diferenca = aux - cont
    n *= diferenca
    cont += 1 

print(n)