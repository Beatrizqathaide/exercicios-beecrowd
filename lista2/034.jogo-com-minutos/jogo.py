#Leia a hora de início e de término de um jogo, em horas e minutos (hora inicial, minuto inicial, hora final, minuto final). Em seguida, imprima a duração do jogo, sabendo que o jogo pode começar em um dia e terminar em outro dia,

#Obs.: Com tempo máximo de jogo de 24 horas e tempo mínimo de jogo de 1 minuto.

horaInicial, minutoInicial, horaFinal, minutoFinal = map(int, input().split()) #função map aplica a função desejada em cada elemento do vetor

#Essa solução é um poco confusa, mas deu cert no VSCode e no Bee, fiz os cálculos manualmente para entender o funcionamento

minutoInicial += horaInicial * 60
minutoFinal += horaFinal * 60

tempo = minutoFinal - minutoInicial
if tempo <= 0:
    tempo += 24 * 60

hora = tempo // 60 #vai pegar a divisão inteira referente a hora
minuto = tempo % 60 #pega o resto da divisão referente ao minuto 

print(f'O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)')



'''
Essa solução é bem simples, no VsCode deu certo, porém no Bee não foi aceita
hora = horaFinal - horaInicial
minuto = minutoFinal - minutoInicial

if hora < 0:
    hora += 24

if minuto < 0:
    minuto += 60
    hora -= 1 #tira uma hora quando o tempo não chegar a 1 hora

if hora == 0 and minuto == 0:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    print(f'O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)')
'''