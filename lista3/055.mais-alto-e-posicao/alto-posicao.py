#Leia 100 números inteiros. Imprima o valor de leitura mais alto e a posição de entrada.

maior = 0
for c in range(1, 101):
    num = int(input())

    if num > maior:
        maior = num
        posicao = c


print(maior)
print(posicao)