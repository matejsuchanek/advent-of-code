import os
from collections import deque

direct = {
    'U': (-1, 0),
    'D': (+1, 0),
    'L': (0, -1),
    'R': (0, +1),
}
rh_map = {'U': 'R', 'R': 'D', 'D': 'L', 'L': 'U'}
x = y = 0
edge = {(x, y)}
righthand = set()

with open(os.path.join('data', 'aoc18.txt'), 'r') as file:
    for line in file:
        facing, steps, _ = line.split()

        dx, dy = direct[facing]
        for _ in range(int(steps)):
            x += dx
            y += dy
            edge.add((x, y))
            rx, ry = direct[rh_map[facing]]
            righthand.add((x + rx, y + ry))

min_x = min(x for x, y in edge)
max_x = max(x for x, y in edge)
min_y = min(y for x, y in edge)
max_y = max(y for x, y in edge)

righthand -= edge

queue = deque(righthand)
while queue:
    x, y = pos = queue.popleft()
    for dx, dy in direct.values():
        new = (x + dx, y + dy)
        if min_x <= new[0] <= max_x \
           and min_y <= new[1] <= max_y \
           and new not in righthand \
           and new not in edge:
            righthand.add(new)
            queue.append(new)

if any(x == min_x or x == max_x or y == min_y or y == max_y
       for x, y in righthand):
    print((max_x - min_x + 1) * (max_y - min_y + 1) - len(righthand))
else:
    print(len(edge) + len(righthand))
