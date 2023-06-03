#Calcule o consumo médio de um carro, fornecendo a distância total percorrida (em Km) e o total de combustível gasto (em litros).

quilometros = int(input('Quantidade de Quilômetros: '))
litros = float(input('Quantidade de Litros: '))

total = quilometros / litros

print(f'{total:.3f} km/l')