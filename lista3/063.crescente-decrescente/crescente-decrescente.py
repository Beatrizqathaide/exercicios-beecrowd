#Leia um número indeterminado de pares de valores inteiros. Escreva uma mensagem para cada par indicando se esses dois números estão em ordem crescente ou decrescente.

while True:
    x, y = map(int, input().split())
    
    if x < y:
        print('Crescente')
    
    if x > y:
        print('Decrescente')
    
    if x == y:
        break
    