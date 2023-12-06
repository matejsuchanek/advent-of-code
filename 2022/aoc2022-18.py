import os
from collections import deque

cubes = []
with open(os.path.join('data', 'aoc18.txt'), 'r') as file:
    for line in map(str.rstrip, file):
        x, y, z = map(int, line.split(','))
        cubes.append((x, y, z))

moves = [
    (1, 0, 0), (0, 1, 0), (0, 0, 1),
    (-1, 0, 0), (0, -1, 0), (0, 0, -1),
]

cubes_set = set(cubes)
queue = deque()
total = 0
already = set()
for x, y, z in cubes:
    sides = 6
    for dx, dy, dz in moves:
        adj = (x+dx, y+dy, z+dz)
        if adj in cubes_set:
            sides -= 1
        elif adj not in already:
            already.add(adj)
            queue.append({adj})
    total += sides

del already
print(total)

hidden = set()
while len(queue) > 1:
    block = queue.popleft()

    around = set()
    for x, y, z in block:
        for dx, dy, dz in moves:
            adj = (x+dx, y+dy, z+dz)
            if adj in cubes_set:
                continue
            if adj in block:
                continue
            around.add(adj)

    if not around:
        hidden |= block
        continue

    for other in queue:
        if around & other:
            other |= block
            other |= around
            break
    else:
        block |= around
        queue.append(block)

total = 0
for x, y, z in cubes:
    sides = 6
    for dx, dy, dz in moves:
        adj = (x+dx, y+dy, z+dz)
        if adj in cubes_set or adj in hidden:
            sides -= 1
    total += sides

print(total)
