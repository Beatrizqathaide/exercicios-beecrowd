'''
Bilbo Bolseiro vivia em um buraco no chão da Vila dos Hobbits. Um dia, seu amigo Gandalf o convida para uma aventura. A aventura foi baseada em roubar o tesouro de um dragão. Bilbo logo pensou que seria uma loucura roubar um dragão, mas Gandalf tinha uma comitiva de anões com ele para ajudá-lo nessa tarefa.

Bilbo então decidiu calcular quantos dias levariam para chegar à Montanha Solitária, onde o dragão reside atualmente. Para esse cálculo seria necessário dividir a distância em quilômetros da Vila dos Hobbits até a Montanha Solitária pelo número de pessoas que vão na aventura (como ele tirou essa métrica? Não sei, coisa de hobbit). Vale ressaltar que o número de pessoas é o número de anões somado a 2 (porque Bilbo e Gandalf também vão viajar).

Bilbo está muito ocupado preparando os dois cafés da manhã para seus convidados antes de partir para a aventura, e então pediu a você, um hobbit programador muito habilidoso, que escrevesse um programa para o cálculo solicitado acima. Gandalf forneceu a ele uma lista com N nomes que são os anões que vão na aventura e, além disso, a distância X até a Montanha Solitária.

Entrada
A única linha na entrada contém 2 inteiros, N e X, indicando respectivamente o número de anões que Gandalf conseguiu ajudar na aventura e a distância da Vila dos Hobbits até a Montanha Solitária.

Limites: 1 <N <= 100; 1 <X <= 1000.

Saída
Um número real com duas casas decimais indicando o número de dias para chegar à Montanha Solitária.
'''

anoes, distancia = map(int, input().split())

resultado = distancia / (anoes + 2)

print(f'{resultado:.2f}')