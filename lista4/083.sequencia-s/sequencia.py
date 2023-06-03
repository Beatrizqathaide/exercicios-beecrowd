'''
Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado por:
S = 1 + 1/2 + 1/3 + … + 1/100
'''

s = 1
for c in range(2, 101):
    s += 1 / c

print(f'{s:.2f}')
