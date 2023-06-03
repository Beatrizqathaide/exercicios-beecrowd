'''
Maria acabou de começar como estudante de pós-graduação em uma faculdade de medicina e precisa da sua ajuda para organizar um experimento de laboratório pelo qual ela é responsável. Ela quer saber, no final do ano, quantos animais foram usados ​​nesse laboratório e qual a porcentagem de cada tipo de animal que é usado.

Este laboratório utiliza em particular três tipos de animais: rãs, ratos e coelhos. Para obter essas informações, ele sabe exatamente o número de experimentos que foram realizados, o tipo e a quantidade de cada animal utilizado em cada experimento.
'''

casos = int(input())

coelho = 0
rato = 0
sapo = 0
totalAnimais = 0

for c in range(0, casos):
    animal = input().split(' ')
    animal[0] = int(animal[0])
    animal[1] = str(animal[1]).upper()

    totalAnimais += animal[0]

    if animal[1] == 'C':
        coelho += animal[0]
    
    if animal[1] == 'R':
        rato += animal[0]
    
    if animal[1] == 'S':
        sapo += animal[0]

print(f'Total: {totalAnimais} cobaias')
print(f'Total de coelhos: {coelho}')
print(f'Total de ratos: {rato}')
print(f'Total de sapos: {sapo}')
print(f'Percentual de coelhos: {coelho * 100 / totalAnimais:.2f} %')
print(f'Percentual de ratos: {rato * 100 / totalAnimais:.2f} %')
print(f'Percentual de sapos: {sapo * 100 / totalAnimais:.2f} %')