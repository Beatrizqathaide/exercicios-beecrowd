'''
Era uma vez um campeão de WoW
Arthasdk o nome que lhe foi dado
Ele Death agarrou você ao seu lado
Suas Correntes de Gelo pararam seu passo
E Obliterates fez você dizer "OWW!"
Mas um dia nosso herói ficou confuso
Seu Death Grip fracassou totalmente
Em seu desespero mais sombrio
Ele mal podia ouvir
”OMG NOOB u Chains of Iced do que u Death Gripped ”

Entrada
Você recebe uma gravação das habilidades que nosso herói usou em suas batalhas.

A primeira linha de entrada conterá um único inteiro n (1 ≤ n ≤ 100), o número de batalhas que nosso herói jogou.

Em seguida, siga n linhas, cada uma com uma sequência de k i (1 ≤ k i ≤ 1000) caracteres, cada um dos quais é 'C', 'D' ou 'O'. Estes denotam a sequência de habilidades usadas por nosso herói na i -ésima batalha. 'C' é Chains of Ice , 'D' é Death Grip e 'O' é Obliterate .

Saída
Imprima o número de batalhas que nosso herói venceu, assumindo que ele venceu cada batalha onde não fez Chains of Ice imediatamente seguido por Death Grip .
'''

batalhas = int(input())

perdeu = 0

for c in range(0, batalhas):
    lutas = input().upper()
    
    for i in range(len(lutas) - 1):
        if lutas[i] == 'C' and lutas[i + 1] == 'D':
            perdeu += 1

venceu = batalhas - perdeu
print(venceu)