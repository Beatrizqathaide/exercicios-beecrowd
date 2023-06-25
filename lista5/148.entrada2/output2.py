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

for c in range(0, 40):

    if c < 38:
        print('-', end='')
    
    elif c == 38:
        print('-')

for t in range(0, 5):

    if t == 0:
        print('|        Roberto                      |')

    elif t == 2:
        print('|        5786                         |')

    elif t == 4:
        print('|        UNIFEI                       |')

    else:
        print('|                                     |')

for c in range(0, 40):

    if c < 38:
        print('-', end='')
    
    elif c == 38:
        print('-')