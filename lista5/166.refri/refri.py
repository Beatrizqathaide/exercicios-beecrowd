'''
Tim é um bebedor de refrigerante absolutamente obsessivo, ele simplesmente não consegue o suficiente. O mais irritante é que ele quase nunca tem dinheiro, então sua única maneira legal óbvia de obter mais refrigerante é pegar o dinheiro que ganha quando recicla garrafas de refrigerante vazias para comprar novas. Além das garrafas vazias resultantes do seu próprio consumo, por vezes encontra garrafas vazias na rua. Um dia ele estava com muita sede, então ele realmente bebeu refrigerantes até não poder comprar um novo.

Entrada
Três inteiros não negativos E , F , C , onde E  < 1000 é igual ao número de garrafas de refrigerante vazias na posse de Tim no início do dia, F  < 1000 o número de garrafas de refrigerante vazias encontradas durante o dia e 1 < C < 2.000 o número de garrafas vazias necessárias para comprar um novo refrigerante.

Saída
Quantos refrigerantes Tim bebeu em seu dia de sede extra?
'''


e, f, c = map(int, input().split())

total = e + f
garrafas = 0

while total >= c:
    total -= c
    total += 1
    garrafas += 1

print(garrafas)