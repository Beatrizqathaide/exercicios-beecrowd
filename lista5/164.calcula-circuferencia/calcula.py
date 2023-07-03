'''
Muitas coisas aconteceram desde o início da jornada de Bilbo, Gandalf e os anões. Ao passar pelas Montanhas Sombrias, Bilbo se separou de seus amigos e acabou na caverna de Gollum.

Bilbo então encontra um anel e percebe que esse anel pertencia a Gollum, pois ele está desesperado atrás dele, mas Bilbo sente algo vindo do anel e guarda para si. Gollum fica desconfiado, e propõe a Bilbo um jogo de adivinhas, e se Bilbo perdesse, acabaria ali mesmo. Bilbo é forçado a aceitar o jogo.

Gollum, apesar de ser uma criatura desprezível, é muito bom em matemática, então faz a Bilbo uma pergunta envolvendo circunferência de círculos (já pensando em seu anel). Bilbo tem medo de não conseguir resolver o enigma, então ele quebrou a quarta parede e está pedindo para você criar um algoritmo que, dado o raio R do círculo, retorne o tamanho total da circunferência.

Ah, e Gollum disse: "Você pode considerar o valor de pi como 3,14, precioso".

Entrada
Um valor R real que indica o tamanho do raio do círculo da pergunta de Gollum.

Limites: 0 <R <= 10;

Saída
Um valor real com duas casas decimais indicando o tamanho total do círculo da pergunta de Gollum.
'''

raio = float(input())

resultado = 2 * 3.14 * raio

print(f'{resultado:.2f}')