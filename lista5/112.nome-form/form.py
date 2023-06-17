'''
O preenchimento de formulários é uma tarefa simples. Mas é necessário verificar se o espaço reservado para dados é grande o suficiente.

Sua tarefa é, dada uma linha de texto, indicar se ela cabe em um formulário de 80 caracteres.

Entrada
A entrada é uma linha de texto L (1 ≤ |L| ≤ 500).

Saída
A saída é dada em uma única linha. Deve ser "SIM" (sem aspas) se a linha de texto L tiver até 80 caracteres. Se L tiver mais de 80 caracteres, a saída deve ser "NÃO".
'''

l = input()

if len(l) > 80:
    print('NO')
else:
    print('YES')