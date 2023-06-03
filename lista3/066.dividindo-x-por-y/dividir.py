#Escreva um programa que leia dois números X e Y e imprima o resultado da divisão de X por Y. Caso não seja possível, imprima a mensagem "divisão impossivel".

n = int(input())

for n in range(0, n):
    
    x, y = input().split()
    x = int(x)
    y = int(y)

    if y == 0:
        print('divisao impossivel')
    else:
        resultado = float(x / y)
        print(resultado)