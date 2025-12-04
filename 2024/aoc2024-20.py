import os
from collections import deque

from common import Vector, looks

walls = set()
start = end = None
X = Y = 0

with open(os.path.join('data', 'aoc20.txt')) as file:
    for x, line in enumerate(file):
        X = x
        for y, c in enumerate(line.rstrip()):
            if c == '#':
                walls.add(Vector(x, y))
            elif c == 'S':
                start = Vector(x, y)
            elif c == 'E':
                end = Vector(x, y)
            Y = max(Y, y)

i = 0
node_to_order = {start: 0}
order_to_node = {0: start}
node = start
while node != end:
    for move in looks:
        new = node + move
        if new not in walls and new not in node_to_order:
            i += 1
            node_to_order[new] = i
            order_to_node[i] = new
            node = new
            break

length = node_to_order[end]

for allowed in (2, 20):
    result = 0

    jumps = {}
    queue = deque()
    queue.append((0, Vector(0, 0)))
    while queue:
        dist, node = queue.popleft()
        if node in jumps:
            continue
        jumps[node] = dist
        if dist < allowed:
            queue.extend((dist + 1, node + move) for move in looks)

    for i in range(length):
        node = order_to_node[i]
        for move, skip in jumps.items():
            new = node + move
            if 0 < new.x < X \
               and 0 < new.y < Y \
               and new not in walls:
                order = node_to_order[new]
                saved = order - i - skip
                if saved >= 100:
                    result += 1

    print(result)
