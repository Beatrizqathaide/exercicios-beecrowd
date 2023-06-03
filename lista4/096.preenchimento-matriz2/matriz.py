#Escreva um programa que leia um número T e preencha um vetor N[1000] com os números de 0 a T-1 repetidas vezes, como no exemplo abaixo.

t = int(input())
num = 0

for c in range(0, 1000):
    print(f'N[{c}] = {num}')
    num += 1
    
    if num == t - 0:
        num = 0