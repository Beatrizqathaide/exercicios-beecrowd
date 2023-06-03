'''
Seu programa deve ler um inteiro X vezes indefinidas (o programa deve parar quando X for igual a zero). Para cada X imprima a sequência de 1 a X, com um espaço entre cada um desses números.

P.S.: Cuidado. Não deixe nenhum espaço após o último número de cada linha, caso contrário, você receberá um erro de apresentação.
'''

while True:
    x = int(input())

    if x == 0:
        break

    cont = 1
    if x > 0:    
        while cont <= x:
            if cont == x:
                print(cont, end='\n')
            else:
                print(cont, end=' ')
            cont += 1
