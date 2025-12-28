import os

rocks = set()
cubes = set()
rows = cols = 0

with open(os.path.join('data', 'aoc14.txt'), 'r') as file:
    for r, line in enumerate(map(str.rstrip, file)):
        rows += 1
        cols = len(line)

        for c, x in enumerate(line):
            if x == '#':
                cubes.add((r, c))
            elif x == 'O':
                rocks.add((r, c))

acc = []

for epoch in range(1000):
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

    old_rocks = rocks
    rocks = set()
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in old_rocks:
                continue
            i = c
            while i > 0:
                t = (r, i-1)
                if t in cubes or t in rocks:
                    break
                i -= 1
            rocks.add((r, i))

    old_rocks = rocks
    rocks = set()
    for c in range(cols):
        for r in range(rows-1, -1, -1):
            if (r, c) not in old_rocks:
                continue
            i = r
            while i < (rows - 1):
                t = (i+1, c)
                if t in cubes or t in rocks:
                    break
                i += 1
            rocks.add((i, c))

    old_rocks = rocks
    rocks = set()
    for r in range(rows):
        for c in range(cols-1, -1, -1):
            if (r, c) not in old_rocks:
                continue
            i = c
            while i < (cols - 1):
                t = (r, i+1)
                if t in cubes or t in rocks:
                    break
                i += 1
            rocks.add((r, i))

    total = 0
    for r, _ in rocks:
        total += rows - r
    acc.append(total)

for length in range(2, len(acc) // 2):
    if acc[-2*length:-length] == acc[-length:]:
        cycle = acc[-length:]
        break

mod = (1_000_000_000 - 1000 - 1) % length
print(cycle[mod])
