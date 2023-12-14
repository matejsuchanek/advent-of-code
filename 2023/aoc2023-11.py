import os

space = []
empty_rows = set()
empty_cols = set()

with open(os.path.join('data', 'aoc11.txt'), 'r') as file:
    for i, line in enumerate(file):
        row = line.rstrip()
        space.append(row)
        if '#' not in row:
            empty_rows.add(i)

for i in range(len(space[0])):
    if all(row[i] == '.' for row in space):
        empty_cols.add(i)

galaxies = []

for x, row in enumerate(space):
    for y, ch in enumerate(row):
        if ch == '#':
            galaxies.append((x, y))

for val in (2, 1_000_000):
    total = 0
    for idx, (x, y) in enumerate(galaxies):
        for i, j in galaxies[idx+1:]:
            dist_r = dist_c = 0
            if x != i:
                dist_r = 1 + sum(val if k in empty_rows else 1
                                 for k in range(min(i, x)+1, max(i, x)))
            if y != j:
                dist_c = 1 + sum(val if k in empty_cols else 1
                                 for k in range(min(j, y)+1, max(j, y)))

            total += dist_r + dist_c

    print(total)
