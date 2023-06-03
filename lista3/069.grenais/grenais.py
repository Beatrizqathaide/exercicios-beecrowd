'''
A Federação Gaúcha de Futebol convidou você a escrever um programa para apresentar um resultado estatístico de vários GRENAIS. Escreva um programa que leia o número de gols marcados pelo Inter e o número de gols marcados pelo Grêmio em um GRENAL. Escreva a mensagem "Novo grenal (1-sim 2-nao)" e solicite uma resposta. Se a resposta for 1, devem ser lidos dois novos números (outro caso de entrada) perguntando o número de gols marcados pelas equipes em uma nova partida, caso contrário o programa deve ser finalizado, imprimindo:

- Quantos GRENAIS fizeram parte das estatísticas.
- O número de vitórias do Inter.
- O número de vitórias do Grêmio.
- O número de empates.
- Uma mensagem indicando o time que ganhou o maior número de GRENAIS (ou a mensagem: "Não houve vencedor" se ambos os times ganharam a mesma quantidade de GRENAIS).
'''

continua = 1
grenais = 0
vitoriaInter = 0
vitoriaGremio = 0
empate = 0

while True:
    if continua == 1:
        golInter, golGremio = input().split()
        golInter = int(golInter)
        golGremio = int(golGremio)

    if continua == 2:
        break
    
    if golInter > golGremio:
        vitoriaInter += 1
    
    if golGremio > golInter:
        vitoriaGremio += 1

    if golInter == golGremio:
        empate += 1
    
    if vitoriaInter > vitoriaGremio:
        timeVencedor = 'Inter'
    
    if vitoriaGremio > vitoriaInter:
        timeVencedor = 'Gremio'
    
    grenais += 1
    
    continua = int(input('Novo grenal (1-sim 2-nao)\n'))

print(f'{grenais} grenais')
print(f'Inter:{vitoriaInter}')
print(f'Gremio:{vitoriaGremio}')
print(f'Empates:{empate}')
print(f'{timeVencedor} venceu mais')