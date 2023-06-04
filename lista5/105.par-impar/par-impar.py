'''
A amarelinha é provavelmente a brincadeira onde as crianças da casa mais se divertem, porém a brincadeira tem causado bons momentos de discussão e choro nas crianças que a praticam. A causa do transtorno é decidir quem será o próximo a pular, mas recentemente Quico (O Gênio!) teve uma ótima ideia para resolver o problema. Basicamente o jogo só pode ser jogado a cada dois jogadores em um turno e escolher o próximo jogador Quico indicou usar o método tradicional par ou ímpar, onde ambos os jogadores informam um número e se a soma desses números for par, o jogador que escolher Vitória PAR ou vice-versa. Porém o uso desse método tem deixado o Quico louco, louco, louco... E por isso pediu a sua ajuda, pediu a você um programa que dava o nome dos jogadores, suas respectivas escolhas (PAR ou IMPAR) e os números , diga quem foi o vencedor.

Entrada
A primeira linha de entrada contém um único inteiro QT (1 ≤ QT ≤ 100), indicando o número de casos de teste a seguir. Cada caso de teste contém duas linhas. Na primeira linha será informado o nome do jogador 1 seguido de sua escolha, “PAR” ou “IMPAR”, e após o nome do jogador 2 seguido de sua escolha, “PAR” ou “IMPAR”. Na segunda linha do caso de teste, contém dois números inteiros N (1 ≤ N ≤ 10⁹) e M (1 ≤ M ≤ 10⁹), representando respectivamente os números escolhidos pelos jogadores 1 e jogador 2. Garantiu que a escolha do jogador 1 (PAR ou IMPAR) serão diferentes da escolha do jogador 2 (PAR ou IMPAR) e que o nome dos jogadores seja composto apenas por letras e não ultrapasse 100 caracteres.

Saída
Para cada caso de teste, imprima uma única linha contendo o nome do jogador vencedor.
'''

qt = int(input())

for c in range(0, qt):
    j1, esc1, j2, esc2 = map(str, input().split())
    n1, n2 = map(int, input().split())

    res = n1 + n2

    if res % 2 == 0:
        if esc1 == 'PAR':
            print(j1)
        else:
            print(j2)
    
    else:
        if esc1 == 'IMPAR':
            print(j1)
        else:
            print(j2)
