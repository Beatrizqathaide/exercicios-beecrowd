#Escreva um programa que leia duas notas de um aluno. Calcule e imprima a média dessas pontuações. Seu programa deve aceitar apenas pontuações válidas [0..10]. Cada pontuação deve ser validada separadamente.


notas = []

while True:
    nota = float(input())

    if len(notas) <=2:
        if nota < 0 or nota > 10:
            print('nota invalida')
        else:
            notas.append(nota)

    if len(notas) == 2:
        break

media = (notas[0] + notas[1]) / len(notas)

print(f'media = {media}')
