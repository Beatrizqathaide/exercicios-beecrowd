'''
Larissa é uma estudiosa muito inteligente e estudiosa, por isso se dedica a diversas atividades. O final do ano, mês de sua última apresentação, chegou. Ela, muito ocupada, precisa saber se pode realizar sua apresentação antes do Natal! Mas antes de sua apresentação ela deve passar por uma checagem com seu conselheiro oriental, Prof. Takanada

Entrada
A entrada é composta por um    valor E (0 < E < 25) que representa o dia em que a tese final foi entregue para verificação. Um valor   D (0 < D < 25)   representando a data final a ser enviada para verificação.

Saída
Mostre, para cada caso de teste, se o acadêmico fará a apresentação ou não. A única possibilidade da entrega não ser realizada na data é por falta de orientação da Takanada. Caso não seja possível, imprima "Eu odeio a professora!". Se for entregue até 3 dias antes do prazo, imprima "Muito bem! Apresenta antes do Natal!", Caso contrário, estando muito próximo do prazo, imprima "Parece o trabalho do meu filho!", Neste último caso, é acrescentado mais dois dias para correções, e se a data final for menor que a véspera do Natal (24), pode ser apresentado, devendo ser impresso "TCC Apresentado!"", caso contrário imprima "Reprovado! Entao eh nataaaaal!".
'''

while True:
    try:

        e, d = map(int, input().split())

        if e <= d - 3:
            print('Muito bem! Apresenta antes do Natal!')

        elif e == d - 1:
            print('Parece o trabalho do meu filho!')
            d += 2
            if d <= 24:
                print('TCC Apresentado!')
            else:
                print('Fail! Entao eh nataaaaal!')

        else:
            print('Eu odeio a professora!') 
            
    except EOFError:
        break