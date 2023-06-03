
#Leia os quatro valores correspondentes aos eixos x e y de dois pontosLeia os quatro valores correspondentes aos eixos x e y de dois pontos no plano, p1 (x1, y1) e p2 (x2, y2) e calcule a distância entre eles , mostrando quatro casas decimais após a vírgula, de acordo com a fórmula:

from math import sqrt
import math
x1, y1 = input("Valor: ").split(' ')
x1 = float(x1)
y1 = float(y1)

x2, y2 = input("Valor: ").split(' ')
x2 = float(x2)
y2 = float(y2)

distancia = sqrt(((x2 - x1) ** 2 + (y2 - y1) ** 2))

print(f'{distancia:.4f}')