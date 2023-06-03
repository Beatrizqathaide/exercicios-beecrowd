#Escreva um programa que leia um array N [20]. Depois, troque o primeiro elemento pelo último, o segundo elemento pelo penúltimo, etc., Até trocar o 10º pelo 11º. imprima a matriz modificada.

numeros = []
for c in range(0, 5):
    num = int(input())
    numeros.append(num)

cont = 0
for n in range(len(numeros) - 1, -1, -1):
    print(f'N[{cont}] = {numeros[n]}')
    cont += 1
