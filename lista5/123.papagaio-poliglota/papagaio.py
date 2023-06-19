'''
Humberto tem um papagaio esperto. Quando está com as duas pernas no chão, o papagaio fala português. Quando ele levanta a perna esquerda, ele fala em inglês. Por fim, quando levanta a mão direita, fala francês. Nico, amigo de Humberto, ficou fascinado com o animal. Em sua empolgação, ele perguntou: "E quando ele levantou os dois?" Antes que Humberto pudesse responder, o papagaio gritou: "Ah, vou cair, seu idiota!"

Entrada
A entrada consiste em vários casos de teste. Cada caso de teste consiste em uma string informando a situação de elevação da perna do papagaio. “direita” significa que a perna direita está levantada, “esquerda” significa que a perna esquerda está levantada, “nenhuma” significa que nenhuma das pernas está levantada e “as duas” significa que ambas as pernas estão levantadas.

Saída
Para a condição de levantar a perna de cada papagaio, imprima a linguagem que ele usará. Para inglês, imprima “ingles”, para francês imprima “frances” e para português imprima “portugues”. Se ele levantar as duas pernas, imprima "caiu". Quebre uma linha para cada caso de teste.
'''

while True:
    try:
        t = input()

        if t == 'esquerda':
            print('ingles')
        elif t == 'direita':
            print('frances')
        elif t == 'nenhuma':
            print('portugues')
        elif t == 'as duas':
            print('caiu')
    
    except EOFError:
        break