#Leia os valores de dois pontos flutuantes de precisão dupla A e B, correspondentes às notas de dois alunos. Após isso, calcule a média do aluno, considerando que a nota A tem peso 3,5 e B tem peso 7,5. Cada nota pode ser de zero a dez, sempre com um dígito após a vírgula. Não se esqueça de imprimir o final da linha após o resultado, caso contrário você receberá “Erro de apresentação”. Não se esqueça do espaço antes e depois do sinal de igual.

nota1 = float(input('Digite a 1° Nota: '))
nota2 = float(input('Digite a 2° Nota: '))
media = ((nota1 * 3.5) + (nota2 * 7.5)) / 11 #aqui se trata de uma média ponderada, por isso, soma os pesos e divide as notas pelo total de pesos
print(f'MEDIA = {media:.5f}')