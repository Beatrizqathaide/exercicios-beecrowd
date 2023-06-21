'''
Jon Marius gritou demais no recente show de Justin Bieber, e agora precisa ir ao médico por causa da dor de garganta. A orientação do médico é dizer “aaah”. Infelizmente, os médicos às vezes precisam que Jon Marius diga “aaah” por um tempo, o que Jon Marius nunca foi bom. Cada médico requer um certo nível de “aah” – alguns exigem “aaaaaah”, enquanto outros podem realmente diagnosticar sua garganta com apenas um “h”. (Eles costumam diagnosticar errado, mas isso está além do escopo deste problema.) Como Jon Marius não quer ir ao médico e perder tempo, ele quer comparar quanto tempo consegue segurar o “aaah” com o requisitos do médico. (Afinal, quem quer ficar todo tipo “aaah” quando o médico quer que você faça “aaaaaah”?)

Todos os dias, Jon Marius liga para um médico diferente e pergunta quanto tempo seu “aaah” deve durar. Descubra se Jon Marius perderia seu tempo indo ao médico indicado.

Entrada
A entrada consiste em duas linhas. A primeira linha é o “aaah” que Jon Marius é capaz de dizer naquele dia. A segunda linha é o “aah” que o médico quer ouvir. Somente 'a' e 'h' minúsculos serão usados ​​na entrada, e cada linha conterá entre 0 e 999 'a's, inclusive, seguido por um único 'h'.

Saída
Emita "vá" se Jon Marius puder ir ao médico e emita "não" caso contrário.
'''

j = input()
m = input()

if len(j) < len(m):
    print('não')
else:
    print('ir')