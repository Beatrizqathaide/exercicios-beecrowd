'''
Escreva um programa para ler duas partituras de um aluno. Calcule e imprima a média semestral. O programa deve aceitar apenas pontuações válidas (uma pontuação deve caber no intervalo [0,10]). Cada pontuação deve ser validada separadamente.

O programa deve imprimir uma mensagem "novo calculo (1-sim 2-nao)" que significa "novo calculo (1-sim 2-não)". Após, a entrada será (1 ou 2). 1 significa um novo cálculo, 2 significa que a execução deve ser finalizada.
'''
continua = 1
notas = []

while True:
    if continua == 1:
        while True:
            nota = float(input())

            if len(notas) <= 2:
                if nota < 0 or nota > 10:
                    print('nota invalida')
                else:
                    notas.append(nota)

            if len(notas) == 2:
                break

        media = (notas[0] + notas[1]) / len(notas)

        print(f'media = {media:.2f}')
        notas = []

    continua = int(input('novo calculo (1-sim 2-nao)'))
    if continua == 2:
        break