#Leia 3 números de ponto flutuante. Depois, imprima as raízes da fórmula de bhaskara. Se for impossível calcular as raízes por divisão por zero ou raiz quadrada de um número negativo, apresenta a mensagem “Impossivel calcular”

from math import sqrt
a, b, c = input().split(' ')

a = float(a)
b = float(b)
c = float(c)

delta = (b) ** 2 - 4 * a *c

if a == 0 or b == 0 or c == 0 or delta < 0:
    print('Impossivel calcular')

else:
    r1 = (- (b) + sqrt(delta)) / (2 * a)
    r2 = (- (b) - sqrt(delta)) / (2 * a)
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')
