#Leia um inteiro N que é o número de casos de teste. Cada caso de teste é uma linha contendo dois números inteiros X e Y.

n = int(input())
soma = 0
cont = 0
temp = 0

while cont < n:
    x, y = map(int, input().split())

    if y < x:
        temp = y
        y = x
        x = temp
  
    for c in range(x + 1, y):
        if c % 2 != 0:
            soma += c
    
    print(soma)
    cont += 1
    soma = 0
