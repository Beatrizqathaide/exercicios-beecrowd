'''
Um dia, o grande herói Chapolout ajudou um cientista que criou muitas invenções. Uma dessas invenções é um sistema que abre a porta secreta do laboratório. O sistema consiste em retirar uma porta lateral da vela do castiçal, que ela abre, e ao colocar a vela de volta no lustre, a porta se fecha. Mas Chapolout descobriu que a vela era apenas uma farsa. Na verdade, o cientista assistente, chamado Pepe, que abriu a porta do laboratório, por dentro. Um tempo depois, o sistema foi modificado para rodar também o projeto inicial. Um sensor de pressão colocado abaixo da vela do candelabro, para que a remoção do sistema de vela ativa. Este sistema emite um relatório de log para cada vez que a porta é aberta ou fechada, mas o log é bastante confuso. A cada registro são registrados três números inteiros, sendo a hora e o minuto em que ocorreu o evento e um valor que representa a porta aberta ou fechada no momento. Pepe pede sua ajuda para converter os dados de log em dados mais legíveis para ele.

Escreva um programa que, dado um registro de log, seja convertido em textos mais legíveis.

Entrada
A primeira linha contém o número de casos de teste. Cada linha de um caso de teste possui três inteiros H, M e O, sendo o tempo, os minutos da ocorrência e a própria instância (zero se a porta se fechou ou se a porta se abriu).

Saída
Para cada caso de teste, imprima a hora da ocorrência, na devida forma, seguida de um espaço, um hífen e um espaço, e a frase "A porta abriu!" ou "A porta fechada!" conforme a ocorrência registrada.
'''

t = int(input())

for c in range(0, t):
    h, m, o = map(int, input().split())

    if o == 1:
        print(f'{h:02}:{m:02} - A porta abriu!')
    else:
        print(f'{h:02}:{m:02} - A porta fechou!')