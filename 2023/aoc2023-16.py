import os
from collections import deque

NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)

redirs = {
    ('/', EAST): [NORTH],
    ('/', WEST): [SOUTH],
    ('/', SOUTH): [WEST],
    ('/', NORTH): [EAST],
    ('\\', EAST): [SOUTH],
    ('\\', WEST): [NORTH],
    ('\\', SOUTH): [EAST],
    ('\\', NORTH): [WEST],
    ('|', EAST): [NORTH, SOUTH],
    ('|', WEST): [NORTH, SOUTH],
    ('-', SOUTH): [WEST, EAST],
    ('-', NORTH): [WEST, EAST],
}

grid = []

with open(os.path.join('data', 'aoc16.txt'), 'r') as file:
    for line in file:
        grid.append(line.rstrip())

edges = []
for x in range(len(grid)):
    edges.append(((x, 0), EAST))
    edges.append(((x, len(grid[x])-1), WEST))
for y in range(len(grid[0])):
    edges.append(((0, y), SOUTH))
    edges.append(((len(grid)-1, y), NORTH))

best = 0
for init in edges:
    queue = deque([init])
    seen = set()
    energy = set()

    while queue:
        entry = queue.popleft()
        seen.add(entry)
        energy.add(entry[0])

        (x, y), direct = entry
        moves = redirs.get((grid[x][y], direct), [direct])
        for move in moves:
            new_x, new_y = (x + move[0], y + move[1])
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[new_x]):
                new_entry = ((new_x, new_y), move)
                if new_entry not in seen:
                    queue.append(new_entry)

    best = max(best, len(energy))
    if init == ((0, 0), EAST):
        print(len(energy))

print(best)
