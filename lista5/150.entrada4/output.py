'''
Seu professor gostaria que você fizesse um programa com as seguintes características:

Crie vinte e seis inteiros;
Atribua à primeira variável o valor 97;
Atribuir as demais variáveis ​​ao valor da primeira soma de uma unidade;
Mostrar na tela os valores numéricos da primeira variável, um espaço no braço, o caractere 'e' , outro espaço em branco e seu valor alfanumérico (caracteres);
Repita para todas as outras variáveis.
Entrada
Não há.

Saída
O resultado do seu programa deve ser o mesmo que o exemplo de saída.
'''

a = 'abcdefghijklmnopqrstuvwxyz'

cont = 0

for c in range(97, 123):
    print(c, 'e', a[cont])
    cont += 1