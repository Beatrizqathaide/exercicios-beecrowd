#A seguinte sequência de números 0 1 1 2 3 5 8 13 21 ... é conhecida como a sequência de Fibonacci. A partir daí, cada número após os 2 primeiros é igual à soma dos dois números anteriores. Escreva um algoritmo que leia um inteiro N (N < 46) e imprima os primeiros N números dessa sequência.

n = int(input())

t1 = 0
t2 = 1

print(t1, end=' ')
print(t2, end=' ')

cont = 2

while cont < n:
    t3 = t1 + t2
    if cont == n - 1:
        print(t3, end='\n')

    else:
        print(t3, end=' ')

    t1 = t2
    t2 = t3

    cont += 1