#Escreva um algoritmo para ler um número indeterminado de dados, cada um contendo a idade de um indivíduo. Os dados finais, que não entrarão nos cálculos, contêm o valor de uma idade negativa. Calcule e imprima a idade média desse grupo de indivíduos.

soma = 0
cont = 0
while True:
    idade = int(input())

    if idade < 0:
        break

    soma += idade
    cont += 1

media = soma / cont
print(f'{media:.2f}')