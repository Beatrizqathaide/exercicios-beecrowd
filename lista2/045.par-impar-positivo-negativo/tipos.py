# Faça um programa que leia cinco valores inteiros. Conte quantos desses valores são pares, ímpares, positivos e negativos. Imprima essas informações.

pares = 0
impares = 0
positivos = 0
negativos = 0

for n in range(0, 5):
    num = int(input())

    if num % 2 == 0:
        pares += 1
    
    if num % 2 != 0:
        impares += 1
    
    if num > 0:
        positivos += 1
    
    if num < 0:
        negativos += 1

print(f'{pares} valor(es) par(es)')
print(f'{impares} valor(es) impar(es)')
print(f'{positivos} valor(es) positivo(s)')
print(f'{negativos} valor(es) negativo(s)')