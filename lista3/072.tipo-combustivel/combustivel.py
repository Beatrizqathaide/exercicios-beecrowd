#Um posto de gasolina deseja determinar qual de seus produtos é a preferência de seus clientes. Escreva um programa para ler o tipo de combustível fornecido (codificado da seguinte forma: 1. Álcool 2. Gasolina 3. Diesel 4. Fim). Se você inserir um código inválido (fora do intervalo de 1 a 4), um novo código deverá ser solicitado. O programa terminará quando o código inserido for o número 4.

combustivel = 0
alcool = 0
gasolina = 0
diesel = 0

while combustivel != 4:
    combustivel = int(input(''))

    if combustivel == 1:
        alcool += 1
    
    if combustivel == 2:
        gasolina += 1
    
    if combustivel == 3:
        diesel += 1
    
print('MUITO OBRIGADO')
print(f'Alcool: {alcool}')
print(f'Gasolina: {gasolina}')
print(f'Diesel: {diesel}')
