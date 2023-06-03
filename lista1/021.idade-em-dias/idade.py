#Ler um valor inteiro correspondente à idade de uma pessoa (em dias) e imprimi-lo em anos, meses e dias, seguido de sua respectiva mensagem “ano(s)”, “mes(es)”, “dia(s)”.

#Nota: apenas para facilitar o cálculo, considere o ano inteiro com 365 dias e 30 dias todos os meses. Nos casos de teste nunca haverá uma situação que permita 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício para testar raciocínio matemático simples.

idade = int(input('Idade em dias: '))

ano = int(idade / 365) #dividir pela quantidade de dias que o ano tem
resto = idade % 365 #pega o resto da divisão do ano
mes = int(resto / 30) #dividir o resto da divisão do ano pela quantidade de dias que o mês tem
dia = resto % 30 #pega o resto da divisão que é a quantidade de dias

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dia} dia(s)')
