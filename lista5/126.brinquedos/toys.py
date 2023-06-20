'''
Papai Noel lê cartas de Natal todos os anos para saber o que dar a cada criança. O problema é que muitas crianças não mandam cartas para o Papai Noel, então ele decidiu que, para economizar tempo, vai dar o mesmo presente para as crianças que não enviaram cartas. Então ele decidiu que para as crianças que são meninos vai dar um carrinho de brinquedo e para as meninas uma boneca.

Entrada
A primeira linha da entrada tem um inteiro N (0 < N ≤ 1000), o número de crianças que não enviaram a carta ao Papai Noel. As próximas N linhas consistem em duas strings, a primeira é o nome da criança e a segunda é uma letra, que pode ser 'M', para dizer que é um menino, ou 'F' se for uma menina.

Saída
A saída consiste em 2 linhas. Na primeira linha deve constar a quantidade de carrinhos que o Papai Noel deve fazer, seguido da palavra "carrinhos", e na segunda linha, a quantidade de bonecos seguida da palavra "bonecas".
'''

n = int(input())

c = 0
b = 0

for t in range(0, n):
    cr, s = map(str, input().split())

    if s== 'M':
        c += 1

    if s == 'F':
        b += 1

print(c, 'carrinhos')
print(b, 'bonecas')