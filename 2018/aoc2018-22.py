import heapq
import os
from functools import lru_cache


@lru_cache(maxsize=None)
def geologic(x, y):
    if x == y == 0:
        return 0
    elif X == x and Y == y:
        return 0
    elif y == 0:
        return x * 16807
    elif x == 0:
        return y * 48271
    else:
        return erosion(x - 1, y) * erosion(x, y - 1)


@lru_cache(maxsize=None)
def erosion(x, y):
    return (geologic(x, y) + depth) % 20183


moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

with open(os.path.join('data', 'aoc22.txt')) as file:
    line = next(file)
    _, _, depth = line.partition(': ')
    depth = int(depth)

    line = next(file)
    _, _, target = line.partition(': ')
    X, Y = map(int, target.split(','))


risk = 0
for y in range(Y + 1):
    for x in range(X + 1):
        risk += erosion(x, y) % 3

print(risk)

NEITHER, GEAR, TORCH = range(3)
ROCKY, WET, NARROW = range(3)

allowed = {
    ROCKY: [GEAR, TORCH],
    WET: [GEAR, NEITHER],
    NARROW: [TORCH, NEITHER],
}

h = lambda node, tool: \
    abs(node[0] - X) + abs(node[1] - Y) + 7 * (tool != TORCH)
queue = []
queue.append((h((0, 0), TORCH), 0, (0, 0, TORCH)))
already = set()
while queue:
    _, step, entry = heapq.heappop(queue)
    if entry == (X, Y, TORCH):
        print(step)
        break
    if entry in already:
        continue
    already.add(entry)

    (x, y, tool) = entry
    cur = erosion(x, y) % 3
    for alt in allowed[cur]:
        new = (x, y, alt)
        if new not in already:
            heapq.heappush(
                queue,
                (h((x, y), alt) + step + 7, step + 7, new)
            )

    for dx, dy in moves:
        (nx, ny) = (x + dx, y + dy)
        if nx < 0 or ny < 0:
            continue
        kind = erosion(nx, ny) % 3
        if tool in allowed[kind]:
            heapq.heappush(
                queue,
                (h((nx, ny), tool) + step + 1, step + 1, (nx, ny, tool))
            )
