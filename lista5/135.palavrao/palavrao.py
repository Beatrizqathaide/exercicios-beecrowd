'''
Recentemente, Juquinha aprendeu a falar palavrões. Essas palavras do português brasileiro são comumente chamadas de "palavrao"s. Espantada com a descoberta do menino, a mãe o proibiu de dizer qualquer "palavrao", sob o risco de o menino perder a mesada.

Como Juquinha detesta ficar sem mesada, ele contratou você para desenvolver um programa para dizer a ele se uma palavra é um "palavrao" ou não.

"Palavrao"s são palavras que contém dez ou mais caracteres, todas as outras palavras são consideradas "palavrinhas".

Entrada
A entrada consiste em vários casos de teste. Cada caso contém uma string que descreve a palavra que Juquinha deseja procurar. Esta string é composta apenas por letras minúsculas e seu comprimento não excede 20 caracteres.

Saída
Para cada caso de teste, imprima se a palavra que Juquinha consultou é um "palavrao" (palavra grande) ou uma "palavrinha" (outras palavras).
'''

p = input()

if len(p) >= 10:
    print('palavrao')

else:
    print('palavrinha')

