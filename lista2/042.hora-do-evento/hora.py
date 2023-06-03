'''
Peter está organizando um evento em sua universidade. O evento será no mês de abril, começando e terminando no mês de abril. O problema é: Peter quer calcular a duração do evento em segundos, sabendo obviamente o horário de início e término do evento.

Você sabe que o evento pode levar de alguns segundos a alguns dias, portanto, você deve ajudar Peter a calcular o tempo total correspondente à duração do evento.

Obs: Considere que o evento do caso de teste tem a duração mínima de um minuto.
'''

d1 = int(input().split()[1])
h1, m1, s1 = map(int, input().split(':'))
t1 = s1 + (m1 * 60) + (h1 * 60 * 60) + (d1 * 24 * 60 *60)

d2 = int(input().split()[1])
h2, m2, s2 = map(int, input().split(':'))

t2 = s2 + (m2 * 60) + (h2 * 60 * 60) + (d2 * 24 * 60 *60)

diferenca = t2 - t1

dia = diferenca // (24 * 60 * 60)
diferenca = diferenca % (24 * 60 * 60)

hora = diferenca // (60 * 60)
diferenca = diferenca % (60 * 60)

minuto = diferenca // 60
diferenca = diferenca % 60

segundo = diferenca

print(f'{dia} dia(s)')
print(f'{hora} hora(s)')
print(f'{minuto} minuto(s)')
print(f'{segundo} segundo(s)')
