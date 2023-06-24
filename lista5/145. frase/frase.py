'''
Seu professor gostaria de fazer um programa com as seguintes características:

Leia uma frase que terá uma vírgula no meio do texto;
Imprima a primeira parte da frase;
Imprima a segunda parte da frase.
Entrada
A entrada consiste em vários arquivos de teste. Em cada arquivo de teste há uma linha. A linha contém uma frase com no máximo 100 caracteres (pode conter espaço em branco) e uma vírgula. Conforme mostrado no exemplo de entrada a seguir.

Saída
Para cada arquivo na entrada, você tem um arquivo de saída. O arquivo de saída tem duas linhas de acordo com as etapas 2 e 3. Conforme mostrado no exemplo de saída a seguir.
'''

while True:
    try:
        
        frase = input()

        d = frase.split(',')

        for c in d:
            print(c)
            
    except EOFError:
        break
