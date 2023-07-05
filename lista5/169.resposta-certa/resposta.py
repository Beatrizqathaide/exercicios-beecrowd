'''
Roumes era um aluno acima da média. Nas provas de matemática, ele sempre tirava nota máxima, acertando todas as contas, mas seu segredo não estava em fazer as contas corretamente. Ele interpretou o que viu no ambiente ao seu redor e pôde deduzir as respostas para as perguntas. Você também pode ser alguém especial, assim como Roumes.

Entrada
A entrada consiste em vários casos de teste. Cada caso contém um número N , representando o número de questões. As próximas N linhas mostram o que você viu para chegar à resposta.

Saída
Para cada pergunta feita, imprima a palavra 'resposta', seguida de um espaço, depois o número da pergunta, dois pontos, um espaço e a resposta.
'''

n = int(input())

for c in range(1, n + 1):
    v = int(input())
    print(f'resposta {c}: {v}')
