#Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas em um mês e o valor que ele recebeu por hora. Imprima o número do funcionário e o salário que ele receberá no final do mês, com duas casas decimais.

#Não se esqueça de imprimir o final da linha após o resultado, caso contrário você receberá “Erro de apresentação”.
#Não se esqueça do espaço antes e depois do sinal igual e depois do U$.

number = int(input('Número do Funcionário: '))
horas_trabalhadas = int(input('Horas trabalhadas: '))
valor_hora = float(input('Valor recebido por hora trabalhada: '))
salary = horas_trabalhadas * valor_hora

print(f'NUMBER = {number}')
print(f'SALARY = U$ {salary:.2f}')
