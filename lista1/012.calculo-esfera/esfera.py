#Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio (R). A fórmula para calcular o volume é: (4/3) * pi * R3. Considere (atribua) para pi o valor 3,14159.

#Dica: Use (4/3.0) ou (4.0/3) em sua fórmula, pois algumas linguagens (incluindo C++) assumem que o resultado da divisão entre dois inteiros é outro inteiro. :)

r = float(input('Raio: '))
pi = 3.14159
volume = (4 / 3.0) * pi * r ** 3

print(f'VOLUME = {volume:.3f}')