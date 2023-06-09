'''
A degustação cega de chá é a habilidade de identificar um chá usando apenas seus sentidos de olfato e paladar.

Como parte do Desafio Ideal dos Consumidores de Chá Puro (ICPC), é organizado um programa de TV local. Durante o show, um bule cheio é preparado e cinco competidores recebem uma xícara de chá cada. Os participantes devem cheirar, provar e avaliar a amostra para identificar o tipo de chá, que pode ser: (1) chá branco; (2) chá verde; (3) chá preto; ou (4) chá de ervas. No final, as respostas são verificadas para determinar o número de palpites corretos.

Dado o tipo de chá real e as respostas fornecidas, determine o número de competidores que obtiveram a resposta correta.

Entrada
A primeira linha contém um inteiro T representando o tipo de chá (1 ≤ T ≤ 4). A segunda linha contém cinco inteiros A, B, C, D e E, indicando a resposta dada por cada competidor (1 ≤ A, B, C, D, E ≤ 4).

Saída
Imprima uma linha com um número inteiro representando o número de competidores que obtiveram a resposta correta.
'''

t = int(input())

a, b, c, d, e = map(int, input().split())

cont = 0

if a == t:
    cont += 1
if b == t:
    cont += 1 
if c == t:
    cont += 1
if d == t:
    cont += 1
if e == t:
    cont += 1

print(cont)