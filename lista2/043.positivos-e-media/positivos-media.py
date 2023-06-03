#Leia 6 valores que podem ser números de ponto flutuante. Após, imprima quantos deles foram positivos. Na próxima linha, imprima a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

positivos = 0
soma = 0

for c in  range(0, 6):
    num = float(input())
    if num > 0:
        positivos += 1
        soma += num

media = soma / positivos
print(f'{positivos} valores positivos')
print(f'{media:.1f}')