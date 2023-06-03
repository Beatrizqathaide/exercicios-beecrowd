'''
Leia um inteiro N (2 < N < 1000). Imprima a tabuada de multiplicação de N.
1 x N = N 2 x N = 2N ... 10 x N = 10N
'''

n = int(input())

for c in range(1, 11):
    print(f'{c} x {n} = {c * n}')