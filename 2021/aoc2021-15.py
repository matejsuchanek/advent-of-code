import heapq
import os


def get_adjancent(r, c):
    adj = []
    if c > 0:
        adj.append((r, c-1))
    if c < len(grid[0]) - 1:
        adj.append((r, c+1))
    if r > 0:
        adj.append((r-1, c))
    if r < len(grid) - 1:
        adj.append((r+1, c))
    return adj


small_grid = []
large_grid_tmp = []
large_grid = []
with open(os.path.join('data', 'aoc15.txt'), 'r') as file:
    for line in file:
        row = [int(n) for n in line.rstrip()]
        small_grid.append(row)

        large_row = []
        for i in range(5):
            for n in row:
                new = n + i
                if new > 9:
                    new -= 9
                large_row.append(new)
        large_grid_tmp.append(large_row)

    large_grid = []
    for i in range(5):
        for row in large_grid_tmp:
            large_row = []
            for n in row:
                new = n + i
                if new > 9:
                    new -= 9
                large_row.append(new)
            large_grid.append(large_row)
    del large_grid_tmp

for grid in (small_grid, large_grid):
    queue = [(0, (0, 0))]
    already = set()
    end = (len(grid) - 1, len(grid[-1]) - 1)
    while queue:
        score, pos = heapq.heappop(queue)
        if pos == end:
            print(score)
            break
        if pos in already:
            continue
        already.add(pos)
        for node in get_adjancent(*pos):
            x, y = node
            cost = grid[x][y]
            heapq.heappush(queue, (score + cost, node))
