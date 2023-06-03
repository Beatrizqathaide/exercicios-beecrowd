#Leia três valores (variáveis A, B e C), que são as notas dos três alunos. Em seguida, calcule a média, considerando que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5. Considere que cada nota pode ir de 0 a 10,0, sempre com uma casa decimal.

a = float(input('Primeira nota: '))
b = float(input('Segunda nota: '))
c = float(input('Terceira nota: '))

media = ((a * 2) + (b * 3) + (c * 5)) / 10

print(f'MÉDIA = {media:.1f}')