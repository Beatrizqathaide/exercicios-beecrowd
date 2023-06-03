'''
Você conseguiu dois cabos circulares de energia. A primeira tem raio R1 e a segunda R2. Você precisa comprar um conduíte circular (veja a imagem abaixo) que caiba nesses dois cabos:

Qual é o menor raio de um conduíte que você precisa comprar? Em outras palavras, dados dois círculos, qual é o menor raio de um terceiro círculo que circunscreve os outros dois?

Entrada
Na primeira linha há um inteiro T (T ≤ 10000), indicando o número de casos de teste.

Na única linha de cada caso de teste teremos os dois inteiros R1 e R2 indicando o raio dos cabos. Os inteiros serão positivos e toda a matemática caberá em um inteiro regular de 32 bits.
Saída
Em cada caso de teste, imprima a resposta em uma única linha.
'''


t = int(input())

for c in range(0, t):
    r1, r2 = map(int, input().split())
    res = r1 + r2
    print(res)
