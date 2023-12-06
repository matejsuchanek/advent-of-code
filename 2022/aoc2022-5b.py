import os
from collections import defaultdict

stacks = defaultdict(list)

with open(os.path.join('data', 'aoc5.txt'), 'r') as file:
    rows = []
    for line in file:
        if line.strip() == '':
            break
        rows.append(line)

    order = rows.pop().split()
    while rows:
        line = rows.pop()
        for i, x in zip(range(1, len(line), 4), order):
            if line[i] != ' ':
                stacks[x].append(line[i])

    for _, count, _, s, _, t in map(str.split, file):
        stacks[t].extend(stacks[s][-int(count):])
        for i in range(int(count)):
            stacks[s].pop()

    result = ''.join(stacks[x][-1] for x in order)

print(result)
