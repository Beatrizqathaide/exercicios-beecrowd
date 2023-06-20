'''
Resumindo a história até aqui, tivemos lutas com aranhas, trolls, orcs, wargs, fugas em barris e muita luta com o dragão Smaug. Depois que Smaug foi derrotado, os anões reivindicaram a Montanha Solitária e todas as suas riquezas. No entanto, os humanos que vivem perto da montanha foram os responsáveis ​​por derrotar Smaug e também querem parte da riqueza. Algumas riquezas da montanha também pertenciam aos elfos, e eles também querem reivindicar sua parte.

Thorin, o anão líder da aventura, fica ávido pelo ouro da montanha e perde a sanidade, travando assim uma guerra contra humanos e elfos.

O que nenhum deles esperava era que os orcs e wargs também estivessem cobiçando a montanha, e eles vieram de surpresa. Assim, humanos, elfos e anões (o lado bom) têm que se unir para combater os orcs e wargs (o lado mau), travando assim a Batalha dos Cinco Exércitos.

Bilbo, nosso herói até então, abstém-se desta batalha, pois esta tomou proporções muito grandes para um hobbit, porém, consegue estimar quem vencerá. Nesse caso, basta somar o número de exércitos de cada lado e verificar qual é o maior. Porém, Bilbo sabe que Gandalf tem um plano b caso os exércitos de homens, elfos e anões percam ou empatem, e esse plano é chamar o exército de águias, aumentando assim o número do bom exército.

Calcule para Bilbo quem vencerá a Batalha dos Cinco Exércitos.

Ah, e se mesmo com as águias os dois grandes exércitos empatarem, Bilbo estará lá com sua espada Sting, para destruir o último orc ou warg.

Entrada
Contém 6 números inteiros, H, E, A, O, W e X, representando o número do exército de humanos, elfos, anões, orcs, wargs e águias, respectivamente.

Saída
Se o lado bom vencer: “A Terra-média está segura.”, Se não, “Sauron voltou.”.
'''

h, e, a, o, w, x = map(int, input().split())

b = h + e + a + x

m = o + w

if b > m:
    print('Middle-earth is safe.')
else:
    print('Sauron has returned.')