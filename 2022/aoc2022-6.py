import os

with open(os.path.join('data', 'aoc6.txt'), 'r') as file:
    data = file.read().rstrip()

i = 0
while True:
    acc = ''
    ok = True
    for j in range(4):
        c = data[i+j]
        if c in acc:
            ok = False
            break
        acc += c

    if ok:
        break
    i += 1

print(i+4)

i = 0
while True:
    acc = set()
    ok = True
    for j in range(14):
        c = data[i+j]
        if c in acc:
            ok = False
            break
        acc.add(c)

    if ok:
        break
    i += 1

print(i+14)
