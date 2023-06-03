#Ler quatro números (N1, N2, N3, N4), sendo um deles com 1 dígito após a vírgula, correspondendo a 4 notas obtidas por um aluno. Calcule a média com pesos 2, 3, 4 e 1 respectivamente, para essas 4 pontuações e imprima a mensagem "Mídia: " (Média), seguida do resultado calculado. Se a média foi 7,0 ou mais, imprima a mensagem "Aluno aprovado". (Aluno aprovado). Se a média foi inferior a 5,0, imprima a mensagem: "Aluno reprovado". (Aluno Reprovado). Se a média ficou entre 5,0 e 6,9, incluindo estes, o programa deve imprimir a mensagem "Aluno em exame". (Estudante em exame).

#Em caso de exame, leia mais uma pontuação. Imprima a mensagem "Nota do exame: " (Pontuação do exame) seguida da nota digitada. Recalcule a média (soma a nota do exame com a média calculada anteriormente e divida por 2) e imprima a mensagem “Aluno aprovado”. (Aluno aprovado) em caso de média igual ou superior a 5,0) ou "Aluno reprovado". (Aluno reprovado) em caso de média igual ou inferior a 4,9. Para estes 2 casos (aprovados ou reprovados após o exame) imprima a mensagem "Mídia final: " (Média final) seguida da média final deste aluno na última linha.

n1, n2, n3, n4 = input().split(' ')
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
print(f'Media: {media:.1f}')

if media >= 7 or media == 10:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
elif media >= 5 or media <= 6.9:
    print('Aluno em exame.')
    n5 = float(input())
    print(f'Nota do exame: {n5}')
    mediaExame = (media + n5) / 2
    if mediaExame >= 5:
        print('Aluno aprovado.')
    if mediaExame <= 4.9:
        print('Aluno reprovado.')
    print(f'Media final: {mediaExame:.1f}')