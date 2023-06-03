#Escreva um programa que leia 6 números. Esses números serão apenas positivos ou negativos (desconsidere valores nulos). Imprima o número total de números positivos.

positivos = 0

for c in range(0, 6):
    num = float(input())
    if num > 0:
        positivos += 1

print(f'{positivos} valores positivos')