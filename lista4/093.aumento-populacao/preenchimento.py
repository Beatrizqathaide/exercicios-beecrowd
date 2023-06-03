''''
Mariazinha quer resolver um problema interessante. Dada a população e a taxa de crescimento de 2 cidades (A e B), ela gostaria de saber quantos anos seriam necessários para que a cidade menor (sempre A) fosse maior que a cidade maior (sempre B) em população. Claro, ela só quer saber o resultado para as cidades de que a taxa de crescimento da cidade A é maior que a taxa de crescimento da cidade B, portanto, ela separou esses casos de teste para você. Seu trabalho é construir um programa que imprima o tempo em anos para cada caso de teste.

Porém, em alguns casos o tempo pode ser tão grande e Mariazinha não quer saber o tempo exato para esses casos. Desta forma, para estes casos de teste, basta imprimir a mensagem "Mais de 1 seculo", que significa "Mais de um Século".
'''

t = int(input())

for c in range(0, t):
    pa, pb, g1, g2 = input().split()
    pa = int(pa)
    pb = int(pb)
    g1 = float(g1) / 100
    g2 = float(g2) / 100

    anos = 0

    while True:
        pa = int(pa + (pa * g1))
        pb = int(pb + (pb * g2))
        
        anos += 1

        if pa > pb or anos > 100:
            break

    if anos <= 100:
        print(f'{anos} anos.')
    else:
        print('Mais de 1 seculo.')