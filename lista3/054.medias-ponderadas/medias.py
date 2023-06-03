#Leia um inteiro N, que representa o número de casos de teste a seguir. Cada caso de teste consiste em três números de ponto flutuante, cada um com um dígito após o ponto decimal. Imprima a média ponderada para cada um desses conjuntos de três números, considerando que o primeiro número tem peso 2, o segundo número tem peso 3 e o terceiro número tem peso 5.

n = int(input())

for c in range(0, n):
    a, b, c = map(float, input().split())

    media = ((a * 2) + (b * 3) + (c * 5)) / 10

    print(f'{media:.1f}')