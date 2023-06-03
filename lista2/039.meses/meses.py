#Leia um número inteiro entre 1 e 12, inclusive. Correspondente a este número, deve-se imprimir o mês do ano, em inglês, com a primeira letra maiúscula.

mes = int(input())

meses = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

for k, v in meses.items():
    if mes == k:
        print(v)