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




a = 'Roberto'
b = '5786'
c = 'UNIFEI'
t = '|'

for cont in range(0, 7):

    if cont == 0 or cont == 6:
        for i in range(0, 39):

            if i < 38:
                print('-', end='')

            elif i == 38:
                print('-')

    if cont == 1:
        print(f'{t:>1}{a:^24}{t:>14}')

    elif cont == 3:
        print(f'{t:>1}{b:^21}{t:>17}')

    elif cont == 5:
        print(f'{t:>1}{c:^23}{t:>15}')

    elif cont == 2 or cont == 4:
        print(f'{t:<1}{t:>38}')