'''
Dada uma letra do alfabeto, indique sua posição.

Entrada
Um único caractere L, uma letra maiúscula ('A' - 'Z') do alfabeto.

Saída
Um único inteiro, que representa a posição da letra no alfabeto.
'''

l = input()

a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for c in range(0, len(a)):
    if l == a[c]:
        print(c + 1)
