a = 'Casa / suja / chão / sujo'

#a = a.split('/')

#print(f'Com split pronta: {a}')


lista = []

#transforma a string em lista
for c in range(0, len(a)):
    lista.append(a[c])

print(lista)

separador = []

for c in range(0, len(lista)):
    if lista[c] == '/':
        separador.append(c)

