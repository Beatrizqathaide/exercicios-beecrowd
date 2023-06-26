'''
Seu professor gostaria de fazer uma tela com as seguintes características:

Ter 39 traços (-) na primeira linha;
Tenha um | abaixo do primeiro travessão e do trigésimo nono travessão da primeira linha, abaixo do travessão deve começar a escrever a palavra "Roberto" e o restante preencher no meio com espaço em branco;
Tenha um | abaixo do primeiro traço e do trigésimo nono traço da primeira linha, preencha o meio com um espaço em branco;
Tenha um | abaixo do primeiro travessão e do trigésimo nono travessão da primeira linha, abaixo do 10 travessão você deve começar a digitar o número "5786" e o restante preencher no meio com espaço em branco;
Repita o procedimento 3;
Tenha um | abaixo do primeiro travessão e do trigésimo nono travessão da primeira linha, abaixo do travessão 10 deve-se começar a escrever a palavra "UNIFEI" e o restante preencher no meio com espaço em branco;
Repita o procedimento 1.
Ao final deve ficar como na imagem a seguir:

--------------------------------------- (39 traces)
|        Roberto                      |
|                                     |
|        5786                         |
|                                     |
|        UNIFEI                       |
--------------------------------------- (39 traces)
Entrada
Não há.

Saída
A saída será impressa como mostrado acima.
'''




x = 'x = 35'
t = '|'

for cont in range(0, 7):

    if cont == 0 or cont == 6:
        for c in range(0, 39):

            if c < 38:
                print('-', end='')

            elif c == 38:
                print('-')

    if cont == 1:
        print(f'{t:<1}{x:^2}{t:>32}')

    elif cont == 3:
        print(f'{t:>1}{x:^36}{t:>2}')

    elif cont == 5:
        print(f'{t:>1}{x:>37}{t:>1}')

    elif cont == 2 or cont == 4:
        print(f'{t:<1}{t:>38}')