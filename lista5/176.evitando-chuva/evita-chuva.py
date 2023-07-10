'''
Rafael detesta chuva e para não se molhar passou a usar um sistema de previsão do tempo. Nesse sistema ele consegue prever se vai chover na hora que vai trabalhar e/ou na hora que volta do trabalho.

Rafael também detesta carregar guarda-chuva quando não está chovendo. Para evitá-lo, ele vai comprar vários guarda-chuvas e guardá-los
em casa e no escritório, e só vai usá-los quando estiver chovendo. Ou seja, se estiver chovendo na hora que ele for trabalhar, ele vai pegar um guarda-chuva que está em casa, usar no caminho para o trabalho e deixar lá. Da mesma forma, se estiver chovendo na hora que ele volta do trabalho, ele pega um guarda-chuva que está no escritório, usa na volta para casa e deixa lá.

Dadas as previsões meteorológicas, descubra quantos guarda-chuvas Rafael deve comprar e guardar em casa e no escritório, de forma que nunca se molhe e nunca tenha que carregar um guarda-chuva se não estiver chovendo.

Entrada
A primeira linha de entrada possui um inteiro N , indicando quantos dias foram previstos pelo sistema meteorológico (1 <= N <= 1000).

A seguir haverá N linhas, cada uma com duas palavras SD e SN , indicando a previsão do dia na hora que Rafael vai trabalhar, e na hora que Rafael volta do trabalho, respectivamente. Se a palavra for "sol", significa que a esta hora não vai chover, e se a palavra for "chuva", significa que a esta hora vai chover.

Saída
Para cada caso de teste, você deve imprimir uma linha com dois inteiros C e E , indicando quantos guarda-chuvas Rafael deve comprar e guardar em casa e no escritório.
'''

dias = int(input())

compraCasa = 0
compraTrabalho = 0
extraCasa = 0
extraTrabalho = 0

for c in range(0, dias):
    casa, trabalho = map(str, input().split())

    if casa == 'chuva' and extraCasa == 0:
        compraCasa += 1
        extraTrabalho += 1
    
    elif casa == 'chuva' and extraCasa > 0:
        extraCasa -= 1
        extraTrabalho += 1

    
    if trabalho == 'chuva' and extraTrabalho == 0:
        compraTrabalho += 1
        extraCasa += 1
    
    elif trabalho == 'chuva' and extraTrabalho > 0:
        extraTrabalho -= 1
        extraCasa += 1

print(compraCasa, compraTrabalho)