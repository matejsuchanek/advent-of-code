import os

UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)

rotations = [RIGHT, DOWN, LEFT, UP]

grid = []

with open(os.path.join('data', 'aoc22.txt'), 'r') as file:
    for line in file:
        row = line.rstrip()
        if not row:
            break
        grid.append(row)

    path = []
    x = 0
    for c in next(file).rstrip():
        if c.isdigit():
            x = 10 * x + int(c)
        else:
            path.append(x)
            path.append(c)
            x = 0
    if x > 0:
        path.append(x)

pos = (0, grid[0].index('.'))
facing = rotations.index(RIGHT)

for instr in path:
    if instr == 'L':
        facing = (facing - 1) % 4
        continue
    if instr == 'R':
        facing = (facing + 1) % 4
        continue

    dx, dy = rotations[facing]
    for _ in range(instr):
        x, y = pos
        if dx != 0:
            while True:
                x += dx
                if x < 0:
                    x = len(grid) - 1
                elif x == len(grid):
                    x = 0
                if y < len(grid[x]) and grid[x][y] != ' ':
                    break
        else:
            while True:
                y += dy
                if y < 0:
                    y = len(grid[x]) - 1
                elif y == len(grid[x]):
                    y = 0
                if grid[x][y] != ' ':
                    break

        if grid[x][y] == '#':
            break
        assert grid[x][y] == '.'
        pos = (x, y)

out = (pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + facing
print(out)
