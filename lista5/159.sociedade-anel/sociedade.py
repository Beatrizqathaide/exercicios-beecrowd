'''
Frodo era um pequeno hobbit (pessoas pequenas e com pés peludos) que vivia tranquilamente no Condado, tomando seus vários cafés da manhã repletos de muitas comidas suculentas que uma boa dieta hobbit fornece.
Um dia seu tio Bilbo entrega a ele seu famoso anel de ouro, e Gandalf, um mago muito "legal", diz a Frodo que esse anel não era normal e deveria ser jogado na Montanha da Perdição, para que um grande mal fosse evitado. Para esta jornada, uma comitiva foi formada, composta por anões, elfos, humanos, hobbits e magos.
Frodo quer saber a quantidade de cada raça que irá com ele para a jornada. Dada uma lista de pessoas que se alistaram, informe Frodo da comitiva.

Entrada

A primeira linha da entrada é composta por um inteiro N (0 < N <= 10), indicando o número de pessoas que se alistaram. Cada uma das próximas N Next linhas são compostas por uma string (sem espaços e apenas de caracteres alfanuméricos) e uma maiúscula, indicando, respectivamente, o nome e o tipo da raça do respectivo ser. Este personagem pode ser:
● A - Para anões;
● E - Para elfos;
● H - Para humanos;
● M - Para mágicos;
● X - Para hobbits (X, pois todo hobbit é um mistério para o mundo).
Saída
Deverá ser apresentado um relatório com a comitiva de Frodo, indicando em cada linha quantos seres de cada espécie estarão na viagem, seguindo a ordem: hobbits, humanos, elfos, anões e mágicos (em português).
'''

n = int(input())

a = 0
e = 0
h = 0
m = 0
x = 0

for c in range(0, n):
    criatura = input()
        
    if criatura[len(criatura) - 1] == 'A':
        a += 1
    
    elif criatura[len(criatura) - 1] == 'E':
        e += 1

    elif criatura[len(criatura) - 1] == 'H':
        h += 1

    elif criatura[len(criatura) - 1] == 'M':
        m += 1

    elif criatura[len(criatura) - 1] == 'X':
        x += 1

print(f'{x} Hobbit(s)')
print(f'{h} Humano(s)')
print(f'{e} Elfo(s)')
print(f'{a} Anao(oes)')
print(f'{m} Mago(s)')