import os
from collections import defaultdict

lines = []

with open(os.path.join('data', 'aoc3.txt'), 'r') as file:
    for line in file:
        lines.append(line.rstrip())

prim = 0
gears = defaultdict(list)

for i, line in enumerate(lines):
    cur_n = 0
    cur_gears = set()
    is_adj = False
    for j, c in enumerate(line):
        if c.isdigit():
            cur_n = 10 * cur_n + int(c)
            for x in (-1, 0, 1):
                if (i+x) < 0 or (i+x) >= len(lines):
                    continue
                for y in (-1, 0, 1):
                    z = lines[i+x][j+y:j+y+1]
                    if not z.isdigit() and z != '.':
                        is_adj = True
                    if z == '*':
                        cur_gears.add((i+x, j+y))
            continue

        if cur_n != 0:
            if is_adj:
                prim += cur_n
            for gear in cur_gears:
                gears[gear].append(cur_n)
            cur_n = 0
            is_adj = False
            cur_gears = set()

    if cur_n != 0:
        if is_adj:
            prim += cur_n
        for gear in cur_gears:
            gears[gear].append(cur_n)
        cur_n = 0
        is_adj = False
        cur_gears = set()

print(prim)
sec = sum(val[0] * val[1] for val in gears.values() if len(val) == 2)
print(sec)
