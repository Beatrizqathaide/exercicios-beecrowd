'''
Leia um número inteiro que é o número de código para discagem telefônica. Em seguida, imprima o destino de acordo com a tabela a seguir:

Se o número de entrada não for encontrado na tabela acima, a saída deve ser:
DDD não cadastrado
Isso significa “DDD não encontrado” em português.
'''

num = int(input())

ddd = {
        61: 'Brasilia', 
        71: 'Salvador', 
        11: 'Sao Paulo', 
        21: 'Rio de Janeiro', 
        32: 'Juiz de Fora', 
        19: 'Campinas', 
        27: 'Vitoria', 
        31: 'Belo Horizonte'
}


if num not in ddd:
    print('DDD não encontrado')
else:
    for k, v in ddd.items():
        if k == num:
            print(v)