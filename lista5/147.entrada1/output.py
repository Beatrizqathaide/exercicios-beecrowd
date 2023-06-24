'''
Seu professor de programação gostaria de fazer uma tela com as seguintes características:

Ter 39 traços (-) na primeira linha;
Tenha um | abaixo do primeiro traço e do trigésimo nono traço da primeira linha, preencha o meio com um espaço em branco;
Repita o procedimento 2 mais quatro vezes;
Repita o procedimento 1.
Ao final deve ficar como na imagem a seguir:

--------------------------------------- (39 traços)
| |
| |
| |
| |
| |
--------------------------------------- (39 traços)
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
    print('|                                     |')

for c in range(0, 40):

    if c < 38:
        print('-', end='')
    
    elif c == 38:
        print('-')