#Leia três números inteiros e ordene-os em ordem crescente. Após, imprima esses valores em ordem crescente, uma linha em branco e depois os valores na sequência conforme foram lidos.

a, b, c = input().split(' ')

a = int(a)
b = int(b)
c = int(c)

lista = [a, b, c]

ordem = sorted(lista)

for c in ordem:
    print(c)

print('\n')

for n in lista:
    print(n)