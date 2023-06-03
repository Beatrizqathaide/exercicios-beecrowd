#O programa deve ler um inteiro X vezes indefinidas (parar quando X=0). Para cada X, imprima a soma de cinco números pares consecutivos de X, incluindo-o se X for par. Se o número de entrada for 4, por exemplo, a saída deve ser 40, que é o resultado da operação: 4+6+8+10+12. Se o número de entrada for 11, por exemplo, a saída deve ser 80, que é o resultado de 12+14+16+18+20.

while True:
    x = int(input())
    if x == 0:
        break

    if x % 2 != 0:
        x = x + 1

    soma = 0
    for c in range(0, 5):
        soma += x
        x += 2
    print(soma)
