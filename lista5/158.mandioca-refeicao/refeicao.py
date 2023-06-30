'''
Todos os anos, no mês de abril, o Curupira, o Boitatá, o Boto rosa (este em sua forma de homem, como Dona Chica gosta mais), Mapinguari e Iara se encontram na Dona Chica para relembrar seus momentos com Mani, a linda menina de pele branca . E como não poderia ser diferente o prato principal desse encontro é a mandioca. Cada um come de uma a dez porções de mandioca e sempre avisam a Dona. Chica com antecedência sobre quantas porções vão comer naquele dia. O tamanho da porção de cada um é diferente, mas são sempre os mesmos. As porções são as seguintes (em gramas):

Curupira come 300
Boitatá come 1500
Boto come 600
Mapinguari come 1000
Iara come 150

Dona chica, por sua vez, come sempre 225 gramas de mandioca. Cansada de ter que calcular a cada ano quanta mandioca preparar, ela entrou em contato com você para escrever um programa que informa quanta mandioca deve ser preparada em gramas.

Entrada
A entrada consiste em 5 inteiros cada um representando as porções que os convidados do Dona Chica irão consumir. O primeiro inteiro representa as porções de Curupira, o segundo de Boitatá, o terceiro de Boto, o quarto de Mapinguari e o quinto de Iara.

Saída
A saída consiste em um único inteiro representando a quantidade de mandioca que Dona Chica deve preparar em gramas. Não se esqueça da quebra de linha após o awnser :).
'''

convidados = [300, 1500, 600, 1000, 150]

res = 0

for r in range(0, 5):
    c = int(input())
    res += c * convidados[r]

print(res + 225)
