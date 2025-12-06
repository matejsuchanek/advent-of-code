import os

with open(os.path.join('data', 'aoc2.txt')) as file:
    data = file.read()

start = list(map(int, data.split(',')))
ints = start[:]
ints[1:3] = 12, 2

for i in range(0, len(ints), 4):
    x = ints[i]
    if x == 1:
        value = ints[ints[i+1]] + ints[ints[i+2]]
    elif x == 2:
        value = ints[ints[i+1]] * ints[ints[i+2]]
    elif x == 99:
        break
    ints[ints[i+3]] = value

print(ints[0])

const = 19690720
n = v = 0

while True:
    ints = start[:]
    ints[1:3] = n, v
    for i in range(0, len(ints), 4):
        x = ints[i]
        if x == 1:
            value = ints[ints[i+1]] + ints[ints[i+2]]
        elif x == 2:
            value = ints[ints[i+1]] * ints[ints[i+2]]
        elif x == 99:
            break
        ints[ints[i+3]] = value

    if ints[0] == const:
        break
    n += 1
    v -= 1
    if v < 0:
        v = n
        n = 0

print(100 * n + v)
