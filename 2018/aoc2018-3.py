import os
import re

regex = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

grid = [[0 for x in range(1000)] for x in range(1000)]

already = set()
with open(os.path.join('data', 'aoc3.txt')) as file:
    for line in file:
        claim, x, y, w, h = map(int, regex.match(line).groups())
        for i in range(x, x+w):
            for j in range(y, y+h):
                if grid[i][j]:
                    if grid != -1:
                        already.add(grid[i][j])
                        already.add(claim)
                        grid[i][j] = -1
                else:
                    grid[i][j] = claim

out = 0
for r in grid:
    for i in r:
        out += (i == -1)
print(out)

for i in range(1, claim+1):
    if i not in already:
        print(i)
        break
