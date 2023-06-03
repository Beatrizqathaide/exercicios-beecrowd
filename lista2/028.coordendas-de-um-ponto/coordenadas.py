#Escreva um algoritmo que leia dois valores flutuantes (x e y), que devem representar as coordenadas de um ponto em um plano. Em seguida, determine a qual quadrante o ponto pertence, ou se você está em um dos eixos cartesianos ou na origem (x = y = 0).

#Se o ponto estiver na origem, escreva a mensagem "Origem".

#Se o ponto estiver no eixo X escreva "Eixo X", senão se o ponto estiver no eixo Y escreva "Eixo Y".

x, y = input().split(' ')

x = float(x)
y = float(y)

if x == 0 and y == 0:
    print('Origem')
elif x == 0 and y != 0:
    print('Eixo Y')
elif x != 0 and y == 0:
    print('Eixo X')
elif x > 0 and y > 0:
    print('Q1')
elif x < 0 and y > 0:
    print('Q2')
elif x < 0 and y < 0:
    print('Q3')
elif x > 0 and y < 0:
    print('Q4')