import os

grid = []
positions = 0
with open(os.path.join('data', 'aoc11.txt'), 'r') as file:
    for line in file:
        row = [int(c) for c in line.rstrip()]
        grid.append(row)
        positions += len(row)

steps = [
    (0, +1), (+1, +1), (+1, 0), (+1, -1),
    (0, -1), (-1, -1), (-1, 0), (-1, +1),
]

count = 0
i = 0
while True:
    queue = []
    flashed = set()
    for r, row in enumerate(grid):
        for col, val in enumerate(row):
            val += 1
            grid[r][col] = val
            if val > 9:
                pair = (r, col)
                queue.append(pair)
                flashed.add(pair)

    for pos in queue:
        x, y = pos
        for dx, dy in steps:
            x_new, y_new = x+dx, y+dy
            if 0 <= x_new < len(grid) and 0 <= y_new < len(grid[0]):
                pair = x_new, y_new
                if pair not in flashed:
                    val = grid[x_new][y_new]
                    val += 1
                    grid[x_new][y_new] = val
                    if val > 9:
                        queue.append(pair)
                        flashed.add(pair)

    count += len(flashed)
    for x, y in queue:
        grid[x][y] = 0

    i += 1
    if i == 100:
        print(count)

    if len(flashed) == positions:
        print(i)
        break
