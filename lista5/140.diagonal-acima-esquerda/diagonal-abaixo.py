'''
Lê um caractere maiúsculo que indica uma operação que será realizada em um array M [12][12]. Em seguida, calcule e imprima a soma ou média considerando apenas os números que estão acima da diagonal principal do array, conforme a figura a seguir (área verde).

Entrada
A primeira linha da entrada contém um único caractere maiúsculo O ('S' ou 'M'), indicando a operação Soma ou Média (Média em português) a ser realizada com os elementos do array. Siga 144 números de ponto flutuante da matriz.

Saída
Imprima o resultado calculado (soma ou média), com um dígito após a vírgula.
'''

o = input().upper()

matriz = []

for l in range(0, 12):
    linha = []
    for c in range(0, 12):
        linha.append(float(input()))
    matriz.append(linha)
    
soma = 0

for l in range(0, 12):
    for c in range(0, 12):
        if c < l:
            soma += matriz[l][c]

media = soma / 66

if o == 'S':
    print(f'{soma:.1f}')

elif o == 'M':
    print(f'{media:.1f}')