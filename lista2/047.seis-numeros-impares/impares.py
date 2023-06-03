#Leia um valor inteiro X e imprima os 6 números ímpares consecutivos de X, um valor por linha, incluindo X se for o caso.

num = int(input())

for n in range(num, (num + 12)):
    if n % 2 != 0:
        print(n)