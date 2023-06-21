'''
Amelia ama o natal, e sua parte favorita nessa data é montar a árvore de natal! Ela adora decorar a árvore com bolinhas e luzes coloridas, para que fique bem alegre e divertida! No entanto, Amélia gosta das coisas bem distribuídas e exige que a sua árvore não tenha mais de metade dos ramos em bolas. Então, se a sua árvore de Natal tiver G ramos, ela precisa de G /2 bolinhas. Se o número G de ramos for ímpar, esse valor será arredondado para baixo.

Este ano, a Amélia decidiu renovar a sua árvore e vai comprar uma nova. Além disso, algumas de suas bolas quebraram e ela precisará saber quantas bolas novas precisará comprar para manter sua árvore equilibrada do jeito que ela gosta!

Para isso, ela quer sua ajuda! Dado o número de bolas que Amelia tem e o número de galhos que sua nova árvore terá, diga a Amelia quantas bolas de Natal ela precisa comprar para decorar sua nova árvore!

Entrada
A entrada é constituída por dois valores inteiros, lidos em duas linhas, B (1 < B < 10 3 ) e G  (100 < G  < 1000) indicando, respetivamente, o número de bolas que Amélia já possui e o número de ramos da sua nova árvore de natal.

Saída
Imprima o número de bolas que Amélia precisa comprar para completar sua árvore, com a mensagem "Faltam B bolinha(s)" (em inglês, Missing B ball(s)), onde B é o número de bolas que Amélia precisa comprar. Se Amelia tiver bolas suficientes, imprima a mensagem "Amelia tem todas as bolas!" (em inglês, "Amelia tem todas as bolas!")
'''

from math import floor # floor arredonda o numero pra baixo

b = int(input())
g = int(input())

r = g / 2

if b < r:
    f = r - b
    f = floor(f)
    print(f'Faltam {f} bolinha(s)')
    
else:
    print('Amelia tem todas as bolas!')