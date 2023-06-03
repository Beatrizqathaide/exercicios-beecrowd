'''Leia os valores flutuantes de três pontos (A, B e C) e verifique se é possível fazer um triângulo com eles. Se for possível, calcule o perímetro do triângulo e imprima a mensagem:

Perímetro = XX.X

Caso não seja possível, calcule a área do trapézio que tem como base A e B e C como altura, e imprima a mensagem:

Área = XX.X'''

a, b, c = input().split(' ')

a = float(a)
b = float(b)
c = float(c)


if (b + c > a) and (c + a > b) and (a + b > c):
        perimetro = a + b + c
        print(f'Perimetro = {perimetro:.1f}')
else:
    area = (a + b) * c / 2
    print(f'Area = {area:.1f}')