'''
Leia um valor inteiro N. Depois, leia esses valores N e imprima uma mensagem para cada valor dizendo se esse valor é ímpar, par, positivo ou negativo. Em caso de zero (0), embora a descrição correta seja "EVEN NULL", pois por definição zero é par, seu programa deve imprimir apenas "NULL", sem aspas.
'''

n = int(input())

for c in range(0, n):
    x = int(input())

    if x % 2 == 0:
        if x > 0:
            print('EVEN POSITIVE') #par positivo
        if x < 0:
            print('EVEN NEGATIVE') #par negativo
    
    if x % 2 != 0:
        if x > 0:
            print('ODD POSITIVE') #impar positivo
        if x < 0:
            print('ODD NEGATIVE') #impar negativo
    
    if x == 0:
        print('NULL')