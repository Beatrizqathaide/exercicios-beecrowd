'''
Dados dois inteiros, n e m, quantos dígitos têm n m ?

Exemplos:

2 e 10 - 2 10 = 1024 - 4 dígitos

3 e 9 - 39 = 19683 - 5 dígitos

Entrada
A entrada é composta por vários casos de teste. A primeira linha tem um inteiro C, representando o número de casos de teste. As seguintes linhas C contêm dois inteiros N e M (1 <= N, M <= 100).

Saída
Para cada caso de teste de entrada do seu programa, você deve imprimir um inteiro contendo a quantidade de dígitos do resultado da potência calculada no respectivo caso de teste.
'''

c = int(input())

for i in range(0, c):
    n, m = map(int, input().split())

    potencia = n
    for p in range(1, m):
        potencia *= n

    potencia = str(potencia)
    print(len(potencia))