'''Leia 3 números duplos (A, B e C) representando os lados de um triângulo e organize-os em ordem decrescente, de modo que o lado A seja o maior dos três lados. Em seguida, determine o tipo de triângulo que eles podem fazer, com base nos seguintes casos sempre escrevendo uma mensagem apropriada:
se A ≥ B + C, escreva a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, escreva a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, escreva a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, escreva a mensagem: TRIANGULO ACUTANGULO
se os três lados forem do mesmo tamanho, escreva a mensagem: TRIANGULO EQUILATERO
se apenas dois lados forem iguais e o terceiro for diferente, escreva a mensagem: TRIANGULO ISOSCELES'''

x, y, z = input().split(' ')

x = float(x)
y = float(y)
z = float(z)

if x >= y and x >= z:
    a = x
    b = y
    c = z
if y >= x and y >= z:
    a = y
    b = x
    c = z
if z >= x and z >= y:
    a = z
    b = x
    c = y


if a >= b + c:
    print('NÃO FORMA TRIANGULO')
elif a * a == (b * b) + (c * c):
    print('TRIANGULO RETANGULO')
elif a * a > (b * b) + (c * c):
    print('TRIANGULO OBTUSANGULO')
elif a * a < (b * b) + (c * c):
    print('TRIANGULO ACUTANGULO')
if a == b and a == c:
    print('TRIANGULO EQUILATERO')
elif a == b or b == c or a == c:
    print('TRIANGULO ISOSCELES')

