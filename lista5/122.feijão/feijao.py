'''
Conta-se nos arredores de Montes Claros que, há muito tempo no mercado municipal, Sebastião e seus companheiros de trabalho sempre jogam um jogo de adivinhação após a entrega dos produtos agrícolas colhidos na semana que aconteceu. O jogo "Adivinhe onde está o feijão" consiste em esconder um grão de feijão em um dos quatro copos opacos e, após embaralhá-los, o apostador deve adivinhar em qual copo está o vegetal.



Este ano, devido ao grande sucesso cultural e histórico e à enorme quantidade de pessoas que praticam este jogo no mercado municipal, a Câmara Municipal decidiu realizar um campeonato "Adivinha Onde Está o Feijão". No entanto, ela precisa de um programa para mostrar aos espectadores onde estavam os feijões após o final de um jogo. Sabendo que a próxima Maratona de Programação acontecerá na cidade, ela logo encomendou uma solução aos excelentes programadores. Dessa forma, você deve auxiliar a organização nessa missão com um programa que informará, ao final de uma partida, onde estava o feijão.

Entrada
A entrada conterá apenas uma linha com quatro números inteiros, C1, C2, C3 e C4 separados por um espaço. O valor Ci = 1 indica que o feijão estava no copo número i, e Ci = 0 indica que o copo i estava vazio ao final do jogo. Sempre haverá exatamente um copo com o feijão.

Saída
Escreva na saída uma linha contendo um inteiro entre 1 e 4, correspondente à posição onde estavam os feijões.
'''

c1, c2, c3, c4 = map(int, input().split())

l = [c1, c2, c3, c4]
for c in range(0, len(l)):
    if l[c] == 1:
        print(c + 1)