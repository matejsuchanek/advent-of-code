import os
import re

from common import Vector, looks

pattern = re.compile(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)\b')
X, Y = 101, 103

init = []

with open(os.path.join('data', 'aoc14.txt')) as file:
    for line in file:
        groups = pattern.match(line).groups()
        pos.x, pos.y, vx, vy = map(int, groups)
        init.append((Vector(pos.x, pos.y), Vector(vx, vy)))

robots = init[:]

for step in range(100):
    for i, (pos, vel) in enumerate(robots):
        new = (pos + vel) % (X, Y)
        robots[i] = (new, vel)

quad = [0] * 4

for pos, _ in robots:
    if pos.x < (X // 2) and pos.y < (Y // 2):
        quad[0] += 1
    elif pos.x > (X // 2) and pos.y < (Y // 2):
        quad[1] += 1
    elif pos.x < (X // 2) and pos.y > (Y // 2):
        quad[2] += 1
    elif pos.x > (X // 2) and pos.y > (Y // 2):
        quad[3] += 1

print(quad[0] * quad[1] * quad[2] * quad[3])

robots = init[:]
step = 0
best = 0

while True:
    step += 1

    occupied = set()
    for i, (pos, vel) in enumerate(robots):
        new = (pos + vel) % (X, Y)
        occupied.add(new)
        robots[i] = (new, vel)

    has_adj = sum(
        any(
            pos + look in occupied
            for look in looks
        )
        for pos, _ in robots
    )

    if has_adj >= best:
        best = has_adj
        grid = [list(' ' * X) for _ in range(Y)]
        for pos in occupied:
            grid[pos.y][pos.x] = 'x'
        for line in grid:
            print(''.join(line))
