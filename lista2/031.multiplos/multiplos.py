'''Leia dois valores inteiros (A e B). Após, o programa deve imprimir a mensagem “Sao Multiplos” (são múltiplos) ou “Nao são Multiplos” (não são múltiplos), correspondente aos valores lidos.'''

a, b = input().split(' ')

a = int(a)
b = int(b)

if b % a == 0 or a % b == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')