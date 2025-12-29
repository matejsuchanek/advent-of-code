import os
from collections import Counter


with open(os.path.join('data', 'aoc18.txt')) as file:
    rows = list(map(str.rstrip, file))

dirs = []
for x in (-1, 0, 1):
    for y in (-1, 0, 1):
        if x or y:
            dirs.append((x, y))

configs = {}
jmax = len(rows)
kmax = len(rows[0])
i = 0
while True:
    config = ''.join(rows)
    if config in configs:
        base = configs[config]
        diff = i - base
        left = 1_000_000_000 - i
        index = base + (left % diff)
        cs = {c for c, idx in configs.items() if idx == index}
        string = cs.pop()
        woods = string.count('|')
        lys = string.count('#')
        print(woods * lys)
        break

    configs[config] = i

    new = []
    for j, row in enumerate(rows):
        new_row = ''
        for k, c in enumerate(row):
            counter = Counter()
            for x, y in dirs:
                jx, ky = (j + x, k + y)
                if 0 <= jx < jmax and 0 <= ky < kmax:
                    counter[rows[jx][ky]] += 1
            if c == '.':
                if counter['|'] >= 3:
                    c = '|'
            elif c == '|':
                if counter['#'] >= 3:
                    c = '#'
            elif c == '#':
                if counter['|'] == 0 or counter['#'] == 0:
                    c = '.'
            new_row += c
        new.append(new_row)

    rows = new
    i += 1
