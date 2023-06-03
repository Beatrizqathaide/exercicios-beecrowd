#Neste problema você tem que ler um valor inteiro e calcular o menor número possível de notas em que o valor pode ser decomposto. As notas possíveis são 100, 50, 20, 10, 5, 2 e 1. Imprima o valor lido e a lista de notas.

valor = int(input('Digite um valor: R$ '))
resultado = valor
cont100 = 0
cont50 = 0
cont20 = 0
cont10 = 0
cont5 = 0
cont2 = 0
cont1 = 0

while resultado != 0:
    if resultado >= 100:
        resultado -= 100
        cont100 += 1
    
    elif resultado >= 50:
        resultado -= 50
        cont50 += 1

    elif resultado >= 20:
        resultado -= 20
        cont20 += 1
    
    elif resultado >= 10:
        resultado -= 10
        cont10 += 1
    
    elif resultado >= 5:
        resultado -= 5
        cont5 += 1

    elif resultado >= 2:
        resultado -= 2
        cont2 += 1
    
    elif resultado >= 1:
        resultado -= 1
        cont1 += 1

print(f'Valor digitado: {valor}')
print(f'{cont100} nota(s) de R$ 100,00')
print(f'{cont50} nota(s) de R$ 50,00')
print(f'{cont20} nota(s) de R$ 20,00')
print(f'{cont10} nota(s) de R$ 10,00')
print(f'{cont5} nota(s) de R$ 5,00')
print(f'{cont2} nota(s) de R$ 2,00')
print(f'{cont1} nota(s) de R$ 1,00')