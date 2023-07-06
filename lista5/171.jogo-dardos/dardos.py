'''
John e Mary criaram sua própria versão de dardos, dardos à distância. Cada um lança 3 dardos, escolhendo a que distância jogará do alvo. No jogo normal de dardos, um número x é marcado pela distância entre onde o dardo atingiu e o centro do alvo. No jogo do João e da Maria é pontuado xd onde d é a distância entre o atirador e o alvo.

John pede para você fazer um algoritmo que dá a pontuação dada a distância de cada turno, retorna o vencedor

Entrada
A primeira linha da entrada consiste em um número N de casos de teste. Em cada caso de teste haverá 6 linhas, onde as 3 primeiras linhas correspondem às notas de João e as 3 linhas seguintes às notas de Maria. Cada linha de um caso de teste consiste em dois números X e D onde X é a pontuação e D é a distância

Saída
A saída consiste no vencedor de cada caso de teste.
'''

testes = int(input())

cont = 0

while cont < testes:
    maria = 0
    joao = 0
    for c in range(0, 6):

        pontos, distancia = map(int, input().split())

        if c >= 0 and c <= 2:
            maria += pontos * distancia
            
        else:
            joao += pontos * distancia
           
    if maria < joao:
        print('MARIA')
    else:
        print('JOAO')

    cont += 1
