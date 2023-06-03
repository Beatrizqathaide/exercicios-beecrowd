#Faça um programa que leia três valores de ponto flutuante: A, B e C. Em seguida, calcule e mostre:
#a) a área do triângulo retângulo que tem base A e altura C.
#b) a área do círculo do raio C. (pi = 3,14159)
#c) a área do trapézio que tem A e B por base e C por altura.
#d) a área do quadrado que tem lado B.
#e) a área do retângulo que tem lados A e B.

a, b, c = input().split(' ') #captura a entrada

#tranforma no formato desejado
a = float(a)
b = float(b)
c = float(c)

triangulo = (a * c) / 2
circulo = 3.14159 * c ** 2
trapezio = ((a + b) * c) / 2
quadrado = b * b
retangulo = a * b

print(f'TRIANGULO = {triangulo:.3f}')
print(f'CIRCULO = {circulo:.3f}')
print(f'TRAPEZIO = {trapezio:.3f}')
print(f'QUADRADO = {quadrado:.3f}')
print(f'RETANGULO = {retangulo:.3f}')