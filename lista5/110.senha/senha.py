'''
O Sr. Amnésio tinha muita dificuldade em guardar senhas. Para lembrá-los, ele sempre usava números, e escrevia em pedaços de papel, que também se perdiam com facilidade, fazendo com que precisasse trocar a senha toda vez que isso acontecia. Cansado, pensou de uma forma mais prática: colocava no papel o próximo número da senha, então usava sempre a mesma conta para lembrar a senha com base no número escrito no papel. Mas ele também esqueceu a fórmula, portanto, pediu que você escrevesse um programa que, dado o número do papel, digitasse a senha correspondente. Escreva um programa que, dado um número, digite sua senha.

Entrada
A entrada terá muitos casos de teste. Cada caso de teste terá um número N, representando o número escrito no papel (1001 ≤ N ≤ 9999). A entrada termina com o fim do arquivo.

Saída
Para cada caso de teste, imprima a senha correspondente. Em todos os casos, a fórmula será a mesma nos exemplos abaixo.
'''



while True:
    try:
        n = int(input())

        s = n - 1
        print(s)
    except EOFError:
        break