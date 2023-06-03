#Neste problema, seu trabalho é ler três palavras em português. Essas palavras definem um animal de acordo com a tabela abaixo, da esquerda para a direita. Após, imprima o animal escolhido definido por essas três palavras.

a = input()
b = input()
c = input()

palavras = [a, b, c]

animais = {
            'aguia': ['vertebrado', 'ave', 'carnivoro'],
            'pomba': ['vertebrado', 'ave', 'onivoro'], 
            'homem': ['vertebrado', 'mamifero', 'onivoro'],
            'vaca': ['vertebrado', 'mamifero', 'herbivoro'],
            'pulga': ['invertebrado', 'inseto', 'hematofago'],
            'lagarta': ['invertebrado', 'inseto', 'herbivoro'],
            'sanguessuga': ['invertebrado', 'anelideo', 'hematofago'],
            'minhoca': ['invertebrado', 'anelideo', 'onivoro']
           }

for k, animal in animais.items():
    if palavras == animal:
        print(k)