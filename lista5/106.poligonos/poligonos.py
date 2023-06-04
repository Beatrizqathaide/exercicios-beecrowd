'''
Na geometria euclidiana, um polígono regular é um polígono equiangular (todos os ângulos são iguais em medida) e equilátero (todos os lados têm o mesmo comprimento). Um polígono simples é aquele que não se intercepta em nenhum lugar. Abaixo podemos ver vários mosaicos feitos de polígonos regulares.

Você deve escrever um programa que, dado o número e o comprimento dos lados de um polígono regular, mostre seu perímetro.

Entrada
A entrada são dois inteiros positivos: N e L, que são, respectivamente, o número de lados e o comprimento de cada lado de um polígono regular (3 ≤ N ≤ 1000000 e 1 ≤ L ≤ 4000).

Saída
A saída é o perímetro P do polígono regular em uma única linha.
'''

n, l = map(int, input().split())

p = n*l

print(p)