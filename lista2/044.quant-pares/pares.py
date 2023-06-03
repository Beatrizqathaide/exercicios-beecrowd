#Faça um programa que leia cinco valores inteiros. Conte quantos desses valores são pares e imprima essas informações.

pares = 0

for n in range(0, 5):
    num = int(input())
    if num % 2 == 0:
        pares += 1

print(f'{pares} valores pares')