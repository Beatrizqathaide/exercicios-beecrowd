'''
A organização OIBR, a Olimpíada Internacional de Basquete Robô, começa a ter problemas com duas equipes: os Bit Warriors e os Byte Bulls. É que os robôs dessas equipes acertam quase todos os arremessos de qualquer posição na quadra! Pensando bem, o jogo de basquete seria estranho se os jogadores pudessem acertar qualquer arremesso, certo? Uma das medidas que a OIBR está implementando é uma nova pontuação para os lançamentos, de acordo com a distância do robô até o início da quadra. A quadra tem 2.000 centímetros de comprimento, conforme a figura.

Dada a distância D do robô até o início da quadra, onde está a cesta, a regra é a seguinte:

• Se D ≤ 800, a cesta vale 1 ponto;

• Se 800 < D ≤ 1400, a cesta vale 2 pontos;

• Se 1400 < D ≤ 2000, a cesta vale 3 pontos. A organização do OIBR precisa de ajuda para automatizar o placar do jogo. Dado o valor da distância D, você deve escrever um programa para calcular o número de pontos de lançamento.

Entrada
A primeira e única linha da entrada contém um inteiro D (0 ≤ D ≤ 2000) indicando a distância dos robôs até o início do bloco, em centímetros, no lançamento.

Saída
Seu programa deve produzir uma única linha, contendo um inteiro, 1, 2 ou 3, indicando a temporada de lançamento.
'''

d = int(input())

if d <= 800:
    print('1')
elif d <= 1400:
    print('2')
elif d <= 2000:
    print('3')