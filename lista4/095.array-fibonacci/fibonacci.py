#Escreva um programa que leia um número e imprima o número de Fibonacci correspondente a este número lido. Lembre-se que os primeiros elementos da série de Fibonacci são 0 e 1 e cada termo seguinte é a soma dos dois anteriores. Todos os números de Fibonacci calculados neste programa devem caber em um número de 64 bits sem sinal.

t = int(input())

for i in range(0, t):

    n = int(input())
    
    if n > 1:
      t1 = 0
      t2 = 1
      
      for c in range(2, n + 1):
        
        t3 = t1 + t2
            
        t1 = t2
        t2 = t3

    elif n == 0:
      t3 = 0
    
    elif n == 1:
        t3 = 1
        
    print(f'Fib({n}) = {t3}')
