'''
Seu professor de programação gostaria que você fizesse um programa com as seguintes características:

Coloque sete espaços em branco e coloque o caractere 'A';
Coloque seis espaços em branco e coloque o caractere 'B', um espaço e o caractere 'B';
Coloque cinco espaços em branco e coloque o caractere 'C', três espaços em branco e o caractere 'C';
Coloque quatro espaços em branco e coloque o caractere 'D', cinco espaços em branco e o caractere 'D';
Coloque três espaços em branco e coloque o caractere 'E', sete espaços em branco e o caractere 'E';
Repita o procedimento 4;
Repita o procedimento 3;
Repita o procedimento 2;
Repita o procedimento 1.
Entrada
Não há.

Saída
O resultado do seu programa deve ser escrito de acordo com o exemplo de saída.
'''

a = 'ABCDEDCBA'

for c in range(0, len(a)):
    if a[c] == 'A':
        print(f'{a[c]:>8}')

    elif a[c] == 'B':
        print(f'{a[c]:>7}{a[c]:>2}')
    
    elif a[c] == 'C':
        print(f'{a[c]:>6}{a[c]:>4}')
    
    elif a[c] == 'D':
        print(f'{a[c]:>5}{a[c]:>6}')
    
    else:
        print(f'{a[c]:>4}{a[c]:>8}')