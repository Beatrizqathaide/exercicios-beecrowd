'''
Odin criou para Thor a arma mais fiel e poderosa possível, o martelo Mjolnir. Feito de um minério místico especial chamado Uru e forjado no coração de uma estrela pelos ferreiros Deuses de Asgard, Brokk e Eitri, lendários ferreiros.

Um dia, Thor desafiou seus amigos para ver quem conseguiria erguer o Mjölnir.

Escreva um programa que, dado um nome e a força em Newtons aplicada para tentar levantar o Thunder Hammer, informe a pessoa que conseguiu levantá-lo.

Entrada
Deve ser informado um inteiro C , que é a quantidade de casos de teste. Cada caso de teste começa com uma palavra, que é o primeiro nome de quem está tentando levantar o Mjölnir, e um inteiro N (1 ≤ N ≤ 25000), indicando a força aplicada para cima em Newtons para puxar o martelo de então tente levantá-lo .

Saída
Para cada caso de teste imprima um caractere 'S', se a pessoa conseguiu levantar ou 'N' se não conseguiu.
'''

c = int(input())

for i in range(0, c):
    p, n = map(str, input().split())

    if p == 'Thor':
        print('Y')
    else:
        print('N')

