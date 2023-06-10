'''
Rock, Paper, Airstrike é um jogo infantil muito popular, no qual duas ou mais crianças formam um círculo e fazem gestos com as mãos na tentativa de obter a vitória. As regras são surpreendentemente complexas para um jogo infantil, mas ainda é bastante popular em todo o mundo.

Os jogos são muito simples. Os jogadores podem escolher entre o sinal da Pedra (punho), o sinal do papel (a palma da mão aberta) e o sinal para o Ataque Aéreo (como o papel, mas com apenas o polegar e o dedo mínimo estendidos).

Um jogo com dois jogadores tem as seguintes regras para determinar um vencedor:

Airstrike vs. Rock: Neste caso, o jogador com Airstrike derrota o jogador com Rock por razões óbvias.
Pedra vs. Papel: Neste caso o jogador com Pedra derrota o de Papel, porque Pedra dói mais.
Paper vs. Airstrike: Aqui o Airstrike vence porque o Airstrike sempre vence e o Paper é patético.
Paper vs. Paper: Nesta variação, ambos os jogadores ganham porque o Paper é inútil e ninguém que enfrenta o Paper pode perder.
Rock vs. Rock: Para este caso não há vencedor porque depende do que os jogadores decidirem fazer com o Rock e geralmente não fazem nada no final.
Airstrike vs. Airstrike: Quando isso acontece, todos os jogadores perdem devido à Aniquilação Mútua.
Sua tarefa é escrever um programa que, dada a escolha de dois jogadores, diga quem ganhou o jogo.

Entrada
A entrada consiste em N (1 ≤ N ≤ 1000) casos de teste. N deve ser lido na primeira linha de entrada. Cada caso de teste é composto por duas linhas, cada uma contendo uma string. A primeira string é o sinal escolhido pelo Jogador 1 e a segunda string é o sinal escolhido pelo Jogador 2. Essas strings podem ser:

“ataque”: representar ataque aéreo
“pedra”: representar o Rock
“papel”: tp representa papel
Saída
A saída deve conter:

“Jogador 1 venceu”: se o Jogador 1 ganhou o jogo
“Jogador 2 venceu”: se o Jogador 2 ganhou o jogo
“Ambos venceram”: se os dois ganharam o jogo
“Sem ganhador”: se não houver ganhador
“Aniquilacao mutua”: se ocorrer Aniquilação Mútua
Cada saída de um caso de teste deve estar em uma linha.
'''
  
n = int(input())

for c in range(0, n):
    j1 = input()
    j2 = input()

    if j1 == 'pedra' and j2 == 'pedra':
        print('Sem ganhador')
    
    elif j1 == 'papel' and j2 == 'papel':
        print('Ambos venceram')

    elif j1 == 'ataque' and j2 == 'ataque':
        print('Aniquilacao mutua')

    elif j1 == 'ataque' and j2 == 'pedra' or j1 == 'pedra' and j2 == 'papel' or j1 == 'ataque' and j2 == 'papel':
        print('Jogador 1 venceu')

    elif j2 == 'ataque' and j1 == 'pedra' or j2 == 'pedra' and j1 == 'papel' or j2 == 'ataque' and j1 == 'papel':
        print('Jogador 2 venceu')
