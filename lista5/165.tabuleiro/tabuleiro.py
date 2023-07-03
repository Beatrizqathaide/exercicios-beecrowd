'''
Keanu estava testando novos modelos de tabuleiro de xadrez quando teve a seguinte dúvida:
Quantos quadrados brancos e quantos quadrados pretos tem um tabuleiro de xadrez de tamanho n x n ? 

tabuleiro de xadrez tamanho 3x3: 5 quadrados brancos e 4 quadrados pretos

tabuleiro de xadrez tamanho 4x4: 8 quadrados brancos e 8 quadrados pretos

Observe que o quadrado superior e mais à esquerda é sempre branco.

Entrada
A entrada consiste em uma linha com um único inteiro n .

2≤ n ≤ 100

Saída
Imprima " a quadrados brancos e b quadrados pretos" sem aspas, onde a é o número de quadrados brancos e b o número de quadrados pretos.
'''

from math import ceil

numero = int(input())

qtdade = numero * numero

if qtdade % 2 == 0:
    quadradoa = int(qtdade / 2)
    quadradob = int(qtdade / 2)

else:
    quadradoa = ceil((qtdade / 2))
    quadradob = ceil((qtdade / 2) - 1)

print(f'{quadradoa} casas brancas e {quadradob} casas pretas')