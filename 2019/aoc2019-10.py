import os
from math import gcd


def iterator():
    for x in range(h):
        for y in range(w):
            yield x, y


def generate_inter(i, j, x, y):
    if x == i:
        sign = 1 if y > j else -1
        for d in range(1, abs(y - j)):
            yield i, j + d * sign
    elif y == j:
        sign = 1 if x > i else -1
        for d in range(1, abs(x - i)):
            yield i + d * sign, j
    else:
        lr = x - i
        td = y - j
        GCD = gcd(abs(lr), abs(td))
        if GCD == 1:
            return
        step_i = lr // GCD
        step_j = td // GCD
        for d in range(1, GCD):
            yield i + d * step_i, j + d * step_j


with open(os.path.join('data', 'aoc10.txt')) as file:
    grid = file.read().splitlines()

h, w = len(grid), len(grid[0])
best = 0
station = None
for i, j in iterator():
    total = 0
    if grid[i][j] != '#':
        continue
    for x, y in iterator():
        if grid[x][y] != '#':
            continue
        if (i, j) == (x, y):
            continue
        for a, b in generate_inter(i, j, x, y):
            if grid[a][b] == '#':
                break
        else:
            total += 1
    if total > best:
        best = total
        station = i, j

print(best)

around = []

for i, j in iterator():
    if station == (i, j):
        continue
    if grid[i][j] == '#':
        diff_x, diff_y = (station[0] - i, station[1] - j)
        if diff_x > 0 and diff_y <= 0:
            quad = 0
        elif diff_x <= 0 and diff_y < 0:
            quad = 1
        elif diff_x < 0 and diff_y >= 0:
            quad = 2
        elif diff_x >= 0 and diff_y > 0:
            quad = 3
        if quad % 2 == 1:
            diff_x, diff_y = abs(diff_y), abs(diff_x)
        else:
            diff_x, diff_y = abs(diff_x), abs(diff_y)
        div = gcd(diff_x, diff_y)
        base_pair = (diff_x // div, diff_y // div)
        around.append(
            (div, quad, diff_y/diff_x, base_pair, (i, j))
        )

in_order = []
counter_for = {}
for div, quad, num, pair, pos in sorted(around):
    index = counter_for.setdefault((quad, pair), 1)
    counter_for[quad, pair] += 1
    in_order.append((index, quad, num, pos))
in_order.sort()

target = in_order[199][-1]
print(target[1] * 100 + target[0])
