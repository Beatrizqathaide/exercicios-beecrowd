'''
As sequências Iccanobif são sequências em que cada termo é sempre igual à soma dos próximos dois subsequentes a ele. Exceto pelos dois últimos termos que são sempre iguais a 1

Exemplo de uma sequência Iccanobif com 10 termos: 55, 34, 21, 13, 8, 5, 3, 2, 1, 1.

Sua tarefa é, dado um valor inteiro, imprimir a sequência Iccanobif de tamanho correspondente.

Entrada
A entrada consiste em um único inteiro N (1 ≤ N ≤ 40) representando o tamanho da sequência Iccanobif desejada.

Saída
A saída consiste em uma única linha contendo os termos da sequência Iccanobif de tamanho N separados por um único espaço.
'''

n = int(input())

t1 = 1
t2 = 1

f = [t1, t2]

for i in range(0, n - 2):
    t3 = t1 + t2

    f.append(t3)

    t1 = t2
    t2 = t3

for c in range(len(f) - 1, - 1, -1):
    
    if c == 0:
        print(f[c])
    
    else:
        print(f[c], end=' ')


