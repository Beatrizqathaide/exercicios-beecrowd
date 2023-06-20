'''
John é um estudante de matemática, mas poucas pessoas sabem disso. Um dia, um de seus colegas, pensando que John não sabia conceitos básicos de matemática, desafiou-o a realizar um cálculo simples que era: Calcule o resto da divisão de A ÷ B.

Como John é muito tímido e vocês são melhores amigos, ele informou qual era a resposta para o problema e pediu que você passasse essa informação para esse colega que o desafiou. Você consegue ?

Dados dois inteiros A e B, diga qual é o resto da divisão de A ÷ B que John passou para você.

Entrada
A entrada contém dois inteiros A e B (1 <= A, B <= 100000).

Saída
A saída contém um único inteiro que é o resto da divisão de A ÷ B.
'''

a = int(input())

b = int(input())

r = a % b

print(r)