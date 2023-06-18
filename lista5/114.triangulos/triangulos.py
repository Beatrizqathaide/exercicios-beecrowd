'''
Dados três valores, descubra se eles formam um triângulo. Se sim, verifique se o triângulo é escaleno, isóceles ou equilátero e se é um triângulo retângulo ou não.

Entrada
A entrada é dada por três inteiros A,B e C (0 < A,B,C < 105).

Saída
A saída deve ser uma única linha contendo a string "Invalido" se os valores de entrada não representarem um triângulo.

Se os valores puderem ser os lados de um triângulo a saída deve ser "Valido-Equilatero" se tal triângulo for equilátero, "Valido-Escaleno" se for escaleno ou "Valido-Isoceles" se for isóceles. A próxima linha de saída deve ser "Retangulo: S" se o triângulo for retângulo ou "Retangulo: N" caso contrário, conforme mostrado nos exemplos.
'''

a, b, c = map(int, input().split())

if a < b + c and b < a + c and c < a + b:
    if a == b and a == c:
        print('Valido-Equilatero')
    elif a == b or a == c or b ==c:
        print('Valido-Isoceles')
    else:
        print('Valido-Escaleno')

    if a * a + b * b == c * c or b * b + c * c == a * a or c * c + a * a == b * b:
        print('Retangulo: S')
    else:
        print('Retangulo: N')

else:
    print('Invalido')
