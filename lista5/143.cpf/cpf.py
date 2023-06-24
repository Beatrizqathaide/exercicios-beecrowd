'''
Seu professor gostaria de fazer um programa com as seguintes características:

Lê os dados de um CPF no formato XXX.YYY.ZZZ-DD ;
Imprima os quatro números, um valor por linha.

Entrada
A entrada consiste em vários arquivos de teste. Em cada arquivo de teste há uma linha. A linha tem o seguinte formato XXX.YYY.ZZZ-DD , onde XXX, YYY, ZZZ, DD são números inteiros. Conforme mostrado no exemplo de entrada a seguir.

Saída
Para cada arquivo na entrada, você tem um arquivo de saída. O arquivo de saída tem quatro linhas com um número inteiro em cada uma delas conforme foi inserido. Conforme mostrado no exemplo de saída a seguir.
'''

while True:
    try:
        cpf = input()
        cpf = cpf.replace('-', '.')
        p = cpf.split('.')

        for c in p:
            print(c)
    
    except EOFError:
        break