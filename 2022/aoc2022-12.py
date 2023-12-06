import os
from collections import deque

grid = []
every = []
with open(os.path.join('data', 'aoc12.txt'), 'r') as file:
    for i, line in enumerate(map(str.rstrip, file)):
        grid.append(line)
        pos = line.find('S')
        if pos != -1:
            start = (i, pos)

        left = 0
        while True:
            pos = line.find('a', left)
            if pos == -1:
                break
            every.append((i, pos))
            left = pos + 1

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

queue = deque([(start, 0)])
visited = {start}

while queue:
    (x, y), steps = queue.popleft()
    c = grid[x][y]
    if c == 'E':
        break
    if c == 'S':
        c = 'a'

    for dx, dy in moves:
        new = (x + dx, y + dy)
        if not (0 <= new[0] < len(grid) and 0 <= new[1] < len(grid[0])):
            continue
        if new in visited:
            continue
        new_c = grid[new[0]][new[1]]
        if new_c == 'E':
            new_c = 'z'
        if ord(new_c) - ord(c) <= 1:
            queue.append((new, steps + 1))
            visited.add(new)

print(steps)

minimal = steps
for init in every:
    queue = deque([(init, 0)])
    visited = {init}

    ok = False
    while queue:
        (x, y), steps = queue.popleft()
        c = grid[x][y]
        if c == 'E':
            ok = True
            break
        if c == 'S':
            c = 'a'

        for dx, dy in moves:
            new = (x + dx, y + dy)
            if not (0 <= new[0] < len(grid) and 0 <= new[1] < len(grid[0])):
                continue
            if new in visited:
                continue
            new_c = grid[new[0]][new[1]]
            if new_c == 'E':
                new_c = 'z'
            if ord(new_c) - ord(c) <= 1:
                queue.append((new, steps + 1))
                visited.add(new)

    if ok:
        minimal = min(minimal, steps)

print(minimal)
