'''
System of a Download é uma famosa banda de Hacker Metal! Certa vez, eles criaram um aparelho, com seis botões, numerados de 0 a 5, e colocaram naquele aparelho seus 11 maiores sucessos. Para reproduzir uma dessas músicas, você deve pressionar dois botões. Com isso, os números desses dois botões são adicionados e, em seguida, a música correspondente é tocada. Número da soma, conforme relação abaixo:

0 - PROXICIDADE
1 - P.Y.N.G.
2 - DNSUEY!
3 - SERVIDORES
4 - HOSPEDAGEM!
5 - CRIPTONIZAR
6 - DIA OFFLINE
7 - SAL
8 - RESPONDA!
9 - RAR?
10 - ANTENAS WIFI

Por exemplo, se os botões pressionados forem 3 e 4, tocará a música 7 - SALT

Escreva um programa que, dados os dois botões pressionados, determine qual música será tocada.

Entrada
Será informado um inteiro C, que será o número de casos de teste. Cada caso tem dois valores inteiros, X e Y, representando quais botões foram pressionados.

Saída
Para cada caso de teste, imprima o nome da música correspondente.
Mais sobre o texto original
'''
c = int(input())

lista = ['PROXYCITY', 'P.Y.N.G.', 'DNSUEY!', 'SERVERS', 'HOST!', 'CRIPTONIZE', 'OFFLINE DAY', 'SALT', 'ANSWER!', 'RAR?', 'WIFI ANTENNAS']

for i in range(0, c):
    x, y = map(int, input().split())

    r = x + y

    for k in range(0, len(lista)):
        if r == k:
            print(lista[k])