from collections import deque
import os

def get_adjancent(r, c):
    adj = []
    if c > 0:
        adj.append((r, c-1))
    if c < len(row) - 1:
        adj.append((r, c+1))
    if r > 0:
        adj.append((r-1, c))
    if r < len(grid) - 1:
        adj.append((r+1, c))
    return adj


grid = []
with open(os.path.join('data', 'aoc9.txt'), 'r') as file:
    for line in file:
        row = [int(c) for c in line.rstrip()]
        grid.append(row)

sizes = []
risk = 0
for r, row in enumerate(grid):
    for c, val in enumerate(row):
        adj = get_adjancent(r, c)
        if all(val < grid[x][y] for x, y in adj):
            risk += val + 1
            basin = {(r, c)}
            queue = deque([(r, c)])
            while queue:
                x, y = queue.popleft()
                for pair in get_adjancent(x, y):
                    x_, y_ = pair
                    if grid[x_][y_] == 9:
                        continue
                    if pair in basin:
                        continue
                    basin.add(pair)
                    queue.append(pair)
            sizes.append(len(basin))

print(risk)
sizes.sort()
print(sizes[-1] * sizes[-2] * sizes[-3])
