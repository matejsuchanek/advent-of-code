import os

rocks = set()
cubes = set()
rows = cols = 0

with open(os.path.join('data', 'aoc14.txt'), 'r') as file:
    for r, line in enumerate(file):
        rows += 1
        cols = len(line.rstrip())

        for c, x in enumerate(line.rstrip()):
            if x == '#':
                cubes.add((r, c))
            elif x == 'O':
                rocks.add((r, c))

old_rocks = rocks
rocks = set()
for c in range(cols):
    for r in range(rows):
        if (r, c) not in old_rocks:
            continue
        i = r
        while i > 0:
            t = (i-1, c)
            if t in cubes or t in rocks:
                break
            i -= 1
        rocks.add((i, c))

total = 0
for r, _ in rocks:
    total += rows - r
print(total)
