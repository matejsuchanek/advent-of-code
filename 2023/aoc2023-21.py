import os

grid = []
start = None

with open(os.path.join('data', 'aoc21.txt')) as file:
    for i, line in enumerate(file):
        grid.append(line.rstrip())
        if 'S' in grid[-1]:
            start = (i, grid[-1].index('S'))

reach = {start}
directs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for _ in range(64):
    new = set()
    for x, y in reach:
        for dx, dy in directs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < len(grid) \
               and 0 <= ny < len(grid[nx]) \
               and grid[nx][ny] != '#':
                new.add((nx, ny))
    reach = new
    print(len(new))
