'''
Seu professor gostaria de fazer um programa com as seguintes características:

Ler uma data no formato DD/MM/AA ;
Imprima a data no formato MM/DD/AA ;
Imprima a data no formato AA/MM/DD ;
Imprima a data no formato DD-MM-AA .
Entrada
A entrada consiste em vários arquivos de teste. Em cada arquivo de teste há uma linha. A linha tem o seguinte formato DD/MM/AA onde DD, MM e AA são números inteiros. Conforme mostrado no exemplo de entrada a seguir.

Saída
Para cada arquivo na entrada, você tem um arquivo de saída. O arquivo de saída tem três linhas de acordo com os procedimentos 2, 3 e 4. Conforme mostrado no exemplo de saída a seguir.
'''

while True:
    try:
        d, m, a = map(str, input().split('/'))

        print(f'{m}/{d}/{a}')
        print(f'{a}/{m}/{d}')
        print(f'{d}-{m}-{a}')

    except EOFError:
        break