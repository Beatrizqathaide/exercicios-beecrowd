'''
Vinicius leva a forma física muito a sério e, todas as manhãs, às 6h, faça chuva ou faça sol, no verão e no inverno, ele corre em uma pista ao redor de uma lagoa. Ao longo da pista de corrida existem N sinais igualmente espaçados. Para não desanimar de se exercitar, Vinícius conta o número de placas pelas quais passou e verifica se correu pelo menos 10%, pelo menos 20%, . . . , pelo menos 90% de seu treinamento.

Vamos ajudar o Vinícius calculando para ele o número de sinais que ele precisa contar para ter completado pelo menos 10%, 20%, . . . , 90% do seu treino, dado o número de voltas que pretende realizar e o número total de sinais ao longo da pista

Por exemplo, suponha que Vinicius queira fazer 3 voltas e a pista tenha 17 placas. Para garantir que ele correu pelo menos 30% de seu treinamento, ele precisa contar 16 sinais. Para garantir pelo menos 60%, ele precisa contar 31 sinais.

Entrada
A entrada consiste em uma única linha, que contém dois inteiros, V e N (1 ≤ V , N ≤ 10 4 ), onde V é o número desejado de voltas e N é o número de sinais ao longo da pista.

Saída
Seu programa deve gerar uma única linha, contendo nove inteiros, representando o número de sinais que devem ser contados para garantir que pelo menos 10%, 20%, . . . , 90% do treinamento foi concluído, respectivamente.
'''
from math import ceil

voltas, placas = map(int, input().split())

total = voltas * placas

treinamento = []

for c in range(10, 100, 10):
    porcentagens = ceil(c * total / 100)
    treinamento.append(porcentagens)

for i in range(0, len(treinamento)):
    if i < len(treinamento) - 1:
        print(treinamento[i], end=' ')
    
    else:
        print(treinamento[i])