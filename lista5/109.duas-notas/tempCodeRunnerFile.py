n, m = map(int, input().split())

troco = m - n
nota = 0

while True:
    if m == 0 and n == 0 or troco == 0:
        break

    if troco >= 100:
        troco -= 100
        nota += 1

    elif troco >= 50:
        troco -= 50
        nota += 1

    elif troco >= 20:
        troco -= 20
        nota += 1

    elif troco >= 10:
        troco -= 10
        nota += 1

    elif troco >= 5:
        troco -= 5
        nota += 1

    elif troco >= 2:
        troco -= 2
        nota += 1

if nota == 2:
    print('possible')

else:
    print('impossible')