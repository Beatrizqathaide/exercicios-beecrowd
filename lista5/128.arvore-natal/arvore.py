'''
Todos os anos, Roberto gosta de escolher sua árvore de Natal, não deixa ninguém escolher por ele, pois acha que a árvore para ser bonita, deve atender algumas condições, como altura, espessura e número de galhos, para que possa pendurar muitos Decorações de Natal nele.

Roberto quer que sua árvore tenha pelo menos 200 centímetros de altura, mas não quer que ela tenha mais de 300 centímetros, ou a árvore não caberá em sua casa. Quanto à espessura, ele quer que sua árvore tenha um tronco com 50 centímetros de diâmetro ou mais. A árvore deve ter 150 ramos ou mais.

Entrada
A primeira linha de entrada contém um inteiro N(0 < N ≤ 10000), o número de casos de teste. As próximas N linhas contêm 3 inteiros cada, h, d e g(0 < a, d, g ≤ 5000), a altura da árvore em centímetros, seu diâmetro em centímetros e a quantidade de galhos da árvore.

Saída
Sua tarefa é, para cada árvore, imprimir Sim, se for uma árvore que o Roberto pode escolher, ou Nao, se for uma árvore que ele não deve escolher.
'''

t = int(input())

for c in range(0, t):
    h, d, g = map(int, input().split())

    if h >= 200 and h <= 300 and d >= 50 and g >= 150:
        print('Sim')
    else:
        print('Nao')