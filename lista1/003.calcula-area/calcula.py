#A fórmula para calcular a área de uma circunferência é definida como A = π . R2. Considerando para este problema que π = 3,14159:
#Calcule a área usando a fórmula dada na descrição do problema.

r = float(input('Digite o raio: '))
a = 3.14159 * (r ** 2)

print(f'A={a:.4f}')