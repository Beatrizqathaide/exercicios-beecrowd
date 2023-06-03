#Escreva um algoritmo para ler um valor A e um valor N. Imprima a soma de N números de A (inclusive). Enquanto N for negativo ou ZERO, um novo N (somente N) deve ser lido. Todos os valores de entrada estão na mesma linha.

valores = input().split()

a = int(valores[0])
n = int(valores[-1])

soma = 0

for c in range(0, n):
    soma = soma + a + c

print(soma)
