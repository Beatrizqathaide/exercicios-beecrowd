#Neste problema, a tarefa é ler um código de um produto 1, o número de unidades do produto 1, o preço de uma unidade do produto 1, o código de um produto 2, o número de unidades do produto 2 e o preço. para uma unidade de produto 2. Após isso, calcule e mostre o valor a ser pago.

'''total = 0
for c in range(0, 2):
    codigo = int(input('Código: '))
    unidades = int(input('Quantas unidades: '))
    preco = float(input('Preço: '))

    valor = preco * unidades
    total += valor
print(f'VALOR A PAGAR: R$ {total:.2f}')
'''
total = 0
for c in range(0, 2):
    codigo, unidades, preco = input().split(' ') #entrada de 3 variáveis de uma vez na mesma linha separadas por espaço
    codigo = int(codigo) #tranforma para o formato que eu quero
    unidades = int(unidades)
    preco = float(preco)

    valor = preco * unidades
    total += valor
print(f'VALOR A PAGAR: R$ {total:.2f}')