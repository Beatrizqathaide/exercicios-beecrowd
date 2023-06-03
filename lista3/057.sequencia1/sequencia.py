#Faça um programa que imprima a sequência como no exemplo a seguir.

i = 1
j = 60
print(f'I={i} J={j}')

while True:
    i += 3
    j -= 5
    print(f'I={i} J={j}')
    if j == 0:
        break