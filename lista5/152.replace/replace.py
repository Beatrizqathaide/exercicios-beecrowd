a = 'Dona Ana é bem velhinha'

def meuReplace(string, troca, substituto):
    lista = []

    #transforma a string em lista
    for i in range(0, len(string)):
        lista.append(string[i])

    #localiza o elemento a ser trocado e faz a troca
    for c in range(0, len(lista)):
        if lista[c] == troca:
            lista[c] = substituto

    
    #faz o print com a troca do elemento
    for l in range(0, len(lista)):
        if l < len(lista) - 1:
            print(lista[l], end='')
        if l == len(lista) - 1:
            print(lista[l])

print(meuReplace(a, 'a', '*'))