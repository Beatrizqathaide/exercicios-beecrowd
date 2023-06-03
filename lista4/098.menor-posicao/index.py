'''
Escreva um programa que leia um número N. Este N é o tamanho de um array X[N]. Em seguida, leia cada um dos números de X, encontre o menor elemento deste array e sua posição dentro do array, imprimindo esta informação.
'''

n = int(input())

lista = list(map(int, input().split()))

menor = lista[0]
posicao = 0

for i in range(0, len(lista)):
    
    if lista[i] < menor:
        menor = lista[i]
        posicao = i

print(f'Menor valor: {menor}')
print(f'Posicao: {posicao}')

