'''
Para conter a greve geral estudantil, o governo realizou uma reunião com a UFSC. Durante a reunião, a UFSC explicou todos os gastos necessários para mantê-la funcionando até o final do ano, e o Governo informou os valores que poderia oferecer para cobrir essas despesas. A reunião foi pouco organizada, e vários valores individuais foram mencionados, então ninguém sabe se os valores oferecidos são suficientes para cobrir todas as despesas da universidade.

Dada a lista de valores citada na reunião, sua tarefa será somar as despesas e verbas oferecidas para informar aos alunos da UFSC se a greve deve ou não cessar.

Entrada
A entrada começa com um inteiro N (1 ≤ N ≤ 100.000) que indica o número de valores citados na reunião. Cada linha tem um caractere T e um inteiro C (1≤ C ≤ 100.000) separados por um espaço em branco. T será igual a 'V' se o valor C representar uma subvenção do governo, ou igual a 'G' se o valor C representar uma despesa da universidade.

Saída
Imprima "A greve vai parar." Se os números do governo forem suficientes para cobrir todos os gastos da universidade até o final do ano, ou imprimir “SEM CORTE, LUTA!” De outra forma. (Em ambos os casos a frase deve ser impressa sem aspas).
'''

n = int(input())

subvencao = 0
despesa = 0

for i in range(0, n):
    t, c = map(str, input().split())
    c = int(c)

    if t == "V":
        subvencao += c

    if t == 'G':
        despesa += c

if subvencao > despesa:
    print('A greve vai parar.')

else:
    print('NAO VAI TER CORTE, VAI TER LUTA!')

