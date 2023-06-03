'''
O Brasil é o país anfitrião da copa do mundo este ano. No entanto, há muitas pessoas protestando contra o governo. Nas redes sociais é possível ver pessoas dizendo que a copa do mundo não vai acontecer.

Mas esses boatos de que não vai ter copa do mundo são totalmente falsos, a presidente Dilma Rousseff já avisou: a copa vai acontecer, e se alguém reclamar, a gente vai sediar de novo!

Entrada
A entrada contém vários casos de teste e termina com EOF. Cada caso de teste consiste em uma linha contendo um número N de reclamações sobre a copa do mundo encaminhadas ao presidente (0 ≤ N ≤ 100).

Saída
Para cada teste, a saída consiste em uma linha dizendo "vai ter copa!" se não houver reclamações para presidente. Se houver reclamações, a saída deve ser "vai ter duas!".
'''

while True:
    try:
        n = int(input())
    
        if n == 0:
            print("vai ter copa!")
        else:
            print('vai ter duas!')
    except EOFError:
        break
