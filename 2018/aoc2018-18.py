import os
from collections import Counter


with open(os.path.join('data', 'aoc18.txt')) as file:
    rows = list(map(str.rstrip, file))

dirs = []
for x in (-1, 0, 1):
    for y in (-1, 0, 1):
        if x or y:
            dirs.append((x, y))

for i in range(10):
    new = []
    for j, row in enumerate(rows):
        new_row = ''
        for k, c in enumerate(row):
            counter = Counter()
            for x, y in dirs:
                if 0 <= j + x < len(rows) and 0 <= k + y < len(row):
                    counter[rows[j+x][k+y]] += 1
            if c == '.':
                if counter['|'] >= 3:
                    c = '|'
            elif c == '|':
                if counter['#'] >= 3:
                    c = '#'
            elif c == '#':
                if counter['|'] >= 1 and counter['#'] >= 1:
                    pass
                else:
                    c = '.'
            new_row += c
        new.append(new_row)

    rows = new

woods = 0
lys = 0
for row in rows:
    woods += row.count('|')
    lys += row.count('#')

print(woods * lys)
