'''
E aí, gostou da Escola de Inverno esse ano? Para que esta Escola acontecesse, muitos trabalharam, seja na redação dos problemas, na configuração do Portal, na organização do evento ou na captação de recursos. O nosso agradecimento especial este ano vai para o Professor Ricardo Oliveira, que não só aceitou o nosso convite para vir ministrar os workshops como também tem participado na organização desta Escola. Temos a certeza que a sua experiência e o seu percurso no ICPC como competidor e como treinador nos motivaram e inspiraram a todos.

Esperamos que tenham gostado destes últimos dias em Essos e em Westeros, esperamos que tenham aprendido muito e se divertido. Mas não é só em Essos e em Westeros que você deve se divertir. Aqui, no Beyond the Wall, programar também é divertido. Continue estudando, continue treinando e mais e mais. O importante é o caminho que você escolhe seguir a partir de agora. Nosso conselho é que você sempre aproveite cada momento, cada workshop, cada escola, cada sessão de treinamento, sempre praticando ou estudando em casa. Nossos dias nunca mais vão voltar.

Entrada
A entrada consiste em um único inteiro N (1 ≤ N ≤ 34) em uma linha.

Saída
Imprima os N primeiros caracteres da citação de Søren Kierkegaard definidos pelas letras sublinhadas nesta declaração do problema. Tenha cuidado, pois nenhum espaço em branco foi sublinhado - você deve adivinhar o número e a localização dos espaços em branco na frase. A única linha de saída deve consistir apenas em letras maiúsculas e espaços em branco e deve ser encerrada no final da linha.
'''

msg = str('LIFE IS NOT A PROBLEM TO BE SOLVED')

n = int(input())

cont = 0

while cont <= n-1:
    if cont < n-1:
        print(msg[cont], end='')
    else:
        print(msg[cont])
    cont += 1