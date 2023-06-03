'''
Papai Noel está brincando com seus elfos para entretê-los durante a véspera de Natal. A brincadeira consiste em os elfos escreverem números em pedaços de papel e colocarem no gorro do Papai Noel. Depois de tudo terminado de colocar os números, o Papai Noel sorteia um número e esse número é quantos "Ho" ele deve dizer.

Seu trabalho é ajudar o Papai Noel fazendo um problema que mostre todos os "Ho" que ele deve falar dado o número sorteado.

Entrada
A entrada consiste em um único inteiro N (0 < N ≤ 106) representando quantos "Ho" serão falados pelo Papai Noel.

Saída
A saída consiste em todos os "Ho" que o Papai Noel deve falar separados por um espaço. Após o último "Ho" você deve apresentar um "!" terminando o programa.
'''

n = int(input())

cont = 0

while cont <= n:
    if cont < n - 1:
        print('Ho', end=' ')
    if cont == n:
        print('Ho!')

    cont+=1