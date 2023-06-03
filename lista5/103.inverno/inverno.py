'''
Bem-vindo à Escola de Inverno de Erechim do Concurso ICPC Sub-regional Brasileiro! Esperamos sinceramente que aprendam muito nestes dias para que tenham muito sucesso nos concursos de Programação que estão por vir, mas acima de tudo esperamos que gostem da Escola, pois quando nos divertimos e nos divertimos estudando e programando, o treinamento deixa de ser um fardo e se torna um hobby. Então se divirta!

O inverno é uma estação maravilhosa, não é? Todos nós adoramos vestir um poncho, participar de uma roda de chimarrão, assar pinhões no fogão a lenha… Mas nem todo mundo gosta do inverno, principalmente em lugares onde o inverno costuma ser muito cruel. Em Westeros, por exemplo, o humor das pessoas é definido de acordo com as tendências climáticas. Com base nas temperaturas dos últimos três dias, as pessoas podem estar tristes ou alegres, sendo mais provável que façam guerra ou façam amor, respetivamente. E, sejamos sinceros, é justamente pelas cenas de amor e guerra que amamos Game of Thrones!

Se a temperatura diminuiu do 1º para o 2º dia, mas aumentou ou permaneceu constante do 2º para o 3º, as pessoas estão felizes (primeira figura).
Se a temperatura aumentou do 1º para o 2º dia, mas diminuiu ou permaneceu constante do 2º para o 3º, as pessoas ficam tristes (segunda figura).
Se a temperatura aumentou do 1º para o 2º dia e do 2º para o 3º, mas subiu do 2º para o 3º menos do que havia subido do 1º para o 2º, o povo fica triste (terceira figura).
Se a temperatura aumentou do 1º para o 2º dia e do 2º para o 3º, mas aumentou do 2º para o 3º pelo menos o que havia aumentado do 1º para o 2º, as pessoas ficam felizes (quarta figura).
Se a temperatura diminuiu do 1º para o 2º dia e do 2º para o 3º, mas diminuiu do 2º para o 3º menos do que havia diminuído do 1º para o 2º, as pessoas estão felizes (quinta figura).
Se a temperatura baixou do 1º para o 2º dia e do 2º para o 3º, mas diminuiu do 2º para o 3º pelo menos o que havia diminuído do 1º para o 2º, o povo fica triste (sexta figura).
Se a temperatura permaneceu constante do 1º ao 2º dia, as pessoas ficam felizes se a temperatura aumentou do 2º ao 3º ou tristes caso contrário (respectivamente, sétima e oitava cifras).
'''

a, b, c = map(int, input().split())

if a > b and b <= c:
    print(':)')

elif a < b and b >= c:
    print(':(')

elif a < b and b < c and c - b < b - a:
    print(':(')

elif a < b and b < c and c - b >= b - a:
    print(':)')

elif a > b and b > c and a - b > b - c:
    print(':)')

elif a > b and b > c and b - c >= b - c:
    print(':(')

elif a == b and b < c:
    print(':)')

else:
    print(':(')
