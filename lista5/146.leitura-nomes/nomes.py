'''
Seu professor gostaria de fazer um programa com as seguintes características:

Leia 10 nomes, sem espaços;
Imprima o terceiro nome da lista;
Imprima o sétimo nome da lista;
Imprima o nono nome da lista.
Entrada
A entrada consiste em vários arquivos de teste. Cada arquivo de teste tem dez linhas. Cada linha tem um nome de no máximo 30 caracteres e sem espaço. Conforme mostrado no exemplo de entrada a seguir.

Saída
Para cada arquivo na entrada, você tem um arquivo de saída. O arquivo de saída tem três linhas de acordo com os procedimentos 2, 3 e 4. Conforme mostrado no exemplo de saída a seguir.
'''

while True:

    try:
        n = []

        for c in range(0, 10):
            n.append(input())

            if c == 2:
                t = n[c]

            if c == 6:
                s = n[c]

            if c == 8:
                o = n[c]

        print(t)
        print(s)
        print(o)
    
    except EOFError:
        break