'''
Devita é o príncipe dos Calsadins. Juntamente com Pana, eles vão atrás de Tataroko, nome de nascimento de Kogu, para tentar dominar o mundo. Possui um rastreador que mede o nível de energia de qualquer ser vivo. Todos os seres com o nível menor ou igual a 8000, considera como se fosse um inseto ("Inseto"). Ao passar desse valor, que foi o caso de Kogu, ele fica atônito e grita "Mais de 8000", que significa "Já passou de 8000". Com base nisso, use a mesma tecnologia e analise o nível de energia dos seres vivos.

Entrada
A entrada é composta por vários casos de teste. A primeira linha contém um inteiro C relativo ao número de casos de teste. Então haverá C linhas, com um inteiro N (100 <= N <= 100000) relativo ao nível de energia de um ser vivo.

Saída
Para cada valor lido, imprima o texto correspondente.
'''

t = int(input())

for c in range(0, t):
    i = int(input())

    if i <= 8000:
        print('Inseto!')
    else:
        print('Mais de 8000!')