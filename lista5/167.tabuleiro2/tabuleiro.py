'''
No tabuleiro de xadrez, a casa do tabuleiro na linha 1, coluna 1 (canto superior esquerdo) é sempre branca e as cores das casas se alternam entre o branco e o preto, segundo o padrão conhecido como ... xadrez! Desta forma, como o tabuleiro tradicional tem oito linhas e oito colunas, a casa da linha 8, coluna 8 (canto inferior direito) também será branca. Neste problema, porém, queremos saber a cor do quadrado do tabuleiro no canto inferior direito de uma bandeja com quaisquer dimensões: L linhas e C colunas. No exemplo da figura, para L = 6 e C = 9, o quadrado do tabuleiro no canto inferior direito será preto!

Entrada
A primeira linha da entrada contém um inteiro L (1 ≤ L ≤ 1000) indicando o número de linhas no tabuleiro de xadrez. A segunda linha da entrada contém um inteiro C (1 ≤ C ≤ 1000) representando o número de colunas.

Saída
Imprima uma linha na saída. A linha deve conter um número inteiro, representando a cor da casa no canto inferior direito do tabuleiro: 1, se for branca; e 0, se for preto.
'''

linha = int(input())
coluna = int(input())

cor = linha + coluna

if cor % 2 == 0:
    print('1')

else:
    print('0')