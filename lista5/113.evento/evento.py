'''
Prog e Cackto recentemente começaram a jogar um RPG chamado Fortress. Neste jogo, para o jogador evoluir seu nível, ele precisa derrotar monstros, o que dá um valor de experiência (XP) para o jogador.

A produtora do jogo, Extreme Games, anunciou que na próxima semana será realizado o primeiro evento XP deste jogo no qual aumentará a experiência dos monstros em um valor X. Como o Prog e o Cackto estão em um nível muito alto em que os monstros possuem uma quantidade de pontos de experiência muito alta, eles estão tendo dificuldades em calcular a quantidade de pontos de experiência que os monstros terão durante o evento. Você pode ajudá-los?

Entrada
Haverá vários casos de teste. Cada caso de teste contém dois valores: X (0 < X ≤ 3) indicando o aumento no valor de EXP dos monstros e M (10 ≤ M ≤ 232-1) indicando o valor de EXP do monstro. A entrada termina com os valores X == 0 e M == 0, nos quais não devem ser processados.

Saída
Para cada caso, seu programa deve mostrar um valor E, valor do novo Monster EXP.
'''

while True:

    x, m = map(int, input().split())

    if x == 0 and m == 0:
        break

    e = x * m

    print(e)

