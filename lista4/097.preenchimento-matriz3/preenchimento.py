#Leia um número X. Coloque este X na primeira posição de uma matriz N [100]. Em cada posição subsequente (1 a 99) coloque metade do número inserido na posição anterior, conforme exemplo abaixo. Imprima todo o vetor N.

matriz = []

x = float(input())

matriz.append(x)

for i in range(0, 100):
    
    x = x / 2
    matriz.append(x)
    print(f'N[{i}] = {matriz[i]:.4f}')