'''
Leia um inteiro N que é o número de casos de teste a seguir. Cada caso de teste contém dois inteiros X e Y. Imprima uma linha de saída para cada caso de teste que é a soma de Y números ímpares de X incluindo-o se for o caso. Por exemplo:
para a entrada 4 5, a saída deve ser 45, ou seja: 5 + 7 + 9 + 11 + 13
para a entrada 7 4, a saída deve ser 40, ou seja: 7 + 9 + 11 + 13
'''

n = int(input())

contLaço = 0
while contLaço < n:
    x, y = input().split()

    x = int(x)
    y = int(y)

    if x % 2 == 0:
        x = x + 1

    aux = x
    cont = 1

    while cont < y:
        x = x + (aux + 2)
        cont += 1
        aux += 2

    print(x)
    
    contLaço += 1

