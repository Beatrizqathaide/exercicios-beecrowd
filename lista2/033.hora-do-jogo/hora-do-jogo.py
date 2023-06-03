#Leia a hora de início e a hora de término de um jogo, em horas. Em seguida, calcule a duração do jogo, sabendo que o jogo pode começar em um dia e terminar em outro dia, com duração máxima de 24 horas. A mensagem deve ser impressa em português “O JOGO DUROU X HORA(S)” que significa “O JOGO DUROU X HORA(S)”

inicio, termino = input().split(' ')

inicio = int(inicio)
termino = int(termino)

if inicio < termino:
    duracao = termino - inicio
else:
    duracao = (24 - inicio) + termino

print(f'O JOGO DUROU {duracao} HORA(S)')