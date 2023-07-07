'''
Jon Marius esqueceu como somar dois números enquanto fazia pesquisas para seu doutorado. E agora ele tem uma longa lista de problemas de adição que precisa resolver, além dos problemas de informática! Você pode ajudá-lo?

Em sua lista atual, Jon Marius tem dois tipos de problemas: problemas de adição na forma “ a + b ” e o problema sempre retornando “P=NP”. Jon Marius é uma pessoa bastante distraída, então pode ter resolvido esse último problema várias vezes, já que vive esquecendo a solução. Além disso, ele gostaria de resolver esses problemas sozinho, então você deve ignorá-los.

Entrada
A primeira linha de entrada será um único inteiro N (1 ≤ N ≤ 1000) denotando o número de casos de teste. Em seguida, siga N linhas com ”P=NP” ou um problema de adição na forma ” a + b ”, onde a , b ∈ [0, 1000] são números inteiros.

Saída
Emita o resultado de cada adição. Para linhas contendo “P=NP”, saída “skipped”.
'''

testes = int(input())

for c in range(0, testes):
    problema = input()
    if problema != 'P=NP':
        problema = problema.split('+')
        problema[0] = int(problema[0])
        problema[1] = int(problema[1])
        resultado = problema[0] + problema[1]
        print(resultado)
        
    else:
        print('skipped')
        