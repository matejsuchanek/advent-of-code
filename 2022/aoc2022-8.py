import math
import os
"""
import numpy as np
grid = np.array(grid, dtype=int)
total = 0
for r in range(grid.shape[0]):
    for c in range(grid.shape[1]):
        n = grid[r, c]
        if np.all(grid[r, :c] < n):
            total += 1
        elif np.all(grid[r, c+1:] < n):
            total += 1
        elif np.all(grid[:r, c] < n):
            total += 1
        elif np.all(grid[r+1:, c] < n):
            total += 1
print(total)
"""

grid = []
with open(os.path.join('data', 'aoc8.txt'), 'r') as file:
    for line in map(str.rstrip, file):
        grid.append([int(c) for c in line])

total = 0
for r, row in enumerate(grid):
    for c, n in enumerate(row):
        if all(x < n for x in row[:c]):
            total += 1
        elif all(x < n for x in row[c+1:]):
            total += 1
        elif all(other[c] < n for other in grid[:r]):
            total += 1
        elif all(other[c] < n for other in grid[r+1:]):
            total += 1

print(total)

best = 0
for r, row in enumerate(grid):
    for c, n in enumerate(row):
        counts = []

        # up
        count = 0
        for other in reversed(grid[:r]):
            count += 1
            if other[c] >= n:
                break
        counts.append(count)

        # left
        count = 0
        for x in reversed(row[:c]):
            count += 1
            if x >= n:
                break
        counts.append(count)

        # down
        count = 0
        for other in grid[r+1:]:
            count += 1
            if other[c] >= n:
                break
        counts.append(count)

        # right
        count = 0
        for x in row[c+1:]:
            count += 1
            if x >= n:
                break
        counts.append(count)
        prod = math.prod(counts)
        best = max(best, prod)

print(best)
