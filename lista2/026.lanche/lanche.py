#Usando a tabela a seguir, escreva um programa que leia um código e a quantidade de um item. Após, imprima o valor a pagar. Este é um programa muito simples com o único intuito de praticar comandos de seleção.

'''
1 -  cahorro quente  - R$4,00
2 -  x-salada        - R$4,50
3 -  x-bacon         - R$5,00
4 -  torrada simples - R$2,00
5 -  refrigerante    - R$1,50
'''
x, y = input().split(' ')

x = int(x) #codigo
y = int(y) #quantidade

if x == 1:
    total = 4.00 * y
elif x == 2:
    total = 4.50 * y
elif x == 3:
    total = 5.00 * y
elif x == 4:
    total = 2.00 * y
elif x == 5:
    total = 1.50 * y

print(f'Total: R$ {total:.2f}')