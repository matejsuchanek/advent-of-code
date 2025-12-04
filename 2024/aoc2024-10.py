import os
from collections import deque, defaultdict

grid = []

with open(os.path.join('data', 'aoc10.txt')) as file:
    for line in file:
        grid.append([int(x) for x in line.strip()])

total = rating = 0
for sx, line in enumerate(grid):
    for sy, val in enumerate(line):
        if val != 0:
            continue

        peaks = defaultdict(lambda: 0)
        queue = deque()
        queue.append((sx, sy))
        while queue:
            (x, y) = queue.popleft()
            val = grid[x][y]
            if val == 9:
                peaks[x, y] += 1
                continue

            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= nx < len(grid) \
                   and 0 <= ny < len(grid[nx]) \
                   and grid[nx][ny] == (val + 1):
                    queue.append((nx, ny))

        total += len(peaks)
        rating += sum(peaks.values())

print(total)
print(rating)
