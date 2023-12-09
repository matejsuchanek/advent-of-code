import os

data = [0] * 9

with open(os.path.join('data', 'aoc6.txt'), 'r') as file:
    line = next(file)
    for n in line.split(','):
        data[int(n)] += 1

for a, b in [(0, 80), (80, 256)]:
    for i in range(a, b):
        add = data[0]
        new = data[1:]
        new[6] += add
        new.append(add)
        data = new

    print(sum(data))
