#Um número primo é um número que é divisível apenas por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, porque só pode ser dividido por 1 e por 7.

n = int(input())

for c in range(0, n):
    num = int(input())
    primo = 0
    for i in range(1, num + 1):
        if num % i == 0:
            primo += 1
        
    if primo == 2:
        print(f'{num} eh primo')
    else:
        print(f'{num} nao eh primo')