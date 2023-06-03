# Faça um programa que leia o nome de um vendedor, seu salário fixo e o total da venda feita por ele mesmo no mês (em dinheiro). Considerando que este vendedor recebe 15% sobre todos os produtos vendidos, escreva o salário final (total) deste vendedor ao final do mês, com duas casas decimais.

# - Não esqueça de imprimir o final da linha após o resultado, caso contrário você receberá “Erro de apresentação”.

# - Não se esqueça dos espaços em branco.

vendedor = input('Nome: ')
salario = float(input('Salário fixo: R$'))
vendas = float(input('Total da venda no mês: R$'))
total = (vendas * 15 / 100) + salario

print(f'TOTAL = R$ {total:.2f}')