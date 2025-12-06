import os
from heapq import *

alpha = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

lines = []
with open(os.path.join('data', 'aoc20.txt')) as file:
    for line in file:
        lines.append(line.rstrip('\n'))

tmp = {}
portals = {}
grid = []

for i, line in enumerate(lines):
    new = ''
    for j, c in enumerate(line):
        if c in alpha:
            new += ' '
        else:
            new += c
        if c != '.':
            continue
        for di, dj in dirs:
            other = lines[i + di][j + dj]
            another = lines[i + 2*di][j + 2*dj]
            if other in alpha and another in alpha:
                if di == -1 or dj == -1:
                    port = another + other
                else:
                    port = other + another
                loc = (i - 2, j - 2)
                if port in tmp:
                    other_loc = tmp.pop(port)
                    portals[loc] = other_loc
                    portals[other_loc] = loc
                else:
                    tmp[port] = loc
                break
    line = new[2:-2]
    grid.append(line)

start = tmp.pop('AA')
end = tmp.pop('ZZ')
assert not tmp
del tmp

max_i, max_j = len(grid), len(grid[0])

queue = [(0, start)]
already = set()
while True:
    d, pos = heappop(queue)
    if pos == end:
        print(d)
        break
    if pos in already:
        continue
    already.add(pos)
    push = []
    if pos in portals:
        push.append(portals[pos])
    for di, dj in dirs:
        x, y = other = (pos[0] + di, pos[1] + dj)
        if 0 <= x < max_i and 0 <= y < max_j:
            if grid[x][y] == '.':
                push.append(other)
    for n in push:
        if n not in already:
            heappush(queue, (d + 1, n))
