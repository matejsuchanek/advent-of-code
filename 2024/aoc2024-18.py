import heapq
import itertools
import os

from common import Vector, looks

obstructs = []

with open(os.path.join('data', 'aoc18.txt')) as file:
    for line in file:
        x, y = map(int, line.rstrip().split(','))
        obstructs.append(Vector(x, y))

start = Vector(0, 0)
end = Vector(70, 70)

# A*
h = lambda n: abs(end.x - n.x) + abs(end.y - n.y)

heap = [(h(start), 0, start)]
already = set()
blocked = set(obstructs[:1024])

while True:
    _, steps, node = heapq.heappop(heap)
    if node == end:
        break
    if node in already:
        continue
    already.add(node)
    for move in looks:
        new = node + move
        if 0 <= new.x <= end.x \
           and 0 <= new.y <= end.y \
           and new not in blocked:
            heapq.heappush(heap, (h(new) + steps + 1, steps + 1, new))

print(steps)

for i in itertools.count(1):
    blocked = set(obstructs[:i])

    heap = [(h(start), 0, start)]
    already = set()

    found = False
    while heap:
        _, steps, node = heapq.heappop(heap)
        if node == end:
            found = True
            break
        if node in already:
            continue
        already.add(node)
        for move in looks:
            new = node + move
            if 0 <= new.x <= end.x \
               and 0 <= new.y <= end.y \
               and new not in blocked:
                heapq.heappush(heap, (h(new) + steps + 1, steps + 1, new))

    if not found:
        the_node = obstructs[i-1]
        break

print(f'{the_node.x},{the_node.y}')
