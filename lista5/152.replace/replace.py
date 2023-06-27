a = 'Dona Ana é bem velhinha'

lista = []

#transforma a string em lista
for i in range(0, len(a)):
    lista.append(a[i])

#localiza o elemento a ser trocado e faz a troca
for c in range(0, len(lista)):
    if lista[c] == 'a':
        lista[c] = '*'

#faz o print com a troca do elemento
for l in range(0, len(lista)):
    if l < len(lista) - 1:
        print(lista[l], end='')
    if l == len(lista) - 1:
        print(lista[l])
