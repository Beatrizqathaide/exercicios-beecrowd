'''
Neste problema, sua tarefa é ler um array A[100]. Ao final, imprima todas as posições do array que armazenam um número 
menor ou igual a 10 e o número armazenado nessa posição.
'''

for c in range(0, 100):
    num = input()
    num = float(num)

    if num <= 10:
        num = float(num)
        print(f'A[{c}] = {num:.1f}')
