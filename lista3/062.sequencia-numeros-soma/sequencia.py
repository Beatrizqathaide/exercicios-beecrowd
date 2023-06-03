#Ler um número indeterminado de pares de valores M e N (parar quando algum desses valores for menor ou igual a zero). Para cada par, imprima a sequência do menor para o maior (incluindo ambos) e a soma de inteiros consecutivos entre eles (incluindo ambos).

soma = 0
temp = 0

while True:
    m, n = map(int, input().split(' '))

    if m <= 0 or n <= 0:
        break

    if n < m:
        temp = n
        n = m
        m = temp

    for num in range(m, n + 1):
        print(num, end=' ')
        soma += num

    print(f'Sum={soma}')
    soma = 0