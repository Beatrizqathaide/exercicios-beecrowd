'''
Sua tarefa neste problema é ler um número que é uma coluna de um array onde uma operação será realizada, um caractere maiúsculo, indicando a operação a ser realizada e todos os elementos de um array bidimensional M [12][12 ] . Então, você deve calcular e imprimir a soma ou média de todos os elementos dentro da área verde de acordo com o caso. A figura a seguir ilustra o caso em que se insere o número 5 na coluna do array, mostrando todos os elementos que devem ser considerados na operação.

Entrada
A primeira linha da entrada contém um inteiro simples C (0 ≤ C ≤ 11) indicando a coluna a ser considerada na operação. A segunda linha da entrada contém um único caractere maiúsculo T ('S' ou 'M'), indicando a operação Soma ou Média (Média em português) a ser realizada com os elementos do array. Siga 144 números de ponto flutuante da matriz.

Saída
Imprima o resultado calculado (soma ou média), com um dígito após a vírgula.
'''

n = int(input()) 

operacao = input() 

matriz = [] 

for l in range(0, 12):
    linha = [] 
    for c in range(0, 12):
        linha.append(float(input()))
    matriz.append(linha)

soma = 0

for l in range(0, 12):
    soma += matriz[l][n]

if operacao == 'S':
    resultado = soma

elif operacao == 'M':
    resultado = soma / 12

print(f'{resultado:.1f}')