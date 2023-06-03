#Neste problema você precisa ler 15 números e deve colocá-los em dois arrays diferentes: par se o número for par ou impar se este número for ímpar. Mas o tamanho de cada uma das duas matrizes é de apenas 5 posições. Então toda vez que você preencher um dos dois arrays, você deve imprimir o array inteiro para poder usá-lo novamente para os próximos números que forem lidos. Ao final, todos os números restantes de cada um desses dois arrays devem ser impressos começando pelo array ímpar. Cada array pode ser preenchido quantas vezes forem necessárias.

par = []
impar = []

for c in range(0, 15):
    num = int(input())

    if num % 2 == 0:
        par.append(num)
        
        if len(par) == 5:
            for i in range(0, 5):
                print(f'par[{i}] = {par[i]}')
            
            par.clear()
        
    else:
        impar.append(num)
        
        if len(impar) == 5:
            for a in range(0, 5):
                print(f'impar[{a}] = {impar[a]}')
            
            impar.clear()

for a in range(0, len(impar)):
    print(f'impar[{a}] = {impar[a]}')

for i in range(0, len(par)):
    print(f'par[{i}] = {par[i]}')