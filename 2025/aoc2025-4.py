import os

def steps(x, y):
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if i or j:
                yield (x + i, y + j)


access = 0
grid = []

with open(os.path.join('data', 'aoc4.txt')) as file:
    for line in file:
        grid.append(list(line.rstrip()))

for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if grid[i][j] != '@':
            continue
        adj = 0
        for x, y in steps(i, j):
            if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
                adj += grid[x][y] == '@'
        access += adj < 4

print(access)

removed = 0
while True:
    new_grid = []
    now_removed = 0
    for i, row in enumerate(grid):
        new_row = []
        for j, c in enumerate(row):
            if grid[i][j] != '@':
                new_row.append('.')
                continue
            adj = 0
            for x, y in steps(i, j):
                if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
                    adj += grid[x][y] == '@'
            if adj < 4:
                now_removed += 1
                new_row.append('.')
            else:
                new_row.append('@')
        new_grid.append(new_row)
    if not now_removed:
        break
    grid = new_grid
    removed += now_removed

print(removed)
