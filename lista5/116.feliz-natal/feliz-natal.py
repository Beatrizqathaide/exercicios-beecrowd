'''
Merry Christmaaas!

You get so happy at Christmas that you want to scream at everyone: "Merry Christmas!!". To put all this happiness out, you wrote a program that, given an I index of happiness, your Christmas scream is more lively.

Input
The input consists of an integer I (1 < I ≤ 104) that represents that happiness index.

Output
The output consists of the phrase "Feliz natal!" ("Merry Christmas" in Portuguese), and the last a of the sentence is repeated I times. A line break is necessary after printing the sentence.

Input Sample	Output Sample
5

Feliz nataaaaal!
'''

n = int(input())

cont = 0
m = ['Feliz nat']

while cont <= n:
    if cont < n:
        m.append('a')
    if cont == n:
        m.append('l!')

    cont+=1

for c in range(0, len(m)):
    if c < len(m) - 1:
        print(m[c], end='')
    if c == len(m) - 1:
        print(m[c])