'''Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado por:
S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?'''

s = 1
aux = 2

for c in range(3, 40, 2):
    s += c / aux
    aux *= 2

print(f'{s:.2f}')