import heapq
import os
from collections import defaultdict

from common import Vector

moves = {
    '^': Vector(-1, 0),
    '>': Vector(0, +1),
    'v': Vector(+1, 0),
    '<': Vector(0, -1),
}
turns = {
    '^': '<>',
    '>': '^v',
    'v': '<>',
    '<': '^v',
}

start = end = None
grid = []

with open(os.path.join('data', 'aoc16.txt')) as file:
    for i, line in enumerate(file):
        grid.append(line.rstrip())
        if 'S' in line:
            start = Vector(i, line.index('S'))
        if 'E' in line:
            end = Vector(i, line.index('E'))

heap = [(0, '>', start, None)]
best = {}
queue = set()
prev = defaultdict(set)
top = float('inf')

while heap:
    (cost, facing, pos, last) = entry = heapq.heappop(heap)
    node = (facing, pos)
    if cost > top:
        continue
    if cost > best.get(node, float('inf')):
        continue

    best[node] = cost
    if last is not None:
        prev[node].add(last)
    if pos == end:
        queue.add(node)
        top = cost
        continue

    new = pos + moves[facing]
    if grid[new.x][new.y] != '#':
        heapq.heappush(heap, (cost + 1, facing, new, node))
    for turn in turns[facing]:
        heapq.heappush(heap, (cost + 1000, turn, pos, node))

print(top)

tiles = {start, end}
while queue:
    node = queue.pop()
    tiles.add(node[1])
    queue |= prev[node]

print(len(tiles))
