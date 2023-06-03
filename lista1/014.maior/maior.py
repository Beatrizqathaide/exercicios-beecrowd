#Faça um programa que leia 3 valores inteiros e apresente o maior seguido da mensagem "eh o maior". Use a seguinte fórmula: (a+b+abs(a-b)) / 2

a, b, c = input().split(' ') #entrada de 3 variáveis de uma vez na mesma linha separadas por espaço

#tranforma a variável no formato desejado
a = int(a)
b= int(b)
c = int(c)

maiorAB = (a + b + abs(a - b)) / 2 

maiorC = (maiorAB + c + abs(maiorAB - c)) / 2

print(f'{maiorC} eh o maior')