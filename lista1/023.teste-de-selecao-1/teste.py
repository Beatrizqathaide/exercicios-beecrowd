#Leia 4 valores inteiros A, B, C e D. Então se B for maior que C e D for maior que A e se a soma de C e D for maior que a soma de A e B e se C e D forem valores positivos e se A for par, escreva a mensagem “Valores aceitos”. Caso contrário, escreva a mensagem “Valores não aceitos” (Valores não aceitos).

a, b, c, d = input().split(' ')

a = int(a)
b = int(b)
c = int(c)
d = int(d)

soma1 = c + d
soma2 = a + b

if (b > c) and (d > a) and (soma1 > soma2) and (c > 0) and (d > 0) and (a % 2 == 0):
    print('Valores aceitos')
else:
    print('Valores não aceitos')