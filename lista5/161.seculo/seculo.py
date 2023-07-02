'''
Depois de uma aula de história muito boa - sucedendo uma aula de matemática muito ruim - alguns alunos de uma escola específica ficam em dúvida sobre um problema simples. A professora perguntou-lhes qual era o valor numérico (para simplificar, deve ser decimal e conter algarismos arábicos) do século de um determinado ano mas, como poucos alunos o sabiam, resolveu pedir-vos ajuda para criar um programa que faz exatamente isso para fins educacionais.

Para quem não lembra dessa aula de história, o século 1, por exemplo, significa os anos entre 1 e 100, o século 2 os anos entre 101 e 200, o século 3 os anos entre 201 e 300 e assim por diante.

Entrada
A entrada contém vários casos de teste e é finalizada no final do arquivo. Cada linha é um novo caso de teste e contém um único inteiro  N  (1 ≤  N  ≤ 10 9 ), que significa o valor de algum ano que deve ser processado.

Saída
Para cada caso de teste, imprima uma linha com o valor do século do ano correspondente.
'''

from math import ceil

while True:
    try:

        ano = int(input())
        seculo = ceil(ano / 100)
               
        print(seculo)
    
    except EOFError:
        break

