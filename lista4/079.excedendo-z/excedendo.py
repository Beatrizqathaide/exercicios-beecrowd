'''
Escreva um programa que leia dois inteiros: X e Z (Z deve ser lido quantas vezes forem necessárias, até que um número maior que X seja lido). Conte quantos inteiros devem ser somados em sequência (começando em e incluindo X) para que a soma exceda Z o mínimo possível e escreva esse número.

A entrada pode ter, por exemplo, os números 21 21 15 30. Neste caso, o número 21 é assumido para X, Os números 21 e 15 devem ser ignorados por serem menores ou iguais a X. O número 30 é dentro da especificação (maior que X) e é válido. Portanto, o resultado final deve ser 2 para este caso de teste, pois a soma (21 + 22) é maior que 30.
'''

x = int(input())
temp = x
z = 0
cont = 0

while True:
    while x >= z:
        z = int(input())

    if z > x:
        x = x + (temp + 1)
    cont += 1

    if x > z:
        break

print(cont)