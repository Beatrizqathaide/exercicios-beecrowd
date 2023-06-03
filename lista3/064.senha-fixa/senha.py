#Escreva um programa que continue lendo uma senha até que ela seja válida. Para cada senha errada lida, escreva a mensagem "Senha inválida". Quando a senha for digitada corretamente imprima a mensagem "Acesso Permitido" e finalize o programa. A senha correta é o número 2002.

senhaValida = 2002

while True:
    senha = int(input())

    if senha != senhaValida:
        print('Senha Inválida')
    
    elif senha == senhaValida:
        print('Acesso Permitido')
        break