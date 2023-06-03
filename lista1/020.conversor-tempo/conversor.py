#Ler um valor inteiro, que é a duração em segundos de um determinado evento em uma fábrica, e informá-lo expresso em horas:minutos:segundos.


valor = int(input('Digite o valor: '))

horas = int(valor / 3600) #1 hora tem 3600 segundos
resto = valor % 3600 #pega o restao de segundos que sobraram das horas
minutos = resto // 60 #
segundos = valor % 60

print(f'{horas}:{minutos}:{segundos}')