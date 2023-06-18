'''
Todos em Nlogônia estão muito animados com a inauguração do Ricardo Barreiro World, o mais novo parque de diversões do país. Sua montanha-russa, a mais rápida do continente, está sendo amplamente divulgada na TV e no Rádio. É a atração que todos, desde as crianças até as vovós, querem pedalar.

Infelizmente, algumas restrições foram impostas pelo governo durante a homologação do atrativo. Por questões de segurança, há uma altura mínima e máxima que as pessoas devem ter para andar na montanha-russa.

No dia da inauguração, cada convidado preencheu um cadastro no qual indicava sua altura. Para reduzir as filas e otimizar a operação, você foi contratado para escrever um programa que, dado o número de convidados, a altura mínima e máxima permitida e a altura de cada convidado, determina quantos convidados podem andar na montanha-russa .

Entrada
A entrada contém vários casos de teste. A primeira linha de cada caso de teste contém três inteiros N (1 ≤ N ≤ 100), Amin e Amax (50 ≤ Amin ≤ Amax ≤ 250), o número de convidados, a altura mínima e máxima permitida, respectivamente, em centímetros.

Cada uma das próximas N linhas contém um inteiro (50 ≤ Ai ≤ 250), a altura do i-ésimo convidado, em centímetros.

A entrada termina com fim de arquivo (EOF).

Saída
Para cada caso de teste, imprima uma única linha contendo o número de convidados permitidos para andar na montanha-russa.
'''

while True:
    
    try:
        cont = 0
        n, amin, amax  = map(int, input().split())
        for c in range(0, n):
            alt = int(input())
            if alt >= amin and alt <= amax:
                cont += 1
    
        print(cont)

    except EOFError:
        break