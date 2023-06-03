#Leia um valor de ponto flutuante com duas casas decimais. Isso representa um valor monetário. Depois disso, calcule o menor número possível de notas e moedas em que o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0,50, 0,25, 0,10, 0,05 e 0,01. Imprima a mensagem “NOTAS:” seguida da lista de notas e a mensagem “MOEDAS:” seguida da lista de moedas.

num = float(input())

notas = [100, 50, 20, 10, 5, 2]

print('NOTAS:')
for nota in notas:
    quantidadeNotas = int(num / nota)
    print(f'{quantidadeNotas} nota(s) de R$ {nota:.2f}')
    num -= quantidadeNotas * nota

moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('MOEDAS:')
for moeda in moedas:
    quantidadeMoedas = int(round(num, 2)/ moeda)
    print(f'{quantidadeMoedas} moeda(s) de R$ {moeda:.2f}')
    num -= quantidadeMoedas * moeda