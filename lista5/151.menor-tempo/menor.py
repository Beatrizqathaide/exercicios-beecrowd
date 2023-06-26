'''
Umil Bolt é um excelente corredor. Sua especialidade é a corrida de 100 metros. Todos os dias, ele faz uma bateria de tentativas para fazer esse teste em um tempo cada vez mais rápido. Pode-se observar que, dependendo do número de tentativas, seu desempenho melhora ou piora. Sobre isso, ele pede sua ajuda para calcular a tentativa mais rápida de cada bateria diária.

Entrada
A entrada é composta por vários casos de teste. A primeira linha de cada caso de teste contém um inteiro T (2 <= T <= 99) relativo ao número de tentativas de um dia. As T linhas seguintes contêm um número real Ti (9 <= Ti <= 11) relativo ao tempo, em segundos, da i-ésima tentativa de bateria. A entrada termina com o fim do arquivo.

Saída
Para cada caso de teste da entrada do seu programa, você deve imprimir um número real contendo o tempo da tentativa mais rápida de cada bateria.
'''

while True:
    try:

        t = int(input())
        x = []
        for c in range(0, t):
            
            x.append(float(input()))
        
        menor = x[0]
        for n in x:
            if n < menor:
                menor = n
            
        print(menor)

    except EOFError:
        break

