#O Joãozinho quer calcular e mostrar a quantidade de litros de combustível gasto em uma viagem, usando um carro que faz 12 Km/L. Para isso, ele gostaria que você o ajudasse através de um programa simples. Para realizar o cálculo, é necessário ler o tempo gasto (em horas) e a mesma velocidade média (km/h). Desta forma, você pode obter a distância e, em seguida, calcular quantos litros seriam necessários. Mostre o valor com três casas decimais após o ponto.

tempo = int(input('Tempo: '))
velocidade = int(input('Velocidade: '))

litros = tempo * velocidade / 12

print(f'{litros:.3f}')