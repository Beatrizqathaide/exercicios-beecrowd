#Escreva um programa para ler as coordenadas (X, Y) de um número indeterminado de pontos no sistema cartesiano. Para cada ponto escreva o quadrante ao qual ele pertence. O programa termina quando pelo menos uma das duas coordenadas é NULL (nesta situação sem escrever nenhuma mensagem).

while True:
    x, y = input().split()

    x = int(x)
    y = int(y)

    if x > 0 and y > 0:
        print('primeiro')
    
    elif x < 0 and y > 0:
        print('segundo')
    
    elif x < 0 and y < 0:
        print('terceiro')
    
    elif x > 0  and y < 0:
        print('quarto')
    
    else:
        break