'''
Tio Patinhas era um milionário que morava em sua mansão, e tinha três sobrinhos: Huguinho, Zezinho e Luisinho. Ele se confundia facilmente entre os três sobrinhos porque eram muito parecidos, apesar das idades diferentes. Um dia, os três fizeram uma aposta com o tio: se ele adivinhasse quem era o sobrinho do meio, ou seja, nem o mais novo nem o mais velho, dariam a ele uma moeda de ouro e, se errasse, teria que dar a cada um. um uma moeda de ouro. Então o tio pede sua ajuda para ganhar essa aposta

Entrada
A entrada consiste em vários casos de teste. Cada caso contém três valores inteiros H , Z e L , que representam as idades de Huguinho, Zezinho e Luisinho, respectivamente.

Saída
Para cada caso de teste imprima o nome do sobrinho do meio em letras minúsculas.
'''

h, z, l = map(int, input().split())

#zezinho
if h > z and z > l or h < z and z < l:
    print('zezinho')

#huguinho
elif z > h and h > l or z < h and h < l:  
    print('huguinho')

#luisinho
else:
    print('luisinho')

