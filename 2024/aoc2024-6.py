import os
from collections import defaultdict

from common import Vector


def is_in_grid(pos):
    (x, y) = (pos.x, pos.y)
    return (0 <= x < len(grid)) and (0 <= y < len(grid[x]))


def is_cycle(pos, face, block):
    my_obstacles = obstacle | {block}
    seen = set()
    while is_in_grid(pos):
        while (new := pos + face) in my_obstacles:
            face = right[face]
        if (pos, face) in seen:
            print(block)
            return True

        seen.add((pos, face))
        pos = new

    return False


right = {
    Vector(-1, 0): Vector(0,  1),
    Vector(0,  1): Vector(1,  0),
    Vector(1,  0): Vector(0, -1),
    Vector(0, -1): Vector(-1, 0),
}

face = Vector(-1, 0)
visited = set()
obstacle = set()

grid = []
with open(os.path.join('data', 'aoc6.txt')) as file:
    for i, line in enumerate(file):
        line = line.rstrip()
        grid.append(line)
        for j, c in enumerate(line):
            if c == '^':
                pos = Vector(i, j)
            elif c == '#':
                obstacle.add(Vector(i, j))

while is_in_grid(pos):
    visited.add(pos)
    while (new := pos + face) in obstacle:
        face = right[face]
    pos = new

print(len(visited))
