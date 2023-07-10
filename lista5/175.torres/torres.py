'''
Saruman, o Branco, um grande mago da Terra-média, traiu as boas maneiras e se juntou ao senhor do mal, Sauron. Sauron comanda a torre de Minas Morgul, que abriga um de seus servos mais temidos, o Rei Bruxo de Angmar, um dos Nazgûl (ex-reis humanos que foram corrompidos pelos poderes dos anéis de Sauron). Saruman comanda a torre de Orthanc, onde cria seus servos Uruk-hai, orcs mais terríveis que os convencionais. Para comunicação, eles usam as relíquias esféricas chamadas Palantír, que ficam no topo de suas torres.
A Terra-média avança cada vez mais em tecnologia, muito impulsionada pelas guerras que a afetam diariamente. Um dos problemas que tem prejudicado sua população é a Interferência de Comunicação Magnética (ICM). Pesquisadores de Minas Tirith, a grande cidadela de Gondor, concluíram que para calcular o ICM dos Palantír's, basta dividir a distância entre os dois Palantír's pela soma de seus diâmetros. Gandalf, o Cinzento, chegou a questionar essa conclusão, alegando que não fazia muito sentido, mas ele mesmo concluiu que dar sentido às coisas não faz sentido.
Saruman e Sauron precisam de uma comunicação estável porque temem que Frodo e seus amigos possam atrapalhar seus planos, então eles querem saber quanto ICM existe na comunicação de seus Palantír's, para que saibam quanta magia devem usar na comunicação .

Entrada
A entrada é composta por 3 números inteiros, N (0 < N < 10000), X e Y (0 < X ​​, Y < 100), que indicam, respectivamente, a distância entre o Palantír, o diâmetro do Palantír de Sauron e o diâmetro do Palantír de Saruman.

Saída
Um valor duplo que indica o ICM da comunicação do Palatír de Sauron e Saruman, com 2 casas decimais.
'''

dist, dm1, dm2 = map(int, input().split())

comuincacao = dist / (dm1 + dm2)

print(f'{comuincacao:.2f}')
