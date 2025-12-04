import os
from collections import deque

from common import Vector, looks

def flood_fill(start, char, eq=True, dont=None):
    if dont is None:
        dont = set()
    seen = set()
    queue = deque()
    queue.append(start)

    while queue:
        node = queue.popleft()
        if node in seen:
            continue

        seen.add(node)
        for look in looks:
            new = node + look
            if 0 <= new.x < len(grid) \
               and 0 <= new.y < len(grid[new.x]) \
               and (((grid[new.x][new.y] == char) is eq) or (eq is None)) \
               and new not in dont:
                queue.append(new)

    return seen


grid = []

with open(os.path.join('data', 'aoc12.txt')) as file:
    for i, line in enumerate(file):
        grid.append(line.strip())

total = discount = 0

already = set()
for i, line in enumerate(grid):
    for j in range(len(line)):
        start = Vector(i, j)
        if start in already:
            continue

        perim = sides = 0

        region = flood_fill(start, grid[i][j])

        already |= region
        border = set()
        for node in region:
            adj = set()
            for look in looks:
                new = node + look
                if 0 <= new.x < len(grid) \
                   and 0 <= new.y < len(grid[new.x]) \
                   and grid[new.x][new.y] == grid[i][j]:
                    adj.add(new)

            if len(adj) < 4:
                perim += 4 - len(adj)
                border.add(node)

        total += perim * len(region)

print(total)
