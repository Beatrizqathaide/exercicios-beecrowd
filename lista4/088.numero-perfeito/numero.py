#Em matemáticonta, um número perfeito é um número inteiro para o qual a soma de todos os seus próprios divisores positivos (excluindo a si mesmo) é igual ao próprio número. Por exemplo o número 6 é perfeito, pois 1+2+3 é igual a 6. Sua tarefa é escrever um programa que leia números inteiros e imprima uma mensagem informando se esses números são perfeitos ou não são perfeitos.

n = int(input())

for i in range(0, n):
    num = int(input())
    soma = 0
    cont = 1

    while cont < num:
        if num % cont == 0:
            soma += cont
        
        cont += 1
    
    if soma == num:
        print(f'{num} eh perfeito')
    
    else:
        print(f'{num} nao eh perfeito')
