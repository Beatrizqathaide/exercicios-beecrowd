#Leia uma matriz X[10]. Depois, substitua cada número nulo ou negativo de X por 1. Imprima todos os números armazenados na matriz X.

x = []
for c in range(0, 10):
    num = int(input())
    x.append(num)

    if num <= 0:
        x[c] = 1
    
    print(f'X[{c}] = {x[c]}')