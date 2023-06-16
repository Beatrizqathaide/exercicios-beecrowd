'''
Gilberto é um famoso vendedor de esfihas. Porém, embora todos gostem de suas esfihas, ele só consegue dar o troco com duas notas diferentes, ou seja, nem sempre é possível acertar o troco. Para facilitar a vida de Gil, faça um programa para ele verificar se é possível dar o troco exato usando duas notas diferentes.

Notas disponíveis: 2, 5, 10, 20, 50 e 100.

Entrada
A entrada contém um inteiro N representando o preço de compra e então um inteiro M representando o preço pago pelo cliente (N < M ≤ 104). Leia a entrada até N = M = 0.

Saída
Imprima "possível" se for possível dar o troco exato ou "impossível" se não for.
'''

n, m = map(int, input().split())

troco = m - n
nota = 0

while True:
    if m == 0 and n == 0 or troco == 0 or troco == 1:
        break

    if troco >= 100:
        troco -= 100
        nota += 1

    elif troco >= 50:
        troco -= 50
        nota += 1

    elif troco >= 20:
        troco -= 20
        nota += 1

    elif troco >= 10:
        troco -= 10
        nota += 1

    elif troco >= 5:
        troco -= 5
        nota += 1

    elif troco >= 2:
        troco -= 2
        nota += 1

if nota == 2:
    print('possible')

else:
    print('impossible')
