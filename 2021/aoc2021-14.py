from collections import Counter
import os

transp = {}
with open(os.path.join('data', 'aoc14.txt'), 'r') as file:
    polymer = next(file).rstrip()

    next(file)
    for line in file:
        l, r = line.rstrip().split(' -> ')
        transp[l] = r

for i in range(40):
    new = []
    length = len(polymer)
    for j in range(length - 1):
        a, b = polymer[j], polymer[j + 1]
        new.append(a)
        c = transp.get(a + b)
        if c:
            new.append(c)
    new.append(polymer[-1])
    polymer = new
    if i + 1 in (10, 40):
        ct = Counter(polymer)
        pairs = ct.most_common()

        print(pairs[0][1] - pairs[-1][1])
