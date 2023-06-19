'''
A fabricação de presentes de Natal é uma tarefa muito complicada. Várias vezes os duendes ficam acordados até tarde trabalhando para que tudo seja feito no prazo e com perfeição.

Para administrar melhor sua agenda, os leprechauns estipularam quantos minutos levariam para fabricar cada presente.

É quase fim do dia e um dos leprechauns pediu sua ajuda.

Faltam N minutos para o tempo acabar, e há dois presentes restantes para o elfo Ed fabricar. Ajude-o a descobrir se ele conseguirá fabricar os dois presentes hoje ou se deve atrasar o trabalho para o dia seguinte.

Entrada
Cada caso de teste começa com um inteiro N, indicando quantos minutos faltam para a hora de ir embora (2 <= N <= 100).

A seguir, haverá dois inteiros A e B, indicando quantos minutos leva para fabricar cada um dos dois presentes que Ed precisa fabricar (1 <= A, B <= 100).

Saída
Imprima uma linha, contendo a instrução "Farei hoje!" se é possível fabricar os dois brindes antes da hora de ir embora, ou "Deixa para amanha!" de outra forma.
'''

m = int(input())

a, b = map(int, input().split())
r = a + b

if r > m:
    print('Deixa para amanha!')
else:
    print('Farei hoje!')